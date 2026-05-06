#!/usr/bin/env python3
"""
Ticker Reddit Script
====================

Fetches Reddit posts for a specific stock ticker from investment subreddits
via the SociaVault API. Returns top posts with top 3 comments each,
formatted for use in the Context analysis step.

Subreddits: r/stocks, r/ValueInvesting
Lookback: 90 days
Search: "$TICKER OR company_name" for coverage

Usage:
    python Scripts/ticker_reddit.py ADBE
    python Scripts/ticker_reddit.py ADBE NOW MSFT

Output:
    Data/tickers/{TICKER}/{TICKER}_social.md
"""

import os
import sys
import argparse
import requests
import time
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_utils import (
    get_writeup_directory,
    get_data_directory,
    ensure_directory_exists,
    save_json,
    get_company_name,
)

SOCIAVAULT_BASE_URL = "https://api.sociavault.com/v1"
SUBREDDITS = ["stocks", "ValueInvesting"]
LOOKBACK_DAYS = 90
MIN_SCORE = 10
MAX_POSTS = 20           # total posts in output (across all subreddits)
COMMENTS_FOR_TOP_N = 15  # fetch comments only for top N posts by score
MAX_RETRIES = 3
RETRY_DELAY = 2

BOT_KEYWORDS = [
    "i am a bot", "action was performed automatically",
    "contact the moderators", "submission statement",
]


# ---------------------------------------------------------------------------
# SociaVault client
# ---------------------------------------------------------------------------

class SociaVaultClient:
    def __init__(self, api_key):
        self.headers = {"X-API-Key": api_key, "Content-Type": "application/json"}

    def search_subreddit(self, subreddit, query):
        params = {
            "subreddit": subreddit,
            "query": query,
            "timeframe": "year",
            "sort": "relevance",
            "trim": False,
        }
        for attempt in range(MAX_RETRIES):
            try:
                r = requests.get(
                    f"{SOCIAVAULT_BASE_URL}/scrape/reddit/subreddit/search",
                    headers=self.headers,
                    params=params,
                    timeout=30,
                )
                if r.status_code == 429:
                    delay = RETRY_DELAY * (2 ** attempt)
                    print(f"  Rate limit — retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                if r.status_code == 402:
                    raise Exception("Insufficient SociaVault credits")
                if r.status_code == 401:
                    raise Exception("Invalid SOCIAVAULT_API_KEY")
                r.raise_for_status()
                return r.json()
            except requests.exceptions.Timeout:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_DELAY * (2 ** attempt))
                    continue
                raise Exception("Request timed out after retries")
        raise Exception("Request failed after all retries")

    def fetch_comments(self, thread_url):
        """Fetch top 3 comments for a post. Returns empty list on any failure."""
        try:
            time.sleep(0.5)  # light throttle between comment fetches
            r = requests.get(
                f"{SOCIAVAULT_BASE_URL}/scrape/reddit/post/comments",
                headers=self.headers,
                params={"url": thread_url, "trim": True},
                timeout=20,
            )
            if r.status_code != 200:
                return []
            raw = r.json().get("data", {}).get("comments", [])
            comments = raw if isinstance(raw, list) else list(raw.values()) if isinstance(raw, dict) else []
            comments.sort(key=lambda x: x.get("score", 0), reverse=True)
            return [c for c in comments[:3] if not is_bot(c.get("body", ""))]
        except Exception:
            return []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_bot(text):
    if not text:
        return False
    return any(k in text.lower() for k in BOT_KEYWORDS)


def extract_posts(api_response):
    raw = api_response.get("data", {}).get("posts", {})
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        return list(raw.values())
    return []


def filter_by_date(posts, days=LOOKBACK_DAYS):
    cutoff = datetime.now() - timedelta(days=days)
    kept = []
    for p in posts:
        iso = p.get("created_at_iso", "")
        if not iso:
            continue
        try:
            if iso.endswith("Z"):
                iso = iso[:-1] + "+00:00"
            if datetime.fromisoformat(iso).replace(tzinfo=None) >= cutoff:
                kept.append(p)
        except ValueError:
            continue
    return kept


def filter_by_score(posts, min_score=MIN_SCORE):
    return [p for p in posts if p.get("votes", p.get("score", 0)) >= min_score]


def deduplicate(posts):
    """Remove duplicate posts by URL/permalink."""
    seen = set()
    unique = []
    for p in posts:
        key = p.get("url") or p.get("permalink") or p.get("title", "")
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def post_url(post):
    """Return a full Reddit URL for this post."""
    url = post.get("url", "")
    if url and url.startswith("http"):
        return url
    permalink = post.get("permalink", "")
    if permalink:
        return f"https://reddit.com{permalink}"
    return ""


def format_date(iso):
    if not iso:
        return ""
    try:
        if iso.endswith("Z"):
            iso = iso[:-1] + "+00:00"
        return datetime.fromisoformat(iso).strftime("%b %d, %Y")
    except ValueError:
        return ""


def subreddit_name(post):
    sub = post.get("subreddit", {})
    if isinstance(sub, dict):
        return sub.get("name", "unknown")
    return str(sub) if sub else "unknown"


# ---------------------------------------------------------------------------
# Fetch and process
# ---------------------------------------------------------------------------

def fetch_ticker(client, ticker):
    """Fetch and filter posts for a ticker. Returns sorted post list."""
    company = get_company_name(ticker)
    query = f"${ticker} OR {ticker}"
    if company:
        query += f" OR {company}"

    print(f"  Query: {query!r}")

    all_posts = []
    for sub in SUBREDDITS:
        print(f"  Searching r/{sub}...")
        try:
            data = client.search_subreddit(sub, query)
            posts = extract_posts(data)
            print(f"    {len(posts)} raw posts")
            all_posts.extend(posts)
        except Exception as e:
            print(f"  ⚠ r/{sub} failed: {e}")

    if not all_posts:
        return []

    posts = filter_by_date(all_posts)
    print(f"  After date filter ({LOOKBACK_DAYS}d): {len(posts)}")

    posts = filter_by_score(posts)
    print(f"  After score filter (≥{MIN_SCORE}): {len(posts)}")

    posts = deduplicate(posts)
    posts.sort(key=lambda p: p.get("votes", p.get("score", 0)), reverse=True)
    posts = posts[:MAX_POSTS]

    # Fetch comments for top N posts
    print(f"  Fetching comments for top {min(COMMENTS_FOR_TOP_N, len(posts))} posts...")
    for i, p in enumerate(posts):
        if i >= COMMENTS_FOR_TOP_N:
            p["top_comments"] = []
            continue
        url = post_url(p)
        p["top_comments"] = client.fetch_comments(url) if url else []

    return posts


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def build_markdown(ticker, posts):
    lines = []
    lines.append(f"# Reddit: {ticker}")
    lines.append(
        f"*Generated: {datetime.now().strftime('%Y-%m-%d')} | "
        f"Lookback: {LOOKBACK_DAYS} days | "
        f"Sources: r/{', r/'.join(SUBREDDITS)}*"
    )
    lines.append("")

    if not posts:
        lines.append("*No posts found matching the search criteria.*")
        return "\n".join(lines)

    total_votes = sum(p.get("votes", p.get("score", 0)) for p in posts)
    total_comments = sum(p.get("num_comments", 0) for p in posts)
    lines.append(
        f"**Posts found:** {len(posts)} | "
        f"**Total upvotes:** {total_votes:,} | "
        f"**Total comments:** {total_comments:,}"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    for i, p in enumerate(posts, 1):
        title = p.get("title", "No title").strip()
        score = p.get("votes", p.get("score", 0))
        num_comments = p.get("num_comments", 0)
        sub = subreddit_name(p)
        date_str = format_date(p.get("created_at_iso", ""))
        url = post_url(p)

        lines.append(f"#### {i}. {title}")

        stats = f"**↑{score:,}** • {num_comments:,} comments • r/{sub}"
        if date_str:
            stats += f" • {date_str}"
        lines.append(stats)

        if url:
            lines.append(f"[View Thread]({url})")

        body = p.get("selftext", "").strip()
        if body:
            # Trim long bodies to keep token load reasonable
            if len(body) > 400:
                body = body[:400] + "..."
            lines.append("")
            lines.append(f"> {body}")

        comments = p.get("top_comments", [])
        if comments:
            lines.append("")
            lines.append("**Top Comments:**")
            for c in comments:
                author = c.get("author", "unknown")
                c_score = c.get("score", 0)
                body_c = " ".join(
                    line for line in c.get("body", "").strip().splitlines() if line.strip()
                )
                if len(body_c) > 300:
                    body_c = body_c[:300] + "..."
                lines.append(f"* **u/{author}** (↑{c_score}): {body_c}")

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_ticker(client, ticker):
    print(f"\n[{ticker}]")
    posts = fetch_ticker(client, ticker)

    if posts is None:
        return False  # hard failure (exception propagated)

    md = build_markdown(ticker, posts)

    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_social.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  Saved: {out_path} ({len(posts)} posts)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Reddit posts for a stock ticker")
    parser.add_argument("tickers", nargs="+", help="Ticker symbol(s)")
    args = parser.parse_args()

    api_key = os.environ.get("SOCIAVAULT_API_KEY")
    if not api_key:
        print("Error: SOCIAVAULT_API_KEY environment variable not set")
        sys.exit(1)

    client = SociaVaultClient(api_key)
    tickers = [t.upper() for t in args.tickers]

    results = {}
    for ticker in tickers:
        try:
            results[ticker] = process_ticker(client, ticker)
        except Exception as e:
            print(f"  ✗ {ticker} failed: {e}")
            results[ticker] = False

    # Verification summary
    print("\n--- Summary ---")
    failures = []
    for ticker, ok in results.items():
        status = "✓" if ok else "✗ FAILED"
        print(f"  {status}  {ticker}")
        if not ok:
            failures.append(ticker)

    if failures:
        print(f"\nFailed tickers: {', '.join(failures)}")
        sys.exit(1)

    print("\nDone.")


if __name__ == "__main__":
    main()

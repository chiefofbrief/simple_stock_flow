#!/usr/bin/env python3
"""
News Script  (Perigon + FMP, self-contained)
============================================

Ticker-focused recent news from two sources, folded into one file:
  - Perigon  (goperigon /stories/all): clustered stories with summaries + key points.
    Fetched PER MONTH (from/to filter on the story's createdAt) so coverage is spread
    across the window instead of collapsing onto the most recently-updated clusters.
  - FMP      (/news/stock): individual articles, also fetched per-month for even coverage.

Output:
    Stock Data/{T}/{T}_news.md
    Stock Data/{T}/raw/{T}_news_perigon.json
    Stock Data/{T}/raw/{T}_news_fmp.json

Usage:
    python news.py AAPL
    python news.py AAPL --months 6
"""

import sys
import os
import argparse
import time
import requests
from datetime import datetime, timedelta
from collections import Counter

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    save_json,
    get_date_range_months_back,
    make_request_with_retry,
    REQUEST_TIMEOUT,
)

FMP_BASE = "https://financialmodelingprep.com/stable"
PERIGON_URL = "https://api.goperigon.com/v1/stories/all"
FMP_API_KEY = os.getenv("FMP_API_KEY")
PERIGON_API_KEY = os.getenv("PERIGON_API_KEY")
ITEMS_PER_MONTH = 10


def month_windows(months):
    """Yield (from_date, to_date) strings for each 30-day window, newest first."""
    today = datetime.now()
    for i in range(months):
        to_d = (today - timedelta(days=i * 30)).strftime("%Y-%m-%d")
        from_d = (today - timedelta(days=(i + 1) * 30)).strftime("%Y-%m-%d")
        yield from_d, to_d


# ---------------------------------------------------------------------------
# Perigon  — clustered stories, fetched per month (from/to filter on createdAt)
# ---------------------------------------------------------------------------

def simplify_perigon_story(story):
    """Keep only what /stories/all actually provides (it is a cluster, no single URL)."""
    kps = [kp.get("point") for kp in (story.get("keyPoints") or [])[:3] if kp.get("point")]
    return {
        "date": story.get("createdAt"),           # when the story broke (not last-updated)
        "name": story.get("name"),
        "summary": story.get("summary") or story.get("shortSummary"),
        "keyPoints": kps,
        "articleCount": story.get("uniqueCount", 1),
    }


def fetch_perigon(ticker, months):
    if not PERIGON_API_KEY:
        print("  ⚠ PERIGON_API_KEY not set — skipping Perigon")
        return []
    out = []
    for i, (from_d, to_d) in enumerate(month_windows(months)):
        params = {
            # sortBy=relevance keeps stories that are actually ABOUT the company; count/date
            # surface generic multi-ticker roundups (short-interest dumps) that only mention it.
            "apiKey": PERIGON_API_KEY, "companySymbol": ticker, "sortBy": "relevance",
            "size": ITEMS_PER_MONTH, "showReprints": False, "from": from_d, "to": to_d,
        }
        data = make_request_with_retry(lambda: requests.get(PERIGON_URL, params=params, timeout=REQUEST_TIMEOUT))
        if isinstance(data, dict) and data.get("results"):
            out.extend(simplify_perigon_story(s) for s in data["results"][:ITEMS_PER_MONTH])
        elif isinstance(data, dict) and data.get("error"):
            print(f"  ⚠ Perigon [{from_d}..{to_d}]: {data['error']}")
        if i < months - 1:
            time.sleep(0.4)
    return sorted(out, key=lambda s: s.get("date") or "", reverse=True)


# ---------------------------------------------------------------------------
# FMP  — individual articles, fetched per month
# ---------------------------------------------------------------------------

def fetch_fmp(ticker, months):
    if not FMP_API_KEY:
        print("  ⚠ FMP_API_KEY not set — skipping FMP")
        return []
    articles = []
    for i, (from_d, to_d) in enumerate(month_windows(months)):
        params = {"symbols": ticker, "from": from_d, "to": to_d, "limit": ITEMS_PER_MONTH, "apikey": FMP_API_KEY}
        data = make_request_with_retry(lambda: requests.get(f"{FMP_BASE}/news/stock", params=params, timeout=REQUEST_TIMEOUT))
        if isinstance(data, list):
            articles.extend(data)
        if i < months - 1:
            time.sleep(0.4)
    return sorted(articles, key=lambda x: x.get("publishedDate", ""), reverse=True)


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def generate_markdown(ticker, stories, articles, from_date, to_date):
    md = [f"# {ticker} News", f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
          f"**Date Range:** {from_date} to {to_date}", ""]

    # --- Summary ---
    perigon_media = sum((s.get("articleCount") or 1) for s in stories)
    fmp_sources = {a.get("publisher") or a.get("site") for a in articles if (a.get("publisher") or a.get("site"))}
    md += ["## Summary", "",
           f"- **Perigon:** {len(stories)} stories (aggregating {perigon_media} articles)",
           f"- **FMP:** {len(articles)} articles from {len(fmp_sources)} sources",
           f"- **Total:** {len(stories) + len(articles)} items", ""]

    # time distribution — Perigon by createdAt month, FMP by publishedDate month
    p_month = Counter((s.get("date") or "")[:7] for s in stories if s.get("date"))
    f_month = Counter((a.get("publishedDate") or "")[:7] for a in articles if a.get("publishedDate"))
    months = sorted((set(p_month) | set(f_month)) - {""}, reverse=True)
    if months:
        md += ["### Time Distribution", "| Month | Perigon | FMP |", "|---|---|---|"]
        md += [f"| {m} | {p_month.get(m, 0)} | {f_month.get(m, 0)} |" for m in months]
        md.append("")
    md += ["---", ""]

    # --- Perigon stories ---
    md.append(f"## Perigon Stories ({len(stories)})")
    md.append("")
    for s in stories:
        date = (s.get("date") or "")[:10] or "Unknown"
        n = s.get("articleCount") or 1
        md.append(f"### {date} | {s.get('name', 'Untitled')}")
        md.append(f"*{n} articles in cluster*")
        md.append("")
        if s.get("summary"):
            md += [s["summary"], ""]
        if s.get("keyPoints"):
            md.append("**Key Points:**")
            md += [f"- {kp}" for kp in s["keyPoints"]]
            md.append("")
        md += ["---", ""]

    # --- FMP articles ---
    md.append(f"## FMP Articles ({len(articles)})")
    md.append("")
    for a in articles:
        date = (a.get("publishedDate") or "")[:10] or "Unknown"
        md.append(f"### {date} | {a.get('title', 'Untitled')}")
        md.append(f"**Source:** {a.get('publisher') or a.get('site') or 'Unknown'}")
        if a.get("url"):
            md.append(f"**URL:** {a['url']}")
        md.append("")
        if a.get("text"):
            md += [a["text"], ""]
        md += ["---", ""]

    return "\n".join(md)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process(ticker, months):
    print(f"\n=== News: {ticker} ===")
    from_date, to_date = get_date_range_months_back(months)

    stories = fetch_perigon(ticker, months)
    articles = fetch_fmp(ticker, months)

    if not stories and not articles:
        raise ValueError("no news retrieved from Perigon or FMP")

    raw_dir = get_data_directory(ticker)
    ensure_directory_exists(raw_dir)
    save_json({"date_range": {"from": from_date, "to": to_date}, "stories": stories},
              os.path.join(raw_dir, f"{ticker}_news_perigon.json"))
    save_json({"date_range": {"from": from_date, "to": to_date}, "articles": articles},
              os.path.join(raw_dir, f"{ticker}_news_fmp.json"))

    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_news.md")
    with open(out_path, "w") as f:
        f.write(generate_markdown(ticker, stories, articles, from_date, to_date))

    print(f"  Perigon: {len(stories)} stories | FMP: {len(articles)} articles")
    print(f"  ✓ Saved: {out_path}")


def main():
    ap = argparse.ArgumentParser(description="News — Perigon + FMP, ticker-focused")
    ap.add_argument("ticker")
    ap.add_argument("--months", type=int, default=3, help="Lookback in months (default 3)")
    args = ap.parse_args()

    try:
        process(args.ticker.upper(), args.months)
    except Exception as e:
        print(f"  ✗ FAILED: {e}")
        sys.exit(1)
    print("\nDone.")


if __name__ == "__main__":
    main()

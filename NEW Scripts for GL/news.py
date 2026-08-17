#!/usr/bin/env python3
"""
News Script  (Perigon + FMP, self-contained)
============================================

Ticker-focused recent news from two sources, folded into one file.

Coverage strategy — both sources are fetched PER 30-day window across the lookback
(default 3 months), so news is spread across the whole period instead of collapsing
onto whatever cluster was touched most recently.

Perigon (/stories/all) is fetched TWICE per window and merged/deduped:
  - sortBy=relevance : the stories that are actually ABOUT the company (drops the
    generic multi-ticker short-interest roundups that only mention it), but these
    time-cluster around big-news weeks.
  - sortBy=createdAt : the freshest stories in the window (recency the relevance
    sort misses).
Together they give significant + fresh. (sortBy=count is avoided — it surfaces junk.)

FMP (/news/stock) returns individual articles per window, newest first.

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
from collections import Counter, OrderedDict

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

# Per-window pull sizes — tuned so each source lands near ~50 items over 3 windows.
PERIGON_RELEVANCE = 12   # significant stories (junk-free)
PERIGON_FRESH = 8        # freshest stories (recency)
FMP_PER_WINDOW = 16


def month_windows(months):
    """Yield (from_date, to_date, label) for each rolling 30-day window, newest first."""
    today = datetime.now()
    for i in range(months):
        to_d = (today - timedelta(days=i * 30)).strftime("%Y-%m-%d")
        from_d = (today - timedelta(days=(i + 1) * 30)).strftime("%Y-%m-%d")
        yield from_d, to_d, f"{from_d} → {to_d}"


# ---------------------------------------------------------------------------
# Perigon
# ---------------------------------------------------------------------------

def simplify_perigon_story(story, window):
    kps = [kp.get("point") for kp in (story.get("keyPoints") or [])[:3] if kp.get("point")]
    return {
        "id": story.get("id"),
        "window": window,
        "date": story.get("createdAt"),           # when the story broke
        "name": story.get("name"),
        "summary": story.get("summary") or story.get("shortSummary"),
        "keyPoints": kps,
        "articleCount": story.get("uniqueCount", 1),
    }


def _perigon_call(ticker, from_d, to_d, sort_by, size):
    params = {"apiKey": PERIGON_API_KEY, "companySymbol": ticker, "sortBy": sort_by,
              "size": size, "showReprints": False, "from": from_d, "to": to_d}
    data = make_request_with_retry(lambda: requests.get(PERIGON_URL, params=params, timeout=REQUEST_TIMEOUT))
    if isinstance(data, dict) and data.get("results"):
        return data["results"]
    if isinstance(data, dict) and data.get("error"):
        print(f"  ⚠ Perigon [{sort_by} {from_d}..{to_d}]: {data['error']}")
    return []


def fetch_perigon(ticker, months):
    if not PERIGON_API_KEY:
        print("  ⚠ PERIGON_API_KEY not set — skipping Perigon")
        return []
    by_id = OrderedDict()
    for i, (from_d, to_d, label) in enumerate(month_windows(months)):
        # relevance (significant) + createdAt (fresh), merged & deduped per window
        for sort_by, size in (("relevance", PERIGON_RELEVANCE), ("createdAt", PERIGON_FRESH)):
            for s in _perigon_call(ticker, from_d, to_d, sort_by, size):
                sid = s.get("id")
                if sid and sid not in by_id:
                    by_id[sid] = simplify_perigon_story(s, label)
            time.sleep(0.3)
    return sorted(by_id.values(), key=lambda s: s.get("date") or "", reverse=True)


# ---------------------------------------------------------------------------
# FMP
# ---------------------------------------------------------------------------

def fetch_fmp(ticker, months):
    if not FMP_API_KEY:
        print("  ⚠ FMP_API_KEY not set — skipping FMP")
        return []
    articles = []
    for i, (from_d, to_d, label) in enumerate(month_windows(months)):
        params = {"symbols": ticker, "from": from_d, "to": to_d, "limit": FMP_PER_WINDOW, "apikey": FMP_API_KEY}
        data = make_request_with_retry(lambda: requests.get(f"{FMP_BASE}/news/stock", params=params, timeout=REQUEST_TIMEOUT))
        if isinstance(data, list):
            for a in data:
                a["_window"] = label
            articles.extend(data)
        if i < months - 1:
            time.sleep(0.3)
    return sorted(articles, key=lambda x: x.get("publishedDate", ""), reverse=True)


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def generate_markdown(ticker, stories, articles, months, from_date, to_date):
    md = [f"# {ticker} News", f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
          f"**Date Range:** {from_date} to {to_date}", ""]

    # --- Summary ---
    perigon_media = sum((s.get("articleCount") or 1) for s in stories)
    fmp_sources = {a.get("publisher") or a.get("site") for a in articles if (a.get("publisher") or a.get("site"))}
    md += ["## Summary", "",
           f"- **Perigon:** {len(stories)} stories (aggregating {perigon_media} articles)",
           f"- **FMP:** {len(articles)} articles from {len(fmp_sources)} sources",
           f"- **Total:** {len(stories) + len(articles)} items", ""]

    # coverage by fetch window (rolling 30-day windows, newest first)
    p_win = Counter(s.get("window") for s in stories)
    f_win = Counter(a.get("_window") for a in articles)
    md += ["### Coverage by Window (rolling 30-day)", "| Window | Perigon | FMP |", "|---|---|---|"]
    for _, _, label in month_windows(months):
        md.append(f"| {label} | {p_win.get(label, 0)} | {f_win.get(label, 0)} |")
    md += ["", "---", ""]

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
        f.write(generate_markdown(ticker, stories, articles, months, from_date, to_date))

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

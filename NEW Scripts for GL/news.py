#!/usr/bin/env python3
"""
News Script  (Perigon + FMP, self-contained)
============================================

Ticker-focused recent news from two sources, folded into one file:
  - Perigon  (goperigon /stories/all): clustered stories with summaries, key points,
    and sentiment; distributed across the lookback window.
  - FMP      (/news/stock): individual articles, fetched per-month for even coverage.

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
from collections import Counter, defaultdict

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


# ---------------------------------------------------------------------------
# Perigon
# ---------------------------------------------------------------------------

def fetch_perigon(ticker, from_date, to_date):
    if not PERIGON_API_KEY:
        print("  ⚠ PERIGON_API_KEY not set — skipping Perigon")
        return []
    params = {
        "apiKey": PERIGON_API_KEY, "companySymbol": ticker, "sortBy": "updatedAt",
        "size": 100, "showReprints": False, "from": from_date, "to": to_date,
    }
    data = make_request_with_retry(lambda: requests.get(PERIGON_URL, params=params, timeout=REQUEST_TIMEOUT))
    if not isinstance(data, dict) or "results" not in data:
        print(f"  ⚠ Perigon returned no results ({data.get('error') if isinstance(data, dict) else 'bad response'})")
        return []
    return data.get("results", [])


def simplify_perigon_story(story):
    articles = story.get("articles", []) or []
    first = articles[0] if articles else {}
    kps = [kp.get("point") for kp in (story.get("keyPoints") or [])[:3] if kp.get("point")]
    return {
        "clusterId": story.get("clusterId"),
        "name": story.get("name"),
        "summary": story.get("summary"),
        "keyPoints": kps,
        "sentiment": story.get("sentiment", {}) or {},
        "updatedAt": story.get("updatedAt"),
        "uniqueCount": story.get("uniqueCount", 1),
        "source": (first.get("source", {}) or {}).get("name") or (story.get("source", {}) or {}).get("name") or "Unknown",
        "url": first.get("url"),
    }


def distribute_stories(stories, months):
    """Even temporal coverage: up to ITEMS_PER_MONTH from each 30-day window, newest first."""
    if not stories:
        return []
    today = datetime.now()
    picked = []
    for i in range(months):
        to_d = today - timedelta(days=i * 30)
        from_d = today - timedelta(days=(i + 1) * 30)
        window = []
        for s in stories:
            ds = (s.get("updatedAt") or "").split("T")[0]
            if not ds:
                continue
            try:
                d = datetime.strptime(ds, "%Y-%m-%d")
            except ValueError:
                continue
            if from_d <= d <= to_d:
                window.append(s)
        window.sort(key=lambda x: x.get("updatedAt", ""), reverse=True)
        picked.extend(window[:ITEMS_PER_MONTH])
    return sorted(picked, key=lambda x: x.get("updatedAt", ""), reverse=True)


# ---------------------------------------------------------------------------
# FMP
# ---------------------------------------------------------------------------

def fetch_fmp(ticker, months):
    if not FMP_API_KEY:
        print("  ⚠ FMP_API_KEY not set — skipping FMP")
        return []
    today = datetime.now()
    articles = []
    for i in range(months):
        to_d = (today - timedelta(days=i * 30)).strftime("%Y-%m-%d")
        from_d = (today - timedelta(days=(i + 1) * 30)).strftime("%Y-%m-%d")
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
    perigon_media = sum((s.get("uniqueCount") or 1) for s in stories)
    fmp_sources = {a.get("publisher") or a.get("site") for a in articles if (a.get("publisher") or a.get("site"))}
    md += ["## Summary", "",
           f"- **Perigon:** {len(stories)} stories (from {perigon_media} media items)",
           f"- **FMP:** {len(articles)} articles from {len(fmp_sources)} sources",
           f"- **Total:** {len(stories) + len(articles)} items", ""]

    # time distribution
    p_month = Counter((s.get("updatedAt") or "")[:7] for s in stories if s.get("updatedAt"))
    f_month = Counter((a.get("publishedDate") or "")[:7] for a in articles if a.get("publishedDate"))
    months = sorted((set(p_month) | set(f_month)) - {""}, reverse=True)
    if months:
        md += ["### Time Distribution", "| Month | Perigon | FMP |", "|---|---|---|"]
        md += [f"| {m} | {p_month.get(m, 0)} | {f_month.get(m, 0)} |" for m in months]
        md.append("")

    # sentiment (Perigon)
    pos = sum(1 for s in stories if (s.get("sentiment") or {}).get("positive", 0) > (s.get("sentiment") or {}).get("negative", 0))
    neg = sum(1 for s in stories if (s.get("sentiment") or {}).get("negative", 0) > (s.get("sentiment") or {}).get("positive", 0))
    neu = len(stories) - pos - neg
    comps = [(s.get("sentiment") or {}).get("positive", 0) - (s.get("sentiment") or {}).get("negative", 0)
             for s in stories if s.get("sentiment")]
    avg = sum(comps) / len(comps) if comps else 0
    md += ["### Sentiment (Perigon)", "",
           f"Avg composite: {avg:+.3f}  |  positive-leaning: {pos}  |  neutral: {neu}  |  negative-leaning: {neg}",
           "", "---", ""]

    # --- Perigon stories ---
    md.append(f"## Perigon Stories ({len(stories)})")
    md.append("")
    for s in stories:
        date = (s.get("updatedAt") or "")[:10] or "Unknown"
        md.append(f"### {date} | {s.get('name', 'Untitled')}")
        if s.get("source") and s["source"] != "Unknown":
            md.append(f"**Source:** {s['source']}")
        if s.get("url"):
            md.append(f"**URL:** {s['url']}")
        sent = s.get("sentiment") or {}
        p, n, u = sent.get("positive", 0), sent.get("negative", 0), sent.get("neutral", 0)
        md.append(f"**Sentiment:** {p - n:+.2f} (pos {p:.2f}, neg {n:.2f}, neu {u:.2f})")
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

    raw_stories = fetch_perigon(ticker, from_date, to_date)
    stories = distribute_stories([simplify_perigon_story(s) for s in raw_stories], months)
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

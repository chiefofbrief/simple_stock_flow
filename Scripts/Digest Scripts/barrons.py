#!/usr/bin/env python3
"""
Barron's Markets News Fetcher (via Perigon)
===========================================

Fetches the most recent market news and analysis from Barron's via Perigon API.
Refined for high-density markdown output with clean links.

Usage:
    python Scripts/Digest Scripts/barrons.py --date 2026-04-07
"""

import os
import sys
import argparse
import requests
from datetime import datetime
from dateutil import parser as date_parser

# ============================================================================
# CONFIGURATION
# ============================================================================

PERIGON_BASE_URL = "https://api.goperigon.com/v1/all"
DEFAULT_ARTICLE_COUNT = 20

def format_date(date_str):
    try:
        dt = date_parser.parse(date_str)
        return dt.strftime('%B %d, %Y at %I:%M %p')
    except Exception:
        return date_str

def fetch_barrons(api_key, target_date=None, count=DEFAULT_ARTICLE_COUNT):
    params = {
        "apiKey": api_key,
        "source": "barrons.com",
        "showReprints": "false",
        "sortBy": "pubDate",
        "size": 100,
    }
    
    if target_date:
        params["from"] = target_date
        params["to"] = target_date
    else:
        params["from"] = (datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    try:
        r = requests.get(PERIGON_BASE_URL, params=params, timeout=15)
        r.raise_for_status()
        articles = r.json().get('articles', [])
        
        if target_date:
            articles = [a for a in articles if a.get('pubDate', '').startswith(target_date)]
        
        return articles[:count]
    except Exception as e:
        print(f"Error fetching Barron's: {e}", file=sys.stderr)
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', type=str, help="Target date in YYYY-MM-DD")
    parser.add_argument('--count', type=int, default=DEFAULT_ARTICLE_COUNT)
    args = parser.parse_args()

    api_key = os.getenv('PERIGON_API_KEY')
    if not api_key:
        print("Error: Missing PERIGON_API_KEY", file=sys.stderr)
        return

    articles = fetch_barrons(api_key, target_date=args.date, count=args.count)

    print(f"## Barron's News")
    if not articles:
        print("_No articles found for this date._")
        return

    for i, a in enumerate(articles, 1):
        title = a.get('title', 'No Title').strip()
        url = a.get('url', '#')
        pub_time = format_date(a.get('pubDate'))
        desc = a.get('description') or a.get('summary') or ""
        
        # Clean description (remove extra whitespace and truncation artifacts)
        desc = desc.replace('\n', ' ').strip()
        if len(desc) > 300: desc = desc[:297] + "..."

        print(f"### {i}. {title}")
        print(f"**{pub_time}** — [Read Full Article]({url})")
        if desc:
            print(f"\n{desc}")
        print("\n---")

if __name__ == "__main__":
    main()

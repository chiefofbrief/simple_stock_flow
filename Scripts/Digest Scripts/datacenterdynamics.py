#!/usr/bin/env python3
"""
Data Center Dynamics News Fetcher (via Perigon)
================================================

Fetches and displays the latest Data Center Dynamics news via the Perigon API.

Usage:
    python datacenterdynamics.py --markdown
    python datacenterdynamics.py --date 2026-04-14 --markdown
"""

import os
import sys
import argparse
import requests
from datetime import datetime, timedelta
from dateutil import parser as date_parser

# ============================================================================
# CONFIGURATION
# ============================================================================

PERIGON_BASE_URL = "https://api.goperigon.com/v1/all"
DEFAULT_COUNT = 20

def fetch_dcd(api_key, target_date=None, count=DEFAULT_COUNT):
    params = {
        "apiKey": api_key,
        "source": "datacenterdynamics.com",
        "showReprints": "false",
        "sortBy": "pubDate",
        "size": count,
    }

    if target_date:
        params["from"] = target_date
        params["to"] = target_date
    else:
        params["from"] = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    try:
        r = requests.get(PERIGON_BASE_URL, params=params, timeout=15)
        r.raise_for_status()
        articles = r.json().get('articles', [])
        if target_date:
            articles = [a for a in articles if a.get('pubDate', '').startswith(target_date)]
        return articles[:count]
    except Exception as e:
        print(f"Error fetching DCD: {e}", file=sys.stderr)
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', type=str, help='Target date (YYYY-MM-DD)')
    parser.add_argument('--markdown', action='store_true')
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    api_key = os.getenv('PERIGON_API_KEY')
    if not api_key:
        print("Error: Missing PERIGON_API_KEY", file=sys.stderr)
        return

    articles = fetch_dcd(api_key, target_date=args.date, count=args.count)

    if args.markdown:
        print("## Data Center Dynamics - Cloud & Infra News")
        if not articles:
            print(f"\n_No new stories for {args.date if args.date else 'the timeframe'}_")
            return
        for a in articles:
            title = a.get('title', 'No Title').strip()
            url = a.get('url', '#')
            pub_date = a.get('pubDate', '')[:10]
            desc = (a.get('description') or a.get('summary') or '').replace('\n', ' ').strip()
            if len(desc) > 500:
                desc = desc[:497] + "..."
            print(f"### {title}")
            print(f"_{pub_date}_ | [Read Online]({url})\n")
            if desc:
                print(f"{desc}\n")
            print("---\n")
    else:
        for a in articles:
            print(f"{a.get('pubDate','')[:10]} | {a.get('title','')}")

if __name__ == "__main__":
    main()

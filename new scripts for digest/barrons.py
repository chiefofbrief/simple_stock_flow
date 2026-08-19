#!/usr/bin/env python3
"""
Barron's News Fetcher (via Perigon)
====================================

Fetches the most recent Barron's articles from the last 24 hours via Perigon API.

Usage:
    python "new scripts for digest/barrons.py" [--count 50]

Required environment variables:
    PERIGON_API_KEY
"""

import os
import sys
import argparse
import requests
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from dateutil import parser as date_parser
from urllib.parse import urlparse

PERIGON_BASE_URL = "https://api.goperigon.com/v1/all"
DEFAULT_COUNT = 50
ET = ZoneInfo("America/New_York")


def format_date(date_str):
    try:
        dt = date_parser.parse(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt_et = dt.astimezone(ET)
        return dt_et.strftime('%B %d, %Y at %I:%M %p ET')
    except Exception:
        return date_str


def fetch_barrons(api_key, count=DEFAULT_COUNT):
    since = (datetime.now(timezone.utc) - timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%SZ')

    params = {
        "apiKey": api_key,
        "source": "barrons.com",
        "showReprints": "false",
        "sortBy": "pubDate",
        "from": since,
        "size": 100,
    }

    try:
        r = requests.get(PERIGON_BASE_URL, params=params, timeout=15)
        r.raise_for_status()
        articles = r.json().get('articles', [])

        # Remove market-data pages (not news articles)
        articles = [a for a in articles if '/market-data/' not in a.get('url', '')]

        # Deduplicate by URL path and description
        seen_paths = set()
        seen_descs = set()
        unique = []
        for a in articles:
            path = urlparse(a.get('url', '')).path
            desc = (a.get('description') or a.get('summary') or '').strip().lower()
            if path in seen_paths:
                continue
            if desc and desc in seen_descs:
                continue
            seen_paths.add(path)
            if desc:
                seen_descs.add(desc)
            unique.append(a)

        return unique[:count]
    except Exception as e:
        print(f"Error fetching Barron's: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    api_key = os.getenv('PERIGON_API_KEY')
    if not api_key:
        print("Error: Missing PERIGON_API_KEY", file=sys.stderr)
        return

    articles = fetch_barrons(api_key, args.count)

    print("## Barron's")
    if not articles:
        print("_No articles in the last 24 hours._")
        return

    for i, a in enumerate(articles, 1):
        title = a.get('title', 'No Title').strip()
        url = a.get('url', '#')
        pub_time = format_date(a.get('pubDate', ''))
        desc = a.get('description') or a.get('summary') or ""
        desc = desc.replace('\n', ' ').strip()
        if len(desc) > 300:
            desc = desc[:297] + "..."

        print(f"### {i}. {title}")
        print(f"**{pub_time}** — [Read Full Article]({url})")
        if desc:
            print(f"\n{desc}")
        print("\n---")


if __name__ == "__main__":
    main()

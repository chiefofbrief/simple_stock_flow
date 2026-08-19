#!/usr/bin/env python3
"""
Fierce Network Newsletter Fetcher (via Kill the Newsletter)
============================================================

Fetches Fierce Network newsletter entries from the last 24 hours
via a Kill the Newsletter Atom feed.

Usage:
    python "new scripts for digest/fierce.py" [--count 10]
"""

import sys
import argparse
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from dateutil import parser as date_parser

try:
    import feedparser
except ImportError:
    print("Error: feedparser not installed. Run: pip install feedparser", file=sys.stderr)
    sys.exit(1)

RSS_URL = "https://kill-the-newsletter.com/feeds/y10af23zprp47havfsqx.xml"
DEFAULT_COUNT = 10
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


def fetch_fierce(count=DEFAULT_COUNT):
    since = datetime.now(timezone.utc) - timedelta(hours=24)
    try:
        feed = feedparser.parse(RSS_URL)
        articles = []
        for entry in feed.entries:
            pub = entry.get('published') or entry.get('updated') or ''
            try:
                dt = date_parser.parse(pub)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if dt < since:
                    continue
            except Exception:
                pass

            # Skip confirmation/welcome emails only — keep all editorial content
            title = entry.get('title', '').lower()
            if any(k in title for k in ['confirm', 'welcome', "you're in", 'thank you']):
                continue

            articles.append({
                'title': entry.get('title', 'No Title').strip(),
                'url': entry.get('link', '#'),
                'pubDate': pub,
            })
        return articles[:count]
    except Exception as e:
        print(f"Error fetching Fierce Network: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    articles = fetch_fierce(args.count)

    print("### Fierce Network")
    if not articles:
        print("_No newsletter in the last 24 hours._")
        return

    for i, a in enumerate(articles, 1):
        title = a['title']
        url = a['url']
        pub_time = format_date(a['pubDate'])

        print(f"#### {i}. {title}")
        print(f"**{pub_time}** — [Read Full Article]({url})")
        print("\n---")


if __name__ == "__main__":
    main()

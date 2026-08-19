#!/usr/bin/env python3
"""
Power Magazine News Fetcher (via RSS)
=======================================

Fetches Power Magazine articles from the last 24 hours via RSS feed.

Usage:
    python "new scripts for digest/powermag.py" [--count 10]
"""

import html
import re
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

RSS_URL = "https://www.powermag.com/rss/"
DEFAULT_COUNT = 10
ET = ZoneInfo("America/New_York")


def strip_html(text):
    return re.sub(r'<[^>]+>', '', text).strip()


def format_date(date_str):
    try:
        dt = date_parser.parse(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt_et = dt.astimezone(ET)
        return dt_et.strftime('%B %d, %Y at %I:%M %p ET')
    except Exception:
        return date_str


def fetch_powermag(count=DEFAULT_COUNT):
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
            articles.append({
                'title': entry.get('title', 'No Title').strip(),
                'url': entry.get('link', '#'),
                'pubDate': pub,
                'description': entry.get('summary', ''),
            })
        return articles[:count]
    except Exception as e:
        print(f"Error fetching Power Magazine: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    articles = fetch_powermag(args.count)

    print("### Power Magazine")
    if not articles:
        print("_No articles in the last 24 hours._")
        return

    for i, a in enumerate(articles, 1):
        title = a['title']
        url = a['url']
        pub_time = format_date(a['pubDate'])
        desc = html.unescape(strip_html(a['description'])).replace('\n', ' ').strip()
        if len(desc) > 300:
            desc = desc[:297] + "..."

        print(f"#### {i}. {title}")
        print(f"**{pub_time}** — [Read Full Article]({url})")
        if desc:
            print(f"\n{desc}")
        print("\n---")


if __name__ == "__main__":
    main()

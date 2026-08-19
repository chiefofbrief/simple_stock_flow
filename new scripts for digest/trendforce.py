#!/usr/bin/env python3
"""
TrendForce News Fetcher (scraper)
===================================

Scrapes TrendForce news articles from the last 24 hours.

Usage:
    python "new scripts for digest/trendforce.py" [--count 20]

Dependencies:
    curl_cffi, beautifulsoup4
"""

import sys
import re
import argparse
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from bs4 import BeautifulSoup

try:
    from curl_cffi import requests
except ImportError:
    print("Error: curl_cffi not installed. Run: pip install curl_cffi", file=sys.stderr)
    sys.exit(1)

NEWS_URL = "https://www.trendforce.com/news/"
BASE_URL = "https://www.trendforce.com"
DEFAULT_COUNT = 20
ET = ZoneInfo("America/New_York")
IMPERSONATE = "safari15_5"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com',
}


def fetch_html(url):
    session = requests.Session()
    resp = session.get(url, timeout=30, impersonate=IMPERSONATE, headers=HEADERS, allow_redirects=True)
    resp.raise_for_status()
    return resp.text


def parse_articles(html, since, count):
    soup = BeautifulSoup(html, 'html.parser')
    articles = []

    for item in soup.find_all('div', class_='insight-list-item'):
        # Title and link
        a_tag = item.find('a', class_='title-link')
        if not a_tag:
            continue
        title = a_tag.get_text(strip=True)
        href = a_tag.get('href', '')
        url = href if href.startswith('http') else f"{BASE_URL}{href}"

        # Date — inside div.insight-tag, text node after the <i> icon
        date_tag = item.find('div', class_='insight-tag')
        date_str = ''
        if date_tag:
            # Extract just the date text, stripping icon text
            raw = date_tag.get_text(separator=' ', strip=True)
            match = re.search(r'\d{4}-\d{2}-\d{2}', raw)
            if match:
                date_str = match.group(0)

        # Parse and filter by date
        pub_dt = None
        if date_str:
            try:
                pub_dt = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
            except ValueError:
                pass

        if pub_dt and pub_dt < since:
            continue

        articles.append({
            'title': title,
            'url': url,
            'pubDate': date_str,
        })

        if len(articles) >= count:
            break

    return articles


def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.strftime('%B %d, %Y')
    except Exception:
        return date_str


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    since = datetime.now(timezone.utc) - timedelta(hours=24)

    try:
        html = fetch_html(NEWS_URL)
    except Exception as e:
        print(f"Error fetching TrendForce: {e}", file=sys.stderr)
        print("### TrendForce\n\n_Error fetching content._")
        return

    articles = parse_articles(html, since, args.count)

    print("### TrendForce")
    if not articles:
        print("_No articles in the last 24 hours._")
        return

    for i, a in enumerate(articles, 1):
        print(f"#### {i}. {a['title']}")
        print(f"**{format_date(a['pubDate'])}** — [Read Full Article]({a['url']})")
        print("\n---")


if __name__ == "__main__":
    main()

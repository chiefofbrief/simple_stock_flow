#!/usr/bin/env python3
"""
International Intrigue Newsletter Fetcher
==========================================

Scrapes the International Intrigue archive for all posts on a given date,
then fetches and outputs their full content as markdown.

Usage:
    python Scripts/Digest Scripts/intrigue.py [--date YYYY-MM-DD] [--markdown]

Dependencies:
    pip install curl_cffi beautifulsoup4 html2text
"""

import sys
import argparse
import time
import json
import re
import datetime
from bs4 import BeautifulSoup
import html2text

try:
    from curl_cffi import requests
except ImportError:
    print("Error: curl_cffi not installed. Run: pip install curl_cffi", file=sys.stderr)
    sys.exit(1)

ARCHIVE_URL = "https://archives.internationalintrigue.io/"
BASE_URL = "https://archives.internationalintrigue.io"
REQUEST_TIMEOUT = 30

IMPERSONATE = "safari15_5"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com',
}


def fetch_html(url, session):
    resp = session.get(url, timeout=REQUEST_TIMEOUT, impersonate=IMPERSONATE, headers=HEADERS, allow_redirects=True)
    resp.raise_for_status()
    return resp.text


def parse_archive_posts(archive_html):
    """
    Returns list of (date, url, title_snippet) from the archive page.
    Date is a datetime.date object.
    """
    soup = BeautifulSoup(archive_html, 'html.parser')
    posts = []

    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/p/' not in href or len(href) <= 3:
            continue

        text = a.get_text(separator=' ', strip=True)

        # Date is at the start of the link text: "Apr 21, 2026•..."
        date_match = re.match(r'([A-Z][a-z]{2}\s+\d{1,2},\s+\d{4})', text)
        if not date_match:
            continue

        try:
            post_date = datetime.datetime.strptime(date_match.group(1), "%b %d, %Y").date()
        except ValueError:
            continue

        full_url = href if href.startswith('http') else f"{BASE_URL}{href}"
        posts.append((post_date, full_url, text[:80]))

    # Deduplicate by URL
    seen = set()
    unique = []
    for item in posts:
        if item[1] not in seen:
            seen.add(item[1])
            unique.append(item)

    return unique


def extract_post_content(post_html):
    """Extract title, date string, and markdown body from a post page."""
    soup = BeautifulSoup(post_html, 'html.parser')

    # Title: prefer JSON-LD, fall back to h1
    title = None
    json_ld = soup.find('script', type='application/ld+json')
    if json_ld:
        try:
            data = json.loads(json_ld.string)
            title = data.get('headline')
        except Exception:
            pass
    if not title:
        h1 = soup.find('h1')
        title = h1.get_text(strip=True) if h1 else 'International Intrigue'

    # Date: JSON-LD, then <time>, then meta
    date_str = None
    if json_ld:
        try:
            data = json.loads(json_ld.string)
            date_str = data.get('datePublished')
        except Exception:
            pass
    if not date_str:
        t = soup.find('time')
        if t:
            date_str = t.get('datetime') or t.get_text(strip=True)
    if not date_str:
        m = soup.find('meta', property='article:published_time')
        if m:
            date_str = m.get('content')

    # Format date nicely if ISO
    if date_str and 'T' in date_str:
        try:
            dt = datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            date_str = dt.strftime('%B %d, %Y')
        except Exception:
            pass

    # Body: article > main > content div
    article = soup.find('article') or soup.find('main')
    if not article:
        article = soup.find('div', class_=lambda c: c and any(
            k in c.lower() for k in ['content', 'post-body', 'entry']
        ))

    if article:
        for tag in article.find_all(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.body_width = 0
        body = h.handle(str(article)).strip()
        # Remove unrendered Beehiiv personalization tokens e.g. {{first_name | Intriguer}}
        body = re.sub(r'\{\{[^}]+\}\}', '', body)
        # Collapse any double spaces or space-before-punctuation left behind
        body = re.sub(r'  +', ' ', body)
        body = re.sub(r' ([.,!?])', r'\1', body)
    else:
        body = 'Could not extract article body.'

    return title, date_str, body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help='Target date YYYY-MM-DD (default: yesterday)')
    parser.add_argument('--markdown', action='store_true', help='No-op: output is always markdown')
    args = parser.parse_args()

    try:
        session = requests.Session()

        archive_html = fetch_html(ARCHIVE_URL, session)
        posts = parse_archive_posts(archive_html)

        if args.date:
            target_date = datetime.date.fromisoformat(args.date)
            matched = [(url, snippet) for (date, url, snippet) in posts if date == target_date]
            if not matched and posts:
                matched = [(posts[0][1], posts[0][2])]
                print(f"Warning: No Intrigue posts found for {target_date}, using most recent ({posts[0][0]}).", file=sys.stderr)
        else:
            # No date specified — always fetch most recent post
            matched = [(posts[0][1], posts[0][2])] if posts else []

        if not matched:
            print("Error: No posts found in archive.", file=sys.stderr)
            return

        print("## International Intrigue")

        for i, (url, _) in enumerate(matched):
            if i > 0:
                time.sleep(1)  # polite delay between fetches
            post_html = fetch_html(url, session)
            title, date_str, body = extract_post_content(post_html)

            print(f"### {title}")
            if date_str:
                print(f"_{date_str}_")
            print()
            print(body)
            print("\n---\n")

    except Exception as e:
        print(f"Error fetching Intrigue: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

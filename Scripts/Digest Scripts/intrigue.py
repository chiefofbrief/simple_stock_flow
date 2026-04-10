#!/usr/bin/env python3
"""
International Intrigue Newsletter Fetcher
==========================================

Fetches the latest issue from the International Intrigue RSS feed.

Usage:
    python Scripts/Digest Scripts/intrigue.py
"""

import sys
import requests
import html2text
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

RSS_URL = "https://www.internationalintrigue.io/feed/"

def main():
    try:
        r = requests.get(RSS_URL, timeout=15)
        r.raise_for_status()

        root = ET.fromstring(r.text)
        ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}
        item = root.findall('.//item')[0]

        title = item.findtext('title', 'International Intrigue').strip()
        pub_date = item.findtext('pubDate', '').strip()
        content_html = item.findtext('content:encoded', namespaces=ns) or item.findtext('description') or ''

        # Strip HTML to markdown
        soup = BeautifulSoup(content_html, 'html.parser')
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.body_width = 0
        body = h.handle(str(soup)).strip()

        print("## International Intrigue")
        print(f"### {title}")
        if pub_date:
            print(f"_{pub_date}_")
        print()
        print(body)
        print("\n---\n")

    except Exception as e:
        print(f"Error fetching Intrigue: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()

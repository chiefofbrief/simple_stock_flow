"""
ServeTheHome RSS Feed Fetcher
=============================

Fetches and displays the latest server, workstation, and datacenter hardware 
reviews and news from ServeTheHome.

Usage:
    python servethehome.py                    # Last 24 hours/same day (default)
    python servethehome.py --days 0           # Today only
    python servethehome.py --markdown         # Output for Peter's Digest
"""

import sys
import argparse
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import html2text
from datetime import datetime, timedelta, timezone

try:
    from curl_cffi import requests
except ImportError:
    print("Error: curl_cffi not installed. Run: pip install curl_cffi")
    sys.exit(1)

# ============================================================================
# CONFIGURATION
# ============================================================================

RSS_FEED_URL = "https://www.servethehome.com/feed/"
DEFAULT_DAYS = 1
DEFAULT_COUNT = 15

def fetch_rss_feed(url):
    try:
        session = requests.Session()
        response = session.get(url, timeout=30, impersonate="chrome120")
        response.raise_for_status()
        return response.text
    except Exception as e:
        return None

def parse_rss_feed(xml_content):
    if not xml_content:
        return []
        
    soup = BeautifulSoup(xml_content, 'xml')
    items = soup.find_all('item')
    articles = []
    
    for item in items:
        # Standard RSS tags
        articles.append({
            'title': item.title.get_text(strip=True) if item.title else 'No Title',
            'link': item.link.get_text(strip=True) if item.link else '',
            'description': item.description.get_text(strip=True) if item.description else '',
            'pubDate': item.pubDate.get_text(strip=True) if item.pubDate else ''
        })
    return articles

def filter_articles(articles, days, target_date=None):
    if target_date:
        filtered = []
        for art in articles:
            try:
                dt = datetime.strptime(art['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
                if dt.strftime('%Y-%m-%d') == target_date:
                    filtered.append(art)
            except:
                pass
        return filtered

    # WordPress uses: "Wed, 08 Apr 2026 03:21:39 +0000"
    now = datetime.now(timezone.utc)
    cutoff = (now - timedelta(days=days)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    filtered = []
    for art in articles:
        try:
            # Parse RFC 2822
            dt = datetime.strptime(art['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
            if dt >= cutoff:
                filtered.append(art)
        except:
            filtered.append(art)
    return filtered

def to_markdown(html):
    if not html:
        return ""
    h = html2text.HTML2Text()
    h.ignore_links, h.ignore_images, h.body_width = False, True, 0
    h.ignore_tables = True
    return h.handle(html).strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=DEFAULT_DAYS)
    parser.add_argument('--date', type=str, help='Specific date (YYYY-MM-DD)')
    parser.add_argument('--markdown', action='store_true')
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    xml = fetch_rss_feed(RSS_FEED_URL)
    articles = filter_articles(parse_rss_feed(xml), args.days, args.date)
    articles = articles[:args.count]

    if args.markdown:
        print(f"## ServeTheHome - Hardware & Infra Insights")
        if not articles:
            print(f"\n_No new reviews for {args.date if args.date else 'the timeframe'}_")
            return 0
        for art in articles:
            print(f"### {art['title']}")
            print(f"_{art['pubDate']}_ | [Read Review]({art['link']})\n")
            # Truncate to 3,000 characters to save tokens
            content = to_markdown(art['description'])
            print(f"{content[:3000]}\n\n---\n")
    else:
        console = Console()
        console.print(Panel(Text("ServeTheHome", style="bold white on blue"), border_style="blue"))
        for art in articles:
            console.print(f"[bold]{art['title']}[/bold] [dim]({art['pubDate']})[/dim]")
            console.print(f"[blue]{art['link']}[/blue]\n")

if __name__ == "__main__":
    main()

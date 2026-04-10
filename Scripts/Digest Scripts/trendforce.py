"""
TrendForce Market Intelligence RSS Feed Fetcher
===============================================

Fetches and displays the latest semiconductor and energy market intelligence 
from TrendForce's RSS feeds.

Usage:
    python trendforce.py                      # Last 24 hours/same day (default)
    python trendforce.py --days 0             # Today only
    python trendforce.py --markdown           # Output for Peter's Digest
"""

import sys
import argparse
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import html2text
from datetime import datetime, timedelta

try:
    from curl_cffi import requests
except ImportError:
    print("Error: curl_cffi not installed. Run: pip install curl_cffi")
    sys.exit(1)

# ============================================================================
# CONFIGURATION
# ============================================================================

FEEDS = {
    "Semiconductors": "https://www.trendforce.com/feed/Semiconductors.html",
    "Energy": "https://www.trendforce.com/feed/Energy.html"
}
DEFAULT_DAYS = 1
DEFAULT_COUNT = 10

def fetch_rss_feed(url):
    try:
        session = requests.Session()
        # Impersonate Chrome to ensure access
        response = session.get(url, timeout=30, impersonate="chrome120")
        response.raise_for_status()
        return response.text
    except Exception as e:
        return None

def parse_rss_feed(xml_content, category):
    if not xml_content:
        return []
        
    soup = BeautifulSoup(xml_content, 'xml')
    items = soup.find_all('item')
    articles = []
    
    for item in items:
        articles.append({
            'category': category,
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
                date_clean = art['pubDate'].split(' +')[0].split(' -')[0]
                dt = datetime.strptime(date_clean, '%a, %d %b %Y %H:%M:%S')
                if dt.strftime('%Y-%m-%d') == target_date:
                    filtered.append(art)
            except:
                pass
        return filtered

    # TrendForce uses: "Tue, 07 Apr 2026 17:01:56 +0800"
    cutoff = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days)
    filtered = []
    for art in articles:
        try:
            # Strip timezone (+0800) for parsing
            date_clean = art['pubDate'].split(' +')[0].split(' -')[0]
            dt = datetime.strptime(date_clean, '%a, %d %b %Y %H:%M:%S')
            if dt >= cutoff:
                filtered.append(art)
        except:
            filtered.append(art)
    return filtered

def to_markdown(html):
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

    all_articles = []
    for name, url in FEEDS.items():
        xml = fetch_rss_feed(url)
        if xml:
            articles = parse_rss_feed(xml, name)
            all_articles.extend(filter_articles(articles, args.days, args.date))

    # Sort by date (newest first)
    all_articles.sort(key=lambda x: x['pubDate'], reverse=True)
    all_articles = all_articles[:args.count]

    if args.markdown:
        print(f"## TrendForce - Market Intelligence")
        if not all_articles:
            print(f"\n_No new reports for {args.date if args.date else 'the timeframe'}_")
            return 0
        for art in all_articles:
            print(f"### [{art['category']}] {art['title']}")
            print(f"_{art['pubDate']}_ | [Read Report]({art['link']})\n")
            # Truncate to 3,000 characters to save tokens and focus on signal
            content = to_markdown(art['description'])
            print(f"{content[:3000]}\n\n---\n")
    else:
        console = Console()
        console.print(Panel(Text("TrendForce Market Intelligence", style="bold yellow"), border_style="yellow"))
        for art in all_articles:
            console.print(f"[[bold cyan]{art['category']}[/bold cyan]] [bold]{art['title']}[/bold]")
            console.print(f"[dim]{art['pubDate']}[/dim] | [blue]{art['link']}[/blue]\n")

if __name__ == "__main__":
    main()

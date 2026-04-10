"""
Fierce Network RSS Feed Fetcher (via Kill the Newsletter)
=========================================================

Fetches and displays the latest from the Fierce Network newsletter.
This is an Atom feed converted from email.

Usage:
    python fierce.py                          # Last 24 hours/same day (default)
    python fierce.py --days 0                 # Today only
    python fierce.py --markdown               # Output for Peter's Digest
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

RSS_FEED_URL = "https://kill-the-newsletter.com/feeds/y10af23zprp47havfsqx.xml"
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

def parse_atom_feed(xml_content):
    if not xml_content:
        return []
        
    soup = BeautifulSoup(xml_content, 'xml')
    # Atom uses 'entry' instead of 'item'
    entries = soup.find_all('entry')
    articles = []
    
    for entry in entries:
        content_tag = entry.find('content')
        # Atom structure check
        articles.append({
            'title': entry.title.get_text(strip=True) if entry.title else 'No Title',
            'link': entry.link.get('href') if entry.link else '',
            'description': content_tag.get_text(strip=True) if content_tag else '',
            'pubDate': entry.published.get_text(strip=True) if entry.published else entry.updated.get_text(strip=True) if entry.updated else ''
        })
    return articles

def filter_articles(articles, days, target_date=None):
    if target_date:
        # Broader keywords to catch onboarding/boilerplate emails
        SKIP_KEYWORDS = ['thank you', 'officially in', 'confirm', 'you’re in', 'you\'re in', 'welcome', 'onboarding']
        filtered = []
        for art in articles:
            if any(key in art['title'].lower() for key in SKIP_KEYWORDS):
                continue
            try:
                # Handle 'Z' suffix for fromisoformat
                date_str = art['pubDate'].replace('Z', '+00:00')
                dt = datetime.fromisoformat(date_str)
                if dt.strftime('%Y-%m-%d') == target_date:
                    filtered.append(art)
            except:
                pass
        return filtered

    now = datetime.now(timezone.utc)
    cutoff = (now - timedelta(days=days)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    # Broader keywords to catch onboarding/boilerplate emails
    SKIP_KEYWORDS = ['thank you', 'officially in', 'confirm', 'you’re in', 'you\'re in', 'welcome', 'onboarding']
    
    filtered = []
    for art in articles:
        title_lower = art['title'].lower()
        # Skip if any keyword matches
        if any(key in title_lower for key in SKIP_KEYWORDS):
            continue
            
        try:
            date_str = art['pubDate'].replace('Z', '+00:00')
            dt = datetime.fromisoformat(date_str)
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
    h.ignore_tables = True # Strips layout tables for much cleaner output
    return h.handle(html).strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=DEFAULT_DAYS)
    parser.add_argument('--date', type=str, help='Specific date (YYYY-MM-DD)')
    parser.add_argument('--markdown', action='store_true')
    parser.add_argument('--count', type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    xml = fetch_rss_feed(RSS_FEED_URL)
    articles = filter_articles(parse_atom_feed(xml), args.days, args.date)
    articles = articles[:args.count]

    if args.markdown:
        print(f"## Fierce Network - Industry News")
        if not articles:
            print(f"\n_No new stories for {args.date if args.date else 'the timeframe'}_")
            return 0
        for art in articles:
            print(f"### {art['title']}")
            print(f"_{art['pubDate']}_ | [View Email]({art['link']})\n")
            # Truncate to 3,000 characters to save tokens
            content = to_markdown(art['description'])
            print(f"{content[:3000]}\n\n---\n")
    else:
        console = Console()
        console.print(Panel(Text("Fierce Network", style="bold red"), border_style="red"))
        for art in articles:
            console.print(f"[bold]{art['title']}[/bold] [dim]({art['pubDate']})[/dim]")
            console.print(f"[blue]{art['link']}[/blue]\n")

if __name__ == "__main__":
    main()

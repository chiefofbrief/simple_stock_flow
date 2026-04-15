"""
Fierce Network RSS Feed Fetcher (via Kill the Newsletter)
=========================================================

Fetches and displays the latest from the Fierce Network newsletter.
This is an Atom feed converted from email. Sponsor blocks, webinars,
whitepapers, events, and footer are stripped; only editorial content is kept.

Usage:
    python fierce.py                          # Last 24 hours/same day (default)
    python fierce.py --days 0                 # Today only
    python fierce.py --markdown               # Output for Peter's Digest
"""

import sys
import re
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

# Patterns that trigger entering skip mode (rest of block is sponsor content)
SKIP_BLOCK_TRIGGERS = [
    'a message from',
    'brought to you by',
]

# Headings that trigger skip mode (webinar/whitepaper promos)
SKIP_HEADING_PREFIXES = ['webinar:', 'whitepaper:']

# Individual lines to always drop regardless of skip state
SKIP_LINE_FRAGMENTS = [
    'register today', 'register now', 'download this', 'download now',
    'latest news:', 'check it out',
    'fierce telecom', 'fierce wireless', 'silverlinings',
    '## cloud\n', '##  cloud',
    'join us:', 'streamtv europe', 'sensors converge',
    'subscribeadvertise', 'subscribe\n', 'advertise\n',
    'editor in chief', 'publisher:',
    '1111b s governors', 'contact support',
    'kill the n',
    'privacy policy',
    'questex',
    'linkedin logo', 'twitter logo', 'facebook logo', 'youtube logo',
]

# Hard stop — everything from here down is footer/events
STOP_FRAGMENTS = [
    '## upcoming events',
    'unsubscribe to',
    'this email was sent to',
]

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
    entries = soup.find_all('entry')
    articles = []

    for entry in entries:
        content_tag = entry.find('content')
        articles.append({
            'title': entry.title.get_text(strip=True) if entry.title else 'No Title',
            'link': entry.link.get('href') if entry.link else '',
            'html': content_tag.get_text(strip=False) if content_tag else '',
            'pubDate': entry.published.get_text(strip=True) if entry.published else entry.updated.get_text(strip=True) if entry.updated else ''
        })
    return articles

def filter_articles(articles, days, target_date=None):
    SKIP_KEYWORDS = ['thank you', 'officially in', 'confirm', "you're in", "you're in", 'welcome', 'onboarding']

    if target_date:
        filtered = []
        for art in articles:
            if any(key in art['title'].lower() for key in SKIP_KEYWORDS):
                continue
            try:
                date_str = art['pubDate'].replace('Z', '+00:00')
                dt = datetime.fromisoformat(date_str)
                if dt.strftime('%Y-%m-%d') == target_date:
                    filtered.append(art)
            except:
                pass
        return filtered

    now = datetime.now(timezone.utc)
    cutoff = (now - timedelta(days=days)).replace(hour=0, minute=0, second=0, microsecond=0)
    filtered = []
    for art in articles:
        if any(key in art['title'].lower() for key in SKIP_KEYWORDS):
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
    h.ignore_links = True
    h.ignore_images = True
    h.body_width = 0
    h.ignore_tables = True
    return h.handle(html).strip()

def extract_editorial(markdown_text):
    """Strip sponsor blocks, webinars, events, and footer from newsletter markdown."""
    lines = markdown_text.split('\n')
    result = []
    skipping = False

    for line in lines:
        line_lower = line.lower().strip()

        # Hard stop at footer / events
        if any(stop in line_lower for stop in STOP_FRAGMENTS):
            break

        # Always drop specific junk lines
        if any(frag in line_lower for frag in SKIP_LINE_FRAGMENTS):
            continue

        # Skip standalone date fragments (e.g. "13-15" or "Apr")
        if re.match(r'^\d{1,2}-\d{1,2}$', line.strip()):
            continue
        if re.match(r'^[A-Z][a-z]{2}$', line.strip()):
            continue

        # Skip webinar/event date lines: "Tuesday, May 12, 2026 | 11am ET"
        if re.match(r'^(monday|tuesday|wednesday|thursday|friday|saturday|sunday),', line_lower):
            continue

        # Handle skip state
        if skipping:
            # Resume on editorial headings (but not webinar/whitepaper headings)
            if line.startswith('## ') and not any(line_lower.lstrip('# ').startswith(p) for p in SKIP_HEADING_PREFIXES):
                skipping = False
                result.append(line)
            # Resume on author bylines
            elif re.match(r'^By [A-Z]', line):
                skipping = False
                result.append(line)
            # Otherwise stay in skip mode
            continue

        # Enter skip mode on sponsor block triggers
        if any(trigger in line_lower for trigger in SKIP_BLOCK_TRIGGERS):
            skipping = True
            continue

        # Enter skip mode on webinar/whitepaper headings
        if line.startswith('## ') and any(line_lower.lstrip('# ').startswith(p) for p in SKIP_HEADING_PREFIXES):
            skipping = True
            continue

        result.append(line)

    # Remove orphaned headings (## heading with no body before next heading)
    cleaned = []
    for i, line in enumerate(result):
        if line.startswith('## '):
            # Look ahead for non-empty content before next heading
            has_body = False
            for j in range(i + 1, min(i + 6, len(result))):
                if result[j].strip() == '':
                    continue
                if result[j].startswith('#'):
                    break
                has_body = True
                break
            if not has_body:
                continue
        cleaned.append(line)

    # Collapse excessive blank lines
    text = '\n'.join(cleaned)
    while '\n\n\n' in text:
        text = text.replace('\n\n\n', '\n\n')

    return text.strip()

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
        print("## Fierce Network - Industry News")
        if not articles:
            print(f"\n_No new stories for {args.date if args.date else 'the timeframe'}_")
            return 0
        for art in articles:
            print(f"### {art['title']}")
            print(f"_{art['pubDate']}_ | [View Email]({art['link']})\n")
            md = to_markdown(art['html'])
            editorial = extract_editorial(md)
            print(f"{editorial}\n\n---\n")
    else:
        console = Console()
        console.print(Panel(Text("Fierce Network", style="bold red"), border_style="red"))
        for art in articles:
            console.print(f"[bold]{art['title']}[/bold] [dim]({art['pubDate']})[/dim]")
            console.print(f"[blue]{art['link']}[/blue]\n")

if __name__ == "__main__":
    main()

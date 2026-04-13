"""
Perigon News API Script
=======================

Fetches news data from Perigon API for stock analysis workflow.
Optimized to use 1 API call with local distribution across 3 months.

Usage:
    python news_perigon.py TICKER [--months N] [--markdown]

Example:
    python news_perigon.py IBM --months 3
"""

import requests
import os
import sys
import argparse
from datetime import datetime, timedelta
from collections import defaultdict

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    make_request_with_retry,
    get_data_directory,
    ensure_directory_exists,
    get_date_range_months_back,
    save_json,
    REQUEST_TIMEOUT
)

# ============================================================================
# DISTRIBUTION LOGIC
# ============================================================================

def filter_distributed_stories(stories, months=3, items_per_month=10):
    """Distribute stories evenly across the specified number of months locally.
    
    Takes a large pool of stories and selects up to `items_per_month` 
    from each 30-day window to ensure temporal distribution.
    """
    if not stories:
        return []
        
    # Sort stories descending by date
    sorted_stories = sorted(stories, key=lambda x: x.get('updatedAt', ''), reverse=True)
    
    distributed = []
    today = datetime.now()
    
    for i in range(months):
        to_date = today - timedelta(days=i*30)
        from_date = today - timedelta(days=(i+1)*30)
        
        # Find stories in this window
        window_stories = []
        for s in sorted_stories:
            date_str = s.get('updatedAt', '')
            if not date_str:
                continue
            try:
                # Perigon format: "2025-12-20T12:06:30.666272+00:00"
                # Strip microseconds/timezone for basic comparison
                base_date = date_str.split('T')[0]
                story_date = datetime.strptime(base_date, '%Y-%m-%d')
                if from_date <= story_date <= to_date:
                    window_stories.append(s)
            except (ValueError, IndexError):
                continue
                
        # Take the top N for this month
        distributed.extend(window_stories[:items_per_month])
        
    # Re-sort the final selection descending
    return sorted(distributed, key=lambda x: x.get('updatedAt', ''), reverse=True)

def group_by_month(items, date_field='updatedAt', sentiment_field='sentiment'):
    """Group items by month with sentiment aggregation"""
    monthly = defaultdict(lambda: {'count': 0, 'items': [], 'sentiment_scores': []})

    for item in items:
        date_str = item.get(date_field)
        if not date_str:
            continue

        try:
            month_key = date_str[:7]  # "2025-12"

            monthly[month_key]['count'] += 1
            monthly[month_key]['items'].append(item)

            sentiment = item.get(sentiment_field)
            if sentiment is not None and isinstance(sentiment, dict):
                score = sentiment.get('positive', 0) - sentiment.get('negative', 0)
                monthly[month_key]['sentiment_scores'].append(score)
        except (ValueError, AttributeError, KeyError):
            continue

    result = {}
    for month, data in sorted(monthly.items()):
        avg_sentiment = None
        if data['sentiment_scores']:
            avg_sentiment = sum(data['sentiment_scores']) / len(data['sentiment_scores'])

        result[month] = {
            'count': data['count'],
            'avg_sentiment': round(avg_sentiment, 3) if avg_sentiment is not None else None
        }

    return result

# ============================================================================
# PERIGON API
# ============================================================================

def fetch_perigon_stories(ticker, api_key, from_date, to_date, quiet=False):
    """Fetch news stories from Perigon API (Single Call)"""
    if not quiet:
        print(f"\nFetching Perigon stories for {ticker}...")
        print(f"  Date range: {from_date} to {to_date}")

    params = {
        'apiKey': api_key,
        'companySymbol': ticker,
        'sortBy': 'updatedAt',
        'size': 100,  # Grab up to 100 to filter locally
        'showReprints': False,
        'from': from_date,
        'to': to_date
    }

    return make_request_with_retry(
        lambda: requests.get(
            "https://api.goperigon.com/v1/stories/all",
            params=params,
            timeout=REQUEST_TIMEOUT
        )
    )

def simplify_perigon_story(story):
    """Extract simplified fields from Perigon story"""
    articles = story.get('articles', [])
    first_article = articles[0] if articles else {}

    key_points = story.get('keyPoints', [])
    simplified_key_points = [kp.get('point') for kp in key_points[:3] if kp.get('point')]

    return {
        'clusterId': story.get('clusterId'),
        'name': story.get('name'),
        'summary': story.get('summary'),
        'keyPoints': simplified_key_points,
        'sentiment': story.get('sentiment', {}),
        'updatedAt': story.get('updatedAt'),
        'source': first_article.get('source', {}).get('name') or story.get('source', {}).get('name') or "Unknown",
        'url': first_article.get('url')
    }

def save_perigon_data(data, ticker, from_date, to_date, months=3, quiet=False):
    """Save distributed Perigon data to JSON file"""
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

    if 'error' in data:
        if not quiet:
            print(f"⚠️  Warning: Perigon API error: {data['error']}")
        return None

    raw_stories = data.get('results', [])
    simplified_stories = [simplify_perigon_story(story) for story in raw_stories]

    # Distribute locally to ensure 3-month coverage
    distributed_stories = filter_distributed_stories(simplified_stories, months=months, items_per_month=10)
    
    monthly_summary = group_by_month(distributed_stories, 'updatedAt', 'sentiment')

    output = {
        'date_range': {
            'from': from_date,
            'to': to_date
        },
        'stories': distributed_stories,
        'monthly_summary': monthly_summary
    }

    filename = os.path.join(data_dir, f"{ticker}_news_perigon.json")

    if save_json(output, filename):
        if not quiet:
            print(f"✓ Saved Perigon data: {filename}")
            print(f"  - {len(distributed_stories)} distributed stories (from {len(simplified_stories)} raw results)")
            print(f"  - {len(monthly_summary)} months of data")
        return filename
    return None

def main():
    parser = argparse.ArgumentParser(description="Perigon News Data Tool")
    parser.add_argument('target', type=str, help='Target company ticker')
    parser.add_argument('--months', type=int, default=3, help='Number of months to look back')
    parser.add_argument('--markdown', action='store_true', help='Suppress output')

    args = parser.parse_args()
    ticker = args.target.upper()
    perigon_key = os.getenv('PERIGON_API_KEY')

    if not perigon_key:
        print("Error: PERIGON_API_KEY environment variable not set")
        sys.exit(1)

    markdown_mode = args.markdown
    from_date, to_date = get_date_range_months_back(args.months)

    perigon_data = fetch_perigon_stories(ticker, perigon_key, from_date, to_date, quiet=markdown_mode)
    save_perigon_data(perigon_data, ticker, from_date, to_date, months=args.months, quiet=markdown_mode)

if __name__ == "__main__":
    main()

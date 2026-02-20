"""
Perigon News API Script
=======================

Fetches news data from Perigon API for stock analysis workflow.

Usage:
    python news_perigon.py TICKER [--months N] [--markdown]

Example:
    python news_perigon.py IBM --months 3

Outputs (in data/tickers/{TICKER}/raw/ folder):
    - {TICKER}_news_perigon.json - Perigon Stories results with time-based aggregations

Output Structure:
    - date_range: Start and end dates for the data
    - stories: Full list of simplified stories (raw data preserved)
    - last_30_days: Filtered list of stories from last 30 days
    - monthly_summary: Aggregated data by month with count and average sentiment

Prerequisites:
    - PERIGON_API_KEY environment variable must be set
    - Target ticker folder will be created if it doesn't exist

Notes:
    - Default 3-month lookback from current date
    - Top 30 results from Perigon
    - Perigon handles reprints internally via showReprints=False
    - Simplified output format for easier analysis
    - Pre-computed time-based aggregations for analyst convenience
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
# TIME-BASED FILTERING & AGGREGATION
# ============================================================================

def filter_last_30_days(items, date_field='updatedAt'):
    """Filter items to only those from last 30 days

    Args:
        items: List of items to filter
        date_field: Name of the date field in each item (default: 'updatedAt')

    Returns:
        List of items from last 30 days
    """
    cutoff_date = datetime.now() - timedelta(days=30)
    filtered = []

    for item in items:
        date_str = item.get(date_field)
        if not date_str:
            continue

        try:
            # Perigon: "2025-12-20T12:06:30.666272+00:00"
            item_date = datetime.fromisoformat(date_str.replace('+00:00', ''))

            if item_date >= cutoff_date:
                filtered.append(item)
        except (ValueError, AttributeError):
            continue

    return filtered

def group_by_month(items, date_field='updatedAt', sentiment_field='sentiment'):
    """Group items by month with sentiment aggregation

    Args:
        items: List of items to group
        date_field: Name of the date field in each item (default: 'updatedAt')
        sentiment_field: Field name for sentiment score (default: 'sentiment')

    Returns:
        Dict with month keys (YYYY-MM) and aggregated data
    """
    monthly = defaultdict(lambda: {'count': 0, 'items': [], 'sentiment_scores': []})

    for item in items:
        date_str = item.get(date_field)
        if not date_str:
            continue

        try:
            month_key = date_str[:7]  # "2025-12"

            monthly[month_key]['count'] += 1
            monthly[month_key]['items'].append(item)

            # Add sentiment if field specified
            sentiment = item.get(sentiment_field)
            if sentiment is not None and isinstance(sentiment, dict):
                # Perigon sentiment is a dict with positive/negative/neutral
                # Convert to single score: positive - negative
                score = sentiment.get('positive', 0) - sentiment.get('negative', 0)
                monthly[month_key]['sentiment_scores'].append(score)
        except (ValueError, AttributeError, KeyError):
            continue

    # Calculate average sentiment for each month
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
    """Fetch news stories from Perigon API

    Args:
        ticker: Stock ticker symbol
        api_key: Perigon API key
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)
        quiet: Suppress console output

    Returns:
        dict: API response
    """
    if not quiet:
        print(f"\nFetching Perigon stories for {ticker}...")
        print(f"  Date range: {from_date} to {to_date}")

    params = {
        'apiKey': api_key,
        'companySymbol': ticker,
        'sortBy': 'updatedAt',
        'size': 30,
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
    """Extract simplified fields from Perigon story

    Args:
        story: Full story object from Perigon API

    Returns:
        dict: Simplified story with essential fields
    """
    # Extract first article details
    articles = story.get('articles', [])
    first_article = articles[0] if articles else {}

    # Extract key points (limit to top 3)
    key_points = story.get('keyPoints', [])
    simplified_key_points = [kp.get('point') for kp in key_points[:3] if kp.get('point')]

    return {
        'clusterId': story.get('clusterId'),
        'name': story.get('name'),
        'summary': story.get('summary'),
        'keyPoints': simplified_key_points,
        'companies': [
            {
                'name': c.get('name'),
                'symbols': c.get('symbols', [])
            }
            for c in story.get('companies', [])[:5]
        ],
        'people': [
            {
                'name': p.get('name')
            }
            for p in story.get('people', [])[:5]
        ],
        'topics': [t for t in story.get('topics', [])[:5]],
        'sentiment': story.get('sentiment', {}),
        'createdAt': story.get('createdAt'),
        'updatedAt': story.get('updatedAt'),
        'uniqueCount': story.get('uniqueCount'),
        'first_article': {
            'source': first_article.get('source', {}).get('name'),
            'url': first_article.get('url')
        } if first_article else None
    }

def save_perigon_data(data, ticker, from_date, to_date, quiet=False):
    """Save Perigon data to JSON file

    Args:
        data: API response data
        ticker: Stock ticker symbol
        from_date: Start date for metadata
        to_date: End date for metadata
        quiet: Suppress console output

    Returns:
        str: Filename of saved file, or None if failed
    """
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

    # Check for errors
    if 'error' in data:
        if not quiet:
            print(f"⚠️  Warning: Perigon API error: {data['error']}")
        return None

    # Extract stories and simplify
    stories = data.get('results', [])
    simplified_stories = [simplify_perigon_story(story) for story in stories]

    # Build output structure with aggregations
    last_30_days = filter_last_30_days(simplified_stories, 'updatedAt')
    monthly_summary = group_by_month(simplified_stories, 'updatedAt', 'sentiment')

    output = {
        'date_range': {
            'from': from_date,
            'to': to_date
        },
        'stories': simplified_stories,
        'last_30_days': last_30_days,
        'monthly_summary': monthly_summary
    }

    filename = os.path.join(data_dir, f"{ticker}_news_perigon.json")

    if save_json(output, filename):
        if not quiet:
            print(f"✓ Saved Perigon data: {filename}")
            print(f"  - {len(simplified_stories)} total stories")
            print(f"  - {len(last_30_days)} stories in last 30 days")
            print(f"  - {len(monthly_summary)} months of data")
        return filename
    else:
        return None

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Fetch and save news data from Perigon API

    Requires PERIGON_API_KEY environment variable.
    Outputs JSON file to data/tickers/{TICKER}/raw/ directory.
    """
    parser = argparse.ArgumentParser(description="Perigon News Data Tool")
    parser.add_argument('target', type=str, help='Target company ticker')
    parser.add_argument('--months', type=int, default=3,
                       help='Number of months to look back (default: 3)')
    parser.add_argument('--markdown', action='store_true',
                       help='Suppress output for master script aggregation')

    args = parser.parse_args()

    ticker = args.target.upper()

    # Get API key from environment
    perigon_key = os.getenv('PERIGON_API_KEY')

    if not perigon_key:
        print("Error: PERIGON_API_KEY environment variable not set")
        sys.exit(1)

    markdown_mode = args.markdown

    if not markdown_mode:
        print("\n" + "="*60)
        print("PERIGON NEWS DATA")
        print("="*60)
        print(f"Target Company: {ticker}")
        print("="*60 + "\n")

    # Get date range
    from_date, to_date = get_date_range_months_back(args.months)
    if not markdown_mode:
        print(f"Date range: {from_date} to {to_date} (~{args.months} months)")

    # Fetch from Perigon API
    perigon_data = fetch_perigon_stories(ticker, perigon_key, from_date, to_date, quiet=markdown_mode)

    # Save data
    perigon_file = save_perigon_data(perigon_data, ticker, from_date, to_date, quiet=markdown_mode)

    if perigon_file and not markdown_mode:
        print("\n" + "="*60)
        print(f"✓ Perigon data fetched successfully for {ticker}")
        print("="*60 + "\n")

if __name__ == "__main__":
    main()

"""
AlphaVantage News API Script
=============================

Fetches news sentiment data from AlphaVantage API for stock analysis workflow.

Usage:
    python news_alphavantage.py TICKER [--months N] [--markdown]

Example:
    python news_alphavantage.py IBM --months 3

Outputs (in data/stocks/{TICKER}/ folder):
    - {TICKER}_news_alphavantage.json - AlphaVantage NEWS_SENTIMENT results with time-based aggregations

Output Structure:
    - date_range: Start and end dates for the data
    - articles: Full list of simplified articles (raw data preserved)
    - last_30_days: Filtered list of articles from last 30 days
    - monthly_summary: Aggregated data by month with count and average sentiment

Prerequisites:
    - ALPHAVANTAGE_API_KEY environment variable must be set
    - Target ticker folder will be created if it doesn't exist

Notes:
    - Default 3-month lookback from current date
    - Top 30 results from AlphaVantage
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

def filter_last_30_days(items, date_field='time_published'):
    """Filter items to only those from last 30 days

    Args:
        items: List of items to filter
        date_field: Name of the date field in each item (default: 'time_published')

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
            # AlphaVantage: "20251227T133319"
            item_date = datetime.strptime(date_str, "%Y%m%dT%H%M%S")

            if item_date >= cutoff_date:
                filtered.append(item)
        except (ValueError, AttributeError):
            continue

    return filtered

def group_by_month(items, date_field='time_published', sentiment_field='overall_sentiment_score'):
    """Group items by month with sentiment aggregation

    Args:
        items: List of items to group
        date_field: Name of the date field in each item (default: 'time_published')
        sentiment_field: Field name for sentiment score (default: 'overall_sentiment_score')

    Returns:
        Dict with month keys (YYYY-MM) and aggregated data
    """
    monthly = defaultdict(lambda: {'count': 0, 'items': [], 'sentiment_scores': []})

    for item in items:
        date_str = item.get(date_field)
        if not date_str:
            continue

        try:
            month_key = f"{date_str[:4]}-{date_str[4:6]}"  # "2025-12"

            monthly[month_key]['count'] += 1
            monthly[month_key]['items'].append(item)

            # Add sentiment if field specified
            sentiment = item.get(sentiment_field)
            if sentiment is not None:
                # AlphaVantage sentiment is already a single number
                monthly[month_key]['sentiment_scores'].append(float(sentiment))
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
# ALPHAVANTAGE API
# ============================================================================

def fetch_alphavantage_news(ticker, api_key, from_date, to_date, quiet=False):
    """Fetch news sentiment from AlphaVantage API

    Args:
        ticker: Stock ticker symbol
        api_key: AlphaVantage API key
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)
        quiet: Suppress console output

    Returns:
        dict: API response
    """
    if not quiet:
        print(f"\nFetching AlphaVantage NEWS_SENTIMENT for {ticker}...")
        print(f"  Date range: {from_date} to {to_date}")

    # Convert date format to YYYYMMDDTHHMM
    from_datetime = datetime.strptime(from_date, "%Y-%m-%d")
    time_from = from_datetime.strftime("%Y%m%dT%H%M")

    params = {
        'function': 'NEWS_SENTIMENT',
        'tickers': ticker,
        'sort': 'LATEST',
        'limit': 30,
        'time_from': time_from,
        'apikey': api_key
    }

    # Build URL manually for AlphaVantage
    url = 'https://www.alphavantage.co/query'

    return make_request_with_retry(
        lambda: requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    )

def simplify_alphavantage_article(article):
    """Extract simplified fields from AlphaVantage article

    Args:
        article: Full article object from AlphaVantage API

    Returns:
        dict: Simplified article with essential fields
    """
    return {
        'title': article.get('title'),
        'summary': article.get('summary'),
        'url': article.get('url'),
        'time_published': article.get('time_published'),
        'source': article.get('source'),
        'overall_sentiment_score': article.get('overall_sentiment_score'),
        'ticker_sentiment': article.get('ticker_sentiment', [])[:5]  # Top 5 tickers
    }

def save_alphavantage_data(data, ticker, from_date, to_date, quiet=False):
    """Save AlphaVantage data to JSON file

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
            print(f"⚠️  Warning: AlphaVantage API error: {data['error']}")
        return None

    if 'Error Message' in data:
        if not quiet:
            print(f"⚠️  Warning: AlphaVantage API error: {data['Error Message']}")
        return None

    if 'Note' in data:
        if not quiet:
            print(f"⚠️  Warning: AlphaVantage rate limit: {data['Note']}")
        return None

    # Extract articles and simplify (truncate to 30 for consistency)
    articles = data.get('feed', [])[:30]
    simplified_articles = [simplify_alphavantage_article(article) for article in articles]

    # Build output structure with aggregations
    last_30_days = filter_last_30_days(simplified_articles, 'time_published')
    monthly_summary = group_by_month(simplified_articles, 'time_published', 'overall_sentiment_score')

    output = {
        'date_range': {
            'from': from_date,
            'to': to_date
        },
        'articles': simplified_articles,
        'last_30_days': last_30_days,
        'monthly_summary': monthly_summary
    }

    filename = os.path.join(data_dir, f"{ticker}_news_alphavantage.json")

    if save_json(output, filename):
        if not quiet:
            print(f"✓ Saved AlphaVantage data: {filename}")
            print(f"  - {len(simplified_articles)} total articles")
            print(f"  - {len(last_30_days)} articles in last 30 days")
            print(f"  - {len(monthly_summary)} months of data")
        return filename
    else:
        return None

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Fetch and save news data from AlphaVantage API

    Requires ALPHAVANTAGE_API_KEY environment variable.
    Outputs JSON file to data/stocks/{TICKER}/ directory.
    """
    parser = argparse.ArgumentParser(description="AlphaVantage News Data Tool")
    parser.add_argument('target', type=str, help='Target company ticker')
    parser.add_argument('--months', type=int, default=3,
                       help='Number of months to look back (default: 3)')
    parser.add_argument('--markdown', action='store_true',
                       help='Suppress output for master script aggregation')

    args = parser.parse_args()

    ticker = args.target.upper()

    # Get API key from environment
    alphavantage_key = os.getenv('ALPHAVANTAGE_API_KEY')

    if not alphavantage_key:
        print("Error: ALPHAVANTAGE_API_KEY environment variable not set")
        sys.exit(1)

    markdown_mode = args.markdown

    if not markdown_mode:
        print("\n" + "="*60)
        print("ALPHAVANTAGE NEWS DATA")
        print("="*60)
        print(f"Target Company: {ticker}")
        print("="*60 + "\n")

    # Get date range
    from_date, to_date = get_date_range_months_back(args.months)
    if not markdown_mode:
        print(f"Date range: {from_date} to {to_date} (~{args.months} months)")

    # Fetch from AlphaVantage API
    alphavantage_data = fetch_alphavantage_news(ticker, alphavantage_key, from_date, to_date, quiet=markdown_mode)

    # Save data
    av_file = save_alphavantage_data(alphavantage_data, ticker, from_date, to_date, quiet=markdown_mode)

    if av_file and not markdown_mode:
        print("\n" + "="*60)
        print(f"✓ AlphaVantage data fetched successfully for {ticker}")
        print("="*60 + "\n")

if __name__ == "__main__":
    main()

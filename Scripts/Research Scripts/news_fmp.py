"""
FMP News API Script
===================

Fetches news data from Financial Modeling Prep API for stock analysis workflow.
Uses a chunked fetching strategy to ensure 3-month coverage for high-volume stocks.

Usage:
    python news_fmp.py TICKER [--months N] [--markdown]

Example:
    python news_fmp.py IBM --months 3
"""

import requests
import os
import sys
import argparse
import time
from datetime import datetime, timedelta
from collections import defaultdict

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    make_request_with_retry,
    get_data_directory,
    ensure_directory_exists,
    save_json,
    REQUEST_TIMEOUT
)

def fetch_fmp_news_for_period(ticker, api_key, from_date, to_date, limit=10):
    """Fetch news from FMP for a specific date range"""
    params = {
        'symbols': ticker,
        'from': from_date,
        'to': to_date,
        'limit': limit,
        'apikey': api_key
    }
    
    url = "https://financialmodelingprep.com/stable/news/stock"
    
    response = make_request_with_retry(
        lambda: requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    )
    
    # Handle both list (success) and dict (error) responses
    if isinstance(response, list):
        return response
    return []

def fetch_fmp_news(ticker, api_key, months=3, items_per_month=10, quiet=False):
    """Fetch news across multiple months to ensure distributed coverage (3 calls)"""
    if not quiet:
        print(f"\nFetching FMP news for {ticker}...")
        
    all_articles = []
    today = datetime.now()
    
    for i in range(months):
        to_date_obj = today - timedelta(days=i*30)
        from_date_obj = today - timedelta(days=(i+1)*30)
        
        to_date_str = to_date_obj.strftime('%Y-%m-%d')
        from_date_str = from_date_obj.strftime('%Y-%m-%d')
        
        if not quiet:
            print(f"  Fetching window {i+1}: {from_date_str} to {to_date_str}...")
            
        articles = fetch_fmp_news_for_period(
            ticker, 
            api_key, 
            from_date_str, 
            to_date_str, 
            limit=items_per_month
        )
        
        if articles:
            all_articles.extend(articles)
            
        # Small delay between calls
        if i < months - 1:
            time.sleep(0.5)
            
    return all_articles

def save_fmp_data(articles, ticker, months, quiet=False):
    """Save FMP data to JSON file"""
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

    # Sort descending by date
    articles = sorted(articles, key=lambda x: x.get('publishedDate', ''), reverse=True)

    # Group by month for summary
    monthly_summary = defaultdict(int)
    for article in articles:
        date_str = article.get('publishedDate', '')
        if date_str and len(date_str) >= 7:
            month_key = date_str[:7]
            monthly_summary[month_key] += 1

    to_date = datetime.now().strftime('%Y-%m-%d')
    from_date = (datetime.now() - timedelta(days=months*30)).strftime('%Y-%m-%d')

    output = {
        'date_range': {
            'from': from_date,
            'to': to_date
        },
        'articles': articles,
        'monthly_summary': dict(monthly_summary)
    }

    filename = os.path.join(data_dir, f"{ticker}_news_fmp.json")

    if save_json(output, filename):
        if not quiet:
            print(f"✓ Saved FMP data: {filename}")
            print(f"  - {len(articles)} total articles distributed over {len(monthly_summary)} months")
        return filename
    return None

def main():
    parser = argparse.ArgumentParser(description="FMP News Data Tool")
    parser.add_argument('target', type=str, help='Target company ticker')
    parser.add_argument('--months', type=int, default=3, help='Number of months to look back')
    parser.add_argument('--markdown', action='store_true', help='Suppress output')

    args = parser.parse_args()
    ticker = args.target.upper()
    fmp_key = os.getenv('FMP_API_KEY')

    if not fmp_key:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

    markdown_mode = args.markdown

    articles = fetch_fmp_news(ticker, fmp_key, months=args.months, quiet=markdown_mode)
    
    if articles:
        save_fmp_data(articles, ticker, args.months, quiet=markdown_mode)
    else:
        if not markdown_mode:
            print("No articles found or API error.")

if __name__ == "__main__":
    main()

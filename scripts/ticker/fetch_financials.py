#!/usr/bin/env python3
"""
Financial Data Fetcher
======================

Fetches raw financial statement and market data from AlphaVantage.
Consolidates all responses into a single raw JSON file for downstream processing.

Endpoints Fetched:
- INCOME_STATEMENT
- BALANCE_SHEET
- CASH_FLOW
- OVERVIEW
- SHARES_OUTSTANDING

Usage:
    python fetch_financials.py TICKER
"""

import sys
import os
import time
import argparse

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    fetch_alpha_vantage,
    get_data_directory,
    ensure_directory_exists,
    save_json
)

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
API_DELAY = 12  # seconds between API calls (free tier: 5/min)

def fetch_all_raw_data(ticker):
    print(f"\nFetching all raw financial data for {ticker}...")
    
    endpoints = {
        'income': 'INCOME_STATEMENT',
        'balance': 'BALANCE_SHEET',
        'cashflow': 'CASH_FLOW',
        'overview': 'OVERVIEW',
        'shares': 'SHARES_OUTSTANDING'
    }
    
    raw_data = {
        'ticker': ticker,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    for i, (key, function) in enumerate(endpoints.items()):
        print(f"  → Fetching {key} ({function})...")
        url = f"https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={API_KEY}"
        data = fetch_alpha_vantage(url)
        
        if data:
            raw_data[key] = data
            print(f"    ✓ Success")
        else:
            print(f"    ✗ Failed")
            # We continue even if one fails, but downstream might need it
        
        # Rate limiting
        if i < len(endpoints) - 1:
            time.sleep(API_DELAY)
            
    return raw_data

def main():
    parser = argparse.ArgumentParser(description="Fetch raw financial data")
    parser.add_argument("ticker", help="Stock ticker symbol")
    args = parser.parse_args()
    
    ticker = args.ticker.upper()
    
    if not API_KEY:
        print("Error: ALPHAVANTAGE_API_KEY environment variable not set")
        sys.exit(1)
        
    raw_data = fetch_all_raw_data(ticker)
    
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    
    output_path = os.path.join(data_dir, f"{ticker}_financial_raw.json")
    if save_json(raw_data, output_path):
        print(f"\n✓ Saved raw data to: {output_path}")
    else:
        print(f"\n❌ Failed to save raw data")

if __name__ == "__main__":
    main()

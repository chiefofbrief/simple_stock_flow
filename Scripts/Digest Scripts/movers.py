#!/usr/bin/env python3
"""
Market Movers (Losers, Gainers & Actives)
=========================================

Fetches biggest stock losers, biggest gainers, and most actively traded stocks from FMP.
Refined for high-density markdown output.

Usage:
    python Scripts/Digest Scripts/movers.py --markdown
"""

import requests
import os
import sys
import argparse

# ============================================================================
# CONFIGURATION
# ============================================================================

FMP_BASE_URL = "https://financialmodelingprep.com/stable"
MIN_PRICE = 1.00  # Filter stocks below this price

# ============================================================================
# API FUNCTIONS
# ============================================================================

def fetch_fmp(endpoint, api_key):
    """Fetch data from Financial Modeling Prep API"""
    try:
        url = f"{FMP_BASE_URL}/{endpoint}?apikey={api_key}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {endpoint}: {e}", file=sys.stderr)
        return []

# ============================================================================
# DATA PROCESSING
# ============================================================================

def get_table_rows(data, count=15):
    """Filter and prepare rows for markdown table."""
    rows = []
    seen = set()
    
    filtered = [s for s in data if float(s.get('price', 0)) >= MIN_PRICE]
    
    for stock in filtered:
        symbol = stock.get('symbol', 'N/A')
        if symbol in seen: continue
        seen.add(symbol)
        
        price = float(stock.get('price', 0))
        change = float(stock.get('changesPercentage', 0))
        name = stock.get('name', 'N/A')[:40]
        
        rows.append({
            'sym': symbol,
            'price': price,
            'change': change,
            'name': name
        })
        if len(rows) >= count: break
    return rows

# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--markdown', action='store_true')
    args = parser.parse_args()

    fmp_key = os.getenv('FMP_API_KEY')
    if not fmp_key:
        print("Error: Missing FMP_API_KEY", file=sys.stderr)
        sys.exit(1)

    # Fetch data
    losers_raw = fetch_fmp("biggest-losers", fmp_key)
    gainers_raw = fetch_fmp("biggest-gainers", fmp_key)
    actives_raw = fetch_fmp("most-actives", fmp_key)

    # Process
    losers = get_table_rows(losers_raw)
    gainers = get_table_rows(gainers_raw)
    actives = get_table_rows(actives_raw)

    # Find Overlaps (Stocks in Movers + Actives)
    active_syms = {s['sym'] for s in actives}
    
    def format_row(row, active_set):
        flag = " 🔥" if row['sym'] in active_set else ""
        return f"| {row['sym']}{flag} | ${row['price']:.2f} | {row['change']:+.2f}% | {row['name']} |"

    print("## Market Movers")
    
    if losers:
        print("\n### Biggest Losers")
        print("| Symbol | Price | Change % | Company Name |")
        print("|:---|:---|:---|:---|")
        for r in losers:
            print(format_row(r, active_set=active_syms))

    if gainers:
        print("\n### Top Gainers")
        print("| Symbol | Price | Change % | Company Name |")
        print("|:---|:---|:---|:---|")
        for r in gainers:
            print(format_row(r, active_set=active_syms))

    if actives:
        print("\n### Most Actively Traded")
        print("| Symbol | Price | Change % | Company Name |")
        print("|:---|:---|:---|:---|")
        for r in actives:
            print(f"| {r['sym']} | ${r['price']:.2f} | {r['change']:+.2f}% | {r['name']} |")

    print("\n_🔥 = Also in Top 15 Most Active (High Conviction Move)_")
    print("\n---")

if __name__ == '__main__':
    main()

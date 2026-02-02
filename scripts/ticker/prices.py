#!/usr/bin/env python3
"""
Price Analysis Script
======================

Fetches historical price data and calculates technical trend statistics.
Implements a "Dual-Horizon" approach:
1. Long-Term Context (5-Year Annual)
2. Short-Term Catalyst (12-Month Monthly)

Metrics:
- 1-Month, 1-Year & 5-Year Returns
- Price vs 5-Year Average
- Volatility (CV)
- Recent Monthly Trend

Usage:
    python prices.py TICKER [TICKER ...]

Output:
    data/analysis/{TICKER}/{TICKER}_prices.json
    data/analysis/{TICKER}/{TICKER}_prices.txt
"""

import sys
import os
import argparse
from datetime import datetime

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    fetch_alpha_vantage,
    get_data_directory,
    ensure_directory_exists,
    save_json
)

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def calculate_cagr(start_val, end_val, years):
    if start_val <= 0 or end_val <= 0 or years <= 0:
        return None
    return ((end_val / start_val) ** (1 / years)) - 1

def analyze_prices(ticker):
    print(f"\nFetching Price Data for {ticker}...")
    
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={ticker}&apikey={API_KEY}"
    data = fetch_alpha_vantage(url)
    
    if not data or "Monthly Adjusted Time Series" not in data:
        print(f"❌ Failed to fetch price data for {ticker}")
        return None

    ts = data["Monthly Adjusted Time Series"]
    
    # Parse data into list of dicts
    prices = []
    for date_str, values in ts.items():
        prices.append({
            "date": date_str,
            "close": safe_float(values.get("5. adjusted close")),
            "volume": safe_float(values.get("6. volume"))
        })
    
    # Sort chronological (oldest first)
    prices.sort(key=lambda x: x["date"])
    
    if not prices:
        return None

    # Filter to last 5 years (60 months)
    prices_5yr = prices[-60:] if len(prices) > 60 else prices
    
    current = prices_5yr[-1]
    start_5yr = prices_5yr[0]
    
    # Short-term subsets
    prices_1yr = prices_5yr[-12:] if len(prices_5yr) >= 12 else prices_5yr
    start_1yr = prices_1yr[0]
    
    # 1-Month momentum
    prev_month = prices_5yr[-2] if len(prices_5yr) >= 2 else current

    # Basic Stats
    current_price = current["close"]
    high_52w = max(p["close"] for p in prices_1yr)
    low_52w = min(p["close"] for p in prices_1yr)
    avg_price_5yr = sum(p["close"] for p in prices_5yr) / len(prices_5yr)
    
    # CAGR & Returns
    years_count = (len(prices_5yr) - 1) / 12
    cagr = calculate_cagr(start_5yr["close"], current["close"], years_count)
    return_1mo = (current_price - prev_month["close"]) / prev_month["close"] if prev_month["close"] else 0
    return_1yr = (current_price - start_1yr["close"]) / start_1yr["close"] if start_1yr["close"] else 0
    return_5yr = (current_price - start_5yr["close"]) / start_5yr["close"] if start_5yr["close"] else 0
    
    # Volatility (CV)
    closes = [p["close"] for p in prices_5yr]
    mean_price = sum(closes) / len(closes)
    variance = sum((x - mean_price) ** 2 for x in closes) / len(closes)
    std_dev = variance ** 0.5
    cv = std_dev / mean_price if mean_price else 0

    analysis = {
        "ticker": ticker,
        "as_of": current["date"],
        "current_price": current_price,
        "stats": {
            "52w_high": high_52w,
            "52w_low": low_52w,
            "vs_52w_high_pct": (current_price - high_52w) / high_52w if high_52w else 0,
            "cagr_5yr": cagr,
            "return_1mo": return_1mo,
            "return_1yr": return_1yr,
            "return_5yr": return_5yr,
            "volatility_cv": cv,
            "avg_price_5yr": avg_price_5yr,
            "vs_5yr_avg_pct": (current_price - avg_price_5yr) / avg_price_5yr if avg_price_5yr else 0
        },
        "history_recent": prices_1yr,
        "history_annual": []
    }

    # Annualize history for Long-Term view
    seen_years = set()
    for p in reversed(prices_5yr):
        year = p["date"][:4]
        if year not in seen_years:
            analysis["history_annual"].append({
                "year": year,
                "date": p["date"],
                "close": p["close"]
            })
            seen_years.add(year)
    
    analysis["history_annual"].reverse()
    
    return analysis

def save_output(ticker, data):
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    
    # 1. JSON (Data)
    json_path = os.path.join(data_dir, f"{ticker}_prices.json")
    save_json(data, json_path)
    print(f"   ✓ Saved JSON to {json_path}")

    # 2. Text (Summary Table)
    txt_path = os.path.join(data_dir, f"{ticker}_prices.txt")
    
    s = data["stats"]
    from tabulate import tabulate
    
    lines = []
    lines.append(f"PRICE ANALYSIS: {ticker}")
    lines.append(f"Price: ${data['current_price']:.2f} | Date: {data['as_of']}")
    lines.append("=" * 50)
    
    # Performance Table
    perf = [
        ["1-Month Return", f"{s['return_1mo']:.1%}"],
        ["1-Year Return", f"{s['return_1yr']:.1%}"],
        ["5-Year Return", f"{s['return_5yr']:.1%}"],
        ["5-Year CAGR", f"{s['cagr_5yr']:.1%}" if s['cagr_5yr'] else "-"],
        ["vs 5-Yr Avg", f"{s['vs_5yr_avg_pct']:.1%}"],
        ["Volatility (CV)", f"{s['volatility_cv']:.2f}"],
        ["52w Range", f"${s['52w_low']:.2f} - ${s['52w_high']:.2f}"]
    ]
    lines.append(tabulate(perf, tablefmt="simple"))
    lines.append("-" * 50)
    
    # Recent Trend (12 Months)
    lines.append("\nRECENT TREND (Last 12 Months)")
    recent = []
    for p in reversed(data['history_recent']):
        recent.append([p['date'], f"${p['close']:.2f}"])
    lines.append(tabulate(recent, headers=["Month", "Close"], tablefmt="simple"))

    # Long-Term Context (5 Years)
    lines.append("\nLONG-TERM CONTEXT (5 Years)")
    hist = [[h['year'], f"${h['close']:.2f}"] for h in data['history_annual']]
    lines.append(tabulate(hist, headers=["Year", "Close"], tablefmt="simple"))

    with open(txt_path, "w") as f:
        f.write("\n".join(lines))
    print(f"   ✓ Saved Summary to {txt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tickers", nargs='+', help="Ticker symbol(s)")
    args = parser.parse_args()
    
    if not API_KEY:
        print("Error: ALPHAVANTAGE_API_KEY not set")
        sys.exit(1)
    
    for ticker in args.tickers:
        result = analyze_prices(ticker.upper())
        if result:
            save_output(ticker.upper(), result)

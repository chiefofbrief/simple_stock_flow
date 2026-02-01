#!/usr/bin/env python3
"""
Price Analysis Script
======================

Fetches historical price data and calculates technical trend statistics.
Focuses on long-term trends (5-year monthly) and recent momentum.

Metrics:
- 5-Year CAGR & Total Return
- Volatility (CV) & Drawdowns
- 52-Week High/Low stats
- Trend Slope
- Monthly/Annual Price History

Usage:
    python prices.py TICKER

Output:
    data/analysis/{TICKER}/{TICKER}_prices.json
    data/analysis/{TICKER}/{TICKER}_prices.md
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
        print("❌ Failed to fetch price data")
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
    start = prices_5yr[0]
    
    # Basic Stats
    current_price = current["close"]
    high_52w = max(p["close"] for p in prices_5yr[-12:])
    low_52w = min(p["close"] for p in prices_5yr[-12:])
    
    # CAGR
    years = (len(prices_5yr) - 1) / 12
    cagr = calculate_cagr(start["close"], current["close"], years)
    
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
            "vs_52w_high_pct": (current_price - high_52w) / high_52w,
            "cagr_5yr": cagr,
            "volatility_cv": cv,
            "total_return_5yr": (current_price - start["close"]) / start["close"]
        },
        "history_annual": []
    }

    # Annualize history (Year-End prices)
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
    print(f"✓ Saved JSON to {json_path}")

    # 2. Text (Summary Table)
    txt_path = os.path.join(data_dir, f"{ticker}_prices.txt")
    
    s = data["stats"]
    from tabulate import tabulate
    
    lines = []
    lines.append(f"PRICE SUMMARY: {ticker}")
    lines.append(f"Price: ${data['current_price']:.2f} | Date: {data['as_of']}")
    lines.append("=" * 40)
    
    stats = [
        ["5-Yr CAGR", f"{s['cagr_5yr']:.1%}" if s['cagr_5yr'] else "-"],
        ["Total Return", f"{s['total_return_5yr']:.1%}" if s['total_return_5yr'] else "-"],
        ["Volatility (CV)", f"{s['volatility_cv']:.2f}" if s['volatility_cv'] else "-"],
        ["52w Range", f"${s['52w_low']:.2f} - ${s['52w_high']:.2f}"],
        ["vs High", f"{s['vs_52w_high_pct']:.1%}" if s['vs_52w_high_pct'] else "-"]
    ]
    lines.append(tabulate(stats, tablefmt="simple"))
    lines.append("-" * 40)
    
    # History (Recent 5)
    hist = [[h['year'], f"${h['close']:.2f}"] for h in data['history_annual'][:5]]
    lines.append(tabulate(hist, headers=["Year", "Close"], tablefmt="simple"))

    with open(txt_path, "w") as f:
        f.write("\n".join(lines))
    print(f"✓ Saved Summary to {txt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker", help="Stock ticker symbol")
    args = parser.parse_args()
    
    if not API_KEY:
        print("Error: ALPHAVANTAGE_API_KEY not set")
        sys.exit(1)
        
    result = analyze_prices(args.ticker.upper())
    if result:
        save_output(args.ticker.upper(), result)

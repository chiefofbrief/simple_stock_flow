#!/usr/bin/env python3
"""
Valuation Analysis Script
=========================

Combines Price and Earnings data to calculate valuation metrics.
Strictly implements the P/E logic from the original screener.

Metrics:
- Trailing P/E
- 5-Year Average P/E
- P/E Trends (YoY, vs 5yr Avg)
- Price-EPS Correlation (5yr)

Usage:
    python valuation.py TICKER

Output:
    data/analysis/{TICKER}/{TICKER}_valuation.json
    data/analysis/{TICKER}/{TICKER}_valuation.txt
"""

import sys
import os
import argparse
import json
import subprocess
from tabulate import tabulate

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
    load_json
)

def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def calculate_avg(values):
    clean = [v for v in values if v is not None]
    return sum(clean) / len(clean) if clean else None

def calculate_cagr(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2 or clean[0] <= 0 or clean[-1] <= 0:
        return None
    years = len(clean) - 1
    return (((clean[-1] / clean[0]) ** (1 / years)) - 1)

def calculate_slope(values):
    clean = [(i, v) for i, v in enumerate(values) if v is not None]
    if len(clean) < 2: return None
    n = len(clean)
    sum_x = sum(i for i, _ in clean)
    sum_y = sum(v for _, v in clean)
    sum_xy = sum(i * v for i, v in clean)
    sum_x2 = sum(i * i for i, _ in clean)
    denominator = n * sum_x2 - sum_x * sum_x
    if denominator == 0: return None
    return (n * sum_xy - sum_x * sum_y) / denominator

def calculate_correlation(values1, values2):
    """Pearson correlation"""
    if not values1 or not values2: return None
    paired = [(v1, v2) for v1, v2 in zip(values1, values2) if v1 is not None and v2 is not None]
    if len(paired) < 2: return None
    
    n = len(paired)
    sum_x = sum(x for x, _ in paired)
    sum_y = sum(y for _, y in paired)
    sum_xy = sum(x * y for x, y in paired)
    sum_x2 = sum(x * x for x, _ in paired)
    sum_y2 = sum(y * y for _, y in paired)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
    
    if denominator == 0: return None
    return numerator / denominator

def ensure_data_exists(ticker, script_name, json_name):
    """Checks for data file, runs script if missing."""
    data_dir = get_data_directory(ticker)
    file_path = os.path.join(data_dir, json_name)
    
    if not os.path.exists(file_path):
        print(f"🔄 Missing {json_name}, running {script_name}...")
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
        subprocess.run([sys.executable, script_path, ticker], check=True)
    
    return load_json(file_path)

def analyze_valuation(ticker):
    # Ensure inputs exist
    prices_data = ensure_data_exists(ticker, "prices.py", f"{ticker}_prices.json")
    earnings_data = ensure_data_exists(ticker, "earnings.py", f"{ticker}_earnings.json")
    
    if not prices_data or not earnings_data:
        print("❌ Failed to load input data")
        return None

    # Extract Key Metrics
    current_price = prices_data.get("current_price")
    
    # Calculate TTM EPS from recent quarters
    recent_q = earnings_data.get("recent_quarters", [])
    ttm_eps = None
    if len(recent_q) >= 4:
        vals = [q.get("reported") for q in recent_q[:4]]
        if all(v is not None for v in vals):
            ttm_eps = sum(vals)

    # Calculate Trailing P/E
    trailing_pe = None
    if current_price and ttm_eps and ttm_eps > 0:
        trailing_pe = current_price / ttm_eps

    # Historical P/E (Year End Price / Annual EPS)
    # We need to match Annual History from prices with Annual Trend from earnings
    price_hist = {str(h['year']): h['close'] for h in prices_data.get("history_annual", [])}
    eps_hist = {str(a['fiscalDate'])[:4]: a['eps'] for a in earnings_data.get("annual_trend", [])}
    
    common_years = sorted(set(price_hist.keys()) & set(eps_hist.keys()))
    
    pe_history = []
    pe_values = []
    
    for year in common_years:
        p = price_hist[year]
        e = eps_hist[year]
        if p and e and e > 0:
            pe = p / e
            pe_history.append({"year": year, "pe": pe})
            pe_values.append(pe)
    
    # Stats on P/E History
    mean_5yr = calculate_avg(pe_values)
    cagr = calculate_cagr(pe_values)
    slope = calculate_slope(pe_values)
    
    # Comparisons
    vs_5yr_avg = None
    if trailing_pe and mean_5yr:
        vs_5yr_avg = (trailing_pe - mean_5yr) / mean_5yr

    # Price-EPS Correlation
    # Align the lists strictly by year for correlation
    price_vals_corr = []
    eps_vals_corr = []
    for year in common_years:
        price_vals_corr.append(price_hist[year])
        eps_vals_corr.append(eps_hist[year])
        
    correlation = calculate_correlation(price_vals_corr, eps_vals_corr)

    return {
        "ticker": ticker,
        "current_stats": {
            "price": current_price,
            "ttm_eps": ttm_eps,
            "trailing_pe": trailing_pe,
            "pe_5yr_avg": mean_5yr,
            "vs_5yr_avg_pct": vs_5yr_avg
        },
        "trends": {
            "pe_cagr_5yr": cagr,
            "pe_slope": slope,
            "price_eps_correlation": correlation
        },
        "history": pe_history
    }

def save_output(ticker, data):
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    
    # 1. JSON (Data)
    json_path = os.path.join(data_dir, f"{ticker}_valuation.json")
    save_json(data, json_path)
    print(f"✓ Saved JSON to {json_path}")
    
    # 2. Text (Summary Table)
    txt_path = os.path.join(data_dir, f"{ticker}_valuation.txt")
    
    s = data["current_stats"]
    t = data["trends"]
    
    lines = []
    lines.append(f"VALUATION SUMMARY: {ticker}")
    lines.append("=" * 40)
    
    # Main Table
    table = [
        ["Trailing P/E", f"{s['trailing_pe']:.2f}" if s['trailing_pe'] else "-"],
        ["5-Yr Avg P/E", f"{s['pe_5yr_avg']:.2f}" if s['pe_5yr_avg'] else "-"],
        ["vs 5-Yr Avg", f"{s['vs_5yr_avg_pct']:.1%}" if s['vs_5yr_avg_pct'] else "-"],
        ["P/E CAGR", f"{t['pe_cagr_5yr']:.1%}" if t['pe_cagr_5yr'] else "-"],
        ["Price-EPS Corr", f"{t['price_eps_correlation']:.2f}" if t['price_eps_correlation'] else "-"]
    ]
    lines.append(tabulate(table, tablefmt="simple"))
    lines.append("-" * 40)
    
    # History Table
    lines.append("P/E HISTORY")
    h_table = [[h['year'], f"{h['pe']:.2f}"] for h in data['history']]
    lines.append(tabulate(h_table, headers=["Year", "P/E"], tablefmt="simple"))
    
    with open(txt_path, "w") as f:
        f.write("\n".join(lines))
        
    print(f"✓ Saved Summary to {txt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker", help="Stock ticker symbol")
    args = parser.parse_args()
    
    result = analyze_valuation(args.ticker.upper())
    if result:
        save_output(args.ticker.upper(), result)

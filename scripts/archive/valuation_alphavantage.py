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
    python valuation.py TICKER [TICKER ...]

Output:
    data/tickers/{TICKER}/raw/{TICKER}_valuation.json
    data/tickers/{TICKER}/raw/{TICKER}_valuation.txt

    When multiple tickers provided:
    data/screening/Daily_Screening_YYYY-MM-DD.txt (aggregated)
"""

import sys
import os
import argparse
import json
import subprocess
from datetime import datetime
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
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ticker", script_name)
        subprocess.run([sys.executable, script_path, ticker], check=True)

    return load_json(file_path)

def analyze_valuation(ticker):
    # Ensure inputs exist
    prices_data = ensure_data_exists(ticker, "prices.py", f"{ticker}_prices.json")
    earnings_data = ensure_data_exists(ticker, "earnings.py", f"{ticker}_earnings.json")
    
    if not prices_data or not earnings_data:
        print(f"❌ Failed to load input data for {ticker}")
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
    price_vals_corr = []
    eps_vals_corr = []
    for year in common_years:
        price_vals_corr.append(price_hist[year])
        eps_vals_corr.append(eps_hist[year])

    correlation = calculate_correlation(price_vals_corr, eps_vals_corr)

    # Quarterly P/E Calculation
    quarterly_pe = []
    price_monthly = {p['date']: p['close'] for p in prices_data.get("history_recent", [])}

    for q in recent_q:
        q_date = q.get("fiscalDate")
        q_eps = q.get("reported")

        # Try to find matching price (exact match or closest month)
        q_price = price_monthly.get(q_date)

        if q_price and q_eps and q_eps > 0:
            q_pe = q_price / q_eps
            quarterly_pe.append({
                "date": q_date,
                "price": q_price,
                "eps": q_eps,
                "pe": q_pe
            })

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
        "history": pe_history,
        "quarterly_pe": quarterly_pe
    }

def save_output(ticker, data):
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

    # 1. JSON (Data)
    json_path = os.path.join(data_dir, f"{ticker}_valuation.json")
    save_json(data, json_path)
    print(f"   ✓ Saved JSON to {json_path}")

    # 2. Text (Summary Table)
    txt_path = os.path.join(data_dir, f"{ticker}_valuation.txt")

    s = data["current_stats"]
    t = data["trends"]

    lines = []
    lines.append("=" * 70)
    lines.append(f"VALUATION ANALYSIS: {ticker}")
    lines.append("=" * 70)
    curr_pe = f"{s['trailing_pe']:.2f}" if s['trailing_pe'] else "N/A"
    avg_pe = f"{s['pe_5yr_avg']:.2f}" if s['pe_5yr_avg'] else "N/A"
    lines.append(f"\nCURRENT P/E: {curr_pe} | 5-YR AVG: {avg_pe}")
    lines.append("")

    # Main Table
    lines.append("SUMMARY METRICS")
    lines.append("-" * 70)
    table = [
        ["Trailing P/E", curr_pe],
        ["5-Yr Avg P/E", avg_pe],
        ["vs 5-Yr Avg", f"{s['vs_5yr_avg_pct']:.1%}" if s['vs_5yr_avg_pct'] else "-"],
        ["P/E CAGR (5yr)", f"{t['pe_cagr_5yr']:.1%}" if t['pe_cagr_5yr'] else "-"],
        ["Price-EPS Correlation", f"{t['price_eps_correlation']:.2f}" if t['price_eps_correlation'] else "-"]
    ]
    lines.append(tabulate(table, tablefmt="simple"))
    lines.append("")

    # History Table
    lines.append("=" * 70)
    lines.append("P/E HISTORY (Annual)")
    lines.append("=" * 70)
    h_table = []
    for i, h in enumerate(data['history']):
        pe_str = f"{h['pe']:.2f}"
        if i > 0:
            prev_pe = data['history'][i-1]['pe']
            delta = h['pe'] - prev_pe
            delta_pct = (delta / prev_pe) if prev_pe else 0
            change_str = f"{delta:+.2f} ({delta_pct:+.1%})"
        else:
            change_str = "-"
        h_table.append([h['year'], pe_str, change_str])
    lines.append(tabulate(h_table, headers=["Year", "P/E", "Change"], tablefmt="simple"))
    lines.append("=" * 70)

    # Quarterly P/E Table
    if data.get('quarterly_pe'):
        lines.append("")
        lines.append("=" * 70)
        lines.append("P/E HISTORY (Quarterly)")
        lines.append("=" * 70)
        q_table = []
        for i, q in enumerate(data['quarterly_pe']):
            pe_str = f"{q['pe']:.2f}"
            price_str = f"${q['price']:.2f}"
            eps_str = f"${q['eps']:.2f}"
            if i > 0:
                prev_pe = data['quarterly_pe'][i-1]['pe']
                delta = q['pe'] - prev_pe
                delta_pct = (delta / prev_pe) if prev_pe else 0
                change_str = f"{delta:+.2f} ({delta_pct:+.1%})"
            else:
                change_str = "-"
            q_table.append([q['date'], price_str, eps_str, pe_str, change_str])
        lines.append(tabulate(q_table, headers=["Quarter", "Price", "EPS", "P/E", "Change"], tablefmt="simple"))
        lines.append("=" * 70)

    with open(txt_path, "w") as f:
        f.write("\n".join(lines))

    print(f"   ✓ Saved Summary to {txt_path}")

def create_aggregated_screening_report(tickers):
    """Create aggregated Daily_Screening report combining all ticker data

    Args:
        tickers: List of ticker symbols that were processed
    """
    today = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join("data", "screening", f"Daily_Screening_{today}.txt")

    lines = []
    lines.append("=" * 80)
    lines.append(f"                    DAILY SCREENING REPORT - {today}")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Tickers Analyzed: {', '.join(tickers)}")
    lines.append(f"Total Count: {len(tickers)}")
    lines.append("")
    lines.append("=" * 80)
    lines.append("")

    for i, ticker in enumerate(tickers, 1):
        data_dir = get_data_directory(ticker)

        # Section header
        lines.append("")
        lines.append("")
        lines.append("█" * 80)
        lines.append(f"█  TICKER {i}/{len(tickers)}: {ticker}".ljust(79) + "█")
        lines.append("█" * 80)
        lines.append("")

        # Read and append each component
        for filename in [f"{ticker}_prices.txt", f"{ticker}_earnings.txt", f"{ticker}_valuation.txt"]:
            filepath = os.path.join(data_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    content = f.read()
                    lines.append(content)
                    lines.append("")
            else:
                lines.append(f"⚠️  WARNING: {filename} not found")
                lines.append("")

        lines.append("─" * 80)
        lines.append("")

    # Write aggregated report
    ensure_directory_exists(os.path.dirname(output_path))
    with open(output_path, 'w') as f:
        f.write("\n".join(lines))

    print(f"\n📊 Aggregated Screening Report: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tickers", nargs='+', help="Ticker symbol(s)")
    args = parser.parse_args()

    # Process each ticker
    processed_tickers = []
    for ticker in args.tickers:
        print(f"\nProcessing Valuation for {ticker.upper()}...")
        result = analyze_valuation(ticker.upper())
        if result:
            save_output(ticker.upper(), result)
            processed_tickers.append(ticker.upper())

    # Create aggregated report if multiple tickers
    if len(processed_tickers) > 1:
        create_aggregated_screening_report(processed_tickers)
    elif len(processed_tickers) == 1:
        print(f"\n💡 Tip: Run with multiple tickers to generate Daily_Screening report")

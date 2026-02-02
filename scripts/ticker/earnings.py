#!/usr/bin/env python3
"""
Earnings Analysis Script
=========================

Fetches earnings history and future estimates.
Implements a "Dual-Horizon" approach:
1. Long-Term Context (5-Year Annual Trend)
2. Short-Term Catalyst (Last 4 Quarters + Next Estimate)

Metrics:
- Simple Delta (Reported vs Estimated)
- Forward Delta (Last Reported vs Next Consensus)
- Annual EPS CAGR & Stability (CV)
- Recent Surprise Momentum

Usage:
    python earnings.py TICKER [TICKER ...]

Output:
    data/analysis/{TICKER}/{TICKER}_earnings.json
    data/analysis/{TICKER}/{TICKER}_earnings.txt
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

def analyze_earnings(ticker):
    print(f"\nFetching Earnings Data for {ticker}...")
    
    # 1. Historical Earnings
    url_hist = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={API_KEY}"
    data_hist = fetch_alpha_vantage(url_hist)
    
    # 2. Estimates
    url_est = f"https://www.alphavantage.co/query?function=EARNINGS_ESTIMATES&symbol={ticker}&apikey={API_KEY}"
    data_est = fetch_alpha_vantage(url_est)

    if not data_hist:
        print(f"❌ Failed to fetch earnings history for {ticker}")
        return None

    annual = data_hist.get("annualEarnings", [])
    quarterly = data_hist.get("quarterlyEarnings", [])
    
    # Process Annual (Long-Term)
    annual_trend = []
    eps_values = []
    for a in annual[:5]: 
        val = safe_float(a.get("reportedEPS"))
        annual_trend.append({
            "fiscalDate": a.get("fiscalDateEnding"),
            "eps": val
        })
        if val is not None:
            eps_values.append(val)
    
    # Earnings Stability (CV)
    stability_cv = None
    if len(eps_values) > 1:
        mean_eps = sum(eps_values) / len(eps_values)
        if mean_eps != 0:
            variance = sum((x - mean_eps) ** 2 for x in eps_values) / len(eps_values)
            stability_cv = (variance ** 0.5) / abs(mean_eps)

    # Process Quarterly (Recent)
    recent_quarters = []
    for q in quarterly[:4]:
        rep = safe_float(q.get("reportedEPS"))
        est = safe_float(q.get("estimatedEPS"))
        delta = rep - est if (rep is not None and est is not None) else None
        
        recent_quarters.append({
            "fiscalDate": q.get("fiscalDateEnding"),
            "reported": rep,
            "estimated": est,
            "delta": delta,
            "surprise_pct": (delta / abs(est)) if (delta is not None and est) else None
        })

    # Forward Delta Calculation
    estimates = data_est.get("estimates", []) if data_est else []
    next_est = safe_float(estimates[0].get("eps_estimate_average")) if estimates else None
    last_reported = recent_quarters[0]["reported"] if recent_quarters else None
    
    forward_delta = None
    if next_est is not None and last_reported is not None:
        forward_delta = next_est - last_reported

    analysis = {
        "ticker": ticker,
        "stability_cv": stability_cv,
        "forward_metrics": {
            "next_est": next_est,
            "last_reported": last_reported,
            "forward_delta": forward_delta
        },
        "annual_trend": annual_trend,
        "recent_quarters": recent_quarters,
        "estimates": estimates[:5]
    }
    
    return analysis

def save_output(ticker, data):
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    
    # 1. JSON
    json_path = os.path.join(data_dir, f"{ticker}_earnings.json")
    save_json(data, json_path)
    print(f"   ✓ Saved JSON to {json_path}")

    # 2. Text Summary
    txt_path = os.path.join(data_dir, f"{ticker}_earnings.txt")
    from tabulate import tabulate

    lines = []
    lines.append(f"EARNINGS ANALYSIS: {ticker}")
    fm = data["forward_metrics"]
    lr_str = f"${fm['last_reported']:.2f}" if fm['last_reported'] is not None else "N/A"
    ne_str = f"${fm['next_est']:.2f}" if fm['next_est'] is not None else "N/A"
    lines.append(f"Last Reported: {lr_str} | Next Est: {ne_str}")
    delta_str = f"{fm['forward_delta']:+.2f}" if fm['forward_delta'] is not None else "N/A"
    lines.append(f"Forward Delta: {delta_str}")
    lines.append(f"Stability (CV): {data['stability_cv']:.2f}" if data['stability_cv'] is not None else "Stability (CV): N/A")
    lines.append("=" * 65)
    
    # Recent Performance
    lines.append("RECENT PERFORMANCE (Last 4 Quarters)")
    q_rows = []
    for q in data["recent_quarters"]:
        delta = f"{q['delta']:+.2f}" if q['delta'] is not None else "-"
        surp = f"{q['surprise_pct']:.1%}" if q['surprise_pct'] else "-"
        q_rows.append([q['fiscalDate'], f"${q['reported']:.2f}", f"${q['estimated']:.2f}", delta, surp])
    lines.append(tabulate(q_rows, headers=["Date", "Reported", "Estimated", "Delta", "Surp %"], tablefmt="simple"))
    lines.append("-" * 65)
    
    # Forward Estimates
    if data["estimates"]:
        lines.append("\nUPCOMING ESTIMATES")
        est_rows = [[e.get('date'), e.get('horizon'), f"${safe_float(e.get('eps_estimate_average')):.2f}"] for e in data['estimates']]
        lines.append(tabulate(est_rows, headers=["Fiscal Date", "Horizon", "Consensus"], tablefmt="simple"))

    # Long-Term Trend
    lines.append("\nLONG-TERM CONTEXT (5 Years)")
    trend = [[a['fiscalDate'], f"${a['eps']:.2f}"] for a in data['annual_trend']]
    lines.append(tabulate(trend, headers=["Fiscal Year End", "Reported EPS"], tablefmt="simple"))

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
        result = analyze_earnings(ticker.upper())
        if result:
            save_output(ticker.upper(), result)

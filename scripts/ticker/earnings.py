#!/usr/bin/env python3
"""
Earnings Analysis Script
=========================

Fetches earnings history and future estimates.
Focuses on EPS trends, surprises, and consensus estimates.

Metrics:
- Annual EPS Trend (5-year)
- Recent Quarterly Performance (Beat/Miss)
- Consensus Estimates (Next Q, Next Year)
- Revisions Momentum

Usage:
    python earnings.py TICKER

Output:
    data/analysis/{TICKER}/{TICKER}_earnings.json
    data/analysis/{TICKER}/{TICKER}_earnings.md
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
    
    # 2. Estimates (if available in your tier, otherwise this might fail gracefully)
    url_est = f"https://www.alphavantage.co/query?function=EARNINGS_ESTIMATES&symbol={ticker}&apikey={API_KEY}"
    data_est = fetch_alpha_vantage(url_est)

    if not data_hist:
        print("❌ Failed to fetch earnings history")
        return None

    annual = data_hist.get("annualEarnings", [])
    quarterly = data_hist.get("quarterlyEarnings", [])
    
    # Process Annual (Trend)
    annual_trend = []
    for a in annual[:5]: # Last 5 years
        annual_trend.append({
            "fiscalDate": a.get("fiscalDateEnding"),
            "eps": safe_float(a.get("reportedEPS"))
        })
    
    # Process Quarterly (Surprises)
    recent_quarters = []
    for q in quarterly[:4]: # Last 4 quarters
        rep = safe_float(q.get("reportedEPS"))
        est = safe_float(q.get("estimatedEPS"))
        surprise = rep - est if (rep is not None and est is not None) else None
        surprise_pct = (surprise / abs(est)) if (surprise is not None and est) else None
        
        recent_quarters.append({
            "fiscalDate": q.get("fiscalDateEnding"),
            "reported": rep,
            "estimated": est,
            "surprise": surprise,
            "surprise_pct": surprise_pct
        })

    analysis = {
        "ticker": ticker,
        "annual_trend": annual_trend,
        "recent_quarters": recent_quarters,
        "estimates": data_est.get("estimates", [])[:5] if data_est else [] # Top 5 upcoming
    }
    
    return analysis

def save_output(ticker, data):
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    
    # 1. JSON (Data)
    json_path = os.path.join(data_dir, f"{ticker}_earnings.json")
    save_json(data, json_path)
    print(f"✓ Saved JSON to {json_path}")

    # 2. Text (Summary Table)
    txt_path = os.path.join(data_dir, f"{ticker}_earnings.txt")
    from tabulate import tabulate

    lines = []
    lines.append(f"EARNINGS SUMMARY: {ticker}")
    lines.append("=" * 60)
    
    # Annual Trend
    lines.append("ANNUAL EPS (Last 5)")
    trend = [[a['fiscalDate'], f"${a['eps']:.2f}"] for a in data['annual_trend']]
    lines.append(tabulate(trend, headers=["Fiscal Date", "EPS"], tablefmt="simple"))
    lines.append("-" * 60)
    
    # Quarterly Surprises
    lines.append("QUARTERLY SURPRISES")
    q_rows = []
    for q in data["recent_quarters"]:
        surp = f"{q['surprise_pct']:.1%}" if q['surprise_pct'] else "-"
        q_rows.append([q['fiscalDate'], f"${q['reported']:.2f}", f"${q['estimated']:.2f}", surp])
    lines.append(tabulate(q_rows, headers=["Date", "Reported", "Est", "Surp %"], tablefmt="simple"))
    lines.append("-" * 60)
    
    # Estimates
    if data["estimates"]:
        lines.append("CONSENSUS ESTIMATES")
        est = [[e.get('date'), e.get('horizon'), e.get('eps_estimate_average')] for e in data['estimates']]
        lines.append(tabulate(est, headers=["Date", "Horizon", "EPS Avg"], tablefmt="simple"))

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
        
    result = analyze_earnings(args.ticker.upper())
    if result:
        save_output(args.ticker.upper(), result)

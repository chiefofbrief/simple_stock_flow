#!/usr/bin/env python3
"""
Earnings & Valuation Script
===========================

Fetches earnings history from FMP and combines it with local price data.
Uses the single /stable/earnings endpoint for both history and next estimate.

Metrics:
- P/E Trend (Current vs 1y, 3y, 5y, Avg)
- Price-Earnings Correlation (1yr)
- EPS Trend (5yr CAGR, Stability)
- Forward Delta (Next Est vs Last Actual)

Usage:
    python scripts/earnings.py TICKER [TICKER ...]
"""

import sys
import os
import argparse
import statistics
import requests
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
    load_json,
    parse_tickers_from_session_notes,
)

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 2.0

def fetch_earnings_data(ticker):
    """Fetch earnings history (includes next estimate if available)."""
    # Fetch 40 entries to ensure we have ~10 years of quarters for TTM blocks
    url = f"{FMP_BASE}/earnings?symbol={ticker}&limit=40&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  Error fetching earnings for {ticker}: HTTP {r.status_code}")
            return None
        return r.json()
    except Exception as e:
        print(f"  Exception fetching {ticker}: {e}")
        return None

def get_local_price_data(ticker):
    data_dir = get_data_directory(ticker)
    path = os.path.join(data_dir, f"{ticker}_price.json")
    return load_json(path) if os.path.exists(path) else None

def safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None

def calculate_cagr(start_val, end_val, years):
    if start_val <= 0 or end_val <= 0 or years <= 0:
        return None
    return (end_val / start_val) ** (1 / years) - 1

def analyze_ticker(ticker, history, price_data):
    if not history: return None

    # 1. Identify Next Estimate vs Last Actual
    # history is newest first
    next_est = None
    next_date = None
    last_actual = None
    actual_quarters = []

    for h in history:
        act = safe_float(h.get("epsActual"))
        est = safe_float(h.get("epsEstimated"))
        dt = h.get("date")
        
        # Next estimate is the first entry with null actual but valid estimate
        if act is None and est is not None and next_est is None:
            next_est = est
            next_date = dt
        elif act is not None:
            if last_actual is None:
                last_actual = act
            actual_quarters.append({"date": dt, "actual": act, "estimated": est})

    if not actual_quarters: return None
    
    # Sort oldest -> newest for TTM aggregation
    actual_quarters_sorted = sorted(actual_quarters, key=lambda x: x['date'])

    # 2. 5-Year Annual TTM Blocks
    annual_eps = []
    # Work backwards from the most recent quarter to build 4-quarter TTM years
    for i in range(len(actual_quarters_sorted), 3, -4):
        chunk = actual_quarters_sorted[i-4:i]
        ttm = sum(q['actual'] for q in chunk)
        annual_eps.append({"date": chunk[-1]['date'], "eps": ttm})

    # Statistics (5yr CAGR & Stability)
    # annual_eps is newest first due to building from end of sorted list
    cagr_5yr = None
    if len(annual_eps) >= 6: # Need 6 points for 5 full intervals
        cagr_5yr = calculate_cagr(annual_eps[5]['eps'], annual_eps[0]['eps'], 5)
    elif len(annual_eps) >= 2:
        cagr_5yr = calculate_cagr(annual_eps[-1]['eps'], annual_eps[0]['eps'], len(annual_eps)-1)
    
    stability_cv = None
    if len(annual_eps) > 1:
        # Calculate CV across the last 5 years of TTM blocks
        vals = [x['eps'] for x in annual_eps[:5]]
        mean_eps = statistics.mean(vals)
        if mean_eps and abs(mean_eps) > 0.001:
            stability_cv = statistics.stdev(vals) / abs(mean_eps)

    # 3. Valuation (P/E)
    ttm_eps = annual_eps[0]['eps'] if annual_eps else None
    curr_price = price_data.get("current_price")
    curr_pe = curr_price / ttm_eps if ttm_eps and ttm_eps > 0 else None

    def get_past_pe(years_ago):
        metric_key = f"vs_{years_ago}yr"
        pct_change = price_data["table_metrics"].get(metric_key)
        if pct_change is None: return None
        past_price = curr_price / (1 + pct_change)
        if len(annual_eps) > years_ago:
            past_eps = annual_eps[years_ago]['eps']
            if past_eps and past_eps > 0:
                return past_price / past_eps
        return None

    pe_1y = get_past_pe(1)
    pe_3y = get_past_pe(3)
    pe_5y = get_past_pe(5)
    pe_vals = [p for p in [curr_pe, pe_1y, pe_3y, pe_5y] if p is not None]
    pe_avg = statistics.mean(pe_vals) if pe_vals else None

    # 4. Correlation (1-Year)
    recent_trend = price_data["supplementary"].get("recent_trend", [])
    corr_1y = None
    if recent_trend:
        p_series, e_series = [], []
        for p_pt in recent_trend:
            date_str = p_pt["date"]
            valid_qs = [q for q in actual_quarters_sorted if q['date'] <= date_str]
            if len(valid_qs) >= 4:
                p_series.append(p_pt["close"])
                e_series.append(sum(q['actual'] for q in valid_qs[-4:]))
        if len(p_series) > 1:
            # Round correlation to 2 decimal places
            corr_1y = round(statistics.correlation(p_series, e_series), 2)

    return {
        "ticker": ticker,
        "as_of": price_data.get("as_of"),
        "metrics": {
            "current_pe": curr_pe,
            "pe_1y": pe_1y,
            "pe_3y": pe_3y,
            "pe_5y": pe_5y,
            "pe_avg": pe_avg,
            "vs_1y": (curr_pe - pe_1y)/pe_1y if curr_pe and pe_1y else None,
            "vs_3y": (curr_pe - pe_3y)/pe_3y if curr_pe and pe_3y else None,
            "vs_5y": (curr_pe - pe_5y)/pe_5y if curr_pe and pe_5y else None,
            "vs_avg": (curr_pe - pe_avg)/pe_avg if curr_pe and pe_avg else None,
            "corr_1y": corr_1y,
            "eps_cagr": cagr_5yr,
            "stability": stability_cv,
            "fwd_delta": next_est - last_actual if next_est is not None and last_actual is not None else None,
            "next_est": next_est,
            "next_date": next_date
        },
        "history": {
            "annual_eps": annual_eps[:10], # Show last 10 TTM blocks
            "quarterly": actual_quarters[:4] # Already newest first
        }
    }

def format_pe(val): return f"{val:.1f}x" if val is not None else "-"
def format_pct(val, dec=0): return f"{val:+.{dec}%}" if val is not None else "-"
def format_curr(val): return f"${val:.2f}" if val is not None else "-"

def format_summary_table(results):
    headers = ["Ticker", "Cur P/E", "vs1Y", "vs3Y", "vs5Y", "vsAvg", "1yCorr", "||", "EPS CAGR", "Stability", "Fwd Delta"]
    rows = []
    for r in results:
        m = r["metrics"]
        rows.append([
            r["ticker"], format_pe(m["current_pe"]), format_pct(m["vs_1y"]), format_pct(m["vs_3y"]),
            format_pct(m["vs_5y"]), format_pct(m["vs_avg"]), f"{m['corr_1y']:.2f}" if m['corr_1y'] is not None else "-",
            "||", format_pct(m["eps_cagr"], 1), f"{m['stability']:.2f}" if m['stability'] is not None else "-",
            format_curr(m["fwd_delta"])
        ])
    col_w = [max(len(str(row[i])) for row in [headers] + rows) for i in range(len(headers))]
    fmt = lambda row: " | ".join(str(row[i]).rjust(col_w[i]) for i in range(len(headers)))
    return "\n".join([fmt(headers), "-+-".join("-" * w for w in col_w)] + [fmt(r) for r in rows])

def format_detailed(r):
    m, h = r["metrics"], r["history"]
    lines = ["=" * 80, f"TICKER: {r['ticker']} | Price Date: {r['as_of']}", "=" * 80, ""]
    lines.extend(["1. VALUATION TREND (P/E History)", "   Metric   | Current | 1Yr Ago | 3Yr Ago | 5Yr Ago | Avg", "   ---------+---------+---------+---------+---------+-------"])
    lines.append(f"   P/E Ratio| {format_pe(m['current_pe']):>7} | {format_pe(m['pe_1y']):>7} | {format_pe(m['pe_3y']):>7} | {format_pe(m['pe_5y']):>7} | {format_pe(m['pe_avg']):>5}")
    lines.append(f"   vs Cur   |       - | {format_pct(m['vs_1y']):>7} | {format_pct(m['vs_3y']):>7} | {format_pct(m['vs_5y']):>7} | {format_pct(m['vs_avg']):>5}")
    lines.extend(["", "2. RELATIONSHIP & GROWTH", f"   > 1-Year Correlation: {m['corr_1y']:.2f}" if m['corr_1y'] is not None else "   > 1-Year Correlation: N/A", f"   > 5-Year EPS CAGR:    {format_pct(m['eps_cagr'], 1)}", f"   > Earnings Stability: {m['stability']:.2f}" if m['stability'] is not None else "   > Earnings Stability: N/A", ""])
    lines.extend(["3. ESTIMATES vs ACTUALS (Catalyst Check)", "   Quarter     | Estimate | Reported | Surprise | Delta", "   ------------+----------+----------+----------+-------"])
    if m['next_est'] is not None:
        lines.append(f"   Next (Est)  | {format_curr(m['next_est']):>8} |        - |        - | (Due: {m['next_date']})")
    else:
        lines.append(f"   Next (Est)  |      N/A |        - |        - | (No estimate found)")
    
    for q in h["quarterly"]:
        e, a = q['estimated'], q['actual']
        s = (a - e)/abs(e) if e and a is not None else 0
        lines.append(f"   {q['date']:11} | {format_curr(e):>8} | {format_curr(a):>8} | {format_pct(s, 1):>8} | {format_curr(a-e if e else 0)}")
    lines.append(f"\n   > Forward Delta: {format_curr(m['fwd_delta'])} (Next Est vs Last Actual)")
    lines.extend(["", "4. ANNUAL TREND (TTM Blocks - Last 5 Years)", "   TTM End Date| EPS      | Growth", "   ------------+----------+-------"])
    for i, a in enumerate(h["annual_eps"]):
        prev_eps = h["annual_eps"][i+1]['eps'] if i < len(h["annual_eps"])-1 else None
        g = "-"
        if prev_eps is not None and abs(prev_eps) > 0.001:
            g = format_pct((a['eps'] - prev_eps)/abs(prev_eps), 1)
        lines.append(f"   {a['date']:11} | {format_curr(a['eps']):>8} | {g:>6}")
    return "\n".join(lines)

def get_legend():
    return "\nLEGEND:\nvsXYr: % difference between Current P/E and P/E X years ago.\n1yCorr: Correlation (0-1) between Price and Earnings over last 12 months.\nStability: CV of Annual EPS (Lower = Smoother growth).\nFwd Delta: Next Quarter Estimate minus Last Reported EPS. (+ = Growth exp).\n"

def main():
    parser = argparse.ArgumentParser(description="Earnings & Valuation Analysis")
    parser.add_argument("tickers", nargs="*", help="Ticker symbol(s)")
    parser.add_argument(
        "--category",
        nargs="+",
        choices=["losers", "ai", "other"],
        help="Read tickers from SESSION_NOTES by category",
    )
    parser.add_argument("--all", action="store_true", help="All categories from SESSION_NOTES")
    args = parser.parse_args()

    # Resolve ticker list
    tickers = []
    if args.all:
        tickers = parse_tickers_from_session_notes(["losers", "ai", "other"])
    elif args.category:
        tickers = parse_tickers_from_session_notes(args.category)

    if args.tickers:
        tickers.extend(t.upper() for t in args.tickers)

    if not tickers:
        print("Error: no tickers specified. Use positional args, --category, or --all")
        sys.exit(1)

    # Deduplicate
    seen = set()
    unique_tickers = []
    for t in tickers:
        if t not in seen:
            seen.add(t)
            unique_tickers.append(t)
    tickers = unique_tickers

    print(f"Processing {len(tickers)} tickers: {', '.join(tickers)}\n")

    results = []
    for i, ticker in enumerate(tickers):
        if i > 0:
            time.sleep(API_CALL_DELAY)
        
        price_data = get_local_price_data(ticker)
        if not price_data:
            print(f"Skipping {ticker}: No local price data found (run price.py first)")
            continue
            
        print(f"Fetching {ticker}...")
        history = fetch_earnings_data(ticker)
        res = analyze_ticker(ticker, history, price_data)
        if res:
            results.append(res)
            save_json(res, os.path.join(get_data_directory(ticker), f"{ticker}_earnings.json"))

    if not results: return
    today = datetime.now().strftime("%Y-%m-%d")
    summary = format_summary_table(results)
    content = f"EARNINGS & VALUATION — {today}\n\n{summary}\n\n{get_legend()}\n" + "\n".join([format_detailed(r) for r in results])
    with open(os.path.join("data", "screening", f"Earnings_{today}.txt"), "w") as f:
        f.write(content)
    print(f"\nReport saved.\n\n{summary}\n")

if __name__ == "__main__":
    main()

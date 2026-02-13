#!/usr/bin/env python3
"""
Price Context Script
====================

Fetches 5 years of dividend-adjusted daily price data from FMP and computes
price context metrics for screening triage.

Metrics computed:
- vs_1yr through vs_5yr (current price vs. close N years ago)
- price_vs_5yr_avg, 52w_high, 52w_low, 52w_position
- cagr_5yr, upside_if_revert (to 1yr avg)
- cv (coefficient of variation), z_score (of recent 1mo return)
- max_drawdown_5yr, drop_vs_max_drawdown
- trend_slope_1yr, trend_slope_5yr (in per-ticker JSON only)

Usage:
    python scripts/price.py AAPL MSFT NOW
    python scripts/price.py --category losers
    python scripts/price.py --all

Output:
    Summary table to stdout
    data/tickers/{TICKER}/raw/{TICKER}_price.json
    data/screening/Price_YYYY-MM-DD.txt
"""

import sys
import os
import re
import argparse
import statistics
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
)

import requests
import time

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 2  # seconds between API calls

# ---------------------------------------------------------------------------
# SESSION_NOTES ticker extraction
# ---------------------------------------------------------------------------

CATEGORY_HEADERS = {
    "losers": "### Screening Candidates — Losers",
    "ai": "### Screening Candidates — AI",
    "other": "### Screening Candidates — Other",
}


def parse_tickers_from_session_notes(categories):
    """Extract bold ticker symbols from SESSION_NOTES.md for given categories."""
    notes_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "SESSION_NOTES.md",
    )
    if not os.path.exists(notes_path):
        print(f"Error: {notes_path} not found")
        sys.exit(1)

    with open(notes_path, "r") as f:
        content = f.read()

    tickers = []
    for cat in categories:
        header = CATEGORY_HEADERS.get(cat)
        if not header:
            print(f"Warning: unknown category '{cat}', skipping")
            continue

        idx = content.find(header)
        if idx == -1:
            print(f"Warning: header '{header}' not found in SESSION_NOTES.md")
            continue

        # Extract from header to next ### or --- section break
        section_start = idx + len(header)
        next_section = re.search(r"\n###\s|\n---", content[section_start:])
        section_end = section_start + next_section.start() if next_section else len(content)
        section = content[section_start:section_end]

        # Match **TICKER** patterns (uppercase letters, possibly with dots for BRK.B etc.)
        found = re.findall(r"\*\*([A-Z][A-Z0-9.]+)\*\*", section)
        tickers.extend(found)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for t in tickers:
        if t not in seen:
            seen.add(t)
            unique.append(t)

    return unique


# ---------------------------------------------------------------------------
# FMP data fetching
# ---------------------------------------------------------------------------


def fetch_fmp_prices(ticker, years=5):
    """Fetch dividend-adjusted daily prices from FMP for the last N years."""
    from_date = (datetime.now() - timedelta(days=years * 365 + 30)).strftime("%Y-%m-%d")
    url = (
        f"{FMP_BASE}/historical-price-eod/dividend-adjusted"
        f"?symbol={ticker}&from={from_date}&apikey={FMP_API_KEY}"
    )

    try:
        r = requests.get(url, timeout=30)
    except requests.exceptions.RequestException as e:
        print(f"  Error fetching {ticker}: {e}")
        return None

    if r.status_code != 200:
        print(f"  Error fetching {ticker}: HTTP {r.status_code}")
        return None

    try:
        data = r.json()
    except ValueError:
        print(f"  Error: invalid JSON for {ticker}")
        return None

    if isinstance(data, dict) and "error" in data:
        print(f"  API error for {ticker}: {data['error']}")
        return None

    if not data or not isinstance(data, list):
        print(f"  No data returned for {ticker}")
        return None

    return data


# ---------------------------------------------------------------------------
# Metrics computation
# ---------------------------------------------------------------------------


def derive_monthly_closes(daily_prices):
    """From daily prices (newest-first from FMP), derive month-end closes.

    Returns list of (date_str, close) sorted oldest-first.
    """
    # Sort oldest-first
    sorted_prices = sorted(daily_prices, key=lambda p: p["date"])

    monthly = {}
    for p in sorted_prices:
        month_key = p["date"][:7]  # YYYY-MM
        monthly[month_key] = (p["date"], p["adjClose"])

    return [(date, close) for date, close in monthly.values()]


def find_close_n_years_ago(monthly_closes, years):
    """Find the close price closest to N years ago from the most recent date."""
    if not monthly_closes:
        return None
    target = datetime.strptime(monthly_closes[-1][0], "%Y-%m-%d") - timedelta(days=years * 365)
    best = None
    best_diff = float("inf")
    for date_str, close in monthly_closes:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        diff = abs((dt - target).days)
        if diff < best_diff:
            best_diff = diff
            best = close
    # Only accept if within ~2 months of target
    if best_diff > 75:
        return None
    return best


def compute_max_drawdown(daily_prices_sorted):
    """Compute max peak-to-trough drawdown from daily prices (oldest-first)."""
    peak = daily_prices_sorted[0]["adjClose"]
    max_dd = 0.0
    for p in daily_prices_sorted:
        price = p["adjClose"]
        if price > peak:
            peak = price
        dd = (peak - price) / peak if peak > 0 else 0
        if dd > max_dd:
            max_dd = dd
    return max_dd


def linear_regression_slope(values):
    """Slope of linear regression (y=values, x=0..n-1). Returns slope."""
    n = len(values)
    if n < 2:
        return None
    x_mean = (n - 1) / 2.0
    y_mean = sum(values) / n
    num = sum((i - x_mean) * (v - y_mean) for i, v in enumerate(values))
    den = sum((i - x_mean) ** 2 for i in range(n))
    if den == 0:
        return None
    return num / den


def analyze_ticker(ticker, daily_prices):
    """Compute all price context metrics for a single ticker."""

    # Sort oldest-first
    sorted_daily = sorted(daily_prices, key=lambda p: p["date"])

    if len(sorted_daily) < 30:
        print(f"  Warning: only {len(sorted_daily)} days of data for {ticker}")
        return None

    current_price = sorted_daily[-1]["adjClose"]
    current_date = sorted_daily[-1]["date"]

    # Monthly closes (oldest-first)
    monthly_closes = derive_monthly_closes(daily_prices)

    if len(monthly_closes) < 2:
        print(f"  Warning: insufficient monthly data for {ticker}")
        return None

    monthly_prices = [c for _, c in monthly_closes]

    # --- Returns vs N years ago ---
    vs_years = {}
    for y in [1, 2, 3, 4, 5]:
        old_price = find_close_n_years_ago(monthly_closes, y)
        if old_price and old_price > 0:
            vs_years[f"vs_{y}yr"] = (current_price - old_price) / old_price
        else:
            vs_years[f"vs_{y}yr"] = None

    # --- 5yr average ---
    avg_5yr = statistics.mean(monthly_prices)
    price_vs_5yr_avg = (current_price - avg_5yr) / avg_5yr if avg_5yr > 0 else None

    # --- 52-week high/low/position ---
    one_year_ago = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    daily_1yr = [p for p in sorted_daily if p["date"] >= one_year_ago]
    if daily_1yr:
        high_52w = max(p["adjHigh"] for p in daily_1yr)
        low_52w = min(p["adjLow"] for p in daily_1yr)
        range_52w = high_52w - low_52w
        position_52w = (current_price - low_52w) / range_52w if range_52w > 0 else 0.5
    else:
        high_52w = low_52w = current_price
        position_52w = 0.5

    # --- CAGR 5yr ---
    first_price = monthly_prices[0]
    years_span = len(monthly_prices) / 12.0
    if first_price > 0 and current_price > 0 and years_span > 0:
        cagr_5yr = (current_price / first_price) ** (1.0 / years_span) - 1
    else:
        cagr_5yr = None

    # --- Upside if revert to 1yr avg ---
    monthly_1yr = monthly_prices[-12:] if len(monthly_prices) >= 12 else monthly_prices
    avg_1yr = statistics.mean(monthly_1yr)
    upside_if_revert = (avg_1yr - current_price) / current_price if current_price > 0 else None

    # --- Monthly returns ---
    monthly_returns = []
    for i in range(1, len(monthly_prices)):
        if monthly_prices[i - 1] > 0:
            monthly_returns.append(
                (monthly_prices[i] - monthly_prices[i - 1]) / monthly_prices[i - 1]
            )

    # --- CV (coefficient of variation) ---
    if monthly_prices and statistics.mean(monthly_prices) > 0:
        cv = statistics.stdev(monthly_prices) / statistics.mean(monthly_prices) if len(monthly_prices) > 1 else 0
    else:
        cv = None

    # --- Z-score of most recent monthly return ---
    if len(monthly_returns) >= 3:
        recent_return = monthly_returns[-1]
        mean_return = statistics.mean(monthly_returns)
        std_return = statistics.stdev(monthly_returns)
        z_score = (recent_return - mean_return) / std_return if std_return > 0 else 0
    else:
        z_score = None
        recent_return = monthly_returns[-1] if monthly_returns else None

    # --- Max drawdown (5yr, from daily data) ---
    max_dd = compute_max_drawdown(sorted_daily)

    # --- Drop vs max drawdown ---
    recent_1mo_return = monthly_returns[-1] if monthly_returns else 0
    if max_dd > 0 and recent_1mo_return < 0:
        drop_vs_max_dd = abs(recent_1mo_return) / max_dd
    else:
        drop_vs_max_dd = 0.0

    # --- Trend slopes (supplementary) ---
    monthly_1yr_prices = monthly_prices[-12:] if len(monthly_prices) >= 12 else monthly_prices
    slope_1yr = linear_regression_slope(monthly_1yr_prices)
    slope_5yr = linear_regression_slope(monthly_prices)

    return {
        "ticker": ticker,
        "as_of": current_date,
        "current_price": current_price,
        "table_metrics": {
            "vs_1yr": vs_years.get("vs_1yr"),
            "vs_2yr": vs_years.get("vs_2yr"),
            "vs_3yr": vs_years.get("vs_3yr"),
            "vs_4yr": vs_years.get("vs_4yr"),
            "vs_5yr": vs_years.get("vs_5yr"),
            "cv": cv,
            "z_score": z_score,
            "52w_high": high_52w,
            "52w_low": low_52w,
            "52w_position": position_52w,
            "drop_vs_max_drawdown": drop_vs_max_dd,
            "upside_if_revert": upside_if_revert,
            "cagr_5yr": cagr_5yr,
        },
        "supplementary": {
            "price_vs_5yr_avg": price_vs_5yr_avg,
            "max_drawdown_5yr": max_dd,
            "trend_slope_1yr": slope_1yr,
            "trend_slope_5yr": slope_5yr,
            "avg_price_1yr": avg_1yr,
            "avg_price_5yr": avg_5yr,
            "monthly_returns": monthly_returns,
        },
    }


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def format_pct(val, decimals=0):
    if val is None:
        return "-"
    return f"{val:+.{decimals}%}"


def format_table(results):
    """Format results into a comparison table string."""
    headers = [
        "Ticker", "Price", "vs1Y", "vs2Y", "vs3Y", "vs5Y",
        "CV", "Z-Score", "52w Pos", "Drop/MaxDD", "Revert↑", "5yr CAGR",
    ]

    rows = []
    for r in results:
        m = r["table_metrics"]
        rows.append([
            r["ticker"],
            f"${r['current_price']:.2f}",
            format_pct(m["vs_1yr"]),
            format_pct(m["vs_2yr"]),
            format_pct(m["vs_3yr"]),
            format_pct(m["vs_5yr"]),
            f"{m['cv']:.2f}" if m["cv"] is not None else "-",
            f"{m['z_score']:+.1f}" if m["z_score"] is not None else "-",
            f"{m['52w_position']:.0%}" if m["52w_position"] is not None else "-",
            f"{m['drop_vs_max_drawdown']:.0%}" if m["drop_vs_max_drawdown"] else "-",
            format_pct(m["upside_if_revert"]),
            format_pct(m["cagr_5yr"], 1),
        ])

    # Compute column widths
    col_widths = [max(len(str(row[i])) for row in [headers] + rows) for i in range(len(headers))]

    def fmt_row(row):
        return " | ".join(str(row[i]).rjust(col_widths[i]) for i in range(len(headers)))

    lines = []
    lines.append(fmt_row(headers))
    lines.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        lines.append(fmt_row(row))

    return "\n".join(lines)


def save_results(results):
    """Save per-ticker JSON and batch summary."""
    for r in results:
        ticker = r["ticker"]
        data_dir = get_data_directory(ticker)
        ensure_directory_exists(data_dir)
        json_path = os.path.join(data_dir, f"{ticker}_price.json")
        save_json(r, json_path)
        print(f"  Saved {json_path}")

    # Batch summary
    if results:
        today = datetime.now().strftime("%Y-%m-%d")
        screening_dir = os.path.join("data", "screening")
        ensure_directory_exists(screening_dir)
        summary_path = os.path.join(screening_dir, f"Price_{today}.txt")
        table = format_table(results)
        header = f"PRICE CONTEXT — {today}\nTickers: {', '.join(r['ticker'] for r in results)}\n\n"
        with open(summary_path, "w") as f:
            f.write(header + table + "\n")
        print(f"\n  Batch summary: {summary_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Price context for screening triage")
    parser.add_argument("tickers", nargs="*", help="Ticker symbol(s)")
    parser.add_argument(
        "--category",
        nargs="+",
        choices=["losers", "ai", "other"],
        help="Read tickers from SESSION_NOTES by category",
    )
    parser.add_argument("--all", action="store_true", help="All categories from SESSION_NOTES")
    args = parser.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

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
        print(f"Fetching {ticker}...")
        daily = fetch_fmp_prices(ticker)
        if not daily:
            continue
        analysis = analyze_ticker(ticker, daily)
        if analysis:
            results.append(analysis)

    if not results:
        print("\nNo results to display.")
        sys.exit(1)

    # Print table
    print(f"\n{'=' * 120}")
    print(format_table(results))
    print(f"{'=' * 120}\n")

    # Save
    save_results(results)


if __name__ == "__main__":
    main()

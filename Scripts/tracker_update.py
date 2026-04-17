#!/usr/bin/env python3
"""
Tracker Update Script
=====================

Fetches market data for all tickers in the PIPELINE and WATCHLIST tables of
Stock_Tracker.md and writes the metrics back into those tables in-place.

Metrics updated (columns 5-15 in both tables):
  Mkt Cap | Price | vs_3M | vs_1Y | 52w_below | Price CAGR (5yr) |
  P/E | EPS CAGR | Beats (4Q) | Fwd Delta | Next Earnings

Saves per-ticker JSON to Data/tickers/{TICKER}/raw/ for compatibility
with the rest of the workflow (price.py, earnings.py).

Usage:
    python Scripts/tracker_update.py              # all tickers in tracker
    python Scripts/tracker_update.py AXON META    # specific tickers only
"""

import sys
import os
import argparse
import statistics
import requests
import time
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
)

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 2  # seconds between FMP calls

TRACKER_PATH = "Stock_Tracker.md"

# Columns 5-15 (1-indexed in pipe-split) are the market data columns
# and are identical in both PIPELINE and WATCHLIST tables.
MARKET_COL_INDICES = {
    "mkt_cap":        5,
    "price":          6,
    "vs_3m":          7,
    "vs_1y":          8,
    "52w_below":      9,
    "price_cagr_5yr": 10,
    "pe":             11,
    "eps_cagr":       12,
    "beats_4q":       13,
    "fwd_delta":      14,
    "next_earnings":  15,
}


# ---------------------------------------------------------------------------
# Tracker parsing
# ---------------------------------------------------------------------------

def parse_tickers_from_tracker():
    """Read all tickers from PIPELINE and WATCHLIST sections of Stock_Tracker.md."""
    tickers = []
    seen = set()

    with open(TRACKER_PATH, "r") as f:
        lines = f.readlines()

    current_section = None
    in_data = False  # True after we've passed the header row

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("## PIPELINE"):
            current_section = "PIPELINE"
            in_data = False
            continue
        elif stripped.startswith("## WATCHLIST"):
            current_section = "WATCHLIST"
            in_data = False
            continue
        elif stripped.startswith("## "):
            current_section = None
            in_data = False
            continue

        if current_section not in ("PIPELINE", "WATCHLIST"):
            continue

        if not stripped.startswith("|"):
            continue

        cells = [c.strip() for c in stripped.split("|")]
        if len(cells) < 3:
            continue

        ticker_cell = cells[1]

        # Header row
        if ticker_cell == "Ticker":
            in_data = True
            continue

        # Separator row (all dashes/colons)
        if not ticker_cell or ticker_cell.replace("-", "").replace(":", "").strip() == "":
            continue

        if in_data and ticker_cell not in seen:
            tickers.append(ticker_cell)
            seen.add(ticker_cell)

    return tickers


# ---------------------------------------------------------------------------
# FMP data fetching
# ---------------------------------------------------------------------------

def fetch_profile(ticker):
    """Fetch company profile (includes market cap) from FMP."""
    url = f"{FMP_BASE}/profile?symbol={ticker}&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [profile] HTTP {r.status_code}")
            return None
        data = r.json()
        return data[0] if isinstance(data, list) and data else None
    except Exception as e:
        print(f"  [profile] Error: {e}")
        return None


def fetch_prices(ticker, years=5):
    """Fetch 5 years of dividend-adjusted daily prices from FMP."""
    from_date = (datetime.now() - timedelta(days=years * 365 + 30)).strftime("%Y-%m-%d")
    url = (
        f"{FMP_BASE}/historical-price-eod/dividend-adjusted"
        f"?symbol={ticker}&from={from_date}&apikey={FMP_API_KEY}"
    )
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [price] HTTP {r.status_code}")
            return None
        data = r.json()
        if not data or not isinstance(data, list):
            print(f"  [price] No data returned")
            return None
        return data
    except Exception as e:
        print(f"  [price] Error: {e}")
        return None


def fetch_earnings_history(ticker):
    """Fetch earnings history (40 entries = ~10 years of quarters) from FMP."""
    url = f"{FMP_BASE}/earnings?symbol={ticker}&limit=40&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [earnings] HTTP {r.status_code}")
            return None
        return r.json()
    except Exception as e:
        print(f"  [earnings] Error: {e}")
        return None


# ---------------------------------------------------------------------------
# Metrics computation
# ---------------------------------------------------------------------------

def safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def compute_price_metrics(ticker, daily_prices):
    """Compute all price metrics needed for the tracker."""
    sorted_daily = sorted(daily_prices, key=lambda p: p["date"])
    if len(sorted_daily) < 30:
        print(f"  [price] Insufficient data ({len(sorted_daily)} days)")
        return None

    current_price = sorted_daily[-1]["adjClose"]
    current_date = sorted_daily[-1]["date"]
    now = datetime.now()

    # vs_3M: price change vs. ~90 days ago
    target_3m = (now - timedelta(days=90)).strftime("%Y-%m-%d")
    prior_3m = [p for p in sorted_daily if p["date"] <= target_3m]
    vs_3m = None
    if prior_3m and prior_3m[-1]["adjClose"] > 0:
        vs_3m = (current_price - prior_3m[-1]["adjClose"]) / prior_3m[-1]["adjClose"]

    # vs_1Y: price change vs. ~1 year ago
    target_1y = (now - timedelta(days=365)).strftime("%Y-%m-%d")
    prior_1y = [p for p in sorted_daily if p["date"] <= target_1y]
    vs_1y = None
    if prior_1y and prior_1y[-1]["adjClose"] > 0:
        vs_1y = (current_price - prior_1y[-1]["adjClose"]) / prior_1y[-1]["adjClose"]

    # 52-week high and % below it
    one_year_ago = (now - timedelta(days=365)).strftime("%Y-%m-%d")
    daily_1yr = [p for p in sorted_daily if p["date"] >= one_year_ago]
    high_52w = max(p["adjHigh"] for p in daily_1yr) if daily_1yr else current_price
    below_52w = (high_52w - current_price) / high_52w if high_52w > 0 else 0.0

    # Price CAGR (5yr) using monthly closes
    monthly = {}
    for p in sorted_daily:
        month_key = p["date"][:7]
        monthly[month_key] = p["adjClose"]
    monthly_prices = list(monthly.values())
    cagr_5yr = None
    if len(monthly_prices) >= 2 and monthly_prices[0] > 0:
        years_span = len(monthly_prices) / 12.0
        if years_span > 0:
            cagr_5yr = (current_price / monthly_prices[0]) ** (1.0 / years_span) - 1

    return {
        "ticker": ticker,
        "as_of": current_date,
        "current_price": current_price,
        "vs_3m": vs_3m,
        "vs_1y": vs_1y,
        "52w_high": high_52w,
        "52w_below": below_52w,
        "cagr_5yr": cagr_5yr,
        # Passthrough fields for compatibility with earnings.py logic
        "table_metrics": {"vs_1yr": vs_1y},
        "supplementary": {"recent_trend": []},
    }


def compute_earnings_metrics(ticker, history, price_data):
    """Compute P/E, EPS CAGR, beat streak, and forward delta from earnings history."""
    if not history:
        return None

    next_est = None
    next_date = None
    last_actual = None
    actual_quarters = []

    for h in history:
        act = safe_float(h.get("epsActual"))
        est = safe_float(h.get("epsEstimated"))
        dt = h.get("date")

        if act is None and est is not None and next_est is None:
            next_est = est
            next_date = dt
        elif act is not None:
            if last_actual is None:
                last_actual = act
            actual_quarters.append({"date": dt, "actual": act, "estimated": est})

    if not actual_quarters:
        return None

    actual_sorted = sorted(actual_quarters, key=lambda x: x["date"])

    # Build TTM annual blocks (4 quarters each) for P/E and EPS CAGR
    annual_eps = []
    for i in range(len(actual_sorted), 3, -4):
        chunk = actual_sorted[i - 4:i]
        ttm = sum(q["actual"] for q in chunk)
        annual_eps.append({"date": chunk[-1]["date"], "eps": ttm})
    # annual_eps[0] = most recent TTM, annual_eps[1] = 1yr ago, etc.

    # Current P/E (TTM)
    curr_price = price_data.get("current_price")
    ttm_eps = annual_eps[0]["eps"] if annual_eps else None
    curr_pe = curr_price / ttm_eps if (ttm_eps and ttm_eps > 0 and curr_price) else None

    # EPS CAGR (5yr if available, otherwise full span)
    cagr_5yr = None
    if len(annual_eps) >= 6:
        s, e = annual_eps[5]["eps"], annual_eps[0]["eps"]
        if s > 0 and e > 0:
            cagr_5yr = (e / s) ** (1 / 5) - 1
    elif len(annual_eps) >= 2:
        s, e = annual_eps[-1]["eps"], annual_eps[0]["eps"]
        yrs = len(annual_eps) - 1
        if s > 0 and e > 0 and yrs > 0:
            cagr_5yr = (e / s) ** (1 / yrs) - 1

    # Beats (4Q): newest 4 quarters, newest first, formatted as +/+/-/+
    newest_4 = sorted(actual_quarters, key=lambda x: x["date"], reverse=True)[:4]
    symbols = []
    for q in newest_4:
        act, est = q["actual"], q["estimated"]
        if est is None or act is None:
            symbols.append("?")
        elif act >= est:
            symbols.append("+")
        else:
            symbols.append("-")
    beats_str = "/".join(symbols) if symbols else None

    # Forward delta: next quarter estimate minus last actual EPS
    fwd_delta = None
    if next_est is not None and last_actual is not None:
        fwd_delta = next_est - last_actual

    return {
        "current_pe": curr_pe,
        "eps_cagr": cagr_5yr,
        "beats_4q": beats_str,
        "fwd_delta": fwd_delta,
        "next_date": next_date,
    }


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def fmt_mktcap(val):
    if val is None:
        return "—"
    if val >= 1e12:
        return f"${val / 1e12:.2f}T"
    if val >= 1e9:
        return f"${val / 1e9:.2f}B"
    if val >= 1e6:
        return f"${val / 1e6:.2f}M"
    return f"${val:.0f}"


def fmt_price(val):
    return f"${val:.2f}" if val is not None else "—"


def fmt_pct(val, sign=True):
    if val is None:
        return "—"
    return f"{val:+.1%}" if sign else f"{val:.1%}"


def fmt_pe(val):
    return f"{val:.1f}x" if val is not None else "—"


def fmt_fwd_delta(val):
    return f"${val:+.2f}" if val is not None else "—"


# ---------------------------------------------------------------------------
# Tracker update
# ---------------------------------------------------------------------------

def update_tracker(ticker_metrics):
    """Write computed metrics back into the market data columns of Stock_Tracker.md."""
    with open(TRACKER_PATH, "r") as f:
        lines = f.readlines()

    current_section = None
    in_data = False
    new_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("## PIPELINE"):
            current_section = "PIPELINE"
            in_data = False
        elif stripped.startswith("## WATCHLIST"):
            current_section = "WATCHLIST"
            in_data = False
        elif stripped.startswith("## "):
            current_section = None
            in_data = False

        if current_section in ("PIPELINE", "WATCHLIST") and stripped.startswith("|"):
            cells = line.split("|")
            if len(cells) >= 3:
                ticker_cell = cells[1].strip()

                if ticker_cell == "Ticker":
                    in_data = True
                elif in_data and ticker_cell and not ticker_cell.replace("-", "").replace(":", "").strip() == "":
                    if ticker_cell in ticker_metrics:
                        m = ticker_metrics[ticker_cell]
                        cells[MARKET_COL_INDICES["mkt_cap"]]        = f" {m['mkt_cap']} "
                        cells[MARKET_COL_INDICES["price"]]           = f" {m['price']} "
                        cells[MARKET_COL_INDICES["vs_3m"]]           = f" {m['vs_3m']} "
                        cells[MARKET_COL_INDICES["vs_1y"]]           = f" {m['vs_1y']} "
                        cells[MARKET_COL_INDICES["52w_below"]]       = f" {m['52w_below']} "
                        cells[MARKET_COL_INDICES["price_cagr_5yr"]]  = f" {m['price_cagr_5yr']} "
                        cells[MARKET_COL_INDICES["pe"]]              = f" {m['pe']} "
                        cells[MARKET_COL_INDICES["eps_cagr"]]        = f" {m['eps_cagr']} "
                        cells[MARKET_COL_INDICES["beats_4q"]]        = f" {m['beats_4q']} "
                        cells[MARKET_COL_INDICES["fwd_delta"]]       = f" {m['fwd_delta']} "
                        cells[MARKET_COL_INDICES["next_earnings"]]   = f" {m['next_earnings']} "
                        line = "|".join(cells)

        new_lines.append(line)

    with open(TRACKER_PATH, "w") as f:
        f.writelines(new_lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Update market data columns in Stock_Tracker.md via FMP."
    )
    parser.add_argument(
        "tickers",
        nargs="*",
        help="Specific ticker(s) to update. Defaults to all tickers in tracker.",
    )
    args = parser.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

    tickers = [t.upper() for t in args.tickers] if args.tickers else parse_tickers_from_tracker()

    if not tickers:
        print("No tickers found in tracker.")
        sys.exit(1)

    print(f"Updating {len(tickers)} ticker(s): {', '.join(tickers)}\n")

    ticker_metrics = {}

    for i, ticker in enumerate(tickers):
        print(f"[{i + 1}/{len(tickers)}] {ticker}")

        # --- Profile (market cap) ---
        if i > 0:
            time.sleep(API_CALL_DELAY)
        profile = fetch_profile(ticker)
        mkt_cap = profile.get("marketCap") if profile else None

        # --- Price data ---
        time.sleep(API_CALL_DELAY)
        daily_prices = fetch_prices(ticker)
        price_metrics = compute_price_metrics(ticker, daily_prices) if daily_prices else None

        if price_metrics:
            data_dir = get_data_directory(ticker)
            ensure_directory_exists(data_dir)
            save_json(price_metrics, os.path.join(data_dir, f"{ticker}_price.json"))

        # --- Earnings data ---
        time.sleep(API_CALL_DELAY)
        earnings_history = fetch_earnings_history(ticker)
        earnings_metrics = None
        if earnings_history and price_metrics:
            earnings_metrics = compute_earnings_metrics(ticker, earnings_history, price_metrics)
            if earnings_metrics:
                save_json(
                    earnings_metrics,
                    os.path.join(get_data_directory(ticker), f"{ticker}_earnings.json"),
                )

        # --- Format for tracker ---
        m = {
            "mkt_cap":        fmt_mktcap(mkt_cap),
            "price":          fmt_price(price_metrics["current_price"]) if price_metrics else "—",
            "vs_3m":          fmt_pct(price_metrics["vs_3m"]) if price_metrics else "—",
            "vs_1y":          fmt_pct(price_metrics["vs_1y"]) if price_metrics else "—",
            "52w_below":      fmt_pct(price_metrics["52w_below"], sign=False) if price_metrics else "—",
            "price_cagr_5yr": fmt_pct(price_metrics["cagr_5yr"]) if price_metrics else "—",
            "pe":             fmt_pe(earnings_metrics["current_pe"]) if earnings_metrics else "—",
            "eps_cagr":       fmt_pct(earnings_metrics["eps_cagr"]) if earnings_metrics else "—",
            "beats_4q":       earnings_metrics["beats_4q"] if earnings_metrics and earnings_metrics["beats_4q"] else "—",
            "fwd_delta":      fmt_fwd_delta(earnings_metrics["fwd_delta"]) if earnings_metrics else "—",
            "next_earnings":  earnings_metrics["next_date"] if earnings_metrics and earnings_metrics["next_date"] else "—",
        }
        ticker_metrics[ticker] = m

        print(
            f"  Cap: {m['mkt_cap']}  Price: {m['price']}  "
            f"vs3M: {m['vs_3m']}  vs1Y: {m['vs_1y']}  "
            f"52w↓: {m['52w_below']}  P/E: {m['pe']}  "
            f"EPS CAGR: {m['eps_cagr']}  Beats: {m['beats_4q']}"
        )

    print(f"\nWriting to {TRACKER_PATH}...")
    update_tracker(ticker_metrics)
    print("Done.")


if __name__ == "__main__":
    main()

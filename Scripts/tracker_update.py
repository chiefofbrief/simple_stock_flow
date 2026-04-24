#!/usr/bin/env python3
"""
Tracker Update Script
=====================

Fetches market data for all tickers in PIPELINE, WATCHLIST, and Trade Tracker
sections of Stock_Tracker.md and writes the metrics back in-place.

Metrics updated (PIPELINE / WATCHLIST):
  Mkt Cap | Price | vs_1M | vs_1Y | Price CAGR (5yr) |
  P/E | EPS QoQ | EPS YoY | EPS CAGR (5yr) | Rev YoY | Fwd Delta | Next Earnings

Metrics updated (Trade Tracker):
  Price | vs_1M | vs_1Y | P/E | EPS QoQ | EPS YoY | Rev YoY | Fwd Delta | Next Earnings

Saves per-ticker JSON to Data/tickers/{TICKER}/raw/ for compatibility
with the rest of the workflow (price.py, earnings.py).

Usage:
    python Scripts/tracker_update.py              # all tickers in tracker
    python Scripts/tracker_update.py AXON META    # specific tickers only
"""

import sys
import os
import argparse
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

# Column indices for PIPELINE and WATCHLIST (1-indexed in pipe-split)
# Ticker=1, Tag=2, Mkt Cap=3, Price=4, vs_1M=5, vs_1Y=6, Price CAGR=7,
# P/E=8, EPS QoQ=9, EPS YoY=10, EPS CAGR=11, Rev YoY=12, Fwd Delta=13, Next Earnings=14
MARKET_COL_INDICES = {
    "mkt_cap":        3,
    "price":          4,
    "vs_1m":          5,
    "vs_1y":          6,
    "price_cagr_5yr": 7,
    "pe":             8,
    "eps_qoq":        9,
    "eps_yoy":        10,
    "eps_cagr":       11,
    "rev_yoy":        12,
    "fwd_delta":      13,
    "next_earnings":  14,
}

# Column indices for Trade Tracker (1-indexed in pipe-split)
# Ticker=1, Entry Date=2, Entry Price=3, Shares=4, Cost Basis=5,
# Price=6, vs_1M=7, vs_1Y=8, P/E=9, EPS QoQ=10, EPS YoY=11,
# Rev YoY=12, Fwd Delta=13, Next Earnings=14, Thesis=15
TRADE_COL_INDICES = {
    "price":          6,
    "vs_1m":          7,
    "vs_1y":          8,
    "pe":             9,
    "eps_qoq":        10,
    "eps_yoy":        11,
    "rev_yoy":        12,
    "fwd_delta":      13,
    "next_earnings":  14,
}


# ---------------------------------------------------------------------------
# Tracker parsing
# ---------------------------------------------------------------------------

def parse_tickers_from_tracker():
    """Read all unique tickers from PIPELINE, WATCHLIST, and Trade Tracker."""
    tickers = []
    seen = set()

    with open(TRACKER_PATH, "r") as f:
        lines = f.readlines()

    current_section = None
    in_data = False

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
        elif stripped.startswith("## Trade Tracker"):
            current_section = "TRADE"
            in_data = False
            continue
        elif stripped.startswith("## "):
            current_section = None
            in_data = False
            continue

        if current_section not in ("PIPELINE", "WATCHLIST", "TRADE"):
            continue

        if not stripped.startswith("|"):
            continue

        cells = [c.strip() for c in stripped.split("|")]
        if len(cells) < 3:
            continue

        ticker_cell = cells[1]

        if ticker_cell == "Ticker":
            in_data = True
            continue

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
    """Fetch earnings history (40 entries) from FMP for fwd_delta and eps_cagr."""
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


def fetch_income_statement(ticker):
    """Fetch 8 quarters of GAAP income statements from FMP."""
    url = f"{FMP_BASE}/income-statement?symbol={ticker}&period=quarter&limit=8&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [income_stmt] HTTP {r.status_code}")
            return None
        data = r.json()
        return data if isinstance(data, list) else None
    except Exception as e:
        print(f"  [income_stmt] Error: {e}")
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
    """Compute price metrics: current price, vs_1M, vs_1Y, Price CAGR (5yr)."""
    sorted_daily = sorted(daily_prices, key=lambda p: p["date"])
    if len(sorted_daily) < 30:
        print(f"  [price] Insufficient data ({len(sorted_daily)} days)")
        return None

    current_price = sorted_daily[-1]["adjClose"]
    current_date = sorted_daily[-1]["date"]
    now = datetime.now()

    # vs_1M: price change vs. ~30 days ago
    target_1m = (now - timedelta(days=30)).strftime("%Y-%m-%d")
    prior_1m = [p for p in sorted_daily if p["date"] <= target_1m]
    vs_1m = None
    if prior_1m and prior_1m[-1]["adjClose"] > 0:
        vs_1m = (current_price - prior_1m[-1]["adjClose"]) / prior_1m[-1]["adjClose"]

    # vs_1Y: price change vs. ~1 year ago
    target_1y = (now - timedelta(days=365)).strftime("%Y-%m-%d")
    prior_1y = [p for p in sorted_daily if p["date"] <= target_1y]
    vs_1y = None
    if prior_1y and prior_1y[-1]["adjClose"] > 0:
        vs_1y = (current_price - prior_1y[-1]["adjClose"]) / prior_1y[-1]["adjClose"]

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
        "vs_1m": vs_1m,
        "vs_1y": vs_1y,
        "cagr_5yr": cagr_5yr,
    }


def compute_earnings_metrics(ticker, history, price_data):
    """Compute EPS CAGR (5yr) and Fwd Delta from earnings history."""
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

    # Build TTM annual blocks for EPS CAGR
    annual_eps = []
    for i in range(len(actual_sorted), 3, -4):
        chunk = actual_sorted[i - 4:i]
        ttm = sum(q["actual"] for q in chunk)
        annual_eps.append({"date": chunk[-1]["date"], "eps": ttm})

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

    # Forward delta: next quarter estimate minus last actual EPS
    fwd_delta = None
    if next_est is not None and last_actual is not None:
        fwd_delta = next_est - last_actual

    return {
        "eps_cagr": cagr_5yr,
        "fwd_delta": fwd_delta,
        "next_date": next_date,
    }


def compute_gaap_pe(income_data, current_price):
    """Compute TTM GAAP P/E from the 4 most recent quarterly income statements."""
    if not income_data or not current_price:
        return None
    eps_vals = [safe_float(q.get("eps")) for q in income_data[:4]]
    eps_vals = [e for e in eps_vals if e is not None]
    if len(eps_vals) < 4:
        return None
    ttm_eps = sum(eps_vals)
    return current_price / ttm_eps if ttm_eps > 0 else None


def compute_quarterly_metrics(income_data):
    """Compute EPS QoQ, EPS YoY, and Rev YoY from quarterly income statements.

    income_data is sorted most-recent-first (standard FMP order):
      [0] = most recent quarter
      [1] = prior quarter      (for QoQ)
      [4] = same quarter -1yr  (for YoY)
    """
    if not income_data or len(income_data) < 2:
        return {"eps_qoq": None, "eps_yoy": None, "rev_yoy": None}

    q0 = income_data[0]
    q1 = income_data[1] if len(income_data) > 1 else None
    q4 = income_data[4] if len(income_data) > 4 else None

    eps0 = safe_float(q0.get("eps"))
    rev0 = safe_float(q0.get("revenue"))

    # EPS QoQ
    eps_qoq = None
    if q1 is not None and eps0 is not None:
        eps1 = safe_float(q1.get("eps"))
        if eps1 is not None and eps1 != 0:
            eps_qoq = (eps0 - eps1) / abs(eps1)

    # EPS YoY
    eps_yoy = None
    if q4 is not None and eps0 is not None:
        eps4 = safe_float(q4.get("eps"))
        if eps4 is not None and eps4 != 0:
            eps_yoy = (eps0 - eps4) / abs(eps4)

    # Rev YoY
    rev_yoy = None
    if q4 is not None and rev0 is not None:
        rev4 = safe_float(q4.get("revenue"))
        if rev4 is not None and rev4 > 0:
            rev_yoy = (rev0 - rev4) / rev4

    return {
        "eps_qoq": eps_qoq,
        "eps_yoy": eps_yoy,
        "rev_yoy": rev_yoy,
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
    """Write computed metrics back into Stock_Tracker.md in-place."""
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
        elif stripped.startswith("## Trade Tracker"):
            current_section = "TRADE"
            in_data = False
        elif stripped.startswith("## "):
            current_section = None
            in_data = False

        if current_section in ("PIPELINE", "WATCHLIST", "TRADE") and stripped.startswith("|"):
            cells = line.split("|")
            if len(cells) >= 3:
                ticker_cell = cells[1].strip()

                if ticker_cell == "Ticker":
                    in_data = True
                elif in_data and ticker_cell and not ticker_cell.replace("-", "").replace(":", "").strip() == "":
                    if ticker_cell in ticker_metrics:
                        m = ticker_metrics[ticker_cell]

                        if current_section in ("PIPELINE", "WATCHLIST"):
                            cells[MARKET_COL_INDICES["mkt_cap"]]        = f" {m['mkt_cap']} "
                            cells[MARKET_COL_INDICES["price"]]           = f" {m['price']} "
                            cells[MARKET_COL_INDICES["vs_1m"]]           = f" {m['vs_1m']} "
                            cells[MARKET_COL_INDICES["vs_1y"]]           = f" {m['vs_1y']} "
                            cells[MARKET_COL_INDICES["price_cagr_5yr"]]  = f" {m['price_cagr_5yr']} "
                            cells[MARKET_COL_INDICES["pe"]]              = f" {m['pe']} "
                            cells[MARKET_COL_INDICES["eps_qoq"]]         = f" {m['eps_qoq']} "
                            cells[MARKET_COL_INDICES["eps_yoy"]]         = f" {m['eps_yoy']} "
                            cells[MARKET_COL_INDICES["eps_cagr"]]        = f" {m['eps_cagr']} "
                            cells[MARKET_COL_INDICES["rev_yoy"]]         = f" {m['rev_yoy']} "
                            cells[MARKET_COL_INDICES["fwd_delta"]]       = f" {m['fwd_delta']} "
                            cells[MARKET_COL_INDICES["next_earnings"]]   = f" {m['next_earnings']} "
                        elif current_section == "TRADE":
                            cells[TRADE_COL_INDICES["price"]]          = f" {m['price']} "
                            cells[TRADE_COL_INDICES["vs_1m"]]          = f" {m['vs_1m']} "
                            cells[TRADE_COL_INDICES["vs_1y"]]          = f" {m['vs_1y']} "
                            cells[TRADE_COL_INDICES["pe"]]             = f" {m['pe']} "
                            cells[TRADE_COL_INDICES["eps_qoq"]]        = f" {m['eps_qoq']} "
                            cells[TRADE_COL_INDICES["eps_yoy"]]        = f" {m['eps_yoy']} "
                            cells[TRADE_COL_INDICES["rev_yoy"]]        = f" {m['rev_yoy']} "
                            cells[TRADE_COL_INDICES["fwd_delta"]]      = f" {m['fwd_delta']} "
                            cells[TRADE_COL_INDICES["next_earnings"]]  = f" {m['next_earnings']} "

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

        # --- Income statement: GAAP P/E, EPS QoQ/YoY, Rev YoY ---
        time.sleep(API_CALL_DELAY)
        income_data = fetch_income_statement(ticker)
        gaap_pe = compute_gaap_pe(
            income_data,
            price_metrics["current_price"] if price_metrics else None,
        )
        quarterly = compute_quarterly_metrics(income_data) if income_data else {
            "eps_qoq": None, "eps_yoy": None, "rev_yoy": None
        }

        # --- Earnings history: EPS CAGR, Fwd Delta, Next Earnings ---
        time.sleep(API_CALL_DELAY)
        earnings_history = fetch_earnings_history(ticker)
        earnings_metrics = None
        if earnings_history and price_metrics:
            earnings_metrics = compute_earnings_metrics(ticker, earnings_history, price_metrics)

        if earnings_metrics:
            save_json(
                {**earnings_metrics, **quarterly, "gaap_pe": gaap_pe},
                os.path.join(get_data_directory(ticker), f"{ticker}_earnings.json"),
            )

        # --- Format for tracker ---
        m = {
            "mkt_cap":        fmt_mktcap(mkt_cap),
            "price":          fmt_price(price_metrics["current_price"]) if price_metrics else "—",
            "vs_1m":          fmt_pct(price_metrics["vs_1m"]) if price_metrics else "—",
            "vs_1y":          fmt_pct(price_metrics["vs_1y"]) if price_metrics else "—",
            "price_cagr_5yr": fmt_pct(price_metrics["cagr_5yr"]) if price_metrics else "—",
            "pe":             fmt_pe(gaap_pe),
            "eps_qoq":        fmt_pct(quarterly["eps_qoq"]),
            "eps_yoy":        fmt_pct(quarterly["eps_yoy"]),
            "eps_cagr":       fmt_pct(earnings_metrics["eps_cagr"]) if earnings_metrics else "—",
            "rev_yoy":        fmt_pct(quarterly["rev_yoy"]),
            "fwd_delta":      fmt_fwd_delta(earnings_metrics["fwd_delta"]) if earnings_metrics else "—",
            "next_earnings":  earnings_metrics["next_date"] if earnings_metrics and earnings_metrics["next_date"] else "—",
        }
        ticker_metrics[ticker] = m

        print(
            f"  Cap: {m['mkt_cap']}  Price: {m['price']}  "
            f"vs1M: {m['vs_1m']}  vs1Y: {m['vs_1y']}  "
            f"P/E: {m['pe']}  EPS QoQ: {m['eps_qoq']}  "
            f"EPS YoY: {m['eps_yoy']}  Rev YoY: {m['rev_yoy']}"
        )

    print(f"\nWriting to {TRACKER_PATH}...")
    update_tracker(ticker_metrics)
    print("Done.")


if __name__ == "__main__":
    main()

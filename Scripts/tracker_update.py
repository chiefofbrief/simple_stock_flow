#!/usr/bin/env python3
"""
Tracker Update Script
=====================

Fetches market data for all tickers in PIPELINE, WATCHLIST, and Trade Tracker
sections of Stock_Tracker.md and writes the metrics back in-place.

Metrics updated (PIPELINE / WATCHLIST):
  Mkt Cap | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY |
  Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings

Metrics updated (Trade Tracker):
  Price | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY | Rev YoY | Next Earnings

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
# Ticker=1, Tag=2, Mkt Cap=3, vs_1Y=4, P/E=5,
# Avg EPS QoQ (4Q)=6, EPS YoY=7, Yrs Profitable (5yr)=8,
# Rev YoY=9, FCF YoY=10, Op Margin %=11, Debt/OCF=12, Next Earnings=13
MARKET_COL_INDICES = {
    "mkt_cap":          3,
    "vs_1y":            4,
    "pe":               5,
    "avg_eps_qoq_4q":   6,
    "eps_yoy":          7,
    "yrs_profitable":   8,
    "rev_yoy":          9,
    "fcf_yoy":          10,
    "op_margin":        11,
    "debt_ocf":         12,
    "next_earnings":    13,
}

# Column indices for Trade Tracker (1-indexed in pipe-split)
# Ticker=1, Entry Date=2, Entry Price=3, Shares=4, Cost Basis=5,
# Price=6, vs_1Y=7, P/E=8, Avg EPS QoQ (4Q)=9, EPS YoY=10,
# Rev YoY=11, Next Earnings=12, Thesis=13
TRADE_COL_INDICES = {
    "price":            6,
    "vs_1y":            7,
    "pe":               8,
    "avg_eps_qoq_4q":   9,
    "eps_yoy":          10,
    "rev_yoy":          11,
    "next_earnings":    12,
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
    """Fetch earnings history (next earnings date) from FMP."""
    url = f"{FMP_BASE}/earnings?symbol={ticker}&limit=10&apikey={FMP_API_KEY}"
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
    """Fetch 20 quarters of GAAP income statements from FMP.

    20 quarters covers ~5 years, enabling Yrs Profitable computation
    without a separate annual income statement call.
    """
    url = f"{FMP_BASE}/income-statement?symbol={ticker}&period=quarter&limit=20&apikey={FMP_API_KEY}"
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


def fetch_cashflow_statement(ticker):
    """Fetch 8 quarters of cash flow statements from FMP.

    Used for: FCF YoY (q0 vs q4) and OCF TTM (sum q0-q3).
    """
    url = f"{FMP_BASE}/cash-flow-statement?symbol={ticker}&period=quarter&limit=8&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [cashflow] HTTP {r.status_code}")
            return None
        data = r.json()
        return data if isinstance(data, list) else None
    except Exception as e:
        print(f"  [cashflow] Error: {e}")
        return None


def fetch_balance_sheet(ticker):
    """Fetch most recent quarterly balance sheet from FMP.

    Used for: total debt (for Debt/OCF computation).
    """
    url = f"{FMP_BASE}/balance-sheet-statement?symbol={ticker}&period=quarter&limit=1&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [balance] HTTP {r.status_code}")
            return None
        data = r.json()
        return data if isinstance(data, list) else None
    except Exception as e:
        print(f"  [balance] Error: {e}")
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
    """Compute price metrics: current price, vs_1Y, Price CAGR (5yr)."""
    sorted_daily = sorted(daily_prices, key=lambda p: p["date"])
    if len(sorted_daily) < 30:
        print(f"  [price] Insufficient data ({len(sorted_daily)} days)")
        return None

    current_price = sorted_daily[-1]["adjClose"]
    current_date = sorted_daily[-1]["date"]
    now = datetime.now()

    # vs_1Y: price change vs. ~1 year ago
    target_1y = (now - timedelta(days=365)).strftime("%Y-%m-%d")
    prior_1y = [p for p in sorted_daily if p["date"] <= target_1y]
    vs_1y = None
    if prior_1y and prior_1y[-1]["adjClose"] > 0:
        vs_1y = (current_price - prior_1y[-1]["adjClose"]) / prior_1y[-1]["adjClose"]

    return {
        "ticker": ticker,
        "as_of": current_date,
        "current_price": current_price,
        "vs_1y": vs_1y,
    }


def extract_next_earnings(earnings_history):
    """Extract next scheduled earnings date from earnings history."""
    if not earnings_history:
        return None
    for h in earnings_history:
        act = safe_float(h.get("epsActual"))
        est = safe_float(h.get("epsEstimated"))
        if act is None and est is not None:
            return h.get("date")
    return None


def compute_gaap_pe(income_data, current_price):
    """Compute TTM GAAP P/E from the 4 most recent quarterly income statements.

    Uses epsDiluted (net income / diluted weighted average shares) — the most
    conservative and analytically standard GAAP figure, accounting for dilution
    from stock options, RSUs, and convertible instruments.
    """
    if not income_data or not current_price:
        return None
    eps_vals = [safe_float(q.get("epsDiluted")) for q in income_data[:4]]
    eps_vals = [e for e in eps_vals if e is not None]
    if len(eps_vals) < 4:
        return None
    ttm_eps = sum(eps_vals)
    return current_price / ttm_eps if ttm_eps > 0 else None


def compute_quarterly_metrics(income_data):
    """Compute EPS metrics and operating margin from quarterly income statements.

    income_data is sorted most-recent-first (standard FMP order):
      [0] = most recent quarter
      [1] = prior quarter      (for QoQ)
      [4] = same quarter -1yr  (for YoY)

    Returns:
      avg_eps_qoq_4q  — average of last 4 quarterly QoQ EPS changes
      eps_yoy         — EPS % change vs same quarter last year
      rev_yoy         — Revenue % change vs same quarter last year
      op_margin_ttm   — TTM operating income / TTM revenue
    """
    if not income_data or len(income_data) < 2:
        return {
            "avg_eps_qoq_4q": None,
            "eps_yoy": None,
            "rev_yoy": None,
            "op_margin_ttm": None,
        }

    q0 = income_data[0]
    q4 = income_data[4] if len(income_data) > 4 else None

    eps0 = safe_float(q0.get("epsDiluted"))
    rev0 = safe_float(q0.get("revenue"))

    # Avg EPS QoQ (4Q): average of 4 most recent quarter-over-quarter EPS changes
    # Uses epsDiluted throughout for consistency with P/E computation.
    qoq_vals = []
    for i in range(4):
        if i + 1 >= len(income_data):
            break
        eps_i  = safe_float(income_data[i].get("epsDiluted"))
        eps_i1 = safe_float(income_data[i + 1].get("epsDiluted"))
        if eps_i is not None and eps_i1 is not None and eps_i1 != 0:
            qoq_vals.append((eps_i - eps_i1) / abs(eps_i1))
    avg_eps_qoq_4q = sum(qoq_vals) / len(qoq_vals) if qoq_vals else None

    # EPS YoY
    eps_yoy = None
    if q4 is not None and eps0 is not None:
        eps4 = safe_float(q4.get("epsDiluted"))
        if eps4 is not None and eps4 != 0:
            eps_yoy = (eps0 - eps4) / abs(eps4)

    # Rev YoY
    rev_yoy = None
    if q4 is not None and rev0 is not None:
        rev4 = safe_float(q4.get("revenue"))
        if rev4 is not None and rev4 > 0:
            rev_yoy = (rev0 - rev4) / rev4

    # Op Margin % (TTM): sum of last 4 quarters
    ttm_op_income = sum(
        (safe_float(income_data[i].get("operatingIncome")) or 0) for i in range(min(4, len(income_data)))
    )
    ttm_revenue = sum(
        (safe_float(income_data[i].get("revenue")) or 0) for i in range(min(4, len(income_data)))
    )
    op_margin_ttm = ttm_op_income / ttm_revenue if ttm_revenue > 0 else None

    return {
        "avg_eps_qoq_4q": avg_eps_qoq_4q,
        "eps_yoy": eps_yoy,
        "rev_yoy": rev_yoy,
        "op_margin_ttm": op_margin_ttm,
    }


def compute_yrs_profitable(income_data):
    """Count profitable years (positive TTM net income) out of last 5.

    Groups 20 quarters into 5 TTM blocks (most recent first).
    Returns an integer 0-5, or None if insufficient data.
    """
    if not income_data or len(income_data) < 4:
        return None

    profitable = 0
    years_checked = 0
    for year_idx in range(5):
        start = year_idx * 4
        end = start + 4
        if end > len(income_data):
            break
        chunk = income_data[start:end]
        ttm_net = sum((safe_float(q.get("netIncome")) or 0) for q in chunk)
        if ttm_net > 0:
            profitable += 1
        years_checked += 1

    return profitable if years_checked > 0 else None


def compute_cashflow_metrics(cashflow_data):
    """Compute FCF YoY and OCF TTM from quarterly cash flow statements.

    Returns:
      fcf_yoy  — FCF % change vs same quarter last year
      ocf_ttm  — TTM operating cash flow (sum of last 4 quarters)
    """
    if not cashflow_data or len(cashflow_data) < 2:
        return {"fcf_yoy": None, "ocf_ttm": None}

    # FCF YoY: most recent quarter vs same quarter prior year
    fcf0 = safe_float(cashflow_data[0].get("freeCashFlow"))
    fcf4 = safe_float(cashflow_data[4].get("freeCashFlow")) if len(cashflow_data) > 4 else None
    fcf_yoy = None
    if fcf0 is not None and fcf4 is not None and fcf4 != 0:
        fcf_yoy = (fcf0 - fcf4) / abs(fcf4)

    # OCF TTM: sum of last 4 quarters of operating cash flow
    ocf_vals = [
        safe_float(cashflow_data[i].get("operatingCashFlow"))
        for i in range(min(4, len(cashflow_data)))
    ]
    ocf_vals = [v for v in ocf_vals if v is not None]
    ocf_ttm = sum(ocf_vals) if ocf_vals else None

    return {"fcf_yoy": fcf_yoy, "ocf_ttm": ocf_ttm}


def compute_debt_ocf(balance_data, ocf_ttm):
    """Compute Debt/OCF ratio from most recent balance sheet and TTM OCF.

    Returns None if OCF is zero or negative (ratio is meaningless or infinite).
    """
    if not balance_data or ocf_ttm is None or ocf_ttm <= 0:
        return None
    total_debt = safe_float(balance_data[0].get("totalDebt"))
    if total_debt is None:
        return None
    return total_debt / ocf_ttm


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


def fmt_ratio(val):
    """Format a ratio like Debt/OCF as X.Xx."""
    return f"{val:.1f}x" if val is not None else "—"


def fmt_margin(val):
    """Format operating margin as X.X% (no forced sign — margins are usually positive)."""
    if val is None:
        return "—"
    return f"{val:+.1%}" if val < 0 else f"{val:.1%}"


def fmt_yrs(val):
    """Format years profitable as integer/5."""
    return f"{val}/5" if val is not None else "—"


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
                            cells[MARKET_COL_INDICES["vs_1y"]]          = f" {m['vs_1y']} "
                            cells[MARKET_COL_INDICES["pe"]]             = f" {m['pe']} "
                            cells[MARKET_COL_INDICES["avg_eps_qoq_4q"]] = f" {m['avg_eps_qoq_4q']} "
                            cells[MARKET_COL_INDICES["eps_yoy"]]        = f" {m['eps_yoy']} "
                            cells[MARKET_COL_INDICES["yrs_profitable"]] = f" {m['yrs_profitable']} "
                            cells[MARKET_COL_INDICES["rev_yoy"]]        = f" {m['rev_yoy']} "
                            cells[MARKET_COL_INDICES["fcf_yoy"]]        = f" {m['fcf_yoy']} "
                            cells[MARKET_COL_INDICES["op_margin"]]      = f" {m['op_margin']} "
                            cells[MARKET_COL_INDICES["debt_ocf"]]       = f" {m['debt_ocf']} "
                            cells[MARKET_COL_INDICES["next_earnings"]]  = f" {m['next_earnings']} "

                            # Auto-update LOSER — EPS+ sub-tag:
                            # Apply when EPS YoY > 0 and vs_1Y < 0; strip otherwise.
                            tag = cells[2].strip()
                            if tag.startswith("LOSER"):
                                raw_eps_yoy = m.get("_eps_yoy_raw")
                                raw_vs_1y   = m.get("_vs_1y_raw")
                                base_tag = tag.replace(" — EPS+", "").strip()
                                if raw_eps_yoy is not None and raw_vs_1y is not None:
                                    if raw_eps_yoy > 0 and raw_vs_1y < 0:
                                        cells[2] = f" {base_tag} — EPS+ "
                                    else:
                                        cells[2] = f" {base_tag} "

                        elif current_section == "TRADE":
                            cells[TRADE_COL_INDICES["price"]]           = f" {m['price']} "
                            cells[TRADE_COL_INDICES["vs_1y"]]           = f" {m['vs_1y']} "
                            cells[TRADE_COL_INDICES["pe"]]              = f" {m['pe']} "
                            cells[TRADE_COL_INDICES["avg_eps_qoq_4q"]]  = f" {m['avg_eps_qoq_4q']} "
                            cells[TRADE_COL_INDICES["eps_yoy"]]         = f" {m['eps_yoy']} "
                            cells[TRADE_COL_INDICES["rev_yoy"]]         = f" {m['rev_yoy']} "
                            cells[TRADE_COL_INDICES["next_earnings"]]   = f" {m['next_earnings']} "

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

        # --- Price data (vs_1Y; also provides current_price for P/E) ---
        time.sleep(API_CALL_DELAY)
        daily_prices = fetch_prices(ticker)
        price_metrics = compute_price_metrics(ticker, daily_prices) if daily_prices else None

        if price_metrics:
            data_dir = get_data_directory(ticker)
            ensure_directory_exists(data_dir)
            save_json(price_metrics, os.path.join(data_dir, f"{ticker}_price.json"))

        # --- Income statement: P/E, Avg EPS QoQ (4Q), EPS YoY, Rev YoY, Op Margin %, Yrs Profitable ---
        time.sleep(API_CALL_DELAY)
        income_data = fetch_income_statement(ticker)
        gaap_pe = compute_gaap_pe(
            income_data,
            price_metrics["current_price"] if price_metrics else None,
        )
        quarterly = compute_quarterly_metrics(income_data) if income_data else {
            "avg_eps_qoq_4q": None, "eps_yoy": None, "rev_yoy": None, "op_margin_ttm": None,
        }
        yrs_profitable = compute_yrs_profitable(income_data) if income_data else None

        # --- Cash flow statement: FCF YoY, OCF TTM (for Debt/OCF) ---
        time.sleep(API_CALL_DELAY)
        cashflow_data = fetch_cashflow_statement(ticker)
        cashflow = compute_cashflow_metrics(cashflow_data) if cashflow_data else {
            "fcf_yoy": None, "ocf_ttm": None,
        }

        # --- Balance sheet: total debt (for Debt/OCF) ---
        time.sleep(API_CALL_DELAY)
        balance_data = fetch_balance_sheet(ticker)
        debt_ocf = compute_debt_ocf(balance_data, cashflow.get("ocf_ttm"))

        # --- Earnings history: next earnings date ---
        time.sleep(API_CALL_DELAY)
        earnings_history = fetch_earnings_history(ticker)
        next_earnings = extract_next_earnings(earnings_history)

        # --- Save combined financials JSON ---
        if income_data:
            save_json(
                {
                    **quarterly,
                    "gaap_pe": gaap_pe,
                    "yrs_profitable": yrs_profitable,
                    **cashflow,
                    "debt_ocf": debt_ocf,
                    "next_earnings": next_earnings,
                },
                os.path.join(get_data_directory(ticker), f"{ticker}_financials.json"),
            )

        # --- Format for tracker ---
        m = {
            "mkt_cap":          fmt_mktcap(mkt_cap),
            "price":            fmt_price(price_metrics["current_price"]) if price_metrics else "—",
            "vs_1y":            fmt_pct(price_metrics["vs_1y"]) if price_metrics else "—",
            "pe":               fmt_pe(gaap_pe),
            "avg_eps_qoq_4q":   fmt_pct(quarterly["avg_eps_qoq_4q"]),
            "eps_yoy":          fmt_pct(quarterly["eps_yoy"]),
            "yrs_profitable":   fmt_yrs(yrs_profitable),
            "rev_yoy":          fmt_pct(quarterly["rev_yoy"]),
            "fcf_yoy":          fmt_pct(cashflow["fcf_yoy"]),
            "op_margin":        fmt_margin(quarterly["op_margin_ttm"]),
            "debt_ocf":         fmt_ratio(debt_ocf),
            "next_earnings":    next_earnings if next_earnings else "—",
            # Raw values for LOSER — EPS+ tag logic (not written to tracker columns)
            "_eps_yoy_raw":     quarterly["eps_yoy"],
            "_vs_1y_raw":       price_metrics["vs_1y"] if price_metrics else None,
        }
        ticker_metrics[ticker] = m

        print(
            f"  Cap: {m['mkt_cap']}  vs1Y: {m['vs_1y']}  P/E: {m['pe']}  "
            f"Avg EPS QoQ: {m['avg_eps_qoq_4q']}  EPS YoY: {m['eps_yoy']}  "
            f"Yrs Prof: {m['yrs_profitable']}  Rev YoY: {m['rev_yoy']}  "
            f"FCF YoY: {m['fcf_yoy']}  Op Margin: {m['op_margin']}  Debt/OCF: {m['debt_ocf']}"
        )

    print(f"\nWriting to {TRACKER_PATH}...")
    update_tracker(ticker_metrics)
    print("Done.")


if __name__ == "__main__":
    main()

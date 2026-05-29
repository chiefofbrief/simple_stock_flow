#!/usr/bin/env python3
"""
Tracker Update Script
=====================

Fetches market data for all tickers in the unified Ticker Tracker table
of Stock_Tracker.md and writes the metrics back in-place.

Metrics updated (all auto-computed columns):
  Mkt Cap | Spread | P/E Corr | Price | Price vs_1Y | Price vs_2Y |
  EPS TTM | EPS vs_1Y | EPS vs_2Y | EPS QoQ (4Q) | P/E | P/OE |
  ROIC | ROIC Δ1Y | ROIC Δ2Y | OCF/NI | FCF TTM | FCF vs_1Y | FCF vs_2Y |
  Rev TTM | Rev vs_1Y | Rev vs_2Y | Debt/OCF | Next Earn | Last Earn

Manual columns (read but never overwritten):
  Tag | Thesis | $/Dollar

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
API_CALL_DELAY = 2

TRACKER_PATH = "Stock_Tracker.md"

# Column indices (1-indexed in pipe-split) for the unified Ticker Tracker table.
# | Ticker | Tag | Mkt Cap | Spread | P/E Corr | Price | Price vs_1Y | Price vs_2Y |
# | EPS TTM | EPS vs_1Y | EPS vs_2Y | EPS QoQ (4Q) | P/E | P/OE |
# | ROIC | ROIC Δ1Y | ROIC Δ2Y | OCF/NI | FCF TTM | FCF vs_1Y | FCF vs_2Y |
# | Rev TTM | Rev vs_1Y | Rev vs_2Y | Debt/OCF | Next Earn | Thesis | $/Dollar |
#   1        2     3        4        5          6       7      8
#   9          10          11          12             13    14
#   15    16          17          18      19        20          21
#   22       23          24          25         26          27      28
MARKET_COL_INDICES = {
    "mkt_cap":        3,
    "spread":         4,
    "pe_corr":        5,
    "price":          6,
    "vs_1y":          7,
    "vs_2y":          8,
    "eps_ttm":        9,
    "eps_vs1y":       10,
    "eps_vs2y":       11,
    "avg_eps_qoq_4q": 12,
    "pe":             13,
    "poe":            14,
    "roic":           15,
    "roic_delta1y":   16,
    "roic_delta2y":   17,
    "ocf_ni":         18,
    "fcf_ttm":        19,
    "fcf_vs1y":       20,
    "fcf_vs2y":       21,
    "rev_ttm":        22,
    "rev_vs1y":       23,
    "rev_vs2y":       24,
    "debt_ocf":       25,
    "next_earn":      26,
    "last_earn":      27,
    # col 28 = Thesis   — manual, never overwritten
    # col 29 = $/Dollar — manual, never overwritten
}

# Trade Tracker column indices (unchanged from v1)
TRADE_COL_INDICES = {
    "price":          6,
    "vs_1y":          7,
    "pe":             8,
    "avg_eps_qoq_4q": 9,
    "eps_vs1y":       10,
    "rev_vs1y":       11,
    "next_earn":      12,
}


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _get(url, label, ticker):
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [{ticker}] [{label}] HTTP {r.status_code}")
            return None
        data = r.json()
        if isinstance(data, dict) and "error" in data:
            print(f"  [{ticker}] [{label}] API error: {data['error']}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"  [{ticker}] [{label}] Request error: {e}")
        return None


# ---------------------------------------------------------------------------
# Tracker parsing
# ---------------------------------------------------------------------------

def parse_tickers_from_tracker():
    """Read all unique tickers from Ticker Tracker and Trade Tracker sections."""
    tickers = []
    seen = set()

    with open(TRACKER_PATH, "r") as f:
        lines = f.readlines()

    current_section = None
    in_data = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# Ticker Tracker"):
            current_section = "TRACKER"
            in_data = False
            continue
        elif stripped.startswith("## Trade Tracker"):
            current_section = "TRADE"
            in_data = False
            continue
        elif stripped.startswith("## ") or stripped.startswith("# "):
            current_section = None
            in_data = False
            continue

        if current_section not in ("TRACKER", "TRADE"):
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
    url = f"{FMP_BASE}/profile?symbol={ticker}&apikey={FMP_API_KEY}"
    data = _get(url, "profile", ticker)
    return data[0] if isinstance(data, list) and data else None


def fetch_prices(ticker, years=3):
    """3 years of daily prices — enough for Price vs_2Y and 12-month P/E correlation."""
    from_date = (datetime.now() - timedelta(days=years * 365 + 30)).strftime("%Y-%m-%d")
    url = (
        f"{FMP_BASE}/historical-price-eod/dividend-adjusted"
        f"?symbol={ticker}&from={from_date}&apikey={FMP_API_KEY}"
    )
    data = _get(url, "prices", ticker)
    return data if isinstance(data, list) and data else None


def fetch_income(ticker, limit=12):
    """12 quarters — covers current TTM plus 2 years of historical comparisons."""
    url = (
        f"{FMP_BASE}/income-statement"
        f"?symbol={ticker}&period=quarter&limit={limit}&apikey={FMP_API_KEY}"
    )
    data = _get(url, "income", ticker)
    return data if isinstance(data, list) else None


def fetch_cashflow(ticker, limit=12):
    """12 quarters — covers FCF TTM plus vs_1Y and vs_2Y comparisons."""
    url = (
        f"{FMP_BASE}/cash-flow-statement"
        f"?symbol={ticker}&period=quarter&limit={limit}&apikey={FMP_API_KEY}"
    )
    data = _get(url, "cashflow", ticker)
    return data if isinstance(data, list) else None


def fetch_balance(ticker, limit=12):
    """12 quarters — needed for ROIC Δ1Y and Δ2Y historical snapshots."""
    url = (
        f"{FMP_BASE}/balance-sheet-statement"
        f"?symbol={ticker}&period=quarter&limit={limit}&apikey={FMP_API_KEY}"
    )
    data = _get(url, "balance", ticker)
    return data if isinstance(data, list) else None


def fetch_earnings_history(ticker):
    url = f"{FMP_BASE}/earnings?symbol={ticker}&limit=10&apikey={FMP_API_KEY}"
    data = _get(url, "earnings", ticker)
    return data if isinstance(data, list) else None


# ---------------------------------------------------------------------------
# Price metrics
# ---------------------------------------------------------------------------

def compute_price_metrics(daily_prices):
    """Current price, vs_1Y, Price vs_2Y. Returns sorted price list for P/E corr reuse."""
    if not daily_prices or len(daily_prices) < 30:
        return None

    sorted_prices = sorted(daily_prices, key=lambda p: p["date"])
    current = sorted_prices[-1]["adjClose"]
    now = datetime.now()

    def vs(days):
        target = (now - timedelta(days=days)).strftime("%Y-%m-%d")
        candidates = [p for p in sorted_prices if p["date"] <= target]
        if candidates and candidates[-1]["adjClose"] > 0:
            return (current - candidates[-1]["adjClose"]) / candidates[-1]["adjClose"]
        return None

    return {
        "price":         current,
        "vs_1y":         vs(365),
        "vs_2y":         vs(730),
        "sorted_prices": sorted_prices,
    }


# ---------------------------------------------------------------------------
# Earnings metrics
# ---------------------------------------------------------------------------

def compute_eps_metrics(income_data):
    """EPS TTM, vs_1Y, vs_2Y, Avg EPS QoQ (4Q). Uses epsDiluted throughout."""
    if not income_data or len(income_data) < 4:
        return {"eps_ttm": None, "eps_vs1y": None, "eps_vs2y": None, "avg_eps_qoq": None}

    eps0    = safe_float(income_data[0].get("epsDiluted"))
    eps_ttm = sum((safe_float(income_data[i].get("epsDiluted")) or 0) for i in range(4))

    eps_vs1y = None
    if len(income_data) > 4:
        eps4 = safe_float(income_data[4].get("epsDiluted"))
        if eps0 is not None and eps4 is not None and eps4 != 0:
            eps_vs1y = (eps0 - eps4) / abs(eps4)

    eps_vs2y = None
    if len(income_data) > 8:
        eps8 = safe_float(income_data[8].get("epsDiluted"))
        if eps0 is not None and eps8 is not None and eps8 != 0:
            eps_vs2y = (eps0 - eps8) / abs(eps8)

    qoq_vals = []
    for i in range(4):
        if i + 1 >= len(income_data):
            break
        e_cur  = safe_float(income_data[i].get("epsDiluted"))
        e_prev = safe_float(income_data[i + 1].get("epsDiluted"))
        if e_cur is not None and e_prev is not None and e_prev != 0:
            qoq_vals.append((e_cur - e_prev) / abs(e_prev))
    avg_qoq = sum(qoq_vals) / len(qoq_vals) if qoq_vals else None

    return {
        "eps_ttm":     eps_ttm,
        "eps_vs1y":    eps_vs1y,
        "eps_vs2y":    eps_vs2y,
        "avg_eps_qoq": avg_qoq,
    }


# ---------------------------------------------------------------------------
# Revenue metrics
# ---------------------------------------------------------------------------

def compute_rev_metrics(income_data):
    """Revenue TTM, vs_1Y, vs_2Y."""
    if not income_data or len(income_data) < 4:
        return {"rev_ttm": None, "rev_vs1y": None, "rev_vs2y": None}

    rev_ttm = sum((safe_float(income_data[i].get("revenue")) or 0) for i in range(4))
    rev0    = safe_float(income_data[0].get("revenue"))

    rev_vs1y = None
    if len(income_data) > 4:
        rev4 = safe_float(income_data[4].get("revenue"))
        if rev0 is not None and rev4 is not None and rev4 > 0:
            rev_vs1y = (rev0 - rev4) / rev4

    rev_vs2y = None
    if len(income_data) > 8:
        rev8 = safe_float(income_data[8].get("revenue"))
        if rev0 is not None and rev8 is not None and rev8 > 0:
            rev_vs2y = (rev0 - rev8) / rev8

    return {"rev_ttm": rev_ttm, "rev_vs1y": rev_vs1y, "rev_vs2y": rev_vs2y}


# ---------------------------------------------------------------------------
# FCF / cash flow metrics
# ---------------------------------------------------------------------------

def compute_fcf_metrics(cashflow_data):
    """FCF TTM, vs_1Y, vs_2Y, OCF TTM, SBC TTM."""
    if not cashflow_data or len(cashflow_data) < 4:
        return {
            "fcf_ttm": None, "fcf_vs1y": None, "fcf_vs2y": None,
            "ocf_ttm": None, "sbc_ttm": None,
        }

    fcf_ttm = sum((safe_float(cashflow_data[i].get("freeCashFlow")) or 0) for i in range(4))
    ocf_ttm = sum((safe_float(cashflow_data[i].get("operatingCashFlow")) or 0) for i in range(4))
    sbc_ttm = sum((safe_float(cashflow_data[i].get("stockBasedCompensation")) or 0) for i in range(4))
    fcf0    = safe_float(cashflow_data[0].get("freeCashFlow"))

    fcf_vs1y = None
    if len(cashflow_data) > 4:
        fcf4 = safe_float(cashflow_data[4].get("freeCashFlow"))
        if fcf0 is not None and fcf4 is not None and fcf4 != 0:
            fcf_vs1y = (fcf0 - fcf4) / abs(fcf4)

    fcf_vs2y = None
    if len(cashflow_data) > 8:
        fcf8 = safe_float(cashflow_data[8].get("freeCashFlow"))
        if fcf0 is not None and fcf8 is not None and fcf8 != 0:
            fcf_vs2y = (fcf0 - fcf8) / abs(fcf8)

    return {
        "fcf_ttm":  fcf_ttm,
        "fcf_vs1y": fcf_vs1y,
        "fcf_vs2y": fcf_vs2y,
        "ocf_ttm":  ocf_ttm,
        "sbc_ttm":  sbc_ttm,
    }


# ---------------------------------------------------------------------------
# ROIC (current + Δ1Y + Δ2Y) — mirrors screen.py exactly
# ---------------------------------------------------------------------------

def _roic_at(income_slice, balance_row):
    if not income_slice or len(income_slice) < 4 or not balance_row:
        return None

    def sum4(key):
        return sum((safe_float(income_slice[i].get(key)) or 0) for i in range(4))

    ni       = sum4("netIncome")
    interest = sum4("interestExpense")
    pretax   = sum4("incomeBeforeTax")
    tax_exp  = sum4("incomeTaxExpense")

    if pretax == 0:
        return None
    tax_rate = tax_exp / pretax
    nopat    = ni + abs(interest) * (1 - tax_rate)

    equity = safe_float(balance_row.get("totalEquity"))
    debt   = safe_float(balance_row.get("totalDebt"))
    cash   = safe_float(balance_row.get("cashAndCashEquivalents")) or 0

    if equity is None or debt is None:
        return None
    invested_capital = equity + debt - cash
    if invested_capital <= 0:
        return None

    return nopat / invested_capital


def compute_roic_metrics(income_data, balance_data):
    """
    ROIC at current, 1Y ago, 2Y ago, and pp deltas.

    Income slices:  [0:4]  = current TTM
                    [4:8]  = TTM ending 1 year ago
                    [8:12] = TTM ending 2 years ago

    Balance sheets: [0]    = most recent quarter
                    [4]    = ~1 year ago
                    [8]    = ~2 years ago
    """
    roic_now = _roic_at(
        income_data[0:4]  if income_data else None,
        balance_data[0]   if balance_data else None,
    )
    roic_1y = _roic_at(
        income_data[4:8]  if income_data and len(income_data) >= 8 else None,
        balance_data[4]   if balance_data and len(balance_data) >= 5 else None,
    )
    roic_2y = _roic_at(
        income_data[8:12] if income_data and len(income_data) >= 12 else None,
        balance_data[8]   if balance_data and len(balance_data) >= 9 else None,
    )

    vs1y_pp = (roic_now - roic_1y) if (roic_now is not None and roic_1y is not None) else None
    vs2y_pp = (roic_now - roic_2y) if (roic_now is not None and roic_2y is not None) else None

    return {"roic": roic_now, "roic_vs1y_pp": vs1y_pp, "roic_vs2y_pp": vs2y_pp}


# ---------------------------------------------------------------------------
# Valuation
# ---------------------------------------------------------------------------

def compute_gaap_pe(income_data, price):
    """GAAP TTM P/E from last 4 quarters of diluted EPS."""
    if not income_data or not price or len(income_data) < 4:
        return None
    eps_ttm = sum((safe_float(income_data[i].get("epsDiluted")) or 0) for i in range(4))
    return price / eps_ttm if eps_ttm > 0 else None


def compute_poe(market_cap, fcf_ttm, sbc_ttm):
    """P/Owner Earnings = Market Cap / (FCF TTM - SBC TTM)."""
    if market_cap is None or fcf_ttm is None or sbc_ttm is None:
        return None
    owner_earnings = fcf_ttm - sbc_ttm
    if owner_earnings <= 0:
        return None
    return market_cap / owner_earnings


def compute_ocf_ni(ocf_ttm, income_data):
    """OCF/NI = TTM Operating Cash Flow / TTM Net Income."""
    if ocf_ttm is None or not income_data or len(income_data) < 4:
        return None
    ni_ttm = sum((safe_float(income_data[i].get("netIncome")) or 0) for i in range(4))
    if ni_ttm == 0:
        return None
    return ocf_ttm / ni_ttm


def compute_debt_ocf(balance_data, ocf_ttm):
    """Debt/OCF = Total Debt (most recent quarter) / OCF TTM."""
    if not balance_data or ocf_ttm is None or ocf_ttm <= 0:
        return None
    total_debt = safe_float(balance_data[0].get("totalDebt"))
    if total_debt is None:
        return None
    return total_debt / ocf_ttm


# ---------------------------------------------------------------------------
# P/E Correlation — mirrors screen.py exactly
# ---------------------------------------------------------------------------

def compute_pe_correlation(sorted_prices, income_data):
    """
    Pearson correlation between monthly price and TTM EPS over trailing 12 months.
    Requires at least 4 data points.
    """
    if not sorted_prices or not income_data or len(income_data) < 4:
        return None

    quarters = []
    for q in income_data:
        dt  = q.get("date") or q.get("period")
        eps = safe_float(q.get("epsDiluted"))
        if dt and eps is not None:
            quarters.append((dt, eps))
    quarters.sort(key=lambda x: x[0])

    def ttm_eps_at(date_str):
        available = [eps for dt, eps in quarters if dt <= date_str]
        return sum(available[-4:]) if len(available) >= 4 else None

    now = datetime.now()
    price_series, eps_series = [], []

    for month_offset in range(12):
        target = (now - timedelta(days=30 * month_offset)).strftime("%Y-%m-%d")
        candidates = [p for p in sorted_prices if p["date"] <= target]
        if not candidates:
            continue
        px  = candidates[-1]["adjClose"]
        ttm = ttm_eps_at(target)
        if ttm is not None and ttm > 0:
            price_series.append(px)
            eps_series.append(ttm)

    if len(price_series) < 4:
        return None

    try:
        return round(statistics.correlation(price_series, eps_series), 2)
    except statistics.StatisticsError:
        return None


# ---------------------------------------------------------------------------
# Next earnings
# ---------------------------------------------------------------------------

def extract_next_earnings(earnings_history):
    if not earnings_history:
        return None
    for h in earnings_history:
        act = safe_float(h.get("epsActual"))
        est = safe_float(h.get("epsEstimated"))
        if act is None and est is not None:
            return h.get("date")
    return None


def extract_last_earnings(earnings_history):
    """Most recent quarter where actual EPS was reported."""
    if not earnings_history:
        return None
    for h in earnings_history:
        act = safe_float(h.get("epsActual"))
        if act is not None:
            return h.get("date")
    return None


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

def fmt_eps(val):
    if val is None:
        return "—"
    return f"${val:.2f}" if val >= 0 else f"-${abs(val):.2f}"

def fmt_pct(val, sign=True):
    if val is None:
        return "—"
    return f"{val:+.1%}" if sign else f"{val:.1%}"

def fmt_pe(val):
    return f"{val:.1f}x" if val is not None else "—"

def fmt_dollars(val):
    if val is None:
        return "—"
    b = val / 1e9
    if abs(b) >= 1:
        return f"${b:.2f}B"
    m = val / 1e6
    return f"${m:.1f}M"

def fmt_pp(val):
    if val is None:
        return "—"
    return f"{val * 100:+.1f}pp"

def fmt_ratio(val):
    return f"{val:.1f}x" if val is not None else "—"

def fmt_corr(val):
    return f"{val:+.2f}" if val is not None else "—"


# ---------------------------------------------------------------------------
# Anomaly detection
# ---------------------------------------------------------------------------

def check_anomalies(ticker, m):
    flags = []
    pe       = m.get("_pe_raw")
    eps_vs1y = m.get("_eps_vs1y_raw")
    fcf_vs1y = m.get("_fcf_vs1y_raw")
    avg_qoq  = m.get("_avg_eps_qoq_raw")
    vs_1y    = m.get("_vs_1y_raw")
    debt_ocf = m.get("_debt_ocf_raw")

    if pe is not None and (pe < 2 or pe > 500):
        flags.append(f"  {ticker:<6}  P/E = {pe:.1f}x  (expected 2–500x)")
    if eps_vs1y is not None and (eps_vs1y < -5.0 or eps_vs1y > 20.0):
        flags.append(f"  {ticker:<6}  EPS vs_1Y = {eps_vs1y:+.1%}  (expected -500% to +2000%)")
    if fcf_vs1y is not None and (fcf_vs1y < -10.0 or fcf_vs1y > 50.0):
        flags.append(f"  {ticker:<6}  FCF vs_1Y = {fcf_vs1y:+.1%}  (expected -1000% to +5000%)")
    if avg_qoq is not None and (avg_qoq < -5.0 or avg_qoq > 20.0):
        flags.append(f"  {ticker:<6}  Avg EPS QoQ = {avg_qoq:+.1%}  (expected -500% to +2000%)")
    if vs_1y is not None and vs_1y > 10.0:
        flags.append(f"  {ticker:<6}  vs_1Y = {vs_1y:+.1%}  (expected < +1000%)")
    if debt_ocf is not None and debt_ocf > 20.0:
        flags.append(f"  {ticker:<6}  Debt/OCF = {debt_ocf:.1f}x  (expected < 20x)")

    return flags


# ---------------------------------------------------------------------------
# Tracker update
# ---------------------------------------------------------------------------

def update_tracker(ticker_metrics):
    """Write computed metrics back into the tracker file in-place."""
    with open(TRACKER_PATH, "r") as f:
        lines = f.readlines()

    current_section = None
    in_data = False
    new_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# Ticker Tracker"):
            current_section = "TRACKER"
            in_data = False
        elif stripped.startswith("## Trade Tracker"):
            current_section = "TRADE"
            in_data = False
        elif stripped.startswith("## ") or stripped.startswith("# "):
            current_section = None
            in_data = False

        if current_section in ("TRACKER", "TRADE") and stripped.startswith("|"):
            cells = line.split("|")
            if len(cells) >= 3:
                ticker_cell = cells[1].strip()

                if ticker_cell == "Ticker":
                    in_data = True
                elif in_data and ticker_cell and not ticker_cell.replace("-", "").replace(":", "").strip() == "":
                    if ticker_cell in ticker_metrics:
                        m = ticker_metrics[ticker_cell]

                        if current_section == "TRACKER":
                            cells[MARKET_COL_INDICES["mkt_cap"]]        = f" {m['mkt_cap']} "
                            cells[MARKET_COL_INDICES["spread"]]         = f" {m['spread']} "
                            cells[MARKET_COL_INDICES["pe_corr"]]        = f" {m['pe_corr']} "
                            cells[MARKET_COL_INDICES["price"]]          = f" {m['price']} "
                            cells[MARKET_COL_INDICES["vs_1y"]]          = f" {m['vs_1y']} "
                            cells[MARKET_COL_INDICES["vs_2y"]]          = f" {m['vs_2y']} "
                            cells[MARKET_COL_INDICES["eps_ttm"]]        = f" {m['eps_ttm']} "
                            cells[MARKET_COL_INDICES["eps_vs1y"]]       = f" {m['eps_vs1y']} "
                            cells[MARKET_COL_INDICES["eps_vs2y"]]       = f" {m['eps_vs2y']} "
                            cells[MARKET_COL_INDICES["avg_eps_qoq_4q"]] = f" {m['avg_eps_qoq_4q']} "
                            cells[MARKET_COL_INDICES["pe"]]             = f" {m['pe']} "
                            cells[MARKET_COL_INDICES["poe"]]            = f" {m['poe']} "
                            cells[MARKET_COL_INDICES["roic"]]           = f" {m['roic']} "
                            cells[MARKET_COL_INDICES["roic_delta1y"]]   = f" {m['roic_delta1y']} "
                            cells[MARKET_COL_INDICES["roic_delta2y"]]   = f" {m['roic_delta2y']} "
                            cells[MARKET_COL_INDICES["ocf_ni"]]         = f" {m['ocf_ni']} "
                            cells[MARKET_COL_INDICES["fcf_ttm"]]        = f" {m['fcf_ttm']} "
                            cells[MARKET_COL_INDICES["fcf_vs1y"]]       = f" {m['fcf_vs1y']} "
                            cells[MARKET_COL_INDICES["fcf_vs2y"]]       = f" {m['fcf_vs2y']} "
                            cells[MARKET_COL_INDICES["rev_ttm"]]        = f" {m['rev_ttm']} "
                            cells[MARKET_COL_INDICES["rev_vs1y"]]       = f" {m['rev_vs1y']} "
                            cells[MARKET_COL_INDICES["rev_vs2y"]]       = f" {m['rev_vs2y']} "
                            cells[MARKET_COL_INDICES["debt_ocf"]]       = f" {m['debt_ocf']} "
                            cells[MARKET_COL_INDICES["next_earn"]]      = f" {m['next_earn']} "
                            cells[MARKET_COL_INDICES["last_earn"]]      = f" {m['last_earn']} "

                            # Auto-update LOSER — EPS+ sub-tag
                            tag = cells[2].strip()
                            if tag.startswith("LOSER"):
                                raw_eps_vs1y = m.get("_eps_vs1y_raw")
                                raw_vs_1y    = m.get("_vs_1y_raw")
                                base_tag = tag.replace(" — EPS+", "").strip()
                                if raw_eps_vs1y is not None and raw_vs_1y is not None:
                                    if raw_eps_vs1y > 0 and raw_vs_1y < 0:
                                        cells[2] = f" {base_tag} — EPS+ "
                                    else:
                                        cells[2] = f" {base_tag} "

                        elif current_section == "TRADE":
                            cells[TRADE_COL_INDICES["price"]]          = f" {m['price']} "
                            cells[TRADE_COL_INDICES["vs_1y"]]          = f" {m['vs_1y']} "
                            cells[TRADE_COL_INDICES["pe"]]             = f" {m['pe']} "
                            cells[TRADE_COL_INDICES["avg_eps_qoq_4q"]] = f" {m['avg_eps_qoq_4q']} "
                            cells[TRADE_COL_INDICES["eps_vs1y"]]       = f" {m['eps_vs1y']} "
                            cells[TRADE_COL_INDICES["rev_vs1y"]]       = f" {m['rev_vs1y']} "
                            cells[TRADE_COL_INDICES["next_earn"]]      = f" {m['next_earn']} "

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
        print("Error: FMP_API_KEY environment variable not set.")
        sys.exit(1)

    tickers = [t.upper() for t in args.tickers] if args.tickers else parse_tickers_from_tracker()

    if not tickers:
        print("No tickers found in tracker.")
        sys.exit(1)

    print(f"Updating {len(tickers)} ticker(s): {', '.join(tickers)}\n")

    ticker_metrics = {}
    all_anomalies  = []

    for i, ticker in enumerate(tickers):
        print(f"[{i + 1}/{len(tickers)}] {ticker}  ", end="", flush=True)

        if i > 0:
            time.sleep(API_CALL_DELAY)
        profile    = fetch_profile(ticker)
        market_cap = safe_float(profile.get("marketCap")) if profile else None

        time.sleep(API_CALL_DELAY)
        daily_prices = fetch_prices(ticker, years=3)
        price_m      = compute_price_metrics(daily_prices) if daily_prices else None

        if price_m:
            data_dir = get_data_directory(ticker)
            ensure_directory_exists(data_dir)
            save_json(
                {"ticker": ticker, "current_price": price_m["price"], "vs_1y": price_m["vs_1y"]},
                os.path.join(data_dir, f"{ticker}_price.json"),
            )

        time.sleep(API_CALL_DELAY)
        income_data = fetch_income(ticker, limit=12)

        time.sleep(API_CALL_DELAY)
        cashflow_data = fetch_cashflow(ticker, limit=12)

        time.sleep(API_CALL_DELAY)
        balance_data = fetch_balance(ticker, limit=12)

        time.sleep(API_CALL_DELAY)
        earnings_history = fetch_earnings_history(ticker)

        print("done.")

        # --- Compute ---
        price         = price_m["price"]         if price_m else None
        vs_1y         = price_m["vs_1y"]         if price_m else None
        vs_2y         = price_m["vs_2y"]         if price_m else None
        sorted_prices = price_m["sorted_prices"] if price_m else None

        eps_m  = compute_eps_metrics(income_data)
        rev_m  = compute_rev_metrics(income_data)
        fcf_m  = compute_fcf_metrics(cashflow_data)
        roic_m = compute_roic_metrics(income_data, balance_data)

        pe       = compute_gaap_pe(income_data, price)
        poe      = compute_poe(market_cap, fcf_m["fcf_ttm"], fcf_m["sbc_ttm"])
        ocf_ni   = compute_ocf_ni(fcf_m["ocf_ttm"], income_data)
        debt_ocf = compute_debt_ocf(balance_data, fcf_m["ocf_ttm"])
        corr     = compute_pe_correlation(sorted_prices, income_data) if sorted_prices else None

        spread = None
        if vs_1y is not None and eps_m["eps_vs1y"] is not None:
            spread = vs_1y - eps_m["eps_vs1y"]

        next_earn = extract_next_earnings(earnings_history)
        last_earn = extract_last_earnings(earnings_history)

        # --- Format ---
        m = {
            "mkt_cap":        fmt_mktcap(market_cap),
            "spread":         fmt_pct(spread),
            "pe_corr":        fmt_corr(corr),
            "price":          fmt_price(price),
            "vs_1y":          fmt_pct(vs_1y),
            "vs_2y":          fmt_pct(vs_2y),
            "eps_ttm":        fmt_eps(eps_m["eps_ttm"]),
            "eps_vs1y":       fmt_pct(eps_m["eps_vs1y"]),
            "eps_vs2y":       fmt_pct(eps_m["eps_vs2y"]),
            "avg_eps_qoq_4q": fmt_pct(eps_m["avg_eps_qoq"]),
            "pe":             fmt_pe(pe),
            "poe":            fmt_pe(poe),
            "roic":           fmt_pct(roic_m["roic"], sign=False),
            "roic_delta1y":   fmt_pp(roic_m["roic_vs1y_pp"]),
            "roic_delta2y":   fmt_pp(roic_m["roic_vs2y_pp"]),
            "ocf_ni":         fmt_ratio(ocf_ni),
            "fcf_ttm":        fmt_dollars(fcf_m["fcf_ttm"]),
            "fcf_vs1y":       fmt_pct(fcf_m["fcf_vs1y"]),
            "fcf_vs2y":       fmt_pct(fcf_m["fcf_vs2y"]),
            "rev_ttm":        fmt_dollars(rev_m["rev_ttm"]),
            "rev_vs1y":       fmt_pct(rev_m["rev_vs1y"]),
            "rev_vs2y":       fmt_pct(rev_m["rev_vs2y"]),
            "debt_ocf":       fmt_ratio(debt_ocf),
            "next_earn":      next_earn if next_earn else "—",
            "last_earn":      last_earn if last_earn else "—",
            # Raw values for tag logic and anomaly detection
            "_vs_1y_raw":       vs_1y,
            "_pe_raw":          pe,
            "_eps_vs1y_raw":    eps_m["eps_vs1y"],
            "_avg_eps_qoq_raw": eps_m["avg_eps_qoq"],
            "_fcf_vs1y_raw":    fcf_m["fcf_vs1y"],
            "_debt_ocf_raw":    debt_ocf,
        }
        ticker_metrics[ticker] = m

        print(
            f"  Cap: {m['mkt_cap']}  Spread: {m['spread']}  P/E: {m['pe']}  "
            f"ROIC: {m['roic']}  EPS vs1Y: {m['eps_vs1y']}  Debt/OCF: {m['debt_ocf']}"
        )

        anomalies = check_anomalies(ticker, m)
        all_anomalies.extend(anomalies)

    print(f"\nWriting to {TRACKER_PATH}...")
    update_tracker(ticker_metrics)

    if all_anomalies:
        print("\n⚠  Data anomalies detected — manual audit recommended:")
        for flag in all_anomalies:
            print(flag)
    else:
        print("No data anomalies detected.")

    print("\nDone.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Screen Script
=============

Fetches all screening metrics for a list of arbitrary tickers and produces
a structured screening summary for use with Prompts/prompt_screen.md.

Metrics produced:
  Signal    — Spread (Price vs_1Y minus EPS vs_1Y), P/E Correlation 1Y
  Size      — Mkt Cap
  Price     — Current price, vs_1Y, vs_2Y
  Earnings  — EPS TTM, EPS vs_1Y, EPS vs_2Y, Avg EPS QoQ (4Q)
  Valuation — P/E (GAAP TTM), P/Owner Earnings (FCF TTM - SBC TTM)
  Quality   — ROIC, ROIC vs_1Y (pp), ROIC vs_2Y (pp),
               OCF/NI, FCF TTM, FCF vs_1Y, FCF vs_2Y,
               Revenue TTM, Rev vs_1Y, Rev vs_2Y,
               Debt/OCF

Usage:
    python Scripts/screen.py PLTR SMCI ARM RDDT

Output:
    Data/screening/Screen_{DATE}.txt
"""

import sys
import os
import argparse
import statistics
import requests
import time
from datetime import datetime, timedelta

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 2


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
# FMP fetching
# ---------------------------------------------------------------------------

def fetch_profile(ticker):
    url = f"{FMP_BASE}/profile?symbol={ticker}&apikey={FMP_API_KEY}"
    data = _get(url, "profile", ticker)
    return data[0] if isinstance(data, list) and data else None


def fetch_prices(ticker, years=3):
    """3 years of daily prices — enough for vs_2Y and 12-month correlation."""
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
    """12 quarters — index [0] = current, [4] = 1Y ago, [8] = 2Y ago for ROIC history."""
    url = (
        f"{FMP_BASE}/balance-sheet-statement"
        f"?symbol={ticker}&period=quarter&limit={limit}&apikey={FMP_API_KEY}"
    )
    data = _get(url, "balance", ticker)
    return data if isinstance(data, list) else None


# ---------------------------------------------------------------------------
# Price metrics
# ---------------------------------------------------------------------------

def compute_price_metrics(daily_prices):
    """Current price, vs_1Y, vs_2Y. Returns sorted price list for reuse in correlation."""
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

    eps0   = safe_float(income_data[0].get("epsDiluted"))
    eps_ttm = sum((safe_float(income_data[i].get("epsDiluted")) or 0) for i in range(4))

    # YoY: most recent quarter vs same quarter 1 year ago (index 4)
    eps_vs1y = None
    if len(income_data) > 4:
        eps4 = safe_float(income_data[4].get("epsDiluted"))
        if eps0 is not None and eps4 is not None and eps4 != 0:
            eps_vs1y = (eps0 - eps4) / abs(eps4)

    # 2Y: most recent quarter vs same quarter 2 years ago (index 8)
    eps_vs2y = None
    if len(income_data) > 8:
        eps8 = safe_float(income_data[8].get("epsDiluted"))
        if eps0 is not None and eps8 is not None and eps8 != 0:
            eps_vs2y = (eps0 - eps8) / abs(eps8)

    # Avg QoQ: average of 4 most recent quarter-over-quarter EPS changes
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
        "eps_ttm":    eps_ttm,
        "eps_vs1y":   eps_vs1y,
        "eps_vs2y":   eps_vs2y,
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
# ROIC (current + 1Y ago + 2Y ago)
# ---------------------------------------------------------------------------

def _roic_at(income_slice, balance_row):
    """
    ROIC for a 4-quarter income slice paired with a balance sheet snapshot.
    Mirrors the computation in tracker_update.py for consistency.
    """
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
    tax_rate     = tax_exp / pretax
    nopat        = ni + abs(interest) * (1 - tax_rate)

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
    ROIC at current, 1Y ago, and 2Y ago, expressed as % and pp deltas.

    Income slices:  [0:4]  = current TTM
                    [4:8]  = TTM ending 1 year ago
                    [8:12] = TTM ending 2 years ago

    Balance sheets: [0]    = most recent quarter (current)
                    [4]    = ~1 year ago
                    [8]    = ~2 years ago
    """
    roic_now = _roic_at(
        income_data[0:4]   if income_data else None,
        balance_data[0]    if balance_data else None,
    )
    roic_1y = _roic_at(
        income_data[4:8]   if income_data and len(income_data) >= 8 else None,
        balance_data[4]    if balance_data and len(balance_data) >= 5 else None,
    )
    roic_2y = _roic_at(
        income_data[8:12]  if income_data and len(income_data) >= 12 else None,
        balance_data[8]    if balance_data and len(balance_data) >= 9 else None,
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
    if not balance_data or ocf_ttm is None or ocf_ttm == 0:
        return None
    total_debt = safe_float(balance_data[0].get("totalDebt"))
    if total_debt is None:
        return None
    return total_debt / ocf_ttm


# ---------------------------------------------------------------------------
# P/E Correlation
# ---------------------------------------------------------------------------

def compute_pe_correlation(sorted_prices, income_data):
    """
    Pearson correlation between monthly price and TTM EPS over trailing 12 months.

    Samples one price per month (most recent available on or before target date).
    For each price sample, computes the TTM EPS from the 4 most recent quarterly
    earnings reports available at that date. Requires at least 4 data points.
    """
    if not sorted_prices or not income_data or len(income_data) < 4:
        return None

    # Build quarter-date → EPS list, sorted oldest-first for TTM lookup
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
# Formatting
# ---------------------------------------------------------------------------

def fmt_price(val):
    if val is None:
        return "—"
    return f"${val:.2f}"

def fmt_eps(val):
    if val is None:
        return "—"
    return f"${val:.2f}" if val >= 0 else f"-${abs(val):.2f}"

def fmt_pct(val):
    return f"{val:+.1%}" if val is not None else "—"

def fmt_pct_plain(val):
    return f"{val:.1%}" if val is not None else "—"

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
    """ROIC delta in percentage points, e.g. +3.1pp."""
    if val is None:
        return "—"
    return f"{val * 100:+.1f}pp"

def fmt_ratio(val):
    return f"{val:.2f}x" if val is not None else "—"

def fmt_corr(val):
    return f"{val:+.2f}" if val is not None else "—"

def fmt_mktcap(val):
    if val is None:
        return "—"
    b = val / 1e9
    if b >= 1000:
        return f"${b/1000:.2f}T"
    return f"${b:.1f}B"


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

BLOCK_WIDTH = 46

def fmt_row(label, value):
    return f"  {label:<28}{value}"

def format_ticker_block(ticker, m):
    sep   = "═" * BLOCK_WIDTH
    ruled = lambda s: f"  ── {s} {'─' * (BLOCK_WIDTH - len(s) - 6)}"
    lines = [
        sep,
        ticker,
        "",
        ruled("SIGNAL"),
        fmt_row("Spread (Price−EPS 1Y)", m["spread"]),
        fmt_row("P/E Correlation 1Y",    m["corr_1y"]),
        fmt_row("Mkt Cap",               m["mkt_cap"]),
        "",
        ruled("PRICE"),
        fmt_row("Price",  m["price"]),
        fmt_row("vs_1Y",  m["vs_1y"]),
        fmt_row("vs_2Y",  m["vs_2y"]),
        "",
        ruled("EARNINGS"),
        fmt_row("EPS (TTM)",        m["eps_ttm"]),
        fmt_row("EPS vs_1Y",        m["eps_vs1y"]),
        fmt_row("EPS vs_2Y",        m["eps_vs2y"]),
        fmt_row("Avg EPS QoQ (4Q)", m["avg_eps_qoq"]),
        "",
        ruled("VALUATION"),
        fmt_row("P/E (GAAP TTM)",   m["pe"]),
        fmt_row("P/Owner Earnings", m["poe"]),
        "",
        ruled("QUALITY"),
        fmt_row("ROIC",             m["roic"]),
        fmt_row("ROIC vs_1Y",       m["roic_vs1y_pp"]),
        fmt_row("ROIC vs_2Y",       m["roic_vs2y_pp"]),
        fmt_row("OCF/NI",           m["ocf_ni"]),
        fmt_row("FCF (TTM)",        m["fcf_ttm"]),
        fmt_row("FCF vs_1Y",        m["fcf_vs1y"]),
        fmt_row("FCF vs_2Y",        m["fcf_vs2y"]),
        fmt_row("Revenue (TTM)",    m["rev_ttm"]),
        fmt_row("Rev vs_1Y",        m["rev_vs1y"]),
        fmt_row("Rev vs_2Y",        m["rev_vs2y"]),
        fmt_row("Debt/OCF",         m["debt_ocf"]),
        "",
    ]
    return "\n".join(lines)


def write_screening_file(tickers, blocks, out_dir):
    today   = datetime.now().strftime("%Y-%m-%d")
    out_path = os.path.join(out_dir, f"Screen_{today}.txt")

    header_lines = [
        f"SCREEN — {today}",
        f"Tickers: {', '.join(tickers)}",
        f"Script:  Scripts/screen.py",
        f"Prompt:  Prompts/prompt_screen.md",
        "",
        "All percentages are point-in-time comparisons (most recent quarter vs.",
        "same quarter 1 or 2 years ago). ROIC deltas are in percentage points (pp).",
        "P/Owner Earnings = Market Cap / (FCF TTM - SBC TTM).",
        "Spread = Price vs_1Y minus EPS vs_1Y.",
        "Debt/OCF = Total Debt (most recent quarter) / OCF TTM.",
        "",
    ]

    with open(out_path, "w") as f:
        f.write("\n".join(header_lines))
        f.write("\n")
        f.write("\n".join(blocks))

    return out_path


# ---------------------------------------------------------------------------
# Per-ticker orchestration
# ---------------------------------------------------------------------------

def process_ticker(ticker):
    """Fetch all data and compute all metrics for one ticker."""
    print(f"  profile...", end=" ", flush=True)
    time.sleep(API_CALL_DELAY)
    profile    = fetch_profile(ticker)
    market_cap = safe_float(profile.get("marketCap")) if profile else None

    print(f"prices...", end=" ", flush=True)
    time.sleep(API_CALL_DELAY)
    daily_prices = fetch_prices(ticker, years=3)
    price_m      = compute_price_metrics(daily_prices) if daily_prices else None

    print(f"income...", end=" ", flush=True)
    time.sleep(API_CALL_DELAY)
    income_data = fetch_income(ticker, limit=12)

    print(f"cashflow...", end=" ", flush=True)
    time.sleep(API_CALL_DELAY)
    cashflow_data = fetch_cashflow(ticker, limit=12)

    print(f"balance...", end=" ", flush=True)
    time.sleep(API_CALL_DELAY)
    balance_data = fetch_balance(ticker, limit=12)

    print("done.")

    # --- Compute ---
    price        = price_m["price"]         if price_m else None
    vs_1y        = price_m["vs_1y"]         if price_m else None
    vs_2y        = price_m["vs_2y"]         if price_m else None
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

    # Spread = Price vs_1Y - EPS vs_1Y (negative = earnings outpacing price = good signal)
    # Matches tracker convention: ≤ 0% is the compelling signal.
    spread = None
    if eps_m["eps_vs1y"] is not None and vs_1y is not None:
        spread = vs_1y - eps_m["eps_vs1y"]

    # --- Format ---
    return {
        "spread":        fmt_pct(spread),
        "corr_1y":       fmt_corr(corr),
        "mkt_cap":       fmt_mktcap(market_cap),
        "price":         fmt_price(price),
        "vs_1y":         fmt_pct(vs_1y),
        "vs_2y":         fmt_pct(vs_2y),
        "eps_ttm":       fmt_eps(eps_m["eps_ttm"]),
        "eps_vs1y":      fmt_pct(eps_m["eps_vs1y"]),
        "eps_vs2y":      fmt_pct(eps_m["eps_vs2y"]),
        "avg_eps_qoq":   fmt_pct(eps_m["avg_eps_qoq"]),
        "pe":            fmt_pe(pe),
        "poe":           fmt_pe(poe),
        "roic":          fmt_pct_plain(roic_m["roic"]),
        "roic_vs1y_pp":  fmt_pp(roic_m["roic_vs1y_pp"]),
        "roic_vs2y_pp":  fmt_pp(roic_m["roic_vs2y_pp"]),
        "ocf_ni":        fmt_ratio(ocf_ni),
        "fcf_ttm":       fmt_dollars(fcf_m["fcf_ttm"]),
        "fcf_vs1y":      fmt_pct(fcf_m["fcf_vs1y"]),
        "fcf_vs2y":      fmt_pct(fcf_m["fcf_vs2y"]),
        "rev_ttm":       fmt_dollars(rev_m["rev_ttm"]),
        "rev_vs1y":      fmt_pct(rev_m["rev_vs1y"]),
        "rev_vs2y":      fmt_pct(rev_m["rev_vs2y"]),
        "debt_ocf":      fmt_ratio(debt_ocf),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Screen arbitrary tickers before tracker addition."
    )
    parser.add_argument(
        "tickers",
        nargs="+",
        help="Tickers to screen (e.g. PLTR SMCI ARM)",
    )
    args = parser.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set.")
        sys.exit(1)

    tickers = [t.upper() for t in args.tickers]
    print(f"Screening {len(tickers)} ticker(s): {', '.join(tickers)}\n")

    out_dir = "Data/screening"
    os.makedirs(out_dir, exist_ok=True)

    blocks       = []
    failed       = []

    for i, ticker in enumerate(tickers):
        print(f"[{i + 1}/{len(tickers)}] {ticker}  ", end="", flush=True)
        try:
            m     = process_ticker(ticker)
            block = format_ticker_block(ticker, m)
            blocks.append(block)
            print(f"         Spread: {m['spread']}  ROIC: {m['roic']}  P/E: {m['pe']}  P/OE: {m['poe']}  Debt/OCF: {m['debt_ocf']}")
        except Exception as e:
            print(f"\n  ERROR: {e}")
            blocks.append(f"{'═' * BLOCK_WIDTH}\n{ticker}\n  ERROR: {e}\n")
            failed.append(ticker)

    out_path = write_screening_file(tickers, blocks, out_dir)

    print(f"\nOutput: {out_path}")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    print(f"\nNext step: run Prompts/prompt_screen.md with the output above.")


if __name__ == "__main__":
    main()

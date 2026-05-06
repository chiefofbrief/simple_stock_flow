#!/usr/bin/env python3
"""
Price & Earnings Script
=======================

Fetches price history and earnings data for one or more tickers and produces
per-ticker JSON files plus a combined screening summary.

Replaces the separate price.py + earnings.py scripts. Price data is computed
first and passed in-memory to the earnings analysis — no disk dependency
between the two phases.

Metrics produced:
  Price   — vs_1yr–5yr, 52w position, CAGR, CV, z-score, max drawdown,
             upside-to-revert, 12-month trend
  Earnings — GAAP P/E, Adj P/E, P/E trend (1/3/5yr), price-earnings
             correlation, EPS CAGR, beat/miss history, forward estimate

Usage:
    python Scripts/price_earnings.py ADBE NOW
    python Scripts/price_earnings.py --category losers
    python Scripts/price_earnings.py --all

Output (per ticker):
    Data/tickers/{TICKER}/raw/{TICKER}_price.json
    Data/tickers/{TICKER}/raw/{TICKER}_earnings.json

Output (batch):
    Data/screening/Price_Earnings_{DATE}.txt
"""

import sys
import os
import re
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
    parse_tickers_from_tracker,
)

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 2


# ---------------------------------------------------------------------------
# FMP fetching
# ---------------------------------------------------------------------------

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


def fetch_prices(ticker):
    from_date = (datetime.now() - timedelta(days=5 * 365 + 30)).strftime("%Y-%m-%d")
    url = (
        f"{FMP_BASE}/historical-price-eod/dividend-adjusted"
        f"?symbol={ticker}&from={from_date}&apikey={FMP_API_KEY}"
    )
    data = _get(url, "price", ticker)
    if not data or not isinstance(data, list):
        return None
    return data


def fetch_earnings(ticker):
    url = f"{FMP_BASE}/earnings?symbol={ticker}&limit=40&apikey={FMP_API_KEY}"
    return _get(url, "earnings", ticker)


def fetch_income_statement(ticker):
    url = (
        f"{FMP_BASE}/income-statement"
        f"?symbol={ticker}&period=quarter&limit=8&apikey={FMP_API_KEY}"
    )
    data = _get(url, "income", ticker)
    return data if isinstance(data, list) else None


# ---------------------------------------------------------------------------
# Price metrics
# ---------------------------------------------------------------------------

def derive_monthly_closes(daily_prices):
    sorted_prices = sorted(daily_prices, key=lambda p: p["date"])
    monthly = {}
    for p in sorted_prices:
        monthly[p["date"][:7]] = (p["date"], p["adjClose"])
    return list(monthly.values())


def find_close_n_years_ago(monthly_closes, years):
    if not monthly_closes:
        return None
    target = datetime.strptime(monthly_closes[-1][0], "%Y-%m-%d") - timedelta(days=years * 365)
    best, best_diff = None, float("inf")
    for date_str, close in monthly_closes:
        diff = abs((datetime.strptime(date_str, "%Y-%m-%d") - target).days)
        if diff < best_diff:
            best_diff, best = diff, close
    return best if best_diff <= 75 else None


def compute_max_drawdown(sorted_daily):
    peak = sorted_daily[0]["adjClose"]
    max_dd = 0.0
    for p in sorted_daily:
        price = p["adjClose"]
        if price > peak:
            peak = price
        dd = (peak - price) / peak if peak > 0 else 0
        if dd > max_dd:
            max_dd = dd
    return max_dd


def linear_slope(values):
    n = len(values)
    if n < 2:
        return None
    x_mean = (n - 1) / 2.0
    y_mean = sum(values) / n
    num = sum((i - x_mean) * (v - y_mean) for i, v in enumerate(values))
    den = sum((i - x_mean) ** 2 for i in range(n))
    return num / den if den else None


def compute_price_metrics(ticker, daily_prices):
    sorted_daily = sorted(daily_prices, key=lambda p: p["date"])
    if len(sorted_daily) < 30:
        print(f"  [{ticker}] Only {len(sorted_daily)} days of price data — insufficient")
        return None

    current_price = sorted_daily[-1]["adjClose"]
    current_date = sorted_daily[-1]["date"]
    monthly_closes = derive_monthly_closes(daily_prices)

    if len(monthly_closes) < 2:
        print(f"  [{ticker}] Insufficient monthly price data")
        return None

    monthly_prices = [c for _, c in monthly_closes]

    vs_years = {}
    for y in [1, 2, 3, 4, 5]:
        old = find_close_n_years_ago(monthly_closes, y)
        vs_years[f"vs_{y}yr"] = (current_price - old) / old if old and old > 0 else None

    avg_5yr = statistics.mean(monthly_prices)
    price_vs_5yr_avg = (current_price - avg_5yr) / avg_5yr if avg_5yr > 0 else None

    one_year_ago = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    daily_1yr = [p for p in sorted_daily if p["date"] >= one_year_ago]
    if daily_1yr:
        high_52w = max(p["adjHigh"] for p in daily_1yr)
        low_52w = min(p["adjLow"] for p in daily_1yr)
        rng = high_52w - low_52w
        position_52w = (current_price - low_52w) / rng if rng > 0 else 0.5
    else:
        high_52w = low_52w = current_price
        position_52w = 0.5

    first_price = monthly_prices[0]
    years_span = len(monthly_prices) / 12.0
    cagr_5yr = (
        (current_price / first_price) ** (1.0 / years_span) - 1
        if first_price > 0 and current_price > 0 and years_span > 0
        else None
    )

    monthly_1yr = monthly_prices[-12:] if len(monthly_prices) >= 12 else monthly_prices
    avg_1yr = statistics.mean(monthly_1yr)
    upside_if_revert = (avg_1yr - current_price) / current_price if current_price > 0 else None

    monthly_returns = []
    for i in range(1, len(monthly_prices)):
        if monthly_prices[i - 1] > 0:
            monthly_returns.append(
                (monthly_prices[i] - monthly_prices[i - 1]) / monthly_prices[i - 1]
            )

    cv = (
        statistics.stdev(monthly_prices) / statistics.mean(monthly_prices)
        if len(monthly_prices) > 1 and statistics.mean(monthly_prices) > 0
        else None
    )

    if len(monthly_returns) >= 3:
        recent_return = monthly_returns[-1]
        mean_r = statistics.mean(monthly_returns)
        std_r = statistics.stdev(monthly_returns)
        z_score = (recent_return - mean_r) / std_r if std_r > 0 else 0
    else:
        z_score = None

    max_dd = compute_max_drawdown(sorted_daily)
    recent_1mo = monthly_returns[-1] if monthly_returns else 0
    drop_vs_max_dd = abs(recent_1mo) / max_dd if max_dd > 0 and recent_1mo < 0 else 0.0

    monthly_1yr_prices = monthly_prices[-12:] if len(monthly_prices) >= 12 else monthly_prices
    slope_1yr = linear_slope(monthly_1yr_prices)
    slope_5yr = linear_slope(monthly_prices)

    recent_12m = monthly_closes[-12:] if len(monthly_closes) >= 12 else monthly_closes
    start_idx = len(monthly_closes) - len(recent_12m)
    prev = monthly_closes[start_idx - 1][1] if start_idx > 0 else None
    recent_trend = []
    for date, close in recent_12m:
        delta = (close - prev) / prev if prev and prev > 0 else None
        recent_trend.append({"date": date, "close": close, "change_pct": delta})
        prev = close

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
            "recent_trend": recent_trend,
        },
    }


# ---------------------------------------------------------------------------
# Earnings metrics
# ---------------------------------------------------------------------------

def safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def compute_gaap_pe(income_data, current_price):
    if not income_data or not current_price:
        return None
    eps_vals = [safe_float(q.get("eps")) for q in income_data[:4]]
    eps_vals = [e for e in eps_vals if e is not None]
    if len(eps_vals) < 4:
        return None
    ttm_eps = sum(eps_vals)
    return current_price / ttm_eps if ttm_eps > 0 else None


def compute_earnings_metrics(ticker, history, price_data, gaap_pe=None):
    if not history:
        return None

    next_est = next_date = last_actual = None
    actual_quarters = []

    for h in history:
        act = safe_float(h.get("epsActual"))
        est = safe_float(h.get("epsEstimated"))
        dt = h.get("date")
        if act is None and est is not None and next_est is None:
            next_est, next_date = est, dt
        elif act is not None:
            if last_actual is None:
                last_actual = act
            actual_quarters.append({"date": dt, "actual": act, "estimated": est})

    if not actual_quarters:
        return None

    actual_quarters_sorted = sorted(actual_quarters, key=lambda x: x["date"])

    annual_eps = []
    for i in range(len(actual_quarters_sorted), 3, -4):
        chunk = actual_quarters_sorted[i - 4:i]
        ttm = sum(q["actual"] for q in chunk)
        annual_eps.append({"date": chunk[-1]["date"], "eps": ttm})

    cagr_5yr = None
    if len(annual_eps) >= 6:
        cagr_5yr = (annual_eps[0]["eps"] / annual_eps[5]["eps"]) ** (1 / 5) - 1 if annual_eps[5]["eps"] > 0 else None
    elif len(annual_eps) >= 2:
        years = len(annual_eps) - 1
        cagr_5yr = (annual_eps[0]["eps"] / annual_eps[-1]["eps"]) ** (1 / years) - 1 if annual_eps[-1]["eps"] > 0 else None

    stability_cv = None
    if len(annual_eps) > 1:
        vals = [x["eps"] for x in annual_eps[:5]]
        mean_eps = statistics.mean(vals)
        if mean_eps and abs(mean_eps) > 0.001:
            stability_cv = statistics.stdev(vals) / abs(mean_eps)

    ttm_eps = annual_eps[0]["eps"] if annual_eps else None
    curr_price = price_data["current_price"]
    curr_pe = curr_price / ttm_eps if ttm_eps and ttm_eps > 0 else None

    def past_pe(years_ago):
        pct = price_data["table_metrics"].get(f"vs_{years_ago}yr")
        if pct is None:
            return None
        past_price = curr_price / (1 + pct)
        if len(annual_eps) > years_ago:
            past_eps = annual_eps[years_ago]["eps"]
            if past_eps and past_eps > 0:
                return past_price / past_eps
        return None

    pe_1y, pe_3y, pe_5y = past_pe(1), past_pe(3), past_pe(5)
    pe_vals = [p for p in [curr_pe, pe_1y, pe_3y, pe_5y] if p is not None]
    pe_avg = statistics.mean(pe_vals) if pe_vals else None

    recent_trend = price_data["supplementary"].get("recent_trend", [])
    corr_1y = None
    if recent_trend:
        p_series, e_series = [], []
        for pt in recent_trend:
            valid_qs = [q for q in actual_quarters_sorted if q["date"] <= pt["date"]]
            if len(valid_qs) >= 4:
                p_series.append(pt["close"])
                e_series.append(sum(q["actual"] for q in valid_qs[-4:]))
        if len(p_series) > 1:
            corr_1y = round(statistics.correlation(p_series, e_series), 2)

    return {
        "ticker": ticker,
        "as_of": price_data.get("as_of"),
        "metrics": {
            "gaap_pe": gaap_pe,
            "current_pe": curr_pe,
            "pe_1y": pe_1y,
            "pe_3y": pe_3y,
            "pe_5y": pe_5y,
            "pe_avg": pe_avg,
            "vs_1y": (curr_pe - pe_1y) / pe_1y if curr_pe and pe_1y else None,
            "vs_3y": (curr_pe - pe_3y) / pe_3y if curr_pe and pe_3y else None,
            "vs_5y": (curr_pe - pe_5y) / pe_5y if curr_pe and pe_5y else None,
            "vs_avg": (curr_pe - pe_avg) / pe_avg if curr_pe and pe_avg else None,
            "corr_1y": corr_1y,
            "eps_cagr": cagr_5yr,
            "stability": stability_cv,
            "fwd_delta": next_est - last_actual if next_est is not None and last_actual is not None else None,
            "next_est": next_est,
            "next_date": next_date,
        },
        "history": {
            "annual_eps": annual_eps[:10],
            "quarterly": actual_quarters[:4],
        },
    }


# ---------------------------------------------------------------------------
# Verification / outlier detection
# ---------------------------------------------------------------------------

OUTLIER_RULES = [
    ("gaap_pe",    lambda v: v < 2 or v > 500,   "P/E outside 2–500x"),
    ("eps_cagr",   lambda v: v < -0.9 or v > 5,  "EPS CAGR outside -90% to +500%"),
    ("corr_1y",    lambda v: abs(v) > 1,          "Correlation outside -1 to 1"),
    ("vs_1yr",     lambda v: v > 10,              "Price up >1000% vs 1yr ago"),
    ("cagr_5yr",   lambda v: abs(v) > 2,          "Price CAGR outside ±200%"),
]

def check_outliers(ticker, price_data, earn_data):
    flags = []
    if price_data:
        m = price_data["table_metrics"]
        for key, test, msg in OUTLIER_RULES:
            if key in m and m[key] is not None and test(m[key]):
                flags.append(f"  ⚠ {ticker}: {msg} ({key} = {m[key]:.2f})")
    if earn_data:
        m = earn_data["metrics"]
        for key, test, msg in OUTLIER_RULES:
            if key in m and m[key] is not None and test(m[key]):
                flags.append(f"  ⚠ {ticker}: {msg} ({key} = {m[key]:.2f})")
    return flags


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def fmt_pct(val, dec=0):
    return f"{val:+.{dec}%}" if val is not None else "-"

def fmt_pe(val):
    return f"{val:.1f}x" if val is not None else "-"

def fmt_curr(val):
    return f"${val:.2f}" if val is not None else "-"


def format_price_table(price_results):
    headers = ["Ticker", "Price", "vs1Y", "vs2Y", "vs3Y", "vs5Y",
               "CV", "Z-Score", "52w Pos", "Drop/MaxDD", "Revert↑", "5yr CAGR"]
    rows = []
    for r in price_results:
        m = r["table_metrics"]
        rows.append([
            r["ticker"], f"${r['current_price']:.2f}",
            fmt_pct(m["vs_1yr"]), fmt_pct(m["vs_2yr"]),
            fmt_pct(m["vs_3yr"]), fmt_pct(m["vs_5yr"]),
            f"{m['cv']:.2f}" if m["cv"] else "-",
            f"{m['z_score']:+.1f}" if m["z_score"] else "-",
            f"{m['52w_position']:.0%}" if m["52w_position"] is not None else "-",
            f"{m['drop_vs_max_drawdown']:.0%}" if m["drop_vs_max_drawdown"] else "-",
            fmt_pct(m["upside_if_revert"]),
            fmt_pct(m["cagr_5yr"], 1),
        ])
    col_w = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]
    fmt = lambda row: " | ".join(str(row[i]).rjust(col_w[i]) for i in range(len(headers)))
    return "\n".join([fmt(headers), "-+-".join("-" * w for w in col_w)] + [fmt(r) for r in rows])


def format_earnings_table(earn_results):
    headers = ["Ticker", "GAAP P/E", "Adj P/E", "vs1Y", "vs3Y", "vs5Y",
               "vsAvg", "1yCorr", "||", "EPS CAGR", "Stability", "Fwd Delta"]
    rows = []
    for r in earn_results:
        m = r["metrics"]
        rows.append([
            r["ticker"], fmt_pe(m["gaap_pe"]), fmt_pe(m["current_pe"]),
            fmt_pct(m["vs_1y"]), fmt_pct(m["vs_3y"]),
            fmt_pct(m["vs_5y"]), fmt_pct(m["vs_avg"]),
            f"{m['corr_1y']:.2f}" if m["corr_1y"] is not None else "-",
            "||",
            fmt_pct(m["eps_cagr"], 1),
            f"{m['stability']:.2f}" if m["stability"] is not None else "-",
            fmt_curr(m["fwd_delta"]),
        ])
    col_w = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]
    fmt = lambda row: " | ".join(str(row[i]).rjust(col_w[i]) for i in range(len(headers)))
    return "\n".join([fmt(headers), "-+-".join("-" * w for w in col_w)] + [fmt(r) for r in rows])


def format_trend_table(ticker, trend_data):
    headers = ["Date", "Close", "MoM %"]
    rows = [[d["date"], f"${d['close']:.2f}", fmt_pct(d["change_pct"], 1)]
            for d in reversed(trend_data)]
    col_w = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]
    fmt = lambda row: " | ".join(str(row[i]).rjust(col_w[i]) for i in range(len(headers)))
    return (f"Recent Trend: {ticker}\n" +
            "\n".join([fmt(headers), "-+-".join("-" * w for w in col_w)] +
                      [fmt(r) for r in rows]))


# ---------------------------------------------------------------------------
# Per-ticker processing
# ---------------------------------------------------------------------------

def process_ticker(ticker):
    """Fetch price + earnings for one ticker. Returns (price_data, earn_data) or raises."""
    # --- Price ---
    time.sleep(API_CALL_DELAY)
    daily = fetch_prices(ticker)
    if not daily:
        raise ValueError(f"No price data returned")
    if len(daily) < 30:
        raise ValueError(f"Insufficient price data ({len(daily)} days)")

    price_data = compute_price_metrics(ticker, daily)
    if not price_data:
        raise ValueError("Price metrics computation failed")

    # Save price JSON
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    save_json(price_data, os.path.join(data_dir, f"{ticker}_price.json"))

    # --- Earnings (in-memory price_data, no disk read) ---
    time.sleep(API_CALL_DELAY)
    history = fetch_earnings(ticker)
    if not history:
        raise ValueError("No earnings data returned")

    time.sleep(API_CALL_DELAY)
    income_data = fetch_income_statement(ticker)
    gaap_pe = compute_gaap_pe(income_data, price_data["current_price"])

    earn_data = compute_earnings_metrics(ticker, history, price_data, gaap_pe=gaap_pe)
    if not earn_data:
        raise ValueError("No actual earnings quarters found")

    save_json(earn_data, os.path.join(data_dir, f"{ticker}_earnings.json"))

    return price_data, earn_data


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Price & Earnings — combined fetch")
    parser.add_argument("tickers", nargs="*", help="Ticker symbol(s)")
    parser.add_argument("--category", nargs="+", choices=["losers", "ai", "other"])
    parser.add_argument("--all", action="store_true", help="All tracker categories")
    args = parser.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

    tickers = []
    if args.all:
        tickers = parse_tickers_from_tracker(["losers", "ai", "other"])
    elif args.category:
        tickers = parse_tickers_from_tracker(args.category)
    if args.tickers:
        tickers.extend(t.upper() for t in args.tickers)

    if not tickers:
        print("Error: no tickers specified")
        sys.exit(1)

    seen = set()
    tickers = [t for t in tickers if not (t in seen or seen.add(t))]

    print(f"Processing {len(tickers)} ticker(s): {', '.join(tickers)}\n")

    price_results, earn_results, all_outliers = [], [], []
    failures = []

    for i, ticker in enumerate(tickers):
        if i > 0:
            time.sleep(API_CALL_DELAY)
        print(f"[{i+1}/{len(tickers)}] {ticker}")
        try:
            price_data, earn_data = process_ticker(ticker)
            price_results.append(price_data)
            earn_results.append(earn_data)
            outliers = check_outliers(ticker, price_data, earn_data)
            all_outliers.extend(outliers)
            m = earn_data["metrics"]
            corr_str = f"{m['corr_1y']:.2f}" if m['corr_1y'] is not None else '-'
            print(
                f"  Price: ${price_data['current_price']:.2f}  "
                f"vs1Y: {fmt_pct(price_data['table_metrics']['vs_1yr'])}  "
                f"GAAP P/E: {fmt_pe(m['gaap_pe'])}  "
                f"EPS CAGR: {fmt_pct(m['eps_cagr'], 1)}  "
                f"Corr: {corr_str}"
            )
        except Exception as e:
            print(f"  ✗ FAILED: {e}")
            failures.append(ticker)

    # --- Batch output ---
    if price_results:
        today = datetime.now().strftime("%Y-%m-%d")
        out_dir = os.path.join("Data", "screening")
        ensure_directory_exists(out_dir)
        out_path = os.path.join(out_dir, f"Price_Earnings_{today}.txt")

        lines = [
            f"PRICE & EARNINGS — {today}",
            f"Tickers: {', '.join(r['ticker'] for r in price_results)}",
            "", "--- PRICE ---", "",
            format_price_table(price_results),
        ]

        for r in price_results:
            trend = r["supplementary"].get("recent_trend", [])
            if trend:
                lines += ["", "-" * 40, "", format_trend_table(r["ticker"], trend)]

        if earn_results:
            lines += ["", "--- EARNINGS ---", "", format_earnings_table(earn_results)]

        lines += [
            "",
            "LEGEND (Price):",
            "CV: Volatility relative to price. Z-Score: Std devs of recent 1mo return.",
            "52w Pos: Position in 52-week range. Drop/MaxDD: Recent drop as % of worst 5yr drawdown.",
            "Revert↑: Upside if price reverts to 1yr average.",
            "",
            "LEGEND (Earnings):",
            "vsXY: % diff between current P/E and P/E X years ago.",
            "1yCorr: Correlation between price and earnings over last 12 months.",
            "Stability: CV of annual EPS (lower = smoother). Fwd Delta: Next est minus last actual.",
        ]

        with open(out_path, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"\nBatch summary: {out_path}")

    # --- Summary ---
    print("\n--- Summary ---")
    for ticker in tickers:
        status = "✗ FAILED" if ticker in failures else "✓"
        print(f"  {status}  {ticker}")

    if all_outliers:
        print("\n⚠ Outliers detected — verify before analysis:")
        for flag in all_outliers:
            print(flag)

    if failures:
        print(f"\nFailed: {', '.join(failures)}")
        sys.exit(1)

    print("\nDone.")


if __name__ == "__main__":
    main()

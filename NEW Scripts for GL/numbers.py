#!/usr/bin/env python3
"""
Numbers Script  (financials + valuation + price, consolidated)
==============================================================

The workhorse. For a target ticker and >=1 MANUALLY chosen peer, fetches FMP statements,
segmentation, earnings, quote, and 24 months of price, then produces one markdown report:

    1. Sales            — TTM sales + growth, annual & quarterly ACCELERATION, product segments
    2. Key Metrics      — Gross Margin, FCF/Sales, ROIC, Debt/Sales (+ 5yr troughs on GM & FCF/Sales)
    3. Valuation        — EV/Sales, GAAP & Adjusted P/E, 24-month price + delta vs trough
    4. Detailed Fin.    — full annual & quarterly metric tables (raw FCF, debt, R&D, S&M, SBC, ...)
    + Peer Comparison   — target vs peer(s) on the key metrics, growth, and valuation

Acceleration (revenue only):
    Annual   — TTM 4-quarter-sum basis: (Srev[0:4]/Srev[4:8]-1) series, 3 years (like large-actives)
    Quarterly— single-quarter YoY: (rev[i]/rev[i+4]-1) series, 4 quarters
Troughs (parity w/ large-actives): GP/Sales & FCF/Sales, current vs worst single year over 5.

Usage:
    python numbers.py AAPL --peers MSFT
    python numbers.py AAPL --peers MSFT GOOGL

Output:
    Stock Data/{T}/{T}_numbers.md
    Stock Data/{T}/raw/*.json   (target + peer raw, peer files ticker-prefixed)
"""

import sys
import os

# This file is named numbers.py, which shadows the Python stdlib `numbers` module.
# Run directly, the script's own directory sits on sys.path, so stdlib imports that
# pull in `numbers` (statistics -> fractions -> decimal -> numbers) would resolve to
# THIS file and crash. Drop the script dir before importing stdlib/3rd-party deps so
# `numbers` resolves to the real module, then re-add it for the local shared_utils.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != _HERE]

import argparse
import statistics
import requests
import time
from datetime import datetime, timedelta

sys.path.insert(0, _HERE)
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    save_json,
)

FMP_BASE = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")
API_DELAY = 0.3

# ============================================================================
# Math helpers
# ============================================================================

def sf(v):
    if v is None:
        return None
    try:
        return float(v)
    except (ValueError, TypeError):
        return None

def div(n, d):
    if n is None or d is None or d == 0:
        return None
    return n / d

def pct(cur, prev):
    if cur is None or prev is None or prev == 0:
        return None
    return (cur - prev) / abs(prev)

def cagr(vals):
    c = [v for v in vals if v is not None]
    if len(c) < 2 or c[0] <= 0 or c[-1] <= 0:
        return None
    try:
        return (c[-1] / c[0]) ** (1 / (len(c) - 1)) - 1
    except Exception:
        return None

def cv(vals):
    c = [v for v in vals if v is not None]
    if len(c) < 2:
        return None
    m = statistics.mean(c)
    if abs(m) < 1e-9:
        return None
    return statistics.stdev(c) / abs(m)

def ssum(seq, a, b):
    """Sum seq[a:b]; None if the slice is short or contains a None."""
    if b > len(seq):
        return None
    part = seq[a:b]
    return None if any(x is None for x in part) else sum(part)

# ============================================================================
# Fetch
# ============================================================================

def _get(url, label, ticker):
    try:
        r = requests.get(url, timeout=40)
        if r.status_code != 200:
            print(f"  [{ticker}] [{label}] HTTP {r.status_code}")
            return None
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"  [{ticker}] [{label}] {e}")
        return None

def fetch_all(ticker):
    """Fetch every endpoint numbers.py needs for one ticker. Returns dict or None."""
    q = f"symbol={ticker}&apikey={FMP_API_KEY}"
    out = {}
    endpoints = {
        "inc_a":  f"{FMP_BASE}/income-statement?{q}&period=annual&limit=10",
        "inc_q":  f"{FMP_BASE}/income-statement?{q}&period=quarter&limit=20",
        "bal_a":  f"{FMP_BASE}/balance-sheet-statement?{q}&period=annual&limit=10",
        "bal_q":  f"{FMP_BASE}/balance-sheet-statement?{q}&period=quarter&limit=8",
        "cf_a":   f"{FMP_BASE}/cash-flow-statement?{q}&period=annual&limit=10",
        "cf_q":   f"{FMP_BASE}/cash-flow-statement?{q}&period=quarter&limit=8",
        "seg":    f"{FMP_BASE}/revenue-product-segmentation?{q}",
        "earn":   f"{FMP_BASE}/earnings?{q}&limit=8",
        "quote":  f"{FMP_BASE}/quote?{q}",
        "price":  f"{FMP_BASE}/historical-price-eod/dividend-adjusted?{q}"
                  f"&from={(datetime.now() - timedelta(days=760)).strftime('%Y-%m-%d')}",
    }
    for key, url in endpoints.items():
        time.sleep(API_DELAY)
        out[key] = _get(url, key, ticker)
    # income annual/quarter + cash flow are the minimum required
    if not out["inc_a"] or not out["inc_q"] or not out["cf_a"]:
        print(f"  [{ticker}] Missing required statements")
        return None
    return out

# ============================================================================
# Per-period metric extraction
# ============================================================================

def decide_use_sm(inc_a, inc_q):
    """Use the dedicated Selling & Marketing line only if it is CONSISTENTLY reported.

    FMP populates sellingAndMarketingExpenses inconsistently (0 in most AAPL quarters, a
    spurious value in one). Requiring the latest annual AND latest quarter to both carry a
    positive value avoids a single stray quarter flipping the basis. Otherwise fall back to
    the always-present combined SG&A line, applied uniformly to every period.
    """
    def latest_sm(lst):
        rows = sorted([x for x in (lst or []) if x.get("date")], key=lambda x: x["date"], reverse=True)
        return sf(rows[0].get("sellingAndMarketingExpenses")) if rows else None
    a, q = latest_sm(inc_a), latest_sm(inc_q)
    return (a is not None and a > 0) and (q is not None and q > 0)


def period_metrics(inc, bal, cf, use_sm):
    """All per-period metrics from aligned income/balance/cashflow dicts."""
    g = lambda d, k: sf(d.get(k)) if d else None

    rev = g(inc, "revenue")
    gp = g(inc, "grossProfit")
    oi = g(inc, "operatingIncome")
    ni = g(inc, "netIncome")
    ebit = g(inc, "ebit")
    rd = g(inc, "researchAndDevelopmentExpenses")
    sm_mkt = g(inc, "sellingAndMarketingExpenses")
    sga = g(inc, "sellingGeneralAndAdministrativeExpenses")
    int_exp = g(inc, "interestExpense")
    pretax = g(inc, "incomeBeforeTax")
    tax = g(inc, "incomeTaxExpense")

    assets = g(bal, "totalAssets")
    ca = g(bal, "totalCurrentAssets")
    cl = g(bal, "totalCurrentLiabilities")
    debt = g(bal, "totalDebt")
    equity = g(bal, "totalEquity")
    cash = g(bal, "cashAndCashEquivalents")
    goodwill = g(bal, "goodwill")

    ocf = g(cf, "operatingCashFlow")
    fcf = g(cf, "freeCashFlow")
    capex = g(cf, "capitalExpenditure")
    da = g(cf, "depreciationAndAmortization")
    sbc = g(cf, "stockBasedCompensation")

    # S&M vs SG&A: single ticker-wide choice (see decide_use_sm)
    sm, sm_src = (sm_mkt, "S&M") if use_sm else (sga, "SG&A")

    # ROIC = NOPAT / invested capital
    tax_rate = div(tax, pretax)
    roic = None
    if ni is not None and tax_rate is not None and equity is not None and debt is not None:
        nopat = ni + (abs(int_exp) if int_exp else 0) * (1 - tax_rate)
        inv_cap = equity + debt - (cash or 0)
        roic = div(nopat, inv_cap)

    net_debt = (debt - cash) if debt is not None and cash is not None else None
    abs_capex = abs(capex) if capex is not None else None

    return {
        "revenue": rev,
        "gross_margin": div(gp, rev),
        "operating_margin": div(oi, rev),
        "rd": rd,
        "rd_to_sales": div(rd, rev),
        "sm": sm,
        "sm_to_sales": div(sm, rev),
        "sm_src": sm_src,
        "ocf": ocf,
        "fcf": fcf,
        "fcf_to_sales": div(fcf, rev),
        "ocf_to_ni": div(ocf, ni),
        "sbc": sbc,
        "sbc_to_sales": div(sbc, rev),
        "working_capital": (ca - cl) if ca is not None and cl is not None else None,
        "capex": capex,
        "da": da,
        "capex_to_da": div(abs_capex, da),
        "da_to_sales": div(da, rev),
        "total_debt": debt,
        "cash": cash,
        "net_debt": net_debt,
        "debt_to_sales": div(debt, rev),
        "debt_to_assets": div(debt, assets),
        "debt_to_ocf": div(debt, ocf),
        "interest_coverage": div(ebit, abs(int_exp)) if int_exp else None,
        "goodwill_to_sales": div(goodwill, rev),
        "roic": roic,
        "_oi": oi,
    }

def period_label(rec):
    """Filing-style label: 'FY2025' for annual, 'Q3 FY26' for quarters. Falls back to date."""
    fy = rec.get("fiscalYear")
    per = rec.get("period")
    if fy is None:
        return (rec.get("date") or "")[:7]
    if per and per != "FY":
        return f"{per} FY{str(fy)[-2:]}"
    return f"FY{fy}"


def align(inc_list, bal_list, cf_list, use_sm):
    """Align statements by date (oldest first). Returns (metrics, dates, labels)."""
    inc_s = sorted([x for x in (inc_list or []) if x.get("date")], key=lambda x: x["date"])
    bal_by = {x["date"]: x for x in (bal_list or []) if x.get("date")}
    cf_by = {x["date"]: x for x in (cf_list or []) if x.get("date")}
    metrics, dates, labels = [], [], []
    for inc in inc_s:
        d = inc["date"]
        bal = bal_by.get(d)
        cf = cf_by.get(d)
        if cf is None:
            continue
        metrics.append(period_metrics(inc, bal, cf, use_sm))
        dates.append(d)
        labels.append(period_label(inc))
    return metrics, dates, labels

def ttm_metrics(inc_q, bal_q, cf_q, use_sm):
    """TTM: sum last 4 quarters of flows, latest quarter of balance-sheet stocks."""
    inc = sorted([x for x in (inc_q or []) if x.get("date")], key=lambda x: x["date"], reverse=True)[:4]
    cf = sorted([x for x in (cf_q or []) if x.get("date")], key=lambda x: x["date"], reverse=True)[:4]
    bal = sorted([x for x in (bal_q or []) if x.get("date")], key=lambda x: x["date"], reverse=True)
    if len(inc) < 4 or len(cf) < 4:
        return None
    s = lambda lst, k: (lambda vals: None if any(v is None for v in vals) else sum(vals))(
        [sf(x.get(k)) for x in lst])
    b = lambda k: sf(bal[0].get(k)) if bal else None

    rev = s(inc, "revenue"); gp = s(inc, "grossProfit"); oi = s(inc, "operatingIncome")
    ni = s(inc, "netIncome"); ebit = s(inc, "ebit"); rd = s(inc, "researchAndDevelopmentExpenses")
    int_exp = s(inc, "interestExpense"); pretax = s(inc, "incomeBeforeTax"); tax = s(inc, "incomeTaxExpense")
    sm_mkt = s(inc, "sellingAndMarketingExpenses"); sga = s(inc, "sellingGeneralAndAdministrativeExpenses")
    ocf = s(cf, "operatingCashFlow"); fcf = s(cf, "freeCashFlow")
    capex = s(cf, "capitalExpenditure"); da = s(cf, "depreciationAndAmortization"); sbc = s(cf, "stockBasedCompensation")
    debt = b("totalDebt"); cash = b("cashAndCashEquivalents"); equity = b("totalEquity")
    assets = b("totalAssets"); ca = b("totalCurrentAssets"); cl = b("totalCurrentLiabilities")
    goodwill = b("goodwill")

    sm, sm_src = (sm_mkt, "S&M") if use_sm else (sga, "SG&A")

    tax_rate = div(tax, pretax); roic = None
    if ni is not None and tax_rate is not None and equity is not None and debt is not None:
        nopat = ni + (abs(int_exp) if int_exp else 0) * (1 - tax_rate)
        roic = div(nopat, equity + debt - (cash or 0))

    return {
        "revenue": rev, "gross_margin": div(gp, rev), "operating_margin": div(oi, rev),
        "rd": rd, "rd_to_sales": div(rd, rev), "sm": sm, "sm_to_sales": div(sm, rev), "sm_src": sm_src,
        "ocf": ocf, "fcf": fcf, "fcf_to_sales": div(fcf, rev), "ocf_to_ni": div(ocf, ni),
        "sbc": sbc, "sbc_to_sales": div(sbc, rev),
        "working_capital": (ca - cl) if ca is not None and cl is not None else None,
        "capex": capex, "da": da, "capex_to_da": div(abs(capex) if capex else None, da),
        "da_to_sales": div(da, rev),
        "total_debt": debt, "cash": cash, "net_debt": (debt - cash) if debt is not None and cash is not None else None,
        "debt_to_sales": div(debt, rev), "debt_to_assets": div(debt, assets), "debt_to_ocf": div(debt, ocf),
        "interest_coverage": div(ebit, abs(int_exp)) if int_exp else None,
        "goodwill_to_sales": div(goodwill, rev), "roic": roic, "_oi": oi,
    }

# ============================================================================
# Acceleration (revenue only)
# ============================================================================

def quarterly_rev(inc_q):
    """Newest-first list of (date, label, revenue) from quarterly income statements."""
    rows = sorted([x for x in (inc_q or []) if x.get("date")], key=lambda x: x["date"], reverse=True)
    return [(x["date"], period_label(x), sf(x.get("revenue"))) for x in rows]

def annual_accel(qr):
    """TTM 4-quarter-sum basis. Returns up to 3 rows: (label, yoy_growth, accel_pp)."""
    rev = [r for _, _, r in qr]
    labels = [l for _, l, _ in qr]
    def ttm(a):
        return ssum(rev, a, a + 4)
    # growth at window-start s: TTM(s)/TTM(s+4) - 1 ; windows Y0,Y-1,Y-2,Y-3 at s=0,4,8,12
    growth = {}
    for s in (0, 4, 8, 12):
        cur, prev = ttm(s), ttm(s + 4)
        growth[s] = (cur / prev - 1) if (cur and prev) else None
    rows = []
    for s in (0, 4, 8):
        if len(rev) < s + 8:
            break
        g = growth[s]
        a = (g - growth[s + 4]) if (g is not None and growth.get(s + 4) is not None) else None
        label = f"TTM to {labels[s]}" if s < len(labels) else "-"
        rows.append((label, g, a))
    return rows

def quarterly_accel(qr):
    """Single-quarter YoY. Returns up to 4 rows: (quarter_label, yoy_growth, accel_pp)."""
    rev = [r for _, _, r in qr]
    labels = [l for _, l, _ in qr]
    def yoy(i):
        if i + 4 < len(rev) and rev[i] is not None and rev[i + 4] not in (None, 0):
            return rev[i] / rev[i + 4] - 1
        return None
    rows = []
    for i in range(4):
        if i + 4 >= len(rev):
            break
        g = yoy(i)
        a = (g - yoy(i + 1)) if (g is not None and yoy(i + 1) is not None) else None
        rows.append((labels[i], g, a))
    return rows

# ============================================================================
# Segmentation
# ============================================================================

def segmentation(seg):
    """Latest FY product segments: list of (name, revenue, pct_of_total, yoy). + fy label."""
    if not seg or not isinstance(seg, list):
        return [], None
    rows = sorted(seg, key=lambda x: x.get("fiscalYear", 0), reverse=True)
    latest = rows[0]
    prior = rows[1] if len(rows) > 1 else None
    data = latest.get("data", {}) or {}
    prior_data = (prior.get("data", {}) if prior else {}) or {}
    total = sum(v for v in data.values() if isinstance(v, (int, float)))
    out = []
    for name, val in sorted(data.items(), key=lambda kv: kv[1] if isinstance(kv[1], (int, float)) else 0, reverse=True):
        p = div(val, total)
        pv = prior_data.get(name)
        yoy = pct(val, pv) if isinstance(pv, (int, float)) else None
        out.append((name, val, p, yoy))
    return out, latest.get("fiscalYear")

# ============================================================================
# Valuation + price
# ============================================================================

def gaap_pe(inc_q, price):
    eps = [sf(x.get("eps")) for x in sorted([y for y in (inc_q or []) if y.get("date")],
                                            key=lambda x: x["date"], reverse=True)[:4]]
    eps = [e for e in eps if e is not None]
    if len(eps) < 4 or price is None:
        return None
    tot = sum(eps)
    return div(price, tot) if tot > 0 else None

def adj_pe(earn, price):
    if not earn or price is None:
        return None
    acts = [sf(x.get("epsActual")) for x in sorted([y for y in earn if y.get("date")],
                                                   key=lambda x: x["date"], reverse=True)]
    acts = [a for a in acts if a is not None][:4]
    if len(acts) < 4:
        return None
    tot = sum(acts)
    return div(price, tot) if tot > 0 else None

def ev_to_sales(quote, ttm, bal_q):
    if not quote or not ttm:
        return None
    mc = sf(quote[0].get("marketCap")) if isinstance(quote, list) and quote else None
    rev = ttm.get("revenue")
    debt = ttm.get("total_debt")
    cash = ttm.get("cash")
    if mc is None or rev in (None, 0) or debt is None or cash is None:
        return None
    return (mc + debt - cash) / rev

def monthly_closes(price):
    """Last 24 monthly closes as (YYYY-MM, close). Newest last."""
    if not price or not isinstance(price, list):
        return []
    rows = sorted(price, key=lambda x: x.get("date", ""))
    monthly = {}
    for p in rows:
        d = p.get("date", "")
        c = sf(p.get("adjClose"))
        if d and c is not None:
            monthly[d[:7]] = (d[:7], c)
    return list(monthly.values())[-24:]

# ============================================================================
# Build one ticker's bundle
# ============================================================================

def build_bundle(ticker, raw):
    use_sm = decide_use_sm(raw["inc_a"], raw["inc_q"])
    ann, ann_dates, ann_labels = align(raw["inc_a"], raw["bal_a"], raw["cf_a"], use_sm)
    ann, ann_dates, ann_labels = ann[-5:], ann_dates[-5:], ann_labels[-5:]   # last 5 fiscal years
    qtr, qtr_dates, qtr_labels = align(raw["inc_q"], raw["bal_q"], raw["cf_q"], use_sm)
    qtr, qtr_dates, qtr_labels = qtr[-5:], qtr_dates[-5:], qtr_labels[-5:]    # last 5 quarters
    ttm = ttm_metrics(raw["inc_q"], raw["bal_q"], raw["cf_q"], use_sm)

    # operating leverage series (annual + quarterly)
    def op_lev(series):
        out = [None]
        for i in range(1, len(series)):
            oi_c = pct(series[i]["_oi"], series[i - 1]["_oi"])
            rev_c = pct(series[i]["revenue"], series[i - 1]["revenue"])
            out.append(oi_c / rev_c if (rev_c not in (None, 0) and oi_c is not None) else None)
        return out
    ann_oplev = op_lev(ann)
    qtr_oplev = op_lev(qtr)

    qr = quarterly_rev(raw["inc_q"])
    ttm_yoy = None
    _rev = [r for _, _, r in qr]
    cur, prev = ssum(_rev, 0, 4), ssum(_rev, 4, 8)
    if cur and prev:
        ttm_yoy = cur / prev - 1

    # troughs: worst annual GM / FCF-to-sales over last 5 years
    gm_series = [m["gross_margin"] for m in ann]
    fcfs_series = [m["fcf_to_sales"] for m in ann]
    gm_trough = min([v for v in gm_series if v is not None], default=None)
    fcfs_trough = min([v for v in fcfs_series if v is not None], default=None)

    quote = raw.get("quote")
    price = sf(quote[0].get("price")) if isinstance(quote, list) and quote else None

    segs, seg_fy = segmentation(raw.get("seg"))
    mcloses = monthly_closes(raw.get("price"))
    trough_price = min([c for _, c in mcloses], default=None) if mcloses else None

    return {
        "ticker": ticker,
        "ann": ann, "ann_dates": ann_dates, "ann_labels": ann_labels, "ann_oplev": ann_oplev,
        "qtr": qtr, "qtr_dates": qtr_dates, "qtr_labels": qtr_labels, "qtr_oplev": qtr_oplev,
        "ttm": ttm, "ttm_yoy": ttm_yoy,
        "annual_accel": annual_accel(qr), "quarterly_accel": quarterly_accel(qr),
        "gm_trough": gm_trough, "fcfs_trough": fcfs_trough,
        "segs": segs, "seg_fy": seg_fy,
        "price": price, "monthly_closes": mcloses, "trough_price": trough_price,
        "ev_sales": ev_to_sales(quote, ttm, raw.get("bal_q")),
        "gaap_pe": gaap_pe(raw["inc_q"], price),
        "adj_pe": adj_pe(raw.get("earn"), price),
        "sm_label": (ttm or {}).get("sm_src", "S&M"),
    }

# ============================================================================
# Formatting
# ============================================================================

def f_pct(v, dec=1):
    return f"{v*100:+.{dec}f}%" if v is not None else "-"

def f_pct_abs(v, dec=1):
    return f"{v*100:.{dec}f}%" if v is not None else "-"

def f_pp(v):
    return f"{v*100:+.1f}pp" if v is not None else "-"

def f_b(v):
    return f"${v/1e9:,.2f}B" if v is not None else "-"

def f_x(v):
    return f"{v:.2f}x" if v is not None else "-"

def f_price(v):
    return f"${v:,.2f}" if v is not None else "-"

# ============================================================================
# Markdown — one full report for the target
# ============================================================================

def cell(val, fmt, div_by=1):
    if val is None:
        return "-"
    try:
        return fmt.format(val / div_by)
    except Exception:
        return str(val)

def detail_table(bundle):
    """Full annual (with deltas/TTM/avg/CAGR/CV) + quarterly tables."""
    sm = bundle["sm_label"]
    rows_def = [
        ("Revenue ($B)", "revenue", "${:,.2f}", 1e9),
        ("Gross Margin", "gross_margin", "{:.1%}", 1),
        ("Operating Margin", "operating_margin", "{:.1%}", 1),
        ("R&D ($B)", "rd", "${:,.2f}", 1e9),
        ("  ↳ R&D / Sales", "rd_to_sales", "{:.1%}", 1),
        (f"{sm} ($B)", "sm", "${:,.2f}", 1e9),
        (f"  ↳ {sm} / Sales", "sm_to_sales", "{:.1%}", 1),
        ("Op Cash Flow ($B)", "ocf", "${:,.2f}", 1e9),
        ("Free Cash Flow ($B)", "fcf", "${:,.2f}", 1e9),
        ("  ↳ FCF / Sales", "fcf_to_sales", "{:.1%}", 1),
        ("OCF / Net Income", "ocf_to_ni", "{:.2f}x", 1),
        ("SBC ($B)", "sbc", "${:,.2f}", 1e9),
        ("  ↳ SBC / Sales", "sbc_to_sales", "{:.1%}", 1),
        ("Working Capital ($B)", "working_capital", "${:,.2f}", 1e9),
        ("Operating Leverage", "operating_leverage", "{:.2f}", 1),
        ("CapEx ($B)", "capex", "${:,.2f}", 1e9),
        ("D&A ($B)", "da", "${:,.2f}", 1e9),
        ("  ↳ CapEx / D&A", "capex_to_da", "{:.1%}", 1),
        ("  ↳ D&A / Sales", "da_to_sales", "{:.1%}", 1),
        ("Total Debt ($B)", "total_debt", "${:,.2f}", 1e9),
        ("Cash ($B)", "cash", "${:,.2f}", 1e9),
        ("Net Debt ($B)", "net_debt", "${:,.2f}", 1e9),
        ("Debt / Sales", "debt_to_sales", "{:.1%}", 1),
        ("Debt / Assets", "debt_to_assets", "{:.1%}", 1),
        ("Debt / OCF", "debt_to_ocf", "{:.2f}x", 1),
        ("Interest Coverage", "interest_coverage", "{:.1f}x", 1),
        ("Goodwill / Sales", "goodwill_to_sales", "{:.1%}", 1),
        ("ROIC", "roic", "{:.1%}", 1),
    ]

    ann, ttm = bundle["ann"], bundle["ttm"]
    dates = list(bundle["ann_labels"])
    dates = ["-"] * (5 - len(dates)) + dates

    # annual header: Y1 | Y2 Δ% | ... | Y5 Δ% | TTM | 5yr Avg | CAGR | CV
    hdr = "| Metric | " + dates[0] + " | "
    hdr += " | ".join(f"{d} | Δ%" for d in dates[1:]) + " | TTM | 5yr Avg | 5yr CAGR | CV |"
    sep = "|" + "---|" * (1 + 1 + 2 * 4 + 4)

    def metric_series(key):
        if key == "operating_leverage":
            vals = list(bundle["ann_oplev"])
            tval = None
        else:
            vals = [m.get(key) for m in ann]
            tval = ttm.get(key) if ttm else None
        vals = [None] * (5 - len(vals)) + vals
        return vals, tval

    lines = [hdr, sep]
    for label, key, fmt, dv in rows_def:
        vals, tval = metric_series(key)
        show = [abs(v) if (key == "capex" and v is not None) else v for v in vals]
        tshow = abs(tval) if (key == "capex" and tval is not None) else tval
        row = f"| {label} | {cell(show[0], fmt, dv)} |"
        for i in range(1, 5):
            row += f" {cell(show[i], fmt, dv)} |"
            if key != "operating_leverage" and show[i] is not None and show[i-1] not in (None, 0):
                row += f" {f_pct((show[i]-show[i-1])/abs(show[i-1]))} |"
            else:
                row += " - |"
        clean = [v for v in vals if v is not None]
        avg = statistics.mean([abs(v) if key == "capex" else v for v in clean]) if clean else None
        row += f" {cell(tshow, fmt, dv)} |"
        row += f" {cell(avg, fmt, dv)} |"
        row += f" {f_pct_abs(cagr(vals)) if cagr(vals) is not None else '-'} |"
        row += f" {cv(vals):.2f} |" if cv(vals) is not None else " - |"
        lines.append(row)
    annual_md = "\n".join(lines)

    # quarterly table
    qdates = list(bundle["qtr_labels"])
    disp = qdates[1:] if len(qdates) > 1 else qdates
    disp = ["-"] * (4 - len(disp)) + disp
    qhdr = "| Metric | " + " | ".join(f"{d} | Δ%" for d in disp) + " |"
    qsep = "|" + "---|" * (1 + 2 * 4)
    qlines = [qhdr, qsep]
    for label, key, fmt, dv in rows_def:
        if key == "operating_leverage":
            qv = list(bundle["qtr_oplev"])
        else:
            qv = [m.get(key) for m in bundle["qtr"]]
        qv = [None] * (5 - len(qv)) + qv
        qshow = [abs(v) if (key == "capex" and v is not None) else v for v in qv]
        row = f"| {label} |"
        for i in range(1, 5):
            row += f" {cell(qshow[i], fmt, dv)} |"
            if key != "operating_leverage" and qshow[i] is not None and qshow[i-1] not in (None, 0):
                row += f" {f_pct((qshow[i]-qshow[i-1])/abs(qshow[i-1]))} |"
            else:
                row += " - |"
        qlines.append(row)
    quarterly_md = "\n".join(qlines)
    return annual_md, quarterly_md

def full_report(bundle):
    t = bundle["ticker"]
    ttm = bundle["ttm"] or {}
    md = [f"# Numbers: {t}", f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*", ""]

    # --- 1. Sales ---
    md.append("## 1. Sales")
    md.append("")
    md.append(f"**TTM Sales:** {f_b(ttm.get('revenue'))}  |  **TTM YoY Growth:** {f_pct(bundle['ttm_yoy'])}")
    md.append("")
    md.append("**Annual acceleration.** *Growth = trailing 12 months (sum of the last 4 quarters) "
              "vs the prior TTM. Accel = the pp change in that growth rate vs the year before "
              "(+ = growth speeding up, − = slowing).*")
    md.append("")
    md.append("| Window | YoY Growth | Accel (pp) |")
    md.append("|---|---|---|")
    for label, g, a in bundle["annual_accel"]:
        md.append(f"| {label} | {f_pct(g)} | {f_pp(a)} |")
    md.append("")
    md.append("**Quarterly acceleration.** *Growth = each quarter vs the same quarter one year "
              "earlier (YoY, so seasonality cancels). Accel = the pp change vs the prior quarter's "
              "YoY growth.*")
    md.append("")
    md.append("| Quarter | YoY Growth | Accel (pp) |")
    md.append("|---|---|---|")
    for label, g, a in bundle["quarterly_accel"]:
        md.append(f"| {label} | {f_pct(g)} | {f_pp(a)} |")
    md.append("")
    if bundle["segs"]:
        md.append(f"**Product segmentation** (FY{bundle['seg_fy']}):")
        md.append("")
        md.append("| Segment | Revenue | % of Total | YoY |")
        md.append("|---|---|---|---|")
        for name, val, p, yoy in bundle["segs"]:
            md.append(f"| {name} | {f_b(val)} | {f_pct_abs(p)} | {f_pct(yoy)} |")
        md.append("")
    else:
        md.append("*Product segmentation: not reported by FMP for this ticker.*")
        md.append("")

    # --- 2. Key Metrics ---
    md.append("## 2. Key Metrics")
    md.append("")
    md.append("*5yr Trough = the worst single fiscal year for the metric over the last 5 years. "
              "Δ vs Trough = current TTM minus that trough, in percentage points — how far above "
              "(or below) the 5-year low it sits. Troughs apply to gross margin and FCF/Sales.*")
    md.append("")
    md.append("| Metric | TTM / Current | 5yr Trough | Δ vs Trough |")
    md.append("|---|---|---|---|")
    gm = ttm.get("gross_margin"); fcfs = ttm.get("fcf_to_sales")
    md.append(f"| Gross Margin | {f_pct_abs(gm)} | {f_pct_abs(bundle['gm_trough'])} | {f_pp(gm - bundle['gm_trough']) if gm is not None and bundle['gm_trough'] is not None else '-'} |")
    md.append(f"| FCF / Sales | {f_pct_abs(fcfs)} | {f_pct_abs(bundle['fcfs_trough'])} | {f_pp(fcfs - bundle['fcfs_trough']) if fcfs is not None and bundle['fcfs_trough'] is not None else '-'} |")
    md.append(f"| ROIC | {f_pct_abs(ttm.get('roic'))} | — | — |")
    md.append(f"| Debt / Sales | {f_pct_abs(ttm.get('debt_to_sales'))} | — | — |")
    md.append("")

    # --- 3. Valuation ---
    md.append("## 3. Valuation")
    md.append("")
    md.append(f"**EV / Sales:** {f_x(bundle['ev_sales'])}  |  **GAAP P/E:** {f_x(bundle['gaap_pe'])}  |  **Adjusted P/E:** {f_x(bundle['adj_pe'])}")
    md.append("")
    cur_p = bundle["price"]; tr = bundle["trough_price"]
    delta = pct(cur_p, tr) if (cur_p is not None and tr is not None) else None
    md.append(f"**Price:** {f_price(cur_p)}  |  **24mo Trough:** {f_price(tr)}  |  **Δ vs Trough:** {f_pct(delta)}")
    md.append("")
    if bundle["monthly_closes"]:
        md.append("| Month | Close |")
        md.append("|---|---|")
        for m, c in bundle["monthly_closes"]:
            md.append(f"| {m} | {f_price(c)} |")
        md.append("")

    # --- 4. Detailed ---
    annual_md, quarterly_md = detail_table(bundle)
    md.append("## 4. Detailed Financials")
    md.append("")
    md.append("### Annual & Long-Term Trends")
    md.append(annual_md)
    md.append("")
    md.append("### Recent Quarterly Trends")
    md.append(quarterly_md)
    md.append("")
    md.append("---\n*TTM = Trailing Twelve Months. CV = Coefficient of Variation. Accel = pp change in YoY growth.*")
    return "\n".join(md)

def peer_comparison(bundles):
    """One table: target vs peers on the key comparison rows."""
    md = ["## Peer Comparison", "",
          "| Metric | " + " | ".join(b["ticker"] for b in bundles) + " |",
          "|---|" + "---|" * len(bundles)]
    def ttm(b, k): return (b["ttm"] or {}).get(k)
    rows = [
        ("TTM Sales", lambda b: f_b(ttm(b, "revenue"))),
        ("TTM Sales Growth", lambda b: f_pct(b["ttm_yoy"])),
        ("Gross Margin", lambda b: f_pct_abs(ttm(b, "gross_margin"))),
        ("FCF / Sales", lambda b: f_pct_abs(ttm(b, "fcf_to_sales"))),
        ("R&D / Sales", lambda b: f_pct_abs(ttm(b, "rd_to_sales"))),
        ("ROIC", lambda b: f_pct_abs(ttm(b, "roic"))),
        ("Debt / Sales", lambda b: f_pct_abs(ttm(b, "debt_to_sales"))),
        ("Interest Coverage", lambda b: f_x(ttm(b, "interest_coverage"))),
        ("EV / Sales", lambda b: f_x(b["ev_sales"])),
        ("GAAP P/E", lambda b: f_x(b["gaap_pe"])),
        ("Adjusted P/E", lambda b: f_x(b["adj_pe"])),
    ]
    for label, fn in rows:
        md.append(f"| {label} | " + " | ".join(fn(b) for b in bundles) + " |")
    md.append("")
    return "\n".join(md)

# ============================================================================
# Main
# ============================================================================

def save_raw(ticker, target, raw):
    raw_dir = get_data_directory(ticker, None if ticker == target else target)
    ensure_directory_exists(raw_dir)
    for k, v in raw.items():
        if v is not None:
            save_json(v, os.path.join(raw_dir, f"{ticker}_{k}.json"))

def main():
    ap = argparse.ArgumentParser(description="Numbers — financials + valuation + price (needs >=1 peer)")
    ap.add_argument("ticker")
    ap.add_argument("--peers", nargs="+", required=True, metavar="PEER",
                    help="One or more peer tickers (manual, required)")
    args = ap.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY not set")
        sys.exit(1)

    target = args.ticker.upper()
    peers = [p.upper() for p in args.peers][:2]
    all_tickers = [target] + peers

    bundles, failures = [], []
    for t in all_tickers:
        print(f"\nProcessing {t}{' (target)' if t == target else ' (peer)'}...")
        raw = fetch_all(t)
        if not raw:
            print(f"  ✗ {t} FAILED")
            failures.append(t)
            continue
        save_raw(t, target, raw)
        try:
            bundles.append(build_bundle(t, raw))
            print(f"  ✓ {t}")
        except Exception as e:
            import traceback; traceback.print_exc()
            print(f"  ✗ {t} processing failed: {e}")
            failures.append(t)

    if not bundles or bundles[0]["ticker"] != target:
        print("\n✗ Target failed — aborting.")
        sys.exit(1)

    md = full_report(bundles[0]) + "\n\n---\n\n"
    if len(bundles) > 1:
        md += peer_comparison(bundles)
        for pb in bundles[1:]:
            annual_md, quarterly_md = detail_table(pb)
            md += "\n\n---\n\n"
            md += f"## {pb['ticker']} — Detailed Financials\n\n"
            md += "### Annual & Long-Term Trends\n" + annual_md + "\n\n"
            md += "### Recent Quarterly Trends\n" + quarterly_md + "\n"

    out_dir = get_writeup_directory(target)
    ensure_directory_exists(out_dir)
    out_path = os.path.join(out_dir, f"{target}_numbers.md")
    with open(out_path, "w") as f:
        f.write(md)

    print(f"\n✓ Report: {out_path}")
    if failures:
        print(f"⚠ Failed: {', '.join(failures)}")
        if target in failures:
            sys.exit(1)
    print("Done.")

if __name__ == "__main__":
    main()

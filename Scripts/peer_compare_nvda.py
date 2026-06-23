#!/usr/bin/env python3
"""
Peer Compare vs TSM
===================
Builds two tables comparing TSM against a fixed peer set, all in USD.

Table 1 — Current snapshot: Current (latest quarter, annualized x4) and TTM
          (last 4 quarters) for each metric. Peer cells show % gap vs TSM.
Table 2 — Trend: the 3 latest completed fiscal years per company, plus the
          2-year CAGR. Delta-to-TSM shown only on the CAGR (in pp).

Leverages Scripts/screen.py (FMP fetchers, _roic_at, safe_float,
compute_fcf_metrics) and Scripts/price_earnings.py (fetch_earnings = the
earnings-calendar epsActual, which is the ADR-USD EPS that makes TSM correct).

Reliability handling:
  - Currency: income/cashflow values are in each company's reportedCurrency
    (TSM=TWD, ASML=EUR, rest=USD). Converted to USD with FX below.
  - epsActual (earnings calendar) is already in trading currency (USD) -> not
    converted. Used for the Non-GAAP P/E and EPS rows.
  - GAAP P/E and P/OE use the market-cap method (mktcap / NI, mktcap / owner
    earnings) which is split- and share-count-proof.
  - Negative earnings / owner earnings / NOPAT -> "NM" and no % gap.

Usage:  python Scripts/peer_compare_tsm.py
Output: Data/screening/Peer_Compare_NVDA_<date>.md  (+ printed)
"""

import os
import sys
import json
import requests
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import screen          # noqa: E402  (reuse fetchers + _roic_at + safe_float)
import price_earnings  # noqa: E402  (reuse fetch_earnings)

safe_float = screen.safe_float
FMP_BASE = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")

# --- live FX, fetched 2026-06-16 from FMP forex [ESTIMATED: spot rate] ---
EURUSD = 1.16128
USDTWD = 31.496

TICKERS = ["NVDA", "TSM", "AVGO", "ASML", "KLAC", "AMD"]
ANCHOR = "NVDA"
ADR_RATIO = {"TSM": 5}  # ordinary shares per ADR; default 1


def fx_to_usd(currency):
    if currency == "USD":
        return 1.0
    if currency == "EUR":
        return EURUSD
    if currency == "TWD":
        return 1.0 / USDTWD
    return 1.0  # unknown -> assume USD, will be flagged by sanity check


def fetch_annual(ticker, statement, limit=5):
    url = (f"{FMP_BASE}/{statement}?symbol={ticker}"
           f"&period=annual&limit={limit}&apikey={FMP_API_KEY}")
    try:
        r = requests.get(url, timeout=30)
        d = r.json()
        return d if isinstance(d, list) else []
    except Exception:
        return []


def sum4(rows, key):
    return sum((safe_float(rows[i].get(key)) or 0) for i in range(min(4, len(rows))))


def eps_actual_series(earnings):
    """Most-recent-first list of actual quarterly EPS (trading currency = USD)."""
    if not earnings:
        return []
    acts = [(h.get("date"), safe_float(h.get("epsActual")))
            for h in earnings if safe_float(h.get("epsActual")) is not None]
    acts.sort(key=lambda x: x[0], reverse=True)
    return [a[1] for a in acts]


def adj_close_on_or_before(sorted_prices, date_str):
    cands = [p for p in sorted_prices if p["date"] <= date_str]
    return cands[-1]["adjClose"] if cands else None


def roic_single_q_annualized(income_q0, balance_row):
    """ROIC using one quarter's NOPAT annualized (x4) over invested capital."""
    if not income_q0 or not balance_row:
        return None
    ni = safe_float(income_q0.get("netIncome")) or 0
    interest = safe_float(income_q0.get("interestExpense")) or 0
    pretax = safe_float(income_q0.get("incomeBeforeTax"))
    tax = safe_float(income_q0.get("incomeTaxExpense"))
    if not pretax:
        return None
    tax_rate = (tax or 0) / pretax
    nopat = (ni + abs(interest) * (1 - tax_rate)) * 4
    equity = safe_float(balance_row.get("totalEquity"))
    debt = safe_float(balance_row.get("totalDebt"))
    cash = safe_float(balance_row.get("cashAndCashEquivalents")) or 0
    if equity is None or debt is None:
        return None
    ic = equity + debt - cash
    return nopat / ic if ic > 0 else None


def roic_annual(inc_row, bal_row):
    if not inc_row or not bal_row:
        return None
    ni = safe_float(inc_row.get("netIncome")) or 0
    interest = safe_float(inc_row.get("interestExpense")) or 0
    pretax = safe_float(inc_row.get("incomeBeforeTax"))
    tax = safe_float(inc_row.get("incomeTaxExpense"))
    if not pretax:
        return None
    tax_rate = (tax or 0) / pretax
    nopat = ni + abs(interest) * (1 - tax_rate)
    equity = safe_float(bal_row.get("totalEquity"))
    debt = safe_float(bal_row.get("totalDebt"))
    cash = safe_float(bal_row.get("cashAndCashEquivalents")) or 0
    if equity is None or debt is None:
        return None
    ic = equity + debt - cash
    return nopat / ic if ic > 0 else None


def build(ticker):
    prof = screen.fetch_profile(ticker)
    inc = screen.fetch_income(ticker, limit=12) or []
    cf = screen.fetch_cashflow(ticker, limit=12) or []
    bal = screen.fetch_balance(ticker, limit=12) or []
    earn = price_earnings.fetch_earnings(ticker) or []
    inc_a = fetch_annual(ticker, "income-statement")
    cf_a = fetch_annual(ticker, "cash-flow-statement")
    bal_a = fetch_annual(ticker, "balance-sheet-statement")
    daily = screen.fetch_prices(ticker, years=4) or []
    sorted_prices = sorted(daily, key=lambda p: p["date"])

    ccy = (inc[0].get("reportedCurrency") if inc else None) or "USD"
    fx = fx_to_usd(ccy)
    adr = ADR_RATIO.get(ticker, 1)
    mktcap = safe_float(prof.get("marketCap")) if prof else None
    cur_price = sorted_prices[-1]["adjClose"] if sorted_prices else (
        safe_float(prof.get("price")) if prof else None)

    eps_a = eps_actual_series(earn)

    out = {"ticker": ticker, "ccy": ccy, "fx": fx, "mktcap": mktcap,
           "price": cur_price, "current": {}, "ttm": {}, "annual": []}

    # ---- TTM (last 4 quarters) ----
    rev_ttm = sum4(inc, "revenue") * fx
    op_ttm = sum4(inc, "operatingIncome")
    rev_raw_ttm = sum4(inc, "revenue")
    ni_ttm = sum4(inc, "netIncome") * fx
    fcfm = screen.compute_fcf_metrics(cf)
    ocf_ttm = (fcfm["ocf_ttm"] or 0) * fx
    fcf_ttm = (fcfm["fcf_ttm"] or 0) * fx
    sbc_ttm = (fcfm["sbc_ttm"] or 0) * fx
    capex_ttm = abs(sum4(cf, "capitalExpenditure")) * fx
    eps_ttm = sum(eps_a[:4]) if len(eps_a) >= 4 else None
    roic_ttm = screen._roic_at(inc[0:4] if len(inc) >= 4 else None,
                               bal[0] if bal else None)

    t = out["ttm"]
    t["gaap_pe"] = (mktcap / ni_ttm) if (mktcap and ni_ttm > 0) else None
    t["nongaap_pe"] = (cur_price / eps_ttm) if (cur_price and eps_ttm and eps_ttm > 0) else None
    oe_ttm = fcf_ttm - sbc_ttm
    t["poe"] = (mktcap / oe_ttm) if (mktcap and oe_ttm > 0) else None
    # split guard: epsActual straddling a recent split makes nongaap_pe ~10x too low
    if t["gaap_pe"] and t["nongaap_pe"] and t["nongaap_pe"] < t["gaap_pe"] / 4:
        t["nongaap_pe"] = None  # split-distorted source
    t["eps"] = eps_ttm
    t["roic"] = roic_ttm
    t["op_margin"] = (op_ttm / rev_raw_ttm) if rev_raw_ttm else None
    t["capex_rev"] = (capex_ttm / rev_ttm) if rev_ttm else None
    t["fcf_ocf"] = (fcf_ttm / ocf_ttm) if ocf_ttm else None
    t["revenue"] = rev_ttm
    t["ocf"] = ocf_ttm
    t["fcf"] = fcf_ttm
    t["capex"] = capex_ttm

    # ---- Current (latest quarter, annualized x4 where a flow) ----
    if inc and cf:
        rev_q = (safe_float(inc[0].get("revenue")) or 0)
        op_q = (safe_float(inc[0].get("operatingIncome")) or 0)
        ni_q = (safe_float(inc[0].get("netIncome")) or 0)
        fcf_q = (safe_float(cf[0].get("freeCashFlow")) or 0)
        ocf_q = (safe_float(cf[0].get("operatingCashFlow")) or 0)
        sbc_q = (safe_float(cf[0].get("stockBasedCompensation")) or 0)
        capex_q = abs(safe_float(cf[0].get("capitalExpenditure")) or 0)
        eps_q = eps_a[0] if eps_a else None

        ni_q_usd_ann = ni_q * 4 * fx
        oe_q_usd_ann = (fcf_q - sbc_q) * 4 * fx
        c = out["current"]
        c["gaap_pe"] = (mktcap / ni_q_usd_ann) if (mktcap and ni_q_usd_ann > 0) else None
        c["nongaap_pe"] = (cur_price / (eps_q * 4)) if (cur_price and eps_q and eps_q > 0) else None
        c["poe"] = (mktcap / oe_q_usd_ann) if (mktcap and oe_q_usd_ann > 0) else None
        if c["gaap_pe"] and c["nongaap_pe"] and c["nongaap_pe"] < c["gaap_pe"] / 4:
            c["nongaap_pe"] = None  # split-distorted source
        c["eps"] = (eps_q * 4) if eps_q is not None else None
        c["roic"] = roic_single_q_annualized(inc[0], bal[0] if bal else None)
        c["op_margin"] = (op_q / rev_q) if rev_q else None
        c["capex_rev"] = (capex_q / rev_q) if rev_q else None
        c["fcf_ocf"] = (fcf_q / ocf_q) if ocf_q else None
        c["revenue"] = rev_q * 4 * fx
        c["ocf"] = ocf_q * 4 * fx
        c["fcf"] = fcf_q * 4 * fx
        c["capex"] = capex_q * 4 * fx

    # ---- Annual trend (store 4 latest FY: display 3, 4th = base for 3yr CAGR) ----
    n = min(4, len(inc_a), len(cf_a), len(bal_a))
    for i in range(n):
        ai, ac, ab = inc_a[i], cf_a[i], bal_a[i]
        fy_date = ai.get("date")
        rev = (safe_float(ai.get("revenue")) or 0)
        op = (safe_float(ai.get("operatingIncome")) or 0)
        ni = (safe_float(ai.get("netIncome")) or 0)
        shares = safe_float(ai.get("weightedAverageShsOutDil")) or None
        fcf = (safe_float(ac.get("freeCashFlow")) or 0)
        ocf = (safe_float(ac.get("operatingCashFlow")) or 0)
        sbc = (safe_float(ac.get("stockBasedCompensation")) or 0)
        capex = abs(safe_float(ac.get("capitalExpenditure")) or 0)
        ni_usd = ni * fx
        oe_usd = (fcf - sbc) * fx
        fy_price = adj_close_on_or_before(sorted_prices, fy_date) if fy_date else None
        # split/currency-proof historical mkt cap: scale current mkt cap by adj-price ratio
        mc_fy = (mktcap * fy_price / cur_price) if (mktcap and fy_price and cur_price) else None
        # EPS anchored to validated TTM epsActual, scaled by GAAP NI ratio (ADR/split-proof)
        eps_usd = (eps_ttm * ni_usd / ni_ttm) if (eps_ttm and ni_ttm) else None
        out["annual"].append({
            "fy": (fy_date[:4] if fy_date else "?"),
            "gaap_pe": (mc_fy / ni_usd) if (mc_fy and ni_usd > 0) else None,
            "poe": (mc_fy / oe_usd) if (mc_fy and oe_usd > 0) else None,
            "eps": eps_usd,
            "roic": roic_annual(ai, ab),
            "op_margin": (op / rev) if rev else None,
            "capex_rev": (capex / rev) if rev else None,
            "fcf_ocf": (fcf / ocf) if ocf else None,
            "revenue": rev * fx,
            "ocf": ocf * fx,
            "fcf": fcf * fx,
            "capex": capex * fx,
        })
    return out


def main():
    data = {t: build(t) for t in TICKERS}
    with open(os.path.join(os.path.dirname(__file__), "..", "Data", "screening",
              f"Peer_Compare_NVDA_{datetime.now():%Y-%m-%d}.json"), "w") as f:
        json.dump(data, f, indent=2)
    # print a compact JSON for inspection
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()

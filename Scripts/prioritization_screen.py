#!/usr/bin/env python3
"""Prioritization screen — growth-oriented, sales-anchored stock ranking.

Reproduces the screen described in `prioritization metrics explanation.md`.
Per-ticker FMP `stable` calls only (no bulk endpoints).

Usage:
    python prioritization_screen.py                      # default ticker list
    python prioritization_screen.py NVDA,TSM,MU,...      # custom tickers (comma-sep)
    python prioritization_screen.py @tickers.txt         # tickers from file (one per line or comma-sep)
    python prioritization_screen.py NVDA,TSM out.csv     # custom tickers + output path

Env: FMP_API_KEY must be set.
"""
import os, sys, csv, json, time, ssl, urllib.request
from datetime import date, datetime

FMP_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
CA = "/root/.ccr/ca-bundle.crt"
_CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else None

DEFAULT_TICKERS = ["TSM", "NVDA", "AVGO", "AMD", "ASML", "KLAC", "AMKR", "INTC", "MU",
                   "CRWV", "AMZN", "GOOGL", "MSFT", "META", "ADBE", "INTU", "CRM",
                   "WDAY", "NOW"]


# --------------------------------------------------------------------------- #
# FMP fetch (with light retry/backoff)
# --------------------------------------------------------------------------- #
def _get(path, retries=4):
    url = f"{FMP_BASE}/{path}{'&' if '?' in path else '?'}apikey={FMP_KEY}"
    for i in range(retries):
        try:
            with urllib.request.urlopen(url, context=_CTX, timeout=120) as r:
                return json.load(r)
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(2 ** i)  # 1s, 2s, 4s, 8s


def sf(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------- #
# FX -> USD
# --------------------------------------------------------------------------- #
def get_fx():
    eur = _get("quote?symbol=EURUSD")[0]["price"]   # USD per EUR
    twd = _get("quote?symbol=USDTWD")[0]["price"]   # TWD per USD
    return eur, twd


def to_usd(v, ccy, eur, twd):
    if v is None:
        return None
    if ccy == "USD":
        return v
    if ccy == "EUR":
        return v * eur
    if ccy == "TWD":
        return v / twd
    return v


# --------------------------------------------------------------------------- #
# ROIC-style helper not needed here; screen uses the 10 columns below.
# --------------------------------------------------------------------------- #
def fetch_ticker(t, eur, twd, today):
    U = lambda v, c: to_usd(v, c, eur, twd)
    pr = _get(f"profile?symbol={t}")[0]
    eod = sorted(_get(f"historical-price-eod/dividend-adjusted?symbol={t}"),
                 key=lambda r: r["date"])
    px = eod[-1]["adjClose"]
    ld = datetime.strptime(eod[-1]["date"], "%Y-%m-%d").date()
    prior = [r for r in eod if (ld - datetime.strptime(r["date"], "%Y-%m-%d").date()).days >= 90]
    mom3 = (px / prior[-1]["adjClose"] - 1) if prior else None

    ipo = pr.get("ipoDate")
    yrs = round((today - datetime.strptime(ipo, "%Y-%m-%d").date()).days / 365.25, 1) if ipo else None
    shares = pr["marketCap"] / pr["price"] if pr.get("price") else None      # ADR-consistent
    mc = px * shares if shares else pr.get("marketCap")

    iq = _get(f"income-statement?symbol={t}&period=quarter&limit=8")
    ia = _get(f"income-statement?symbol={t}&period=annual&limit=8")
    cq = _get(f"cash-flow-statement?symbol={t}&period=quarter&limit=4")
    bq = _get(f"balance-sheet-statement?symbol={t}&period=quarter&limit=1")[0]
    c = iq[0]["reportedCurrency"]

    ttm = lambda src, k, a=0: (sum((U(sf(src[i].get(k)), c) or 0) for i in range(a, a + 4))
                               if len(src) >= a + 4 else None)
    rev = ttm(iq, "revenue")
    rev1 = ttm(iq, "revenue", 4)
    gp = ttm(iq, "grossProfit")
    ocf = ttm(cq, "operatingCashFlow")
    capex = sum(abs(U(sf(cq[i].get("capitalExpenditure")), c) or 0) for i in range(min(4, len(cq))))
    fcf = (ocf - capex) if ocf is not None else None
    debt = U(sf(bq.get("totalDebt")), c) or 0
    cash = U(sf(bq.get("cashAndCashEquivalents")), c) or 0
    ev = mc + debt - cash

    sg_ttm = (rev / rev1 - 1) if rev and rev1 else None
    sg_q = (U(sf(iq[0]["revenue"]), c) / U(sf(iq[4]["revenue"]), c) - 1) \
        if len(iq) >= 5 and iq[4].get("revenue") else None

    # 7-year context flags (ratios -> no FX needed)
    yoys = [ia[i]["revenue"] / ia[i + 1]["revenue"] - 1
            for i in range(min(7, len(ia) - 1)) if ia[i + 1].get("revenue")]
    worst_rev = min(yoys) if yoys else None
    nms = [ia[i]["netIncome"] / ia[i]["revenue"]
           for i in range(min(7, len(ia))) if ia[i].get("revenue")]
    worst_nm = min(nms) if nms else None

    return dict(
        ticker=t, company=pr.get("companyName", t),
        sg_ttm=sg_ttm, sg_q=sg_q,
        gm=(gp / rev) if rev else None,
        fcfs=(fcf / rev) if rev else None,
        evs=(ev / rev) if rev else None,
        mom3=mom3, yrs=yrs, worst_rev=worst_rev, worst_nm=worst_nm,
        industry=pr.get("industry", ""), description=(pr.get("description", "") or "").strip(),
    )


# --------------------------------------------------------------------------- #
# Percentile scoring
# --------------------------------------------------------------------------- #
def percentiles(rows, key, higher_better=True):
    items = [(r["ticker"], r[key]) for r in rows if r[key] is not None]
    n = len(items)
    out = {}
    for tk, v in items:
        beaten = sum(1 for _, w in items if (w < v if higher_better else w > v))
        out[tk] = beaten / (n - 1) * 100 if n > 1 else 50.0
    return out


def score(rows):
    P_ttm = percentiles(rows, "sg_ttm")
    P_q = percentiles(rows, "sg_q")
    P_gm = percentiles(rows, "gm")
    P_fcf = percentiles(rows, "fcfs")
    P_evs = percentiles(rows, "evs", higher_better=False)   # cheaper = better
    for r in rows:
        t = r["ticker"]
        growth = (P_ttm.get(t, 50) + P_q.get(t, 50)) / 2
        gm, fcf, evs = P_gm.get(t, 50), P_fcf.get(t, 50), P_evs.get(t, 50)
        r["score_equal"] = round((growth + gm + fcf + evs) / 4, 1)
        r["score_growth"] = round(0.4 * growth + 0.2 * gm + 0.2 * fcf + 0.2 * evs, 1)


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #
HEADERS = [
    "Ticker", "Company", "Score: growth-weighted (0-100)", "Score: equal (0-100)",
    "Sales growth: TTM vs prior-year TTM (%)", "Sales growth: latest Q vs year-ago Q (%)",
    "Gross profit / Sales (%)", "FCF / Sales (%)", "EV / Sales (x)",
    "Price vs. 3 months ago (%)", "Years since IPO (yrs)",
    "Worst annual sales growth, last 7y (%)", "Worst net profit / Sales, last 7y (%)",
    "Industry", "Description",
]


def pct(v):
    return round(v * 100, 0) if v is not None else ""


def build_row(r):
    yrs = r["yrs"]
    # 7-year cyclicality flags unreliable if <7 years public
    reliable = (yrs is not None and yrs >= 7)
    return [
        r["ticker"], r["company"], r["score_growth"], r["score_equal"],
        pct(r["sg_ttm"]), pct(r["sg_q"]), pct(r["gm"]), pct(r["fcfs"]),
        round(r["evs"], 1) if r["evs"] is not None else "",
        pct(r["mom3"]), yrs if yrs is not None else "",
        pct(r["worst_rev"]) if reliable else "",
        pct(r["worst_nm"]) if reliable else "",
        r["industry"], r["description"],
    ]


def main():
    if not FMP_KEY:
        sys.exit("Error: FMP_API_KEY not set.")
    args = sys.argv[1:]
    tickers, out_path = DEFAULT_TICKERS, "prioritization_screen.csv"
    if args:
        a = args[0]
        if a.startswith("@"):
            txt = open(a[1:]).read()
            tickers = [x.strip().upper() for x in txt.replace(",", "\n").split() if x.strip()]
        else:
            tickers = [x.strip().upper() for x in a.split(",") if x.strip()]
        if len(args) > 1:
            out_path = args[1]

    today = date.today()
    eur, twd = get_fx()
    print(f"FX: EURUSD {eur:.3f}  USDTWD {twd:.2f}  |  {len(tickers)} tickers")

    rows = []
    for t in tickers:
        try:
            rows.append(fetch_ticker(t, eur, twd, today))
        except Exception as e:
            print(f"  [{t}] FAILED: {str(e)[:80]}")
    if not rows:
        sys.exit("No data fetched.")

    score(rows)
    rows.sort(key=lambda r: -r["score_growth"])

    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADERS)
        for r in rows:
            w.writerow(build_row(r))

    # console preview (numeric columns only)
    print(f"\n{'Tk':<6}{'GwWt':>6}{'Eq':>6}{'sTTM':>7}{'sQ':>7}{'GM':>5}{'FCF':>6}{'EV/S':>6}"
          f"{'3mo':>7}{'IPO':>6}{'WrstRev':>8}{'WrstNM':>8}")
    for r in rows:
        b = build_row(r)
        fmt = lambda x: (str(x) if x != "" else "—")
        print(f"{r['ticker']:<6}{fmt(b[2]):>6}{fmt(b[3]):>6}{fmt(b[4]):>7}{fmt(b[5]):>7}"
              f"{fmt(b[6]):>5}{fmt(b[7]):>6}{fmt(b[8]):>6}{fmt(b[9]):>7}{fmt(b[10]):>6}"
              f"{fmt(b[11]):>8}{fmt(b[12]):>8}")
    print(f"\nWrote {out_path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()

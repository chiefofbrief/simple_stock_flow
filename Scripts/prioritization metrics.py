#!/usr/bin/env python3
"""Prioritization screen — growth-oriented, sales-anchored stock ranking.

Reproduces the screen described in `prioritization metrics explanation.md`.
Per-ticker FMP `stable` calls only (no bulk endpoints).

A ticker list is REQUIRED (there is no default) — the screen is always run on a
new batch. Works for any batch size (tens to thousands); each ticker that fails
after retries is skipped, and progress is printed as it goes.

Usage:
    python "prioritization metrics.py" NVDA,TSM,MU            # tickers (comma-sep)
    python "prioritization metrics.py" @tickers.txt          # tickers from file (one per line or comma-sep)
    python "prioritization metrics.py" @tickers.txt out.csv  # tickers from file + output path

Env: FMP_API_KEY must be set.
"""
import os, sys, csv, json, time, ssl, collections, urllib.request
from datetime import date, datetime

FMP_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
CA = "/root/.ccr/ca-bundle.crt"
_CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else None

# Rate limiting: FMP plan allows 300 calls/min. Cap at 290 call-starts per
# rolling 60s (safety margin), enforced across ALL calls including retries.
RATE_LIMIT = 290
_CALL_TIMES = collections.deque()


def _throttle():
    now = time.monotonic()
    while _CALL_TIMES and now - _CALL_TIMES[0] >= 60:
        _CALL_TIMES.popleft()
    if len(_CALL_TIMES) >= RATE_LIMIT:
        time.sleep(60 - (now - _CALL_TIMES[0]) + 0.05)
        now = time.monotonic()
        while _CALL_TIMES and now - _CALL_TIMES[0] >= 60:
            _CALL_TIMES.popleft()
    _CALL_TIMES.append(time.monotonic())


# --------------------------------------------------------------------------- #
# FMP fetch (rate-limited, with retry/backoff)
# --------------------------------------------------------------------------- #
def _get(path, retries=4):
    url = f"{FMP_BASE}/{path}{'&' if '?' in path else '?'}apikey={FMP_KEY}"
    for i in range(retries):
        try:
            _throttle()
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
        ticker=t, company=pr.get("companyName", t), mktcap=mc,
        sg_ttm=sg_ttm, sg_q=sg_q,
        gm=(gp / rev) if rev else None,
        fcfs=(fcf / rev) if rev else None,
        evs=(ev / rev) if rev else None,
        mom3=mom3, yrs=yrs, worst_rev=worst_rev, worst_nm=worst_nm,
        industry=pr.get("industry", ""), description=(pr.get("description", "") or "").strip(),
    )


def fetch_profile_only(t):
    """Triage pass: one call per ticker (profile), no financials."""
    pr = _get(f"profile?symbol={t}")[0]
    return dict(ticker=t, company=pr.get("companyName", t), mktcap=pr.get("marketCap"),
                sector=pr.get("sector", ""), industry=pr.get("industry", ""),
                description=(pr.get("description", "") or "").strip())


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
    "Ticker", "Company",
    "Score: growth-weighted (0-100)", "Score: equal (0-100)",
    "Sales growth: TTM vs prior-year TTM (%)", "Sales growth: latest Q vs year-ago Q (%)",
    "Gross profit / Sales (%)", "FCF / Sales (%)", "EV / Sales (x)",
    "Price vs. 3 months ago (%)", "Years since IPO (yrs)",
    "Worst annual sales growth, last 7y (%)", "Worst net profit / Sales, last 7y (%)",
    "Market Cap ($B)", "Industry", "Description",
]
PROFILE_HEADERS = ["Ticker", "Company", "Sector", "Market Cap ($B)", "Industry", "Description"]


def pct(v):
    return round(v * 100, 0) if v is not None else ""


def bil(v):
    return round(v / 1e9, 1) if v is not None else ""


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
        bil(r["mktcap"]), r["industry"], r["description"],
    ]


def _parse_tickers(spec):
    if spec.startswith("@"):
        txt = open(spec[1:]).read()
        return [x.strip().upper() for x in txt.replace(",", "\n").split() if x.strip()]
    return [x.strip().upper() for x in spec.split(",") if x.strip()]


def _run(tickers, fetch_fn, label):
    """Fetch loop with progress + skip-on-fail. Returns (rows, failed)."""
    n = len(tickers)
    rows, failed = [], []
    for i, t in enumerate(tickers, 1):
        try:
            rows.append(fetch_fn(t))
            status = "ok"
        except Exception as e:
            failed.append(t)
            status = f"FAILED: {str(e)[:60]}"
        if i % 25 == 0 or n <= 50 or status != "ok":
            print(f"  [{i}/{n}] {t} {status}")
    if failed:
        print(f"  {len(failed)} ticker(s) skipped after retries: {', '.join(failed[:20])}"
              + (" ..." if len(failed) > 20 else ""))
    return rows, failed


def main():
    if not FMP_KEY:
        sys.exit("Error: FMP_API_KEY not set.")
    argv = sys.argv[1:]
    profile_only = "--profile-only" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        sys.exit("Usage: prioritization metrics.py <TICKERS|@file> [out.csv] [--profile-only]\n"
                 "  TICKERS: comma-separated (e.g. NVDA,TSM,MU) or @path to a file. No default list.\n"
                 "  --profile-only: triage pass — 1 call/ticker; outputs Ticker, Company,\n"
                 "                  Market Cap, Sector, Industry, Description (no metrics/scores).")
    tickers = _parse_tickers(args[0])
    if not tickers:
        sys.exit("No tickers provided.")
    n = len(tickers)

    # -- triage pass: profile only, 1 call/ticker --
    if profile_only:
        out_path = args[1] if len(args) > 1 else "prioritization triage.csv"
        print(f"Profile-only (triage) | {n} tickers | 1 call/ticker")
        rows, _ = _run(tickers, fetch_profile_only, "profile")
        if not rows:
            sys.exit("No data fetched.")
        with open(out_path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(PROFILE_HEADERS)
            for r in rows:
                w.writerow([r["ticker"], r["company"], r["sector"],
                            bil(r["mktcap"]), r["industry"], r["description"]])
        print(f"\nWrote {out_path} ({len(rows)} rows)")
        return

    # -- full screen: ~6 calls/ticker --
    out_path = args[1] if len(args) > 1 else "prioritization metrics.csv"
    today = date.today()
    eur, twd = get_fx()
    print(f"FX: EURUSD {eur:.3f}  USDTWD {twd:.2f}  |  {n} tickers | ~6 calls/ticker")
    rows, _ = _run(tickers, lambda t: fetch_ticker(t, eur, twd, today), "full")
    if not rows:
        sys.exit("No data fetched.")

    score(rows)
    rows.sort(key=lambda r: -r["score_growth"])
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADERS)
        for r in rows:
            w.writerow(build_row(r))

    # console preview (numeric columns)
    fmt = lambda x: (str(x) if x != "" else "—")
    print(f"\n{'Tk':<6}{'GwWt':>6}{'Eq':>6}{'MC$B':>8}{'sTTM':>7}{'sQ':>7}{'GM':>5}"
          f"{'FCF':>6}{'EV/S':>6}{'3mo':>7}{'IPO':>6}{'WrstRev':>8}{'WrstNM':>8}")
    for r in rows:
        rel = (r["yrs"] is not None and r["yrs"] >= 7)
        print(f"{r['ticker']:<6}{fmt(r['score_growth']):>6}{fmt(r['score_equal']):>6}"
              f"{fmt(bil(r['mktcap'])):>8}{fmt(pct(r['sg_ttm'])):>7}{fmt(pct(r['sg_q'])):>7}"
              f"{fmt(pct(r['gm'])):>5}{fmt(pct(r['fcfs'])):>6}"
              f"{fmt(round(r['evs'],1) if r['evs'] is not None else ''):>6}"
              f"{fmt(pct(r['mom3'])):>7}{fmt(r['yrs'] if r['yrs'] is not None else ''):>6}"
              f"{fmt(pct(r['worst_rev']) if rel else ''):>8}{fmt(pct(r['worst_nm']) if rel else ''):>8}")
    print(f"\nWrote {out_path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()

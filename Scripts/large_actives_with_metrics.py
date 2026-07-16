#!/usr/bin/env python3
"""
Large Actives with Metrics — STANDALONE (no file reads).

The Active Stock Universe (majors + OTC/PNK, active common stock) put through
three filters, enriched per-symbol, then scored on growth and risk.

  filters (all in this script):
      market cap        >= $1B
      dollar volume     >= $1M / day   (price x volume, from the screener)
      prior-year sales  >= $10M USD    (after currency conversion)
  scores:
      growth_score       — 80% sales growth (TTM / latest-Q / 3v3), 20% GP/sales quality
      risk_score         — HIGH = SAFER; leverage + FCF/GP/sales floors & peak-risk
      growth_risk_score  — combined headline: 2/3 growth_score + 1/3 risk_score

Flow (exact order):
  1. Baseline: own screener pull, one call per exchange
       {NASDAQ, NYSE, AMEX, OTC, PNK} & isEtf=false & isFund=false
       & isActivelyTrading=true & marketCapMoreThan=$1B.  The market-cap floor is
       applied server-side (before the screener's 10k row cap) so the OTC/PNK
       small-cap flood never truncates the large caps we keep.  A call still
       returning >= 10,000 STOPS and flags.
  2. Filter: marketCap >= $1B AND price*volume >= $1M/day (both from screener).
  3. Per surviving symbol, 7 calls:
       /profile                              -> description, ipoDate
       /income-statement    period=quarter   -> sales, gross profit, net income (TTM)
       /income-statement    period=annual    -> 7y troughs, 3v3 growth, dilution
       /cash-flow-statement period=quarter   -> FCF (TTM)
       /cash-flow-statement period=annual    -> FCF/sales 7y trough
       /balance-sheet-statement period=quarter -> total debt, cash (latest)
       /grades-consensus                     -> analyst buy % and count
  4. Currency -> USD: /quote-short per distinct reportedCurrency.  Only absolute
       dollar figures are converted (sales, and the EV/PE inputs net income, debt,
       cash); every "/sales" ratio is same-currency numerator/denominator so the
       currency cancels and no conversion is needed.
  5. EV/Sales and P/E are computed IN-HOUSE in USD (not taken from FMP TTM
       endpoints, which mix USD price with local-currency financials):
         ev_to_sales_ttm = (market_cap + total_debt - cash) / sales_ttm     [all USD]
         pe_ratio_ttm    =  market_cap / net_income_ttm                     [all USD]
       EV/Sales is present for every name; P/E is blank when TTM net income <= 0.
  6. Sales filter: keep prior-year TTM sales >= $10M USD.
  7. Scores (last) — percentile blend within the filtered batch:
       P_f = (# strictly lower)/(N-1)*100 ; missing field re-normalises weights.

Metrics (quarters newest-first; [0:4]=TTM, [4:8]=prior TTM):
  sales_growth_ttm_vs_prior_ttm_pct = (Srev[0:4]/Srev[4:8] - 1)*100
  sales_growth_latest_q_yoy_pct     = (rev[0]/rev[4] - 1)*100
  gross_profit_to_sales_ttm_pct     = Sgp[0:4]/Srev[0:4] *100
  gross_profit_to_sales_yoy_change_pp = (Sgp[0:4]/Srev[0:4] - Sgp[4:8]/Srev[4:8])*100
  fcf_to_sales_ttm_pct              = Sfcf[0:4]/Srev[0:4] *100
  total_debt_to_sales_pct           = totalDebt(latest Q)/Srev[0:4] *100
Annual (newest-first):
  sales_growth_3yr_vs_prior_3yr_pct = (avg(rev_a[0:3])/avg(rev_a[3:6]) - 1)*100
  shares_outstanding_yoy_change_pct = (shs_a[0]/shs_a[1] - 1)*100  (+dilution/-buyback)
  worst_growth = min over <=7 of (rev_a[i]/rev_a[i+1] - 1)
  worst_gm     = min over <=7 of (gp_a[i]/rev_a[i])
  worst_fcf    = min over <=7 of (fcf_a[year]/rev_a[year])         (year-matched)
  *_vs_7yr_trough_pp = current - worst*100        (blank if years-since-IPO < 7)

Scores:
  growth_score = 0.35*P(sales_growth_ttm) + 0.25*P(sales_growth_q)
               + 0.20*P(sales_growth_3v3) + 0.10*P(gp_to_sales)
               + 0.10*P(gp_to_sales_chg)
  risk_score (HIGH=SAFER) =
        0.30 *(100 - P(debt_to_sales))
      + 0.125*P(fcf_7y_worst)   + 0.125*(100 - P(fcf_vs_trough))
      + 0.125*P(gp_7y_worst)    + 0.125*(100 - P(gp_vs_trough))
      + 0.10 *P(sales_7y_worst) + 0.10 *(100 - P(sales_vs_trough))
    The 7y-worst LEVELS are computed for the percentiles but not written out;
    the floor is recoverable from any displayed current value minus its delta.
  growth_risk_score = (2*growth_score + risk_score)/3  (BLANK if either is blank)

Saves:   Large_Actives_with_Metrics.csv  (repo root)
API key: FMP_API_KEY.  ~60 min (7 calls/symbol + FX).
"""
import bisect
import csv
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

import requests

BASE = "https://financialmodelingprep.com/stable"
API_KEY = os.environ.get("FMP_API_KEY")
EXCHANGES = ["NASDAQ", "NYSE", "AMEX", "OTC", "PNK"]
MIN_MARKET_CAP = 1_000_000_000
MIN_DOLLAR_VOLUME = 1_000_000
MIN_PRIOR_SALES_USD = 10_000_000
RATE_PER_SEC = 4.8
WORKERS = 5
MAX_RETRIES = 5
TIMEOUT = 60
LIM = 200000
CAP = 10000
CALLS_PER_SYMBOL = 7
TODAY = date.today()

DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
OUT_PATH = os.path.join(DATA_DIR, "Large_Actives_with_Metrics.csv")

# growth_score: 80% sales growth (TTM/latest-Q/3v3), 20% GP/sales quality
GROWTH_WEIGHTS = {
    "sales_growth_ttm_vs_prior_ttm_pct": 0.35,
    "sales_growth_latest_q_yoy_pct": 0.25,
    "sales_growth_3yr_vs_prior_3yr_pct": 0.20,
    "gross_profit_to_sales_ttm_pct": 0.10,
    "gross_profit_to_sales_yoy_change_pp": 0.10,
}
# risk_score: HIGH = SAFER.  (field, weight, invert) — invert=True flips to 100-P
# so "lower is safer" (debt) and "bigger gap is riskier" (deltas) score as safety.
RISK_COMPONENTS = [
    ("total_debt_to_sales_pct", 0.30, True),
    ("_fcf_to_sales_7y_worst_pct", 0.125, False),
    ("fcf_to_sales_vs_7yr_trough_pp", 0.125, True),
    ("_gp_to_sales_7y_worst_pct", 0.125, False),
    ("gross_profit_to_sales_vs_7yr_trough_pp", 0.125, True),
    ("_sales_growth_7y_worst_pct", 0.10, False),
    ("sales_growth_vs_7yr_trough_pp", 0.10, True),
]
OUT_COLS = [
    "symbol", "company_name", "market_cap_usd", "ipo_date",
    "growth_risk_score", "growth_score", "risk_score",
    "ev_to_sales_ttm", "pe_ratio_ttm", "analyst_buy_pct", "analyst_count",
    "description", "sector", "industry",
    "sales_ttm_usd",
    "sales_growth_ttm_vs_prior_ttm_pct", "sales_growth_latest_q_yoy_pct",
    "sales_growth_3yr_vs_prior_3yr_pct",
    "gross_profit_to_sales_ttm_pct", "gross_profit_to_sales_yoy_change_pp",
    "fcf_to_sales_ttm_pct", "total_debt_to_sales_pct",
    "sales_growth_vs_7yr_trough_pp", "gross_profit_to_sales_vs_7yr_trough_pp",
    "fcf_to_sales_vs_7yr_trough_pp",
    "shares_outstanding_yoy_change_pct",
    "exchange", "volume",
]
# sales_prior_ttm_usd is still computed in main() (it is the >=$10M filter key) but
# is no longer written — the growth delta already captures current-vs-prior.


class RateLimiter:
    def __init__(self, per_sec):
        self.interval = 1.0 / per_sec
        self.lock = threading.Lock()
        self.next_t = time.monotonic()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            if self.next_t > now:
                time.sleep(self.next_t - now)
            self.next_t = max(now, self.next_t) + self.interval


limiter = RateLimiter(RATE_PER_SEC)
session = requests.Session()


def gated_get(url):
    for attempt in range(MAX_RETRIES):
        limiter.wait()
        try:
            r = session.get(url, timeout=TIMEOUT)
            if r.status_code == 429:
                time.sleep(3 * (attempt + 1))
                continue
            if r.status_code != 200:
                return None
            return r.json()
        except requests.RequestException:
            time.sleep(2 * (attempt + 1))
    return None


def _f(x):
    try:
        return float(x) if x not in (None, "") else 0.0
    except (TypeError, ValueError):
        return 0.0


def _num(x):
    try:
        return float(x) if x is not None else None
    except (TypeError, ValueError):
        return None


def years_since_ipo(ipo):
    try:
        y, m, d = map(int, ipo.split("-"))
        return (TODAY - date(y, m, d)).days / 365.25
    except Exception:
        return None


def _ssum(lst, a, b):
    if b > len(lst):
        return None
    seg = lst[a:b]
    return None if any(v is None for v in seg) else sum(seg)


def _savg(lst, a, b):
    s = _ssum(lst, a, b)
    return None if s is None else s / (b - a)


# ---------------- 1-2. baseline + market-cap & dollar-volume filters ----------------
def screener(exchange):
    # marketCapMoreThan filters server-side, BEFORE the screener's 10k row cap,
    # so the OTC/PNK small-cap flood never truncates the >=$1B names we keep.
    # Set one dollar below MIN_MARKET_CAP so the exact >= boundary is still owned
    # by the post-pull filter in get_baseline().
    q = {"exchange": exchange, "isEtf": "false", "isFund": "false",
         "isActivelyTrading": "true", "marketCapMoreThan": MIN_MARKET_CAP - 1,
         "limit": LIM, "apikey": API_KEY}
    url = f"{BASE}/company-screener?" + "&".join(f"{k}={v}" for k, v in q.items())
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    d = r.json()
    if not isinstance(d, list):
        raise RuntimeError(f"unexpected response for {exchange}: {str(d)[:160]}")
    if len(d) >= CAP:
        sys.exit(f"\n*** CAP HIT: '{exchange}' returned {len(d)} rows (>= {CAP}). "
                 f"Likely truncated. STOPPING so you can decide how to page it. ***")
    return d


def get_baseline():
    by_symbol = {}
    for ex in EXCHANGES:
        for r in screener(ex):
            sym = (r.get("symbol") or "").strip()
            if not sym or sym in by_symbol:
                continue
            by_symbol[sym] = {"symbol": sym, "company_name": r.get("companyName", ""),
                              "market_cap_usd": r.get("marketCap", ""), "sector": r.get("sector", ""),
                              "industry": r.get("industry", ""), "volume": r.get("volume", ""),
                              "exchange": ex, "_price": r.get("price", "")}
    active = list(by_symbol.values())
    large = [r for r in active
             if _f(r["market_cap_usd"]) >= MIN_MARKET_CAP
             and _f(r["_price"]) * _f(r["volume"]) >= MIN_DOLLAR_VOLUME]
    for r in large:
        r.pop("_price", None)
    print(f"Active universe: {len(active):,}  ->  marketCap>=$1B & $-vol>=$1M/day: {len(large):,}")
    return large


# ---------------- 3. per-symbol enrichment (7 calls) ----------------
def enrich(symbol):
    q = requests.utils.quote(symbol)
    out = {
        "description": "", "ipo_date": "", "reportedCurrency": "",
        "_sales_ttm_local": None, "_sales_ttm_prior_local": None,
        "_net_income_ttm_local": None, "_total_debt_local": None, "_cash_local": None,
        "sales_growth_ttm_vs_prior_ttm_pct": "", "sales_growth_latest_q_yoy_pct": "",
        "sales_growth_3yr_vs_prior_3yr_pct": "",
        "gross_profit_to_sales_ttm_pct": "", "gross_profit_to_sales_yoy_change_pp": "",
        "fcf_to_sales_ttm_pct": "", "total_debt_to_sales_pct": "",
        "analyst_buy_pct": "", "analyst_count": "",
        "shares_outstanding_yoy_change_pct": "",
        "sales_growth_vs_7yr_trough_pp": "", "gross_profit_to_sales_vs_7yr_trough_pp": "",
        "fcf_to_sales_vs_7yr_trough_pp": "",
        "_sales_growth_7y_worst_pct": "", "_gp_to_sales_7y_worst_pct": "",
        "_fcf_to_sales_7y_worst_pct": "",
    }

    # profile
    p = gated_get(f"{BASE}/profile?symbol={q}&apikey={API_KEY}")
    if isinstance(p, list) and p:
        out["description"] = p[0].get("description") or ""
        out["ipo_date"] = p[0].get("ipoDate") or ""

    # income-statement quarter -> TTM sales / gross profit / net income
    sales_ttm = None
    d = gated_get(f"{BASE}/income-statement?symbol={q}&period=quarter&limit=8&apikey={API_KEY}")
    if isinstance(d, list) and d:
        d = sorted(d, key=lambda r: r.get("date") or "", reverse=True)
        out["reportedCurrency"] = d[0].get("reportedCurrency") or ""
        rev = [_num(r.get("revenue")) for r in d]
        gp = [_num(r.get("grossProfit")) for r in d]
        ni = [_num(r.get("netIncome")) for r in d]
        rn, rp = _ssum(rev, 0, 4), _ssum(rev, 4, 8)
        gn, gpp = _ssum(gp, 0, 4), _ssum(gp, 4, 8)
        sales_ttm = rn
        out["_sales_ttm_local"] = rn
        out["_sales_ttm_prior_local"] = rp
        out["_net_income_ttm_local"] = _ssum(ni, 0, 4)
        if rn is not None and rp not in (None, 0):
            out["sales_growth_ttm_vs_prior_ttm_pct"] = round((rn / rp - 1) * 100, 2)
        if len(rev) >= 5 and rev[0] is not None and rev[4] not in (None, 0):
            out["sales_growth_latest_q_yoy_pct"] = round((rev[0] / rev[4] - 1) * 100, 2)
        if gn is not None and rn not in (None, 0):
            out["gross_profit_to_sales_ttm_pct"] = round(gn / rn * 100, 2)
        if gn is not None and rn not in (None, 0) and gpp is not None and rp not in (None, 0):
            out["gross_profit_to_sales_yoy_change_pp"] = round((gn / rn - gpp / rp) * 100, 2)

    # cash-flow quarter -> FCF TTM ; FCF/sales (currency cancels)
    cq = gated_get(f"{BASE}/cash-flow-statement?symbol={q}&period=quarter&limit=8&apikey={API_KEY}")
    if isinstance(cq, list) and cq and sales_ttm not in (None, 0):
        cq = sorted(cq, key=lambda r: r.get("date") or "", reverse=True)
        fcf = [_num(r.get("freeCashFlow")) for r in cq]
        fn = _ssum(fcf, 0, 4)
        if fn is not None:
            out["fcf_to_sales_ttm_pct"] = round(fn / sales_ttm * 100, 2)

    # balance-sheet quarter -> total debt, cash (latest) ; debt/sales (currency cancels)
    bs = gated_get(f"{BASE}/balance-sheet-statement?symbol={q}&period=quarter&limit=4&apikey={API_KEY}")
    if isinstance(bs, list) and bs:
        bs = sorted(bs, key=lambda r: r.get("date") or "", reverse=True)
        b0 = bs[0]
        out["_total_debt_local"] = _num(b0.get("totalDebt"))
        csh = _num(b0.get("cashAndShortTermInvestments"))
        if csh is None:
            csh = _num(b0.get("cashAndCashEquivalents"))
        out["_cash_local"] = csh
        if out["_total_debt_local"] is not None and sales_ttm not in (None, 0):
            out["total_debt_to_sales_pct"] = round(out["_total_debt_local"] / sales_ttm * 100, 2)

    # income-statement annual -> 3v3 growth, dilution, 7y-worst growth & GP/sales
    wg = wm = None
    rev_by_year = {}
    n_annual = 0
    a = gated_get(f"{BASE}/income-statement?symbol={q}&period=annual&limit=8&apikey={API_KEY}")
    if isinstance(a, list) and a:
        a = sorted(a, key=lambda r: r.get("date") or "", reverse=True)
        n_annual = len(a)
        ra = [_num(r.get("revenue")) for r in a]
        ga = [_num(r.get("grossProfit")) for r in a]
        for r in a:
            y = str(r.get("calendarYear") or (r.get("date") or "")[:4])
            rv = _num(r.get("revenue"))
            if y and rv is not None:
                rev_by_year[y] = rv
        # 3-year-vs-prior-3-year smoothed growth
        a3n, a3p = _savg(ra, 0, 3), _savg(ra, 3, 6)
        if a3n is not None and a3p not in (None, 0):
            out["sales_growth_3yr_vs_prior_3yr_pct"] = round((a3n / a3p - 1) * 100, 2)
        # dilution: diluted weighted-average shares YoY (fallback to basic)
        def _shs(r):
            v = _num(r.get("weightedAverageShsOutDil"))
            if v in (None, 0):
                v = _num(r.get("weightedAverageShsOut"))
            return v
        sh = [_shs(r) for r in a]
        if len(sh) >= 2 and sh[0] is not None and sh[1] not in (None, 0):
            out["shares_outstanding_yoy_change_pct"] = round((sh[0] / sh[1] - 1) * 100, 2)
        # 7y troughs (levels)
        gs = [ra[i] / ra[i + 1] - 1 for i in range(min(7, len(ra) - 1))
              if ra[i] is not None and ra[i + 1] not in (None, 0)]
        ms = [ga[i] / ra[i] for i in range(min(7, len(ra)))
              if ga[i] is not None and ra[i] not in (None, 0)]
        wg = min(gs) if gs else None
        wm = min(ms) if ms else None

    # cash-flow annual -> FCF/sales 7y trough (year-matched to annual revenue)
    wfcf = None
    ca = gated_get(f"{BASE}/cash-flow-statement?symbol={q}&period=annual&limit=8&apikey={API_KEY}")
    if isinstance(ca, list) and ca and rev_by_year:
        ca = sorted(ca, key=lambda r: r.get("date") or "", reverse=True)
        margins = []
        for c in ca:
            y = str(c.get("calendarYear") or (c.get("date") or "")[:4])
            f_ = _num(c.get("freeCashFlow"))
            rv = rev_by_year.get(y)
            if f_ is not None and rv not in (None, 0):
                margins.append(f_ / rv)
            if len(margins) >= 7:
                break
        wfcf = min(margins) if margins else None

    # cyclicality: current-vs-7y-worst deltas + internal trough levels
    # (blank on short history — an unreliable trough)
    yrs = years_since_ipo(out["ipo_date"])
    short = (yrs is not None and yrs < 7) or (yrs is None and n_annual < 8)
    if not short:
        cg = out["sales_growth_ttm_vs_prior_ttm_pct"]
        cm = out["gross_profit_to_sales_ttm_pct"]
        cf = out["fcf_to_sales_ttm_pct"]
        if wg is not None:
            out["_sales_growth_7y_worst_pct"] = round(wg * 100, 2)
            if isinstance(cg, (int, float)):
                out["sales_growth_vs_7yr_trough_pp"] = round(cg - wg * 100, 2)
        if wm is not None:
            out["_gp_to_sales_7y_worst_pct"] = round(wm * 100, 2)
            if isinstance(cm, (int, float)):
                out["gross_profit_to_sales_vs_7yr_trough_pp"] = round(cm - wm * 100, 2)
        if wfcf is not None:
            out["_fcf_to_sales_7y_worst_pct"] = round(wfcf * 100, 2)
            if isinstance(cf, (int, float)):
                out["fcf_to_sales_vs_7yr_trough_pp"] = round(cf - wfcf * 100, 2)

    # analyst grades consensus -> % buy + count
    g = gated_get(f"{BASE}/grades-consensus?symbol={q}&apikey={API_KEY}")
    if isinstance(g, list) and g:
        row = g[0]
        sb, b, h, s, ss = (_f(row.get("strongBuy")), _f(row.get("buy")), _f(row.get("hold")),
                           _f(row.get("sell")), _f(row.get("strongSell")))
        tot = sb + b + h + s + ss
        if tot > 0:
            out["analyst_buy_pct"] = round((sb + b) / tot * 100, 1)
            out["analyst_count"] = int(tot)
    return out


# ---------------- 4. FX ----------------
def fx_rate(cur):
    if cur == "USD":
        return 1.0
    d = gated_get(f"{BASE}/quote-short?symbol={cur}USD&apikey={API_KEY}")
    if isinstance(d, list) and d and d[0].get("price"):
        return d[0]["price"]
    d = gated_get(f"{BASE}/quote-short?symbol=USD{cur}&apikey={API_KEY}")
    if isinstance(d, list) and d and d[0].get("price"):
        return 1.0 / d[0]["price"]
    return None


# ---------------- 7. scores ----------------
def _percentiles(rows, field):
    vals = sorted(r[field] for r in rows if isinstance(r.get(field), (int, float)))
    n = len(vals)
    pm = {}
    for r in rows:
        v = r.get(field)
        if isinstance(v, (int, float)):
            pm[id(r)] = 100.0 * bisect.bisect_left(vals, v) / (n - 1) if n > 1 else 50.0
    return pm


def add_scores(rows):
    gmaps = {f: _percentiles(rows, f) for f in GROWTH_WEIGHTS}
    for r in rows:
        num = den = 0.0
        for f, w in GROWTH_WEIGHTS.items():
            if id(r) in gmaps[f]:
                num += w * gmaps[f][id(r)]
                den += w
        r["growth_score"] = round(num / den, 1) if den > 0 else ""

    rmaps = {f: _percentiles(rows, f) for f, _, _ in RISK_COMPONENTS}
    for r in rows:
        num = den = 0.0
        for f, w, inv in RISK_COMPONENTS:
            if id(r) in rmaps[f]:
                p = rmaps[f][id(r)]
                num += w * (100.0 - p if inv else p)
                den += w
        r["risk_score"] = round(num / den, 1) if den > 0 else ""

    # combined headline: 2/3 growth + 1/3 risk. BLANK unless BOTH are present
    # (no partial fallback — a one-sided blend would misrepresent the row).
    for r in rows:
        g = r["growth_score"] if isinstance(r["growth_score"], (int, float)) else None
        rk = r["risk_score"] if isinstance(r["risk_score"], (int, float)) else None
        r["growth_risk_score"] = round((2 * g + rk) / 3, 1) if (g is not None and rk is not None) else ""


def main():
    if not API_KEY:
        sys.exit("FMP_API_KEY is not set in the environment.")
    os.makedirs(DATA_DIR, exist_ok=True)

    base = get_baseline()
    total = len(base)
    print(f"Enriching {total:,} names ({CALLS_PER_SYMBOL} calls each, "
          f"~{CALLS_PER_SYMBOL * total / RATE_PER_SEC / 60:.1f} min)...")
    enriched = {}
    done = 0
    t0 = time.monotonic()
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(enrich, r["symbol"]): r["symbol"] for r in base}
        for fut in as_completed(futs):
            enriched[futs[fut]] = fut.result()
            done += 1
            if done % 250 == 0 or done == total:
                print(f"  {done:,}/{total:,}  ({(time.monotonic()-t0)/60:.1f} min)")
    merged = [{**r, **enriched.get(r["symbol"], {})} for r in base]

    currencies = sorted({r["reportedCurrency"] for r in merged if r.get("reportedCurrency")})
    fx = {c: fx_rate(c) for c in currencies}
    print("FX (USD/unit):", ", ".join(f"{c}={fx[c]:.4g}" if fx[c] else f"{c}=NONE" for c in currencies))

    for r in merged:
        rate = fx.get(r.get("reportedCurrency"))
        rate_eff = rate if rate else 1.0
        mc = _f(r.get("market_cap_usd"))
        sl, spl = r.get("_sales_ttm_local"), r.get("_sales_ttm_prior_local")
        r["sales_ttm_usd"] = "" if sl is None else int(sl * rate_eff)
        r["sales_prior_ttm_usd"] = "" if spl is None else int(spl * rate_eff)
        # P/E = market cap / TTM net income (both USD); blank when no TTM profit
        ni = r.get("_net_income_ttm_local")
        if ni is not None and mc > 0:
            ni_usd = ni * rate_eff
            r["pe_ratio_ttm"] = round(mc / ni_usd, 2) if ni_usd > 0 else ""
        else:
            r["pe_ratio_ttm"] = ""
        # EV/Sales = (market cap + total debt - cash) / TTM sales (all USD)
        td, csh, su = r.get("_total_debt_local"), r.get("_cash_local"), r["sales_ttm_usd"]
        if isinstance(su, int) and su > 0 and td is not None and mc > 0:
            ev_usd = mc + td * rate_eff - (csh or 0.0) * rate_eff
            r["ev_to_sales_ttm"] = round(ev_usd / su, 2)
        else:
            r["ev_to_sales_ttm"] = ""
        r["market_cap_usd"] = int(mc)

    kept = [r for r in merged if isinstance(r.get("sales_prior_ttm_usd"), int)
            and r["sales_prior_ttm_usd"] >= MIN_PRIOR_SALES_USD]
    add_scores(kept)
    kept.sort(key=lambda r: (r["growth_score"] if isinstance(r["growth_score"], (int, float)) else -1),
              reverse=True)

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    print("\n================== LARGE ACTIVES WITH METRICS ==================")
    print(f"Saved: {OUT_PATH}")
    print(f"Baseline (>=$1B & >=$1M/day $-vol): {total:,}  |  "
          f"dropped (prior sales < $10M USD): {total-len(kept):,}  |  kept: {len(kept):,}")
    print(f"Elapsed: {(time.monotonic()-t0)/60:.1f} min  |  columns: {len(OUT_COLS)}")
    print("===============================================================")


if __name__ == "__main__":
    main()

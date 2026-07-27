#!/usr/bin/env python3
"""
Large Actives with Metrics — STANDALONE (no file reads).

The Active Stock Universe (majors + OTC/PNK, active common stock) put through
three filters, enriched per-symbol, then scored and flagged for a
read-at-a-glance dashboard.

  filters (all in this script):
      market cap        >= $1B
      dollar volume     >= $1M / day   (price x volume, from the screener)
      prior-year sales  >= $10M USD    (after currency conversion)

  scores & flags (all DYNAMIC — every cutoff is recomputed from the batch each run):
      growth_score        4 equal parts: TTM growth, latest-Q YoY growth, TTM
                          accel, Q accel.  The two LEVEL parts are floored — below
                          the batch top-third bar they score 0, so only genuinely
                          rapid growers rank.  Accel parts are not floored, not capped.
      growth_context      "Base · Acceleration · Alignment":
                            Base         Strong (TTM growth in top third) / Weak
                            Acceleration Accelerating (TTM accel > +10pp) /
                                         Steady (-10..+10) / Decelerating (< -10)
                            Alignment    Aligned (TTM & latest-Q growth agree — both
                                         top-third or both not) / Not aligned
      profitability_score 50% percentile(gross profit/sales)
                        + 50% percentile(FCF/sales)
      gross_profit_vs_trough, fcf_vs_trough
                          High (top 10% of the vs-5yr-trough delta) /
                          Low (bottom 10%) / blank.  Extremes only.
      debt_risk           HIGH for the worst one-third of the universe by debt
                          burden — FCF<=0-with-debt is automatically worst, the rest
                          ranked by total debt / FCF.  Blank otherwise.
      ev_sales_flag       Low (cheapest third) / High (priciest third) / blank
      pe_flag             Low / High (thirds) / None (no positive P/E) / blank

Flow (exact order):
  1. Baseline: own screener pull, one call per exchange
       {NASDAQ, NYSE, AMEX, OTC, PNK} & isEtf=false & isFund=false
       & isActivelyTrading=true & marketCapMoreThan=$1B.  The market-cap floor is
       applied server-side (before the screener's 10k row cap) so the OTC/PNK
       small-cap flood never truncates the large caps we keep.  A call still
       returning >= 10,000 STOPS and flags.
  2. Filter: marketCap >= $1B AND price*volume >= $1M/day (both from screener).
  3. Per surviving symbol, 7 calls:
       /profile                                -> description, ipoDate
       /income-statement    period=quarter(12) -> sales/gross profit/net income,
                                                  growth levels + acceleration
       /income-statement    period=annual      -> 5y GP/sales trough, dilution
       /cash-flow-statement period=quarter      -> FCF (TTM); debt/FCF input
       /cash-flow-statement period=annual       -> FCF/sales 5y trough
       /balance-sheet-statement period=quarter  -> total debt, cash (latest)
       /grades-consensus                        -> analyst sell % and count
  4. Currency -> USD: /quote-short per distinct reportedCurrency.  Only absolute
       dollar figures are converted (sales, and the EV/PE inputs net income, debt,
       cash); every "/sales" and the debt/FCF ratio is same-currency numerator and
       denominator so the currency cancels and no conversion is needed.
  5. EV/Sales and P/E are computed IN-HOUSE in USD (not taken from FMP TTM
       endpoints, which mix USD price with local-currency financials):
         ev_to_sales_ttm = (market_cap + total_debt - cash) / sales_ttm     [all USD]
         pe_ratio_ttm    =  market_cap / net_income_ttm                     [all USD]
       EV/Sales is present for every name; P/E is blank when TTM net income <= 0.
  6. Sales filter: keep prior-year TTM sales >= $10M USD.
  7. Scores & flags (last) — percentile within the filtered batch:
       P_f = (# strictly lower)/(N-1)*100 ; a missing field re-normalises weights.
       Top third = P >= 66.67 ; bottom third = P <= 33.33 ; deciles = 90 / 10.

Metrics (quarters newest-first; [0:4]=TTM, [4:8]=prior TTM, [8:12]=2-yr-ago TTM):
  sales_growth_ttm_vs_prior_ttm_pct = (Srev[0:4]/Srev[4:8] - 1)*100
  sales_growth_latest_q_yoy_pct     = (rev[0]/rev[4] - 1)*100
  sales_growth_ttm_accel_pp = [(Srev[0:4]/Srev[4:8]-1) - (Srev[4:8]/Srev[8:12]-1)]*100
  sales_growth_q_accel_pp   = [(rev[0]/rev[4]-1) - (rev[1]/rev[5]-1)]*100
  gross_profit_to_sales_ttm_pct     = Sgp[0:4]/Srev[0:4] *100
  fcf_to_sales_ttm_pct              = Sfcf[0:4]/Srev[0:4] *100
  total_debt_to_fcf                 = totalDebt(latest Q) / Sfcf[0:4]  (currency
                                      cancels; negative when TTM FCF < 0)
Annual (newest-first) — context, blank if < 5 annual periods:
  shares_outstanding_yoy_change_pct = (shs_a[0]/shs_a[1] - 1)*100  (+dilution/-buyback)
  worst_gm  = min over the last 5y of (gp_a[i]/rev_a[i])
  worst_fcf = min over the last 5y of (fcf_a[year]/rev_a[year])  (year-matched)
  *_vs_5yr_trough_pp = current - worst*100     (raw backup for the trough flags)

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

DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
OUT_PATH = os.path.join(DATA_DIR, "Large_Actives_with_Metrics.csv")

# growth_score: 4 equal parts.  The two LEVEL parts are floored below the batch
# top-third bar (they score 0 unless in the top third); the two ACCEL parts are not.
GROWTH_WEIGHTS = {
    "sales_growth_ttm_vs_prior_ttm_pct": 0.25,
    "sales_growth_latest_q_yoy_pct": 0.25,
    "sales_growth_ttm_accel_pp": 0.25,
    "sales_growth_q_accel_pp": 0.25,
}
GROWTH_LEVEL_FIELDS = {"sales_growth_ttm_vs_prior_ttm_pct", "sales_growth_latest_q_yoy_pct"}
# profitability_score: gross profit/sales and FCF/sales, equal weight, no floor.
PROFIT_WEIGHTS = {"gross_profit_to_sales_ttm_pct": 0.5, "fcf_to_sales_ttm_pct": 0.5}

# dynamic percentile-rank cutoffs (P is 0..100, recomputed from the batch each run)
TOP_THIRD = 200.0 / 3   # 66.67
BOT_THIRD = 100.0 / 3   # 33.33
TOP_DECILE = 90.0
BOT_DECILE = 10.0
ACCEL_BAND = 10.0       # +/- pp band for growth_context Acceleration (fixed, not ranked)

OUT_COLS = [
    "symbol", "company_name", "market_cap_usd", "ipo_date",
    "growth_score", "growth_context", "profitability_score",
    "gross_profit_vs_trough", "fcf_vs_trough", "debt_risk",
    "ev_sales_flag", "pe_flag",
    "analyst_sell_pct", "analyst_count",
    "industry", "description",
    "sales_ttm_usd",
    "sales_growth_ttm_vs_prior_ttm_pct", "sales_growth_latest_q_yoy_pct",
    "sales_growth_ttm_accel_pp", "sales_growth_q_accel_pp",
    "gross_profit_to_sales_ttm_pct", "fcf_to_sales_ttm_pct",
    "total_debt_to_fcf",
    "gross_profit_to_sales_vs_5yr_trough_pp", "fcf_to_sales_vs_5yr_trough_pp",
    "ev_to_sales_ttm", "pe_ratio_ttm",
    "shares_outstanding_yoy_change_pct",
    "exchange", "volume",
]
# sales_prior_ttm_usd is still computed in main() (it is the >=$10M filter key) but
# is not written — the growth delta already captures current-vs-prior.


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


def _ssum(lst, a, b):
    if b > len(lst):
        return None
    seg = lst[a:b]
    return None if any(v is None for v in seg) else sum(seg)


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
                              "market_cap_usd": r.get("marketCap", ""),
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
        "_fcf_ttm_local": None,
        "sales_growth_ttm_vs_prior_ttm_pct": "", "sales_growth_latest_q_yoy_pct": "",
        "sales_growth_ttm_accel_pp": "", "sales_growth_q_accel_pp": "",
        "gross_profit_to_sales_ttm_pct": "",
        "fcf_to_sales_ttm_pct": "",
        "total_debt_to_fcf": "",
        "analyst_sell_pct": "", "analyst_count": "",
        "shares_outstanding_yoy_change_pct": "",
        "gross_profit_to_sales_vs_5yr_trough_pp": "",
        "fcf_to_sales_vs_5yr_trough_pp": "",
    }

    # profile
    p = gated_get(f"{BASE}/profile?symbol={q}&apikey={API_KEY}")
    if isinstance(p, list) and p:
        out["description"] = p[0].get("description") or ""
        out["ipo_date"] = p[0].get("ipoDate") or ""

    # income-statement quarter (12) -> TTM sales/gross profit/net income + growth accel
    sales_ttm = sales_ttm_prior = None
    d = gated_get(f"{BASE}/income-statement?symbol={q}&period=quarter&limit=12&apikey={API_KEY}")
    if isinstance(d, list) and d:
        d = sorted(d, key=lambda r: r.get("date") or "", reverse=True)
        out["reportedCurrency"] = d[0].get("reportedCurrency") or ""
        rev = [_num(r.get("revenue")) for r in d]
        gp = [_num(r.get("grossProfit")) for r in d]
        ni = [_num(r.get("netIncome")) for r in d]
        rn, rp, rpp = _ssum(rev, 0, 4), _ssum(rev, 4, 8), _ssum(rev, 8, 12)
        gn = _ssum(gp, 0, 4)
        sales_ttm, sales_ttm_prior = rn, rp
        out["_sales_ttm_local"] = rn
        out["_sales_ttm_prior_local"] = rp
        out["_net_income_ttm_local"] = _ssum(ni, 0, 4)
        # levels
        if rn is not None and rp not in (None, 0):
            out["sales_growth_ttm_vs_prior_ttm_pct"] = round((rn / rp - 1) * 100, 2)
        if len(rev) >= 5 and rev[0] is not None and rev[4] not in (None, 0):
            out["sales_growth_latest_q_yoy_pct"] = round((rev[0] / rev[4] - 1) * 100, 2)
        # TTM acceleration: recent TTM growth - prior-year TTM growth (needs 12 quarters)
        if rn is not None and rp not in (None, 0) and rpp not in (None, 0):
            out["sales_growth_ttm_accel_pp"] = round(((rn / rp - 1) - (rp / rpp - 1)) * 100, 2)
        # quarterly acceleration: latest-quarter YoY - previous-quarter YoY (needs 6 quarters)
        if (len(rev) >= 6 and rev[0] is not None and rev[4] not in (None, 0)
                and rev[1] is not None and rev[5] not in (None, 0)):
            out["sales_growth_q_accel_pp"] = round(
                ((rev[0] / rev[4] - 1) - (rev[1] / rev[5] - 1)) * 100, 2)
        # gross profit / sales
        if gn is not None and rn not in (None, 0):
            out["gross_profit_to_sales_ttm_pct"] = round(gn / rn * 100, 2)

    # cash-flow quarter -> FCF/sales TTM (currency cancels); store TTM FCF for debt/FCF
    cq = gated_get(f"{BASE}/cash-flow-statement?symbol={q}&period=quarter&limit=8&apikey={API_KEY}")
    if isinstance(cq, list) and cq:
        cq = sorted(cq, key=lambda r: r.get("date") or "", reverse=True)
        fcf = [_num(r.get("freeCashFlow")) for r in cq]
        fn = _ssum(fcf, 0, 4)
        out["_fcf_ttm_local"] = fn
        if fn is not None and sales_ttm not in (None, 0):
            out["fcf_to_sales_ttm_pct"] = round(fn / sales_ttm * 100, 2)

    # balance-sheet quarter -> total debt, cash (latest)
    bs = gated_get(f"{BASE}/balance-sheet-statement?symbol={q}&period=quarter&limit=4&apikey={API_KEY}")
    if isinstance(bs, list) and bs:
        bs = sorted(bs, key=lambda r: r.get("date") or "", reverse=True)
        b0 = bs[0]
        out["_total_debt_local"] = _num(b0.get("totalDebt"))
        csh = _num(b0.get("cashAndShortTermInvestments"))
        if csh is None:
            csh = _num(b0.get("cashAndCashEquivalents"))
        out["_cash_local"] = csh
    # total debt / TTM FCF (both local -> currency cancels).  Raw multiple backup;
    # negative when TTM FCF < 0.  The debt_risk flag carries the real signal.
    td_, fcf_ = out["_total_debt_local"], out["_fcf_ttm_local"]
    if td_ is not None and fcf_ not in (None, 0):
        out["total_debt_to_fcf"] = round(td_ / fcf_, 2)

    # income-statement annual -> dilution + 5y-worst GP/sales
    wm = None
    rev_by_year = {}
    a = gated_get(f"{BASE}/income-statement?symbol={q}&period=annual&limit=8&apikey={API_KEY}")
    if isinstance(a, list) and a:
        a = sorted(a, key=lambda r: r.get("date") or "", reverse=True)
        ra = [_num(r.get("revenue")) for r in a]
        ga = [_num(r.get("grossProfit")) for r in a]
        for r in a:
            y = str(r.get("calendarYear") or (r.get("date") or "")[:4])
            rv = _num(r.get("revenue"))
            if y and rv is not None:
                rev_by_year[y] = rv
        # dilution: diluted weighted-average shares YoY (fallback to basic)
        def _shs(r):
            v = _num(r.get("weightedAverageShsOutDil"))
            if v in (None, 0):
                v = _num(r.get("weightedAverageShsOut"))
            return v
        sh = [_shs(r) for r in a]
        if len(sh) >= 2 and sh[0] is not None and sh[1] not in (None, 0):
            out["shares_outstanding_yoy_change_pct"] = round((sh[0] / sh[1] - 1) * 100, 2)
        # 5-year trough — worst single-year GP/sales over the last 5 years (needs 5)
        ms = [ga[i] / ra[i] for i in range(min(5, len(ra)))
              if ga[i] is not None and ra[i] not in (None, 0)]
        wm = min(ms) if len(ms) >= 5 else None

    # cash-flow annual -> FCF/sales 5y trough (year-matched to annual revenue)
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
            if len(margins) >= 5:
                break
        wfcf = min(margins) if len(margins) >= 5 else None

    # cyclicality context: current - worst*100 (blank if < 5 annual periods).
    # Raw backup for the gross_profit_vs_trough / fcf_vs_trough flags.
    cm = out["gross_profit_to_sales_ttm_pct"]
    cf = out["fcf_to_sales_ttm_pct"]
    if wm is not None and isinstance(cm, (int, float)):
        out["gross_profit_to_sales_vs_5yr_trough_pp"] = round(cm - wm * 100, 2)
    if wfcf is not None and isinstance(cf, (int, float)):
        out["fcf_to_sales_vs_5yr_trough_pp"] = round(cf - wfcf * 100, 2)

    # analyst grades consensus -> % sell + count
    g = gated_get(f"{BASE}/grades-consensus?symbol={q}&apikey={API_KEY}")
    if isinstance(g, list) and g:
        row = g[0]
        sb, b, h, s, ss = (_f(row.get("strongBuy")), _f(row.get("buy")), _f(row.get("hold")),
                           _f(row.get("sell")), _f(row.get("strongSell")))
        tot = sb + b + h + s + ss
        if tot > 0:
            out["analyst_sell_pct"] = round((s + ss) / tot * 100, 1)
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


# ---------------- 7. scores & flags ----------------
def _percentiles(rows, field):
    vals = sorted(r[field] for r in rows if isinstance(r.get(field), (int, float)))
    n = len(vals)
    pm = {}
    for r in rows:
        v = r.get(field)
        if isinstance(v, (int, float)):
            pm[id(r)] = 100.0 * bisect.bisect_left(vals, v) / (n - 1) if n > 1 else 50.0
    return pm


def add_debt_risk(rows):
    # HIGH = worst one-third of the universe by debt burden.  FCF<=0-with-debt is
    # automatically worst (can't service debt from cash flow at all); the rest are
    # ranked by total debt / FCF (higher = worse).  No-debt or can't-compute names
    # are never flagged.  Recomputed every run.
    target = round(len(rows) / 3)
    auto = []            # FCF <= 0 while carrying debt -> worst possible
    ranked = []          # (debt/FCF, row) for FCF > 0 with debt
    for r in rows:
        td = r.get("_total_debt_local")
        fcf = r.get("_fcf_ttm_local")
        if td is None or td <= 0 or fcf is None:
            continue
        if fcf <= 0:
            auto.append(r)
        else:
            ranked.append((td / fcf, r))
    ranked.sort(key=lambda x: x[0], reverse=True)
    flagged = {id(r) for r in auto}
    for _, r in ranked[:max(0, target - len(auto))]:
        flagged.add(id(r))
    for r in rows:
        r["debt_risk"] = "HIGH" if id(r) in flagged else ""


def add_scores_and_flags(rows):
    gmaps = {f: _percentiles(rows, f) for f in GROWTH_WEIGHTS}
    pmaps = {f: _percentiles(rows, f) for f in PROFIT_WEIGHTS}
    ann = gmaps["sales_growth_ttm_vs_prior_ttm_pct"]
    qtr = gmaps["sales_growth_latest_q_yoy_pct"]
    ev_map = _percentiles(rows, "ev_to_sales_ttm")
    pe_map = _percentiles(rows, "pe_ratio_ttm")
    gp_tr = _percentiles(rows, "gross_profit_to_sales_vs_5yr_trough_pp")
    fcf_tr = _percentiles(rows, "fcf_to_sales_vs_5yr_trough_pp")

    for r in rows:
        rid = id(r)

        # growth_score — the two LEVEL parts score 0 below the batch top third.
        num = den = 0.0
        for f, w in GROWTH_WEIGHTS.items():
            if rid in gmaps[f]:
                p = gmaps[f][rid]
                contrib = 0.0 if (f in GROWTH_LEVEL_FIELDS and p < TOP_THIRD) else p
                num += w * contrib
                den += w
        r["growth_score"] = round(num / den, 1) if den > 0 else ""

        # profitability_score — 50/50 percentiles of gross profit/sales and FCF/sales.
        num = den = 0.0
        for f, w in PROFIT_WEIGHTS.items():
            if rid in pmaps[f]:
                num += w * pmaps[f][rid]
                den += w
        r["profitability_score"] = round(num / den, 1) if den > 0 else ""

        # growth_context = Base · Acceleration · Alignment (built from existing columns).
        base = ("Strong" if ann[rid] >= TOP_THIRD else "Weak") if rid in ann else "n/a"
        av = r.get("sales_growth_ttm_accel_pp")
        if isinstance(av, (int, float)):
            accel = ("Accelerating" if av > ACCEL_BAND
                     else "Decelerating" if av < -ACCEL_BAND else "Steady")
        else:
            accel = "n/a"
        if rid in ann and rid in qtr:
            align = "Aligned" if (ann[rid] >= TOP_THIRD) == (qtr[rid] >= TOP_THIRD) else "Not aligned"
        else:
            align = "n/a"
        r["growth_context"] = f"{base} · {accel} · {align}"

        # trough flags — extremes only (top / bottom decile of the vs-trough delta).
        for src, col in ((gp_tr, "gross_profit_vs_trough"), (fcf_tr, "fcf_vs_trough")):
            if rid in src:
                p = src[rid]
                r[col] = "High" if p >= TOP_DECILE else "Low" if p <= BOT_DECILE else ""
            else:
                r[col] = ""

        # affordability flags — thirds.  Low = cheap (low percentile), High = pricey.
        if rid in ev_map:
            p = ev_map[rid]
            r["ev_sales_flag"] = "Low" if p <= BOT_THIRD else "High" if p >= TOP_THIRD else ""
        else:
            r["ev_sales_flag"] = ""
        if isinstance(r.get("pe_ratio_ttm"), (int, float)):
            p = pe_map[rid]
            r["pe_flag"] = "Low" if p <= BOT_THIRD else "High" if p >= TOP_THIRD else ""
        else:
            r["pe_flag"] = "None"

    add_debt_risk(rows)


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
    add_scores_and_flags(kept)
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

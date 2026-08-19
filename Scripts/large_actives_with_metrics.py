#!/usr/bin/env python3
"""
Large Actives with Metrics — STANDALONE (no file reads).

The Active Stock Universe (majors + OTC/PNK, active common stock) put through
three filters plus an industry exclusion, enriched per-symbol, then ranked by
percentile on every axis for a research-triage dashboard.  The one decision the
sheet supports: "is this worth researching in depth?"  So it exposes each axis as
a raw value AND its percentile rank within the batch — never a black-box score.

  filters:
      market cap        >= $1B
      dollar volume     >= $1M / day   (price x volume, from the screener)
      prior-year sales  >= $10M USD    (after currency conversion)

  industry exclusion (EXCLUDED_INDUSTRIES, applied BEFORE enrichment):
      Removes industries whose metrics are non-comparable or whose "growth" is
      not real-demand, so they don't pollute the percentile scale:
        - balance-sheet / special-accounting financials (banks, insurers, asset
          managers, REITs, real-estate operators).  KEPT: the asset-light
          fee-based infrastructure — Financial - Data & Stock Exchanges and
          Financial - Credit Services (payment networks).
        - monetary / precious metals (Gold, Silver, Other Precious Metals) —
          price-driven, no productive utility.  Industrial commodities (copper,
          uranium, steel, ...) are KEPT — real utility; metrics sort the laggards.
        - Biotechnology — binary trial-outcome lottery.  (Big pharma is a
          different industry and is kept.)

  percentile columns (0-100, HIGHER = BETTER, recomputed from the batch each run;
  P = (# strictly lower)/(N-1)*100; a missing field drops out and re-normalises):
      pctl_growth_ttm       TTM vs prior-TTM sales growth        (level, stable)
      pctl_growth_latest_q  latest-quarter YoY growth            (level, recent)
      pctl_accel_ttm        TTM growth - prior-TTM growth        (accel, stable)
      pctl_accel_4q         latest-Q YoY - year-ago-Q YoY        (accel, recent)
      pctl_gross_margin     gross profit / sales TTM
      pctl_fcf_margin       FCF / sales TTM
      pctl_ev_sales         EV/Sales  (INVERTED: cheaper -> higher percentile)
      pctl_gm_vs_trough     GP margin - 5yr trough   (INVERTED: near trough=higher;
      pctl_fcf_vs_trough    FCF margin - 5yr trough   context only, not in composite.
                            NB non-monotonic at the extreme — a delta below the 5yr
                            trough is a fresh low; read it against the raw delta.)

  composite (the default sort; every axis is still its own visible column):
      growth 0.50 · profitability 0.30 · affordability 0.20
        growth = 0.5*level + 0.5*accel   (stable & recent get equal voice, so the
          level = avg(pctl_growth_ttm, pctl_growth_latest_q)   ranking is not just
          accel = avg(pctl_accel_ttm, pctl_accel_4q)           a lagging indicator)
        profitability = avg(pctl_gross_margin, pctl_fcf_margin)
        affordability = pctl_ev_sales
      Debt is NOT in the composite — it is a standalone risk flag.

  flags kept:
      debt_flag    "neg FCF"   -> total debt > 0 but TTM FCF <= 0 (can't service
                                  debt from cash flow at all)
                   "high >10x" -> TTM FCF > 0 and total debt / FCF > DEBT_FCF_FLAG
                   ""          -> otherwise
      analyst_sell_pct / analyst_count  (from grades-consensus)
      raw pe_ratio_ttm is kept (no P/E flag)

Flow (exact order):
  1. Baseline: own screener pull, one call per exchange
       {NASDAQ, NYSE, AMEX, OTC, PNK} & isEtf=false & isFund=false
       & isActivelyTrading=true & marketCapMoreThan=$1B.  The market-cap floor is
       applied server-side (before the screener's 10k row cap) so the OTC/PNK
       small-cap flood never truncates the large caps we keep.  A call still
       returning >= 10,000 STOPS and flags.
  2. Filter: drop EXCLUDED_INDUSTRIES, then keep marketCap >= $1B AND
       price*volume >= $1M/day (both from screener).  The industry drop happens
       here so excluded names never cost enrichment calls.
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
       denominator so the currency cancels.  If a non-USD currency's FX rate does
       NOT resolve, the USD-derived fields are BLANKED (never assumed at parity),
       which drops the name at the sales filter rather than shipping bad USD data.
  5. EV/Sales and P/E are computed IN-HOUSE in USD (not taken from FMP TTM
       endpoints, which mix USD price with local-currency financials):
         ev_to_sales_ttm = (market_cap + total_debt - cash) / sales_ttm     [all USD]
         pe_ratio_ttm    =  market_cap / net_income_ttm                     [all USD]
       EV/Sales is present for every name with debt; P/E blank when TTM NI <= 0.
  6. Sales filter: keep prior-year TTM sales >= $10M USD.
  7. Percentiles & composite (last) — computed within the filtered batch.

Metrics (quarters newest-first; [0:4]=TTM, [4:8]=prior TTM, [8:12]=2-yr-ago TTM):
  sales_growth_ttm_vs_prior_ttm_pct = (Srev[0:4]/Srev[4:8] - 1)*100
  sales_growth_latest_q_yoy_pct     = (rev[0]/rev[4] - 1)*100
  sales_growth_ttm_accel_pp = [(Srev[0:4]/Srev[4:8]-1) - (Srev[4:8]/Srev[8:12]-1)]*100
  sales_growth_4q_net_accel_pp = [(rev[0]/rev[4]-1) - (rev[4]/rev[8]-1)]*100
       Net acceleration over the last 4 quarters.  Summing the four consecutive
       quarter-over-quarter accelerations telescopes to this two-point endpoint
       difference (the intermediate quarters cancel), needing rev[0], rev[4], rev[8].
  gross_profit_to_sales_ttm_pct     = Sgp[0:4]/Srev[0:4] *100
  fcf_to_sales_ttm_pct              = Sfcf[0:4]/Srev[0:4] *100
  total_debt_to_fcf                 = totalDebt(latest Q) / Sfcf[0:4]  (currency
                                      cancels; negative when TTM FCF < 0)
Annual (newest-first) — context, blank if < 5 annual periods:
  shares_outstanding_yoy_change_pct = (shs_a[0]/shs_a[1] - 1)*100  (+dilution/-buyback)
  worst_gm  = min over the last 5y of (gp_a[i]/rev_a[i])
  worst_fcf = min over the last 5y of (fcf_a[year]/rev_a[year])  (year-matched)
  *_vs_5yr_trough_pp = current - worst*100     (raw backup for the trough percentiles)

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
DIGEST_PATH = os.path.join(DATA_DIR, "digest_stock_reference.csv")

# Industries removed BEFORE enrichment — non-comparable accounting, monetary
# commodities, or lottery-outcome names that would pollute the percentile scale.
# Exact-match against the screener's `industry` field (strings verified against the
# data — a typo here silently fails to exclude).  KEPT on purpose: the asset-light
# fee-based financials (Financial - Data & Stock Exchanges, Financial - Credit
# Services) and every industrial commodity (Copper, Uranium, Steel, Aluminum, ...).
EXCLUDED_INDUSTRIES = {
    # balance-sheet / special-accounting financials
    "Banks - Regional", "Banks - Diversified", "Banks",
    "Asset Management", "Asset Management - Cryptocurrency",
    "Financial - Capital Markets", "Financial - Mortgages",
    "Financial - Diversified", "Financial - Conglomerates",
    "Investment - Banking & Investment Services",
    "Insurance - Property & Casualty", "Insurance - Diversified", "Insurance - Life",
    "Insurance - Specialty", "Insurance - Brokers", "Insurance - Reinsurance",
    # real estate: REITs (FFO not FCF) + operators
    "REIT - Retail", "REIT - Specialty", "REIT - Industrial", "REIT - Residential",
    "REIT - Mortgage", "REIT - Healthcare Facilities", "REIT - Office",
    "REIT - Hotel & Motel", "REIT - Diversified",
    "Real Estate - Services", "Real Estate - Development", "Real Estate - Diversified",
    # monetary / precious metals (price-driven, no productive utility)
    "Gold", "Silver", "Other Precious Metals",
    # binary trial-outcome lottery (big pharma is a different industry, kept)
    "Biotechnology",
}

# composite pillar weights (growth is #1, then profitability, then affordability;
# debt risk is a standalone flag, never folded into the composite).
PILLAR_WEIGHTS = {"growth": 0.50, "profit": 0.30, "afford": 0.20}

# debt_flag threshold: an absolute, legible line (not a floating "worst third").
# With gross debt and post-capex FCF, >10x means >10 years of free cash to retire
# gross debt.  Recomputed nowhere — the number is the number, run to run.
DEBT_FCF_FLAG = 10

OUT_COLS = [
    # identity + the at-a-glance decision block
    "symbol", "company_name", "industry", "market_cap_usd",
    "composite",
    "pctl_growth_ttm", "pctl_growth_latest_q", "pctl_accel_ttm", "pctl_accel_4q",
    "pctl_gross_margin", "pctl_fcf_margin", "pctl_ev_sales",
    "pctl_gm_vs_trough", "pctl_fcf_vs_trough",
    "debt_flag", "analyst_sell_pct", "analyst_count",
    "ipo_date",
    # raw values behind the percentiles (drill-down)
    "sales_ttm_usd",
    "sales_growth_ttm_vs_prior_ttm_pct", "sales_growth_latest_q_yoy_pct",
    "sales_growth_ttm_accel_pp", "sales_growth_4q_net_accel_pp",
    "gross_profit_to_sales_ttm_pct", "fcf_to_sales_ttm_pct",
    "total_debt_to_fcf",
    "gross_profit_to_sales_vs_5yr_trough_pp", "fcf_to_sales_vs_5yr_trough_pp",
    "ev_to_sales_ttm", "pe_ratio_ttm",
    "shares_outstanding_yoy_change_pct",
    "exchange", "volume", "description",
]
# sales_prior_ttm_usd is still computed in main() (it is the >=$10M filter key) but
# is not written — the growth delta already captures current-vs-prior.

# Stripped-down reference written alongside the full CSV on every run — raw growth,
# margin and valuation numbers only (no scores/percentiles), same row set.
DIGEST_COLS = [
    "symbol", "company_name",
    "sales_growth_ttm_vs_prior_ttm_pct", "sales_growth_latest_q_yoy_pct",
    "sales_growth_ttm_accel_pp", "sales_growth_4q_net_accel_pp",
    "gross_profit_to_sales_ttm_pct", "fcf_to_sales_ttm_pct",
    "ev_to_sales_ttm", "pe_ratio_ttm",
]


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
            # 429 (rate limit) and 5xx (transient server errors) are retried with
            # backoff; other non-200s (e.g. 404 = no data) legitimately return None.
            if r.status_code == 429 or r.status_code >= 500:
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


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


# ---------------- 1-2. baseline + industry exclusion + cap/$-vol filters ----------------
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
    # Drop excluded industries here (before enrichment) so they never cost API calls
    # and never enter the percentile population.
    n_excl = sum(1 for r in active if (r.get("industry") or "").strip() in EXCLUDED_INDUSTRIES)
    large = [r for r in active
             if (r.get("industry") or "").strip() not in EXCLUDED_INDUSTRIES
             and _f(r["market_cap_usd"]) >= MIN_MARKET_CAP
             and _f(r["_price"]) * _f(r["volume"]) >= MIN_DOLLAR_VOLUME]
    for r in large:
        r.pop("_price", None)
    print(f"Active universe: {len(active):,}  ->  excluded industries: -{n_excl:,}  ->  "
          f"marketCap>=$1B & $-vol>=$1M/day: {len(large):,}")
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
        "sales_growth_ttm_accel_pp": "", "sales_growth_4q_net_accel_pp": "",
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
        # 4-quarter net acceleration: latest-Q YoY minus year-ago-Q YoY.  Summing the
        # four consecutive quarter-over-quarter accelerations telescopes to this
        # two-point endpoint difference (needs rev[0], rev[4], rev[8]).
        if (len(rev) >= 9 and rev[0] is not None and rev[4] not in (None, 0)
                and rev[8] not in (None, 0)):
            out["sales_growth_4q_net_accel_pp"] = round(
                ((rev[0] / rev[4] - 1) - (rev[4] / rev[8] - 1)) * 100, 2)
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
    # negative when TTM FCF < 0.  The debt_flag carries the real signal.
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
    # Raw backup for the pctl_gm_vs_trough / pctl_fcf_vs_trough percentiles.
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


# ---------------- 7. percentiles, composite & flags ----------------
def _percentiles(rows, field, invert=False):
    # P = (# strictly lower)/(N-1)*100, so higher raw value -> higher percentile.
    # invert=True flips it (100 - P) for fields where LOWER raw is better
    # (EV/Sales, vs-trough deltas), keeping the convention higher percentile = better.
    vals = sorted(r[field] for r in rows if isinstance(r.get(field), (int, float)))
    n = len(vals)
    pm = {}
    for r in rows:
        v = r.get(field)
        if isinstance(v, (int, float)):
            p = 100.0 * bisect.bisect_left(vals, v) / (n - 1) if n > 1 else 50.0
            pm[id(r)] = 100.0 - p if invert else p
    return pm


def add_debt_flag(rows):
    # Absolute, legible risk line.  "neg FCF" = carries debt but TTM FCF <= 0 (can't
    # service debt from cash flow at all); "high >Nx" = total debt / FCF above cutoff.
    # No-debt or can't-compute names are never flagged.
    label = f"high >{DEBT_FCF_FLAG:g}x"
    for r in rows:
        td = r.get("_total_debt_local")
        fcf = r.get("_fcf_ttm_local")
        flag = ""
        if td is not None and td > 0 and fcf is not None:
            if fcf <= 0:
                flag = "neg FCF"
            elif td / fcf > DEBT_FCF_FLAG:
                flag = label
        r["debt_flag"] = flag


def add_scores_and_flags(rows):
    # Every axis becomes a percentile within the filtered batch (higher = better).
    P = {
        "pctl_growth_ttm":      _percentiles(rows, "sales_growth_ttm_vs_prior_ttm_pct"),
        "pctl_growth_latest_q": _percentiles(rows, "sales_growth_latest_q_yoy_pct"),
        "pctl_accel_ttm":       _percentiles(rows, "sales_growth_ttm_accel_pp"),
        "pctl_accel_4q":        _percentiles(rows, "sales_growth_4q_net_accel_pp"),
        "pctl_gross_margin":    _percentiles(rows, "gross_profit_to_sales_ttm_pct"),
        "pctl_fcf_margin":      _percentiles(rows, "fcf_to_sales_ttm_pct"),
        # lower raw is better -> inverted so higher percentile = better
        "pctl_ev_sales":        _percentiles(rows, "ev_to_sales_ttm", invert=True),
        "pctl_gm_vs_trough":    _percentiles(rows, "gross_profit_to_sales_vs_5yr_trough_pp", invert=True),
        "pctl_fcf_vs_trough":   _percentiles(rows, "fcf_to_sales_vs_5yr_trough_pp", invert=True),
    }
    wg, wp, wa = PILLAR_WEIGHTS["growth"], PILLAR_WEIGHTS["profit"], PILLAR_WEIGHTS["afford"]
    for r in rows:
        rid = id(r)
        for col, pm in P.items():
            r[col] = round(pm[rid], 1) if rid in pm else ""

        # composite — growth 0.50 / profitability 0.30 / affordability 0.20.
        # growth = 0.5*level + 0.5*accel so stable & recent signals get equal voice
        # (keeps the ranking from being a pure lagging indicator).  vs-trough
        # percentiles are context columns only and are NOT part of the composite.
        level = _mean([P["pctl_growth_ttm"].get(rid), P["pctl_growth_latest_q"].get(rid)])
        accel = _mean([P["pctl_accel_ttm"].get(rid), P["pctl_accel_4q"].get(rid)])
        growth = _mean([level, accel])
        profit = _mean([P["pctl_gross_margin"].get(rid), P["pctl_fcf_margin"].get(rid)])
        afford = P["pctl_ev_sales"].get(rid)
        num = den = 0.0
        for val, w in ((growth, wg), (profit, wp), (afford, wa)):
            if val is not None:
                num += val * w
                den += w
        r["composite"] = round(num / den, 1) if den > 0 else ""

    add_debt_flag(rows)


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

    fx_blanked = 0
    for r in merged:
        cur = r.get("reportedCurrency")
        rate = fx.get(cur)
        # FX policy: USD (or no currency at all) -> 1.0.  A real non-USD currency
        # whose rate did NOT resolve -> blank the USD-derived fields; never assume
        # parity (that would silently ship ~100-1000x-wrong sales/EV/PE).
        if cur in (None, "", "USD"):
            rate_eff, fx_ok = 1.0, True
        elif rate:
            rate_eff, fx_ok = rate, True
        else:
            rate_eff, fx_ok = None, False
        mc = _f(r.get("market_cap_usd"))
        sl, spl = r.get("_sales_ttm_local"), r.get("_sales_ttm_prior_local")
        if not fx_ok and sl is not None:
            fx_blanked += 1
        r["sales_ttm_usd"] = int(sl * rate_eff) if (fx_ok and sl is not None) else ""
        r["sales_prior_ttm_usd"] = int(spl * rate_eff) if (fx_ok and spl is not None) else ""
        # P/E = market cap / TTM net income (both USD); blank when no TTM profit
        ni = r.get("_net_income_ttm_local")
        if fx_ok and ni is not None and mc > 0:
            ni_usd = ni * rate_eff
            r["pe_ratio_ttm"] = round(mc / ni_usd, 2) if ni_usd > 0 else ""
        else:
            r["pe_ratio_ttm"] = ""
        # EV/Sales = (market cap + total debt - cash) / TTM sales (all USD)
        td, csh, su = r.get("_total_debt_local"), r.get("_cash_local"), r["sales_ttm_usd"]
        if fx_ok and isinstance(su, int) and su > 0 and td is not None and mc > 0:
            ev_usd = mc + td * rate_eff - (csh or 0.0) * rate_eff
            r["ev_to_sales_ttm"] = round(ev_usd / su, 2)
        else:
            r["ev_to_sales_ttm"] = ""
        r["market_cap_usd"] = int(mc)

    kept = [r for r in merged if isinstance(r.get("sales_prior_ttm_usd"), int)
            and r["sales_prior_ttm_usd"] >= MIN_PRIOR_SALES_USD]
    add_scores_and_flags(kept)
    kept.sort(key=lambda r: (r["composite"] if isinstance(r["composite"], (int, float)) else -1),
              reverse=True)

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    # side effect: stripped-down digest (same rows, 10 raw reference columns)
    with open(DIGEST_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=DIGEST_COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    print("\n================== LARGE ACTIVES WITH METRICS ==================")
    print(f"Saved: {OUT_PATH}")
    print(f"Saved: {DIGEST_PATH}")
    print(f"Baseline (>=$1B & >=$1M/day $-vol, excl. industries): {total:,}  |  "
          f"dropped (prior sales < $10M USD): {total-len(kept):,}  |  kept: {len(kept):,}")
    if fx_blanked:
        print(f"FX unresolved -> USD fields blanked (name dropped): {fx_blanked:,}")
    print(f"Elapsed: {(time.monotonic()-t0)/60:.1f} min  |  columns: {len(OUT_COLS)}")
    print("===============================================================")


if __name__ == "__main__":
    main()

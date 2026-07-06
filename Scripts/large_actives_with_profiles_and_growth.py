#!/usr/bin/env python3
"""
Large Actives with Profiles and Growth — STANDALONE (no file reads).

It is the Active Stock Universe (majors + OTC/PNK, active common) plus THREE
filters, additional data, a ranking score, and two cyclicality-context columns:

  filters (all in this script):
      market cap        >= $1B
      dollar volume     >= $1M / day   (price x volume, from the screener)
      prior-year sales  >= $10M USD    (after currency conversion)
  added data : profile fields + sales figures + growth/margin metrics
  score      : GrowthScore
  context    : sales_growth_vs_7y_worst_pp, gp_to_sales_vs_7y_worst_pp (not scored)

Flow (exact order):
  1. Baseline: own screener pull, one call per exchange
       {NASDAQ, NYSE, AMEX, OTC, PNK} & isEtf=false & isFund=false
       & isActivelyTrading=true.  A call returning >= 10,000 STOPS and flags.
  2. Filter: marketCap >= $1B AND price*volume >= $1M/day (both from screener).
  3. Per surviving symbol, 3 calls:
       /profile                          -> description, ipoDate, ceo
       /income-statement period=quarter  -> local sales, currency, TTM metrics
       /income-statement period=annual   -> 7y-worst growth / gross margin
  4. Currency -> USD: /quote-short per distinct currency; convert sales_ttm and
       sales_ttm_prior to USD, 100% complete, BEFORE any sales filtering.
  5. Sales filter: keep prior-year TTM sales >= $10M USD.
  6. GrowthScore (last) — percentile blend within the filtered batch:
       P_f = (# strictly lower)/(N-1)*100
       0.40*P(sales_growth_ttm) + 0.30*P(sales_growth_q)
       + 0.15*P(gp_to_sales_ttm) + 0.15*P(gp_to_sales_chg)
       missing field -> re-normalise the present weights.

Metrics (quarters newest-first; [0:4]=TTM, [4:8]=prior TTM):
  sales_growth_ttm_pct   = (Srev[0:4]/Srev[4:8] - 1)*100
  sales_growth_q_yoy_pct = (rev[0]/rev[4] - 1)*100
  gp_to_sales_ttm_pct    = Sgp[0:4]/Srev[0:4] *100
  gp_to_sales_chg_yoy_pp = (Sgp[0:4]/Srev[0:4] - Sgp[4:8]/Srev[4:8])*100
Cyclicality (annual array, newest-first; large = current far above its 7y low):
  worst_growth = min over up to 7 of (rev_a[i]/rev_a[i+1] - 1)
  worst_gm     = min over up to 7 of (gp_a[i]/rev_a[i])
  sales_growth_vs_7y_worst_pp = sales_growth_ttm_pct - worst_growth*100
  gp_to_sales_vs_7y_worst_pp  = gp_to_sales_ttm_pct  - worst_gm*100
  blank both if years-since-IPO < 7 (unreliable trough on short history).
Growth/margin/cyclicality are ratios (currency cancels); only raw sales get
FX-converted (spot rate on TTM -> approximate, fine for a $10M floor).

Saves:   Large_Actives_with_Profiles_and_Growth.csv  (repo root)
API key: FMP_API_KEY.  ~27 min (3 calls/symbol + FX).
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
TODAY = date.today()

DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
OUT_PATH = os.path.join(DATA_DIR, "Large_Actives_with_Profiles_and_Growth.csv")
BASE_COLS = ["symbol", "companyName", "marketCap", "sector", "industry", "volume", "exchange"]
SCORE_WEIGHTS = {"sales_growth_ttm_pct": 0.40, "sales_growth_q_yoy_pct": 0.30,
                 "gp_to_sales_ttm_pct": 0.15, "gp_to_sales_chg_yoy_pp": 0.15}
OUT_COLS = ["symbol", "companyName", "sector", "industry", "volume", "exchange",
            "description", "ipoDate", "ceo", "marketCap", "GrowthScore",
            "sales_ttm", "sales_ttm_prior", "sales_growth_ttm_pct",
            "sales_growth_q_yoy_pct", "gp_to_sales_ttm_pct", "gp_to_sales_chg_yoy_pp",
            "sales_growth_vs_7y_worst_pp", "gp_to_sales_vs_7y_worst_pp"]


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


# ---------------- 1-2. baseline + market-cap & dollar-volume filters ----------------
def screener(exchange):
    q = {"exchange": exchange, "isEtf": "false", "isFund": "false",
         "isActivelyTrading": "true", "limit": LIM, "apikey": API_KEY}
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
            by_symbol[sym] = {"symbol": sym, "companyName": r.get("companyName", ""),
                              "marketCap": r.get("marketCap", ""), "sector": r.get("sector", ""),
                              "industry": r.get("industry", ""), "volume": r.get("volume", ""),
                              "exchange": ex, "_price": r.get("price", "")}
    active = list(by_symbol.values())
    large = [r for r in active
             if _f(r["marketCap"]) >= MIN_MARKET_CAP
             and _f(r["_price"]) * _f(r["volume"]) >= MIN_DOLLAR_VOLUME]
    for r in large:
        r.pop("_price", None)
    print(f"Active universe: {len(active):,}  ->  marketCap>=$1B & $-vol>=$1M/day: {len(large):,}")
    return large


# ---------------- 3. per-symbol profile + quarterly + annual ----------------
def _ssum(lst, a, b):
    if b > len(lst):
        return None
    seg = lst[a:b]
    return None if any(v is None for v in seg) else sum(seg)


def enrich(symbol):
    out = {"description": "", "ipoDate": "", "ceo": "", "reportedCurrency": "",
           "_sales_ttm_local": None, "_sales_ttm_prior_local": None,
           "sales_growth_ttm_pct": "", "sales_growth_q_yoy_pct": "",
           "gp_to_sales_ttm_pct": "", "gp_to_sales_chg_yoy_pp": "",
           "sales_growth_vs_7y_worst_pp": "", "gp_to_sales_vs_7y_worst_pp": ""}
    p = gated_get(f"{BASE}/profile?symbol={requests.utils.quote(symbol)}&apikey={API_KEY}")
    if isinstance(p, list) and p:
        out["description"] = p[0].get("description") or ""
        out["ipoDate"] = p[0].get("ipoDate") or ""
        out["ceo"] = p[0].get("ceo") or ""

    d = gated_get(f"{BASE}/income-statement?symbol={requests.utils.quote(symbol)}"
                  f"&period=quarter&limit=8&apikey={API_KEY}")
    if isinstance(d, list) and d:
        d = sorted(d, key=lambda r: r.get("date") or "", reverse=True)
        out["reportedCurrency"] = d[0].get("reportedCurrency") or ""
        rev = [_num(r.get("revenue")) for r in d]
        gp = [_num(r.get("grossProfit")) for r in d]
        rn, rp = _ssum(rev, 0, 4), _ssum(rev, 4, 8)
        gn, gpp = _ssum(gp, 0, 4), _ssum(gp, 4, 8)
        out["_sales_ttm_local"] = rn
        out["_sales_ttm_prior_local"] = rp
        if rn is not None and rp not in (None, 0):
            out["sales_growth_ttm_pct"] = round((rn / rp - 1) * 100, 2)
        if len(rev) >= 5 and rev[0] is not None and rev[4] not in (None, 0):
            out["sales_growth_q_yoy_pct"] = round((rev[0] / rev[4] - 1) * 100, 2)
        if gn is not None and rn not in (None, 0):
            out["gp_to_sales_ttm_pct"] = round(gn / rn * 100, 2)
        if gn is not None and rn not in (None, 0) and gpp is not None and rp not in (None, 0):
            out["gp_to_sales_chg_yoy_pp"] = round((gn / rn - gpp / rp) * 100, 2)

    # annual -> 7y-worst context (blank if < 7 years since IPO)
    a = gated_get(f"{BASE}/income-statement?symbol={requests.utils.quote(symbol)}"
                  f"&period=annual&limit=8&apikey={API_KEY}")
    if isinstance(a, list) and a:
        a = sorted(a, key=lambda r: r.get("date") or "", reverse=True)
        ra = [_num(r.get("revenue")) for r in a]
        ga = [_num(r.get("grossProfit")) for r in a]
        gs = [ra[i] / ra[i + 1] - 1 for i in range(min(7, len(ra) - 1))
              if ra[i] is not None and ra[i + 1] not in (None, 0)]
        ms = [ga[i] / ra[i] for i in range(min(7, len(ra)))
              if ga[i] is not None and ra[i] not in (None, 0)]
        wg = min(gs) if gs else None
        wm = min(ms) if ms else None
        yrs = years_since_ipo(out["ipoDate"])
        short = (yrs is not None and yrs < 7) or (yrs is None and len(a) < 8)
        if not short:
            cg, cm = out["sales_growth_ttm_pct"], out["gp_to_sales_ttm_pct"]
            if isinstance(cg, (int, float)) and wg is not None:
                out["sales_growth_vs_7y_worst_pp"] = round(cg - wg * 100, 2)
            if isinstance(cm, (int, float)) and wm is not None:
                out["gp_to_sales_vs_7y_worst_pp"] = round(cm - wm * 100, 2)
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


# ---------------- 6. score ----------------
def add_growth_score(rows):
    pmap = {}
    for fld in SCORE_WEIGHTS:
        vals = sorted(r[fld] for r in rows if isinstance(r.get(fld), (int, float)))
        n = len(vals)
        pmap[fld] = {}
        for r in rows:
            v = r.get(fld)
            if isinstance(v, (int, float)):
                pmap[fld][id(r)] = 100.0 * bisect.bisect_left(vals, v) / (n - 1) if n > 1 else 50.0
    for r in rows:
        num = den = 0.0
        for fld in SCORE_WEIGHTS:
            if id(r) in pmap[fld]:
                num += SCORE_WEIGHTS[fld] * pmap[fld][id(r)]
                den += SCORE_WEIGHTS[fld]
        r["GrowthScore"] = round(num / den, 1) if den > 0 else ""


def main():
    if not API_KEY:
        sys.exit("FMP_API_KEY is not set in the environment.")
    os.makedirs(DATA_DIR, exist_ok=True)

    base = get_baseline()
    total = len(base)
    print(f"Enriching {total:,} names (3 calls each, ~{3*total/RATE_PER_SEC/60:.1f} min)...")
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
        for lk, uk in (("_sales_ttm_local", "sales_ttm"), ("_sales_ttm_prior_local", "sales_ttm_prior")):
            v = r.get(lk)
            r[uk] = "" if v is None else int(v * rate) if rate else int(v)

    kept = [r for r in merged if isinstance(r.get("sales_ttm_prior"), int) and r["sales_ttm_prior"] >= MIN_PRIOR_SALES_USD]
    add_growth_score(kept)
    kept.sort(key=lambda r: (r["GrowthScore"] if isinstance(r["GrowthScore"], (int, float)) else -1), reverse=True)

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    print("\n========== LARGE ACTIVES WITH PROFILES AND GROWTH ==========")
    print(f"Saved: {OUT_PATH}")
    print(f"Baseline (>=$1B & >=$1M/day $-vol): {total:,}  |  dropped (prior sales < $10M USD): {total-len(kept):,}  |  kept: {len(kept):,}")
    print(f"Elapsed: {(time.monotonic()-t0)/60:.1f} min  |  columns: {len(OUT_COLS)}")
    print("============================================================")


if __name__ == "__main__":
    main()

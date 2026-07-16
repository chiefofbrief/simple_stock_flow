#!/usr/bin/env python3
"""
Master Stock Universe — the full, UNFILTERED US universe from FMP's screener.

Every type (common + ETF + fund), every US exchange (NASDAQ, NYSE, AMEX, CBOE,
OTC, PNK), both trading states. isEtf / isFund / isActivelyTrading are columns
so you can see exactly why anything would be filtered, and audit for wrongful
exclusions.

The screener caps at 10,000 rows/call. Each exchange is pulled in type slices
(ETF / fund / common); any slice that hits the cap is split by trading state.
This partitioning (never marketCap bucketing) means null-marketCap names are
never lost.

Saves to:   Master_Stock_Universe.csv  (repo root)
Columns:    symbol, companyName, marketCap, sector, industry, volume,
            exchange, isEtf, isFund, isActivelyTrading
API key:    FMP_API_KEY environment variable

Independent — does not read or depend on any other script or file.
"""
import csv
import os
import sys
from collections import Counter

import requests

BASE = "https://financialmodelingprep.com/stable"
API_KEY = os.environ.get("FMP_API_KEY")
EXCHANGES = ["NASDAQ", "NYSE", "AMEX", "CBOE", "OTC", "PNK"]
TYPE_SLICES = [
    ("etf",    {"isEtf": "true"}),
    ("fund",   {"isFund": "true"}),
    ("common", {"isEtf": "false", "isFund": "false"}),
]
LIM = 200000
CAP = 10000
TIMEOUT = 180

OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
OUT_PATH = os.path.join(OUT_DIR, "Master_Stock_Universe.csv")
FIELDS = ["symbol", "companyName", "marketCap", "sector", "industry", "volume",
          "exchange", "isEtf", "isFund", "isActivelyTrading"]


def fetch(exchange, params, active=None):
    q = {"exchange": exchange, "limit": LIM, **params}
    if active is not None:
        q["isActivelyTrading"] = "true" if active else "false"
    q["apikey"] = API_KEY
    url = f"{BASE}/company-screener?" + "&".join(f"{k}={v}" for k, v in q.items())
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    d = r.json()
    if not isinstance(d, list):
        raise RuntimeError(f"unexpected response {exchange} {params}: {str(d)[:160]}")
    return d


def collect_slice(exchange, label, params):
    d = fetch(exchange, params)
    if len(d) >= CAP:
        out = []
        for act in (True, False):
            chunk = fetch(exchange, params, act)
            if len(chunk) >= CAP:
                print(f"    WARNING: {exchange}/{label}/{'active' if act else 'delisted'} "
                      f"still at cap ({len(chunk)}) — may be truncated.")
            out += chunk
        return out
    return d


def main():
    if not API_KEY:
        sys.exit("FMP_API_KEY is not set in the environment.")
    os.makedirs(OUT_DIR, exist_ok=True)

    by_symbol = {}
    print("Master Stock Universe — pulling all types, all US exchanges...")
    for ex in EXCHANGES:
        added = 0
        for label, params in TYPE_SLICES:
            for r in collect_slice(ex, label, params):
                sym = (r.get("symbol") or "").strip()
                if not sym or sym in by_symbol:
                    continue
                by_symbol[sym] = {
                    "symbol": sym,
                    "companyName": r.get("companyName", ""),
                    "marketCap": r.get("marketCap", ""),
                    "sector": r.get("sector", ""),
                    "industry": r.get("industry", ""),
                    "volume": r.get("volume", ""),
                    "exchange": ex,
                    "isEtf": r.get("isEtf", ""),
                    "isFund": r.get("isFund", ""),
                    "isActivelyTrading": r.get("isActivelyTrading", ""),
                }
                added += 1
        print(f"  {ex:<7} +{added:,}  (cumulative {len(by_symbol):,})")

    rows = list(by_symbol.values())
    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    def truthy(v):
        return str(v).strip().lower() == "true"
    print("\n=============== MASTER STOCK UNIVERSE ===============")
    print(f"Saved: {OUT_PATH}")
    print(f"Total symbols: {len(rows):,}")
    print(f"  commons: {sum(1 for r in rows if not truthy(r['isEtf']) and not truthy(r['isFund'])):,}"
          f"   ETFs: {sum(1 for r in rows if truthy(r['isEtf'])):,}"
          f"   funds: {sum(1 for r in rows if truthy(r['isFund'])):,}")
    exc = Counter(r["exchange"] for r in rows)
    print("  by exchange: " + "  ".join(f"{ex} {exc.get(ex, 0):,}" for ex in EXCHANGES))
    print("====================================================")


if __name__ == "__main__":
    main()

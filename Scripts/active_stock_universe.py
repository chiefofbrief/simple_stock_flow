#!/usr/bin/env python3
"""
Active Stock Universe — live common stocks on US exchanges (majors + OTC).

Standalone. One screener call per exchange:
    exchange in {NASDAQ, NYSE, AMEX, OTC, PNK}
    & isEtf=false & isFund=false & isActivelyTrading=true

OTC and PNK are included (CBOE is not). Each exchange is a single call; if any
call returns >= 10,000 rows it has hit the screener's cap and may be truncated,
so the script STOPS and flags it (paging is a decision to make then) rather than
silently dropping names.

Saves:   Active_Stock_Universe.csv  (repo root)
Columns: symbol, companyName, marketCap, sector, industry, volume, exchange,
         isEtf, isFund, isActivelyTrading
API key: FMP_API_KEY
"""
import csv
import os
import sys
from collections import Counter

import requests

BASE = "https://financialmodelingprep.com/stable"
API_KEY = os.environ.get("FMP_API_KEY")
EXCHANGES = ["NASDAQ", "NYSE", "AMEX", "OTC", "PNK"]
LIM = 200000
CAP = 10000
TIMEOUT = 180

OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
OUT_PATH = os.path.join(OUT_DIR, "Active_Stock_Universe.csv")
FIELDS = ["symbol", "companyName", "marketCap", "sector", "industry", "volume",
          "exchange", "isEtf", "isFund", "isActivelyTrading"]


def fetch(exchange):
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
                 f"The screener truncates at {CAP}, so this exchange is likely "
                 f"incomplete. STOPPING so you can decide how to page it. ***")
    return d


def main():
    if not API_KEY:
        sys.exit("FMP_API_KEY is not set in the environment.")
    os.makedirs(OUT_DIR, exist_ok=True)

    by_symbol = {}
    print("Active Stock Universe — one call per exchange (majors + OTC/PNK)...")
    for ex in EXCHANGES:
        d = fetch(ex)
        added = 0
        for r in d:
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
        print(f"  {ex:<7} {len(d):>6,} rows (+{added:,} new, cumulative {len(by_symbol):,})")

    rows = list(by_symbol.values())
    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    print("\n=============== ACTIVE STOCK UNIVERSE ===============")
    print(f"Saved: {OUT_PATH}")
    print(f"Total: {len(rows):,}")
    exc = Counter(r["exchange"] for r in rows)
    print("By exchange: " + "  ".join(f"{ex} {exc.get(ex, 0):,}" for ex in EXCHANGES))
    print("====================================================")


if __name__ == "__main__":
    main()

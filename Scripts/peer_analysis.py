#!/usr/bin/env python3
"""
Peer Analysis Script
====================

Calls the FMP Stock Peer Comparison endpoint for every ticker in PIPELINE
and WATCHLIST, then filters results to companies that:
  1. Appear in context_ai_supply_chain.md (supply-chain validated)
  2. Are not already in the tracker

Reuses cached Data/tickers/{TICKER}/{TICKER}_peers.json where available.
Appends Priority A candidate table to Tailwind_Review_2026-04-28.md.

Usage:
    python Scripts/peer_analysis.py
"""

import os
import sys
import json
import requests
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import get_data_directory, ensure_directory_exists, save_json

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 1.5

TRACKER_PATH = "Stock_Tracker.md"
WORKING_FILE_PATH = "Tailwind_Review_2026-04-28.md"

# ---------------------------------------------------------------------------
# All tickers explicitly named in context_ai_supply_chain.md
# ---------------------------------------------------------------------------
SUPPLY_CHAIN_UNIVERSE = {
    # L1
    "MP", "CCJ", "FCX", "SCCO", "UUUU", "BWXT", "USAR",
    # L2
    "ASML", "AMAT", "LRCX", "KLAC", "CDNS", "SNPS", "ARM",
    # L3
    "TSM", "AMKR", "ASX", "INTC",
    # L4
    "NVDA", "AMD",
    # L5
    "MU", "HXSCL",
    # L6
    "AVGO", "MRVL",
    # L7
    "COHR", "ANET", "GLW", "LITE", "CSCO", "AAOI",
    # L8
    "GEV", "ETN", "BE", "VST", "CEG", "BWXT", "SMEGF",
    # L9
    "VRT", "ETN", "DLR", "EQIX", "TH", "JCI", "JBL", "IREN",
    # L10
    "AMZN", "MSFT", "GOOGL", "META",
    # L11
    "CRWV", "NBIS", "IREN",
    # L12
    "NVDA", "QCOM", "ABB", "ROK", "ISRG", "TER",
    # L13
    "PLTR", "NOW", "CRWD", "PANW", "SNOW", "DDOG", "ORCL",
    "MDB", "TEM", "IBM", "PL", "SOUN",
}

SUPPLY_CHAIN_LAYERS = {
    "MP": "L1", "CCJ": "L1/L8", "FCX": "L1", "SCCO": "L1",
    "UUUU": "L1", "BWXT": "L1/L8", "USAR": "L1",
    "ASML": "L2", "AMAT": "L2", "LRCX": "L2", "KLAC": "L2",
    "CDNS": "L2", "SNPS": "L2", "ARM": "L2/L4",
    "TSM": "L3", "AMKR": "L3", "ASX": "L3", "INTC": "L3/L4",
    "NVDA": "L4/L12", "AMD": "L4",
    "MU": "L5", "HXSCL": "L5",
    "AVGO": "L6", "MRVL": "L6/L7",
    "COHR": "L7", "ANET": "L7", "GLW": "L7", "LITE": "L7",
    "CSCO": "L7", "AAOI": "L7",
    "GEV": "L8", "ETN": "L8/L9", "BE": "L8", "VST": "L8",
    "CEG": "L8", "SMEGF": "L8",
    "VRT": "L9", "DLR": "L9", "EQIX": "L9", "TH": "L9",
    "JCI": "L9", "JBL": "L9", "IREN": "L9/L11",
    "AMZN": "L10", "MSFT": "L10", "GOOGL": "L10", "META": "L10",
    "CRWV": "L11", "NBIS": "L11",
    "QCOM": "L12", "ABB": "L12", "ROK": "L12",
    "ISRG": "L12", "TER": "L12",
    "PLTR": "L13", "NOW": "L13", "CRWD": "L13", "PANW": "L13",
    "SNOW": "L13", "DDOG": "L13", "ORCL": "L13", "MDB": "L13",
    "TEM": "L13", "IBM": "L13", "PL": "L13", "SOUN": "L13",
}


# ---------------------------------------------------------------------------
# Tracker parsing
# ---------------------------------------------------------------------------

def parse_tracker_tickers():
    """Return all tickers from PIPELINE and WATCHLIST (any tag)."""
    tickers = []
    seen = set()
    current_section = None
    in_data = False

    with open(TRACKER_PATH) as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("## PIPELINE"):
                current_section = "PIPELINE"; in_data = False
            elif stripped.startswith("## WATCHLIST"):
                current_section = "WATCHLIST"; in_data = False
            elif stripped.startswith("## "):
                current_section = None; in_data = False

            if current_section not in ("PIPELINE", "WATCHLIST"):
                continue
            if not stripped.startswith("|"):
                continue

            cells = [c.strip() for c in stripped.split("|")]
            if len(cells) < 3:
                continue
            ticker = cells[1]
            if ticker == "Ticker":
                in_data = True
                continue
            if not in_data or not ticker or ticker.replace("-", "").replace(":", "").strip() == "":
                continue
            if ticker not in seen:
                tickers.append(ticker)
                seen.add(ticker)

    return tickers


# ---------------------------------------------------------------------------
# Peer fetch (with cache)
# ---------------------------------------------------------------------------

def fetch_peers(ticker):
    cache_path = os.path.join(get_data_directory(ticker), f"{ticker}_peers.json")

    if os.path.exists(cache_path):
        print(f"  [cache] {ticker}")
        with open(cache_path) as f:
            data = json.load(f)
        if isinstance(data, list):
            return [item["symbol"] for item in data if "symbol" in item]
        return []

    url = f"{FMP_BASE}/stock-peers?symbol={ticker}&apikey={FMP_API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [peers] HTTP {r.status_code} for {ticker}")
            return []
        data = r.json()
        ensure_directory_exists(get_data_directory(ticker))
        save_json(data, cache_path)
        # Response is a flat list of peer objects: [{symbol, companyName, price, mktCap}, ...]
        if isinstance(data, list):
            return [item["symbol"] for item in data if "symbol" in item]
        return []
    except Exception as e:
        print(f"  [peers] Error for {ticker}: {e}")
        return []


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

    all_tickers = parse_tracker_tickers()
    print(f"Querying peers for {len(all_tickers)} tickers: {', '.join(all_tickers)}\n")

    # ticker -> set of source tickers that returned it as a peer
    peer_sources: dict[str, set] = {}

    for i, ticker in enumerate(all_tickers):
        print(f"[{i+1}/{len(all_tickers)}] {ticker}", end=" ", flush=True)
        if i > 0:
            time.sleep(API_CALL_DELAY)
        peers = fetch_peers(ticker)
        print(f"→ {len(peers)} peers")
        for p in peers:
            peer_sources.setdefault(p, set()).add(ticker)

    # Filter: in supply chain universe AND not already in tracker
    tracker_set = set(all_tickers)
    priority_a = {
        p: sources
        for p, sources in peer_sources.items()
        if p in SUPPLY_CHAIN_UNIVERSE and p not in tracker_set
    }

    # Already tracked supply chain peers (for reference)
    already_tracked = {
        p: sources
        for p, sources in peer_sources.items()
        if p in SUPPLY_CHAIN_UNIVERSE and p in tracker_set
    }

    # Sort by cross-validation count (most sources first)
    priority_a_sorted = sorted(
        priority_a.items(), key=lambda x: len(x[1]), reverse=True
    )

    # --- Print summary ---
    print(f"\n{'='*60}")
    print(f"PRIORITY A — supply chain validated, not in tracker ({len(priority_a_sorted)} candidates)")
    print(f"{'='*60}")
    for ticker, sources in priority_a_sorted:
        layer = SUPPLY_CHAIN_LAYERS.get(ticker, "?")
        print(f"  {ticker:8} | {layer:8} | surfaced by: {', '.join(sorted(sources))} ({len(sources)}x)")

    print(f"\nAlready-tracked supply chain peers: {', '.join(sorted(already_tracked.keys()))}")

    # --- Build markdown for working file ---
    today = datetime.now().strftime("%Y-%m-%d")
    md_rows = [
        f"\n*Peer pull executed {today}. 'Times' = number of tracker tickers that returned this peer.*\n",
        "| Ticker | Layer | Times | Surfaced By |",
        "|--------|-------|-------|-------------|",
    ]
    for ticker, sources in priority_a_sorted:
        layer = SUPPLY_CHAIN_LAYERS.get(ticker, "?")
        md_rows.append(
            f"| {ticker} | {layer} | {len(sources)} | {', '.join(sorted(sources))} |"
        )

    md_block = "\n".join(md_rows)

    # Replace the placeholder in the working file
    marker = "*Populated as FMP peer analysis runs. Format: Primary → Peer | Layer | Rationale*"
    with open(WORKING_FILE_PATH) as f:
        content = f.read()

    if marker in content:
        content = content.replace(marker, marker + "\n" + md_block, 1)
        with open(WORKING_FILE_PATH, "w") as f:
            f.write(content)
        print(f"\nResults appended to {WORKING_FILE_PATH}")
    else:
        print(f"\nWarning: marker not found in {WORKING_FILE_PATH} — printing only.")
        print(md_block)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Profile Script  (run FIRST)
===========================

Fetches company basics and peer candidates for a ticker. This is the entry point of the
pull: it produces the profile the later scripts lean on (market cap, ipoDate, country/ADR)
and a list of SUGGESTED peers for MANUAL selection — you pick which peer(s) to pass to
numbers.py via --peers. No peer is auto-selected.

Endpoints (FMP):
    /profile?symbol={T}
    /stock-peers?symbol={T}

Outputs:
    Stock Data/{T}/raw/{T}_profile.json   raw profile
    Stock Data/{T}/raw/{T}_peers.json     raw suggested-peers list
    Stock Data/{T}/{T}_profile.md         summary (name, sector, market cap, IPO/years public,
                                          description, suggested peers)

Usage:
    python profile.py AAPL
"""

import sys
import os
import argparse
import requests
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    save_json,
    fmt_market_cap,
    years_since,
)

FMP_BASE = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------

def fetch(url, label):
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [{label}] HTTP {r.status_code}")
            return None
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"  [{label}] Request error: {e}")
        return None


def fetch_profile(ticker):
    data = fetch(f"{FMP_BASE}/profile?symbol={ticker}&apikey={FMP_API_KEY}", "profile")
    if isinstance(data, list) and data:
        return data[0]
    return None


def fetch_peers(ticker):
    data = fetch(f"{FMP_BASE}/stock-peers?symbol={ticker}&apikey={FMP_API_KEY}", "stock-peers")
    return data if isinstance(data, list) else []


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def build_markdown(ticker, profile, peers):
    name = profile.get("companyName") or ticker
    lines = []
    lines.append(f"# Profile: {name} ({ticker})")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*")
    lines.append("")

    # --- Snapshot ---
    ipo = profile.get("ipoDate") or ""
    yrs = years_since(ipo)
    public_str = f"{ipo} (public for {yrs} yrs)" if ipo and yrs is not None else (ipo or "N/A")
    is_adr = profile.get("isAdr")
    adr_str = "Yes" if is_adr else "No"

    lines.append("## Snapshot")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Exchange | {profile.get('exchange', 'N/A')} ({profile.get('exchangeFullName', '')}) |")
    lines.append(f"| Sector | {profile.get('sector', 'N/A')} |")
    lines.append(f"| Industry | {profile.get('industry', 'N/A')} |")
    lines.append(f"| Country | {profile.get('country', 'N/A')} |")
    lines.append(f"| ADR | {adr_str} |")
    lines.append(f"| Market Cap | {fmt_market_cap(profile.get('marketCap'))} |")
    lines.append(f"| Currency | {profile.get('currency', 'N/A')} |")
    lines.append(f"| Employees | {profile.get('fullTimeEmployees', 'N/A')} |")
    lines.append(f"| CEO | {profile.get('ceo', 'N/A')} |")
    lines.append(f"| IPO Date | {public_str} |")
    lines.append(f"| Website | {profile.get('website', 'N/A')} |")
    lines.append("")

    # --- Description ---
    desc = (profile.get("description") or "").strip()
    lines.append("## Description")
    lines.append("")
    lines.append(desc if desc else "*No description available.*")
    lines.append("")

    # --- Suggested peers ---
    lines.append("## Suggested Peers")
    lines.append("*Reference only — pick the peer(s) to pass to `numbers.py --peers` manually.*")
    lines.append("")
    if peers:
        lines.append("| Symbol | Company | Market Cap |")
        lines.append("|---|---|---|")
        for p in peers:
            sym = p.get("symbol", "")
            cname = p.get("companyName", "")
            mc = fmt_market_cap(p.get("mktCap"))
            lines.append(f"| {sym} | {cname} | {mc} |")
    else:
        lines.append("*No peers returned by FMP — select a peer manually.*")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Company profile + peer candidates (run first)")
    parser.add_argument("ticker", help="Ticker symbol")
    args = parser.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

    ticker = args.ticker.upper()
    print(f"\n=== Profile: {ticker} ===")

    profile = fetch_profile(ticker)
    if not profile:
        print(f"✗ FAILED: no profile returned for {ticker}")
        sys.exit(1)

    peers = fetch_peers(ticker)
    if not peers:
        print("  ⚠ No peers returned — you'll need to pick a peer manually for numbers.py")

    # --- Save raw ---
    raw_dir = get_data_directory(ticker)
    ensure_directory_exists(raw_dir)
    save_json(profile, os.path.join(raw_dir, f"{ticker}_profile.json"))
    save_json(peers, os.path.join(raw_dir, f"{ticker}_peers.json"))

    # --- Write markdown ---
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    md_path = os.path.join(writeup_dir, f"{ticker}_profile.md")
    with open(md_path, "w") as f:
        f.write(build_markdown(ticker, profile, peers))

    # --- Summary ---
    ipo = profile.get("ipoDate") or ""
    yrs = years_since(ipo)
    print(f"  ✓ {profile.get('companyName', ticker)}")
    print(f"    Sector: {profile.get('sector', 'N/A')} | Industry: {profile.get('industry', 'N/A')}")
    print(f"    Market Cap: {fmt_market_cap(profile.get('marketCap'))} | Country: {profile.get('country', 'N/A')} | ADR: {'Yes' if profile.get('isAdr') else 'No'}")
    if ipo:
        print(f"    IPO: {ipo}" + (f" (public for {yrs} yrs)" if yrs is not None else ""))
    print(f"    Suggested peers: {', '.join(p.get('symbol', '') for p in peers) if peers else 'none'}")
    print(f"  ✓ Saved: {md_path}")
    print("\nDone.")


if __name__ == "__main__":
    main()

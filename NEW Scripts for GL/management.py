#!/usr/bin/env python3
"""
Management & Ownership Script
=============================

Management quality and insider-conviction signals for a ticker:
  1. Track record     — IPO date and years public.
  2. Key executives   — active C-suite/officers: name, title, pay, year born, gender.
  3. Insider trading  — OPEN-MARKET buys vs sells over the last 6 months (the real
                        conviction signal), with a $ takeaway and a transaction table.
                        Routine option exercises / grants / tax-withholding / gifts are
                        excluded — only actual market purchases and sales count.

Endpoints (FMP):
    /key-executives?symbol={T}
    /insider-trading/search?symbol={T}&page=N&limit=100   (paginated to cover the window)
    ipoDate read from Stock Data/{T}/raw/{T}_profile.json (profile.py); falls back to /profile.

Output:
    Stock Data/{T}/{T}_management.md
    Stock Data/{T}/raw/{T}_management.json

Usage:
    python management.py AAPL
"""

import sys
import os
import argparse
import requests
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    save_json,
    load_json,
    years_since,
)

FMP_BASE = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")
INSIDER_MONTHS = 6
MAX_INSIDER_PAGES = 6   # 100 rows/page — cap so very active names don't run away


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
        print(f"  [{label}] {e}")
        return None


def fetch_executives(ticker):
    d = fetch(f"{FMP_BASE}/key-executives?symbol={ticker}&apikey={FMP_API_KEY}", "key-executives")
    return d if isinstance(d, list) else []


def fetch_insider(ticker, cutoff):
    """Paginate insider-trading/search until we pass the 12-month cutoff (or hit the page cap)."""
    rows = []
    for page in range(MAX_INSIDER_PAGES):
        d = fetch(f"{FMP_BASE}/insider-trading/search?symbol={ticker}&page={page}&limit=100"
                  f"&apikey={FMP_API_KEY}", f"insider p{page}")
        if not isinstance(d, list) or not d:
            break
        rows.extend(d)
        oldest = min((x.get("transactionDate") or "9999" for x in d), default="9999")
        if oldest < cutoff:
            break
    return rows


def get_ipo_date(ticker):
    """Prefer the profile.json written by profile.py; fall back to a fresh /profile call."""
    prof = load_json(os.path.join(get_data_directory(ticker), f"{ticker}_profile.json"))
    if prof and prof.get("ipoDate"):
        return prof.get("ipoDate")
    d = fetch(f"{FMP_BASE}/profile?symbol={ticker}&apikey={FMP_API_KEY}", "profile")
    if isinstance(d, list) and d:
        return d[0].get("ipoDate")
    return None


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def f_money(v):
    if v is None:
        return "-"
    a = abs(v)
    if a >= 1e9:
        return f"${v/1e9:,.2f}B"
    if a >= 1e6:
        return f"${v/1e6:,.2f}M"
    return f"${v:,.0f}"

def f_shares(v):
    return f"{v:,.0f}" if v is not None else "-"

def f_price(v):
    return f"${v:,.2f}" if v is not None else "-"


# ---------------------------------------------------------------------------
# Insider processing
# ---------------------------------------------------------------------------

def classify_txn(tt):
    """Open-market only: P-Purchase -> buy, S-Sale -> sell. Everything else is routine."""
    t = (tt or "")
    if t.startswith("P-") or "Purchase" in t:
        return "buy"
    if t.startswith("S-") or "Sale" in t:
        return "sell"
    return None


def process_insiders(rows, cutoff):
    """Filter to open-market P/S in the window with a real price. Returns (txns, totals)."""
    txns = []
    for x in rows:
        d = x.get("transactionDate") or ""
        if d < cutoff:
            continue
        side = classify_txn(x.get("transactionType"))
        price = x.get("price")
        shares = x.get("securitiesTransacted")
        if side is None or not price or price <= 0 or not shares:
            continue
        txns.append({
            "date": d,
            "name": x.get("reportingName", ""),
            "role": x.get("typeOfOwner", ""),
            "type": x.get("transactionType", ""),
            "side": side,
            "shares": shares,
            "price": price,
            "value": price * shares,
        })
    txns.sort(key=lambda t: t["date"], reverse=True)
    buys = [t for t in txns if t["side"] == "buy"]
    sells = [t for t in txns if t["side"] == "sell"]
    totals = {
        "buy_val": sum(t["value"] for t in buys), "buy_n": len(buys),
        "sell_val": sum(t["value"] for t in sells), "sell_n": len(sells),
    }
    totals["net"] = totals["buy_val"] - totals["sell_val"]
    return txns, totals


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def build_markdown(ticker, ipo_date, execs, txns, totals):
    lines = [f"# Management & Ownership: {ticker}",
             f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*", ""]

    # --- Track record ---
    lines.append("## Track Record")
    lines.append("")
    yrs = years_since(ipo_date)
    if ipo_date and yrs is not None:
        lines.append(f"**IPO date:** {ipo_date}  —  public for **{yrs} years**")
    else:
        lines.append("**IPO date:** not available")
    lines.append("")

    # --- Key executives ---
    lines.append("## Key Executives")
    lines.append("")
    active = [e for e in execs if e.get("active", True)]
    active.sort(key=lambda e: e.get("pay") or 0, reverse=True)
    if active:
        lines.append("| Name | Title | Pay | Year Born | Gender |")
        lines.append("|---|---|---|---|---|")
        for e in active:
            pay = f_money(e.get("pay")) if e.get("pay") else "—"
            lines.append(f"| {e.get('name','')} | {e.get('title','')} | {pay} | "
                         f"{e.get('yearBorn') or '—'} | {e.get('gender') or '—'} |")
    else:
        lines.append("*No executive data available.*")
    lines.append("")

    # --- Insider trading ---
    lines.append(f"## Insider Trading — Open-Market, Last {INSIDER_MONTHS} Months")
    lines.append("")
    lines.append("*Open-market purchases (P) and sales (S) only. Routine option exercises, grants, "
                 "tax-withholding, and gifts are excluded — they are not conviction signals.*")
    lines.append("")
    lines.append(
        f"**Open-market activity:** {f_money(totals['buy_val'])} bought ({totals['buy_n']} buys) "
        f"vs {f_money(totals['sell_val'])} sold ({totals['sell_n']} sells)  —  "
        f"**net {f_money(totals['net'])}**."
    )
    lines.append("")
    if txns:
        lines.append("| Date | Insider | Role | Type | Shares | Price | Value |")
        lines.append("|---|---|---|---|---|---|---|")
        for t in txns:
            lines.append(f"| {t['date']} | {t['name']} | {t['role']} | {t['type']} | "
                         f"{f_shares(t['shares'])} | {f_price(t['price'])} | {f_money(t['value'])} |")
    else:
        lines.append("*No open-market insider transactions in the window "
                     "(only routine grants/exercises, or no insider filings).*")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process(ticker):
    print(f"\n=== Management & Ownership: {ticker} ===")
    cutoff = (datetime.now() - timedelta(days=INSIDER_MONTHS * 31)).strftime("%Y-%m-%d")

    ipo_date = get_ipo_date(ticker)
    execs = fetch_executives(ticker)
    insider_rows = fetch_insider(ticker, cutoff)
    txns, totals = process_insiders(insider_rows, cutoff)

    if not execs and not insider_rows and not ipo_date:
        raise ValueError("no management/ownership data returned from FMP")

    raw_dir = get_data_directory(ticker)
    ensure_directory_exists(raw_dir)
    save_json({"ipoDate": ipo_date, "executives": execs, "insider_raw": insider_rows,
               "insider_open_market": txns, "insider_totals": totals},
              os.path.join(raw_dir, f"{ticker}_management.json"))

    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_management.md")
    with open(out_path, "w") as f:
        f.write(build_markdown(ticker, ipo_date, execs, txns, totals))

    yrs = years_since(ipo_date)
    print(f"  Public: {ipo_date or 'n/a'}" + (f" ({yrs} yrs)" if yrs is not None else ""))
    print(f"  Executives: {len([e for e in execs if e.get('active', True)])} active")
    print(f"  Insider ({INSIDER_MONTHS}mo, open-market): {totals['buy_n']} buys / {totals['sell_n']} sells, "
          f"net {f_money(totals['net'])}")
    print(f"  ✓ Saved: {out_path}")


def main():
    ap = argparse.ArgumentParser(description="Management & ownership: execs + insider trades")
    ap.add_argument("tickers", nargs="+", help="Ticker symbol(s)")
    args = ap.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY not set")
        sys.exit(1)

    failures = []
    for t in [x.upper() for x in args.tickers]:
        try:
            process(t)
        except Exception as e:
            print(f"  ✗ {t} FAILED: {e}")
            failures.append(t)

    if failures:
        print(f"\nFailed: {', '.join(failures)}")
        sys.exit(1)
    print("\nDone.")


if __name__ == "__main__":
    main()

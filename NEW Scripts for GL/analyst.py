#!/usr/bin/env python3
"""
Analyst Script
==============

Analyst sentiment for a ticker, grades only (no price targets):
  1. Consensus distribution — how many analysts rate Strong Buy / Buy / Hold / Sell /
     Strong Sell right now, and the % with a Sell rating.
  2. Grade movement — upgrades / downgrades / initiations over the last 90 days.

Endpoints (FMP):
    /grades-consensus?symbol={T}     current buy/hold/sell distribution
    /grades?symbol={T}               recent grade actions (filtered to 90 days)

Output:
    Stock Data/{T}/{T}_analyst.md
    Stock Data/{T}/raw/{T}_analyst.json

Usage:
    python analyst.py AAPL
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
)

FMP_BASE = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")
LOOKBACK_DAYS = 90


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


def fetch_consensus(ticker):
    d = fetch(f"{FMP_BASE}/grades-consensus?symbol={ticker}&apikey={FMP_API_KEY}", "grades-consensus")
    return d[0] if isinstance(d, list) and d else None


def fetch_grades(ticker):
    d = fetch(f"{FMP_BASE}/grades?symbol={ticker}&limit=100&apikey={FMP_API_KEY}", "grades")
    return d if isinstance(d, list) else []


# ---------------------------------------------------------------------------
# Processing
# ---------------------------------------------------------------------------

def recent_grades(grades, days=LOOKBACK_DAYS):
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    return [g for g in grades if (g.get("date") or "") >= cutoff]


def classify(action):
    a = (action or "").lower()
    if "upgrade" in a:
        return "upgrade"
    if "downgrade" in a:
        return "downgrade"
    if "init" in a or "start" in a or "coverage" in a or "resum" in a:
        return "initiate"
    if "maintain" in a or "reiterate" in a or "confirm" in a or "hold" == a:
        return "maintain"
    return "other"


def summarize(grades):
    counts = {"upgrade": 0, "downgrade": 0, "initiate": 0, "maintain": 0, "other": 0}
    for g in grades:
        counts[classify(g.get("action"))] += 1
    return counts


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def build_markdown(ticker, consensus, grades_recent, grades_all):
    lines = [f"# Analyst Grades: {ticker}",
             f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*", ""]

    # --- Consensus distribution ---
    lines.append("## Consensus Distribution")
    lines.append("")
    if consensus:
        order = [("Strong Buy", "strongBuy"), ("Buy", "buy"), ("Hold", "hold"),
                 ("Sell", "sell"), ("Strong Sell", "strongSell")]
        counts = {k: (consensus.get(k) or 0) for _, k in order}
        total = sum(counts.values())
        lines.append("| Rating | Count | % |")
        lines.append("|---|---|---|")
        for label, key in order:
            c = counts[key]
            pctstr = f"{c/total*100:.1f}%" if total else "-"
            lines.append(f"| {label} | {c} | {pctstr} |")
        sell = counts["sell"] + counts["strongSell"]
        sell_pct = f"{sell/total*100:.1f}%" if total else "N/A"
        lines.append("")
        lines.append(f"**Total analysts:** {total}  |  **Sell %** (Sell + Strong Sell): {sell_pct}"
                     f"  |  **Consensus:** {consensus.get('consensus', 'N/A')}")
    else:
        lines.append("*Consensus distribution not available from FMP.*")
    lines.append("")

    # --- Grade movement ---
    lines.append(f"## Grade Movement — Last {LOOKBACK_DAYS} Days")
    lines.append("")
    if grades_recent:
        c = summarize(grades_recent)
        parts = []
        if c["upgrade"]:
            parts.append(f"**{c['upgrade']} upgrade(s)**")
        if c["downgrade"]:
            parts.append(f"**{c['downgrade']} downgrade(s)**")
        if c["initiate"]:
            parts.append(f"**{c['initiate']} initiation(s)**")
        if c["maintain"]:
            parts.append(f"{c['maintain']} maintained")
        if c["other"]:
            parts.append(f"{c['other']} other")
        lines.append("**Summary:** " + (" | ".join(parts) if parts else "no actions"))
        lines.append("")

        # Table shows the actual rating movements (upgrades/downgrades/initiations);
        # maintains are captured in the summary count above, not listed (pure noise here).
        moves = [g for g in grades_recent if classify(g.get("action")) in ("upgrade", "downgrade", "initiate")]
        if moves:
            lines.append("| Date | Firm | Action | Previous → New |")
            lines.append("|---|---|---|---|")
            for g in sorted(moves, key=lambda x: x.get("date", ""), reverse=True):
                action = (g.get("action") or "").capitalize()
                prev = g.get("previousGrade") or "—"
                new = g.get("newGrade") or "—"
                lines.append(f"| {g.get('date','')} | {g.get('gradingCompany','')} | {action} | {prev} → {new} |")
        else:
            lines.append("*No upgrades, downgrades, or initiations in the window — only maintained ratings.*")
    else:
        lines.append(f"*No grade actions in the last {LOOKBACK_DAYS} days.*")
        if grades_all:
            mr = grades_all[0]
            lines.append("")
            lines.append(f"*Most recent action on record: {mr.get('date')} — {mr.get('gradingCompany')} "
                         f"{mr.get('action')} ({mr.get('previousGrade')} → {mr.get('newGrade')}).*")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process(ticker):
    print(f"\n=== Analyst Grades: {ticker} ===")
    consensus = fetch_consensus(ticker)
    grades_all = fetch_grades(ticker)
    grades_rec = recent_grades(grades_all)

    if consensus is None and not grades_all:
        raise ValueError("no grades or consensus data returned from FMP")

    raw_dir = get_data_directory(ticker)
    ensure_directory_exists(raw_dir)
    save_json({"consensus": consensus, "grades_recent": grades_rec, "grades_all": grades_all},
              os.path.join(raw_dir, f"{ticker}_analyst.json"))

    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_analyst.md")
    with open(out_path, "w") as f:
        f.write(build_markdown(ticker, consensus, grades_rec, grades_all))

    # stdout summary
    if consensus:
        tot = sum((consensus.get(k) or 0) for k in ["strongBuy", "buy", "hold", "sell", "strongSell"])
        sell = (consensus.get("sell") or 0) + (consensus.get("strongSell") or 0)
        print(f"  Consensus: {consensus.get('consensus','N/A')} | {tot} analysts | "
              f"Sell {sell/tot*100:.1f}%" if tot else "  Consensus: n/a")
    c = summarize(grades_rec)
    print(f"  Movement ({LOOKBACK_DAYS}d): {c['upgrade']} up | {c['downgrade']} down | "
          f"{c['initiate']} init | {c['maintain']} maintained")
    print(f"  ✓ Saved: {out_path}")


def main():
    ap = argparse.ArgumentParser(description="Analyst grades: consensus distribution + movement")
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

#!/usr/bin/env python3
"""
Analyst Consensus Script
========================

Fetches analyst price targets and grade actions from FMP and produces
a formatted markdown report for use in the Context analysis step.

Endpoints used:
  - /price-target-summary  — coverage count and avg targets across time windows
  - /price-target-consensus — high / low / median / consensus target
  - /grades                 — recent analyst grade actions (upgrades, downgrades, etc.)

Current price is loaded from the local price JSON written by price.py.
No extra API call needed for price.

Usage:
    python Scripts/analyst.py MU
    python Scripts/analyst.py MU NVDA MSFT

Output:
    Data/tickers/{TICKER}/{TICKER}_analyst.md
"""

import sys
import os
import json
import argparse
import requests
import time
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    save_json,
    load_json,
)

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE = "https://financialmodelingprep.com/stable"
API_CALL_DELAY = 2

GRADES_LOOKBACK_DAYS = 90
GRADES_FETCH_LIMIT = 30  # fetch more than we need; we filter by date


# ---------------------------------------------------------------------------
# FMP fetching
# ---------------------------------------------------------------------------

def fetch(url, label):
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [{label}] HTTP {r.status_code}")
            return None
        data = r.json()
        if isinstance(data, list) and not data:
            print(f"  [{label}] Empty response")
            return None
        return data
    except Exception as e:
        print(f"  [{label}] Error: {e}")
        return None


def fetch_price_target_summary(ticker):
    url = f"{FMP_BASE}/price-target-summary?symbol={ticker}&apikey={FMP_API_KEY}"
    data = fetch(url, "target-summary")
    return data[0] if data and isinstance(data, list) else None


def fetch_price_target_consensus(ticker):
    url = f"{FMP_BASE}/price-target-consensus?symbol={ticker}&apikey={FMP_API_KEY}"
    data = fetch(url, "target-consensus")
    return data[0] if data and isinstance(data, list) else None


def fetch_grades(ticker):
    url = f"{FMP_BASE}/grades?symbol={ticker}&limit={GRADES_FETCH_LIMIT}&apikey={FMP_API_KEY}"
    return fetch(url, "grades")


# ---------------------------------------------------------------------------
# Current price from local JSON
# ---------------------------------------------------------------------------

def load_current_price(ticker):
    """Load current price from price.py output. Returns (price, as_of) or (None, None)."""
    # price.py writes to Data/tickers/{TICKER}/{TICKER}_price.json (writeup dir)
    # tracker_update.py writes a simpler version to Data/tickers/{TICKER}/raw/{TICKER}_price.json
    # Try writeup dir first (richer price.py output), fall back to raw
    candidates = [
        os.path.join(get_writeup_directory(ticker), f"{ticker}_price.json"),
        os.path.join(get_data_directory(ticker), f"{ticker}_price.json"),
    ]
    for path in candidates:
        if os.path.exists(path):
            d = load_json(path)
            if d and d.get("current_price"):
                return d["current_price"], d.get("as_of", "unknown")
    return None, None


# ---------------------------------------------------------------------------
# Grade filtering and summarization
# ---------------------------------------------------------------------------

def filter_recent_grades(grades, days=GRADES_LOOKBACK_DAYS):
    """Return only grades within the lookback window, sorted newest-first."""
    if not grades:
        return []
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    return [g for g in grades if g.get("date", "") >= cutoff]


def summarize_grades(grades):
    """Count by action type. Normalize grade labels to Buy/Hold/Sell buckets."""
    counts = {"upgrade": 0, "downgrade": 0, "initiate": 0, "maintain": 0, "other": 0}
    for g in grades:
        action = (g.get("action") or "").lower()
        if "upgrade" in action:
            counts["upgrade"] += 1
        elif "downgrade" in action:
            counts["downgrade"] += 1
        elif "init" in action or "start" in action or "coverage" in action:
            counts["initiate"] += 1
        elif "maintain" in action or "reiterate" in action or "confirm" in action:
            counts["maintain"] += 1
        else:
            counts["other"] += 1
    return counts


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def fmt_price(val):
    return f"${val:,.2f}" if val is not None else "N/A"


def fmt_pct(val):
    if val is None:
        return "N/A"
    return f"{val:+.1%}"


def build_markdown(ticker, summary, consensus, recent_grades, all_grades, current_price, price_as_of):
    lines = []
    lines.append(f"# Analyst Consensus: {ticker}")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d')} | Price as of: {price_as_of}*")
    lines.append("")

    # --- Section 1: Price Targets ---
    lines.append("## Price Targets")
    lines.append("")

    if current_price:
        lines.append(f"**Current Price:** {fmt_price(current_price)}")
    else:
        lines.append("**Current Price:** Not available — run price.py first")

    if consensus:
        median = consensus.get("targetMedian")
        high = consensus.get("targetHigh")
        low = consensus.get("targetLow")
        cons = consensus.get("targetConsensus")

        # Implied upside: use median as primary anchor (more robust to outliers)
        if median and current_price:
            upside = (median - current_price) / current_price
            lines.append(f"**Median Target:** {fmt_price(median)} — implied {fmt_pct(upside)} vs current price")
        if cons and current_price:
            upside_cons = (cons - current_price) / current_price
            lines.append(f"**Consensus Target:** {fmt_price(cons)} — implied {fmt_pct(upside_cons)}")
        lines.append(f"**Target Range:** {fmt_price(low)} (low) — {fmt_price(high)} (high)")
    else:
        lines.append("*Price target consensus not available.*")

    lines.append("")

    if summary:
        lm_count = summary.get("lastMonthCount", 0)
        lq_count = summary.get("lastQuarterCount", 0)
        ly_count = summary.get("lastYearCount", 0)
        lm_avg = summary.get("lastMonthAvgPriceTarget")
        lq_avg = summary.get("lastQuarterAvgPriceTarget")
        ly_avg = summary.get("lastYearAvgPriceTarget")

        lines.append(f"**Coverage:** {ly_count} analyst target(s) in past year | {lq_count} last quarter | {lm_count} last month")
        lines.append("")

        # Target trend table — flag low-count windows as unreliable
        lines.append("**Target Trend:**")
        lines.append("")
        lines.append("| Window | Avg Target | Count | Note |")
        lines.append("|--------|-----------|-------|------|")

        def trend_row(label, avg, count):
            note = "⚠ low coverage — treat as unreliable" if count is not None and count <= 2 else ""
            avg_str = fmt_price(avg) if avg else "N/A"
            count_str = str(count) if count is not None else "N/A"
            return f"| {label} | {avg_str} | {count_str} | {note} |"

        lines.append(trend_row("Last month", lm_avg, lm_count))
        lines.append(trend_row("Last quarter", lq_avg, lq_count))
        lines.append(trend_row("Last year", ly_avg, ly_count))
    else:
        lines.append("*Price target summary not available.*")

    lines.append("")

    # --- Section 2: Grade Actions ---
    lines.append(f"## Grade Actions — Last {GRADES_LOOKBACK_DAYS} Days")
    lines.append("")

    if recent_grades:
        counts = summarize_grades(recent_grades)
        parts = []
        if counts["initiate"]: parts.append(f"**{counts['initiate']} initiation(s)**")
        if counts["upgrade"]:  parts.append(f"**{counts['upgrade']} upgrade(s)**")
        if counts["downgrade"]: parts.append(f"**{counts['downgrade']} downgrade(s)**")
        if counts["maintain"]: parts.append(f"{counts['maintain']} maintained")
        if counts["other"]:    parts.append(f"{counts['other']} other")
        lines.append("**Summary:** " + " | ".join(parts) if parts else "**Summary:** No recent actions")
        lines.append("")
        lines.append("| Date | Firm | Action | Previous | New |")
        lines.append("|------|------|--------|----------|-----|")
        for g in recent_grades:
            date = g.get("date", "")
            firm = g.get("gradingCompany", "")
            action = (g.get("action") or "").capitalize()
            prev = g.get("previousGrade", "—")
            new = g.get("newGrade", "—")
            lines.append(f"| {date} | {firm} | {action} | {prev} | {new} |")
    else:
        lines.append(f"*No grade actions in the last {GRADES_LOOKBACK_DAYS} days.*")

        # If we have older grades, note the most recent one
        if all_grades:
            most_recent = all_grades[0]
            lines.append("")
            lines.append(
                f"*Most recent grade: {most_recent.get('date')} — {most_recent.get('gradingCompany')} "
                f"{most_recent.get('action')} ({most_recent.get('previousGrade')} → {most_recent.get('newGrade')})*"
            )

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_ticker(ticker):
    print(f"\n[{ticker}]")

    current_price, price_as_of = load_current_price(ticker)
    if not current_price:
        print("  ⚠ No local price data found — run price_earnings.py first. Upside % will be omitted.")

    time.sleep(API_CALL_DELAY)
    summary = fetch_price_target_summary(ticker)

    time.sleep(API_CALL_DELAY)
    consensus = fetch_price_target_consensus(ticker)

    time.sleep(API_CALL_DELAY)
    all_grades = fetch_grades(ticker)
    recent_grades = filter_recent_grades(all_grades)

    # Fail loudly if the two primary target endpoints both returned nothing
    if summary is None and consensus is None:
        raise ValueError("No price target data returned from FMP (summary and consensus both empty)")

    # Warn on low analyst coverage
    if summary:
        ly_count = summary.get("lastYearCount", 0) or 0
        if ly_count == 0:
            print(f"  ⚠ Zero analyst targets in past year — coverage is stale or unavailable")
        elif ly_count <= 3:
            print(f"  ⚠ Only {ly_count} analyst target(s) in past year — low coverage, treat targets as unreliable")

    # Save raw JSON to raw/ directory for reference
    # all_grades is saved alongside grades_recent so post-run debugging can distinguish
    # "API returned nothing" from "API returned grades but all outside the lookback window"
    raw_dir = get_data_directory(ticker)
    ensure_directory_exists(raw_dir)
    save_json(
        {"summary": summary, "consensus": consensus, "grades_recent": recent_grades, "grades_all": all_grades},
        os.path.join(raw_dir, f"{ticker}_analyst.json"),
    )

    # Warn when grades exist in FMP but the most recent falls outside the lookback window —
    # this signals a coverage gap (FMP's database hasn't captured recent analyst actions)
    if all_grades and not recent_grades:
        most_recent_date = all_grades[0].get("date", "unknown")
        print(
            f"  ⚠ Grades coverage gap: FMP has {len(all_grades)} grade record(s) but none within "
            f"the last {GRADES_LOOKBACK_DAYS} days. Most recent in FMP: {most_recent_date}. "
            f"Check news sources for analyst actions not captured by FMP."
        )

    md = build_markdown(ticker, summary, consensus, recent_grades, all_grades, current_price, price_as_of)

    # Write markdown to ticker's top-level directory (alongside other analysis files)
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_analyst.md")
    with open(out_path, "w") as f:
        f.write(md)

    print(f"  ✓ Saved: {out_path}")

    # Quick summary to stdout
    if summary:
        print(f"  Coverage: {summary.get('lastYearCount', 0)} analysts (1yr)")
    if consensus and current_price:
        median = consensus.get("targetMedian")
        if median:
            upside = (median - current_price) / current_price
            print(f"  Median target: {fmt_price(median)} ({fmt_pct(upside)} implied)")
    if recent_grades is not None:
        counts = summarize_grades(recent_grades)
        print(f"  Grades ({GRADES_LOOKBACK_DAYS}d): {counts['upgrade']} up | {counts['downgrade']} down | {counts['initiate']} new | {counts['maintain']} maintained")


def main():
    parser = argparse.ArgumentParser(description="Analyst consensus: price targets and grade actions")
    parser.add_argument("tickers", nargs="+", help="Ticker symbol(s)")
    args = parser.parse_args()

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set")
        sys.exit(1)

    tickers = [t.upper() for t in args.tickers]
    failures = []

    for ticker in tickers:
        try:
            process_ticker(ticker)
        except Exception as e:
            print(f"  ✗ FAILED: {e}")
            failures.append(ticker)

    print("\n--- Summary ---")
    for ticker in tickers:
        status = "✗ FAILED" if ticker in failures else "✓"
        print(f"  {status}  {ticker}")

    if failures:
        print(f"\nFailed: {', '.join(failures)}")
        sys.exit(1)
    print("\nDone.")


if __name__ == "__main__":
    main()

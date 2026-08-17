#!/usr/bin/env python3
"""
Earnings Calls Script
=====================

Fetches the latest 2 quarterly earnings-call transcripts (Alpha Vantage), splits each
into prepared remarks vs Q&A, and writes:

    Stock Data/{T}/{T}_earnings_remarks.md   CEO/CFO prepared remarks (per quarter)
    Stock Data/{T}/{T}_earnings_qa.md        Q&A — every turn labeled by speaker/title,
                                             so analyst questions and management answers
                                             are clearly segmented in one file.
    Stock Data/{T}/{T}_earnings_report.md    summary: quarter, call/report date,
                                             transcript entries, analyst questions
    Stock Data/{T}/raw/{T}_ecall_{Q}.json    raw transcript per quarter

Alpha Vantage uses the company's OWN fiscal-quarter naming; fiscal year-end month
(from OVERVIEW) is used to map fiscalDateEnding -> the correct YYYYQN label.

Prerequisite: ALPHAVANTAGE_API_KEY.

Usage:
    python earnings_calls.py AAPL
"""

import sys
import os
import json
import argparse
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    fetch_alpha_vantage,
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
)

AV_BASE = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
RATE_DELAY = 15  # Alpha Vantage is strict on call frequency

MONTH_MAP = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
}


# ============================================================================
# Quarter determination
# ============================================================================

def get_fiscal_year_end_month(ticker):
    print("  Fetching fiscal year end month (OVERVIEW)...")
    data = fetch_alpha_vantage(f"{AV_BASE}?function=OVERVIEW&symbol={ticker}&apikey={API_KEY}")
    if not data:
        print("  ⚠️  OVERVIEW unavailable — defaulting to December FY end")
        return 12
    month = MONTH_MAP.get(data.get("FiscalYearEnd", "December"), 12)
    print(f"  Fiscal year end: month {month}")
    return month


def fiscal_date_to_quarter_str(fiscal_date_str, fye_month):
    """Map a fiscalDateEnding to Alpha Vantage's fiscal-quarter label (e.g. 2026Q3)."""
    d = datetime.strptime(fiscal_date_str, "%Y-%m-%d")
    month, year, fye = d.month, d.year, fye_month
    fiscal_year = year if month <= fye else year + 1
    q_end_months = {((fye - 9) % 12) or 12: 1, ((fye - 6) % 12) or 12: 2,
                    ((fye - 3) % 12) or 12: 3, fye: 4}
    q = q_end_months.get(month)
    if q is None:
        raise ValueError(f"month {month} from '{fiscal_date_str}' doesn't match FY-end {fye}")
    return f"{fiscal_year}Q{q}"


def get_latest_quarters(ticker):
    """Return [{quarter, fiscal_date, reported_date}, ...] for the latest 2 quarters."""
    print(f"\nDetermining latest quarters for {ticker}...")
    fye = get_fiscal_year_end_month(ticker)
    print(f"  Waiting {RATE_DELAY}s for rate limit...")
    time.sleep(RATE_DELAY)

    data = fetch_alpha_vantage(f"{AV_BASE}?function=EARNINGS&symbol={ticker}&apikey={API_KEY}")
    if not data or not data.get("quarterlyEarnings"):
        print("❌ Could not fetch earnings data to determine quarters")
        return []

    rows = sorted(data["quarterlyEarnings"], key=lambda x: x.get("fiscalDateEnding", ""), reverse=True)
    out = []
    for qtr in rows[:2]:
        fd = qtr.get("fiscalDateEnding", "")
        if not fd:
            continue
        try:
            out.append({"quarter": fiscal_date_to_quarter_str(fd, fye),
                        "fiscal_date": fd, "reported_date": qtr.get("reportedDate", "")})
            print(f"  Found: {out[-1]['quarter']} (fiscal {fd}, reported {out[-1]['reported_date']})")
        except (ValueError, KeyError) as e:
            print(f"  ⚠️  Skipping '{fd}': {e}")
    return out


# ============================================================================
# Transcript segmentation
# ============================================================================

QA_TRIGGERS = ["first question", "our first question", "next question",
               "we will now take questions", "question-and-answer", "q&a"]


def find_qa_start_index(transcript):
    """Index where Q&A begins: Operator introducing questions, or the first Analyst turn."""
    for i, entry in enumerate(transcript):
        speaker = entry.get("speaker", "")
        title = entry.get("title", "")
        content = entry.get("content", "").lower()
        if ("Operator" in speaker or "Operator" in title) and any(t in content for t in QA_TRIGGERS):
            return i
        if "Analyst" in title and i > 0:
            return i
    return None


def count_analyst_questions(transcript, qa_idx):
    if qa_idx is None:
        return 0
    return sum(1 for e in transcript[qa_idx:] if "Analyst" in e.get("title", ""))


def format_segment(entries):
    out = []
    for e in entries:
        header = f"**{e.get('speaker', 'Unknown Speaker')}**"
        if e.get("title"):
            header += f" ({e['title']})"
        out.append(f"{header}\n{e.get('content', '')}\n")
    return "\n".join(out)


# ============================================================================
# Output
# ============================================================================

def save_raw(data, ticker, quarter):
    raw_dir = get_data_directory(ticker)
    ensure_directory_exists(raw_dir)
    with open(os.path.join(raw_dir, f"{ticker}_ecall_{quarter}.json"), "w") as f:
        json.dump(data, f, indent=2)


def generate_markdown(ticker, quarters_data):
    writeup = get_writeup_directory(ticker)
    ensure_directory_exists(writeup)
    remarks_path = os.path.join(writeup, f"{ticker}_earnings_remarks.md")
    qa_path = os.path.join(writeup, f"{ticker}_earnings_qa.md")

    quarters_label = ", ".join(q["quarter"] for q in quarters_data)

    with open(remarks_path, "w", encoding="utf-8") as f:
        f.write(f"# Earnings Call Remarks: {ticker}\n\n**Quarters:** {quarters_label}\n\n")
        for i, q in enumerate(quarters_data):
            transcript = q["data"].get("transcript", [])
            qa_idx = find_qa_start_index(transcript)
            label = "CURRENT QUARTER" if i == 0 else "PRIOR QUARTER"
            f.write(f"---\n# {label}: {q['quarter']} (reported {q.get('reported_date','n/a')})\n\n")
            f.write(format_segment(transcript[:qa_idx] if qa_idx else transcript))
            f.write("\n")

    with open(qa_path, "w", encoding="utf-8") as f:
        f.write(f"# Earnings Call Q&A: {ticker}\n\n**Quarters:** {quarters_label}\n\n")
        f.write("*Each turn is labeled by speaker and title — Analyst turns are the "
                "questions, management turns are the answers.*\n\n")
        for i, q in enumerate(quarters_data):
            transcript = q["data"].get("transcript", [])
            qa_idx = find_qa_start_index(transcript)
            label = "CURRENT QUARTER" if i == 0 else "PRIOR QUARTER"
            if qa_idx:
                f.write(f"---\n# {label}: {q['quarter']} (reported {q.get('reported_date','n/a')})\n\n")
                f.write(format_segment(transcript[qa_idx:]))
                f.write("\n")
            else:
                f.write(f"---\n# {label}: {q['quarter']}\n\n*Q&A boundary not detected in transcript.*\n\n")

    return remarks_path, qa_path


def generate_report(ticker, quarters_data):
    writeup = get_writeup_directory(ticker)
    path = os.path.join(writeup, f"{ticker}_earnings_report.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Earnings Calls Summary: {ticker}\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        f.write("| Quarter | Call / Report Date | Transcript Entries | Analyst Questions |\n")
        f.write("|---|---|---|---|\n")
        for q in quarters_data:
            transcript = q["data"].get("transcript", [])
            qa_idx = find_qa_start_index(transcript)
            nq = count_analyst_questions(transcript, qa_idx)
            f.write(f"| {q['quarter']} | {q.get('reported_date','n/a')} | {len(transcript)} | {nq} |\n")
    return path


# ============================================================================
# Main
# ============================================================================

def main():
    ap = argparse.ArgumentParser(description="Earnings call transcripts (Alpha Vantage)")
    ap.add_argument("ticker")
    args = ap.parse_args()
    ticker = args.ticker.upper()

    if not API_KEY:
        print("Error: ALPHAVANTAGE_API_KEY not set")
        sys.exit(1)

    print(f"\n=== Earnings Calls: {ticker} ===")
    quarters = get_latest_quarters(ticker)
    if not quarters:
        sys.exit(1)

    print(f"\nFetching transcripts for: {', '.join(q['quarter'] for q in quarters)}...")
    quarters_data = []
    failures = []
    for i, q in enumerate(quarters):
        if i > 0:
            print(f"  Waiting {RATE_DELAY}s for rate limit...")
            time.sleep(RATE_DELAY)
        data = fetch_alpha_vantage(
            f"{AV_BASE}?function=EARNINGS_CALL_TRANSCRIPT&symbol={ticker}&quarter={q['quarter']}&apikey={API_KEY}")
        if data and "transcript" in data:
            save_raw(data, ticker, q["quarter"])
            quarters_data.append({**q, "data": data})
            print(f"  ✓ {q['quarter']} — {len(data['transcript'])} entries")
        else:
            failures.append(q["quarter"])
            print(f"  ✗ {q['quarter']} — no transcript returned")

    if quarters_data:
        remarks_path, qa_path = generate_markdown(ticker, quarters_data)
        report_path = generate_report(ticker, quarters_data)
        print(f"\n  ✓ Remarks: {remarks_path}")
        print(f"  ✓ Q&A:     {qa_path}")
        print(f"  ✓ Summary: {report_path}")

    if failures:
        print(f"\n⚠ Failed quarters: {', '.join(failures)}")
        if not quarters_data:
            sys.exit(1)
    print("\nDone.")


if __name__ == "__main__":
    main()

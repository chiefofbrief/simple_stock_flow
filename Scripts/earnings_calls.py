#!/usr/bin/env python3
"""
Earnings Call Transcript Preparation Script
==========================================

Fetches latest 2 quarterly earnings call transcripts for a given ticker,
saves raw data, and generates a consolidated markdown file for analysis.

Usage:
    python "Scripts/earnings_calls.py" TICKER

Example:
    python "Scripts/earnings_calls.py" IBM

Outputs:
    Raw Data (data/tickers/{TICKER}/raw/):
        - {TICKER}_ecall_{QUARTER}.json        - Raw API response
        - {TICKER}_ecall_{QUARTER}.txt         - Full transcript text
        - {TICKER}_{QUARTER}_prepared.txt      - CEO/CFO prepared remarks only

    Analysis Input (data/tickers/{TICKER}/):
        - {TICKER}_earnings_calls.md           - Consolidated transcripts (Current + Prior)

Prerequisites:
    - ALPHAVANTAGE_API_KEY environment variable must be set
"""

import json
import os
import sys
import argparse
import time
from datetime import datetime
from shared_utils import (
    fetch_alpha_vantage,
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists
)

# ============================================================================
# QUARTER DETERMINATION
# ============================================================================

def get_fiscal_year_end_month(ticker, api_key):
    """Fetch the company's fiscal year end month from Alpha Vantage OVERVIEW.

    Returns:
        int: Month number (1-12). Defaults to 12 (December) if unavailable.
    """
    print(f"  Fetching fiscal year end month from OVERVIEW...")
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={api_key}'
    data = fetch_alpha_vantage(url)
    if not data:
        print(f"  ⚠️  Could not fetch OVERVIEW — defaulting to December FY end")
        return 12

    fye_str = data.get('FiscalYearEnd', 'December')
    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    month = month_map.get(fye_str, 12)
    print(f"  Fiscal year end: {fye_str} (month {month})")
    return month


def fiscal_date_to_quarter_str(fiscal_date_str, fiscal_year_end_month):
    """Convert a fiscalDateEnding date to Alpha Vantage quarter format.

    Alpha Vantage's EARNINGS_CALL_TRANSCRIPT endpoint uses the company's own
    fiscal quarter naming (e.g., "2026Q4" = the company's fiscal Q4 of FY2026),
    NOT calendar quarters. This function derives the correct label by using
    the company's fiscal year end month.

    Args:
        fiscal_date_str: Date string in "YYYY-MM-DD" format (fiscalDateEnding).
        fiscal_year_end_month: The month (1-12) when the company's fiscal year ends.

    Returns:
        Quarter string in YYYYQN format (e.g., "2026Q4").
    """
    date_obj = datetime.strptime(fiscal_date_str, "%Y-%m-%d")
    month = date_obj.month
    year = date_obj.year
    fye = fiscal_year_end_month

    # Determine fiscal year label.
    # The FY label equals the calendar year of the fiscal year END (Q4 end).
    # If this date's month is after the FY end month, the FY end is in the
    # next calendar year → fiscal year label = year + 1.
    if month <= fye:
        fiscal_year = year
    else:
        fiscal_year = year + 1

    # Determine the quarter number: Q4 ends at fye, Q3 ends 3 months before, etc.
    q_end_months = {
        ((fye - 9) % 12) or 12: 1,
        ((fye - 6) % 12) or 12: 2,
        ((fye - 3) % 12) or 12: 3,
        fye: 4,
    }
    quarter_num = q_end_months.get(month)
    if quarter_num is None:
        raise ValueError(
            f"Month {month} from fiscalDateEnding '{fiscal_date_str}' does not match "
            f"any fiscal quarter end for FY-end month {fye}. "
            f"Expected quarter-end months: {sorted(q_end_months.keys())}"
        )

    return f"{fiscal_year}Q{quarter_num}"


def get_latest_quarters(ticker, api_key):
    """Get the 2 most recent quarter identifiers from EARNINGS endpoint.

    Uses the company's fiscal year end month (from OVERVIEW) to correctly
    map fiscalDateEnding dates to Alpha Vantage's fiscal quarter naming
    convention (e.g., "2026Q4" for the company's own fiscal Q4 of FY2026).

    Returns:
        List of quarter strings in YYYYQN format (e.g., ['2026Q4', '2026Q3'])
        Returns empty list if unable to fetch earnings data.
    """
    print(f"\nDetermining latest quarters for {ticker}...")

    # Get fiscal year end month first — needed for correct quarter mapping
    fiscal_year_end_month = get_fiscal_year_end_month(ticker, api_key)
    print("  Waiting 15s for rate limit...")
    time.sleep(15)

    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={api_key}'
    data = fetch_alpha_vantage(url)
    if not data:
        print(f"❌ Could not fetch earnings data to determine quarters")
        return []

    quarterly_earnings = data.get("quarterlyEarnings", [])
    if not quarterly_earnings:
        print(f"❌ No quarterly earnings data available for {ticker}")
        return []

    # Sort by fiscalDateEnding descending to get most recent first
    sorted_quarters = sorted(
        quarterly_earnings,
        key=lambda x: x.get("fiscalDateEnding", ""),
        reverse=True
    )

    quarters = []
    for qtr in sorted_quarters[:2]:  # Take top 2 most recent
        fiscal_date = qtr.get("fiscalDateEnding", "")
        if not fiscal_date:
            continue

        try:
            quarter_str = fiscal_date_to_quarter_str(fiscal_date, fiscal_year_end_month)
            quarters.append(quarter_str)
            print(f"  Found quarter: {quarter_str} (fiscal date: {fiscal_date})")
        except (ValueError, KeyError) as e:
            print(f"  ⚠️  Skipping '{fiscal_date}': {e}")
            continue

    return quarters

# ============================================================================
# TRANSCRIPT PROCESSING
# ============================================================================

QA_TRIGGERS = [
    "first question",
    "our first question",
    "next question",
    "we will now take questions",
    "question-and-answer",
    "q&a"
]

def find_qa_start_index(transcript):
    """Find where Q&A section starts in transcript"""
    for i, entry in enumerate(transcript):
        speaker = entry.get('speaker', '')
        title = entry.get('title', '')
        content = entry.get('content', '').lower()

        # Q&A starts when Operator introduces questions
        if ('Operator' in speaker or 'Operator' in title) and any(trigger in content for trigger in QA_TRIGGERS):
            return i
        # Or when first Analyst speaks (backup detection)
        elif 'Analyst' in title and i > 0:
            return i

    return None

def format_transcript_segment(entries):
    """Format a list of transcript entries into a readable string"""
    output = []
    for entry in entries:
        speaker = entry.get('speaker', 'Unknown Speaker')
        title = entry.get('title', '')
        content = entry.get('content', '')
        
        header = f"**{speaker}**"
        if title:
            header += f" ({title})"
        
        output.append(f"{header}\n{content}\n")
    return "\n".join(output)

# ============================================================================
# FILE SAVING - RAW
# ============================================================================

def save_raw_files(data, ticker, quarter):
    """Save raw JSON and TXT files to raw/ directory"""
    raw_dir = get_data_directory(ticker)  # specific to raw/
    ensure_directory_exists(raw_dir)

    # 1. Save JSON
    json_path = os.path.join(raw_dir, f"{ticker}_ecall_{quarter}.json")
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)

    # 2. Save Full TXT
    txt_path = os.path.join(raw_dir, f"{ticker}_ecall_{quarter}.txt")
    transcript = data.get('transcript', [])
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(f"EARNINGS CALL: {ticker} {quarter}\n")
        f.write("="*80 + "\n\n")
        
        qa_idx = find_qa_start_index(transcript)
        
        # Prepared Remarks
        f.write("--- PREPARED REMARKS ---\n\n")
        remarks = transcript[:qa_idx] if qa_idx else transcript
        f.write(format_transcript_segment(remarks))
        
        # Q&A
        if qa_idx:
            f.write("\n\n--- Q&A SESSION ---\n\n")
            qa = transcript[qa_idx:]
            f.write(format_transcript_segment(qa))

    print(f"✓ Saved raw files for {quarter}")
    return txt_path

# ============================================================================
# Q&A QUESTIONS EXTRACTION
# ============================================================================

def extract_analyst_questions(transcript, qa_idx):
    """Extract analyst-only entries from the Q&A section of a transcript.

    Returns a list of dicts with keys: speaker, question_num, content.
    Skips Operator intros and all management responses.
    """
    if qa_idx is None:
        return []

    qa_entries = transcript[qa_idx:]
    questions = []
    q_num = 0

    for entry in qa_entries:
        title = entry.get("title", "")
        if "Analyst" in title:
            q_num += 1
            questions.append({
                "question_num": q_num,
                "speaker": entry.get("speaker", "Unknown Analyst"),
                "content": entry.get("content", "").strip(),
            })

    return questions


def generate_qa_questions_markdown(ticker, quarters_data):
    """Generate {TICKER}_qa_questions.md — analyst questions only, no responses."""
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_qa_questions.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Earnings Call — Analyst Questions: {ticker}\n\n")
        f.write(
            f"**Quarters:** {', '.join(q['quarter'] for q in quarters_data)}\n\n"
        )
        f.write(
            "*Analyst questions only — management responses are in "
            f"{ticker}_earnings_qa.md*\n\n"
        )

        for i, q_data in enumerate(quarters_data):
            quarter = q_data["quarter"]
            transcript = q_data["data"].get("transcript", [])
            label = "CURRENT QUARTER" if i == 0 else "PRIOR QUARTER"

            qa_idx = find_qa_start_index(transcript)
            questions = extract_analyst_questions(transcript, qa_idx)

            f.write(f"---\n## {label}: {quarter}\n\n")

            if not questions:
                f.write("*No analyst questions found in this transcript.*\n\n")
                continue

            for q in questions:
                f.write(f"**Q{q['question_num']} — {q['speaker']}**\n")
                f.write(f"{q['content']}\n\n")

    print(f"✓ Generated Q&A questions file: {out_path}")
    return out_path


# ============================================================================
# FILE SAVING - CONSOLIDATED MARKDOWN
# ============================================================================

def generate_consolidated_markdown(ticker, quarters_data):
    """Generate two separate markdown files: Remarks and Q&A"""
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    
    remarks_file = os.path.join(writeup_dir, f"{ticker}_earnings_remarks.md")
    qa_file = os.path.join(writeup_dir, f"{ticker}_earnings_qa.md")
    
    # 1. Generate Remarks File
    with open(remarks_file, 'w', encoding='utf-8') as f:
        f.write(f"# Earnings Call Remarks: {ticker}\n\n")
        f.write(f"**Quarters Analyzed:** {', '.join(q['quarter'] for q in quarters_data)}\n\n")
        
        for i, q_data in enumerate(quarters_data):
            quarter = q_data['quarter']
            transcript = q_data['data'].get('transcript', [])
            label = "CURRENT QUARTER" if i == 0 else "PRIOR QUARTER"
            
            f.write(f"---\n# {label}: {quarter}\n\n")
            qa_idx = find_qa_start_index(transcript)
            remarks = transcript[:qa_idx] if qa_idx else transcript
            f.write(format_transcript_segment(remarks))
            f.write("\n")

    # 2. Generate Q&A File
    with open(qa_file, 'w', encoding='utf-8') as f:
        f.write(f"# Earnings Call Q&A: {ticker}\n\n")
        f.write(f"**Quarters Analyzed:** {', '.join(q['quarter'] for q in quarters_data)}\n\n")
        
        for i, q_data in enumerate(quarters_data):
            quarter = q_data['quarter']
            transcript = q_data['data'].get('transcript', [])
            label = "CURRENT QUARTER" if i == 0 else "PRIOR QUARTER"
            
            qa_idx = find_qa_start_index(transcript)
            if qa_idx:
                f.write(f"---\n# {label}: {quarter}\n\n")
                qa = transcript[qa_idx:]
                f.write(format_transcript_segment(qa))
                f.write("\n")

    print(f"\n✓ Generated Remarks file: {remarks_file}")
    print(f"✓ Generated Q&A file: {qa_file}")
    return remarks_file, qa_file

# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Earnings Call Transcript Fetcher")
    parser.add_argument('target', type=str, help='Target company ticker')
    args = parser.parse_args()

    ticker = args.target.upper()
    api_key = os.getenv('ALPHAVANTAGE_API_KEY')
    
    if not api_key:
        print("Error: ALPHAVANTAGE_API_KEY not set")
        sys.exit(1)

    print(f"\n=== Earnings Calls: {ticker} ===")

    # 1. Identify Quarters
    quarters = get_latest_quarters(ticker, api_key)
    if not quarters:
        sys.exit(1)

    # 2. Fetch Data
    print(f"\nFetching transcripts for: {', '.join(quarters)}...")
    quarters_data = []
    quarter_status = {}  # quarter -> True (ok) / False (failed)

    for i, quarter in enumerate(quarters):
        if i > 0:
            print("  Waiting 15s for rate limit...")
            time.sleep(15)

        url = f'https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&symbol={ticker}&quarter={quarter}&apikey={api_key}'
        data = fetch_alpha_vantage(url)

        if data and 'transcript' in data:
            n_entries = len(data['transcript'])
            save_raw_files(data, ticker, quarter)
            quarters_data.append({'quarter': quarter, 'data': data})
            quarter_status[quarter] = True
            print(f"  ✓ {quarter} — {n_entries} transcript entries")
        else:
            quarter_status[quarter] = False
            print(f"  ✗ FAILED: {quarter} — no transcript data returned")

    # 3. Generate Output
    if quarters_data:
        generate_consolidated_markdown(ticker, quarters_data)
        generate_qa_questions_markdown(ticker, quarters_data)

    # 4. Summary
    print("\n--- Summary ---")
    for q in quarters:
        label = "CURRENT" if q == quarters[0] else "PRIOR"
        status = "✓" if quarter_status.get(q) else "✗ FAILED"
        print(f"  {status}  {q} ({label})")

    failures = [q for q, ok in quarter_status.items() if not ok]
    if failures:
        print(f"\nFailed quarters: {', '.join(failures)}")
        print("Do not proceed with analysis until all transcripts are fetched.")
        sys.exit(1)

    print("\nDone.")

if __name__ == "__main__":
    main()

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

def get_latest_quarters(ticker, api_key):
    """Get the 2 most recent quarter identifiers from EARNINGS endpoint

    Returns:
        List of quarter strings in YYYYQN format (e.g., ['2024Q1', '2023Q4'])
        Returns empty list if unable to fetch earnings data
    """
    print(f"\nDetermining latest quarters for {ticker}...")
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

        # Convert YYYY-MM-DD to YYYYQN format
        try:
            date_obj = datetime.strptime(fiscal_date, "%Y-%m-%d")
            year = date_obj.year
            month = date_obj.month

            # Determine quarter number based on month
            if month in [1, 2, 3]:
                quarter_num = 1
            elif month in [4, 5, 6]:
                quarter_num = 2
            elif month in [7, 8, 9]:
                quarter_num = 3
            else:  # [10, 11, 12]
                quarter_num = 4

            quarter_str = f"{year}Q{quarter_num}"
            quarters.append(quarter_str)
            print(f"  Found quarter: {quarter_str} (fiscal date: {fiscal_date})")
        except ValueError:
            print(f"  ⚠️  Skipping invalid date format: {fiscal_date}")
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
    
    for i, quarter in enumerate(quarters):
        if i > 0:
            print("  Waiting 15s for rate limit...")
            time.sleep(15)
            
        url = f'https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&symbol={ticker}&quarter={quarter}&apikey={api_key}'
        data = fetch_alpha_vantage(url)
        
        if data and 'transcript' in data:
            save_raw_files(data, ticker, quarter)
            quarters_data.append({'quarter': quarter, 'data': data})
        else:
            print(f"⚠️  Failed to fetch {quarter}")

    # 3. Generate Output
    if quarters_data:
        generate_consolidated_markdown(ticker, quarters_data)
    else:
        print("\n❌ No transcripts successfully fetched.")
        sys.exit(1)

if __name__ == "__main__":
    main()

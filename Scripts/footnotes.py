#!/usr/bin/env python3
"""
SEC Filings Preparation Script
================================

Fetches latest 10-K and 10-Q SEC filings, extracts MD&A and Notes sections,
and generates a consolidated markdown for analysis.

Usage:
    python Scripts/footnotes.py TICKER

Example:
    python Scripts/footnotes.py PYPL

Outputs:
    Raw (data/tickers/{TICKER}/raw/):
        - {TICKER}_10k_latest.html    - Full 10-K HTML
        - {TICKER}_10q_latest.html    - Full 10-Q HTML
        - {TICKER}_10k_mda.txt        - MD&A section from 10-K
        - {TICKER}_10k_notes.txt      - Notes section from 10-K
        - {TICKER}_10q_mda.txt        - MD&A section from 10-Q
        - {TICKER}_10q_notes.txt      - Notes section from 10-Q
        - {TICKER}_filings_metadata.json - Filing dates, accession numbers, section stats

    Writeup (data/tickers/{TICKER}/):
        - {TICKER}_notes_mda.md       - Consolidated markdown with all sections

Notes:
    - Fetches the most recent 10-K and 10-Q available from SEC EDGAR
    - SEC rate limit: 10 requests/second (script implements 0.15s delays)
    - User-Agent header required by SEC (configured in script)
"""

import requests
import json
import os
import sys
import argparse
import time
import re
from html.parser import HTMLParser

from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    save_json
)

# ============================================================================
# CONSTANTS
# ============================================================================

SEC_RATE_LIMIT_DELAY = 0.15  # 10 requests/second max
SEC_USER_AGENT = 'Financial Analysis Tool contact@example.com'
REQUEST_TIMEOUT = 30

# Section patterns organized by form type
# 10-K (annual): MD&A is Item 7, Notes follow Item 8
# 10-Q (quarterly): MD&A is Item 2, Notes are under Item 1
SECTION_PATTERNS = {
    '10-K': {
        'mda': {
            'start': r'ITEM\s+7\.\s+MANAGEMENT',
            'ends': [r'ITEM\s+7A\.', r'ITEM\s+8\.']
        },
        'notes': {
            'start': r'NOTES\s+TO\s+CONSOLIDATED\s+FINANCIAL\s+STATEMENTS',
            'ends': [r'ITEM\s+9\.', r'PART\s+III', r'ITEM\s+15\.', r'REPORT\s+OF\s+INDEPENDENT\s+REGISTERED\s+PUBLIC\s+ACCOUNTING\s+FIRM']
        }
    },
    '10-Q': {
        'mda': {
            'start': r'ITEM\s+2\.\s+MANAGEMENT',
            'ends': [r'ITEM\s+3\.', r'ITEM\s+4\.']
        },
        'notes': {
            # More flexible pattern for 10-Q notes
            'start': r'(NOTES\s+TO\s+(CONDENSED\s+)?CONSOLIDATED\s+FINANCIAL\s+STATEMENTS|ITEM\s+1\.\s+FINANCIAL\s+STATEMENTS)',
            'ends': [r'ITEM\s+2\.\s+MANAGEMENT', r'PART\s+II']
        }
    }
}

SECTION_DISPLAY_NAMES = {
    '10-K': {'mda': '10-K MD&A (Item 7)', 'notes': '10-K Notes to Financial Statements'},
    '10-Q': {'mda': '10-Q MD&A (Item 2)', 'notes': '10-Q Notes to Financial Statements'}
}

# ============================================================================
# SEC REQUEST HELPER
# ============================================================================

def _make_sec_request(url, delay=True):
    """Make a request to SEC EDGAR with proper headers and rate limiting"""
    if delay:
        time.sleep(SEC_RATE_LIMIT_DELAY)

    headers = {'User-Agent': SEC_USER_AGENT}
    try:
        return requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    except Exception as e:
        print(f"  Error: Request failed: {e}")
        return None

# ============================================================================
# CIK LOOKUP
# ============================================================================

def get_cik_from_ticker(ticker):
    """Get CIK number from ticker symbol using SEC company tickers JSON"""
    print(f"\nLooking up CIK for {ticker}...")
    url = "https://www.sec.gov/files/company_tickers.json"

    r = _make_sec_request(url, delay=False)
    if not r or r.status_code != 200:
        print(f"  Error: Could not fetch company tickers (HTTP {r.status_code if r else 'No response'})")
        return None

    data = r.json()
    for entry in data.values():
        if entry.get('ticker', '').upper() == ticker.upper():
            cik = str(entry.get('cik_str', '')).zfill(10)
            print(f"  Found CIK: {cik}")
            return cik

    print(f"  Error: Ticker {ticker} not found in SEC database")
    return None

# ============================================================================
# SEC FILINGS FETCHING
# ============================================================================

def fetch_latest_filings(ticker, cik):
    """Fetch latest 10-Q and 10-K filing information from SEC

    Returns:
        tuple: (latest_10q_dict, latest_10k_dict) with filing metadata
    """
    print(f"\nFetching filing information for {ticker} (CIK: {cik})...")
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"

    r = _make_sec_request(url, delay=True)
    if not r or r.status_code != 200:
        print(f"  Error: HTTP {r.status_code if r else 'No response'}")
        return None, None

    try:
        data = r.json()
        recent = data.get('filings', {}).get('recent', {})

        if not recent:
            print(f"  Error: No recent filings found")
            return None, None

        forms = recent.get('form', [])
        accessions = recent.get('accessionNumber', [])
        primary_docs = recent.get('primaryDocument', [])
        report_dates = recent.get('reportDate', [])

        # Find latest 10-Q and 10-K
        filings_found = {'10-Q': None, '10-K': None}

        for i, form in enumerate(forms):
            if form in filings_found and filings_found[form] is None:
                filings_found[form] = {
                    'accession': accessions[i],
                    'document': primary_docs[i],
                    'report_date': report_dates[i]
                }
            if all(filings_found.values()):
                break

        for form_type, filing in filings_found.items():
            if filing:
                print(f"  Found {form_type}: {filing['report_date']}")
            else:
                print(f"  Warning: No {form_type} filing found")

        return filings_found['10-Q'], filings_found['10-K']

    except Exception as e:
        print(f"  Error fetching filings: {e}")
        return None, None

def download_filing(ticker, cik, filing_info, form_type):
    """Download a single SEC filing HTML document"""
    if not filing_info:
        return None

    accession_no_dash = filing_info['accession'].replace('-', '')
    cik_no_zeros = str(int(cik))
    url = f"https://www.sec.gov/Archives/edgar/data/{cik_no_zeros}/{accession_no_dash}/{filing_info['document']}"

    print(f"  Downloading {form_type} filing...")
    r = _make_sec_request(url, delay=True)
    if not r or r.status_code != 200:
        print(f"  Error: Could not download {form_type} (HTTP {r.status_code if r else 'No response'})")
        return None

    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)
    output_file = os.path.join(data_dir, f"{ticker}_{form_type.lower().replace('-', '')}_latest.html")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(r.text)

    print(f"  Saved HTML: {output_file}")
    return output_file

# ============================================================================
# HTML SECTION EXTRACTION
# ============================================================================

class TextExtractor(HTMLParser):
    """HTML parser that extracts visible text content"""
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_script_style = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() in ['script', 'style']:
            self.in_script_style = True

    def handle_endtag(self, tag):
        if tag.lower() in ['script', 'style']:
            self.in_script_style = False

    def handle_data(self, data):
        if not self.in_script_style:
            text = data.strip()
            if text:
                self.text.append(text)

# Minimum word counts required for each section — anything below is treated as a
# failed extraction (likely picked up a table of contents rather than body text).
MIN_SECTION_WORDS = {
    '10-K': {'mda': 3000, 'notes': 1000},
    '10-Q': {'mda': 2000, 'notes': 500},
}

def _is_toc_entry(text, match_pos, lookahead=200):
    """Check if a match position looks like a TOC entry rather than actual content"""
    snippet = text[match_pos:match_pos + lookahead]

    toc_patterns = [
        r'\.{3,}\s*\d',           # Ellipsis followed by page number
        r'\.{3,}\s*F-?\d',        # Ellipsis followed by F-page
        r'\s+\d{1,3}\s*$',        # Ends with just a page number
        r'\s+F-?\d{1,3}\s*$',     # Ends with F-page number
    ]

    for pattern in toc_patterns:
        if re.search(pattern, snippet[:100], re.IGNORECASE):
            return True

    content_patterns = [
        r'Note\s+1\b',
        r'\(Continued\)',
        r'The\s+following',
        r'We\s+have',
        r'As\s+of\s+',
    ]

    for pattern in content_patterns:
        if re.search(pattern, snippet, re.IGNORECASE):
            return False

    return False

def _content_length_after(search_text, start_pos, end_patterns):
    """Return how many characters of content exist between start_pos and the nearest end marker."""
    end_positions = []
    for end_pattern in end_patterns:
        end_match = re.search(end_pattern, search_text[start_pos + 50:], re.IGNORECASE)
        if end_match:
            end_positions.append(start_pos + 50 + end_match.start())
    end_pos = min(end_positions) if end_positions else len(search_text)
    return end_pos - start_pos

def _validate_notes_content(text):
    """Check that notes contain actual note body text, not just a header/TOC listing.

    A real notes section has multi-sentence prose following the note header.
    A TOC listing has only short lines (note title + page number) per note.
    Returns (is_valid, reason).
    """
    # Look for a note header followed by at least 100 chars of body text
    if re.search(r'(?:Note|NOTE|\(\d+\))\s*[-–]?\s*\w.{5,}\n(.{100,})', text, re.DOTALL):
        return True, "OK"
    # Fallback: check total unique sentences (TOC entries are all very short)
    sentences = [s.strip() for s in re.split(r'[.!?]\s+', text) if len(s.strip()) > 60]
    if len(sentences) >= 5:
        return True, "OK"
    return False, "Notes appear to contain only headers or a TOC listing — no substantive body text found"

def extract_section_text(html_content, start_pattern, end_patterns):
    r"""Extract text between section markers using regex.

    Selects the candidate start match that yields the most content (by character
    count to the nearest end marker), which reliably picks the real section body
    over any table-of-contents occurrence of the same heading.

    Args:
        html_content: Raw HTML string
        start_pattern: Regex pattern for section start
        end_patterns: List of regex patterns for section end

    Returns:
        Extracted section text
    """
    # Strip XBRL tags but keep their content
    html_clean = re.sub(r'</?(ix|xbrli):[^>]*>', '', html_content)

    # Extract text from HTML
    parser = TextExtractor()
    parser.feed(html_clean)
    full_text = '\n'.join(parser.text)

    # Normalize whitespace for robust searching only
    # This helps when headers are split across lines or have inconsistent spacing
    normalized_text = re.sub(r'\s+', ' ', full_text)

    # Find the start pattern in normalized text
    start_matches = list(re.finditer(start_pattern, normalized_text, re.IGNORECASE))

    if not start_matches:
        # Fallback: try finding in original text if normalized fails (rare but possible)
        start_matches = list(re.finditer(start_pattern, full_text, re.IGNORECASE))
        search_text = full_text
    else:
        search_text = normalized_text

    if not start_matches:
        return ""

    # Filter out matches near the very end of the document
    text_length = len(search_text)
    threshold = text_length * 0.95
    valid_matches = [m for m in start_matches if m.start() < threshold]
    if not valid_matches:
        return ""

    # Pick the candidate that yields the most content before the nearest end marker.
    # This is more reliable than position-based heuristics: a TOC occurrence will
    # produce very little text before the next section marker, while the real section
    # body will produce orders of magnitude more.
    chosen_start_match = max(
        valid_matches,
        key=lambda m: _content_length_after(search_text, m.start(), end_patterns)
    )

    # Map the position found in search_text back to full_text using the matched keyword
    # so the output preserves the original line structure
    start_keyword = chosen_start_match.group(0)
    full_text_match = re.search(re.escape(start_keyword), full_text, re.IGNORECASE)
    if full_text_match:
        start_pos = full_text_match.start()
        output_text = full_text
    else:
        # Fallback: use normalized position and text
        start_pos = chosen_start_match.start()
        output_text = search_text

    # Find earliest end marker after start
    end_positions = []
    for end_pattern in end_patterns:
        end_match = re.search(end_pattern, output_text[start_pos + 50:], re.IGNORECASE)
        if end_match:
            end_positions.append(start_pos + 50 + end_match.start())

    end_pos = min(end_positions) if end_positions else len(output_text)

    return output_text[start_pos:end_pos].strip()

def _section_stats(text):
    """Calculate basic statistics for an extracted section"""
    if not text:
        return {'lines': 0, 'words': 0, 'chars': 0}
    lines = text.strip().split('\n')
    words = text.split()
    return {
        'lines': len(lines),
        'words': len(words),
        'chars': len(text)
    }

def extract_filing_sections(html_file, ticker, form_type):
    """Extract MD&A and Notes sections from SEC filing HTML.

    Each section is validated against MIN_SECTION_WORDS and, for notes sections,
    against a content marker check. Validation results are stored in each section
    dict under 'validation' so they can be surfaced in the final summary.

    Returns:
        dict: {section_name: {'file': path, 'text': content, 'stats': stats,
                               'validation': {'passed': bool, 'reason': str}}}
        or None on error
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        patterns = SECTION_PATTERNS.get(form_type)
        if not patterns:
            print(f"  Error: Unknown form type: {form_type}")
            return None

        data_dir = get_data_directory(ticker)
        sections = {}

        for section_name, section_patterns in patterns.items():
            print(f"  Extracting {section_name.upper()} section...")
            text = extract_section_text(html_content, section_patterns['start'], section_patterns['ends'])
            file_path = os.path.join(data_dir, f"{ticker}_{form_type.lower().replace('-', '')}_{section_name}.txt")

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)

            stats = _section_stats(text)
            print(f"  Saved {section_name.upper()}: {file_path} ({stats['words']:,} words, {stats['lines']:,} lines)")

            # --- Validation ---
            min_words = MIN_SECTION_WORDS.get(form_type, {}).get(section_name, 0)
            passed = True
            reason = "OK"

            if stats['words'] < min_words:
                passed = False
                reason = f"Only {stats['words']:,} words (minimum {min_words:,}) — likely captured a TOC instead of body text"
            elif section_name == 'notes' and text:
                passed, reason = _validate_notes_content(text)

            sections[section_name] = {
                'file': file_path,
                'text': text,
                'stats': stats,
                'validation': {'passed': passed, 'reason': reason},
            }

        return sections

    except Exception as e:
        print(f"  Error extracting sections: {e}")
        return None

# ============================================================================
# FILING PROCESSING
# ============================================================================

def process_filing(ticker, cik, filing_info, form_type):
    """Download and extract a single filing (10-K or 10-Q)

    Returns:
        tuple: (sections_dict, metadata_dict) - sections_dict keyed by section name
    """
    if not filing_info:
        print(f"\n{'='*60}")
        print(f"Warning: No {form_type} filing available")
        print(f"{'='*60}")
        return None, None

    print(f"\n{'='*60}")
    print(f"Processing {form_type} (Period Ending: {filing_info['report_date']})")
    print(f"{'='*60}")

    html_file = download_filing(ticker, cik, filing_info, form_type)
    if not html_file:
        return None, None

    sections = extract_filing_sections(html_file, ticker, form_type)
    if not sections:
        return None, None

    # Build metadata for this filing
    metadata = {
        'report_date': filing_info['report_date'],
        'accession': filing_info['accession'],
        'document': filing_info['document'],
        'sections': {
            name: {**sec['stats'], 'validation': sec['validation']}
            for name, sec in sections.items()
        }
    }

    return sections, metadata

# ============================================================================
# CONSOLIDATED MARKDOWN GENERATION
# ============================================================================

def generate_consolidated_markdown(ticker, metadata, all_sections):
    """Generate a single consolidated markdown with all extracted sections.

    Args:
        ticker: Ticker symbol
        metadata: Full metadata dict (with filings info)
        all_sections: dict keyed by form_type ('10-K', '10-Q'), values are section dicts

    Returns:
        Markdown string
    """
    md = []
    md.append(f"# {ticker} SEC Filings: Notes & MD&A")
    md.append(f"**Generated:** {time.strftime('%Y-%m-%d')}")

    # Filing summary
    filing_parts = []
    for form_type in ['10-K', '10-Q']:
        filing = metadata.get('filings', {}).get(form_type)
        if filing:
            filing_parts.append(f"{form_type} (period ending {filing['report_date']})")
    md.append(f"**Filings:** {', '.join(filing_parts)}")
    md.append("")

    # Section summary table
    md.append("## Section Summary")
    md.append("")
    md.append("| Section | Words | Lines |")
    md.append("|---------|------:|------:|")

    for form_type in ['10-K', '10-Q']:
        if form_type not in all_sections:
            continue
        display_names = SECTION_DISPLAY_NAMES[form_type]
        for section_name, section_data in all_sections[form_type].items():
            stats = section_data['stats']
            display = display_names.get(section_name, section_name)
            md.append(f"| {display} | {stats['words']:,} | {stats['lines']:,} |")

    md.append("")
    md.append("---")
    md.append("")

    # Full text sections
    for form_type in ['10-K', '10-Q']:
        if form_type not in all_sections:
            continue
        display_names = SECTION_DISPLAY_NAMES[form_type]
        for section_name, section_data in all_sections[form_type].items():
            display = display_names.get(section_name, section_name)
            md.append(f"## {display}")
            md.append("")
            text = section_data['text']
            if text:
                md.append(text)
            else:
                md.append("*Section not found or empty.*")
            md.append("")
            md.append("---")
            md.append("")

    return "\n".join(md)

# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="SEC Filings Preparation Script")
    parser.add_argument('ticker', type=str, help='Target company ticker symbol')
    args = parser.parse_args()
    ticker = args.ticker.upper()

    print("\n" + "="*60)
    print("SEC FILINGS PREPARATION")
    print("="*60)
    print(f"Target: {ticker}")
    print("="*60 + "\n")

    # Get CIK
    cik = get_cik_from_ticker(ticker)
    if not cik:
        print(f"\nError: Could not find CIK for {ticker}")
        sys.exit(1)

    # Fetch latest filings
    latest_10q, latest_10k = fetch_latest_filings(ticker, cik)
    if not latest_10q and not latest_10k:
        print(f"\nError: No filings found for {ticker}")
        sys.exit(1)

    # Process filings
    all_sections = {}
    metadata = {
        'ticker': ticker,
        'cik': cik,
        'fetch_date': time.strftime('%Y-%m-%d'),
        'filings': {}
    }

    for filing_info, form_type in [(latest_10k, '10-K'), (latest_10q, '10-Q')]:
        sections, meta = process_filing(ticker, cik, filing_info, form_type)
        if sections and meta:
            all_sections[form_type] = sections
            metadata['filings'][form_type] = meta

    if not metadata['filings']:
        print(f"\nError: No files created")
        sys.exit(1)

    # Save metadata
    data_dir = get_data_directory(ticker)
    metadata_file = os.path.join(data_dir, f"{ticker}_filings_metadata.json")
    save_json(metadata, metadata_file)
    print(f"\nSaved metadata: {metadata_file}")

    # Generate consolidated markdown
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    md_content = generate_consolidated_markdown(ticker, metadata, all_sections)
    md_file = os.path.join(writeup_dir, f"{ticker}_notes_mda.md")

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    # Validation summary
    print("\n" + "="*60)
    print("EXTRACTION VALIDATION")
    print("="*60)

    display_names = {
        '10-K': {'mda': '10-K MD&A', 'notes': '10-K Notes'},
        '10-Q': {'mda': '10-Q MD&A', 'notes': '10-Q Notes'},
    }

    failures = []
    col_w = 16
    print(f"  {'Section':<{col_w}} {'Words':>8}  {'Minimum':>8}  {'Status'}")
    print(f"  {'-'*col_w}  {'-'*8}  {'-'*8}  {'-'*30}")

    for form_type in ['10-K', '10-Q']:
        if form_type not in all_sections:
            continue
        for section_name, sec in all_sections[form_type].items():
            label = display_names[form_type][section_name]
            words = sec['stats']['words']
            min_words = MIN_SECTION_WORDS.get(form_type, {}).get(section_name, 0)
            v = sec['validation']
            status = "PASS" if v['passed'] else f"FAIL — {v['reason']}"
            print(f"  {label:<{col_w}} {words:>8,}  {min_words:>8,}  {status}")
            if not v['passed']:
                failures.append(f"{label}: {v['reason']}")

    print()

    if failures:
        print("RESULT: FAILED")
        print(f"\n{len(failures)} section(s) did not pass validation:")
        for f in failures:
            print(f"  • {f}")
        print("\nDo not proceed with analysis until extraction is corrected.")
        print("Check the HTML source files in the raw/ directory and re-run.\n")
        sys.exit(1)
    else:
        print("RESULT: ALL SECTIONS PASSED")
        file_count = sum(len(s) for s in all_sections.values()) + 2
        print(f"\nCreated {file_count} files for {ticker}")
        print(f"  Raw data:  {data_dir}/")
        print(f"  Writeup:   {md_file}")
        print(f"\nNext: Run the footnotes analysis prompt\n")


if __name__ == "__main__":
    main()

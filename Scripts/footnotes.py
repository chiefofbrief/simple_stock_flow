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
        - {TICKER}_mda.md             - MD&A sections only (10-K Item 7 + 10-Q Item 2)
        - {TICKER}_notes.md           - Notes to Financial Statements only (10-K + 10-Q)

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

# Section definitions: which ITEM numbers bound each section.
# Used by the discovery-based extractor (primary path).
# 'start_item': the ITEM number that opens this section, or 'NOTES' for the
#               notes-to-financial-statements header (which uses no ITEM prefix).
# 'end_items':  ITEM numbers that close this section.
# 'part_end':   'II' or 'III' if a PART boundary also closes this section.
SECTION_DEFINITIONS = {
    '10-K': {
        'mda':   {'start_item': '7',     'end_items': ['7A', '8'], 'part_end': None,
                  'title_must_contain': 'MANAGEMENT'},
        'notes': {'start_item': 'NOTES', 'end_items': ['9', '15'], 'part_end': 'III'},
    },
    '10-Q': {
        # 10-Qs have TWO "ITEM 2" sections: Part I Item 2 (MD&A) and Part II Item 2
        # (Unregistered Sales). title_must_contain disambiguates between them.
        'mda':   {'start_item': '2',     'end_items': ['3', '4'],  'part_end': None,
                  'title_must_contain': 'MANAGEMENT'},
        'notes': {'start_item': 'NOTES', 'end_items': ['2'],       'part_end': 'II'},
    },
}

# Fallback: regex-based section patterns used when discovery extraction is
# insufficient.  These are the patterns Gemini debugged for INTU — kept here
# as a safety net for unusual filings, not as the primary mechanism.
SECTION_PATTERNS = {
    '10-K': {
        'mda': {
            'start': r'ITEM\s+7\s*[\.\-:]?\s*MANAGEMENT|MANAGEMENT.S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS(?!\s*,)',
            'ends': [r'ITEM\s+7A\s*[\.\-:]?\s*QUANTITATIVE', r'ITEM\s+7A\s*[\.\-:]',
                     r'ITEM\s+8\s*[\.\-:]?\s*FINANCIAL', r'ITEM\s+8\s*[\.\-:]']
        },
        'notes': {
            'start': r'NOTES\s+TO\s+CONSOLIDATED\s+FINANCIAL\s+STATEMENTS',
            'ends': [r'ITEM\s+9\s*[\.\-:]?\s*CHANGES', r'PART\s+III', r'ITEM\s+15\s*[\.\-:]?\s*EXHIBITS']
        }
    },
    '10-Q': {
        'mda': {
            'start': r'ITEM\s+2\s*[\.\-:]?\s*MANAGEMENT',
            'ends': [r'ITEM\s+3\s*[\.\-:]?\s*QUANTITATIVE', r'ITEM\s+4\s*[\.\-:]?\s*CONTROLS']
        },
        'notes': {
            'start': r'(NOTES\s+TO\s+(UNAUDITED\s+)?(CONDENSED\s+)?CONSOLIDATED\s+FINANCIAL\s+STATEMENTS|ITEM\s+1\s*[\.\-:]?\s*FINANCIAL\s+STATEMENTS)',
            'ends': [r'ITEM\s+2\s*[\.\-:]?\s*MANAGEMENT', r'PART\s+II']
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

def html_to_text(html_content):
    """Parse HTML to plain text.

    Returns:
        (full_text, normalized_text) where full_text preserves the original
        line structure emitted by the HTMLParser (better for human/LLM reading)
        and normalized_text collapses all whitespace to single spaces (better
        for robust regex searching across split words and broken lines).
    """
    html_clean = re.sub(r'</?(ix|xbrli):[^>]*>', '', html_content)
    parser = TextExtractor()
    parser.feed(html_clean)
    full_text = '\n'.join(parser.text)
    normalized_text = re.sub(r'\s+', ' ', full_text)
    return full_text, normalized_text


def discover_filing_structure(norm_text):
    """Probe normalized document text to identify real section header positions.

    The problem with hardcoded regex patterns is that the same text (e.g.
    "ITEM 7") appears multiple times in an SEC filing: once in the table of
    contents and once as the actual section header.  Trying to distinguish
    them by formatting (period vs. hyphen vs. colon) requires per-company
    debugging every time.

    This function uses a formatting-agnostic signal instead: a real section
    header has orders of magnitude more content between it and the next
    section marker than a TOC entry does.  A TOC entry for ITEM 7 is followed
    by a page number and then the ITEM 7A entry — a few dozen characters.
    The real ITEM 7 header is followed by thousands of words of MD&A prose.

    Algorithm:
        1. Find every occurrence of "ITEM N" in normalized text.
        2. Measure the character span from each occurrence to the start of
           the next "ITEM N" occurrence.
        3. For each unique item number, select the occurrence with the
           longest span — that is the real section header.
        4. Reject candidates with < 500 chars of span (pure TOC entries).
        5. Separately discover the Notes section header (no ITEM prefix).

    Returns:
        dict with keys:
            'item_headers': {item_num_str: {
                'start': int,            # position in norm_text
                'header_text': str,      # first 120 chars starting at match
                'content_to_next': int,  # chars to next ITEM occurrence
            }}
            'notes_header': {
                'start': int,
                'header_text': str,
                'content_after': int,
            } | None
    """
    from collections import defaultdict

    # 1. Find all ITEM N occurrences (any punctuation, any casing)
    item_re = re.compile(r'\bITEM\s+(\d{1,2}[A-Z]?)\b', re.IGNORECASE)
    all_matches = list(item_re.finditer(norm_text))

    # 2. Compute span from each match to the start of the next ITEM occurrence
    candidates = []
    for i, m in enumerate(all_matches):
        next_start = all_matches[i + 1].start() if i + 1 < len(all_matches) else len(norm_text)
        candidates.append({
            'item': m.group(1).upper(),
            'start': m.start(),
            'content_to_next': next_start - m.start(),
            'header_text': norm_text[m.start():m.start() + 120].strip(),
        })

    # 3 & 4. For each item number, the real header has the longest span.
    #
    # Two-stage filtering before taking max-span:
    #
    # Stage 1 — header-syntax filter: real section headers have ITEM N followed
    #   by punctuation (-, :, .) then title words.  In-body cross-references have
    #   ITEM N followed by a comma or a lowercase function word ("Item 2, our
    #   business..." / "Item 2 for more information...").  Prefer header-like
    #   candidates; fall back to all candidates only if none qualify.
    #
    # Stage 2 — title-keyword filter (per-section, applied at extraction time via
    #   title_must_contain in SECTION_DEFINITIONS): used to distinguish same-numbered
    #   sections in different parts of a filing (e.g., 10-Q Part I Item 2 = MD&A
    #   vs. Part II Item 2 = Unregistered Sales).  Stored in item_headers so the
    #   extractor can apply it when looking up the start anchor.
    _header_suffix_re = re.compile(
        r'\bITEM\s+\d{1,2}[A-Z]?\s*[-:.]', re.IGNORECASE
    )
    _prose_suffix_re = re.compile(
        r'\bITEM\s+\d{1,2}[A-Z]?\s*(?:,|\bfor\b|\bof\b|\bto\b|\bin\b|\band\b)',
        re.IGNORECASE
    )

    by_item = defaultdict(list)
    for c in candidates:
        by_item[c['item']].append(c)

    item_headers = {}
    for item_num, group in by_item.items():
        # Stage 1: prefer header-syntax candidates over prose references
        header_like = [c for c in group if _header_suffix_re.search(c['header_text'][:40])
                       and not _prose_suffix_re.search(c['header_text'][:40])]
        pool = header_like if header_like else group
        # Store ALL header-like candidates (not just the best) so the extractor can
        # apply title_must_contain filtering before choosing the final start anchor.
        best = max(pool, key=lambda x: x['content_to_next'])
        if best['content_to_next'] > 500:   # filters TOC entries (~50-200 chars)
            item_headers[item_num] = {**best, '_all_header_like': pool}

    # 5. Notes section header (not ITEM-prefixed)
    notes_candidates = [
        r'NOTES\s+TO\s+UNAUDITED\s+CONDENSED\s+CONSOLIDATED\s+FINANCIAL\s+STATEMENTS',
        r'NOTES\s+TO\s+CONDENSED\s+CONSOLIDATED\s+FINANCIAL\s+STATEMENTS',
        r'NOTES\s+TO\s+CONSOLIDATED\s+FINANCIAL\s+STATEMENTS',
        r'NOTES\s+TO\s+FINANCIAL\s+STATEMENTS',
        r'NOTE\s+1\s*[.\-\u2013]',
    ]
    # Collect the best candidate across ALL patterns (max content_after wins).
    # Breaking on first-match-above-threshold fails when a later pattern (e.g.
    # NOTE 1) produces a far better match than an earlier pattern that scraped
    # past the 500-char floor via an exhibit-list or TOC occurrence.
    notes_header = None
    best_content = 0

    for pattern in notes_candidates:
        matches = list(re.finditer(pattern, norm_text, re.IGNORECASE))
        if not matches:
            continue

        def _content_after(m):
            # Span from match end to the nearest real item header that follows it
            following = [h['start'] for h in item_headers.values() if h['start'] > m.end()]
            return (min(following) if following else len(norm_text)) - m.end()

        best = max(matches, key=_content_after)
        content_len = _content_after(best)
        if content_len > 500 and content_len > best_content:
            best_content = content_len
            notes_header = {
                'start': best.start(),
                'header_text': norm_text[best.start():best.start() + 120].strip(),
                'content_after': content_len,
            }

    return {'item_headers': item_headers, 'notes_header': notes_header}


def extract_section_by_discovery(full_text, norm_text, structure, start_item, end_items,
                                  part_end=None, title_must_contain=None):
    """Extract a filing section using positions discovered by discover_filing_structure().

    Uses exact discovered positions rather than regex patterns for end boundaries,
    eliminating false matches on in-body references like "see Item 8 of this
    Annual Report" that share phrasing with actual section headers.

    Args:
        full_text:           Original parsed text (preserves line breaks for readability)
        norm_text:           Normalized text (single-space, for position lookup)
        structure:           Output of discover_filing_structure()
        start_item:          Item number string ('7', '2') or 'NOTES'
        end_items:           List of item number strings that terminate this section
        part_end:            'II' or 'III' if a PART boundary also terminates the section
        title_must_contain:  If set, the selected ITEM header's text must contain this
                             substring (case-insensitive).  Used to disambiguate same-
                             numbered sections in different filing parts (e.g., 10-Q
                             Part I Item 2 = MD&A vs. Part II Item 2 = Unregistered
                             Sales).  When the default best candidate does not match,
                             the extractor tries other header-like candidates in
                             descending span order.

    Returns:
        Extracted section text, or "" if the section could not be located.
    """
    item_headers = structure['item_headers']
    notes_header = structure['notes_header']

    # --- Locate start in norm_text ---
    if start_item == 'NOTES':
        if not notes_header:
            return ""
        start_norm = notes_header['start']
        anchor = notes_header['header_text'][:40]
    elif start_item in item_headers:
        entry = item_headers[start_item]
        if title_must_contain:
            # Try each header-like candidate in descending span order until one
            # whose title contains the required keyword is found.
            pool = sorted(entry.get('_all_header_like', [entry]),
                          key=lambda x: x['content_to_next'], reverse=True)
            chosen = next(
                (c for c in pool
                 if title_must_contain.upper() in c['header_text'].upper()),
                None
            )
            if not chosen:
                # No candidate matches — fall back to default best
                chosen = entry
        else:
            chosen = entry
        start_norm = chosen['start']
        anchor = chosen['header_text'][:40]
    else:
        return ""

    # --- Locate end in norm_text ---
    end_candidates = []
    for end_item in end_items:
        if end_item in item_headers and item_headers[end_item]['start'] > start_norm + 100:
            end_candidates.append(item_headers[end_item]['start'])

    if part_end:
        # Search for PART II/III at least 5,000 chars past the start to skip
        # any in-section mentions of "Part II" or "Part III"
        part_re = re.compile(r'\bPART\s+' + re.escape(part_end) + r'\b', re.IGNORECASE)
        for m in part_re.finditer(norm_text, start_norm + 5000):
            end_candidates.append(m.start())
            break

    end_norm = min(end_candidates) if end_candidates else len(norm_text)

    # --- Map norm_text positions back to full_text ---
    # norm_text has single spaces; full_text may have newlines between the same
    # tokens.  Replace escaped spaces in the anchor with \s+ to match either.
    anchor_pattern = re.sub(r'\\ ', r'\\s+', re.escape(anchor))
    start_match = re.search(anchor_pattern, full_text, re.IGNORECASE)
    if not start_match:
        # Can't map back — return the norm_text slice (still readable for LLMs)
        return norm_text[start_norm:end_norm].strip()

    start_full = start_match.start()

    if end_norm < len(norm_text):
        end_anchor = norm_text[end_norm:end_norm + 40]
        end_anchor_pattern = re.sub(r'\\ ', r'\\s+', re.escape(end_anchor))
        end_match = re.search(end_anchor_pattern, full_text[start_full + 100:], re.IGNORECASE)
        end_full = start_full + 100 + end_match.start() if end_match else len(full_text)
    else:
        end_full = len(full_text)

    return full_text[start_full:end_full].strip()


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
    # so the output preserves the original line structure.
    # Use proportional position scaling to handle multiple occurrences of the same header
    # (e.g., TOC vs body) — always pick the full_text occurrence closest to where we expect.
    start_keyword = chosen_start_match.group(0)
    full_text_matches = list(re.finditer(re.escape(start_keyword), full_text, re.IGNORECASE))
    if full_text_matches:
        norm_ratio = chosen_start_match.start() / max(len(search_text), 1)
        expected_ft_pos = int(norm_ratio * len(full_text))
        full_text_match = min(full_text_matches, key=lambda m: abs(m.start() - expected_ft_pos))
        start_pos = full_text_match.start()
        output_text = full_text
    else:
        # Fallback: use normalized position and text, but restore line breaks
        # at sentence boundaries so the output isn't a single collapsed line.
        start_pos = chosen_start_match.start()
        restored = re.sub(r'(?<=[.!?])\s+(?=[A-Z("])', '\n', search_text)
        output_text = restored

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

    Primary path: discover_filing_structure() probes the document to find real
    section header positions (not TOC entries), then extract_section_by_discovery()
    uses those positions directly.  This eliminates false boundary matches caused
    by in-body references to section numbers (e.g. "see Item 8 of this report").

    Fallback: if discovery extraction produces insufficient text (<100 words),
    the original regex-based extract_section_text() is used instead.

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

        # --- Parse HTML once; reused across all sections ---
        full_text, norm_text = html_to_text(html_content)

        # --- Probe document structure ---
        structure = discover_filing_structure(norm_text)

        print(f"\n  Structure discovery:")
        item_headers = structure['item_headers']
        for item_num in sorted(item_headers.keys(), key=lambda x: (len(x), x)):
            h = item_headers[item_num]
            preview = h['header_text'].replace('\n', ' ')[:72]
            print(f"    ITEM {item_num:<3} ({h['content_to_next']:>9,} chars): {preview}")
        if structure['notes_header']:
            nh = structure['notes_header']
            preview = nh['header_text'].replace('\n', ' ')[:72]
            print(f"    NOTES   ({nh['content_after']:>9,} chars): {preview}")
        else:
            print(f"    NOTES: not found by discovery")

        # --- Extract sections ---
        section_defs = SECTION_DEFINITIONS.get(form_type)
        fallback_patterns = SECTION_PATTERNS.get(form_type)
        if not section_defs:
            print(f"  Error: Unknown form type: {form_type}")
            return None

        data_dir = get_data_directory(ticker)
        sections = {}

        for section_name, defn in section_defs.items():
            print(f"\n  Extracting {section_name.upper()} section...")

            # Primary: discovery-based extraction
            text = extract_section_by_discovery(
                full_text, norm_text, structure,
                start_item=defn['start_item'],
                end_items=defn['end_items'],
                part_end=defn.get('part_end'),
                title_must_contain=defn.get('title_must_contain'),
            )

            if len(text.split()) >= 100:
                print(f"  Discovery extraction: {len(text.split()):,} words")
            else:
                # Fallback: regex-based extraction
                print(f"  Discovery insufficient ({len(text.split())} words) — falling back to regex patterns")
                fp = fallback_patterns.get(section_name) if fallback_patterns else None
                if fp:
                    text = extract_section_text(html_content, fp['start'], fp['ends'])
                    print(f"  Fallback extraction: {len(text.split()):,} words")
                else:
                    print(f"  No fallback patterns available for {section_name}")

            file_path = os.path.join(data_dir, f"{ticker}_{form_type.lower().replace('-', '')}_{section_name}.txt")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)

            stats = _section_stats(text)
            print(f"  Saved: {file_path} ({stats['words']:,} words, {stats['lines']:,} lines)")

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
        import traceback
        traceback.print_exc()
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

def generate_section_markdown(ticker, metadata, all_sections, section_type):
    """Generate markdown for a single section type ('mda' or 'notes').

    Args:
        ticker: Ticker symbol
        metadata: Full metadata dict (with filings info)
        all_sections: dict keyed by form_type ('10-K', '10-Q'), values are section dicts
        section_type: 'mda' or 'notes'

    Returns:
        Markdown string
    """
    titles = {
        'mda': 'MD&A',
        'notes': 'Notes to Financial Statements',
    }
    md = []
    md.append(f"# {ticker} SEC Filings: {titles[section_type]}")
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
        if form_type not in all_sections or section_type not in all_sections[form_type]:
            continue
        section_data = all_sections[form_type][section_type]
        display = SECTION_DISPLAY_NAMES[form_type].get(section_type, section_type)
        stats = section_data['stats']
        md.append(f"| {display} | {stats['words']:,} | {stats['lines']:,} |")

    md.append("")
    md.append("---")
    md.append("")

    # Full text sections
    for form_type in ['10-K', '10-Q']:
        if form_type not in all_sections or section_type not in all_sections[form_type]:
            continue
        section_data = all_sections[form_type][section_type]
        display = SECTION_DISPLAY_NAMES[form_type].get(section_type, section_type)
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

    # Generate split markdown files
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)

    mda_file = os.path.join(writeup_dir, f"{ticker}_mda.md")
    notes_file = os.path.join(writeup_dir, f"{ticker}_notes.md")

    mda_content = generate_section_markdown(ticker, metadata, all_sections, 'mda')
    with open(mda_file, 'w', encoding='utf-8') as f:
        f.write(mda_content)

    notes_content = generate_section_markdown(ticker, metadata, all_sections, 'notes')
    with open(notes_file, 'w', encoding='utf-8') as f:
        f.write(notes_content)

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
        print(f"  MD&A:      {mda_file}")
        print(f"  Notes:     {notes_file}")
        print(f"\nNext: Run the footnotes analysis prompt\n")


if __name__ == "__main__":
    main()

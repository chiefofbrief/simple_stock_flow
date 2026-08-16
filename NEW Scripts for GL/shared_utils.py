"""
Shared Utility Functions — GL Stock-Data Scripts
================================================

Common helpers used across the GL scripts (flat folder). Output convention:

    Stock Data/{TICKER}/            <- .md summaries + metrics JSON (writeup dir)
    Stock Data/{TICKER}/raw/        <- raw JSON / HTML (peer raw nests here, ticker-prefixed)

Provides: API request handling with retry, file/dir management, date ranges, file I/O.
"""

import requests
import json
import os
import re
import time
from datetime import datetime, timedelta

# ============================================================================
# CONSTANTS
# ============================================================================

MAX_RETRIES = 3
REQUEST_TIMEOUT = 10
RETRY_DELAY = 5
API_CALL_DELAY = 1

OUTPUT_ROOT = "Stock Data"

# ============================================================================
# DIRECTORY & FILE MANAGEMENT
# ============================================================================

def get_writeup_directory(ticker):
    """Top-level ticker folder for .md summaries and metrics JSON.

    e.g. Stock Data/AAPL
    """
    return os.path.join(OUTPUT_ROOT, ticker)


def get_data_directory(ticker, target_ticker=None):
    """Raw data directory.

    Everything for a ticker (and its peers) lives under the TARGET ticker's folder — no
    separate peer subfolder. Peer raw files land in the same raw/ dir, distinguished by
    their ticker prefix in the filename (e.g. Stock Data/AAPL/raw/MSFT_income_annual.json).

    Args:
        ticker:        Ticker to get a directory for.
        target_ticker: The main ticker of the run. If given (peer case), raw goes under it.

    Returns:
        e.g. Stock Data/AAPL/raw
    """
    primary = target_ticker if target_ticker else ticker
    return os.path.join(OUTPUT_ROOT, primary, "raw")


def ensure_directory_exists(directory):
    """Create directory (and parents) if it doesn't exist."""
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# ============================================================================
# API REQUEST HANDLING
# ============================================================================

def fetch_alpha_vantage(url, max_retries=MAX_RETRIES):
    """Fetch from AlphaVantage with retry logic for rate limits. Returns dict or None."""
    for attempt in range(max_retries):
        if attempt > 0:
            print(f"  ...Retry {attempt}/{max_retries}...")

        try:
            r = requests.get(url, timeout=REQUEST_TIMEOUT)
        except requests.exceptions.RequestException as e:
            print(f"  Error: Network request failed: {e}")
            time.sleep(RETRY_DELAY)
            continue

        if r.status_code != 200:
            print(f"  Error: HTTP {r.status_code}")
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY)
                continue
            return None

        try:
            data = r.json()
        except ValueError:
            print("  Error: Invalid JSON response")
            return None

        if "Error Message" in data:
            print(f"  API Error: {data['Error Message']}")
            return None

        if "Note" in data or "Information" in data:
            msg = data.get("Note") or data.get("Information")
            if "rate limit" in msg.lower() or "call frequency" in msg.lower():
                print(f"  ⚠️  Rate Limit Hit: {msg}")
                if attempt < max_retries - 1:
                    time.sleep(RETRY_DELAY)
                    continue
                print("  ❌ Max retries reached. Rate limit persists.")
                return None

        if attempt == 0:
            time.sleep(API_CALL_DELAY)

        return data

    return None


def make_request_with_retry(request_func, max_retries=MAX_RETRIES):
    """Generic retry wrapper for any request-returning callable. Returns JSON or error dict."""
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                print(f"  Retry {attempt}/{max_retries}...")
                time.sleep(RETRY_DELAY)

            response = request_func()

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                print(f"  Rate limit hit (429), waiting {RETRY_DELAY}s...")
                if attempt < max_retries - 1:
                    time.sleep(RETRY_DELAY)
                    continue
                return {'error': 'Rate limit exceeded', 'status_code': 429}
            else:
                print(f"  HTTP {response.status_code}: {response.text[:200]}")
                if attempt < max_retries - 1:
                    continue
                return {'error': f'HTTP {response.status_code}', 'status_code': response.status_code}

        except requests.exceptions.Timeout:
            print(f"  Request timeout after {REQUEST_TIMEOUT}s")
            if attempt < max_retries - 1:
                continue
            return {'error': 'Request timeout'}
        except Exception as e:
            print(f"  Error: {str(e)}")
            if attempt < max_retries - 1:
                continue
            return {'error': str(e)}

    return {'error': 'Max retries exceeded'}

# ============================================================================
# DATE UTILITIES
# ============================================================================

def get_date_range_months_back(months=6):
    """Return (from_date, to_date) in YYYY-MM-DD, `months` back to today (30-day approx)."""
    to_date = datetime.now()
    from_date = to_date - timedelta(days=months * 30)
    return from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d")

# ============================================================================
# FILE I/O HELPERS
# ============================================================================

def save_json(data, filepath):
    """Save data to JSON (pretty). Returns True/False."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving JSON to {filepath}: {e}")
        return False


def load_json(filepath):
    """Load JSON from file. Returns dict or None."""
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading JSON from {filepath}: {e}")
    return None


def get_company_name(ticker: str) -> str:
    """Resolve a cleaned company name via FMP search-symbol. Empty string if not found."""
    fmp_key = os.environ.get('FMP_API_KEY')
    if not fmp_key:
        return ""

    try:
        url = f"https://financialmodelingprep.com/stable/search-symbol?query={ticker}&limit=5&apikey={fmp_key}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data:
                for item in data:
                    if item.get('symbol') == ticker.upper():
                        name = item.get('name', '')
                        if not name:
                            return ""
                        suffixes = r'(?i)(?:\s+inc\.?|\s+corp\.?|\s+corporation|\s+company|\s+ltd\.?|\s+plc\.?|\s+group|\s+holdings|,\s*inc\.?)$'
                        return re.sub(suffixes, '', name).strip()
    except Exception:
        pass
    return ""


# ============================================================================
# FORMATTING HELPERS
# ============================================================================

def fmt_market_cap(val):
    """Format a market cap number as $X.XXT / $X.XXB / $X.XXM."""
    try:
        v = float(val)
    except (TypeError, ValueError):
        return "N/A"
    for div, suffix in ((1e12, "T"), (1e9, "B"), (1e6, "M")):
        if abs(v) >= div:
            return f"${v/div:,.2f}{suffix}"
    return f"${v:,.0f}"


def years_since(date_str):
    """Whole+decimal years between date_str (YYYY-MM-DD) and today. None if unparseable."""
    if not date_str:
        return None
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return round((datetime.now() - d).days / 365.25, 1)
    except (ValueError, TypeError):
        return None

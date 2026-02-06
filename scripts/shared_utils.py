"""
Shared Utility Functions for Stock Data Preparation Scripts
============================================================

Common functions used across all data preparation scripts:
- SCRIPT_statements.py
- SCRIPT_notes.py
- SCRIPT_calls.py
- SCRIPT_news.py

This module provides:
- API request handling with retry logic
- File and directory management
- Date range calculations
- Tracking document updates
"""

import requests
import json
import os
import time
from datetime import datetime, timedelta

# ============================================================================
# CONSTANTS
# ============================================================================

REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 5
RETRY_DELAY = 60  # seconds
API_CALL_DELAY = 13  # seconds - proactive delay between API calls (safe for free tier: 5 calls/min)

# ============================================================================
# DIRECTORY & FILE MANAGEMENT
# ============================================================================

def get_data_directory(ticker, target_ticker=None):
    """Get the data directory for a ticker using nested structure under data/analysis/

    Args:
        ticker: The ticker to get directory for
        target_ticker: The target (main) ticker. If None, assumes ticker is target.

    Returns:
        Path to data directory (nested if ticker is a peer)
    """
    base_dir = os.path.join("data", "analysis")
    if target_ticker is None or ticker == target_ticker:
        return os.path.join(base_dir, ticker)
    else:
        # Peer ticker - nest under target
        return os.path.join(base_dir, target_ticker, ticker)

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist

    Args:
        directory: Directory path to create
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# ============================================================================
# API REQUEST HANDLING
# ============================================================================

def fetch_alpha_vantage(url, max_retries=MAX_RETRIES):
    """Fetch data from AlphaVantage API with retry logic for rate limits

    Args:
        url: Full API URL to fetch
        max_retries: Maximum number of retry attempts

    Returns:
        dict: JSON response data, or None if failed
    """
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
                print(f"  Waiting {RETRY_DELAY} seconds before retry...")
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

        # Check for rate limit messages (Note or Information)
        if "Note" in data or "Information" in data:
            msg = data.get("Note") or data.get("Information")
            if "rate limit" in msg.lower() or "call frequency" in msg.lower():
                print(f"  ⚠️  Rate Limit Hit: {msg}")
                if attempt < max_retries - 1:
                    print(f"  ⏳ Waiting {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                    continue
                else:
                    print(f"  ❌ Max retries reached. Rate limit persists.")
                    return None
            else:
                # Some other note, seemingly fine but warn just in case
                # print(f"  API Note: {msg}")
                pass

        # Proactive rate limiting: delay before next call
        if attempt == 0:  # Only on first successful attempt (not retries)
            time.sleep(API_CALL_DELAY)

        return data

    return None

def make_request_with_retry(request_func, max_retries=MAX_RETRIES):
    """Generic retry wrapper for any API request

    Args:
        request_func: Lambda/function that makes the actual request
        max_retries: Maximum number of retry attempts

    Returns:
        dict: JSON response or error dict
    """
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
    """Get date range from N months back to today

    Args:
        months: Number of months to look back (default 6)

    Returns:
        tuple: (from_date, to_date) in YYYY-MM-DD format
    """
    to_date = datetime.now()
    from_date = to_date - timedelta(days=months * 30)  # Approximate

    return from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d")

# ============================================================================
# TRACKING DOCUMENT
# ============================================================================

def create_or_update_tracking(ticker, target_ticker, analysis_type, key_findings):
    """Create or update tracking.md file

    Args:
        ticker: The ticker being tracked
        target_ticker: The target (main) ticker
        analysis_type: Type of analysis (e.g., "Earnings Call Data Preparation")
        key_findings: List of strings describing key findings/actions
    """
    data_dir = get_data_directory(ticker, target_ticker)
    tracking_file = os.path.join(data_dir, f"{ticker}_tracking.md")

    # Create tracking file if it doesn't exist
    if not os.path.exists(tracking_file):
        ensure_directory_exists(data_dir)
        with open(tracking_file, 'w') as f:
            f.write(f"# {ticker} Analysis Tracking\n\n")
            f.write("This document tracks all analyses and data preparation activities.\n\n")
            f.write("---\n\n")

    # Append new entry
    with open(tracking_file, 'a') as f:
        f.write(f"## [{datetime.now().strftime('%Y-%m-%d')}] - {analysis_type}\n\n")

        if key_findings:
            f.write("**Key Actions:**\n")
            for finding in key_findings:
                f.write(f"- {finding}\n")
            f.write("\n")

        f.write("---\n\n")

    print(f"✓ Tracking updated: {tracking_file}")

# ============================================================================
# FILE I/O HELPERS
# ============================================================================

def save_json(data, filepath):
    """Save data to JSON file with pretty formatting

    Args:
        data: Data to save (must be JSON-serializable)
        filepath: Full path to output file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving JSON to {filepath}: {e}")
        return False

def load_json(filepath):
    """Load JSON data from file

    Args:
        filepath: Full path to JSON file

    Returns:
        dict: Loaded data, or None if failed
    """
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading JSON from {filepath}: {e}")
    return None

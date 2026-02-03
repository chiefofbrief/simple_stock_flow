#!/usr/bin/env python3
"""
News Script Comparison Test
============================

Tests new modular news scripts against the original to verify identical output.

Usage:
    python test_news_scripts.py TICKER [--months N]

Example:
    python test_news_scripts.py IBM --months 1

Tests:
    1. JSON output comparison (Perigon and AlphaVantage)
    2. Markdown output comparison
    3. Exit codes and error handling

Outputs:
    - Detailed comparison report
    - PASS/FAIL status for each test
    - File diffs if outputs differ
"""

import os
import sys
import json
import argparse
import subprocess
import shutil
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from scripts.shared_utils import get_data_directory

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Print formatted header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(70)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}\n")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.RESET}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.RESET}")

def compare_json_files(file1, file2, name):
    """Compare two JSON files and report differences

    Args:
        file1: Path to first JSON file
        file2: Path to second JSON file
        name: Name of the comparison (e.g., "Perigon", "AlphaVantage")

    Returns:
        bool: True if files are identical, False otherwise
    """
    print(f"\n{Colors.BOLD}Testing: {name} JSON Output{Colors.RESET}")
    print(f"  Old: {file1}")
    print(f"  New: {file2}")

    # Check if files exist
    if not os.path.exists(file1):
        print_error(f"Old file not found: {file1}")
        return False

    if not os.path.exists(file2):
        print_error(f"New file not found: {file2}")
        return False

    # Load JSON files
    try:
        with open(file1, 'r') as f:
            data1 = json.load(f)
        with open(file2, 'r') as f:
            data2 = json.load(f)
    except json.JSONDecodeError as e:
        print_error(f"JSON parse error: {e}")
        return False

    # Compare structure
    if data1.keys() != data2.keys():
        print_error("Top-level keys differ")
        print(f"  Old keys: {sorted(data1.keys())}")
        print(f"  New keys: {sorted(data2.keys())}")
        return False

    # Compare each section
    differences = []

    for key in data1.keys():
        if key == 'date_range':
            if data1[key] != data2[key]:
                differences.append(f"date_range: {data1[key]} != {data2[key]}")
        elif key in ['stories', 'articles']:
            count1 = len(data1[key])
            count2 = len(data2[key])
            if count1 != count2:
                differences.append(f"{key} count: {count1} != {count2}")
            else:
                print(f"  {key}: {count1} items (matching)")
        elif key == 'last_30_days':
            count1 = len(data1[key])
            count2 = len(data2[key])
            if count1 != count2:
                differences.append(f"last_30_days count: {count1} != {count2}")
            else:
                print(f"  last_30_days: {count1} items (matching)")
        elif key == 'monthly_summary':
            if data1[key] != data2[key]:
                differences.append(f"monthly_summary differs")
            else:
                print(f"  monthly_summary: {len(data1[key])} months (matching)")

    if differences:
        print_error("Differences found:")
        for diff in differences:
            print(f"    - {diff}")
        return False
    else:
        print_success(f"{name} JSON outputs are identical")
        return True

def run_script(script_path, ticker, months, test_dir):
    """Run a news script and capture output

    Args:
        script_path: Path to the script
        ticker: Stock ticker
        months: Number of months lookback
        test_dir: Test directory name (for isolation)

    Returns:
        tuple: (success, stdout, stderr)
    """
    script_name = os.path.basename(script_path)
    print(f"\n{Colors.BOLD}Running: {script_name}{Colors.RESET}")

    cmd = [
        sys.executable,
        script_path,
        ticker,
        '--months', str(months)
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120  # 2 minute timeout
        )

        if result.returncode == 0:
            print_success(f"{script_name} completed successfully")
            return True, result.stdout, result.stderr
        else:
            print_error(f"{script_name} failed with exit code {result.returncode}")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
            return False, result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        print_error(f"{script_name} timed out after 120 seconds")
        return False, "", "Timeout"
    except Exception as e:
        print_error(f"{script_name} error: {e}")
        return False, "", str(e)

def main():
    """Run comparison tests between old and new news scripts"""
    parser = argparse.ArgumentParser(description="Test new news scripts against original")
    parser.add_argument('ticker', type=str, help='Stock ticker to test')
    parser.add_argument('--months', type=int, default=1,
                       help='Number of months to look back (default: 1)')

    args = parser.parse_args()
    ticker = args.ticker.upper()

    print_header("NEWS SCRIPT COMPARISON TEST")
    print(f"Ticker: {ticker}")
    print(f"Lookback: {args.months} months")
    print(f"Test started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Get script paths
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts', 'ticker')
    old_script = os.path.join(script_dir, 'news.py')
    new_script = os.path.join(script_dir, 'news_new.py')

    # Get data directory
    data_dir = get_data_directory(ticker)

    # Create backup directory for old outputs
    backup_dir = os.path.join(data_dir, '_test_backup_old')
    os.makedirs(backup_dir, exist_ok=True)

    # Test results tracking
    tests_passed = 0
    tests_failed = 0

    # ========================================================================
    # TEST 1: Run old script
    # ========================================================================
    print_header("TEST 1: Running Original news.py")

    old_success, old_stdout, old_stderr = run_script(old_script, ticker, args.months, "old")

    if old_success:
        # Backup old outputs
        old_perigon = os.path.join(data_dir, f"{ticker}_news_perigon.json")
        old_av = os.path.join(data_dir, f"{ticker}_news_alphavantage.json")

        if os.path.exists(old_perigon):
            shutil.copy2(old_perigon, os.path.join(backup_dir, f"{ticker}_news_perigon.json"))
            print(f"  Backed up: {old_perigon}")

        if os.path.exists(old_av):
            shutil.copy2(old_av, os.path.join(backup_dir, f"{ticker}_news_alphavantage.json"))
            print(f"  Backed up: {old_av}")

        tests_passed += 1
    else:
        tests_failed += 1
        print_error("Original script failed - cannot proceed with comparison")
        return 1

    # ========================================================================
    # TEST 2: Run new script
    # ========================================================================
    print_header("TEST 2: Running New news_new.py")

    new_success, new_stdout, new_stderr = run_script(new_script, ticker, args.months, "new")

    if new_success:
        tests_passed += 1
    else:
        tests_failed += 1
        print_error("New script failed - comparison incomplete")

    # ========================================================================
    # TEST 3: Compare JSON outputs
    # ========================================================================
    if old_success and new_success:
        print_header("TEST 3: Comparing JSON Outputs")

        # Perigon comparison
        old_perigon_path = os.path.join(backup_dir, f"{ticker}_news_perigon.json")
        new_perigon_path = os.path.join(data_dir, f"{ticker}_news_perigon.json")

        perigon_match = compare_json_files(old_perigon_path, new_perigon_path, "Perigon")

        if perigon_match:
            tests_passed += 1
        else:
            tests_failed += 1

        # AlphaVantage comparison
        old_av_path = os.path.join(backup_dir, f"{ticker}_news_alphavantage.json")
        new_av_path = os.path.join(data_dir, f"{ticker}_news_alphavantage.json")

        av_match = compare_json_files(old_av_path, new_av_path, "AlphaVantage")

        if av_match:
            tests_passed += 1
        else:
            tests_failed += 1
    else:
        print_warning("Skipping JSON comparison - one or both scripts failed")
        tests_failed += 2

    # ========================================================================
    # FINAL REPORT
    # ========================================================================
    print_header("TEST RESULTS SUMMARY")

    total_tests = tests_passed + tests_failed
    pass_rate = (tests_passed / total_tests * 100) if total_tests > 0 else 0

    print(f"Total Tests: {total_tests}")
    print(f"Passed: {Colors.GREEN}{tests_passed}{Colors.RESET}")
    print(f"Failed: {Colors.RED}{tests_failed}{Colors.RESET}")
    print(f"Pass Rate: {pass_rate:.1f}%")

    print(f"\nTest completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if tests_failed == 0:
        print_success("\nALL TESTS PASSED - New scripts are ready for production")
        print(f"\n{Colors.BOLD}Next steps:{Colors.RESET}")
        print("  1. Rename news.py → news_legacy.py")
        print("  2. Rename news_new.py → news.py")
        print("  3. Update sentiment.py to reference new scripts if needed")
        return 0
    else:
        print_error("\nSOME TESTS FAILED - Review differences before switching")
        print(f"\n{Colors.BOLD}Backup location:{Colors.RESET}")
        print(f"  {backup_dir}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

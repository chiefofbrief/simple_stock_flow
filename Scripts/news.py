#!/usr/bin/env python3
"""
News Script
===========

Fetches recent news for a stock ticker from Perigon and FMP and produces
a combined markdown report for use in the Context analysis step.

Usage:
    python Scripts/news.py ADBE
    python Scripts/news.py ADBE --months 6

Output:
    Data/tickers/{TICKER}/{TICKER}_news.md
"""

import sys
import os
import argparse
import subprocess

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    get_date_range_months_back,
    load_json,
)

# generate_news_markdown lives in Research Scripts/news.py
import importlib.util
_news_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "Research Scripts", "news.py"
)
_spec = importlib.util.spec_from_file_location("news_formatter", _news_path)
_news_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_news_module)
generate_news_markdown = _news_module.generate_news_markdown


def main():
    parser = argparse.ArgumentParser(description="News fetch — Perigon + FMP")
    parser.add_argument("ticker", help="Ticker symbol")
    parser.add_argument(
        "--months", type=int, default=3, help="News lookback in months (default: 3)"
    )
    args = parser.parse_args()

    ticker = args.ticker.upper()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    research_dir = os.path.join(script_dir, "Research Scripts")
    cmd_args = [ticker, "--months", str(args.months)]

    print(f"\n=== News: {ticker} ===")

    # --- Fetch Perigon ---
    perigon_ok = False
    try:
        subprocess.run(
            [sys.executable, os.path.join(research_dir, "news_perigon.py")] + cmd_args,
            check=True,
        )
        perigon_ok = True
    except subprocess.CalledProcessError as e:
        print(f"  ⚠ Perigon fetch failed: {e}")

    # --- Fetch FMP ---
    fmp_ok = False
    try:
        subprocess.run(
            [sys.executable, os.path.join(research_dir, "news_fmp.py")] + cmd_args,
            check=True,
        )
        fmp_ok = True
    except subprocess.CalledProcessError as e:
        print(f"  ⚠ FMP fetch failed: {e}")

    # --- Load JSON outputs ---
    data_dir = get_data_directory(ticker)
    from_date, to_date = get_date_range_months_back(args.months)

    p_data = {}
    f_data = {}

    perigon_file = os.path.join(data_dir, f"{ticker}_news_perigon.json")
    fmp_file = os.path.join(data_dir, f"{ticker}_news_fmp.json")

    if os.path.exists(perigon_file):
        p_data = load_json(perigon_file) or {}
    if os.path.exists(fmp_file):
        f_data = load_json(fmp_file) or {}

    perigon_count = len(p_data.get("stories", []))
    fmp_count = len(f_data.get("articles", []))

    # --- Verification: fail if no data from either source ---
    if perigon_count == 0 and fmp_count == 0:
        print(f"\n✗ FAILED: No news data retrieved for {ticker} from any source.")
        print("  Check API keys (PERIGON_API_KEY, FMP_API_KEY) and network connectivity.")
        sys.exit(1)

    # --- Generate and save markdown ---
    markdown = generate_news_markdown(ticker, p_data, f_data, from_date, to_date)

    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(writeup_dir)
    out_path = os.path.join(writeup_dir, f"{ticker}_news.md")

    with open(out_path, "w") as f:
        f.write(markdown)

    # --- Summary ---
    print(f"\n--- Summary ---")
    print(f"  Perigon : {'✓' if perigon_ok else '⚠ failed'} — {perigon_count} stories")
    print(f"  FMP     : {'✓' if fmp_ok else '⚠ failed'} — {fmp_count} articles")
    print(f"  Output  : {out_path}")

    # Warn but don't fail if only one source came through
    if not perigon_ok or not fmp_ok:
        print(f"\n  ⚠ One source failed — output is partial. Review before analysis.")

    print("\nDone.")


if __name__ == "__main__":
    main()

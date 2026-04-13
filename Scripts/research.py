#!/usr/bin/env python3
"""
Research Script
===============

Fetches recent news data (Perigon + FMP) for the Research analysis step.
Outputs a combined markdown report for investigating open questions from
prior analyses (Financials, Footnotes, Earnings Calls).

Usage:
    python Scripts/research.py TICKER [--months N]

Output:
    Data/tickers/{TICKER}/{TICKER}_research.md
"""

import sys
import os
import argparse
import subprocess
import importlib.util

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    get_date_range_months_back,
    load_json
)

# Import generate_news_markdown from news.py (path contains a space)
_news_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "Research Scripts", "news.py")
_spec = importlib.util.spec_from_file_location("news", _news_path)
_news_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_news_module)
generate_news_markdown = _news_module.generate_news_markdown


def main():
    parser = argparse.ArgumentParser(description="Research — News Data Fetch (Perigon + FMP)")
    parser.add_argument("ticker", help="Ticker symbol")
    parser.add_argument("--months", type=int, default=3,
                        help="News lookback in months (default: 3)")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sentiment_dir = os.path.join(script_dir, "Research Scripts")
    cmd_args = [ticker, "--months", str(args.months)]

    # 1. Fetch Perigon (1 API call)
    print(f"\nFetching Perigon news for {ticker}...")
    try:
        subprocess.run(
            [sys.executable, os.path.join(sentiment_dir, "news_perigon.py")] + cmd_args,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"  Warning: Perigon fetch failed: {e}")

    # 2. Fetch FMP (1 API call)
    print(f"Fetching FMP news for {ticker}...")
    try:
        subprocess.run(
            [sys.executable, os.path.join(sentiment_dir, "news_fmp.py")] + cmd_args,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"  Warning: FMP fetch failed: {e}")

    # 3. Load JSON outputs
    from_date, to_date = get_date_range_months_back(args.months)
    data_dir = get_data_directory(ticker)
    perigon_file = os.path.join(data_dir, f"{ticker}_news_perigon.json")
    fmp_file = os.path.join(data_dir, f"{ticker}_news_fmp.json")

    p_data = load_json(perigon_file) if os.path.exists(perigon_file) else {}
    f_data = load_json(fmp_file) if os.path.exists(fmp_file) else {}

    # 4. Generate and save combined markdown
    markdown = generate_news_markdown(ticker, p_data, f_data, from_date, to_date)

    output_dir = get_writeup_directory(ticker)
    ensure_directory_exists(output_dir)
    report_path = os.path.join(output_dir, f"{ticker}_research.md")

    with open(report_path, "w") as f:
        f.write(markdown)

    print(f"\nResearch data saved to {report_path}")
    print(f"  Perigon: {len(p_data.get('stories', []))} stories")
    print(f"  FMP:     {len(f_data.get('articles', []))} articles")


if __name__ == "__main__":
    main()

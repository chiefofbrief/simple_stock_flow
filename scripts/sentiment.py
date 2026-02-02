#!/usr/bin/env python3
"""
Sentiment Analysis Master Script
=================================

Aggregates sentiment data from news and social media sources for stock analysis.
Combines output from news.py, reddit.py, tiktok.py, and youtube.py scripts.

Usage:
    python scripts/sentiment.py TICKER --all                    # All sources
    python scripts/sentiment.py TICKER --news --reddit          # Specific sources
    python scripts/sentiment.py TICKER --all --news-months 1    # Override timeline

Output:
    data/analysis/{TICKER}/{TICKER}_sentiment.md
"""

import argparse
import sys
import subprocess
import datetime
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

# Default timeline parameters
DEFAULT_NEWS_MONTHS = 3
DEFAULT_REDDIT_DAYS = 30  # 1 month
DEFAULT_TIKTOK_PERIOD = 'this-month'
DEFAULT_YOUTUBE_PERIOD = 'this_month'

def get_command(source, ticker, args):
    """Get the specific command list for a source based on arguments."""

    # Base commands with ticker and markdown flag
    cmds = {
        'news': ['python', 'scripts/ticker/news.py', ticker, '--markdown'],
        'reddit': ['python', 'scripts/ticker/reddit.py', '--ticker', ticker, '--markdown'],
        'tiktok': ['python', 'scripts/ticker/tiktok.py', ticker, '--markdown'],
        'youtube': ['python', 'scripts/ticker/youtube.py', ticker, '--markdown']
    }

    cmd = cmds.get(source).copy()

    # Append timeline arguments
    if source == 'news':
        months = args.news_months if args.news_months else DEFAULT_NEWS_MONTHS
        cmd.extend(['--months', str(months)])

    elif source == 'reddit':
        days = args.reddit_days if args.reddit_days else DEFAULT_REDDIT_DAYS
        cmd.extend(['--days', str(days)])

    elif source == 'tiktok':
        period = args.tiktok_period if args.tiktok_period else DEFAULT_TIKTOK_PERIOD
        cmd.extend(['--time-period', period])

    elif source == 'youtube':
        period = args.youtube_period if args.youtube_period else DEFAULT_YOUTUBE_PERIOD
        cmd.extend(['--time-period', period])

    return cmd

# ============================================================================
# EXECUTION
# ============================================================================

def run_source(source, ticker, args):
    """Run a single sentiment source and return its markdown output."""
    cmd = get_command(source, ticker, args)

    try:
        # Pass current environment to ensure API keys are available
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            env=os.environ.copy()
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        error_header = f"\n> **Error running {source}**\n"
        error_details = f"> Command: {' '.join(cmd)}\n> Error: {e.stderr}\n\n"
        print(f"Error running {source}: {e.stderr}", file=sys.stderr)
        return error_header + error_details
    except Exception as e:
        return f"\n> **Error running {source}**\n> {str(e)}\n\n"

def save_output(ticker, content):
    """Save aggregated sentiment output to file."""
    # Add parent directory to path for shared_utils
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from shared_utils import get_data_directory, ensure_directory_exists

    output_dir = os.path.join(get_data_directory(ticker), '..', 'analysis', ticker)
    ensure_directory_exists(output_dir)

    filename = os.path.join(output_dir, f"{ticker}_sentiment.md")

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✓ Saved sentiment analysis to: {filename}", file=sys.stderr)
        return filename
    except Exception as e:
        print(f"\n❌ Failed to save sentiment analysis: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="Sentiment Analysis - Master Script")

    # Required ticker argument
    parser.add_argument('ticker', help="Stock ticker symbol (e.g., AAPL, TSLA)")

    # Source selection
    source_group = parser.add_argument_group('source selection')
    source_group.add_argument('--all', action='store_true', help="Run all sentiment sources")
    source_group.add_argument('--news', action='store_true', help="Include news sources")
    source_group.add_argument('--reddit', action='store_true', help="Include Reddit")
    source_group.add_argument('--tiktok', action='store_true', help="Include TikTok")
    source_group.add_argument('--youtube', action='store_true', help="Include YouTube")

    # Timeline overrides
    timeline_group = parser.add_argument_group('timeline overrides')
    timeline_group.add_argument('--news-months', type=int,
                               help=f'News lookback in months (default: {DEFAULT_NEWS_MONTHS})')
    timeline_group.add_argument('--reddit-days', type=int,
                               help=f'Reddit lookback in days (default: {DEFAULT_REDDIT_DAYS})')
    timeline_group.add_argument('--tiktok-period',
                               choices=['yesterday', 'this-week', 'this-month', 'last-3-months', 'last-6-months', 'all_time'],
                               help=f'TikTok time period (default: {DEFAULT_TIKTOK_PERIOD})')
    timeline_group.add_argument('--youtube-period',
                               choices=['last_hour', 'today', 'this_week', 'this_month', 'this_year', 'all_time'],
                               help=f'YouTube time period (default: {DEFAULT_YOUTUBE_PERIOD})')

    # Output control
    parser.add_argument('--no-save', action='store_true',
                       help='Do not save to file (print to stdout only)')

    args = parser.parse_args()

    ticker = args.ticker.upper()

    # Determine which sources to run
    sources = []
    if args.all:
        sources = ['news', 'reddit', 'tiktok', 'youtube']
    else:
        if args.news:
            sources.append('news')
        if args.reddit:
            sources.append('reddit')
        if args.tiktok:
            sources.append('tiktok')
        if args.youtube:
            sources.append('youtube')

    if not sources:
        parser.print_help()
        print("\nError: Must specify at least one source (--all or --news/--reddit/--tiktok/--youtube)", file=sys.stderr)
        sys.exit(1)

    # Generate header
    now = datetime.datetime.now()

    lines = []
    lines.append(f"# {ticker} Sentiment Analysis")
    lines.append(f"**Generated:** {now.strftime('%A, %B %d, %Y at %H:%M')}")
    lines.append(f"**Sources:** {', '.join(sources)}")
    lines.append("---\n")

    # Run each source
    for source in sources:
        print(f"Fetching {source} data for {ticker}...", file=sys.stderr)
        output = run_source(source, ticker, args)
        lines.append(output)
        lines.append("\n---\n")

    # Combine all output
    full_output = "\n".join(lines)

    # Save to file or print to stdout
    if not args.no_save:
        save_output(ticker, full_output)

    # Always print to stdout for user to see
    print(full_output)

if __name__ == "__main__":
    main()

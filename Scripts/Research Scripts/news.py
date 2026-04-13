"""
News Data Wrapper Script
========================

Orchestrates news data collection from Perigon and FMP APIs.
Replaces AlphaVantage with FMP for better volume and reliability.

Usage:
    python news.py TICKER [--months N] [--markdown]

Example:
    python news.py IBM --months 3
"""

import os
import sys
import argparse
import subprocess
from datetime import datetime
from collections import Counter

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    get_date_range_months_back,
    load_json
)

# ============================================================================
# FORMATTED MARKDOWN GENERATION
# ============================================================================

def generate_news_markdown(ticker, perigon_data, fmp_data, from_date, to_date):
    """Generate human-readable formatted markdown combining both news sources"""

    perigon_stories = perigon_data.get('stories', [])
    fmp_articles = fmp_data.get('articles', [])

    # Calculate statistics
    perigon_total_media = sum(story.get('uniqueCount', 1) or 1 for story in perigon_stories)

    fmp_sources = set()
    for article in fmp_articles:
        source = article.get('publisher') or article.get('site')
        if source:
            fmp_sources.add(source)

    # ... (keep time distribution and sentiment logic)

    # Time distribution
    perigon_monthly = Counter()
    for story in perigon_stories:
        date_str = story.get('updatedAt', '')
        if date_str:
            month_key = date_str[:7]  # YYYY-MM
            perigon_monthly[month_key] += 1

    fmp_monthly = Counter()
    for article in fmp_articles:
        date_str = article.get('publishedDate', '')
        if date_str and len(date_str) >= 7:
            month_key = date_str[:7]  # YYYY-MM
            fmp_monthly[month_key] += 1

    # Sentiment stats - Perigon
    perigon_positive = sum(1 for s in perigon_stories if s.get('sentiment', {}).get('positive', 0) > s.get('sentiment', {}).get('negative', 0))
    perigon_negative = sum(1 for s in perigon_stories if s.get('sentiment', {}).get('negative', 0) > s.get('sentiment', {}).get('positive', 0))
    perigon_neutral = len(perigon_stories) - perigon_positive - perigon_negative

    perigon_avg_composite = []
    for s in perigon_stories:
        sent = s.get('sentiment', {})
        if sent:
            composite = sent.get('positive', 0) - sent.get('negative', 0)
            perigon_avg_composite.append(composite)
    perigon_avg = sum(perigon_avg_composite) / len(perigon_avg_composite) if perigon_avg_composite else 0

    # Build markdown
    md = []
    md.append(f"# {ticker} News Data")
    md.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    md.append(f"**Date Range:** {from_date} to {to_date}")
    md.append("")

    # Summary Statistics
    md.append("## Summary Statistics")
    md.append("")
    md.append("### Coverage")
    md.append(f"- **Perigon:** {len(perigon_stories)} stories (aggregated from {perigon_total_media} media items)")
    md.append(f"- **FMP:** {len(fmp_articles)} articles from {len(fmp_sources)} sources")
    md.append(f"- **Total:** {len(perigon_stories) + len(fmp_articles)} items")
    md.append("")

    # Time Distribution
    all_months = sorted(set(perigon_monthly.keys()) | set(fmp_monthly.keys()), reverse=True)
    if all_months:
        md.append("### Time Distribution")
        md.append("| Month | Perigon | FMP |")
        md.append("|-------|---------|-----|")
        for month in all_months:
            md.append(f"| {month} | {perigon_monthly.get(month, 0)} | {fmp_monthly.get(month, 0)} |")
        md.append("")

    # Sentiment Distribution
    md.append("### Sentiment Distribution")
    md.append("")
    md.append(f"**Perigon** (avg composite: {perigon_avg:+.3f})")
    md.append(f"- Positive-leaning: {perigon_positive} stories")
    md.append(f"- Neutral: {perigon_neutral} stories")
    md.append(f"- Negative-leaning: {perigon_negative} stories")
    md.append("")

    md.append("---")
    md.append("")

    # Perigon Stories
    md.append(f"## Perigon Stories ({len(perigon_stories)} stories)")
    md.append("")

    # Sort by date descending
    sorted_stories = sorted(perigon_stories, key=lambda x: x.get('updatedAt', ''), reverse=True)

    for story in sorted_stories:
        date_str = story.get('updatedAt', '')[:10] if story.get('updatedAt') else 'Unknown'
        title = story.get('name', 'Untitled')

        md.append(f"### {date_str} | {title}")

        # Source and URL
        source = story.get('source', 'Unknown')
        url = story.get('url', '')
        if source and source != "Unknown":
            md.append(f"**Source:** {source}")
        if url:
            md.append(f"**URL:** {url}")

        # Sentiment
        sentiment = story.get('sentiment', {})
        pos = sentiment.get('positive', 0)
        neg = sentiment.get('negative', 0)
        neu = sentiment.get('neutral', 0)
        composite = pos - neg
        md.append(f"**Sentiment:** {composite:+.2f} (pos: {pos:.2f}, neg: {neg:.2f}, neu: {neu:.2f})")
        md.append("")

        # Summary
        summary = story.get('summary', '')
        if summary:
            md.append(summary)
            md.append("")

        # Key Points
        key_points = story.get('keyPoints', [])
        if key_points:
            md.append("**Key Points:**")
            for point in key_points:
                md.append(f"- {point}")
            md.append("")

        md.append("---")
        md.append("")

    # FMP Articles
    md.append(f"## FMP Articles ({len(fmp_articles)} articles)")
    md.append("")

    # Sort by date descending
    sorted_articles = sorted(fmp_articles, key=lambda x: x.get('publishedDate', ''), reverse=True)

    for article in sorted_articles:
        date_str = article.get('publishedDate', '')
        formatted_date = date_str[:10] if date_str else 'Unknown'
        title = article.get('title', 'Untitled')

        md.append(f"### {formatted_date} | {title}")

        # Source and URL
        source = article.get('publisher') or article.get('site') or 'Unknown'
        url = article.get('url', '')
        md.append(f"**Source:** {source}")
        if url:
            md.append(f"**URL:** {url}")
        md.append("")

        # Snippet
        text = article.get('text', '')
        if text:
            md.append(text)
            md.append("")

        md.append("---")
        md.append("")

    # Return markdown string
    return '\n'.join(md)

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Orchestrate news data collection from Perigon and FMP"""
    parser = argparse.ArgumentParser(description="News Data Wrapper (Perigon + FMP)")
    parser.add_argument('target', type=str, help='Target company ticker')
    parser.add_argument('--months', type=int, default=3,
                       help='Number of months to look back (default: 3)')
    parser.add_argument('--markdown', action='store_true',
                       help='Output markdown to stdout (for master script aggregation)')

    args = parser.parse_args()

    ticker = args.target.upper()
    markdown_mode = args.markdown

    if not markdown_mode:
        print("\n" + "="*60)
        print("NEWS DATA COLLECTION (PERIGON + FMP)")
        print("="*60)
        print(f"Target Company: {ticker}")
        print("="*60 + "\n")

    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Call individual scripts
    perigon_script = os.path.join(script_dir, 'news_perigon.py')
    fmp_script = os.path.join(script_dir, 'news_fmp.py')

    # Build command arguments
    cmd_args = [ticker, '--months', str(args.months)]
    if markdown_mode:
        cmd_args.append('--markdown')

    # Run Perigon script
    try:
        subprocess.run([sys.executable, perigon_script] + cmd_args, check=True)
    except subprocess.CalledProcessError as e:
        if not markdown_mode:
            print(f"⚠️  Warning: Perigon script failed: {e}")

    # Run FMP script
    try:
        subprocess.run([sys.executable, fmp_script] + cmd_args, check=True)
    except subprocess.CalledProcessError as e:
        if not markdown_mode:
            print(f"⚠️  Warning: FMP script failed: {e}")

    # Get date range for metadata
    from_date, to_date = get_date_range_months_back(args.months)

    # Load the generated JSON files
    data_dir = get_data_directory(ticker)
    perigon_file = os.path.join(data_dir, f"{ticker}_news_perigon.json")
    fmp_file = os.path.join(data_dir, f"{ticker}_news_fmp.json")

    p_data = load_json(perigon_file) if os.path.exists(perigon_file) else {}
    f_data = load_json(fmp_file) if os.path.exists(fmp_file) else {}

    # Generate combined markdown
    markdown_output = generate_news_markdown(ticker, p_data, f_data, from_date, to_date)

    if markdown_mode:
        # Output to stdout for master script
        print(markdown_output)
    else:
        # Display summary to terminal
        print("\n" + "="*60)
        print(f"✓ News data fetched successfully for {ticker}")
        print(f"  - Perigon: {len(p_data.get('stories', []))} stories")
        print(f"  - FMP: {len(f_data.get('articles', []))} articles")
        print("="*60 + "\n")

if __name__ == "__main__":
    main()

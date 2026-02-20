"""
News Data Wrapper Script
========================

Orchestrates news data collection from Perigon and AlphaVantage APIs.

Usage:
    python news.py TICKER [--months N] [--markdown]

Example:
    python news.py IBM --months 3

Outputs (in data/tickers/{TICKER}/raw/ folder):
    - {TICKER}_news_perigon.json - Perigon Stories results
    - {TICKER}_news_alphavantage.json - AlphaVantage NEWS_SENTIMENT results
    - {TICKER}_news_formatted.md - Human-readable formatted markdown combining both sources

Prerequisites:
    - PERIGON_API_KEY environment variable must be set
    - ALPHAVANTAGE_API_KEY environment variable must be set
    - news_perigon.py and news_alphavantage.py must be in same directory

Notes:
    - Calls individual news scripts for modularity
    - Generates combined markdown output
    - Default 3-month lookback from current date
    - Supports --markdown flag for master script aggregation
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

def generate_news_markdown(ticker, perigon_data, alphavantage_data, from_date, to_date):
    """Generate human-readable formatted markdown combining both news sources"""

    perigon_stories = perigon_data.get('stories', [])
    av_articles = alphavantage_data.get('articles', [])

    # Calculate statistics
    perigon_sources = set()
    for story in perigon_stories:
        if story.get('first_article') and story['first_article'].get('source'):
            perigon_sources.add(story['first_article']['source'])

    av_sources = set()
    for article in av_articles:
        if article.get('source'):
            av_sources.add(article['source'])

    # Time distribution
    perigon_monthly = Counter()
    for story in perigon_stories:
        date_str = story.get('updatedAt', '')
        if date_str:
            month_key = date_str[:7]  # YYYY-MM
            perigon_monthly[month_key] += 1

    av_monthly = Counter()
    for article in av_articles:
        date_str = article.get('time_published', '')
        if date_str and len(date_str) >= 6:
            month_key = f"{date_str[:4]}-{date_str[4:6]}"  # YYYY-MM
            av_monthly[month_key] += 1

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

    # Sentiment stats - AlphaVantage
    av_scores = [float(a.get('overall_sentiment_score', 0)) for a in av_articles if a.get('overall_sentiment_score') is not None]
    av_avg = sum(av_scores) / len(av_scores) if av_scores else 0
    av_min = min(av_scores) if av_scores else 0
    av_max = max(av_scores) if av_scores else 0
    av_median = sorted(av_scores)[len(av_scores)//2] if av_scores else 0

    # Top topics from Perigon
    topic_counter = Counter()
    for story in perigon_stories:
        topics = story.get('topics', [])
        if topics:
            for topic in topics:
                # Topics can be either strings or dicts with 'name' field
                if isinstance(topic, dict):
                    topic_name = topic.get('name', '')
                else:
                    topic_name = str(topic)
                if topic_name:
                    topic_counter[topic_name] += 1
    top_topics = topic_counter.most_common(5)

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
    md.append(f"- **Perigon:** {len(perigon_stories)} stories from {len(perigon_sources)} sources")
    md.append(f"- **AlphaVantage:** {len(av_articles)} articles from {len(av_sources)} sources")
    md.append(f"- **Total:** {len(perigon_stories) + len(av_articles)} items")
    md.append("")

    # Time Distribution
    all_months = sorted(set(perigon_monthly.keys()) | set(av_monthly.keys()))
    if all_months:
        md.append("### Time Distribution")
        md.append("| Month | Perigon | AlphaVantage |")
        md.append("|-------|---------|--------------|")
        for month in all_months:
            md.append(f"| {month} | {perigon_monthly.get(month, 0)} | {av_monthly.get(month, 0)} |")
        md.append("")

    # Sentiment Distribution
    md.append("### Sentiment Distribution")
    md.append("")
    md.append(f"**Perigon** (avg composite: {perigon_avg:+.3f})")
    md.append(f"- Positive-leaning: {perigon_positive} stories")
    md.append(f"- Neutral: {perigon_neutral} stories")
    md.append(f"- Negative-leaning: {perigon_negative} stories")
    md.append("")
    md.append(f"**AlphaVantage** (avg: {av_avg:.4f})")
    md.append(f"- Range: {av_min:.4f} to {av_max:.4f}")
    md.append(f"- Median: {av_median:.4f}")
    md.append("")

    # Top Topics
    if top_topics:
        md.append("### Top Topics (Perigon)")
        for i, (topic, count) in enumerate(top_topics, 1):
            md.append(f"{i}. {topic} ({count})")
        md.append("")

    md.append("---")
    md.append("")

    # Perigon Stories
    md.append(f"## Perigon Stories ({len(perigon_stories)} stories)")
    md.append("")

    # Sort by date descending
    sorted_stories = sorted(perigon_stories, key=lambda x: x.get('updatedAt', ''), reverse=True)

    for story in sorted_stories[:30]:
        date_str = story.get('updatedAt', '')[:10] if story.get('updatedAt') else 'Unknown'
        title = story.get('name', 'Untitled')

        md.append(f"### {date_str} | {title}")

        # Source and URL
        first_article = story.get('first_article') or {}
        source = first_article.get('source', 'Unknown')
        url = first_article.get('url', '')
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

    # AlphaVantage Articles
    md.append(f"## AlphaVantage Articles ({len(av_articles)} articles)")
    md.append("")

    # Sort by date descending
    sorted_articles = sorted(av_articles, key=lambda x: x.get('time_published', ''), reverse=True)

    for article in sorted_articles[:30]:
        date_str = article.get('time_published', '')
        if date_str and len(date_str) >= 8:
            formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        else:
            formatted_date = 'Unknown'

        title = article.get('title', 'Untitled')

        md.append(f"### {formatted_date} | {title}")

        # Source and URL
        source = article.get('source', 'Unknown')
        url = article.get('url', '')
        md.append(f"**Source:** {source}")
        if url:
            md.append(f"**URL:** {url}")

        # Sentiment
        sentiment_score = article.get('overall_sentiment_score')
        if sentiment_score is not None:
            md.append(f"**Sentiment:** {float(sentiment_score):.4f}")
        md.append("")

        # Summary
        summary = article.get('summary', '')
        if summary:
            md.append(summary)
            md.append("")

        md.append("---")
        md.append("")

    # Return markdown string
    return '\n'.join(md)

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Orchestrate news data collection from Perigon and AlphaVantage

    Calls individual news scripts and generates combined markdown output.
    """
    parser = argparse.ArgumentParser(description="News Data Wrapper (Perigon + AlphaVantage)")
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
        print("NEWS DATA COLLECTION (PERIGON + ALPHAVANTAGE)")
        print("="*60)
        print(f"Target Company: {ticker}")
        print("="*60 + "\n")

    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Call individual scripts
    perigon_script = os.path.join(script_dir, 'news_perigon.py')
    av_script = os.path.join(script_dir, 'news_alphavantage.py')

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

    # Run AlphaVantage script
    try:
        subprocess.run([sys.executable, av_script] + cmd_args, check=True)
    except subprocess.CalledProcessError as e:
        if not markdown_mode:
            print(f"⚠️  Warning: AlphaVantage script failed: {e}")

    # Get date range for metadata
    from_date, to_date = get_date_range_months_back(args.months)

    # Load the generated JSON files
    data_dir = get_data_directory(ticker)
    perigon_file = os.path.join(data_dir, f"{ticker}_news_perigon.json")
    av_file = os.path.join(data_dir, f"{ticker}_news_alphavantage.json")

    p_data = load_json(perigon_file) if os.path.exists(perigon_file) else {}
    a_data = load_json(av_file) if os.path.exists(av_file) else {}

    # Generate combined markdown
    markdown_output = generate_news_markdown(ticker, p_data, a_data, from_date, to_date)

    if markdown_mode:
        # Output to stdout for master script
        print(markdown_output)
    else:
        # Display summary to terminal
        print("\n" + "="*60)
        print(f"✓ News data fetched successfully for {ticker}")
        print(f"  - Perigon: {len(p_data.get('stories', []))} stories")
        print(f"  - AlphaVantage: {len(a_data.get('articles', []))} articles")
        print("="*60 + "\n")

if __name__ == "__main__":
    main()

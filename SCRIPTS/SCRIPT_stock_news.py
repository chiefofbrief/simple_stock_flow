"""
News Data Preparation Script
=============================

Fetches news data from Perigon and AlphaVantage APIs for stock analysis workflow.

Usage:
    python SCRIPT_news.py TICKER

Example:
    python SCRIPT_news.py IBM

Outputs (in TICKER/ folder):
    - {TICKER}_news_perigon.json - Perigon Stories results (6-month lookback, top 30)
    - {TICKER}_news_alphavantage.json - AlphaVantage NEWS_SENTIMENT results (6-month lookback, top 30)
    - {TICKER}_news_formatted.md - Human-readable formatted markdown combining both sources with statistics

Output Structure:
    Each JSON file contains:
    - date_range: Start and end dates for the data
    - stories/articles: Full list of all items (raw data preserved)
    - last_30_days: Filtered list of items from last 30 days (for current sentiment analysis)
    - monthly_summary: Aggregated data by month with count and average sentiment

Prerequisites:
    - PERIGON_API_KEY environment variable must be set
    - ALPHAVANTAGE_API_KEY environment variable must be set
    - Target ticker folder will be created if it doesn't exist

Notes:
    - 6-month lookback from current date
    - Top 30 results from both Perigon and AlphaVantage (equal representation)
    - No cross-API deduplication (saved as separate files)
    - Perigon handles reprints internally via showReprints=False
    - Simplified output format for easier analysis
    - Pre-computed time-based aggregations for analyst convenience
"""

import requests
import os
import sys
import argparse
from datetime import datetime, timedelta
from collections import defaultdict
from shared_utils import (
    make_request_with_retry,
    get_data_directory,
    ensure_directory_exists,
    get_date_range_months_back,
    save_json,
    REQUEST_TIMEOUT
)

# ============================================================================
# TIME-BASED FILTERING & AGGREGATION
# ============================================================================

def filter_last_30_days(items, date_field, date_format='iso'):
    """Filter items to only those from last 30 days

    Args:
        items: List of items to filter
        date_field: Name of the date field in each item
        date_format: 'iso' for ISO format (Perigon) or 'av' for AlphaVantage format

    Returns:
        List of items from last 30 days
    """
    cutoff_date = datetime.now() - timedelta(days=30)
    filtered = []

    for item in items:
        date_str = item.get(date_field)
        if not date_str:
            continue

        try:
            if date_format == 'iso':
                # Perigon: "2025-12-20T12:06:30.666272+00:00"
                item_date = datetime.fromisoformat(date_str.replace('+00:00', ''))
            else:
                # AlphaVantage: "20251227T133319"
                item_date = datetime.strptime(date_str, "%Y%m%dT%H%M%S")

            if item_date >= cutoff_date:
                filtered.append(item)
        except (ValueError, AttributeError):
            continue

    return filtered

def group_by_month(items, date_field, date_format='iso', sentiment_field=None):
    """Group items by month with optional sentiment aggregation

    Args:
        items: List of items to group
        date_field: Name of the date field in each item
        date_format: 'iso' for ISO format or 'av' for AlphaVantage format
        sentiment_field: Optional field name for sentiment score

    Returns:
        Dict with month keys (YYYY-MM) and aggregated data
    """
    monthly = defaultdict(lambda: {'count': 0, 'items': [], 'sentiment_scores': []})

    for item in items:
        date_str = item.get(date_field)
        if not date_str:
            continue

        try:
            if date_format == 'iso':
                month_key = date_str[:7]  # "2025-12"
            else:
                month_key = f"{date_str[:4]}-{date_str[4:6]}"  # "2025-12"

            monthly[month_key]['count'] += 1
            monthly[month_key]['items'].append(item)

            # Add sentiment if field specified
            if sentiment_field:
                sentiment = item.get(sentiment_field)
                if sentiment is not None:
                    if isinstance(sentiment, dict):
                        # Perigon sentiment is a dict with positive/negative/neutral
                        # Convert to single score: positive - negative
                        score = sentiment.get('positive', 0) - sentiment.get('negative', 0)
                        monthly[month_key]['sentiment_scores'].append(score)
                    else:
                        # AlphaVantage sentiment is already a single number
                        monthly[month_key]['sentiment_scores'].append(float(sentiment))
        except (ValueError, AttributeError, KeyError):
            continue

    # Calculate average sentiment for each month
    result = {}
    for month, data in sorted(monthly.items()):
        avg_sentiment = None
        if data['sentiment_scores']:
            avg_sentiment = sum(data['sentiment_scores']) / len(data['sentiment_scores'])

        result[month] = {
            'count': data['count'],
            'avg_sentiment': round(avg_sentiment, 3) if avg_sentiment is not None else None
        }

    return result

# ============================================================================
# PERIGON API
# ============================================================================

def fetch_perigon_stories(ticker, api_key, from_date, to_date):
    """Fetch news stories from Perigon API

    Args:
        ticker: Stock ticker symbol
        api_key: Perigon API key
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)

    Returns:
        dict: API response
    """
    print(f"\nFetching Perigon stories for {ticker}...")
    print(f"  Date range: {from_date} to {to_date}")

    params = {
        'apiKey': api_key,
        'companySymbol': ticker,
        'sortBy': 'updatedAt',
        'size': 30,
        'showReprints': False,
        'from': from_date,
        'to': to_date
    }

    return make_request_with_retry(
        lambda: requests.get(
            "https://api.goperigon.com/v1/stories/all",
            params=params,
            timeout=REQUEST_TIMEOUT
        )
    )

def simplify_perigon_story(story):
    """Extract simplified fields from Perigon story

    Args:
        story: Full story object from Perigon API

    Returns:
        dict: Simplified story with essential fields
    """
    # Extract first article details
    articles = story.get('articles', [])
    first_article = articles[0] if articles else {}

    # Extract key points (limit to top 3)
    key_points = story.get('keyPoints', [])
    simplified_key_points = [kp.get('point') for kp in key_points[:3] if kp.get('point')]

    return {
        'clusterId': story.get('clusterId'),
        'name': story.get('name'),
        'summary': story.get('summary'),
        'keyPoints': simplified_key_points,
        'companies': [
            {
                'name': c.get('name'),
                'symbols': c.get('symbols', [])
            }
            for c in story.get('companies', [])[:5]
        ],
        'people': [
            {
                'name': p.get('name')
            }
            for p in story.get('people', [])[:5]
        ],
        'topics': [t for t in story.get('topics', [])[:5]],
        'sentiment': story.get('sentiment', {}),
        'createdAt': story.get('createdAt'),
        'updatedAt': story.get('updatedAt'),
        'uniqueCount': story.get('uniqueCount'),
        'first_article': {
            'source': first_article.get('source', {}).get('name'),
            'url': first_article.get('url')
        } if first_article else None
    }

# ============================================================================
# ALPHAVANTAGE API
# ============================================================================

def fetch_alphavantage_news(ticker, api_key, from_date, to_date):
    """Fetch news sentiment from AlphaVantage API

    Args:
        ticker: Stock ticker symbol
        api_key: AlphaVantage API key
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)

    Returns:
        dict: API response
    """
    print(f"\nFetching AlphaVantage NEWS_SENTIMENT for {ticker}...")
    print(f"  Date range: {from_date} to {to_date}")

    # Convert date format to YYYYMMDDTHHMM
    from_datetime = datetime.strptime(from_date, "%Y-%m-%d")
    time_from = from_datetime.strftime("%Y%m%dT%H%M")

    params = {
        'function': 'NEWS_SENTIMENT',
        'tickers': ticker,
        'sort': 'LATEST',
        'limit': 30,
        'time_from': time_from,
        'apikey': api_key
    }

    # Build URL manually for AlphaVantage
    url = 'https://www.alphavantage.co/query'

    return make_request_with_retry(
        lambda: requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    )

def simplify_alphavantage_article(article):
    """Extract simplified fields from AlphaVantage article

    Args:
        article: Full article object from AlphaVantage API

    Returns:
        dict: Simplified article with essential fields
    """
    return {
        'title': article.get('title'),
        'summary': article.get('summary'),
        'url': article.get('url'),
        'time_published': article.get('time_published'),
        'source': article.get('source'),
        'overall_sentiment_score': article.get('overall_sentiment_score'),
        'ticker_sentiment': article.get('ticker_sentiment', [])[:5]  # Top 5 tickers
    }

# ============================================================================
# FILE SAVING
# ============================================================================

def save_perigon_data(data, ticker, from_date, to_date):
    """Save Perigon data to JSON file

    Args:
        data: API response data
        ticker: Stock ticker symbol
        from_date: Start date for metadata
        to_date: End date for metadata

    Returns:
        str: Filename of saved file, or None if failed
    """
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

    # Check for errors
    if 'error' in data:
        print(f"⚠️  Warning: Perigon API error: {data['error']}")
        return None

    # Extract stories and simplify
    stories = data.get('results', [])
    simplified_stories = [simplify_perigon_story(story) for story in stories]

    # Build output structure with aggregations
    last_30_days = filter_last_30_days(simplified_stories, 'updatedAt', 'iso')
    monthly_summary = group_by_month(simplified_stories, 'updatedAt', 'iso', 'sentiment')

    output = {
        'date_range': {
            'from': from_date,
            'to': to_date
        },
        'stories': simplified_stories,
        'last_30_days': last_30_days,
        'monthly_summary': monthly_summary
    }

    filename = os.path.join(data_dir, f"{ticker}_news_perigon.json")

    if save_json(output, filename):
        print(f"✓ Saved Perigon data: {filename}")
        print(f"  - {len(simplified_stories)} total stories")
        print(f"  - {len(last_30_days)} stories in last 30 days")
        print(f"  - {len(monthly_summary)} months of data")
        return filename
    else:
        return None

def save_alphavantage_data(data, ticker, from_date, to_date):
    """Save AlphaVantage data to JSON file

    Args:
        data: API response data
        ticker: Stock ticker symbol
        from_date: Start date for metadata
        to_date: End date for metadata

    Returns:
        str: Filename of saved file, or None if failed
    """
    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

    # Check for errors
    if 'error' in data:
        print(f"⚠️  Warning: AlphaVantage API error: {data['error']}")
        return None

    if 'Error Message' in data:
        print(f"⚠️  Warning: AlphaVantage API error: {data['Error Message']}")
        return None

    if 'Note' in data:
        print(f"⚠️  Warning: AlphaVantage rate limit: {data['Note']}")
        return None

    # Extract articles and simplify (truncate to 30 for equal representation with Perigon)
    articles = data.get('feed', [])[:30]
    simplified_articles = [simplify_alphavantage_article(article) for article in articles]

    # Build output structure with aggregations
    last_30_days = filter_last_30_days(simplified_articles, 'time_published', 'av')
    monthly_summary = group_by_month(simplified_articles, 'time_published', 'av', 'overall_sentiment_score')

    output = {
        'date_range': {
            'from': from_date,
            'to': to_date
        },
        'articles': simplified_articles,
        'last_30_days': last_30_days,
        'monthly_summary': monthly_summary
    }

    filename = os.path.join(data_dir, f"{ticker}_news_alphavantage.json")

    if save_json(output, filename):
        print(f"✓ Saved AlphaVantage data: {filename}")
        print(f"  - {len(simplified_articles)} total articles")
        print(f"  - {len(last_30_days)} articles in last 30 days")
        print(f"  - {len(monthly_summary)} months of data")
        return filename
    else:
        return None

# ============================================================================
# FORMATTED MARKDOWN GENERATION
# ============================================================================

def generate_formatted_markdown(ticker, perigon_data, alphavantage_data, from_date, to_date):
    """Generate human-readable formatted markdown combining both news sources

    Args:
        ticker: Stock ticker symbol
        perigon_data: Processed Perigon data dict (with 'stories' key)
        alphavantage_data: Processed AlphaVantage data dict (with 'articles' key)
        from_date: Start date for metadata
        to_date: End date for metadata

    Returns:
        str: Filename of saved markdown file, or None if failed
    """
    from datetime import datetime
    from collections import Counter

    data_dir = get_data_directory(ticker)
    ensure_directory_exists(data_dir)

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

    for story in sorted_stories:
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

    for article in sorted_articles:
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

    # Save file
    filename = os.path.join(data_dir, f"{ticker}_news_formatted.md")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md))
        print(f"✓ Saved formatted markdown: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Failed to save formatted markdown: {e}")
        return None

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Fetch and save news data from Perigon and AlphaVantage APIs

    Requires PERIGON_API_KEY and ALPHAVANTAGE_API_KEY environment variables.
    Outputs JSON files to {TICKER}/ directory with 6-month news data.
    """
    parser = argparse.ArgumentParser(description="News Data Preparation Tool")
    parser.add_argument('target', type=str, help='Target company ticker')

    args = parser.parse_args()

    ticker = args.target.upper()

    # Get API keys from environment
    perigon_key = os.getenv('PERIGON_API_KEY')
    alphavantage_key = os.getenv('ALPHAVANTAGE_API_KEY')

    if not perigon_key:
        print("Error: PERIGON_API_KEY environment variable not set")
        sys.exit(1)

    if not alphavantage_key:
        print("Error: ALPHAVANTAGE_API_KEY environment variable not set")
        sys.exit(1)

    print("\n" + "="*60)
    print("NEWS DATA PREPARATION")
    print("="*60)
    print(f"Target Company: {ticker}")
    print("="*60 + "\n")

    # Get date range (6 months back)
    from_date, to_date = get_date_range_months_back(6)
    print(f"Date range: {from_date} to {to_date} (~6 months)")

    # Fetch from both APIs
    perigon_data = fetch_perigon_stories(ticker, perigon_key, from_date, to_date)
    alphavantage_data = fetch_alphavantage_news(ticker, alphavantage_key, from_date, to_date)

    # Process and save data
    perigon_file = save_perigon_data(perigon_data, ticker, from_date, to_date)
    av_file = save_alphavantage_data(alphavantage_data, ticker, from_date, to_date)

    # Count results
    perigon_count = len(perigon_data.get('results', [])) if 'error' not in perigon_data else 0
    av_count = len(alphavantage_data.get('feed', [])) if 'error' not in alphavantage_data else 0

    # Generate formatted markdown (only if at least one source succeeded)
    formatted_file = None
    if perigon_file or av_file:
        # Build processed data structures for markdown
        perigon_processed = {}
        if perigon_file:
            stories = perigon_data.get('results', [])
            perigon_processed = {
                'stories': [simplify_perigon_story(story) for story in stories]
            }

        av_processed = {}
        if av_file:
            articles = alphavantage_data.get('feed', [])[:30]
            av_processed = {
                'articles': [simplify_alphavantage_article(article) for article in articles]
            }

        formatted_file = generate_formatted_markdown(ticker, perigon_processed, av_processed, from_date, to_date)

    # Summary
    print("\n" + "="*60)
    print("PROCESSING COMPLETE")
    print("="*60)

    success = False
    if perigon_file:
        print(f"\n✓ Perigon: {perigon_count} stories fetched")
        success = True
    else:
        print(f"\n❌ Perigon: Failed to fetch data")

    if av_file:
        print(f"✓ AlphaVantage: {av_count} articles fetched")
        success = True
    else:
        print(f"❌ AlphaVantage: Failed to fetch data")

    if not success:
        print("\n❌ No news data was successfully fetched")
        print("This may indicate:")
        print("  - API rate limits exceeded")
        print("  - Invalid API keys")
        print("  - Ticker symbol is invalid")
        print("  - Network connectivity issues")
        sys.exit(1)

    print(f"\nOutput files saved to: {ticker}/")
    if perigon_file:
        print(f"  ├── {ticker}_news_perigon.json")
    if av_file:
        print(f"  ├── {ticker}_news_alphavantage.json")
    if formatted_file:
        print(f"  ├── {ticker}_news_formatted.md")
    print()


if __name__ == "__main__":
    main()

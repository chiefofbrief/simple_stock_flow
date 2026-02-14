#!/usr/bin/env python3
"""
AI Infrastructure News Fetcher (via Perigon Stories API)
========================================================

Fetches AI infrastructure news stories using Perigon's Stories endpoint,
which clusters related articles into single events with AI-generated summaries.

Focus: compute, chips, memory, foundry, data centers — the infrastructure
layers where current market opportunity is concentrated.

Installation:
    pip install requests python-dateutil rich

Configuration:
    export PERIGON_API_KEY="your_api_key_here"

Usage:
    python scripts/market/ai_news.py                    # Default: past 1 day, up to 30 stories
    python scripts/market/ai_news.py --markdown          # Output raw markdown (for digest pipeline)
    python scripts/market/ai_news.py --days 7            # Past 7 days
    python scripts/market/ai_news.py --count 30          # Cap at 30 stories

API Cost:
    - 1 Perigon query per run (Stories endpoint)
    - Combined with 1 Barron's query = 2 total daily Perigon calls
    - Budget: 2/day * 30 = 60/month (within 150/month free tier)

Requirements:
    - Python 3.7+
    - requests, python-dateutil, rich
    - Valid Perigon API key
"""

import os
import sys
import time
import argparse
from datetime import datetime, timedelta
from dateutil import parser as date_parser
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

try:
    import requests
except ImportError:
    print("Error: requests not installed. Please run: pip install requests python-dateutil rich")
    sys.exit(1)

# ============================================================================
# CONSTANTS
# ============================================================================

PERIGON_BASE_URL = "https://api.goperigon.com/v1"
REQUEST_TIMEOUT = 30
DEFAULT_COUNT = 30
DEFAULT_DAYS_BACK = 1
MAX_RETRIES = 3
RETRY_DELAY = 5

# Boolean query: AI infrastructure layers (compute, chips, memory, foundry, data centers)
BOOLEAN_QUERY = (
    '("data center" OR "semiconductor" OR "chipmaker" '
    'OR "HBM" OR "high bandwidth memory" OR "DRAM" OR "NAND" '
    'OR "foundry" OR "wafer" OR "lithography" '
    'OR "GPU" OR "graphics processing unit" '
    'OR "TPU" OR "tensor processing unit" '
    'OR "ASIC" OR "custom silicon" '
    'OR "Blackwell" OR "H100")'
)

# ============================================================================
# API FUNCTIONS
# ============================================================================

def _retry_request(request_fn, label="request"):
    """Execute a request function with retry logic and exponential backoff."""
    for attempt in range(MAX_RETRIES):
        try:
            response = request_fn()

            if response.status_code == 503:
                if attempt < MAX_RETRIES - 1:
                    delay = RETRY_DELAY * (2 ** attempt)
                    print(f"  Rate limit hit on {label} (attempt {attempt + 1}/{MAX_RETRIES})")
                    print(f"  Waiting {delay}s before retry...")
                    time.sleep(delay)
                    continue
                else:
                    raise Exception(f"API rate limit exceeded on {label} after {MAX_RETRIES} retries.")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise Exception("Authentication failed. Please check your PERIGON_API_KEY.")
            elif response.status_code == 403:
                raise Exception("Access forbidden. Your API key may not have access to this endpoint.")
            elif response.status_code == 503:
                continue
            else:
                raise Exception(f"API request failed with status {response.status_code}: {str(e)}")
        except requests.exceptions.Timeout:
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAY * (2 ** attempt)
                print(f"  Timeout on {label} (attempt {attempt + 1}/{MAX_RETRIES})")
                print(f"  Retrying in {delay}s...")
                time.sleep(delay)
                continue
            raise Exception(f"API request timed out on {label} after multiple retries.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed on {label}: {str(e)}")

    raise Exception(f"API request failed on {label} after {MAX_RETRIES} retries.")


def fetch_stories(api_key, days_back=DEFAULT_DAYS_BACK, count=DEFAULT_COUNT):
    """Fetch AI infrastructure stories from Perigon Stories endpoint."""
    end_time = datetime.now()
    start_time = end_time - timedelta(days=days_back)

    params = {
        "apiKey": api_key,
        "q": BOOLEAN_QUERY,
        "excludeLabel": "Opinion,Paid News",
        "showReprints": "false",
        "sortBy": "updatedAt",
        "from": start_time.strftime("%Y-%m-%d"),
        "to": end_time.strftime("%Y-%m-%d"),
        "size": count,
        "showNumResults": "true",
    }

    def do_request():
        return requests.get(
            f"{PERIGON_BASE_URL}/stories/all",
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

    return _retry_request(do_request, label="Stories search")


# ============================================================================
# FORMATTING
# ============================================================================

def format_date(date_str):
    """Format an ISO date string into a readable format."""
    try:
        dt = date_parser.parse(date_str)
        return dt.strftime('%B %d, %Y at %I:%M %p')
    except Exception:
        return date_str


def _story_topics(story):
    """Extract topic names from a story dict."""
    topics = story.get("topTopics", [])
    return ", ".join(t.get("name", "") for t in topics if t.get("name"))


def _story_companies(story):
    """Extract company names from a story dict."""
    companies = story.get("companies", [])[:5]
    return ", ".join(c.get("name", "") for c in companies if c.get("name"))


def print_markdown(stories_data, count, days_back):
    """Print stories output in markdown format."""
    day_text = "day" if days_back == 1 else f"{days_back} days"
    stories = stories_data.get("results", [])[:count]
    total = stories_data.get("numResults", len(stories))

    print(f"## AI Infrastructure News (Perigon Stories)")
    print(f"_Showing {len(stories)} of {total} stories from past {day_text}_\n")

    if not stories:
        print("_No stories found._\n")
        return

    for i, s in enumerate(stories, 1):
        name = s.get("name", "Unnamed Story")
        summary = (s.get("shortSummary") or s.get("summary") or "").strip()
        updated = s.get("updatedAt", "")
        unique = s.get("uniqueCount", 0)
        total_articles = s.get("totalCount", 0)
        topics = _story_topics(s)
        companies = _story_companies(s)

        print(f"### {i}. {name}")
        if updated:
            print(f"_{format_date(updated)}_")

        meta_parts = [f"**Articles:** {unique} unique / {total_articles} total"]
        if topics:
            meta_parts.append(f"**Topics:** {topics}")
        if companies:
            meta_parts.append(f"**Companies:** {companies}")
        print(f"{' | '.join(meta_parts)}")

        if summary:
            print(f"\n{summary}")

        # Key points
        key_points = s.get("keyPoints", [])
        if key_points:
            print("\n**Key Points:**")
            for kp in key_points[:4]:
                point = kp.get("point", "")
                if point:
                    print(f"- {point}")

        print("\n---\n")


def display_rich(stories_data, count, days_back, console):
    """Display stories output using rich terminal formatting."""
    day_text = "day" if days_back == 1 else f"{days_back} days"
    stories = stories_data.get("results", [])[:count]
    total = stories_data.get("numResults", len(stories))

    console.print("\n")
    header_text = Text("AI Infrastructure News (Perigon Stories)", style="bold white", justify="center")
    console.print(Panel(header_text, border_style="blue", padding=(1, 2)))
    console.print(f"[dim]Showing {len(stories)} of {total} stories from past {day_text}[/dim]", justify="center")
    console.print("\n" + "=" * console.width + "\n")

    if not stories:
        console.print("[dim]No stories found.[/dim]\n")
        return

    for i, s in enumerate(stories, 1):
        name = s.get("name", "Unnamed Story")
        summary = (s.get("shortSummary") or s.get("summary") or "").strip()
        updated = s.get("updatedAt", "")
        unique = s.get("uniqueCount", 0)
        total_articles = s.get("totalCount", 0)
        topics = _story_topics(s)
        companies = _story_companies(s)

        console.print(Text(f"{i}. {name}", style="bold cyan"))
        if updated:
            console.print(f"[dim]{format_date(updated)}[/dim]")

        meta = [f"[dim]Articles: {unique}/{total_articles}[/dim]"]
        if topics:
            meta.append(f"[dim]Topics: {topics}[/dim]")
        if companies:
            meta.append(f"[dim]Companies: {companies}[/dim]")
        console.print(" | ".join(meta))

        if summary:
            console.print()
            console.print(summary)

        key_points = s.get("keyPoints", [])
        if key_points:
            console.print("\n[bold]Key Points:[/bold]")
            for kp in key_points[:4]:
                point = kp.get("point", "")
                if point:
                    console.print(f"  - {point}")

        if i < len(stories):
            console.print("\n" + "-" * console.width + "\n")

    console.print("\n" + "=" * console.width + "\n")
    console.print()


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Fetch AI infrastructure news via Perigon Stories endpoint"
    )
    parser.add_argument(
        "--count", type=int, default=DEFAULT_COUNT,
        help=f"Maximum number of stories to return (default: {DEFAULT_COUNT})"
    )
    parser.add_argument(
        "--days", type=int, default=DEFAULT_DAYS_BACK,
        help=f"Number of days back to search (default: {DEFAULT_DAYS_BACK})"
    )
    parser.add_argument(
        "--markdown", action="store_true",
        help="Output raw markdown without terminal formatting (for digest pipeline)"
    )
    args = parser.parse_args()

    console = Console()

    api_key = os.environ.get("PERIGON_API_KEY")
    if not api_key:
        if not args.markdown:
            console.print("[red]Error: PERIGON_API_KEY environment variable not set[/red]")
            console.print("\n[yellow]Please set your API key:[/yellow]")
            console.print("  export PERIGON_API_KEY='your_api_key_here'")
            console.print("\n[dim]Get an API key at: https://www.goperigon.com/[/dim]")
        else:
            print("Error: PERIGON_API_KEY environment variable not set")
        return 1

    try:
        day_text = "day" if args.days == 1 else f"{args.days} days"
        if not args.markdown:
            console.print(f"[cyan]Fetching AI infrastructure stories from past {day_text}...[/cyan]")

        stories_data = fetch_stories(api_key, days_back=args.days, count=args.count)

        if args.markdown:
            print_markdown(stories_data, args.count, args.days)
        else:
            n_stories = len(stories_data.get("results", []))
            console.print(f"\n[green]Found {n_stories} stories (1 API query used)[/green]")
            display_rich(stories_data, args.count, args.days, console)

        return 0

    except KeyboardInterrupt:
        if not args.markdown:
            console.print("\n[yellow]Interrupted by user[/yellow]")
        return 1
    except Exception as e:
        if not args.markdown:
            console.print(f"\n[red]Error: {str(e)}[/red]")
            console.print("[yellow]If you encountered an API error, please check your API key and try again.[/yellow]")
        else:
            print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

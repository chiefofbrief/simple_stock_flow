#!/usr/bin/env python3
"""
Tech & Industry News Aggregator
=================================

Runs all tech feed scripts and outputs a combined ## Tech & Industry section.

Sources:
  - TrendForce (via Perigon)
  - Data Center Dynamics (via RSS)
  - SiliconAngle (via RSS)
  - The Robot Report (via RSS)
  - Power Magazine (via RSS)
  - Fierce Network (via Kill the Newsletter)

Usage:
    python "new scripts for digest/tech_feeds.py"

Required environment variables:
    PERIGON_API_KEY  (for TrendForce only)
"""

import sys
import os
import subprocess

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCES = [
    'trendforce',
    'dcd',
    'siliconangle',
    'robotreport',
    'powermag',
    'fierce',
]


def run_source(name):
    cmd = [sys.executable, os.path.join(SCRIPTS_DIR, f'{name}.py')]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            env=os.environ.copy()
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running {name}: {e.stderr}", file=sys.stderr)
        return f"### {name.title()}\n\n_Error fetching content._"
    except Exception as e:
        return f"### {name.title()}\n\n_Error: {str(e)}_"


def main():
    print("## Tech & Industry")

    for source in SOURCES:
        out = run_source(source)
        if out:
            print()
            print(out)
            print()


if __name__ == "__main__":
    main()

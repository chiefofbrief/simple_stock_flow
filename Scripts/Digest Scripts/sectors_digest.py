#!/usr/bin/env python3
"""
Sectors Market Digest
=====================

Orchestrates sector-specific market analysis scripts and aggregates their Markdown output.
Sources are listed flat — categorization is handled by the analysis prompt, not the script.

Usage:
    python Scripts/sectors_digest.py
"""

import sys
import subprocess
import datetime
import os

# ============================================================================
# CONFIGURATION - SOURCES (flat, category-agnostic)
# ============================================================================

SOURCES = [
    {'name': 'SemiAnalysis',         'url': 'https://semianalysis.com/',                    'cmd': [sys.executable, 'Scripts/Digest Scripts/semianalysis.py', '--markdown']},
    {'name': 'TrendForce',           'url': 'https://www.trendforce.com/news/',              'cmd': [sys.executable, 'Scripts/Digest Scripts/trendforce.py', '--markdown']},
    {'name': 'ServeTheHome',         'url': 'https://www.servethehome.com/',                 'cmd': [sys.executable, 'Scripts/Digest Scripts/servethehome.py', '--markdown']},
    {'name': 'Data Center Knowledge','url': 'https://www.datacenterknowledge.com/',          'cmd': [sys.executable, 'Scripts/Digest Scripts/datacenterknowledge.py', '--markdown']},
    {'name': 'Data Center Dynamics', 'url': 'https://www.datacenterdynamics.com/en/',        'cmd': [sys.executable, 'Scripts/Digest Scripts/datacenterdynamics.py', '--markdown']},
    {'name': 'Fierce Network',       'url': 'https://www.fierce-network.com/',               'cmd': [sys.executable, 'Scripts/Digest Scripts/fierce.py', '--markdown']},
    {'name': 'Power Mag',            'url': 'https://www.powermag.com/',                     'cmd': [sys.executable, 'Scripts/Digest Scripts/powermag.py', '--markdown']},
    {'name': 'Benchmark Minerals',   'url': 'https://www.benchmarkminerals.com/',            'cmd': [sys.executable, 'Scripts/Digest Scripts/benchmark.py', '--markdown']},
    {'name': 'SpaceNews',            'url': 'https://spacenews.com/',                        'cmd': [sys.executable, 'Scripts/Digest Scripts/spacenews.py', '--markdown']},
]

def run_module(module_name, cmd):
    """Run a single module and return its output."""
    try:
        # Pass current environment to ensure API keys are available
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True,
            env=os.environ.copy()
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"\n> **Error running {module_name}**\n> {e.stderr}\n\n"
    except Exception as e:
        return f"\n> **Error running {module_name}**\n> {str(e)}\n\n"

def main():
    now = datetime.datetime.now()
    # Calculate yesterday's date
    yesterday = now - datetime.timedelta(days=1)
    target_date_str = yesterday.strftime("%Y-%m-%d")
    
    output_content = []
    
    output_content.append(f"# Peter's Digest: Sectors")
    output_content.append(f"**Generated:** {now.strftime('%A, %B %d, %Y')}")
    output_content.append(f"**Timeframe:** {yesterday.strftime('%A, %B %d, %Y')}")
    output_content.append("---\n")

    # Source checklist with clickable URLs
    source_links = " | ".join(f"[{src['name']}]({src['url']})" for src in SOURCES)
    output_content.append(f"**Sources:** {source_links}\n")
    output_content.append("---\n")

    # Run all sources (flat, no grouping)
    for src in SOURCES:
        cmd = src['cmd'] + ['--date', target_date_str]
        output = run_module(src['name'], cmd)
        if output:
            output_content.append(output)
            output_content.append("\n---\n")

    full_report = "\n".join(output_content)

    # Save to File
    date_str = now.strftime("%Y-%m-%d")
    filename = f"Sectors_Digest_{date_str}.md"
    output_dir = "Peter's Digest/Sectors Digest"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, "w") as f:
        f.write(full_report)
        
    print(f"Sectors Digest generated and saved to: {output_path}")

if __name__ == "__main__":
    main()

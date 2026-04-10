#!/usr/bin/env python3
"""
Sectors Market Digest
=====================

Orchestrates sector-specific market analysis scripts and aggregates their Markdown output.
Groups sources by industry (Compute, Infrastructure, Energy, Materials, Frontier).

Usage:
    python Scripts/sectors_digest.py
"""

import sys
import subprocess
import datetime
import os

# ============================================================================
# CONFIGURATION - GROUPED BY INDUSTRY
# ============================================================================

GROUPS = {
    "1. AI — Compute & Chips": [
        {'name': 'SemiAnalysis', 'cmd': [sys.executable, 'Scripts/Digest Scripts/semianalysis.py', '--markdown']},
        {'name': 'TrendForce (Semi)', 'cmd': [sys.executable, 'Scripts/Digest Scripts/trendforce.py', '--markdown']},
        {'name': 'ServeTheHome', 'cmd': [sys.executable, 'Scripts/Digest Scripts/servethehome.py', '--markdown']}
    ],
    "2. AI — Infrastructure & Cloud": [
        {'name': 'Data Center Knowledge', 'cmd': [sys.executable, 'Scripts/Digest Scripts/datacenterknowledge.py', '--markdown']},
        {'name': 'Data Center Dynamics', 'cmd': [sys.executable, 'Scripts/Digest Scripts/datacenterdynamics.py', '--markdown']},
        {'name': 'Fierce Network', 'cmd': [sys.executable, 'Scripts/Digest Scripts/fierce.py', '--markdown']}
    ],
    "3. AI — Nuclear & Energy": [
        {'name': 'Power Mag', 'cmd': [sys.executable, 'Scripts/Digest Scripts/powermag.py', '--markdown']},
        # Note: TrendForce (Energy) is already covered by the trendforce.py script in Group 1
        # but the script aggregates both, so we list it where it fits best.
    ],
    "4. Critical Minerals & Materials": [
        {'name': 'Benchmark Minerals', 'cmd': [sys.executable, 'Scripts/Digest Scripts/benchmark.py', '--markdown']}
    ],
    "5. Frontier Industries (Space & Defense)": [
        {'name': 'SpaceNews', 'cmd': [sys.executable, 'Scripts/Digest Scripts/spacenews.py', '--markdown']}
    ]
}

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

    # Run Groups in Order
    for group_title, modules in GROUPS.items():
        group_output = []
        for mod in modules:
            # Inject the --date flag into the command
            cmd = mod['cmd'] + ['--date', target_date_str]
            output = run_module(mod['name'], cmd)
            if output:
                group_output.append(output)
        
        if group_output:
            output_content.append(f"# {group_title}")
            output_content.append("\n\n".join(group_output))
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

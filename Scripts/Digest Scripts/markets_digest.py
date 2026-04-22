#!/usr/bin/env python3
"""
Markets Market Digest
=====================

Runs a collection of market analysis scripts and aggregates their Markdown output.
Focuses on Daily discovery of [LOSER] and [TAILWIND] candidates.

Usage:
    python Scripts/markets_digest.py
"""

import argparse
import sys
import subprocess
import datetime
import os

# ============================================================================
# CONFIGURATION - ORDERED BY SECTION
# ============================================================================

SECTION_MACRO = ['macro', 'intrigue']
SECTION_STOCKS = ['movers', 'barrons', 'reddit']

def get_command(module, target_date=None):
    """Get the specific command list for a module."""
    
    # Base commands
    cmds = {
        'macro':    [sys.executable, 'Scripts/Digest Scripts/macro.py', '--markdown'],
        'intrigue': [sys.executable, 'Scripts/Digest Scripts/intrigue.py'],
        'movers':   [sys.executable, 'Scripts/Digest Scripts/movers.py', '--markdown'],
        'barrons':  [sys.executable, 'Scripts/Digest Scripts/barrons.py'],
        'reddit':   [sys.executable, 'Scripts/Digest Scripts/reddit.py']
    }
    
    cmd = cmds.get(module).copy()
    
    # Append specific arguments
    if module == 'barrons':
        if target_date:
            cmd.extend(['--date', target_date])
        cmd.extend(['--count', '40'])
        
    elif module == 'intrigue':
        if target_date:
            cmd.extend(['--date', target_date])

    elif module == 'reddit':
        cmd.extend(['--timeframe', 'day'])

    return cmd

def run_module(module, target_date=None):
    """Run a single module and return its output."""
    cmd = get_command(module, target_date)
    
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
        error_header = f"\n> **Error running {module}**\n"
        error_details = f"> Error: {e.stderr}\n\n"
        print(f"Error running {module}: {e.stderr}", file=sys.stderr)
        return error_header + error_details
    except Exception as e:
        return f"\n> **Error running {module}**\n> {str(e)}\n\n"

def main():
    parser = argparse.ArgumentParser(description="Markets Market Digest - Generator")
    
    # Individual Overrides (Superset for filtering)
    ALL_MODULES = SECTION_MACRO + SECTION_STOCKS
    for mod in ALL_MODULES:
        parser.add_argument(f'--{mod}', action='store_true')

    args = parser.parse_args()
    
    # Determine which modules to run
    active_macro = []
    active_stocks = []
    
    # Check if any individual flags are set
    any_flags = any(getattr(args, mod) for mod in ALL_MODULES)
    
    if not any_flags:
        # Default: Run everything
        active_macro = SECTION_MACRO
        active_stocks = SECTION_STOCKS
    else:
        # Run only the flagged modules
        active_macro = [m for m in SECTION_MACRO if getattr(args, m)]
        active_stocks = [m for m in SECTION_STOCKS if getattr(args, m)]

    # Generate Output Content
    output_content = []
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    target_date_str = yesterday.strftime("%Y-%m-%d")
    
    output_content.append(f"# Peter's Digest: Markets")
    output_content.append(f"**Generated:** {now.strftime('%A, %B %d, %Y')}")
    output_content.append(f"**Timeframe:** {yesterday.strftime('%A, %B %d, %Y')}")
    output_content.append("---\n")

    # 1. MACRO SECTION
    if active_macro:
        macro_outputs = []
        for mod in active_macro:
            out = run_module(mod, target_date_str)
            if out: macro_outputs.append(out)
        
        if macro_outputs:
            output_content.append("# MACRO")
            output_content.append("\n\n---\n\n".join(macro_outputs))
            output_content.append("\n---\n")

    # 2. STOCKS SECTION
    if active_stocks:
        stocks_outputs = []
        for mod in active_stocks:
            out = run_module(mod, target_date_str)
            if out: stocks_outputs.append(out)
        
        if stocks_outputs:
            output_content.append("# STOCKS")
            output_content.append("\n\n---\n\n".join(stocks_outputs))
            output_content.append("\n---\n")

    full_report = "\n".join(output_content)

    # Save to File
    date_str = now.strftime("%Y-%m-%d")
    filename = f"Markets_Digest_{date_str}.md"
    output_dir = "Peter's Digest/Markets Digest"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, "w") as f:
        f.write(full_report)
        
    print(f"Digest generated and saved to: {output_path}")

if __name__ == "__main__":
    main()

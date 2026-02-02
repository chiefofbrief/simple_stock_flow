#!/usr/bin/env python3
"""
Market Discovery Master Script
==============================

Runs a collection of market analysis scripts and aggregates their Markdown output.
Supports both Daily and Weekly digest modes.

Usage:
    python scripts/discovery.py --daily        # Standard Daily Digest (Movers, News, Reddit)
    python scripts/discovery.py --weekly       # Weekly Digest (Macro + 7-day lookback)
    python scripts/discovery.py --barrons      # Run individual modules... 

Output:
    Prints combined Markdown to stdout. Redirect to a file to save.
    Example: python scripts/discovery.py --daily > "data/discovery/Digest_$(date +%F).md"
"""

import argparse
import sys
import subprocess
import datetime
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

# Order of execution for Daily Digest
DAILY_ORDER = ['movers', 'barrons', 'wsj', 'intrigue', 'reddit']

# Order of execution for Weekly Digest (Macro comes first)
WEEKLY_ORDER = ['macro', 'movers', 'barrons', 'wsj', 'intrigue', 'reddit']

def get_command(module, mode='daily'):
    """Get the specific command list for a module based on the mode."""
    
    # Base commands
    cmds = {
        'movers':   ['python', 'scripts/market/movers.py', '--markdown'],
        'intrigue': ['python', 'scripts/market/intrigue.py', '--markdown'],
        'macro':    ['python', 'scripts/market/macro.py', '--markdown'],
        
        # Modules with variable timeframes
        'barrons':  ['python', 'scripts/market/barrons.py', '--markdown'],
        'wsj':      ['python', 'scripts/market/wsj.py', '--markdown'],
        'reddit':   ['python', 'scripts/market/reddit.py', '--markdown']
    }
    
    cmd = cmds.get(module).copy()
    
    # Append specific arguments based on mode
    if module == 'barrons' or module == 'wsj':
        days = '7' if mode == 'weekly' else '1'
        cmd.extend(['--days', days])
        
    elif module == 'reddit':
        timeframe = 'week' if mode == 'weekly' else 'day'
        cmd.extend(['--timeframe', timeframe])
        
    return cmd

# ============================================================================
# EXECUTION
# ============================================================================

def run_module(module, mode):
    """Run a single module and return its output."""
    cmd = get_command(module, mode)
    
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
        error_header = f"\n> **Error running {module}**\n"
        error_details = f"> Command: {' '.join(cmd)}\n> Error: {e.stderr}\n\n"
        print(f"Error running {module}: {e.stderr}", file=sys.stderr)
        return error_header + error_details
    except Exception as e:
        return f"\n> **Error running {module}**\n> {str(e)}\n\n"

def main():
    parser = argparse.ArgumentParser(description="Market Discovery - Digest Generator")
    
    # Modes
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--daily', action='store_true', help="Run Daily Digest (1-day lookback)")
    mode_group.add_argument('--weekly', action='store_true', help="Run Weekly Digest (Macro + 7-day lookback)")
    
    # Individual Overrides
    parser.add_argument('--movers', action='store_true', help="Run Movers")
    parser.add_argument('--macro', action='store_true', help="Run Macro")
    parser.add_argument('--barrons', action='store_true', help="Run Barron's")
    parser.add_argument('--wsj', action='store_true', help="Run WSJ")
    parser.add_argument('--intrigue', action='store_true', help="Run Intrigue")
    parser.add_argument('--reddit', action='store_true', help="Run Reddit")

    args = parser.parse_args()
    
    # Determine Execution Plan
    execution_list = []
    mode = 'daily' # Default for individual flags
    
    if args.weekly:
        mode = 'weekly'
        execution_list = WEEKLY_ORDER
    elif args.daily:
        mode = 'daily'
        execution_list = DAILY_ORDER
    else:
        # Handle individual flags
        # Use WEEKLY_ORDER as the superset for sorting purposes
        potential_modules = WEEKLY_ORDER
        for mod in potential_modules:
            if getattr(args, mod):
                execution_list.append(mod)
        
        if not execution_list:
            parser.print_help()
            sys.exit(1)

    # Generate Header
    now = datetime.datetime.now()
    title = "Weekly Market Digest" if mode == 'weekly' else "Daily Market Digest"
    if not args.weekly and not args.daily:
        title = "Market Discovery Report"

    print(f"# {title}")
    print(f"**Generated:** {now.strftime('%A, %B %d, %Y')}")
    print("---\n")

    # Run Modules
    for module in execution_list:
        output = run_module(module, mode)
        print(output)
        print("\n")

if __name__ == "__main__":
    main()

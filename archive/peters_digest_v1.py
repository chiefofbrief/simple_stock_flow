#!/usr/bin/env python3
"""
Peter's Market Digest
=====================

Runs a collection of market analysis scripts and aggregates their Markdown output.
Supports both Daily and Weekly digest modes.

Usage:
    python scripts/peters_digest.py --daily        # Peter's Daily Digest (AI News, Movers, Reddit)
    python scripts/peters_digest.py --weekly       # Weekly Digest (Macro + 7-day lookback)
    python scripts/peters_digest.py --barrons      # Run individual modules... 

Output:
    Prints combined Markdown to stdout. Redirect to a file to save.
    Example: python scripts/peters_digest.py --daily > "data/discovery/Digest_$(date +%F).md"
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
# Prioritizing Movers -> Barron's -> Reddit -> AI News -> Intrigue
DAILY_ORDER = ['movers', 'barrons', 'reddit', 'ai_news', 'intrigue']

# Order of execution for Weekly Digest (Macro comes first)
WEEKLY_ORDER = ['macro', 'ai_news', 'movers', 'barrons', 'intrigue', 'reddit']

def get_command(module, mode='daily'):
    """Get the specific command list for a module based on the mode."""
    
    # Base commands
    cmds = {
        'movers':   [sys.executable, 'Scripts/Digest Scripts/movers.py', '--markdown'],
        'intrigue': [sys.executable, 'Scripts/Digest Scripts/intrigue.py', '--markdown'],
        'macro':    [sys.executable, 'Scripts/Digest Scripts/macro.py', '--markdown'],
        
        # Modules with variable timeframes
        'barrons':  [sys.executable, 'Scripts/Digest Scripts/barrons.py', '--markdown'],
        'ai_news':  [sys.executable, 'Scripts/Digest Scripts/ai_news.py', '--markdown'],
        'reddit':   [sys.executable, 'Scripts/Digest Scripts/reddit.py', '--markdown']
    }
    
    cmd = cmds.get(module).copy()
    
    # Append specific arguments based on mode
    if module == 'barrons' or module == 'ai_news':
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
        error_details = f"> Command: {' '.join(cmd)}\n> Error: {e.stderr}\n> Output: {e.stdout}\n\n"
        print(f"Error running {module}: {e.stderr}", file=sys.stderr)
        return error_header + error_details
    except Exception as e:
        return f"\n> **Error running {module}**\n> {str(e)}\n\n"

def main():
    parser = argparse.ArgumentParser(description="Peter's Market Digest - Generator")
    
    # Modes
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--daily', action='store_true', help="Run Daily Digest (1-day lookback)")
    mode_group.add_argument('--weekly', action='store_true', help="Run Weekly Digest (Macro + 7-day lookback)")
    
    # Individual Overrides
    parser.add_argument('--movers', action='store_true', help="Run Movers")
    parser.add_argument('--macro', action='store_true', help="Run Macro")
    parser.add_argument('--barrons', action='store_true', help="Run Barron's")
    parser.add_argument('--ai-news', action='store_true', dest='ai_news', help="Run AI News")
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

    # Generate Output Content
    output_content = []
    
    now = datetime.datetime.now()
    title = "Peter's Digest: Markets (Weekly)" if mode == 'weekly' else "Peter's Digest: Markets"
    
    # Simple check if neither flag was set (and list matches neither default)
    is_custom = (not args.weekly and not args.daily and 
                 execution_list != DAILY_ORDER and execution_list != WEEKLY_ORDER)
    
    if is_custom:
         title = "Market Discovery Report"

    output_content.append(f"# {title}")
    output_content.append(f"**Generated:** {now.strftime('%A, %B %d, %Y')}")
    output_content.append("---\n")

    # Run Modules
    for i, module in enumerate(execution_list):
        if i > 0:
            output_content.append("\n---\n")
        
        output = run_module(module, mode)
        output_content.append(output)

    full_report = "\n".join(output_content)

    # Save to File
    date_str = now.strftime("%Y-%m-%d")
    file_prefix = "Markets_Digest_Weekly" if mode == 'weekly' else "Markets_Digest"
    if is_custom:
        file_prefix = "Custom_Digest"
        
    filename = f"{file_prefix}_{date_str}.md"
    
    # Save to Peter's Digest
    # We assume script is run from project root, so relative path is safe
    output_dir = "Peter's Digest/Markets Digest"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, "w") as f:
        f.write(full_report)
        
    print(f"Digest generated and saved to: {output_path}")


if __name__ == "__main__":
    main()

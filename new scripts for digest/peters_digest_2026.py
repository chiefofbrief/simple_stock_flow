#!/usr/bin/env python3
"""
Peter's Digest 2026
===================

Orchestrator for the updated digest pipeline.

Sections:
  - Macro (FMP live data)
  - International Intrigue (most recent post)
  - Barron's (50 most recent, via Perigon)
  - Wall Street Journal (50 most recent, via Perigon)

No date filter — always fetches the most recent content.

Usage:
    python "new scripts for digest/peters_digest_2026.py"

Required environment variables:
    FMP_API_KEY
    PERIGON_API_KEY
"""

import sys
import subprocess
import datetime
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

MODULES = ['macro', 'intrigue', 'barrons', 'wsj', 'tech_feeds']

OUTPUT_DIR = "data/digest"


def get_command(module):
    cmds = {
        'macro':       [sys.executable, os.path.join(SCRIPTS_DIR, 'macro.py'), '--markdown'],
        'intrigue':    [sys.executable, os.path.join(SCRIPTS_DIR, 'intrigue.py')],
        'barrons':     [sys.executable, os.path.join(SCRIPTS_DIR, 'barrons.py')],
        'wsj':         [sys.executable, os.path.join(SCRIPTS_DIR, 'wsj.py')],
        'tech_feeds':  [sys.executable, os.path.join(SCRIPTS_DIR, 'tech_feeds.py')],
    }
    return cmds[module].copy()


def run_module(module):
    cmd = get_command(module)
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
        print(f"Error running {module}: {e.stderr}", file=sys.stderr)
        return f"\n> **Error running {module}**\n> {e.stderr}\n"
    except Exception as e:
        return f"\n> **Error running {module}**\n> {str(e)}\n"


def main():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")

    output_content = []
    output_content.append(f"# Peter's Digest")
    output_content.append(f"**Generated:** {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
    output_content.append("---\n")

    for module in MODULES:
        out = run_module(module)
        if out:
            output_content.append(out)
            output_content.append("\n---\n")

    full_report = "\n".join(output_content)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = f"Peters_Digest_{date_str}.md"
    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, "w") as f:
        f.write(full_report)

    print(f"Digest generated and saved to: {output_path}")


if __name__ == "__main__":
    main()

## Orchestrator Instructions

This prompt is executed by launching one background agent per ticker. Each agent receives this entire prompt with {TICKER} substituted. The orchestrator's only job is to launch the agents and relay their Synthesis outputs when complete. No other decisions are required.

---

## Agent Task

Execute these prompts sequentially for {TICKER}. Read only the first prompt now, then the second after finishing the first, and the third after finishing the second. These are sequential, not parallel. These exact prompts must be used.

1. /workspaces/simple_stock_flow/Prompts/prompt_the_context_software.md
2. /workspaces/simple_stock_flow/Prompts/prompt_the_numbers_software.md
3. /workspaces/simple_stock_flow/Prompts/prompt_the_projection_software.md

---

## Agent Operating Rules

These rules override any conflicting instructions in the individual prompt files above.

### Autonomy & Gates
- Run all three passes without stopping for approval between them.
- The only legitimate stop points are: (1) a required data file is missing or clearly corrupted, or (2) a significant analysis approach question that cannot be resolved from the available files.
- Do not present intermediate outputs or hypotheses in chat. Present only the final Synthesis section when all three passes are complete.

### Output & File Integrity
- Do NOT update the Stock Tracker under any circumstances.
- Never edit any permanent files — scripts, prompts, CLAUDE.md, GEMINI.md, index files, or context files. Your writes are restricted to the thesis file and ticker data files only.
- Write to the thesis file after each pass. Use Write to create the thesis file if it does not exist; use Edit for all subsequent sections.

### Tools
- Use the Grep tool for all search operations. Never use Bash.
- Use Read (with offset/limit) to inspect specific sections of large files. Never read a full MD&A or notes file.

### Context Compaction
- If your context compacts at any point, re-read all files relevant to the current pass before continuing. Do not proceed from memory alone after compaction.

---

## Acknowledgements

Before starting, confirm you agree to the following:

1. You have thoroughly read the first prompt, and you will read each prompt thoroughly at the appropriate time. You will not read all files upfront.

2. You will write to the thesis file after each pass, not once at the end.

3. If context compaction occurs, you will re-read all relevant files before continuing.

4. If any data is missing or seems outdated/incorrect, you will flag it loudly.
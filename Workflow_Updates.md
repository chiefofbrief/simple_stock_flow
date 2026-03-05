

## Workflow Updates (Version 0.6)

- **[COMPLETED] Discovery Phase Overhaul:** Completely restructured `prompt_digest.md` and `prompt_discovery.md` to use the sequential "Active Workflow" pattern (Read -> Analyze -> Ask -> Write). Replaced "Analysis Guidelines" with "Deliverable Requirements" to prevent confusion with `GEMINI.md`. Implemented a two-phase Gap Analysis in the Discovery prompt to force processing of the Digest first, followed by explicit solicitation of user ad-hoc input before finalization.
- **[COMPLETED] Tailwind Tagging Integration:** Removed explicit tagging definitions from the Discovery prompts and instructed them to reference the core investment types (`[LOSER]`, `[TAILWIND]`) directly from `GEMINI.md`.
- **[COMPLETED] Tracker Instructions Enforcement:** Updated `prompt_discovery.md` to explicitly enforce the "Tracker Update Instructions" when modifying `Stock_Tracker.md`.
- **[COMPLETED] Tracker Formatting:** Updated `Stock_Tracker.md` to include daily discovery entries, maintaining alphabetical sorting for PENDING items and ensuring tag updates are correctly applied.
- **[COMPLETED] Remove the thesis section from individual analysis prompts.**
- **[COMPLETED] Gemini.md context issue:** Renamed `Gemini.md` to `GEMINI.md` to trigger automatic loading into context at startup. Updated all internal references in `Index.md` and prompts. Added `GEMINI.md` as required context for all Phase 2 analysis prompts.
- **[COMPLETED] Discovery Step (prompt_discovery.md):** The system should explicitly ask the user for any additional input (tickers, notes, excerpts from the chat window) before finalizing the step. Currently, it processes the Digest and moves on without prompting for user contributions. **Fix:** Added an explicit instruction to `prompt_discovery.md` to solicit additional input as a textual question before the final proposal.
- **[COMPLETED] Tool Access / Gitignore Bug:** The `read_file` tool is being blocked from reading `Data/screening/Price_Data_*.txt` due to `.gitignore` rules. Even after adding an exception (`!data/screening/Price_Data_*.txt`), the tool still considers the file ignored. This requires investigation to determine if it's a case-sensitivity issue (`Data/` vs `data/`) or an aggressive caching mechanism within the tool. **Fix:** Simplified `.gitignore` to use `Data/` (uppercase) exclusively and ignore all `**/raw/` and `**/__pycache__/` directories. This ensures all screening/thesis files are tracked automatically without complex exclusion rules.
- **[COMPLETED] Screening Phase Decision Gates:** The system must pause after generating the Price/Earnings summaries to explicitly propose which tickers should be marked as `PASS` vs `FILTERED`, and require user approval before writing to `Stock_Tracker.md`. Currently, the prompt lacks explicit instructions to stop and ask the user for this decision. **Fix:** Updated `prompt_price.md` and `prompt_earnings.md` to include a "Status Update" section and a mandatory "Instructions for the Assistant" decision gate requiring human approval before updating the Stock Tracker.
- **[COMPLETED] Retaining Screening Q&A:** Currently, the Price and Earnings prompts only instruct the system to copy the final *summary paragraph* to `Stock_Tracker.md` and the detailed Q&A is discarded (per the "no per-ticker files in Phase 1" rule). We should update the workflow to append the full detailed Q&A back into the generated `.txt` files in `Data/screening/` so that the intermediate analytical work isn't lost. **Fix:** Updated `prompt_price.md` and `prompt_earnings.md` to explicitly require appending the full analysis report (Q&A + Summary) to the source data files in `Data/screening/` after approval.
- **[COMPLETED] Financials Prompt Depth:** The answers to the first set of questions (not the overall questions) in the Financials analysis were too succinct and may be missing insights. `prompt_financials.md` needs to be updated to require more detailed and insightful responses for those sections. **Fix:** Updated `prompt_financials.md` Analysis Guidelines to require insightful "why" answers for metrics.
- **[COMPLETED] Deep Dive Decision Gates:** The system should provide its pass/fail recommendation at the end of each Deep Dive step (e.g., after Financials) and require explicit user approval before proceeding to the next step. Note: The final step (Earnings Calls) does not require a pass/fail recommendation, it simply concludes the analysis. **Fix:** Updated all Deep Dive prompts (`financials`, `sentiment`, `footnotes`, `earnings_calls`) to include a "Thesis Synthesis & Recommendation" section and a mandatory "Instructions for the Assistant" decision gate requiring human approval before writing to files.
- **[COMPLETED] Deep Dive Prep Prompt:** Create a 'deep dive prep' prompt to handle moving the Price and Earnings screening summaries over to the Thesis file prior to running the Financials analysis. This will allow the `prompt_financials.md` prompt to focus exclusively on analysis and writing its specific section without having to manage the initial file seeding. **Fix:** Created `Prompts/prompt_deep_dive_prep.md` to initialize the `{TICKER}_Thesis.md` file and seed it with screening context. Updated `GEMINI.md` workflow.
- **[COMPLETED] Footnotes Extraction Bug:** The `Scripts/footnotes.py` script incorrectly extracted the "Risk Factors" section instead of the "Notes to Financial Statements" for the 10-Q, and pulled the Auditor's Report for the 10-K. The regex/extraction logic in this script needs to be refined and tested to ensure it reliably captures the actual financial footnotes. **Fix:** Implemented "Note 1 proximity logic" in `Scripts/footnotes.py` for the Notes section (searching for the match immediately followed by "NOTE 1"). Added "REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM" as a 10-K end marker to prevent bleeding into audit certificates. Verified correct extraction for ADBE 10-K and 10-Q.
- **[COMPLETED] Handling Massive Transcripts (Context Limits):** The output from `Scripts/earnings_calls.py` was so large that the file reader had to truncate it. To prevent missing crucial information at the end of calls (often where the most revealing Q&A happens), we should either update the script to chunk the transcript, extract the Q&A separately from prepared remarks, or use a pre-summarization step. **Fix:** Updated `Scripts/earnings_calls.py` to output two separate markdown files: `{TICKER}_earnings_remarks.md` and `{TICKER}_earnings_qa.md`. Updated `prompt_earnings_calls.md` to require both files. This ensures high-signal Q&A data is never truncated.
- **[COMPLETED] Thesis File Template:** Manually appending text to `ADBE_Thesis.md` led to formatting hiccups and duplicate blocks. Creating a structured `thesis_template.md` with explicit placeholders (e.g., `{{FINANCIALS_ANALYSIS}}`) would make file generation cleaner, whether done by a script or the system, and prevent data overwrite/duplication errors. **Fix:** Addressed by the creation of `prompt_deep_dive_prep.md`, which initializes a structured Thesis file with headers, and the subsequent update of analysis prompts to target those specific sections.
- **[COMPLETED] Missing Data:** The only file I see in `Data/screening/` in the remote repo is `Price_Data_2026-02-25.txt`. Nothing for earnings. Any idea why? I also don’t see the price or earnings analyses anywhere? **Fix:** Confirmed `Earnings_2026-02-25.txt` exists locally but was being filtered by the old `.gitignore` logic. Standardizing `.gitignore` to `Data/` (uppercase) fixed the visibility. Future analyses will be preserved in these files due to prompt updates.
- **[COMPLETED] Financial Analysis (ADBE Specific):**
    - Operating Leverage: Seems to be strange values, possibly incorrect.
    - CapEx ($B): Why are these values negative?
    - Let’s review all our calculated metrics/ratios to make sure the calculations are correct.
    - Recent Quarterly Trends: Table is a mess.
    **Fix:** Audited all ratio calculations in `Scripts/financials.py` and confirmed mathematical correctness. Updated script to fix the broken markdown table separator in the quarterly section, display CapEx as a positive expenditure (using `abs()`), and suppress the meaningless "Δ%" calculation for the Operating Leverage ratio. Verified fixes with ADBE.
- **[COMPLETED]** Increase News Reach: Replaced AlphaVantage with FMP Search Stock News API to eliminate rate limit bottlenecks. Implemented a "Distributed Chunking" strategy to guarantee 3-month coverage:
    - **FMP:** Script executes 3 separate API calls (one per month) to force the return of historical data for high-volume stocks.
    - **Perigon:** Script executes 1 large API call (size=100) and uses a local algorithm to distribute stories evenly across the 3-month timeline (10 stories per month).
- **[COMPLETED]** Source Counting: Fixed "0 sources" bug in `news.py`. Since Perigon "Stories" are AI-clustered aggregations, switched the metric to `uniqueCount` (total media items aggregated in the cluster) and updated markdown to hide "Source" lines for Unknown origins.
- **[COMPLETED]** Video Engagement: Implement a 5,000 view minimum threshold and include post dates in `tiktok.py` and `youtube.py` markdown output.
- **[COMPLETED]** Master Date: Standardize "Generated" date formatting in `sentiment.py`.
- **[COMPLETED]** Reddit Search: Transitioning from "Subreddit Scrape" (which missed low-volume tickers) to "Keyword Search". Implemented dynamic FMP company name lookup to enhance search comprehensiveness across Reddit, TikTok, and YouTube.
- **[COMPLETED] Prompt Restructure (prompt_price.md):** Redesigned the prompt with an "Active Workflow" section at the top to enforce sequential execution (Read -> Analyze -> Ask -> Write). Consolidated "Analysis Guidelines" and "Output Format" into a single section to reduce instruction fragmentation and ensure data-citation rules are followed within the required template.
- **[COMPLETED] Tracker Reorganization & Reset:** Streamlined `Stock_Tracker.md` into three functional sections (Deep Dive, Screening, Filtered Archive) and implemented a "Ticker Dashboard" sorted by workflow progress. Added "Tracker Update Instructions" to standardize how the assistant updates the log, dashboard, and summaries. Reset all ticker data (except HIMS) to prepare for a fresh screening run.
- **[COMPLETED] Price Prompt Examples & GEMINI.md Integration:** Added 10 high-signal analysis examples to `prompt_price.md` to distinguish between "Temporary" and "Permanent" losers. Integrated a mandatory step to read `GEMINI.md` at the start of the workflow to ensure foundational analysis philosophy (e.g., Margin of Safety) is applied before data analysis. Updated Price summaries to be more descriptive and metric-heavy.

## Workflow Update (Version 0.5 - 02-23-2026)

We finished version 0.5 of the workflow on 02-23-2026. Changes mades included: 
* Workflow V1 Setup: Created WORKFLOW v1 directory structure.
* Script Migration: Moved peters_digest.py, price.py, earnings.py, shared_utils.py and all digest scripts to WORKFLOW v1/Scripts/.
* Path Updates: Updated peters_digest.py to point to the new location of digest scripts and save output to WORKFLOW v1/Peter's Digest/. Updated docs/COMMANDS.md.
* Prompt Creation: Created WORKFLOW v1/Prompts/price_analysis_prompt.md.
* Execution: Ran Peter's Digest for today.
* Analysis: Generated and prepended the market analysis to the daily digest file.
* Git Sync: Pushed all changes to the remote repository.
* Stock Tracker Update: Added "Earnings/Valuation Analysis" section to WORKFLOW v1/Stock Tracker.md.
* Earnings Prompt: Created WORKFLOW v1/Prompts/earnings_analysis_prompt.md with specific analysis questions and data inputs.
* Financials Script: Created WORKFLOW v1/Scripts/financials.py to fetch FMP data (Annual & Quarterly), calculate Earnings Risk, Quality, and ROI metrics, and generate detailed markdown reports with statistical analysis (CAGR, CV, Deltas).
* Script Validation: Verified financials.py accuracy against AAPL SEC filings and confirmed manual TTM calculation logic.
* Tracker Enhancements: Added "Earnings Risk", "Earnings Quality", and "ROI" subsections to WORKFLOW v1/Stock Tracker.md.
* Script Update (Quarterly Data): Enhanced financials.py to output "Recent Quarterly Trends" (last 4 quarters + deltas) alongside the annual data tables.
* Script Testing: Verified the enhanced financials.py output with AAPL.
* Metrics Prompts: Created WORKFLOW v1/Prompts/earnings_risk_prompt.md, earnings_quality_prompt.md, and roi_prompt.md with interchangeable roles and specific metrics.
* Prompt Consolidation: Consolidated earnings_risk, earnings_quality, and roi prompts into a single WORKFLOW v1/Prompts/prompt_financials.md, updated with a refined metrics list and embedded guidance.
* Prompt Renaming: Renamed all analysis prompts to follow the prompt_.md convention (prompt_price.md, prompt_earnings.md, prompt_financials.md).
* Financials Script Update: Updated WORKFLOW v1/Scripts/financials.py to match the new prompt_financials.md structure (flattened JSON, single table output, updated metrics). Verified with AAPL.
* Sentiment Prompt Creation: Created WORKFLOW v1/Prompts/prompt_sentiment.md for analyzing news and social media sentiment.
* Sentiment Script Migration: Migrated scripts/sentiment.py and dependencies (news.py, reddit.py, etc.) to WORKFLOW v1/Scripts/ and WORKFLOW v1/Scripts/Sentiment Scripts/.
* Sentiment Script Optimization: Fixed a bug in the YouTube script and lowered Reddit engagement thresholds (10 upvotes, 0 comments) to capture more data. Verified with AAPL.
* Archive Cleanup: Archived old sentiment scripts to archive/scripts/ with _old suffixes to prevent confusion.
* Sentiment Lookback Update: Updated WORKFLOW v1/Scripts/Sentiment Scripts/reddit.py and WORKFLOW v1/Scripts/sentiment.py to use a 90-day (3-month) lookback period by default.
* Footnotes Prompt Creation: Created WORKFLOW v1/Prompts/prompt_footnotes.md for analyzing MD&A and footnotes, ensuring consistency with other analysis prompts.
* SEC Filings Script Migration: Migrated sec_filings.py to WORKFLOW v1/Scripts/ and updated it to use the new shared_utils location.
* SEC Filings Script Optimization: Enhanced sec_filings.py with robust extraction logic (whitespace normalization, flexible regex) to correctly handle 10-Q Notes sections, fixing a failure on AAPL. Verified successful extraction for both AAPL and AMZN.
* Earnings Call Prompt Creation: Created WORKFLOW v1/Prompts/prompt_earnings_calls.md for analyzing earnings call transcripts, focusing on management tone shifts and alignment with previous financial/sentiment analyses.
* Earnings Call Script Implementation: Developed WORKFLOW v1/Scripts/earnings_calls.py to fetch the two most recent quarterly transcripts via AlphaVantage, processing them into a consolidated markdown file with clear "Prepared Remarks" and "Q&A" sections for LLM analysis.
* Earnings Call Script Testing: Verified earnings_calls.py functionality with IBM and AMZN, confirming correct quarter detection (2025Q4/2025Q3), file generation, and markdown structure.
* Documentation Consolidation: Refined Gemini.md to explicitly define the workflow rules and analysis philosophy, replacing redundant guideline docs.
* Sector Guidance: Created AI_Guidelines.md to provide an ecosystem framework for AI-tagged tickers.
* Stock Tracker Creation: Built Stock_Tracker.md as the unified dashboard, migrating active tickers and tagging them with [LOSER] or [AI] tags.
* Discovery Context: Migrated hypotheses from legacy session notes and excerpts into a new Discovery_Context.md file to ground future analyses.
* Discovery Prompt: Created prompt_digest.md to synthesize market news and daily digests into actionable investment flags.
* Naming & Organization: Standardized markdown files to Title_Case.md and renamed sec_filings.py to footnotes.py for consistency.
* Context Linking: Updated all screening and deep dive prompts to correctly reference Discovery_Context.md, AI_Guidelines.md, and the Stock Tracker tags.
* Legacy Archival: Archived all outdated v0 data, docs, guidance, and script folders.
* V1 Unpacking: Extracted the contents of WORKFLOW v1 into the project root and updated all internal paths across prompts and scripts.
* Directory Structure: Capitalized `data/` to `Data/` across all scripts (`shared_utils.py`, `price.py`, `earnings.py`) and documentation to ensure consistency.
* Discovery Prompt: Created `Prompts/prompt_discovery.md` to bridge Peter's Digest/User Input with the Stock Tracker, incorporating auto-add logic and context generation.
* Prompt Updates: Updated all 6 analysis prompts (`price`, `earnings`, `financials`, `sentiment`, `footnotes`, `earnings_calls`) to reference `Data/`, `Stock_Tracker.md`, and the simplified `_Thesis.md` filename.
* Documentation Update: Updated `Index.md` and `Gemini.md` to include the new Discovery step and correct paths.
* Archive Protection: Added `archive/` to `.gitignore` to prevent accidental LLM/script interaction with legacy files.
* Workspace Initialization: Created the `Data/` directory structure (`Data/screening/`, `Data/tickers/`).
* Tools Section: Added "Options APIs" (MarketData, Alpaca, Tradier) to Session Notes.
* Prompt Standardization: Unified roles to "Expert Financial Analyst" and standardized `Context Configuration` headers across updated prompts (`digest`, `discovery`, `price`, `earnings`).
* Digest Prompt: Renamed "Applied Investment Flags" to "General Stock News Analysis", reordered flow (Macro -> General -> AI -> Candidates), removed "Deep Dives", and clarified output location.
* Discovery Prompt: Added explicit workflow for "Context Synchronization" (appending to `Discovery_Context.md`) and "Gap Analysis" (handling duplicates vs. updates). Refined "Context Quality Guidance" integration.
* Price Prompt: Updated to support batch tickers, corrected data inputs to point to script output/text files, and added `Stock_Tracker.md` as required context for Tag checking.
* Earnings Prompt: Updated to support batch tickers, flattened input metrics list, and aligned `[LOSER]` guidance with Price prompt.
* Workflow Alignment: Updated the `Gemini.md` workflow table to include the `-1. Digest` step and fixed the "Reads" column dependencies across steps to accurately reflect prompt instructions.
* Path Corrections: Fixed case-sensitivity issues in all 6 prompt files (changing `scripts/` to `Scripts/` in run commands) to ensure Linux compatibility.
* Script Output Routing: Updated `Scripts/peters_digest.py` to correctly output directly to `Peter's Digest/` instead of an obsolete legacy path.
* Command Flags: Updated `Prompts/prompt_sentiment.md` and `Commands.md` to correctly include the mandatory `--all` flag for the sentiment script execution.
* Source Material Links: Updated `Gemini.md` to reference the correct `Source Material/` directory instead of the legacy `sources/` folder.
* Index Documentation: Updated `Index.md` to properly map `Discovery_Context.md` and document the `Data/screening/` output directory.
* Commands Documentation: Restructured `Commands.md` to list the Digest Generation and Market Discovery phases, and added `python` prefixes to all execution commands.

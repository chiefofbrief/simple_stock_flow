# Repository Index

This is the comprehensive map of the entire investment research workflow repository. Everything required to run the analysis, from orchestration scripts to source material, is indexed here.

## 1. Core Configuration & Tracking
These files establish the rules of the system and track its outputs.

*   `index.md` - (You are here) The master directory map.
*   `GEMINI.md` - The foundational rulebook. Contains the Workflow Overview, Design Philosophy, Analysis Philosophy & Guidelines, and Workflow Steps.
*   `api_index.md` - Comprehensive map of available APIs (FMP, Alphavantage, Perigon, SociaVault) and their specific endpoints for live data.
*   `Stock_Tracker.md` - Central tracker with three sections: PIPELINE (active analysis), WATCHLIST (continuous monitoring, awaiting entry signal), and Trade Tracker (open positions). Market data columns refreshed weekly by `tracker_update.py`.
*   `context_markets.md` - Rolling market context — macro conditions, prevailing narratives, and recurring signals. Updated daily via the Markets Digest flow.
*   `context_ai_supply_chain.md` - AI supply chain context across all 13 layers. Includes structural dynamics, constraint map, and company-level theses.

---

## 2. Prompts (`Prompts/`)
The instructions passed to the LLM for each stage of analysis. Archived prompts (old workflow) are in `archive/prompts/`.

### Digest
*   `prompt_digest_markets.md` - (Digest) Synthesizes the Markets Digest into LOSER candidates and TAILWIND flags. Updates `context_markets.md`.
*   `prompt_context_update_markets.md` - (Digest) Synthesizes past week's digest analyses into a structured update to `context_markets.md`. Surfaces new screening candidates not yet in the tracker.
*   `prompt_ai_supply_chain_update.md` - (Digest) Reviews new source material and updates `context_ai_supply_chain.md` where warranted.

### Maintenance
*   `prompt_tracker_review.md` - (Maintenance) Run after `tracker_update.py`. Identifies top 3 PIPELINE analysis candidates, add-to-position signals, and removal/demotion flags. Updates SC Layer Coverage section in `Stock_Tracker.md`.

### Deep Dive — 3-Step Workflow
*   `prompt_setup.md` - (Step 0 — Gemini) Runs all fetch scripts for a ticker, extracts MD&A excerpts verbatim, verifies file checklist. No analysis.
*   `prompt_the_context.md` - (Step 1 — Claude) Sentiment landscape, analyst consensus, price/earnings framing, MD&A review, narrative pre-check, preliminary hypothesis. Commits to `### Context` in thesis file.
*   `prompt_the_numbers.md` - (Pass 1 — Claude) Full financial metrics analysis (10 metrics incl. ROIC) + 5-category accounting checklist via targeted grep only. Updated hypothesis. Commits to `### The Numbers` in thesis file.
*   `prompt_the_projection.md` - (Pass 2 — Claude) Full earnings call analysis, catalyst assessment, final synthesis + verdict. Commits to `### The Projection` and `### Synthesis` in thesis file.

### Quality Control
*   `prompt_reviewer.md` - (QC) Augments any step prompt with standards for claims, citations, and cross-section consistency checks. Load alongside any analysis step prompt.
*   `prompt_claude_reviewer.md` - (QC) Independent audit of a completed analysis — checks each thesis section directly against source data files, not against the analysis itself.

---

## 3. Scripts (`Scripts/`)
The Python automation layer that fetches data and writes outputs. Archived scripts (old workflow) are in `archive/scripts/`.

### Main Scripts
*   `price_earnings.py` - Fetches price history and earnings data. Outputs `{TICKER}_price.json` + `{TICKER}_earnings.json`. Run before `tracker_update.py` and `financials.py`.
*   `financials.py` - Fetches financial statements; calculates 10 TTM metrics including ROIC. Outputs `{TICKER}_financial_analysis.md`. Supports optional peer comparison via `--peers` flag.
*   `footnotes.py` - Fetches 10-K/10-Q filing text. Outputs `{TICKER}_notes.md` (footnotes) + `{TICKER}_mda.md` (MD&A). Grepped in Pass 1 — never fully loaded into context.
*   `earnings_calls.py` - Fetches call transcripts. Outputs `{TICKER}_earnings_remarks.md` + `{TICKER}_earnings_qa.md`. Auto-extracts analyst questions to `{TICKER}_qa_questions.md`.
*   `news.py` - Fetches recent news (Perigon + FMP combined). Outputs `{TICKER}_news.md`.
*   `analyst.py` - Fetches analyst price targets and grade actions. Outputs `{TICKER}_analyst.md`.
*   `ticker_reddit.py` - Fetches Reddit posts and top comments via SocialVault. Outputs `{TICKER}_social.md`.
*   `tracker_update.py` - Weekly maintenance. Refreshes all market data columns (P/E, ROIC, EPS YoY, FCF, etc.) for all PIPELINE and WATCHLIST tickers in `Stock_Tracker.md` via FMP. Usage: `python Scripts/tracker_update.py` (all tickers) or `python Scripts/tracker_update.py AXON TSM` (specific tickers).
*   `peer_analysis.py` - Runs FMP peer comparison for PIPELINE and WATCHLIST tickers; filters to AI supply chain-validated companies. Supports discovery of sector peers.

### Automation Scripts
*   `automation_peters_digest.py` - End-to-end automation of the Markets Digest workflow.
*   `automation_tracker_priority.py` - Automates Tracker Update + Tracker Review via Vertex AI.

### Shared Utilities
*   `shared_utils.py` - Core toolkit imported by all scripts (API requests, file I/O, token counting, etc.).

### Research Subscripts (`Scripts/Research Scripts/`)
Data collectors called by `Scripts/news.py`.
*   `news.py` - Aggregates and formats Perigon + FMP news into a combined report.
*   `news_fmp.py` - Fetches financial news via FMP Search Stock News API.
*   `news_perigon.py` - Fetches high-signal news stories via Perigon API.

### Digest Scripts (`Scripts/Digest Scripts/`)
Orchestrators and data collectors for the daily Markets and Sectors digests.

**Orchestrators**
*   `markets_digest.py` - Runs the Markets subscripts and aggregates their output into `Markets_Digest_{DATE}.md`. Focuses on LOSER and TAILWIND discovery from macro, price, and broad market news.
*   `sectors_digest.py` - Runs the Sectors subscripts and aggregates their output into `Sectors_Digest_{DATE}.md`. Groups sources by sector (AI Compute, Infrastructure, Energy, Critical Minerals, etc.).

**Markets Subscripts**
*   `macro.py` - Fetches macroeconomic data points.
*   `movers.py` - Identifies top daily market gainers and losers.
*   `intrigue.py` - Identifies unusual market activity or options flow.
*   `barrons.py` - Scrapes Barron's headlines.
*   `wsj.py` - Scrapes Wall Street Journal headlines.
*   `reddit.py` - Scrapes broad market sentiment from Reddit.

**Sectors Subscripts**
*   `semianalysis.py` - Fetches semiconductor and AI industry news from SemiAnalysis.
*   `trendforce.py` - Fetches semiconductor and energy market intelligence from TrendForce.
*   `servethehome.py` - Fetches server, workstation, and datacenter hardware news from ServeTheHome.
*   `datacenterdynamics.py` - Fetches data center and cloud infrastructure news from Data Center Dynamics.
*   `datacenterknowledge.py` - Fetches data center industry and cloud news from Data Center Knowledge.
*   `fierce.py` - Fetches networking and telecom news from the Fierce Network newsletter.
*   `powermag.py` - Fetches nuclear power industry news from Power Mag.
*   `benchmark.py` - Fetches critical minerals, EV battery, and energy transition news from Benchmark Minerals.
*   `spacenews.py` - Fetches space industry, business, and policy news from SpaceNews.

---

## 4. Output Directories
Where the automation layer writes its findings.

*   `Peter's Digest/Markets Digest/` - Daily Markets Digest files generated by `markets_digest.py` (e.g., `Markets_Digest_{DATE}.md`).
*   `Peter's Digest/Sectors Digest/` - Daily Sectors Digest files generated by `sectors_digest.py` (e.g., `Sectors_Digest_{DATE}.md`).
*   `Screening_{DATE}.md` - The daily screening file. Created by `prompt_daily_screening.md` and updated by `prompt_price_earnings.md`. Contains candidates, enriched context, and price & earnings analysis results.
*   `Data/screening/` - The destination for price and earnings data files (`Price_Data_{DATE}.txt`, `Earnings_{DATE}.txt`) fetched by `price.py` and `earnings.py`.
*   `Data/tickers/{TICKER}/` - The destination for all ticker-specific raw JSON data and the final generated `_Thesis.md` files.

---

## 5. Source Material (`Source Material/`)
Reference texts, frameworks, and insights the LLM can leverage.

### Summaries & Insights (`Source Material/summaries/`)
*Consult summaries first before diving into raw texts.*
*   `insights_index.md` - Master thematic map organizing concepts across all books.
*   `alchemy_of_finance/` - Extracted insights on reflexivity theory, boom/bust model, methodology, and stock market application.
*   `financial_statement_analysis/` - Condensed chapter takeaways on accounting mechanics, balance sheets, cash flows, profit, revenue/expense recognition, EBITDA, credit, and equity analysis.
*   `options_beginner_beyond/` - Condensed summaries covering fundamentals, trade execution, Greeks, risk management, and specific strategies (verticals, credit spreads, calendars, covered calls, straddles, collars, butterflies, etc.).
*   `securities_analysis/` - Graham & Dodd principles: investment vs speculation, intrinsic value, margin of safety, senior securities, convertibles, and price/earnings divergences.

### Raw Texts (`Source Material/raw/`)
**CRITICAL WARNING:** These files are extremely large. Explicit user permission must be obtained before attempting to read them to avoid burning compute.
*   `financial_statement_analysis/` - Comprehensive financial analysis textbook (Fridson & Alvarez).
*   `securities_analysis/` - Graham & Dodd excerpts (Parts 4 to 7).
*   `alchemy_of_finance/` - Reflexivity theory applied to stock markets (Forewords, Preface, New Introduction, and Chapter 1).
*   `options_beginner_beyond/` - 30 chapters covering fundamentals, core strategies, advanced strategies, and specialized topics.

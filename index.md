# Repository Index

This is the comprehensive map of the entire investment research workflow repository. Everything required to run the analysis, from orchestration scripts to source material, is indexed here.

## 1. Core Configuration & Tracking
These files establish the rules of the system and track its outputs.

*   `index.md` - (You are here) The master directory map.
*   `GEMINI.md` - The foundational rulebook. Contains the Workflow Overview, Design Philosophy, Analysis Philosophy & Guidelines, and Workflow Steps.
*   `api_index.md` - Comprehensive map of available APIs (FMP, Alphavantage, Perigon, SociaVault) and their specific endpoints for live data.
*   `Stock_Tracker.md` - Tracks all candidates across phases in two tables — LOSERS and TAILWINDS.
*   `context_markets.md` - Rolling market context — macro conditions, prevailing narratives, and recurring signals. Updated daily via the Markets Digest flow.
*   `context_sectors.md` - Sector context, structural dynamics, and companies of interest across all tracked sectors. Includes AI overarching context and per-sector signals.

---

## 2. Prompts (`Prompts/`)
The instructions passed to the LLM for each stage of analysis.

### Digest
*   `prompt_digest_markets.md` - (Digest) Synthesizes the Markets Digest into LOSER candidates and TAILWIND flags. Updates `context_markets.md`.
*   `prompt_digest_sectors.md` - (Digest) Synthesizes the Sectors Digest into structural sector developments by sector. Produces a Screening Candidates shortlist. Updates `context_sectors.md`.

### Screening
*   `prompt_daily_screening.md` - (Screening) Compiles LOSER and TAILWIND candidates from the digest analyses and user input into `Screening_{DATE}.md`. Enriches each candidate with FMP profile, web fetch, and peer data.
*   `prompt_price_earnings.md` - (Screening) Analyzes price action, earnings trends, valuation, and forward estimates in a single integrated report. Writes results directly to `Screening_{DATE}.md`. Can be run standalone or within the daily screening flow.
*   `prompt_screening_completion.md` - (Screening) Wraps up the screening process for a passed ticker. Initializes the Thesis file and updates the Tracker.

### Deep Dive
*   `prompt_financials.md` - (Deep Dive) Analyzes 10 years/quarters of core financial metrics. Supports optional peer comparison via `--peers` flag.
*   `prompt_footnotes.md` - (Deep Dive) Extracts hidden risks/opportunities from 10-K/10-Q footnotes and MD&A. Includes an Accounting Analysis Guide covering revenue recognition, expense manipulation, balance sheet valuation, cash flow classification, and non-GAAP metrics.
*   `prompt_earnings_calls.md` - (Deep Dive) Analyzes management tone and Q&A from the transcript. Cross-references against all prior analyses.
*   `prompt_research.md` - (Deep Dive) Investigates open questions from all prior analyses using recent Perigon and FMP news data, with up to 3 targeted web fetches for unresolved material questions.
*   `prompt_synthesis.md` - (Deep Dive) *(pending)* Final integration of all analyses into a unified investment verdict.

---

## 3. Scripts (`Scripts/`)
The Python automation layer that fetches data, calls the LLM, and writes the outputs.

### Main Orchestrators
*   `price.py` - Fetches price data for use with `prompt_price_earnings.md`.
*   `earnings.py` - Fetches earnings data for use with `prompt_price_earnings.md`.
*   `financials.py` - Fetches financial statements, calculates metrics, and triggers `prompt_financials.md`. Supports optional peer comparison via `--peers` flag.
*   `footnotes.py` - Fetches 10-K/10-Q text and triggers `prompt_footnotes.md`.
*   `earnings_calls.py` - Fetches call transcripts and triggers `prompt_earnings_calls.md`.
*   `research.py` - Fetches Perigon and FMP news data and triggers `prompt_research.md`.

### Shared Utilities
*   `shared_utils.py` - Core toolkit imported by all scripts (handles API requests, dynamic company name lookups, token counting, file I/O, etc.).

### Research Subscripts (`Scripts/Research Scripts/`)
Data collectors utilized by `research.py`.
*   `news.py` - Aggregates and formats news output from the specific APIs below into a combined markdown report.
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

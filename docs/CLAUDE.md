# Workflow Overview

This repository supports stock identification, screening, and fundamental analysis for investment decisions. The approach is modular and flexible—there is no rigid formula, but rather a set of recurring activities and tools designed to work together during iterative investigation.

---

## Philosophy

You're working with a system that combines **pre-built workflows** with **flexible investigation**. Some tasks recur regularly (market scanning, screening, financial analysis), while others emerge during analysis (investigating specific trends, verifying narratives, checking sources). The repository is designed to support both.

**Modularity matters.** Scripts, data, guidance files, and sources are organized so you can pull what's needed for each situation. Use the indexes to navigate and decide what information or tools are required next.

---

## Default Workflow

The standard analysis pipeline progresses through these steps. Each step builds on prior findings — later analyses should review and reference earlier results.

1. **News Analysis** — Identify candidate tickers from market news. User may add or substitute tickers.
2. **Screening** — Quick price and earnings filter to assess whether candidates warrant deeper analysis.
3. **Sentiment Analysis** — News and social media perception. Informed by screening context.
4. **Financial Statement Analysis** — Fundamental assessment of value drivers, risk, and earnings quality. Informed by screening and sentiment findings.
5. **Notes & MD&A Analysis** — SEC filing investigation targeting items raised in steps 3–4, plus disclosure-level red flags.

**This is a default, not a rigid pipeline.** Steps can be reordered, skipped, or repeated as the situation demands. The system is expected to:

- **Complete the current step** before branching into follow-ups
- **Suggest follow-up analyses or intermediate steps** when the data warrants it (e.g., a claim in sentiment that can be checked with a quick script run before moving to statement analysis)
- **Use existing scripts or create new ones** to fetch data that supports the analysis — the repo is built modularly for this purpose
- **Flag when earlier findings materially affect later interpretation** (e.g., sentiment flags margin pressure → statement analysis should investigate margin trends specifically)

---

## Core Activities

### 1. Identification
**Purpose:** Find stocks worth investigating.

**Approach:** Analyze market news and trends to identify potential candidates. This involves synthesizing broad market signals (movers, macro indicators, sector news, sentiment) to spot opportunities or areas of interest.

**Tools:**
- Market scripts: `discovery.py`, `movers.py`, `macro.py`, news sources (Barron's, WSJ)
- Guidance: `guidance/prompts/news_analysis.md`

---

### 2. Screening
**Purpose:** Put candidates in context. Check if the opportunity is real or if we're chasing a trend that's already played out—or one that's heading in the wrong direction.

**Definition:** "Screening" specifically refers to running the `scripts/valuation.py` script, which generates price, earnings, and valuation analysis for one or more tickers.

**Approach:** Examine price and earnings behavior to understand:
- Recent price movements (1-month, 1-year, 5-year)
- Earnings trends and volatility
- Price-earnings correlation and divergences
- P/E positioning (current vs. historical)

We're looking for downtrends to avoid or uptrends with remaining upside. Screening filters candidates before committing to deep analysis.

**Tools:**
- Ticker scripts: `prices.py`, `earnings.py`, `valuation.py`
- Guidance: `guidance/prompts/screening_analysis.md`

---

### 3. Analysis

Deep investigation of screened candidates. Three dimensions:

#### A. Sentiment Analysis
**Purpose:** Understand market perception and external narratives.

**Approach:** Aggregate news coverage and social media discussion to:
- Identify material themes and events
- Assess brand perception and sentiment trends
- Distinguish signal from noise
- Validate or challenge company narratives

**Tools:**
- Ticker scripts: `news.py`, `reddit.py`, `youtube.py`, `tiktok.py`
- Master script: `sentiment.py` (aggregates all sources)
- Guidance: `guidance/prompts/news_analysis.md`, `guidance/prompts/sentiment_analysis.md`

#### B. Fundamental Analysis
**Purpose:** Assess intrinsic value, risk, and earnings drivers.

**Approach:** Analyze financial statements to:
- Extract projection seeds (8 core metrics for forward modeling)
- Calculate undervaluation and risk metrics (13 priority + 17 secondary)
- Investigate trends: What's driving earnings? What's constraining them?
- Check risk levels: credit quality, cash flow, leverage
- Compare to peers (optional): use `financial_statements.py --compare PEER1 PEER2` to include peer comparison tables in the output

**Tools:**
- Master script: `financial_statements.py` (orchestrates fetch, seeds, metrics, and optional peer comparison)
- Ticker scripts: `fetch_financials.py`, `calc_seeds.py`, `calc_metrics.py`, `compare_financials.py`
- Guidance: `guidance/prompts/statement_analysis.md`, `guidance/frameworks/stock_analysis_guidelines.md`

#### C. Notes & MD&A Analysis
**Purpose:** Investigate SEC filing disclosures to address open questions from prior analyses and surface disclosure-level risks.

**Approach:** Search MD&A and Notes to Financial Statements (10-K and 10-Q) to:
- Address investigation items raised by statement and sentiment analyses
- Scan for disclosure red flags (contingent liabilities, off-balance-sheet items, revenue recognition changes, etc.)
- Compare management narrative (MD&A) with accounting detail (Notes)

**Tools:**
- Ticker script: `sec_filings.py` (fetches and extracts SEC filings from EDGAR)
- Guidance: `guidance/prompts/notes_analysis.md`, `guidance/glossaries/notes.md`

---

## Iterative Investigation

The activities above are starting points, not endpoints. After running scripts and generating initial analysis, we continue investigating using the data and resources available.

**How it works:**
1. Run some or all of the core scripts (identification, screening, analysis)
2. Review outputs and identify questions or gaps
3. Investigate further using source material, web searches, additional API calls, or new scripts
4. Synthesize findings and make decisions

**Example scenario:**
- Market news flags concerns about AI chip supply constraints
- Screen semiconductor stocks; NVDA shows strong price momentum but flat earnings
- Run fundamental analysis; notice inventory buildup in recent quarters
- Question: Is inventory buildup a warning signal?
- Check `docs/index_sources.md` → Locate financial statement analysis insights on inventory
- Review `sources/summaries/financial_statement_analysis/Insights - Chapter 13 - Credit Analysis.md` for cash conversion cycle and inventory interpretation
- Web search: "NVDA inventory buildup 2026" for recent industry perspective
- Synthesize: Is this normal lead-time buying or demand weakness?

---

## Source Material

The repository includes reference material from investment and financial analysis texts organized in a hierarchy:

1. **Guidance files** (`guidance/frameworks/`) — Core principles and sector frameworks. Start here.
2. **Insight summaries** (`sources/summaries/`) — Extracted concepts, frameworks, and source quotes organized by topic. Use `sources/summaries/insights_index.md` as the entry point for navigating by theme.
3. **Raw material** (`sources/raw/`) — Original full-text sources for maximum context when summaries aren't sufficient.

Move down the hierarchy when the current level doesn't provide enough depth for the question at hand.

---

## Navigation & Key Files

### Start Here
- **docs/INDEX.md** - Master index linking to all subindexes
- **This file (docs/CLAUDE.md)** - Workflow context and philosophy

### Subindexes
- **docs/index_scripts.md** - All Python scripts (master, market, ticker, utilities)
- **docs/index_guidance.md** - Guidance files and skill files (prompts)
- **docs/index_sources.md** - Reference materials (investment theory, financial analysis)
- **docs/index_data.md** - Data outputs, directory structure, file naming

### Key Guidance Files
- **guidance/frameworks/stock_analysis_guidelines.md** - Core investment principles (margin of safety, intrinsic value, GAAP vs. economic reality)
- **guidance/prompts/news_analysis.md** - Market news synthesis framework
- **guidance/prompts/** - Task-specific prompts (screening, statement analysis, sentiment analysis, news analysis)

### Command Reference
- **docs/COMMANDS.md** - CLI command examples and usage

---

## Working Together

In most sessions, you'll receive script outputs for analysis or be asked to run scripts. We'll chat about the findings, identify what else we need, and use the indexes to decide next steps. The guidance files and prompts provide the analytical framework; the indexes provide navigation; the scripts and data provide raw material.

Flexibility is the goal. Some sessions will follow the full identification → screening → analysis sequence. Others will dive straight into fundamental analysis or iterate on a specific question. Use the structure when it helps; adapt when it doesn't.

---

## Notes

- **Investigation items:** During analysis, flag questions or gaps in `{TICKER}_tracking.md` for resolution through multiple data sources
- **Objectivity:** Never introduce external knowledge or opinions on financial/stock analysis beyond what's in the data, sources, or established financial theory
- **Explain before acting autonomously:** You are expected to seek additional data, run scripts, make API calls, or create new scripts when the analysis calls for it—that's why the repo is built modularly. The requirement is: before starting autonomous preparation or analysis, explain *what* you plan to do and *why* the data or computation is needed, so the user is aware and can provide feedback on the approach.
- **Iteration expected:** Prompts and guidance files are drafts. We'll refine them through actual use.

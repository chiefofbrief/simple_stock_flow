# Workflow Overview

This repository supports stock identification, screening, and fundamental analysis for investment decisions. The approach is modular and flexible—there is no rigid formula, but rather a set of recurring activities and tools designed to work together during iterative investigation.

---

## Philosophy

You're working with a system that combines **pre-built workflows** with **flexible investigation**. Some tasks recur regularly (market scanning, screening, financial analysis), while others emerge during analysis (investigating specific trends, verifying narratives, checking sources). The repository is designed to support both.

**Modularity matters.** Scripts, data, guidance files, and sources are organized so you can pull what's needed for each situation. Use the indexes to navigate and decide what information or tools are required next.

---

## Core Activities

### 1. Identification
**Purpose:** Find stocks worth investigating.

**Approach:** Analyze market news and trends to identify potential candidates. This involves synthesizing broad market signals (movers, macro indicators, sector news, sentiment) to spot opportunities or areas of interest.

**Tools:**
- Market scripts: `discovery.py`, `movers.py`, `macro.py`, news sources (Barron's, WSJ)
- Guidance: `News Analysis Prompt.md`

---

### 2. Screening
**Purpose:** Put candidates in context. Check if the opportunity is real or if we're chasing a trend that's already played out—or one that's heading in the wrong direction.

**Approach:** Examine price and earnings behavior to understand:
- Recent price movements (1-month, 1-year, 5-year)
- Earnings trends and volatility
- Price-earnings correlation and divergences
- P/E positioning (current vs. historical)

We're looking for downtrends to avoid or uptrends with remaining upside. Screening filters candidates before committing to deep analysis.

**Tools:**
- Ticker scripts: `prices.py`, `earnings.py`, `valuation.py`
- Guidance: `SKILL_screening.md`

---

### 3. Analysis

Deep investigation of screened candidates. Two primary dimensions:

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
- Guidance: `SKILL_news.md`, `SKILL_sentiment_analysis.md`

#### B. Fundamental Analysis
**Purpose:** Assess intrinsic value, risk, and earnings drivers.

**Approach:** Analyze financial statements to:
- Extract projection seeds (8 core metrics for forward modeling)
- Calculate undervaluation and risk metrics (13 priority + 17 secondary)
- Investigate trends: What's driving earnings? What's constraining them?
- Check risk levels: credit quality, cash flow, leverage
- Compare to peers (optional)

**Future additions:** Notes to financial statements, MD&A analysis.

**Tools:**
- Ticker scripts: `fetch_financials.py`, `calc_seeds.py`, `calc_metrics.py`, `compare_financials.py`
- Master script: `financial_statements.py`
- Guidance: `SKILL_statement_analysis.md`, `Stock Analysis Guidelines.md`

---

## Iterative Investigation

The activities above are starting points, not endpoints. After running scripts and generating initial analysis, we continue investigating using the data and resources available.

**How it works:**
1. Run some or all of the core scripts (identification, screening, analysis)
2. Review outputs and identify questions or gaps
3. Use indexes to locate relevant information (sources, additional scripts, data)
4. Investigate further: web searches, source material consultation, additional API calls, new script creation
5. Synthesize findings and make decisions

**Example scenario:**
- Market news flags concerns about AI chip supply constraints
- Screen semiconductor stocks; NVDA shows strong price momentum but flat earnings
- Run fundamental analysis; notice inventory buildup in recent quarters
- Question: Is inventory buildup a warning signal?
- Check `index_sources.md` → Locate financial statement analysis insights on inventory
- Review `Sources/Summaries/Financial_Statement_Analysis/Insights - Chapter 13 - Credit Analysis.md` for cash conversion cycle and inventory interpretation
- Web search: "NVDA inventory buildup 2026" for recent industry perspective
- Synthesize: Is this normal lead-time buying or demand weakness?

This iterative process is where the system shines. The indexes, guidance files, and modular scripts enable flexible investigation.

---

## Navigation & Key Files

### Start Here
- **INDEX.md** - Master index linking to all subindexes
- **This file (CLAUDE.md)** - Workflow context and philosophy

### Subindexes
- **index_scripts.md** - All Python scripts (master, market, ticker, utilities)
- **index_guidance.md** - Guidance files and skill files (prompts)
- **index_sources.md** - Reference materials (investment theory, financial analysis)
- **index_data.md** - Data outputs, directory structure, file naming

### Key Guidance Files
- **Stock Analysis Guidelines.md** - Core investment principles (margin of safety, intrinsic value, GAAP vs. economic reality)
- **News Analysis Prompt.md** - Market news synthesis framework
- **SKILL_*.md files** - Task-specific prompts (screening, statement analysis, sentiment analysis, news analysis)

### Command Reference
- **setup/COMMANDS.md** - CLI command examples and usage

---

## Working Together

In most sessions, you'll receive script outputs for analysis or be asked to run scripts. We'll chat about the findings, identify what else we need, and use the indexes to decide next steps. The guidance files and prompts provide the analytical framework; the indexes provide navigation; the scripts and data provide raw material.

Flexibility is the goal. Some sessions will follow the full identification → screening → analysis sequence. Others will dive straight into fundamental analysis or iterate on a specific question. Use the structure when it helps; adapt when it doesn't.

---

## Notes

- **Investigation items:** During analysis, flag questions or gaps in `{TICKER}_tracking.md` for resolution through multiple data sources
- **Objectivity:** Never introduce external knowledge or opinions on financial/stock analysis beyond what's in the data, sources, or established financial theory
- **Iteration expected:** Prompts and guidance files are drafts. We'll refine them through actual use.

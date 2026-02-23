
We are updating our workflow. You are not permitted to make any edits to files without my written approval. Any old files should be archived, not deleted (unless we are just moving them). Review my instructions carefully at all times, and never assume or hallucinate or use your own knowledge unless you ask first; always rely on my instructions and our source material. All new files will go in the folder WORKFLOW v1. Also note that we will eventually move these files from worfklowv1 to another area, so only update paths which are necessary to run the scripts/analyze the output, not for 'cleaning up'. 

Here is what we have done thus far; review the list of completed tasks below, and standby for instructions: 
   * Workflow V1 Setup: Created WORKFLOW v1 directory structure.
   * Script Migration: Moved peters_digest.py, price.py, earnings.py, shared_utils.py and all digest scripts to WORKFLOW v1/Scripts/.
   * Path Updates: Updated peters_digest.py to point to the new location of digest scripts and save output to WORKFLOW v1/Peter's Digest/. Updated docs/COMMANDS.md.
   * Prompt Creation: Created WORKFLOW v1/Prompts/price_analysis_prompt.md.
   * Execution: Ran Peter's Digest for today.
   * Analysis: Generated and prepended the market analysis to the daily digest file.
   * Git Sync: Pushed all changes to the remote repository.
   * Stock Tracker Update: Added "Earnings/Valuation Analysis" section to WORKFLOW v1/Stock Tracker.md.
   * Earnings Prompt: Created WORKFLOW v1/Prompts/earnings_analysis_prompt.md with specific analysis questions and data inputs.
   * Financials Script: Created WORKFLOW v1/Scripts/financials.py to fetch FMP data (Annual & Quarterly), calculate Earnings Risk, Quality, and ROI metrics, and generate detailed
     markdown reports with statistical analysis (CAGR, CV, Deltas).
   * Script Validation: Verified financials.py accuracy against AAPL SEC filings and confirmed manual TTM calculation logic.
   * Tracker Enhancements: Added "Earnings Risk", "Earnings Quality", and "ROI" subsections to WORKFLOW v1/Stock Tracker.md.
   * Script Update (Quarterly Data): Enhanced financials.py to output "Recent Quarterly Trends" (last 4 quarters + deltas) alongside the annual data tables.
   * Script Testing: Verified the enhanced financials.py output with AAPL.
   * Metrics Prompts: Created WORKFLOW v1/Prompts/earnings_risk_prompt.md, earnings_quality_prompt.md, and roi_prompt.md with interchangeable roles and specific metrics.
   * Prompt Consolidation: Consolidated earnings_risk, earnings_quality, and roi prompts into a single WORKFLOW v1/Prompts/prompt_financials.md, updated with a refined metrics list
     and embedded guidance.
   * Prompt Renaming: Renamed all analysis prompts to follow the prompt_.md convention (prompt_price.md, prompt_earnings.md, prompt_financials.md).
   * Financials Script Update: Updated WORKFLOW v1/Scripts/financials.py to match the new prompt_financials.md structure (flattened JSON, single table output, updated metrics).
     Verified with AAPL.
   * Sentiment Prompt Creation: Created WORKFLOW v1/Prompts/prompt_sentiment.md for analyzing news and social media sentiment.
   * Sentiment Script Migration: Migrated scripts/sentiment.py and dependencies (news.py, reddit.py, etc.) to WORKFLOW v1/Scripts/ and WORKFLOW v1/Scripts/Sentiment Scripts/.
   * Sentiment Script Optimization: Fixed a bug in the YouTube script and lowered Reddit engagement thresholds (10 upvotes, 0 comments) to capture more data. Verified with AAPL.
   * Archive Cleanup: Archived old sentiment scripts to archive/scripts/ with _old suffixes to prevent confusion.
   * Sentiment Lookback Update: Updated WORKFLOW v1/Scripts/Sentiment Scripts/reddit.py and WORKFLOW v1/Scripts/sentiment.py to use a 90-day (3-month) lookback period by default.
   * Footnotes Prompt Creation: Created WORKFLOW v1/Prompts/prompt_footnotes.md for analyzing MD&A and footnotes, ensuring consistency with other analysis prompts.
   * SEC Filings Script Migration: Migrated sec_filings.py to WORKFLOW v1/Scripts/ and updated it to use the new shared_utils location.
   * SEC Filings Script Optimization: Enhanced sec_filings.py with robust extraction logic (whitespace normalization, flexible regex) to correctly handle 10-Q Notes sections, fixing a failure on AAPL. Verified successful extraction for both AAPL and AMZN.
   * Earnings Call Prompt Creation: Created WORKFLOW v1/Prompts/prompt_earnings_calls.md for analyzing earnings call transcripts, focusing on management tone shifts and alignment
     with previous financial/sentiment analyses.
   * Earnings Call Script Implementation: Developed WORKFLOW v1/Scripts/earnings_calls.py to fetch the two most recent quarterly transcripts via AlphaVantage, processing them into a
     consolidated markdown file with clear "Prepared Remarks" and "Q&A" sections for LLM analysis.
   * Earnings Call Script Testing: Verified earnings_calls.py functionality with IBM and AMZN, confirming correct quarter detection (2025Q4/2025Q3), file generation, and markdown
     structure.

-----------------------------------------

Below is our workflow summary. Review it thoroughly and standby; this will serve as the basis for all of our work today, and details matter.

# Investment Research Workflow

## Core Architecture: Two-Phase Funnel

---

## Phase 1: Screening

**Goal:** Rapidly filter tickers to identify candidates worth a deep dive.

**Process:**
1. Run price analysis for all tickers. Review output and filter.
2. Run earnings analysis for surviving tickers only. Review output and filter.
3. Tracker is updated automatically after each step.
4. Promote candidates to Deep Dive phase.

| Step        | Script      | Prompt             | Prereq         |
|-------------|-------------|--------------------|----------------|
| 1. Price    | price.py    | prompt_price.md    | None           |
| 2. Earnings | earnings.py | prompt_earnings.md | Price analysis |

---

## Phase 2: Deep Dive

**Goal:** Build a comprehensive investment thesis for promoted candidates.

**Trigger:** User promotes a ticker from Screening.

**Initialization:** Create `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md` and seed it with the ticker's screening summaries from the Tracker.

**Context dependencies per step:**

| Step              | Script            | Prompt                   | Reads from Thesis                        |
|-------------------|-------------------|--------------------------|------------------------------------------|
| 3. Financials     | financials.py     | prompt_financials.md     | Nothing                                  |
| 4. Sentiment      | sentiment.py      | prompt_sentiment.md      | Financials                               |
| 5. Footnotes      | sec_filings.py    | prompt_footnotes.md      | Financials, Sentiment                    |
| 6. Earnings Calls | earnings_calls.py | prompt_earnings_calls.md | Financials, Sentiment, Footnotes         |

---

## Tracker File

`data/screening/Tracker.md`

Single source of truth for all tickers across all phases. Updated automatically after each step with a concise LLM-generated summary of that step's findings.
```
# Ticker Tracker

| Ticker | Last Run   | Current Phase | Status   | Thesis File             |
|--------|------------|---------------|----------|-------------------------|
| AAPL   | 2026-02-22 | Earnings      | PASS     | —                       |
| MSFT   | 2026-02-22 | Price         | FILTERED | —                       |
| NVDA   | 2026-02-20 | Earnings Calls| ACTIVE   | NVDA_Research_Thesis.md |

---

### AAPL
**Price** | 2026-02-22 | PASS
{LLM-generated summary}

**Earnings** | 2026-02-22 | PASS
{LLM-generated summary}

---

### NVDA
**Price** | 2026-02-20 | PASS
{LLM-generated summary}

**Earnings** | 2026-02-20 | PASS
{LLM-generated summary}

**Financials** | 2026-02-20 | PASS
{LLM-generated summary}

**Sentiment** | 2026-02-20 | PASS
{LLM-generated summary}

**Footnotes** | 2026-02-20 | PASS
{LLM-generated summary}

**Earnings Calls** | 2026-02-20 | ACTIVE
{LLM-generated summary}
```

---

## Prompt Header Template
```
# Context Configuration
- **Target Ticker:** {TICKER}
- **Required Data File:** `data/tickers/{TICKER}/{TICKER}_{TYPE}_data.md`
- **Missing Data?** Run: `python scripts/{SCRIPT_NAME}.py {TICKER}`
- **Context File:** `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md`
    - Sections required: {REQUIRED_SECTIONS}
- **Output:**
    - Append full analysis to `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md` under `## {ANALYSIS_TYPE}`.
    - Append concise summary to `data/screening/Tracker.md` under `### {TICKER} > **{ANALYSIS_TYPE}**`.
```
-----------------------------------------




-----------------------------------------

**Immediate items**
- Properly leverage the Indexes
      - Use planning – have the llm describe the sequence of actions it will take.
- Peer comparisons.

**There is a Skills marketplace** 
- /plugins for skills marketplace

**Make it autonomous. Give it a list of tools and general structure, but let it decide which tools to use when. Tools and Skills and Agents: Consider turning the scripts into tools (?) and prompts into skills/agents(?)**
- Skill should have yaml with name and description. Also good to have overview section.
- /skills to see skills you have
- Launch subagents to work in parallel/divide tasks. Subagents get their own context window and can return results to a main agent.
- /agents to create agent.
- Agents can get their own prompt and skills and tools (you ned to specify the tools), even model (have agents assigned to different roles).
- You can include shell commands in files (aka commands).

**Evaluate responses, tools, etc** 
- Don't focus on just the final output. Rate the intetmediate ouputs: Use reflection (consider using diff models for initial output and eval/refined output). 
- Look at what ools are doing (steps, calls, errors).
- Look at other prompts for ideas. 

**Web search is not necessarily an LLM function only. RAG may not be either**
- https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse
- SQL database: use a function that turns your natural-language questions into SQL queries. You provide your question and the database schema as input. The LLM then generates the SQL query that answers your question.

**Tools to Consider**:
- Github Actions: Can be setup with a command: /setup github-actions.
- Google: Big query database on google cloud.
- Google: Flask dashboard.
- Andrew's pakacge (lets you use multiple models): aisuite==0.1.11.
- vertexai (agents?)
- sqlalchemy
- pydantic
- uvicorn
- notebook experience: ipywidgets, jupyter_server, nbclassic, notebook.
- data analysis/display: duckdb, matplotlib, pandas, seaborn, tabulate, tinydb.
- Machine Learning / NLP: jinja2, psycopg2-binary, scikit-learn.
- json for handling structured data.
- pandas for working with tabular data.
- dotenv to load environment variables (e.g., API keys)
- Google workspace extensions (or gmail) for emails

-----------------------------------------

  Workflow Integration Plan

  This plan establishes a modular yet cohesive workflow for connecting our prompts and scripts, defining data flow, dependencies, and execution contexts.

  Core Architecture: The Two-Stage Funnel


  We separate the workflow into two distinct phases to optimize for volume (screening) vs. depth (research).


  Phase 1: Screening (Batch Processing)
  Goal: Rapidly filter 20+ tickers to find candidates worth investigating.
   * Trigger: Daily screening routine.
   * Output Destination: data/screening/Daily_Screening_{DATE}.md (Single aggregate file).
   * Process:
       1. Run Price and Earnings scripts for a batch of tickers.
       2. LLM analyzes results using prompt_price.md and prompt_earnings.md.
       3. Output is appended to the daily screening file.
       4. Decision Point: User reviews the file and selects tickers for "Deep Dive."



  ┌─────────────┬─────────────┬────────────────────┬──────────────────────────────┬───────────────────────────────────┐
  │ Step        │ Script      │ Prompt             │ Dependency                   │ Output                            │
  ├─────────────┼─────────────┼────────────────────┼──────────────────────────────┼───────────────────────────────────┤
  │ 1. Price    │ price.py    │ prompt_price.md    │ None                         │ Append to Daily_Screening_{DATE}.md │
  │ 2. Earnings │ earnings.py │ prompt_earnings.md │ None (Price context helpful) │ Append to Daily_Screening_{DATE}.md │
  └─────────────┴─────────────┴────────────────────┴──────────────────────────────┴───────────────────────────────────┘



  Phase 2: Deep Dive (Research Thesis)
  Goal: Build a comprehensive investment thesis for selected candidates.
   * Trigger: User "promotes" a ticker from Screening.
   * Output Destination: data/tickers/{TICKER}/{TICKER}_Research_Thesis.md (Dedicated thesis file).
   * Initialization: Create the Thesis file and pre-populate it with the Screening notes (Price + Earnings).
   * Process: Run subsequent analysis scripts; each prompt reads the current state of the Thesis file for context and appends its new findings.



  ┌───────────────────┬───────────────────┬────────────────────────┬─────────────────────────────────┬─────────────────────────────┐
  │ Step              │ Script            │ Prompt                 │ Context Dependency              │ Output                      │
  ├───────────────────┼───────────────────┼────────────────────────┼─────────────────────────────────┼─────────────────────────────┤
  │ 3. Financials     │ financials.py     │ prompt_financials.md   │ Thesis (Screening Notes)        │ Append to _Research_Thesis.md │
  │ 4. Sentiment      │ sentiment.py      │ prompt_sentiment.md    │ Thesis (Financials)             │ Append to _Research_Thesis.md │
  │ 5. Footnotes      │ sec_filings.py    │ prompt_footnotes.md    │ Thesis (Financials + Sentiment) │ Append to _Research_Thesis.md │
  │ 6. Earnings Calls │ earnings_calls.py │ prompt_earnings_calls.md │ Thesis (Financials + Sentiment) │ Append to _Research_Thesis.md │
  └───────────────────┴───────────────────┴────────────────────────┴─────────────────────────────────┴─────────────────────────────┘

  ---

  Implementation Tasks

  1. Update Prompts (Standardization)
  Add a "Context Configuration" header to every prompt file to define execution logic and data sources.

  Template Header:


    1 # Context Configuration
    2 - **Target Ticker:** {TICKER}
    3 - **Required Data File:** `data/tickers/{TICKER}/{TICKER}_{TYPE}_data.md`
    4 - **Missing Data?** Run: `python WORKFLOW\ v1/Scripts/{SCRIPT_NAME}.py {TICKER}`
    5 - **Context Source:**
    6     - *Screening Phase:* None.
    7     - *Research Phase:* Read `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md`.
    8 - **Output Destination:**
    9     - *Screening Phase:* Append to `data/screening/Daily_Screening_{DATE}.md`.
   10     - *Research Phase:* Append to `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md` under header "## {ANALYSIS_TYPE}".


  2. Update GEMINI.md (Routing Logic)
  Define the high-level instructions for the CLI to manage this workflow.
   * Screening Mode: Instructions for batch running and aggregate filing.
   * Research Mode: Instructions for creating the Thesis file and sequencing the Deep Dive prompts.
   * Analysis Principles: Reference the external guidance document.


  3. Create guidance/analysis_principles.md (Foundation)
  Centralize the analytical philosophy (skepticism, verification, specific frameworks) to keep individual prompts focused and lightweight.
   * Content:
       * "Trust but verify" (Data vs. Narrative).
       * Soros/Graham frameworks (Reflexivity, Margin of Safety).
       * Specific red flags to always check.

  ---


  Execution Order
   1. Update Prompts: Add headers and context logic.
   2. Update `GEMINI.md`: Define the workflow rules.
   3. Create Guidance: Write analysis_principles.md.



------------------------------------------


1. **Revenue**

**Description**:
Revenue is the foundation of all profitability metrics and the top-line measure of business scale.

**Interpretation**:
- Revenue growth substantially above industry with maintained margins indicates strengthening position; growth above industry with compressing margins suggests buying share through price cuts.
- Companies maintaining price increases through downturns demonstrate pricing power; those forced to cut prices reveal commodity-like competition.
- When revenue declines, distinguish between industry-wide pressure (potentially creating sector-wide opportunity if prices become depressed) versus company-specific weakness indicating loss of competitive position.
- Red flag: Growth substantially outpacing competitors without operational explanation warrants investigation and could signal aggressive accounting.

**Context and Considerations**:
- Revenue growth without margin improvement creates no shareholder value—acceleration alone is meaningless if profit per dollar of sales remains constant or declines.
- Rapid growth attracts competition and rarely persists indefinitely.
- Revenue quality depends on conversion to cash. Monitor the relationship between revenue growth and receivables/inventory growth—significant divergences may indicate revenue is not representing completed economic transactions. See Working Capital metric.
- Contrarian opportunity: Industry-wide revenue decline creating sector-wide price depression when an individual company's competitive position and market share remain intact.

---

2. **Operating Margin (Formula: Operating Income ÷ Revenue × 100)**

**Description**:
Shows management performance before financial structure and taxes—the clearest measure of whether the core business generates durable profit at scale.

**Interpretation**:
- Stable margins over 5-7 years indicate permanence of earning power.
- High margins relative to peers suggest competitive advantages—pricing power, cost advantages, or operational excellence. Such advantages may be sustainable if protected by moats (brand strength, network effects, regulatory barriers, proprietary technology).
- Narrower margins create greater danger—modest adverse changes can quickly produce losses.

**Context and Considerations**:
- Margins well above asset-based returns attract competition; margins below normal may improve as weak competitors exit.
- Confirm management continues investing in the business (see Capital Expenditures). The risk is cutting investment to boost near-term margins while impairing long-term competitiveness through deferred maintenance, reduced R&D, or eliminated advertising.
- Contrarian opportunity: Depressed margins in mature, established companies with solid market positions when driven by temporary factors (one-time charges, transient input cost spikes, short-term demand weakness).

---

3. **Operating Cash Flow**

**Description**:
Measures the actual cash generated by business operations, cutting through accounting discretion to reveal economic reality. Most valuable precisely when income statements are least reliable—in highly leveraged companies, troubled firms, and situations where accounting choices distort reported results.

**Interpretation**:
- Companies can dress up earnings temporarily through accounting choices, but cannot manufacture cash. When income statements and cash flow diverge significantly, it signals either aggressive accounting or deteriorating business fundamentals.
- Strongly positive OCF in mature companies indicates self-funding capability and financial strength.

**Context and Considerations**:
- Contrarian opportunity: Temporarily depressed OCF in fundamentally sound businesses where the divergence from earnings is driven by transient rather than structural factors.

---

4. **Free Cash Flow (Formula: Operating Cash Flow - Capital Expenditures)**

**Description**:
Free cash flow represents the cash an owner can pocket after paying all expenses and making necessary maintenance investments—"the well from which all returns are drawn." It is the ultimate measure of value creation regardless of how that value is deployed (dividends, buybacks, growth investment).

**Interpretation**:
- Consistent FCF generation indicates a self-funding business not dependent on external capital.
- Strong current FCF generation means nothing if the business model is deteriorating or if the company benefited from unsustainable temporary factors.

**Context and Considerations**:
- Self-funding companies avoid painful dependence on external financing. During credit crunches, external financing becomes expensive or unavailable; self-funding companies gain decisive competitive advantage by continuing essential investments while credit-dependent competitors retrench.
- Loss of flexibility feeds on itself: downturn hits → forced choice between cutting profit-enhancing investments or increasing external financing dependence → either path leads to further flexibility loss.
- Contrarian opportunity: Strong FCF generation in out-of-favor companies where the market focuses on reported earnings weakness while ignoring cash generation capacity.

---

5. **OCF / Net Income (Formula: Operating Cash Flow ÷ Net Income)**

**Description**:
Measures earnings quality by comparing reported profits to actual cash collection.

**Interpretation**:
- Ratios consistently near or above 1.0 indicate high-quality earnings backed by cash; ratios substantially below 1.0 reveal gaps between reported profits and cash reality.
- > 1.1: Conservative accounting or efficient working capital management—high quality earnings.
- 0.8 - 1.1: Reasonable earnings quality.
- < 0.8 (especially if deteriorating vs. peers): Earnings significantly exceed cash generation, suggesting potential revenue recognition issues, working capital consumption, or reserve inadequacy.

**Context and Considerations**:
- Contrarian opportunity: In highly leveraged companies, heavy debt loads create large interest expenses that depress net income, yet the company may generate strong cash flow because depreciation provides actual cash available for debt service. Traditional accounting returns can decline while actual cash compounding remains strong—focus on cash generation capacity rather than accounting returns on book equity in these situations.

---

6. **Working Capital (Formula: Current Assets - Current Liabilities)**

**Description**:
Measures the capital employed in day-to-day operations. It tells you how efficiently a company converts its operations into actual cash, and whether growth is self-funding or a cash drain.

**Interpretation**:
- When WC grows faster than revenue (e.g., 30% versus 10%), it indicates cash consumption through deteriorating collection, inventory accumulation, or supplier payment issues—the company is consuming cash beyond what growth justifies.
- Two distinct patterns:
  - Healthy pattern: Payables grow faster than receivables and inventory, meaning vendors' trade credit funds working capital expansion from sales growth. Suppliers are essentially financing the company's growth through trade credit. The company isn't tying up its own cash to fund expansion.
  - Dangerous pattern: Inventory builds disproportionately to sales (goods sitting unsold), while receivables expand (customers paying slowly). This widens the gap between cash needs and supplier financing. It can cascade: deteriorating credit quality causes vendors to tighten terms, which forces the company to seek expensive external financing or cut operations.
- During periods with losses, pattern recognition becomes critical:
  - Favorable: Inventory shrinks faster than losses accumulate, and cash actually improves or payables decline—management is preserving liquidity through the difficult period.
  - Unfavorable: Losses are financed by drawing down cash or piling up current liabilities. Working capital depletes, indicating the company is burning through liquidity concurrent with operational losses.

**Context and Considerations**:
- Growing businesses consume cash building working capital, but working capital as a percentage of sales should remain fairly constant absent business model changes.
- Watch for covenant risk in leveraged companies. Bank agreements often cap total debt. Once a company hits that ceiling, it loses the ability to borrow its way through a rough patch and may be forced to cut investment or operations to stay compliant—potentially at the worst possible time.
- Contrarian opportunity: When the market fixates on near-term earnings weakness, it sometimes ignores a strong working capital position—a liquid, well-managed balance sheet that gives the company staying power through a downturn. That gap between perception and financial reality can be where value hides.

---

7. **Operating Leverage (Formula: % Change in Operating Income ÷ % Change in Revenue)**

**Description**:
Measures how dramatically operating income changes relative to sales volume changes. Reveals both the opportunity for earnings acceleration and the risk of volatility inherent in the fixed-cost structure.

**Interpretation**:
- High operating leverage creates powerful earnings inflection potential. Once fixed costs are covered, each incremental revenue dollar contributes its full margin directly to operating profit—modest sales increases can produce dramatic earnings growth.
- Operating leverage >3× indicates strong earnings sensitivity where revenue growth translates to disproportionate profit growth.
- The same structure that amplifies gains in good times amplifies losses in bad times. When combined with high financial leverage, operating leverage creates particularly severe asymmetric risk—small revenue shortfalls can drive operating income below levels needed to cover interest expense, triggering financial distress.
- Red flag: Operating leverage increasing (rising PP&E %) while revenue growth decelerates.

**Context and Considerations**:
- Contrarian opportunity: Companies with high operating leverage temporarily suffering from low capacity utilization, or businesses with high operating leverage in growing markets—in both cases, the magnification effect works strongly in investors' favor once revenue inflects.

---

8. **Capital Expenditures**

**Description**:
Capex reveals how much cash a business must reinvest just to maintain its competitive position—and how much it's spending to grow.

**Interpretation**:
- The capex/depreciation ratio is a quick lens on capital intensity and growth posture:
  - Ratio <1.0: The company is spending less than its assets are depreciating. This is either an asset-light business model (positive) or underinvestment that will eventually impair competitiveness (negative).
  - Ratio ≈1.0: Maintenance mode. The company is replacing assets roughly as they wear out, consistent with a mature, stable business not in aggressive growth or contraction.
  - Ratio >1.5: Active growth investment beyond replacement. Acceptable, even desirable, if returns on that investment are strong. Concerning if sustained high capex isn't translating into revenue or margin growth.

**Context and Considerations**:
- A business that grows with minimal capex generates far more free cash flow than one that must constantly reinvest to stay competitive. A company spending heavily just to defend its current position (airlines, telecom, utilities) is in a fundamentally different position than one choosing to invest from a position of strength.
- Industry context is essential: software and asset-light business models can scale with minimal incremental capex; manufacturing, energy, and infrastructure businesses require capex roughly proportional to revenue. Cross-industry comparisons are misleading without this adjustment.
- Watch for capex cuts during downturns as a warning sign. Management may be protecting near-term cash flow at the expense of future competitiveness.
- Contrarian opportunity: Companies with a history of high capex transitioning to lower-intensity models (e.g., outsourcing manufacturing, shifting to software/services) may generate a step-change in free cash flow that the market hasn't priced in yet.

---

9. **Depreciation & Amortization**

**Description**:
Non-cash charges that reduce reported earnings but don't require cash outlays in the current period.

**Interpretation**:
- Historical depreciation rate (as % of PP&E) reveals asset intensity:
  - High rates (8-10%) signal an asset-heavy business requiring continuous reinvestment.
  - Low rates (2-3%) indicate an asset-light model with better cash conversion.

**Context and Considerations**:
- For highly leveraged companies, depreciation provides an interest coverage cushion—the company may generate sufficient cash to service debt even when reported earnings appear inadequate. Over the long term, however, companies must replace depreciating assets, so this cushion is temporary.
- Contrarian opportunity: High D&A companies generate more cash than income statements suggest, creating potential hidden value—particularly relevant in leveraged situations.
- Contrarian opportunity: Overly conservative depreciation (rates above peers) understates true earnings; rates materially below peers may signal expense understatement to inflate earnings.
- Key manipulation patterns: writing down assets in bad years to reduce future depreciation, extending useful life assumptions under earnings pressure, and arbitrary year-to-year policy changes with no clear relationship between charges and the property account.

---

10. **Debt / Total Assets (Formula: Total Debt ÷ Total Assets × 100)**

**Description**:
Shows what proportion of the asset base is financed with debt versus equity.

**Interpretation**:
- 30-40%: Moderate leverage—optimal range for many businesses
- Above 60%: High leverage—elevated risk but potential for strong equity returns if well-managed
- Rising ratios indicate leveraging up without corresponding earning power growth, potentially impairing credit quality.

**Context and Considerations**:
- Permanent short-term debt must be included (many borrowers rely on short-term debt that's never actually repaid but rather continuously renewed).
- Convertible debt counts as debt until it's actually converted to equity, not when conversion options exist.
- Contrarian opportunity: Moderate leverage in stable businesses can enhance equity returns without excessive risk.

---

11. **Debt / Operating Cash Flow (Formula: Total Debt ÷ Operating Cash Flow; expressed in years)**

**Description**:
Measures the time required to eliminate all debt if 100% of operating cash flow were dedicated to debt repayment.

**Interpretation**:
- < 3 years: Strong debt service capacity—excellent credit quality, indicates financial strength and capacity for strategic initiatives.
- 3-6 years: Moderate capacity—acceptable for most businesses.
- > 6 years: Weak capacity, elevated default risk.

**Context and Considerations**:
- It's the best single credit quality measure because it's built from two comparatively hard numbers less subject to manipulation than earnings-based metrics. For example, under-depreciation merely moves money between pockets without affecting cash flow. A company with $60M debt and $20M OCF could retire debt in 3 years—clearly more flexible than $80M debt with $10M OCF requiring 8 years.
- Ratio rising due to OCF decline rather than debt increase signals operational deterioration rather than strategic leverage increase.



---------------------------------



1. earnings risk:
   -  Debt / Total Assets: [Debt = S]
   -  Debt / Operating Cash Flow: [P]
   -  NCAV (Net Current Asset Value): [P]
   -  Accruals Gap: [P]
   -  CapEx: [S]
   -  Depreciation & Amortization: [P, S]
   -  Working Capital: [P]
2. earnings quality:
    - Revenue: [P, S]
    - Operating Margin: [P]
    - Operating Cash Flow: [P]
    - Free Cash Flow: [P]
    - OCF / Net Income: [P]
3. roi:
    - ROTC (Return on Total Capital): [P]
    - ROE (Return on Equity): [P]
    - Operating Leverage: [P]


**PROCESS:**

**Quant Analysis:**
1. price.
2. earnings.
3. earnings risk:
   -  Debt / Total Assets: [Debt = S]
   -  Debt / Operating Cash Flow: [P]
   -  NCAV (Net Current Asset Value): [P]
   -  Accruals Gap: [P]
   -  CapEx: [S]
   -  Depreciation & Amortization: [P, S]
   -  Working Capital: [P]
4. earnings quality:
    - Revenue: [P, S]
    - Operating Margin: [P]
    - Operating Cash Flow: [P]
    - Free Cash Flow: [P]
    - OCF / Net Income: [P]
5. roi:
    - ROTC (Return on Total Capital): [P]
    - ROE (Return on Equity): [P]
    - Operating Leverage: [P]

**Qual Analysis**:
2. internal sentiment (earnings calls):
    - What are analysts paying attention to?
    - What narrative is management trying to push?
    - Does internal sentiment align with external sentiment?
4. Notes (financial statments) / MD&A:
    - What do the filings reveal about questions/concerns raised by prior analyses?
    - Do the filings align with prior analyses, or are there areas of divergence?
    - Are there risks that were not identified in prior analyses?


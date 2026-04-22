# Footnotes & MD&A Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided Footnotes and Management's Discussion and Analysis (MD&A) for **{TICKER}** and produce a concise, insightful report.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — The stock's thesis, including the prior Financials and Sentiment analyses.
- `Data/tickers/{TICKER}/{TICKER}_notes_mda.md` — Footnotes and MD&A content. Run: `python Scripts/footnotes.py {TICKER}`
- If `{TICKER}` has an `AI SC` Sector Theme (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant layer section of `context_ai_supply_chain.md`.

### Data Quality Gate

**Before stopping, verify the extraction output.** The script prints a validation table — confirm all four sections PASS:

| Section | Minimum words |
|---|---|
| 10-K MD&A | 3,000 |
| 10-K Notes | 1,000 |
| 10-Q MD&A | 2,000 |
| 10-Q Notes | 500 |

If the script exits with `RESULT: FAILED`, **do not proceed**. Report the failure to the user — a section likely captured a table of contents instead of body text. Do not attempt analysis on incomplete data.

If all sections pass, also do a quick content sanity check on `{TICKER}_notes_mda.md`:
- The 10-K Notes section contains actual note body text (disclosures, accounting policies, tables) — not just a list of note titles with page numbers.
- Both MD&A sections contain year-over-year revenue/expense comparisons and management commentary.

If either sanity check fails despite the word count passing, flag it before stopping.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Analyze the text to answer the questions in the Output Format below.
- All insights must leverage the provided text. Explicitly specify which details led to your conclusion.
- **Financials context:** The Financials analysis in the Thesis file is your primary cross-reference. For each significant disclosure, consider whether it confirms, explains, or challenges the metric conclusions from that analysis. For metric-specific accounting context, refer to the Metric Interpretations in the prior Financial Analysis.
- **Accounting checklist:** When reviewing footnotes and MD&A, specifically look for the items in the Accounting Checklist at the bottom of this prompt.
- **Reference:** Consult `Source Material/summaries/financial_statement_analysis/` for accounting mechanics, earnings manipulation patterns, and credit analysis context. See `Source Material/summaries/insights_index.md` for a thematic map. *CRITICAL WARNING: Do not access Source Material/raw/ without explicit user permission to avoid burning compute.*

### Deliverable

**Questions:**
1. **Data Check:** Have all findings been sourced directly from the footnotes/MD&A text — no outside data introduced?
2. **Financials Cross-Reference Check:** Has each significant disclosure been evaluated against the prior financial analysis conclusions?
3. **Accounting Check:** Have the disclosures been reviewed against the Accounting Checklist below?
4. **Summary Check:** Does the Footnotes & MD&A Summary accurately reflect the findings?

### Output Format

#### {TICKER} Footnotes & MD&A Analysis

**1. Do the footnotes/MD&A reveal anything material not captured in the financial statements?**
[Answer using specific details from the text]

**2. Do the footnotes/MD&A confirm or challenge the conclusions from the financial analysis? Are there accounting policies, estimates, or disclosures that help explain — or cast doubt on — the reported metrics?**
[Answer using specific details from the text]

**3. Do the footnotes/MD&A reveal any accounting choices that appear to be inflating or depressing reported earnings, cash flow, or balance sheet figures?**
[Answer using specific details from the text]

**4. Are there any disclosures that appear incomplete, inconsistent with the financial statements, or that warrant deeper investigation?**
[Answer using specific details from the text]

**Footnotes & MD&A Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Thesis file.]

- **Action:** Ask: *"Do you approve this analysis? Should I update the Thesis file and Stock Tracker?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval:
- Update **### Footnotes & MD&A** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with the full analysis.
- Update `Stock_Tracker.md` — advance **Current Phase** for `{TICKER}` to the next phase.

**STOP. Wait for user approval before committing.**

---

## Accounting Analysis Guide

When reviewing footnotes and MD&A, flag anything that diverges from peers, prior periods, or stated policy — changes often matter more than absolutes. Multiple red flags together indicate systemic problems, not isolated mistakes.

---

### 1. Revenue Recognition

**What to look for:**
- Revenue recognition policy disclosures and any changes from prior periods
- Days Sales Outstanding (DSO) trend: receivables ÷ sales
- Accrued/unbilled receivables as % of revenue vs. peers
- Unearned income balances (for subscription/service businesses)

**Signals:**
- Rising DSO indicates revenue not converting to cash — possible channel stuffing, credit loosening, or fictitious sales
- Allowance for doubtful accounts not keeping pace with receivables growth — earnings inflated by lowering credit standards without proportionally increasing bad debt reserves
- Accrued income materially above peers: revenue recognized before billing (percentage-of-completion abuse or aggressive timing)
- Unearned income unusually low for subscription/service businesses suggests revenue front-loading
- Revenue recognition policy changes coinciding with earnings pressure

**Interpretation:**
- Test reported revenue against any available third-party data (industry shipments, app downloads, pharmacy-level data, etc.) — gaps between reported and independent data are the clearest channel-stuffing signal
- Consistently beating EPS guidance by exactly $0.01-$0.02 is statistically unnatural
- Round-trip transactions: if management lends to counterparties who return cash as "revenue," no wealth has been created — follow the cash flows

---

### 2. Expense Recognition & Cost Capitalization

**What to look for:**
- Capitalization policies for software development, internal costs, or other discretionary items
- Depreciation and useful life assumptions vs. industry peers
- Reserve and accrual levels and changes year-over-year
- "One-time" or "non-recurring" charges and their frequency
- Supplier/vendor rebate accounting policies

**Signals:**
- Useful life extensions reduce D&A and boost earnings — compare annual depreciation rate (D&A ÷ gross PP&E) to peers; material divergence warrants scrutiny
- Costs capitalized that peers expense artificially inflate current earnings
- Cookie-jar reserves: large reserves built in loss periods, then drawn down in recovery — watch for reserves growing disproportionately, then shrinking with precision
- "Non-recurring" charges that recur annually are operating costs in disguise
- Rebates booked immediately rather than amortized over the multi-year contract period

**Interpretation:**
- Big bath accounting: new management takes large write-offs early in tenure, then takes credit for "turnaround" — be skeptical when the recovery looks too clean
- The snowballing principle: manipulation requires ever-larger subsequent manipulations; watch for growing transaction sizes and reserve levels
- Declining profitability → accounting aggression is a documented pattern; when credit ratings fall alongside accounting liberalization, treat as cultural deterioration, not isolated mistakes
- "Seemingly small" reserve additions accumulate to create vast manipulation opportunity

---

### 3. Balance Sheet & Asset Valuation

**What to look for:**
- Goodwill as % of total assets and impairment testing assumptions
- Fair value measurement levels (Level 1/2/3) for financial assets
- Off-balance-sheet obligations: operating leases, pension/post-retirement liabilities, JV guarantees, contingent liabilities
- Related-party transactions and whether terms appear arm's length
- Changes in auditor or unusual audit fee levels

**Signals:**
- Goodwill impairment testing can be gamed indefinitely — watch for sustained goodwill alongside deteriorating business performance; impairment is a lagging indicator
- Level 3 fair value (assumptions about assumptions) creates manipulation opportunity; inflated asset values may not survive scrutiny
- Off-balance-sheet obligations not captured in Debt/Assets or Debt/OCF — add back pension underfunding and operating lease PV to get true leverage picture
- Related-party transactions at non-arm's length terms: classic mechanism for round-trip profits
- Auditor firing after restatement requirement + replacement with obscure firm = high fraud risk (appeared in Enron, Satyam, Celadon)
- Audit fees spiking dramatically or absurdly low relative to company size — both are red flags

**Interpretation:**
- Calculate leverage ratios both with and without goodwill — goodwill cannot be sold, factored, or used in a sale-leaseback; give greater weight to tangibles-only version
- Compare annual depreciation rate (D&A ÷ gross PP&E) to peers — materially lower rate means assets may be overstated
- "Synergies" is one of the most dangerous words in finance — acquisitions at large premiums to book value that rely on synergies rarely deliver

---

### 4. Cash Flow & Working Capital

**What to look for:**
- Classification of specific items as operating vs. investing activities
- Accounts receivable factoring or securitization disclosures
- Working capital component trends: receivables ÷ sales, inventory ÷ COGS
- Company reporting large cash balance while drawing down credit lines

**Signals:**
- Operating outflows reclassified to investing activities artificially inflate OCF
- Receivables factoring pulls forward cash and masks collection quality
- Material increase in receivables or inventory as % of sales is a red flag — W.T. Grant reported positive traditional cash flow until two years before bankruptcy while working capital deteriorated
- Large reported cash balance alongside simultaneous credit line drawdowns is a classic fraud signal

**Interpretation:**
- Working capital changes reveal weakness that EBITDA and "net income + depreciation" completely miss — OCF including working capital changes (net income + depreciation − Δ working capital requirements) is the more informative measure
- Healthy pattern: payables growing faster than receivables and inventory (suppliers financing growth via trade credit)
- Dangerous pattern: inventory builds disproportionately to sales + receivables expand = cash consumed beyond what growth justifies
- Depreciation is a temporary safety valve — over a full cycle, capex equals or exceeds D&A; EBITDA coverage that relies on D&A cushion is not sustainable long-term

---

### 5. Non-GAAP Metrics & Adjusted Earnings

**What to look for:**
- Any "Adjusted," "Core," or non-GAAP earnings definitions in MD&A
- Items excluded from non-GAAP: are they genuinely one-time?
- Stock-based compensation treatment
- "Adjusted EBITDA" with idiosyncratic add-backs

**Signals:**
- Items excluded from non-GAAP that actually recur inflate "adjusted" earnings relative to economic reality
- Stock-based compensation is a real economic cost — excluding it understates true labor expense
- "Run rate" annualization from a single strong month or quarter is aggressive
- When adjusted earnings improve while GAAP, OCF, and working capital deteriorate, the adjusted figure is obscuring the real trend

**Interpretation:**
- Ask three questions about every non-GAAP add-back: Is this genuinely one-time? Would a buyer of the business get credit for eliminating this cost? Do peers use the same adjustment?
- Once analysts fixate on a single metric, companies devote enormous effort to gaming it — analytical diversity is the defense: when one metric is dressed up, others reveal the manipulation
- Willingness to question GAAP is essential, but management-promoted alternatives that eliminate real costs are equally suspect

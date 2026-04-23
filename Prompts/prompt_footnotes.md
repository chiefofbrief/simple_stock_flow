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
- **Accuracy — quote, don't paraphrase:** For accounting policy changes, quote the filing's exact language — do not substitute an interpretation for what the document says.
- **Accuracy — temporal:** When citing figures from multi-period tables, state which period they belong to — a figure in the prior-year column is not a current-year cost.
- **Quality bar:** See the **Example Analysis** at the bottom of this prompt. It demonstrates the required level of rigor, depth, and cross-reference integration — not a template to replicate structurally.

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
- Restructuring charges declining sharply YoY create a one-time tailwind to operating income comparisons — quantify the change before drawing performance conclusions
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
- Calculate leverage ratios both with and without goodwill — goodwill cannot be sold, factored, or used in a sale-leaseback; give greater weight to tangibles-only version
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
- Segment cost reclassifications between segments and corporate — prior-period restatements break trend comparability
- Segment revenue growth rates by individual segment — material inflections may be invisible in consolidated figures
- Upcoming segment reorganizations or consolidations disclosed in the MD&A

**Signals:**
- Items excluded from non-GAAP that actually recur inflate "adjusted" earnings relative to economic reality
- Stock-based compensation is a real economic cost — excluding it understates true labor expense
- "Run rate" annualization from a single strong month or quarter is aggressive
- When adjusted earnings improve while GAAP, OCF, and working capital deteriorate, the adjusted figure is obscuring the real trend

**Interpretation:**
- Ask three questions about every non-GAAP add-back: Is this genuinely one-time? Would a buyer of the business get credit for eliminating this cost? Do peers use the same adjustment?
- Once analysts fixate on a single metric, companies devote enormous effort to gaming it — analytical diversity is the defense: when one metric is dressed up, others reveal the manipulation
- Willingness to question GAAP is essential, but management-promoted alternatives that eliminate real costs are equally suspect

---

## Example Analysis

The following is a completed Footnotes & MD&A analysis for INTU (Intuit). It is included to illustrate the required standard of rigor, depth, and cross-reference integration — the level of specificity expected in quantifying findings, connecting disclosures back to prior financial analysis conclusions, and surfacing items that are easy to miss or misread. Do not replicate its structure or findings mechanically; every company's filing is different.

---

#### INTU Footnotes & MD&A Analysis

**1. Do the footnotes/MD&A reveal anything material not captured in the financial statements?**
Four items are material and not directly visible in the financial statements.

First, a revenue recognition policy change for QuickBooks Desktop. Prior to fiscal 2025, INTU deemed "when-and-if-available product upgrades and enhancements" included in Desktop subscriptions to be not material and did not separately allocate or recognize them. Beginning Q2 FY2025, these upgrades are recognized as a separate performance obligation on a straight-line basis over the subscription term. This carves out a previously-bundled component, creates incremental deferred revenue, and depresses current-period product revenue — contributing to the deceleration of Desktop Ecosystem growth (5% in FY2025 vs. 16% in FY2024). The magnitude is not separately quantified in the filing.

Second, the FY2025 operating income comparison is meaningfully inflated by a $208M YoY decrease in restructuring charges ($223M in FY2024 → $15M in FY2025, from the July 2024 workforce/real estate reorganization). The MD&A discloses this directly: of the $870M increase in total operating expenses, a $208M reduction in restructuring charges partially offset increases in marketing (+$410M), staffing (+$300M), and outside services (+$161M). This means the reported 36% operating income growth and 2.28x operating leverage are partially a restructuring artifact rather than pure business improvement. Stripping this out, underlying operating income growth is closer to 25-28%.

Third, Credit Karma recovered sharply: +32% YoY to $2.26B in FY2025 (from $1.71B in FY2024), driven by personal loans, credit cards, and auto insurance. This segment was a persistent drag post-acquisition and its inflection is a meaningful positive for the thesis — the prior financial analysis treated it as background noise rather than a business quality signal.

Fourth, Online Ecosystem grew 20% ($8.30B) while Desktop Ecosystem grew only 5% ($2.78B). Online is now 75% of Global Business Solutions revenue (up from 72%). The mix shift is positive — Online is higher-quality recurring subscription revenue — but confirms Desktop is in secular decline, with the revenue recognition change further suppressing the reported rate.

Additionally, the footnotes detail ongoing FTC actions regarding INTU's marketing of "free" tax preparation programs. The FTC's ALJ ruled against INTU in August 2023, commissioners affirmed it in January 2024, and a final order (with no monetary penalties, only marketing restrictions) took effect March 2024 while INTU's Fifth Circuit appeal is pending. Separately, INTU settled with 50 state AGs for $141M in FY2022 (already expensed). These are largely resolved matters with contained financial exposure, not an ongoing liability overhang.

**2. Do the footnotes/MD&A confirm or challenge the conclusions from the financial analysis? Are there accounting policies, estimates, or disclosures that help explain — or cast doubt on — the reported metrics?**
The D&A decomposition confirms the financial analysis. The cash flow statement separates depreciation ($172M) from amortization of acquired intangible assets ($637M), confirming that 79% of the D&A addback is benign intangible burn-off from the Mailchimp and Credit Karma acquisitions, not underlying asset consumption. Physical capital intensity is near zero. The $637M amortization will continue declining as these acquired intangibles age toward full amortization, which will mechanically compress OCF/NI toward 1.0x over time — as the financial analysis forecast.

On SBC composition: the $1.97B total is confirmed ($1,968M). Of this, 91% is time-based RSUs (vesting on continued service, valued at intrinsic value at grant) — the remaining 9% is market-based and performance-based RSUs. FY2025 restructuring-related SBC was $0; the $25M figure cited in prior analysis was FY2024 only and is now resolved. By cost line: R&D ($629M), selling & marketing ($541M), cost of service revenue ($420M), and G&A ($375M). The R&D and S&M concentration is consistent with a software company competing heavily on engineering talent and sales execution — both are structurally recurring costs.

The goodwill picture is a significant challenge to the financial analysis's presentation of leverage. Total goodwill is $13.98B; net acquired intangibles are $5.30B — together ~$19.3B, or approximately 57% of total assets. The accounting checklist requires calculating leverage both with and without goodwill, since goodwill cannot be sold, factored, or used in a sale-leaseback. Goodwill impairment testing uses Level 3 assumptions (DCF + market comparables) and is inherently lagging — no impairment has been recorded in FY2023-2025, but goodwill is tested annually in Q4 and carries subjective estimation risk. Debt/Tangible Assets is approximately 50%+, a materially different picture than the 22% Debt/Total Assets figure in the financial analysis. This does not change the debt serviceability conclusion (Debt/OCF of 1.08x remains the correct operating metric) but it does mean the balance sheet is far less "conservative" on a tangible basis than the headline ratio implies.

The operating leverage conclusion also requires revision in light of the restructuring reversal: the 2.28x figure for FY2025 is partly an artifact of $208M in non-recurring charges rolling off, not purely fixed-cost absorption. The underlying operating leverage, absent this tailwind, is lower.

**3. Do the footnotes/MD&A reveal any accounting choices that appear to be inflating or depressing reported earnings, cash flow, or balance sheet figures?**
Three items are relevant.

The most significant is the restructuring reversal: $208M in FY2024 charges did not repeat in FY2025, directly boosting operating income and creating a flattering YoY comparison that will not recur. This is a one-time tailwind embedded in what the financial analysis treated as sustainable operating improvement.

The QuickBooks Desktop revenue recognition change depresses current-period product revenue by allocating and deferring a previously-unbundled component. This is conservative accounting, not aggressive — it understates current revenue rather than inflating it — but it means Desktop Ecosystem growth rates in FY2025 are not fully comparable to prior periods.

On segment reporting: INTU excludes SBC ($1.97B), acquired intangible amortization ($637M), and significant platform-level customer success and technology costs from segment operating income, recording them in "unallocated corporate items." This is standard practice across large software companies (Salesforce, Adobe, and peers use the same structure), not uniquely aggressive. However, the reported segment margins — GBS at 76%, Consumer at 78% — are not economic margins and should not be used for cross-company valuation. The consolidated GAAP operating margin of 27.1% is the correct reference. Additionally, a structural reorganization effective August 1, 2024 moved $1.4B of GBS costs and $573M of Consumer costs into unallocated corporate items, with prior periods retroactively restated. This means segment margins improved not from business improvement alone but partly from cost reclassification — segment trend analysis across years must account for this restatement break.

**4. Are there any disclosures that appear incomplete, inconsistent with the financial statements, or that warrant deeper investigation?**
Two items warrant follow-up.

The IRS Direct File program is entirely absent from the MD&A. The legal contingencies section addresses past FTC litigation but the MD&A does not discuss the structural competitive threat posed by the IRS expanding its own free filing system. This is not a disclosure violation — generic competitive and regulatory risk is addressed in the Risk Factors section of Part I — but the silence means the MD&A provides no management commentary on how they're positioning TurboTax against this threat, what the take-up rate is, or how they view the risk to the April quarter concentration. This warrants direct examination in the Earnings Calls phase.

Effective August 1, 2025, INTU merged the Consumer, Credit Karma, and ProTax segments into a single "Consumer" business. This is disclosed in the 10-K. The consequence is that all historical segment analysis — the Credit Karma +32% inflection, the Consumer margin trend — becomes non-comparable in FY2026 reporting. The Earnings Calls phase should note this reorganization and assess whether management's consolidated view of the "Consumer" segment improves or obscures the Credit Karma thesis.

**Footnotes & MD&A Summary**
The footnotes confirm INTU's capital lightness ($637M of ~$809M D&A is acquired intangible amortization, only $172M is true depreciation) and validate the SBC analysis ($1.97B, 91% time-based RSUs, structurally recurring across R&D and S&M). However, three findings meaningfully revise or complicate the financial analysis. First, the reported 36% operating income growth and 2.28x operating leverage are partly artifacts of a $208M YoY restructuring reversal — underlying improvement is real but overstated by roughly 8-10 operating income points in the FY2025 comparison. Second, goodwill of $13.98B and net acquired intangibles of $5.30B represent ~57% of total assets; Debt/Tangible Assets is approximately 50%+, a materially weaker picture than the 22% headline ratio, though Debt/OCF of 1.08x remains the correct operating leverage metric. Third, the August 1, 2024 segment reorganization reclassified $2B+ in costs into unallocated items, retroactively inflating segment margin trends. On the positive side, Credit Karma's 32% revenue recovery and the 20% Online Ecosystem growth rate are confirmatory signals for the LOSER thesis that were absent from the financial analysis. The IRS Direct File threat and the August 2025 segment consolidation both require Earnings Calls investigation.

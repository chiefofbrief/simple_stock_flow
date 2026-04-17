# Price & Earnings Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided price and earnings data for **{TICKER}** and produce a single, integrated report.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:

**Guidelines**
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.

**Context**
- `context_markets.md` — Current macro conditions, market sentiment, and prevailing narratives. Use this to calibrate conservatism: an elevated-risk or split-sentiment environment raises the bar for TAILWIND passes and warrants additional scrutiny of reversion targets for LOSER candidates.
- `context_sectors.md` *(TAILWIND-tagged tickers only)* — Sector-level dynamics and signals. Use this to assess whether the sector tailwind is intact, accelerating, or fading — directly informs whether the tailwind thesis is still valid and whether it is already priced in.
- `Peter's Digest/Screening/Screening_{DATE}.md` — The stock's classification tags and original flagging context. If running outside the daily screening flow, context will be provided directly.

**Data**
- `Data/screening/Price_Data_{DATE}.txt` — Historical performance, volatility, drawdown, and trend metrics for {TICKER}.
- `Data/screening/Earnings_{DATE}.txt` — P/E ratios, earnings history, growth rates, and forward estimates for {TICKER}.

**Data Check:** Confirm both `Data/screening/Price_Data_{DATE}.txt` and `Data/screening/Earnings_{DATE}.txt` exist and contain entries for the tickers you intend to analyze. If either file is missing, empty, or does not cover all expected tickers, stop and alert the user before proceeding. Otherwise, proceed to Step 2.

---

**Batch Grouping:** If the ticker list contains both `[LOSER]` and `[TAILWIND]` tickers, process them in two separate passes — do not interleave types or combine them into a single response.

1. **Pass 1:** Analyze all `[LOSER]` tickers. Present the full analysis, then **STOP and ask for approval before proceeding to Pass 2.**
2. **Pass 2:** After explicit approval, analyze all `[TAILWIND]` tickers.

If the list contains only one type, this does not apply.

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Evaluate the data against the questions in the Output Format below.
- All insights must leverage the provided data. Explicitly specify which metrics led to your conclusion.
- For conditional sections, confirm the stock's tags from `Peter's Digest/Screening/Screening_{DATE}.md`, apply the relevant conditional:
  - **Question 4** applies to `[LOSER]`-tagged tickers only. If not tagged `[LOSER]`, state "N/A" and skip.
  - **Question 5** applies to `[TAILWIND]`-tagged tickers only. If not tagged `[TAILWIND]`, state "N/A" and skip.
  - **Question 8** applies to `[LOSER]`-tagged tickers only. If not tagged `[LOSER]`, state "N/A" and skip.
  - **Question 9** applies to `[TAILWIND]`-tagged tickers only. If not tagged `[TAILWIND]`, state "N/A" and skip.

**Before applying the framework to each ticker, assess whether the earnings data is reliable enough to support P/E-based analysis.** Flag explicitly if: the company has no P/E (pre-profitability), has been profitable for fewer than 4 quarters, or has a CV high enough to suggest the earnings history is too unstable to anchor a valuation. Where data reliability is low, reduce analytical confidence accordingly and note it prominently in the Status Summary.

### Deliverable

**Questions:**
1. **Data Check:** Have all metrics been sourced directly from `Price_Data_{DATE}.txt` and `Earnings_{DATE}.txt` — no outside data introduced?
2. **Earnings Reliability Check:** Has the reliability of the earnings data been assessed and flagged where relevant (pre-profitability, fewer than 4 quarters of data, high CV)?
3. **Conditional Check:** Has the correct conditional logic been applied based on the stock's tags from `Peter's Digest/Screening/Screening_{DATE}.md`?
4. **Metrics Check:** Does each answer explicitly specify which metrics led to the conclusion?
5. **Summary Check:** Does the Status & Summary accurately reflect the analysis findings?
6. **Consistency Check:** Do the verdicts hold up when compared across the batch? If two tickers share similar characteristics but received different verdicts, is the difference explicitly justified?

**Output Format:**

#### {TICKER} — {Classification} ({PASS / FILTERED})

**1. How does the current price compare to historical levels?**
[Answer using specific metrics]

**2. What are the long-term price and earnings trends and volatility? (past 5 years)**
[Answer using specific metrics]

**3. What are the short-term price and earnings trends and volatility? (past 12 months)**
[Answer using specific metrics]

**4. `[LOSER]` Is the current price drop an anomaly or consistent with the long-term trend?**
[Answer using specific metrics]

**5. `[TAILWIND]` Is the stock trading near the top of its 52-week range or has it surged significantly in recent months, suggesting the tailwind may already be priced in?**
[Answer using specific metrics]

**6. How do the upcoming earnings estimates compare to the company's past performance, and what does this signal about near-term analyst sentiment?**
[Answer using specific metrics]

> **Pre-profitability note:** For companies with negative EPS, a positive Forward Delta means expected narrowing of losses — not expected profit. Frame it accordingly and explicitly note the company remains cash-flow negative.

**7. Is the current P/E under 20x (strong floor), 20–30x (reasonable floor), or over 30x (caution — no meaningful floor)?**
[Answer using specific metrics]

> **Anchoring warning:** A relative P/E discount (e.g., "cheaper than its historical average") does not constitute an absolute floor. Apply the rubric above based on the *absolute* P/E level only.

**8. `[LOSER]` Is the price decline tracking real fundamental deterioration, or is the market overreacting to a healthy business?**
[Answer using specific metrics]

> **Interpretation guidance:** A negative correlation supports an overreaction thesis — price falling while earnings rise. A positive correlation supports a rational repricing thesis — price tracking fundamental deterioration. Address the direction and strength of the correlation explicitly in the Status Summary.

**9. `[TAILWIND]` Does what the company is currently earning justify the current price — and if not, does the earnings trend suggest it will?**
[Answer using specific metrics]

**Status & Summary**
**[PASS / FILTERED].** [A concise paragraph summarizing the findings and rationale. Include one sentence on how current market conditions from `context_markets.md` affect the confidence level of this verdict.]

- **Action:** Ask: *"Do you approve this recommendation? Should I commit this analysis to the screening file?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval, update `Peter's Digest/Screening/Screening_{DATE}.md` as follows:

**Determine the target section:**
- If the ticker is present in the Candidates section of `Peter's Digest/Screening/Screening_{DATE}.md`, write to the **Screening Results** section.
- Otherwise, write to a `## Standalone` section at the bottom of the file. Create the file and/or section if they do not exist.

**For each ticker:**
1. In the Candidates section (or Standalone section), set `**Price & Earnings:**` to PASS or FILTERED.
2. In the Screening Results (or Standalone) section, append the full analysis output — all questions, answers, and Status & Summary — verbatim.
3. Set the Overall verdict.

**After all tickers in the batch are committed:**
4. Update the Status section: `Price & Earnings: Complete`.
5. Present a final summary for all tickers screened — both passed and filtered. For each, provide a brief recommendation on next steps (PIPELINE, WATCHLIST, or DROP) with one-sentence rationale. Then ask the user to decide:

```
Screening complete. Recommended next steps:

- TICKER1: PIPELINE — [rationale]
- TICKER2: WATCHLIST — [rationale]
- TICKER3: DROP — [rationale]

For each ticker you want to keep, please confirm: PIPELINE, WATCHLIST, or DROP.
Run prompt_screening_completion.md for any ticker going to PIPELINE or WATCHLIST.
```

**STOP. Wait for user decisions before proceeding.**

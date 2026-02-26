# Context Configuration
- **Target Ticker:** {TICKER} (or List of Tickers)
- **Required Data:** `Data/screening/Earnings_{DATE}.txt` (Run: `python Scripts/earnings.py {TICKER} [TICKER...]`)
- **Required Context:** 
    - `Stock_Tracker.md` (Check Tags)
    - `Discovery_Context.md` (Read to see if it mentions why the stock is being screened)
- **Output:**
    - Append concise summary to `Stock_Tracker.md` under `### {TICKER} > **Earnings**`.
    - Append the full analysis report (Questions + Summary) to the end of the input data file (`Data/screening/Earnings_{DATE}.txt`).

# Earnings Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided earnings and valuation data and produce a concise, insightful report.

## Input Data
You will be provided with:
1.  **Ticker Symbol**: The stock symbol.
2.  **Valuation & Earnings Metrics**:
    *   `current_pe`: Current P/E Ratio.
    *   `pe_1y`, `pe_3y`, `pe_5y`, `pe_avg`: Historical P/E ratios (1, 3, 5 years ago, and 5yr Average).
    *   `vs_1y`, `vs_3y`, `vs_5y`, `vs_avg`: Percentage difference between Current P/E and historical levels.
    *   `eps_cagr`: 5-Year Annual EPS Compound Annual Growth Rate.
    *   `stability`: Earnings Stability score (Coefficient of Variation of Annual EPS).
    *   `corr_1y`: Correlation coefficient between Price and Earnings over the last 12 months.
    *   `next_est`: Next Quarter Earnings Estimate.
    *   `fwd_delta`: Difference between the Next Estimate and the Last Reported Actual EPS.
    *   `history`: A list containing Annual TTM EPS blocks (5 years) and recent Quarterly (Estimate vs Actual) performance.

## Analysis Guidelines

Analyze the data to answer the following questions. **Crucially, all insights must leverage the provided data. You must explicitly specify which metrics led to your conclusion or contributed to your answer.**

## Output Format

Please structure your response exactly as follows:

### {TICKER} Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
[Answer using specific metrics]

**2. What is the long-term earnings trend and volatility? (past 5 years)**
[Answer using specific metrics]

**3. What is the short-term earnings trend and volatility? (past 12 months)**
[Answer using specific metrics]

**4. What is the correlation between price and earnings?**
[Answer using specific metrics]

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
[Answer using specific metrics]

**6. FOR [LOSER]-TAGGED TICKERS ONLY: Earnings vs Price Trajectory**
*(Check `Stock_Tracker.md`. If the stock's Tags column does not contain `[LOSER]`, simply state "N/A - Not a recent loser" for this section and skip the questions below.)*
*   **Are earnings decreasing along with the price?**
    [Answer using specific metrics]

---
**Status Update (Proposed PASS/FILTERED)**
[PASS / FILTERED]. Provide a 1-sentence rationale based on the earnings analysis.

---
**Earnings/Valuation Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Stock Tracker.]

---
**Instructions for the Assistant:**
1. **Wait for Approval:** Present this complete analysis and the proposed status update to the user.
2. **Explicit Ask:** You **MUST** ask: *"Do you approve this recommendation? Should I update the Stock Tracker and append this analysis to the data file?"*
3. **Write on Approval:** Upon approval:
    - Append the concise **Earnings/Valuation Summary** to `Stock_Tracker.md`.
    - Append this **full analysis report** (including Q&A and Status Update) to the end of the source data file in `Data/screening/`.

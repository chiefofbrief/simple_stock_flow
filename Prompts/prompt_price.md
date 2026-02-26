# Context Configuration
- **Target Ticker:** {TICKER} (or List of Tickers)
- **Required Data:** `Data/screening/Price_Data_{DATE}.txt` (Run: `python Scripts/price.py {TICKER} [TICKER...]`)
- **Required Context:** 
    - `Stock_Tracker.md` (Check Tags)
    - `Discovery_Context.md` (Read to see if it mentions why the stock is being screened)
- **Output:**
    - Append concise summary to `Stock_Tracker.md` under `### {TICKER} > **Price**`.
    - Append the full analysis report (Questions + Summary) to the end of the input data file (`Data/screening/Price_Data_{DATE}.txt`).

# Price Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided stock price data and produce a concise, insightful report.

## Input Data
You will be provided with:
1.  **Ticker Symbol**: The stock symbol.
2.  **Price Metrics**:
    *   `current_price`: The latest closing price.
    *   `vs_1yr`, `vs_3yr`, `vs_5yr`: Percentage change vs historical dates.
    *   `52w_high`, `52w_low`, `52w_position`: Context within the last year's range.
    *   `cagr_5yr`: Compound Annual Growth Rate over 5 years.
    *   `cv`: Coefficient of Variation (volatility metric).
    *   `z_score`: Standard deviations of the most recent monthly return vs history.
    *   `max_drawdown_5yr`: The largest peak-to-trough drop in the last 5 years.
    *   `drop_vs_max_drawdown`: The ratio of the current recent drop to the max drawdown.
    *   `avg_price_1yr`: Average price over the last 12 months.
    *   `upside_if_revert`: Potential upside if price returns to the 1-year average.
    *   `recent_trend`: A list of the last 12 monthly closing prices.

## Analysis Guidelines

Analyze the data to answer the following questions. **Crucially, all insights must leverage the provided data. You must explicitly specify which metrics led to your conclusion or contributed to your answer.**

## Output Format

Please structure your response exactly as follows:

### {TICKER} Price Analysis

**1. How does the current price compare to historical levels?**
[Answer using specific metrics]

**2. What is the long-term price trend and volatility? (past 5 years)**
[Answer using specific metrics]

**3. What is the short-term price trend and volatility? (past 12 months)**
[Answer using specific metrics]

**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*(Check `Stock_Tracker.md`. If the stock's Tags column does not contain `[LOSER]`, simply state "N/A - Not a recent loser" for this section and skip the questions below.)*
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    [Answer using specific metrics]
*   **What is the delta between the current price and its average over the past 12 months?**
    [Answer using specific metrics]

---
**Status Update (Proposed PASS/FILTERED)**
[PASS / FILTERED]. Provide a 1-sentence rationale based on the price analysis.

---
**Price Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Stock Tracker.]

---
**Instructions for the Assistant:**
1. **Wait for Approval:** Present this complete analysis and the proposed status update to the user.
2. **Explicit Ask:** You **MUST** ask: *"Do you approve this recommendation? Should I update the Stock Tracker and append this analysis to the data file?"*
3. **Write on Approval:** Upon approval:
    - Append the concise **Price Summary** to `Stock_Tracker.md`.
    - Append this **full analysis report** (including Q&A and Status Update) to the end of the source data file in `Data/screening/`.

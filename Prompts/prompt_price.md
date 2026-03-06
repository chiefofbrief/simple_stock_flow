# Price Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided stock price data for **{TICKER}** and produce a concise, insightful report.

## Active Workflow: Sequential Steps
Follow these steps exactly:

1. **Gather Data & Context (READ FIRST):**
   - **Philosophy:** Read `GEMINI.md` to review the foundational Analysis Philosophy & Guidelines.
   - **Quantitative Data:** Read `Data/screening/Price_Data_{DATE}.txt` to extract the historical performance, volatility, drawdown, and trend metrics for {TICKER}.
   - **Categorization:** Read `Stock_Tracker.md` to identify the stock's current Tags (e.g., `[LOSER]`, `[TAILWIND]`, `[AI]`).
   - **Catalyst:** Read `Discovery_Context.md` to understand the original reason for screening this stock.

2. **Analyze & Generate Report (In Chat):**
   - Evaluate the data against the **Analysis Guidelines** below.
   - Produce the analysis report in the chat window using the exact structure in the **Output Format** section.
   - End your report with your proposed status (PASS/FILTERED) and the mandatory question: *"Do you approve this recommendation? Should I update the Stock Tracker and append this analysis to the data file?"*

3. **Commit Changes (POST-APPROVAL ONLY):**
   - Only after receiving explicit user approval (e.g., "yes", "go ahead"):
     - **Stock Tracker:** Update `Stock_Tracker.md` by strictly following the **Tracker Update Instructions** at the top of that file.
     - **Data File:** Append the **full analysis report** (including Q&A and Status Update) to the end of `Data/screening/Price_Data_{DATE}.txt`.

## Analysis Guidelines
Analyze the data using the following questions and structure your response exactly as specified. Refer to the **Examples** section below, specifically the subsection matching the stock's tags, to inform your analysis. **Crucially, all insights must leverage the provided data; you must explicitly specify which metrics led to your conclusion.**

### Output Format

#### {TICKER} Price Analysis

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

**5. FOR [TAILWIND]-TAGGED TICKERS ONLY: Pricing of the Tailwind**
*(Check `Stock_Tracker.md`. If the stock's Tags column does not contain `[TAILWIND]`, simply state "N/A - Not a tailwind stock" for this section and skip the questions below.)*
*   **Has the stock experienced a recent, significant upward surge or is it trading near historical highs, suggesting the anticipated improvement may already be fully priced in?**
    [Answer using specific metrics]

---
**Status & Price Summary**
**[PASS / FILTERED].** [A concise paragraph summarizing the findings and rationale. This text will be copied to the Stock Tracker.]

## Examples

### LOSERS

#### AAPL Price Analysis
**1. How does the current price compare to historical levels?**
Current price $264.57 is up +10% vs 1Y and +124% vs 5Y. It sits at 80% of its 52-week range ($200.24 - $278.59).
**2. What is the long-term price trend and volatility? (past 5 years)**
Excellent 5Y CAGR of +16.9% with moderate volatility (CV 0.24). The stock is a long-term compounder.
**3. What is the short-term price trend and volatility? (past 12 months)**
Short-term stability has returned; the price is flat MoM (+0.1%) and has fully recovered from the 5.4% dip in May 2025.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    There is no significant recent drop. The stock is currently just 5% off its all-time highs, whereas historical drawdowns for AAPL have exceeded 30%.
*   **What is the delta between the current price and its average over the past 12 months?**
    The price is 8% *above* its 12-month average (Revert↑ -8%).
---
**Status & Price Summary**
**FILTERED.** Recovered Loser. AAPL is a long-term compounder (+16.9% 5Y CAGR) that has fully recovered from its recent dip, trading at 80% of its 52-week high ($264 vs $278 peak). It currently sits 8% above its 12-month average price, negating the 'temporary loser' thesis and offering no margin of safety for reversion.

#### ABCL Price Analysis
**1. How does the current price compare to historical levels?**
Price $3.56 is up +37% vs 1Y but down -91% vs 5Y.
**2. What is the long-term price trend and volatility? (past 5 years)**
Structural destruction: 5Y CAGR is -36.7%. Extreme volatility (CV 0.88) and a -91% total loss of value indicate a "broken" company.
**3. What is the short-term price trend and volatility? (past 12 months)**
The stock is flat MoM (-1.4%) but has failed to reclaim its level from Nov 2025 when it collapsed 32%.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The current price reflects a permanent 91% drawdown. The recent 1% monthly fluctuation is noise within a terminal decline.
*   **What is the delta between the current price and its average over the past 12 months?**
    The price is essentially at its average (Revert↑ +6%).
---
**Status & Price Summary**
**FILTERED.** Permanent Loser. ABCL is in a terminal downtrend, down 91% over 5 years with a catastrophic -36.7% CAGR. While up 37% YoY, it remains trapped near historical lows (36% of 52w range) and lacks the stable long-term base required for a temporary mispricing thesis; recent volatility is noise within a structural decline.

#### ABSI Price Analysis
**1. How does the current price compare to historical levels?**
Price $2.69 is down -30% vs 1Y and -48% vs 2Y. It sits at 21% of its 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Severe long-term weakness: 5Y CAGR of -39.2% with extreme volatility (CV 0.98).
**3. What is the short-term price trend and volatility? (past 12 months)**
Consistent downward pressure, with MoM declines in Jan (-14%) and Feb (-8%).
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The stock is currently at its lowest level in history. The recent 30% YoY drop is just the latest leg in a permanent 5-year value destruction.
*   **What is the delta between the current price and its average over the past 12 months?**
    Trades 11% below its 12-month average.
---
**Status & Price Summary**
**FILTERED.** Permanent Loser. ABSI is experiencing persistent value destruction, down 30% YoY and 48% over 2 years (-39.2% 5Y CAGR). Trading at just 21% of its 52-week range and 11% below its annual average, the stock sits at all-time lows with no established support level or stable history to justify a reversion bet.

#### ADBE Price Analysis
**1. How does the current price compare to historical levels?**
Price $259.21 is down -41% vs 1Y and -44% vs 5Y. It is at a deep 7% of its 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Historically stable giant now seeing an anomaly. 5Y CAGR is -10.5%, reflecting the recent violent drop from previously high valuations.
**3. What is the short-term price trend and volatility? (past 12 months)**
Violent capitulation: Down -16% in Jan and -10.5% in Feb 2026.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The current 41% drop is one of the most significant in ADBE's modern history, rivaling only the 2008 and 2022 corrections. This is a 2% "Drop/MaxDD" signal only because the stock is currently *at* its max drawdown.
*   **What is the delta between the current price and its average over the past 12 months?**
    The stock trades at a massive 31% discount to its 12-month average.
---
**Status & Price Summary**
**PASS.** Temporary Loser. ADBE is a high-quality incumbent in a violent 'bust' cycle, down 41% YoY and trading at just 7% of its 52-week range ($259 vs $415 peak). Despite its stable history, it is now at 5-year lows. The 31% discount to its 1-year average price ($375) creates a significant margin of safety if its core enterprise moat remains intact.

#### ARM Price Analysis
**1. How does the current price compare to historical levels?**
Price $122.42 is down -7% vs 1Y. It sits at 41% of its 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Extremely high growth: 5Y CAGR of +37.8%. The company is a fundamental winner.
**3. What is the short-term price trend and volatility? (past 12 months)**
Highly volatile (+21% recovery in Feb after a -19% drop in Dec). Current price is stable.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The current 7% YoY dip is minor compared to ARM's historical volatility; it represents just 7% of its maximum 5-year drawdown.
*   **What is the delta between the current price and its average over the past 12 months?**
    The price is 8% below its 12-month average.
---
**Status & Price Summary**
**PASS.** Quality Dip. ARM is a dominant growth winner (+37.8% 5Y CAGR) currently undergoing a minor correction, down 7% YoY and trading at 41% of its 52-week range. The current price ($122) represents a rare 8% discount to its 12-month average, offering a high-quality entry point within a strong structural uptrend.

#### CLVT Price Analysis
**1. How does the current price compare to historical levels?**
Price $2.38 is down -45% vs 1Y and -90% vs 5Y. Sits at 23% of 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Terminal destruction: 5Y CAGR is -35.4% with extreme volatility (CV 0.70). The stock has been in a constant slide for half a decade.
**3. What is the short-term price trend and volatility? (past 12 months)**
Downward momentum continues: -20% in Jan and -13% in Feb 2026.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The current price is at an all-time low, representing a near-total wipeout (-90%).
*   **What is the delta between the current price and its average over the past 12 months?**
    Trades at a 49% discount to its 12-month average.
---
**Status & Price Summary**
**FILTERED.** Permanent Loser. CLVT is down 90% from 5-year highs with a terminal -35.4% CAGR. Although it trades at a massive 49% discount to its 1-year average, this statistical 'upside' is overshadowed by 5 years of consistent value destruction; the stock remains near all-time lows (23% of 52w range) with no signs of structural stabilization.

#### CRM Price Analysis
**1. How does the current price compare to historical levels?**
Price $191.89 is down -35% vs 1Y and -10% vs 5Y. Sits at 14% of 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Stable large-cap history: 5Y CAGR is essentially flat (-2.1%) with low volatility (CV 0.21).
**3. What is the short-term price trend and volatility? (past 12 months)**
Sharp recent capitulation: Down -19.9% in Jan and -8.2% in Feb 2026.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The recent 35% YoY drop is a significant anomaly for CRM, representing a deep discount relative to its historically steady price action.
*   **What is the delta between the current price and its average over the past 12 months?**
    Trades 26% below its 12-month average.
---
**Status & Price Summary**
**PASS.** Temporary Loser. CRM is a stable software giant experiencing a sharp YoY capitulation, down 35% and trading at just 14% of its 52-week range. Despite a flat long-term CAGR (-2.1%), the current dislocation is anomalous; trading at a 26% discount to its 1-year average ($191 vs $259 avg) provides a significant margin of safety for a high-quality incumbent.

#### CRWD Price Analysis
**1. How does the current price compare to historical levels?**
Price $381.07 is down -2% vs 1Y but up +76% vs 5Y. Sits at 31% of its 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Strong long-term performer: 5Y CAGR of +11.6%.
**3. What is the short-term price trend and volatility? (past 12 months)**
Sudden correction: Down -15.7% in Feb 2026 after a period of high valuation.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    The current 15% monthly drop is sharp but within CRWD's historical volatility range. The stock is still near its 5-year highs.
*   **What is the delta between the current price and its average over the past 12 months?**
    Trades 20% below its 12-month average.
---
**Status & Price Summary**
**PASS.** Growth Correction. CRWD is a high-quality performer (+11.6% 5Y CAGR) in a sudden 15.7% monthly correction, now trading at 31% of its 52-week range. The current price ($381) sits 20% below its 12-month average, representing a significant short-term dislocation for a stock that remains in a structural long-term uptrend.

#### CSCO Price Analysis
**1. How does the current price compare to historical levels?**
Price $78.31 is up +25% vs 1Y and +102% vs 5Y. Sits at 73% of its 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Steady compounder: 5Y CAGR of +14.5% with very low volatility (CV 0.21).
**3. What is the short-term price trend and volatility? (past 12 months)**
Upward momentum: +10% in June and +7.5% in Oct. Stable (+1.5%) in the last month.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    There is no current drop; the stock is up 25% on the year and is trading near historical highs.
*   **What is the delta between the current price and its average over the past 12 months?**
    Trades 9% *above* its 12-month average (Revert↑ -9%).
---
**Status & Price Summary**
**FILTERED.** Recovered Loser. CSCO is a steady compounder (+14.5% 5Y CAGR) that has fully absorbed its recent 'AI tax' margin narrative, trading at 73% of its 52-week high ($78 vs $56 low). It now trades at a 9% premium to its 12-month average, negating the 'loser' thesis as the previous sentiment-driven discount has entirely evaporated.

#### CVNA Price Analysis
**1. How does the current price compare to historical levels?**
Price $322.92 is up +39% vs 1Y and +14% vs 5Y. Sits at 52% of its 52-week range.
**2. What is the long-term price trend and volatility? (past 5 years)**
Weak long-term growth (+2.6% CAGR) with extreme volatility (CV 0.78).
**3. What is the short-term price trend and volatility? (past 12 months)**
Mixed; recovered from a 18% drop in Oct but fell -16.7% in late Feb 2026.
**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
*   **How does the current price drop compare to the biggest drawdowns in the stock's history?**
    CVNA is famous for its 95%+ drawdown in 2022. The recent 16% dip is minor (3% of max drawdown) by comparison.
*   **What is the delta between the current price and its average over the past 12 months?**
    Trades 9% below its 12-month average.
---
**Status & Price Summary**
**FILTERED.** Recovered Loser. CVNA is a highly volatile stock (+2.6% 5Y CAGR) that has recovered 39% YoY, currently trading near the midpoint (52%) of its 52-week range. While it trades at a 9% discount to its 1-year average, it lacks the deep 'temporary loser' profile of more stable peers; the current level is far removed from its catastrophic 2022 lows where the true margin of safety existed.

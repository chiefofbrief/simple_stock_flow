# Price Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided stock price data for **{TICKER}** and produce a concise, insightful report.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- `context_markets.md` — Current macro conditions, market sentiment, and prevailing narratives. Use this to calibrate conservatism: an elevated-risk or split-sentiment environment raises the bar for TAILWIND passes and warrants additional scrutiny of reversion targets for LOSER candidates.
- `Screening_{DATE}.md` — The stock's classification tags and original flagging context. If running outside the daily screening flow, context will be provided directly.
- `Data/screening/Price_Data_{DATE}.txt` — Historical performance, volatility, drawdown, and trend metrics for {TICKER}.

**Data Check:** Confirm `Data/screening/Price_Data_{DATE}.txt` exists and contains entries for the tickers you intend to analyze. If the file is missing, empty, or does not cover all expected tickers, stop and alert the user before proceeding.

**Existing Content Check:** If `Data/screening/Price_Data_{DATE}.txt` already contains prior analyses (from an earlier batch), do not overwrite it. Rename the existing file (e.g., `Price_Data_{DATE}_Batch1.txt`) before the script is run again for a new batch.

**STOP. Wait for user approval before proceeding to Step 2.**

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
- For conditional sections, confirm the stock's tags from `Screening_{DATE}.md`, apply the relevant conditional, and refer to the matching example below:
  - **Question 4** applies to `[LOSER]`-tagged tickers only. If not tagged `[LOSER]`, state "N/A - Not a recent loser" and skip.
  - **Question 5** applies to `[TAILWIND]`-tagged tickers only. If not tagged `[TAILWIND]`, state "N/A - Not a tailwind stock" and skip.

### Example Output

#### ADBE — Temporary Loser (PASS)

**1. How does the current price compare to historical levels?**
Price $259.21 is down -41% vs 1Y and -44% vs 5Y. It is at a deep 7% of its 52-week range.

**2. What is the long-term price trend and volatility? (past 5 years)**
Historically stable giant now seeing an anomaly. 5Y CAGR is -10.5%, reflecting the recent violent drop from previously high valuations.

**3. What is the short-term price trend and volatility? (past 12 months)**
Violent capitulation: Down -16% in Jan and -10.5% in Feb 2026.

**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
- **How does the current price drop compare to historical drawdowns and volatility?**
The current 41% drop is one of the most significant in ADBE's modern history, rivaling only the 2008 and 2022 corrections.
- **Is the current price drop an anomaly or consistent with the long-term trend?**
Anomalous. ADBE is a historically stable giant; the recent violent capitulation contradicts its long-term growth profile.
- **Is the 12-month average a reliable target for reversion, or is the statistical 'upside' a mathematical mirage?**
Reliable target. The 31% discount to its 12-month average creates a genuine margin of safety for a historically high-quality business.

**Status & Price Summary**
**PASS.** Temporary Loser. ADBE is a high-quality incumbent in a violent 'bust' cycle, down 41% YoY and trading at just 7% of its 52-week range ($259 vs $415 peak). Despite its stable history, it is now at 5-year lows. The 31% discount to its 1-year average price ($375) creates a significant margin of safety if its core enterprise moat remains intact.

#### PINS — Permanent Loser (FILTERED)

**1. How does the current price compare to historical levels?**
Current price $19.45 is down -47% vs 1Y and down -76% vs 5Y. It sits at 22% of its 52-week range.

**2. What is the long-term price trend and volatility? (past 5 years)**
Severe structural decline: 5Y CAGR is -24.1% with high volatility (CV 0.42).

**3. What is the short-term price trend and volatility? (past 12 months)**
Extremely volatile. The stock suffered sharp drops in Nov (-21.1%), Jan (-14.5%), and Feb (-22.6%) before a recent 13.5% bounce in March.

**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
- **How does the current price drop compare to historical drawdowns and volatility?**
The current price reflects a 76% drawdown from 5-year highs. The recent ~40% plunge over the last quarter is sharp even for PINS.
- **Is the current price drop an anomaly or consistent with the long-term trend?**
Consistent. The stock is in a terminal structural slide (-28.5% 5Y CAGR).
- **Is the 12-month average a reliable target for reversion, or is the statistical 'upside' a mathematical mirage?**
Mathematical mirage. Despite a massive statistical discount to its annual mean, the terminal 5-year downtrend (-24.1% CAGR, -76% total loss) indicates structural impairment rather than a temporary sentiment-driven dip.

**Status & Price Summary**
**FILTERED.** Permanent Loser. Despite a massive statistical discount to its annual mean, the terminal 5-year downtrend (-24.1% CAGR, -76% total loss) indicates structural impairment rather than a temporary sentiment-driven dip. The stock lacks the stable historical base required to justify a "mean reversion" thesis.

#### KD — Extreme Dislocation (PASS)

**1. How does the current price compare to historical levels?**
Current price $13.12 is down -66% vs 1Y and -40% vs 2Y. It sits at just 9% of its 52-week range.

**2. What is the long-term price trend and volatility? (past 5 years)**
Highly destructive long-term trend (since spinoff): CAGR of -17.7% with high volatility (CV 0.43).

**3. What is the short-term price trend and volatility? (past 12 months)**
Violent recent capitulation. The stock was relatively stable in the mid-$20s before suffering consecutive severe drops of -13.4% in Jan and an incredible -46.4% in Feb 2026.

**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
- **How does the current price drop compare to historical drawdowns and volatility?**
The current collapse is extreme and anomalous (Z-score +0.4 for the recent drop speed) driving the stock to its historical floor.
- **Is the current price drop an anomaly or consistent with the long-term trend?**
Anomalous in its speed and intensity (-46.4% monthly drop) despite the negative long-term trend.
- **Is the 12-month average a reliable target for reversion, or is the statistical 'upside' a mathematical mirage?**
Reliable target. The stock trades at a staggering 54% discount to its 12-month average, requiring a 118% gain just to revert to the mean.

**Status & Price Summary**
**PASS.** Extreme Dislocation. KD (Kyndryl) has suffered a catastrophic, sentiment-driven collapse, down 66% YoY and trading at absolute lows (9% of 52w range) following a massive 46% plunge in February due to executive exits and guidance cuts. This "perfect storm" has created a 54% discount to its 1-year mean (requiring a +118% reversion), making it a prime candidate for a deep dive to see if the core FCF remains intact beneath the panic.

### Deliverable

**Questions:**
1. **Data Check:** Have all metrics been sourced directly from `Price_Data_{DATE}.txt` — no outside data introduced?
2. **Conditional Check:** Has the correct conditional logic been applied based on the stock's tags from `Screening_{DATE}.md`?
3. **Metrics Check:** Does each answer explicitly specify which metrics led to the conclusion?
4. **Summary Check:** Does the Status & Price Summary accurately reflect the analysis findings?

**Output Format:**

#### {TICKER} Price Analysis

**1. How does the current price compare to historical levels?**
[Answer using specific metrics]

**2. What is the long-term price trend and volatility? (past 5 years)**
[Answer using specific metrics]

**3. What is the short-term price trend and volatility? (past 12 months)**
[Answer using specific metrics]

**4. FOR [LOSER]-TAGGED TICKERS ONLY: Significant recent drops**
- **How does the current price drop compare to historical drawdowns and volatility?**
  [Answer using specific metrics]
- **Is the current price drop an anomaly or consistent with the long-term trend?**
  [Answer using specific metrics]
- **Is the 12-month average a reliable target for reversion, or is the statistical 'upside' a mathematical mirage?**
  [Answer using specific metrics]

**5. FOR [TAILWIND]-TAGGED TICKERS ONLY: Pricing of the Tailwind**
- **Has the stock experienced a recent, significant upward surge or is it trading near historical highs, suggesting the anticipated improvement may already be fully priced in?**
  [Answer using specific metrics]

**Status & Price Summary**
**[PASS / FILTERED].** [A concise paragraph summarizing the findings and rationale. Include one sentence on how current market conditions from `context_markets.md` affect the confidence level of this verdict — e.g., whether broad market risk raises or lowers the reliability of a reversion target, or whether prevailing sentiment supports or undermines the tailwind thesis.]

- **Action:** Ask: *"Do you approve this recommendation? Should I append this analysis to the data file?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval, append the full analysis output from Step 2 — including all questions, answers, and the Status & Price Summary — verbatim to the end of `Data/screening/Price_Data_{DATE}.txt`.

**STOP. Wait for user approval before committing.**

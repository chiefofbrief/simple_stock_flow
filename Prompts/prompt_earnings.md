# Earnings Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided earnings and valuation data for **{TICKER}** and produce a concise, insightful report.

---

## Step 1: Gather Context

### Mode
This prompt operates in one of two modes, set at the start of the conversation:
- **Discovery Mode:** Tickers have not yet been added to the tracker. Read tags and context from `Discovery_{DATE}.md` instead of `Stock_Tracker.md` and `Discovery_Context.md`. Skip all tracker updates in Step 3.
- **Standalone Mode:** Default behavior. Read tags and context from `Stock_Tracker.md` and `Discovery_Context.md`. Run Step 3 as written.

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- **Discovery Mode:** `Discovery_{DATE}.md` — The stock's current Tags and original reason for screening this stock.
- **Standalone Mode:** `Stock_Tracker.md` — The stock's current Tags. `Discovery_Context.md` — The original reason for screening this stock.
- `Data/screening/Price_Data_{DATE}.txt` — The prior Price analysis findings for {TICKER}.
- `Data/screening/Earnings_{DATE}.txt` — P/E ratios, earnings history, growth rates, and forward estimates for {TICKER}.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Evaluate the data against the questions in the Output Format below.
- All insights must leverage the provided data. Explicitly specify which metrics led to your conclusion.
- Cross-reference the Price analysis findings from `Price_Data_{DATE}.txt` where relevant — earnings and price context should inform each other.
- For conditional sections, confirm the stock's tags from `Discovery_{DATE}.md` (Discovery Mode) or `Stock_Tracker.md` (Standalone Mode), apply the relevant conditional, and refer to the matching example below:
  - **Question 6** applies to `[LOSER]`-tagged tickers only. If not tagged `[LOSER]`, state "N/A - Not a recent loser" and skip.
  - **Question 7** applies to `[TAILWIND]`-tagged tickers only. If not tagged `[TAILWIND]`, state "N/A - Not a tailwind stock" and skip.

### Example Output

#### ADBE — Temporary Loser (PASS)

**1. How does the current P/E ratio compare to historical levels?**
ADBE is trading at a current P/E of **12.4x**, which is a severe discount across every measurable timeframe: **-48% vs. 1Y ago (23.8x)**, **-48% vs. 3Y ago (23.6x)**, and **-54% vs. its 5-year average (26.9x)**. It is currently at its absolute 5-year valuation floor, down **-74%** from its 47.7x peak.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is exceptionally robust. ADBE has maintained a **5-year EPS CAGR of +16.8%**, growing TTM earnings from $7.82 in 2019 to **$20.95** today. With a stability CV of **0.21**, it is one of the most consistent compounders in the software sector.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term momentum remains high, with **+13.7% TTM growth**. The company has beaten quarterly estimates by an average of **+2.1%** over the last four quarters, with reported quarterly EPS rising from $5.08 to $5.50.

**4. What is the correlation between price and earnings?**
There is a **strong negative correlation of -0.84**. This highlights a massive fundamental divergence: the business is generating record cash while the market is violently contracting its multiple.

**5. How do the upcoming earnings estimates compare to the company's past performance, and what does this signal about near-term analyst sentiment?**
The estimate for 2026-03-12 is **$5.87**, a **+$0.37 Forward Delta** over the last actual. Analysts are modestly optimistic, expecting growth to accelerate slightly — a signal that contradicts the "AI-disruption" panic reflected in the price.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
- **Are earnings decreasing along with the price?**
**No.** TTM earnings have increased **13.7% YoY**, while the stock price has collapsed **41% YoY**. This is a textbook "Temporary Price Dislocation."
- **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
**Strong Floor.** At 12.4x P/E, the absolute valuation provides a deep margin of safety independently of its 50% relative discount.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

**Status & Earnings Summary**
**PASS.** Adobe is a high-conviction candidate for a "Loser" thesis. The current 12.4x P/E is half its historical average, despite a consistent 16.8% earnings CAGR and high stability (0.21 CV). The extreme negative correlation (-0.84) between rising earnings and a falling price creates a massive valuation gap, while consistent earnings beats suggest the enterprise moat remains intact despite retail competition fears.

#### CRWD — Growth Stall (FILTERED)

**1. How does the current P/E ratio compare to historical levels?**
At **101.9x**, CRWD's P/E is actually **+3% higher than 1Y ago (99.2x)** and **+30% higher than 3Y ago (78.4x)**. While it is down from its 800x "glamour" peak, it is becoming *more* expensive relative to its recent 3-year history even as the price falls.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
Hyper-growth historically (**+70.4% CAGR**), but scaling into maturity. Volatility is high (**0.55 CV**) as the company recently flipped from losses to profits.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
**Fundamental Stall.** TTM earnings have **declined -4.8%** over the last year (from $3.93 to $3.74). This is a critical divergence from its 70% historical CAGR.

**4. What is the correlation between price and earnings?**
Correlation is **-0.07**, meaning the price is essentially moving on noise, decoupled from the recent stagnation in earnings.

**5. How do the upcoming earnings estimates compare to the company's past performance, and what does this signal about near-term analyst sentiment?**
The next estimate is **$1.07**, a small **-$0.05 Forward Delta** vs. the last actual. Analysts are projecting flat growth ahead — a cautious signal that confirms the stall thesis rather than offering a near-term catalyst for recovery.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
- **Are earnings decreasing along with the price?**
**Yes.** TTM earnings dropped **-4.8%** while the price fell **-2%**. This is not a "Temporary Loser" setup; it is a **Growth Stall** where the multiple remains at a dangerous 100x.
- **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
**Caution.** At 101.9x P/E, there is zero absolute Margin of Safety; the price remains speculative despite the "correction."

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

**Status & Earnings Summary**
**FILTERED.** Growth Stall at Premium Price. Buying a 100x P/E stock when earnings are declining (-4.8% TTM) is speculative, not an investment. Unlike ADBE or CRM, where the multiple compressed while earnings rose, CRWD's multiple has actually *expanded* relative to the last 3 years while growth has stalled. There is no Margin of Safety here; the stock is a high-multiple growth trap.

#### QCOM — Dislocated Narrative Play (PASS)

**1. How does the current P/E ratio compare to historical levels?**
QCOM's current P/E is **11.0x**, which is a **-24% below its historical average (14.5x)** and **-22% vs. 1Y ago (14.1x)**. It is trading at its lowest valuation levels in 5 years (down -52% from its 22.8x peak).

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is positive but cyclical, with a **5-year EPS CAGR of +17.7%**. Stability is exceptional with a CV of **0.13**, the lowest in this batch.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term growth is decent at **+11.5% TTM**, with consistent (though small) quarterly beats of **+1% to +4%**.

**4. What is the correlation between price and earnings?**
Correlation is **0.04**, meaning the price and earnings are moving independently. The price is driven by the "Apple defection" and "memory crunch" narratives rather than actual quarterly reports.

**5. How do the upcoming earnings estimates compare to the company's past performance, and what does this signal about near-term analyst sentiment?**
The next estimate of **$2.57** is a massive **-$0.93 Forward Delta** over the last actual ($3.50). Analysts are pricing in a sharp fundamental hit from the loss of major smartphone customers — a pessimistic near-term signal that suggests the market has not yet fully absorbed the revenue cliff, leaving potential value if the 11x floor holds.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
- **Are earnings decreasing along with the price?**
**Yes, looking forward.** While TTM earnings are up, the upcoming quarterly estimate projects a significant drop, which is the specific catalyst for the recent price weakness.
- **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
**Strong Floor.** At 11x P/E, the absolute valuation provides a massive Margin of Safety for a stable incumbent.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

**Status & Earnings Summary**
**PASS.** Dislocated Narrative Play. Qualcomm is a classic "Loser" setup where a known negative catalyst (Apple defection) has triggered a price drop and an earnings downgrade. At 11x P/E, the stock is trading at a significant discount to its historically stable baseline (0.13 CV). We will PASS this to the Financials phase specifically to determine if the 11x multiple provides a sufficient "Margin of Safety floor" to absorb these known losses or if the economic reality of the customer defection is worse than the GAAP estimates suggest.

### Deliverable

**Questions:**
1. **Data Check:** Have all metrics been sourced directly from `Earnings_{DATE}.txt` — no outside data introduced?
2. **Cross-Reference Check:** Have the Price analysis findings been referenced where relevant?
3. **Conditional Check:** Has the correct conditional logic been applied based on the stock's tags?
4. **Metrics Check:** Does each answer explicitly specify which metrics led to the conclusion?
5. **Summary Check:** Does the Status & Earnings Summary accurately reflect the analysis findings?

**Output Format:**

#### {TICKER} Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
[Answer using specific metrics]

**2. What is the long-term earnings trend and volatility? (past 5 years)**
[Answer using specific metrics]

**3. What is the short-term earnings trend and volatility? (past 12 months)**
[Answer using specific metrics]

**4. What is the correlation between price and earnings?**
[Answer using specific metrics]

**5. How do the upcoming earnings estimates compare to the company's past performance, and what does this signal about near-term analyst sentiment?**
[Answer using specific metrics]

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
- **Are earnings decreasing along with the price?**
  [Answer using specific metrics]
- **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
  [Answer using specific metrics]

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
- **Do the forward earnings estimates project a sudden, significant improvement compared to the historical baseline?**
  [Answer using specific metrics]
- **Is the current valuation (P/E) highly elevated, meaning the stock's price is heavily reliant on these future estimates rather than current cash generation?**
  [Answer using specific metrics]

**Status & Earnings Summary**
**[PASS / FILTERED].** [A concise paragraph summarizing the findings and rationale. This text will be copied to the Stock Tracker.]

- **Action:**
  - **Discovery Mode:** Ask: *"Do you approve this recommendation? Should I append this analysis to the data file?"*
  - **Standalone Mode:** Ask: *"Do you approve this recommendation? Should I update the Stock Tracker and append this analysis to the data file?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit Changes

> **Discovery Mode:** Skip the Stock Tracker updates in this step entirely. Only the data file append applies.

### Scope Guidelines
- **Standalone Mode:** Two commits required — update `Stock_Tracker.md` and append the full analysis output to `Data/screening/Earnings_{DATE}.txt`.
- **Discovery Mode:** One commit required — append the full analysis output to `Data/screening/Earnings_{DATE}.txt` only.
- **Display Scope:** Only the **`Stock_Tracker.md` — Ticker Dashboard table**, **Recent Activity Log**, and **Next Steps** are updated in this step. Trade Tracker is not touched.
- **Batch Handling:** If processing multiple batches on the same date, rename previous data files (e.g., `Earnings_{DATE}_Batch1.txt`) before running scripts or saving analysis to avoid overwriting work.

### Formatting Instructions

**`Stock_Tracker.md` — Ticker Dashboard Table** *(Standalone Mode only)*
When proposing Dashboard updates, apply the following rules to each column:
- **Ticker:** Use the ticker symbol.
- **Last Run:** Set to the current session date.
- **Current Phase:** Set to `Earnings`.
- **Status:** Set to `PASS` for passing tickers. Remove `FILTERED` tickers from the Tracker entirely.
- **Tags:** Carry forward from existing entry. Update only if the analysis result warrants a reclassification.
- **Thesis File:** Leave as `—`.
- **Added:** Leave existing date unchanged.

**`Stock_Tracker.md` — Recent Activity Log** *(Standalone Mode only)*
Prepend a new bullet to the log using the format:
`- **[Date]:** Completed Earnings screening for [TICKERS] — [PASS/FILTERED per ticker].`

**`Stock_Tracker.md` — Next Steps** *(Standalone Mode only)*
Update Next Steps to reflect that Earnings screening is complete and the Screening Completion prompt is ready to run. Use the following format:
`- **Run Screening Completion:** [TICKERS that received PASS] — Earnings complete, Screening Completion next.`

**`Data/screening/Earnings_{DATE}.txt` — Append Analysis** *(Both Modes)*
Append the full analysis output from Step 2 — including all questions, answers, and the Status & Earnings Summary — verbatim to the end of the file.

### Deliverable

**Questions:**
1. **Scope Check:** Are changes limited strictly to the Ticker Dashboard table, Recent Activity Log, Next Steps, and Data File? (Standalone Mode) / Is the only change the Data File append? (Discovery Mode)
2. **Status Check:** Does the Dashboard update accurately reflect the PASS result — and have FILTERED tickers been removed? (Standalone Mode only)
3. **Next Steps Check:** Does the Next Steps update correctly identify PASS tickers for the Screening Completion prompt? (Standalone Mode only)
4. **Append Check:** Has the full Q&A and Status & Earnings Summary from Step 2 been appended verbatim to `Earnings_{DATE}.txt`?

- **Action:**
  - **Standalone Mode:** Ask: *"Do you approve these updates for `Stock_Tracker.md`?"*
  - **Discovery Mode:** Ask: *"Do you approve the data file append?"*
- **Commit:** Upon approval, append the full analysis to `Data/screening/Earnings_{DATE}.txt`. In Standalone Mode, also write all updates to `Stock_Tracker.md`.

**STOP. Wait for user approval before committing.**

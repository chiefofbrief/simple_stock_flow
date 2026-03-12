# Earnings Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided earnings and valuation data for **{TICKER}** and produce a concise, insightful report in the chat window.

## Active Workflow: Sequential Steps
Follow these steps exactly:

1. **Gather Data & Context (READ FIRST):**
   - **Philosophy:** Read `GEMINI.md` to review the foundational Analysis Philosophy & Guidelines.
   - **Quantitative Data:** Read `Data/screening/Earnings_{DATE}.txt` to extract the P/E ratios, earnings history, growth rates, and forward estimates for {TICKER}.
   - **Prior Phase:** Read `Data/screening/Price_Data_{DATE}.txt` to review the previous price analysis findings for this ticker.
   - **Categorization:** Read `Stock_Tracker.md` to identify the stock's current Tags (e.g., `[LOSER]`, `[TAILWIND]`, `[AI]`).
   - **Catalyst:** Read `Discovery_Context.md` to understand the original reason for screening this stock.

2. **Analyze & Generate Report (In Chat):**
   - Evaluate the data against the **Analysis Guidelines** below.
   - Produce the analysis report in the chat window using the exact structure in the **Output Format** section.
   - End your report with your proposed status (PASS/FILTERED) and the mandatory question: *"Do you approve this recommendation? Should I update the Stock Tracker and append this analysis to the data file?"*

3. **Commit Changes (POST-APPROVAL ONLY):**
   - Only after receiving explicit user approval (e.g., "yes", "go ahead"):
     - **Batch Handling:** If you are processing multiple batches on the same date, ensure you rename previous data files (e.g., `Earnings_{DATE}_Batch1.txt`) before running scripts or saving analysis to avoid overwriting work.
     - **Stock Tracker:** Update `Stock_Tracker.md` by strictly following the **Tracker Update Instructions** at the top of that file.
     - **Data File:** Append the **full analysis report** (including Q&A and Status Update) to the end of `Data/screening/Earnings_{DATE}.txt`.

## Analysis Guidelines
Analyze the data using the following questions and structure your response exactly as specified. Refer to the **Examples** section below, specifically the subsection matching the stock's tags, to inform your analysis. **Crucially, all insights must leverage the provided data; you must explicitly specify which metrics led to your conclusion.**

### Output Format

#### {TICKER} Earnings/Valuation Analysis

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

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*(Check `Stock_Tracker.md`. If the stock's Tags column does not contain `[LOSER]`, simply state "N/A - Not a recent loser" for this section and skip the questions below.)*
*   **Are earnings decreasing along with the price?**
    [Answer using specific metrics]
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    [Answer using specific metrics]

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
*(Check `Stock_Tracker.md`. If the stock's Tags column does not contain `[TAILWIND]`, simply state "N/A - Not a tailwind stock" for this section and skip the questions below.)*
*   **Do the forward earnings estimates project a sudden, significant improvement compared to the historical baseline?**
    [Answer using specific metrics]
*   **Is the current valuation (P/E) highly elevated, meaning the stock's price is heavily reliant on these future estimates rather than current cash generation?**
    [Answer using specific metrics]

---
**Status & Earnings Summary**
**[PASS / FILTERED].** [A concise paragraph summarizing the findings and rationale. This text will be copied to the Stock Tracker.]

## Examples

### LOSERS

#### ADBE Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
ADBE is trading at a current P/E of **12.4x**, which is a severe discount across every measurable timeframe: **-48% vs. 1Y ago (23.8x)**, **-48% vs. 3Y ago (23.6x)**, and **-54% vs. its 5-year average (26.9x)**. It is currently at its absolute 5-year valuation floor, down **-74%** from its 47.7x peak.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is exceptionally robust. ADBE has maintained a **5-year EPS CAGR of +16.8%**, growing TTM earnings from $7.82 in 2019 to **$20.95** today. With a stability CV of **0.21**, it is one of the most consistent compounders in the software sector.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term momentum remains high, with **+13.7% TTM growth**. The company has beaten quarterly estimates by an average of **+2.1%** over the last four quarters, with reported quarterly EPS rising from $5.08 to $5.50.

**4. What is the correlation between price and earnings?**
There is a **strong negative correlation of -0.84**. This highlights a massive fundamental divergence: the business is generating record cash while the market is violently contracting its multiple.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The estimate for 2026-03-12 is **$5.87**, a **+$0.37 Forward Delta** over the last actual. This suggests that analysts expect growth to accelerate slightly, contradicting the "AI-disruption" panic reflected in the price.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No.** TTM earnings have increased **13.7% YoY**, while the stock price has collapsed **41% YoY**. This is a textbook "Temporary Price Dislocation."
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Strong Floor.** At 12.4x P/E, the absolute valuation provides a deep margin of safety independently of its 50% relative discount.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**PASS.** Adobe is a high-conviction candidate for a "Loser" thesis. The current 12.4x P/E is half its historical average, despite a consistent 16.8% earnings CAGR and high stability (0.21 CV). The extreme negative correlation (-0.84) between rising earnings and a falling price creates a massive valuation gap, while consistent earnings beats suggest the enterprise moat remains intact despite retail competition fears.

#### ARM Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
ARM's current P/E is **82.7x**. While this is **-21% vs. 1Y ago (104.5x)** and **-12% vs. its short average (93.6x)**, it remains an extreme absolute multiple that leaves no room for error.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is explosive (**+40.0% 5Y CAGR**), but earnings are highly volatile with a stability CV of **0.32**. This is underscored by a major earnings miss in Nov 2025 ($0.15 vs. $0.36 estimate), showing the business is prone to sharp quarterly shocks.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term growth is positive (**+17.5% TTM**), but inconsistent. TTM EPS jumped from $0.76 to $1.48, but the $1.48 figure is actually a deceleration from the growth rates seen in 2025.

**4. What is the correlation between price and earnings?**
The correlation is **0.00**, meaning the current price action is purely sentiment-driven and detached from fundamental updates.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$0.58** is a massive **+$0.15 Forward Delta** over the last actual ($0.43). This is a "priced for perfection" forecast that assumes ARM will immediately return to its highest-ever historical performance level.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No**, earnings are up 17.5% YoY, but the **83x P/E multiple** means the "improvement" is already fully priced in.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Caution.** At 82.7x P/E, there is zero absolute Margin of Safety; the valuation depends entirely on sustaining perfect hyper-growth.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**FILTERED.** Speculative Valuation. While ARM is a dominant growth winner, its 82.7x P/E fails the "safety of principal" test. The market has already discounted a "perfect" 40% growth forecast. With high earnings volatility (0.32 CV) and a recent history of significant misses, the stock lacks any Margin of Safety; any further sentiment shift or growth deceleration could lead to a violent multiple compression toward a more reasonable 40-50x range.

#### CRM Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
CRM's current P/E is **15.3x**, which is a staggering discount of **-47% vs. 1Y ago (29.0x)**, **-50% vs. 3Y ago (30.8x)**, and **-48% vs. its historical average (29.6x)**.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
Salesforce is a highly consistent compounder with a **5-year EPS CAGR of +20.6%**. TTM earnings have risen from $4.80 in 2022 to **$12.55** today. Stability is moderate (**0.40 CV**) as the company has successfully pivoted toward higher margins.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term performance is exceptional, with **+23.2% growth** in the last TTM period. The company has delivered massive positive surprises lately, including a **+24.9% beat** in Feb 2026 ($3.81 vs $3.05 estimate).

**4. What is the correlation between price and earnings?**
There is a **very strong negative correlation of -0.85**. Price has plummeted **-35% YoY** while earnings have surged **+23% YoY**, creating a widening gap between value and price.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The upcoming estimate is **$3.11**, representing a **-$0.70 Forward Delta** compared to the outlier peak of $3.81. However, $3.11 is still higher than the average quarterly earnings of 2025, suggesting the long-term growth trend is intact.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No.** Earnings are accelerating (+23.2%) while the price has capitulated (-35%).
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Strong Floor.** A 15.3x P/E for a 20% grower provides a significant absolute Margin of Safety.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**PASS.** Salesforce is a prime example of a "Temporary Price Dislocation." Trading at 15.3x P/E—nearly half its historical mean—despite 20%+ earnings growth and massive recent beats, the valuation is detached from reality. The extreme -0.85 correlation confirms that the market is ignoring strong fundamentals in favor of a "beaten-down software" narrative.

#### CRWD Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
At **101.9x**, CRWD's P/E is actually **+3% higher than 1Y ago (99.2x)** and **+30% higher than 3Y ago (78.4x)**. While it is down from its 800x "glamour" peak, it is becoming *more* expensive relative to its recent 3-year history even as the price falls.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
Hyper-growth historically (**+70.4% CAGR**), but scaling into maturity. Volatility is high (**0.55 CV**) as the company recently flipped from losses to profits.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
**Fundamental Stall.** TTM earnings have **declined -4.8%** over the last year (from $3.93 to $3.74). This is a critical divergence from its 70% historical CAGR.

**4. What is the correlation between price and earnings?**
Correlation is **-0.07**, meaning the price is essentially moving on noise, decoupled from the recent stagnation in earnings.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate is **$1.07**, a small **-$0.05 Forward Delta** vs. the last actual. This confirms that analysts project a period of flat growth ahead.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **Yes.** TTM earnings dropped **-4.8%** while the price fell **-2%**. This is not a "Temporary Loser" setup; it is a **Growth Stall** where the multiple remains at a dangerous 100x.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Caution.** At 101.9x P/E, the absolute floor is non-existent; the price remains speculative despite the "correction."

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**FILTERED.** Growth Stall at Premium Price. Buying a 100x P/E stock when earnings are declining (-4.8% TTM) is speculative, not an investment. Unlike ADBE or CRM, where the multiple compressed while earnings rose, CRWD’s multiple has actually *expanded* relative to the last 3 years while growth has stalled. There is no Margin of Safety here; the stock is a high-multiple growth trap.

#### IBM Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
IBM's current P/E is **22.0x**, which is a **27% premium** over its 5-year average of **17.3x**, and a **+105% premium** over where it traded 5 years ago (10.7x).

**2. What is the long-term earnings trend and volatility? (past 5 years)**
Extremely slow but stable: **5-year EPS CAGR of +5.9%** with exceptional stability (**0.09 CV**). Note that TTM earnings today ($11.57) are still significantly lower than they were in 2019 ($13.82).

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term performance is decent (**+12.0% TTM growth**), with consistent quarterly beats of **+5% to +12%**.

**4. What is the correlation between price and earnings?**
Correlation is **0.20**, showing a very weak relationship.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$1.83** is seasonally lower than Q4, but reflects YoY growth.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No**, earnings are up 12% YoY, but the **22x P/E multiple** for a 6% grower is historically elevated. Even after a 21% price drop, the stock is not "cheap" by any objective measure.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Reasonable Floor.** 22x is reasonable for a stable business, but the 27% premium over historical levels negates the Margin of Safety.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

#### NFLX Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
NFLX's current P/E is **38.7x**, which is a **-21% discount vs. 1Y ago (49.3x)** and **-26% below its historical average (52.2x)**. While it is significantly lower than its 5-year peak of 88.3x, it remains **+19% higher than its 3-year valuation low (32.5x)**.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is exceptionally strong, with a **5-year EPS CAGR of +32.9%**. TTM earnings have grown from $0.27 in 2019 to **$2.53** today. Stability is moderate with a CV of **0.42**, reflecting the company's successful scaling of its margin structure.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term momentum remains robust, with **+27.1% TTM growth**. The company has consistently delivered strong quarterly EPS, though it did suffer a **-15.2% miss** in Oct 2025 ($0.59 vs $0.70 estimate).

**4. What is the correlation between price and earnings?**
There is a **strong negative correlation of -0.78**. Earnings are continuing their upward trajectory (+27%) while the stock price has contracted 25% from its peak, creating a clear fundamental divergence.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$0.86** is a healthy **+$0.30 Forward Delta** over the last reported actual ($0.56), suggesting that analysts expect growth to return to the record levels seen in mid-2025.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No.** TTM earnings increased 27.1% YoY, while the price corrected 25%. The fundamental business is expanding while the market is contracting the multiple.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Caution.** At 38.7x P/E, the absolute valuation is high; the thesis relies entirely on sustained growth and multiple stability rather than an absolute price floor.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**PASS (with Caution).** Investigating Speculative Multiples. While NFLX is delivering 27% growth and trades 26% below its historical average, its 38.7x P/E is still high in absolute terms and is currently 19% higher than its 3-year valuation floor. We will PASS it to the Financials phase to verify if the "Economic Reality" (FCF and OCF) justifies this multiple or if rising production costs and competition are eroding the quality of its GAAP earnings.

#### NOW Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
ServiceNow (NOW) is trading at a current P/E of **35.1x**, which is a massive discount across all timeframes: **-54% vs. 1Y ago (75.7x)**, **-87% vs. 3Y ago (269.9x)**, and **-89% vs. its historical average (321.1x)**. It is near its absolute 5-year valuation floor (-96% from its high).

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is explosive, with a **5-year EPS CAGR of +97.1%**. Earnings have moved from a loss in 2019 to **$3.51 TTM** today. Volatility is high (**0.92 CV**) as the company scaled rapidly from break-even into massive profitability.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term performance is exceptional, with **+42.9% TTM growth**. The company has consistently beaten quarterly estimates by double digits, including a **+13.3% beat** in Oct 2025 and a **+14.7% beat** in July 2025.

**4. What is the correlation between price and earnings?**
There is an **extreme negative correlation of -0.88**. Price has collapsed (-34% YoY) while earnings have surged (+43% YoY), creating a textbook "Temporary Price Dislocation."

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$0.95** is a minor **+$0.03 Forward Delta** over the last actual ($0.92), projecting a continuation of the record-breaking quarterly performance trend.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No.** Earnings have accelerated (+43%) while the price has capitulated. This is a clear case of "mispricing" where sentiment is detached from the cash-generation reality.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Caution.** 35.1x is high in absolute terms, but the 43% TTM growth rate provides a rapidly rising floor.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**PASS.** High-Quality Dislocation. ServiceNow is a standout candidate for a "Loser" thesis. A 35x P/E for a business with a 97% long-term CAGR and 43% TTM growth represents a violent multiple contraction relative to its 300x+ history. Unlike other software peers, NOW's current growth rate is significantly higher than its multiple, suggesting that the current sector-wide capitulation has created a genuine valuation gap for a fundamental winner.

#### NVO Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
Novo Nordisk (NVO) is trading at a current P/E of **9.9x**, which is a severe discount: **-64% vs. 1Y ago (27.2x)**, **-75% vs. 3Y ago (39.3x)**, and **-61% below its historical average (25.2x)**.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is strong and consistent, with a **5-year EPS CAGR of +23.2%**. Earnings have grown from $1.24 in 2020 to **$3.91 TTM** today. Stability is high with a CV of **0.37**.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term performance remains robust, with **+19.7% TTM growth**. The company has delivered massive positive surprises lately, including a **+32.5% beat** in Nov 2025 ($1.02 vs $0.77 estimate).

**4. What is the correlation between price and earnings?**
There is a **strong negative correlation of -0.72**. Price has collapsed **56% YoY** while earnings have grown **20% YoY**, creating an extreme valuation gap.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$0.93** is a minor **-$0.07 Forward Delta** vs. the peak Q4 actual ($1.00), but remains firmly in line with the $0.90+ quarterly trend established in 2025.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No.** Earnings are growing while the price has been halved.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Strong Floor.** At 9.9x P/E, the absolute valuation is extremely low for a dominant pharmaceutical leader.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**PASS.** Deep Defensive Value. Novo Nordisk represents a massive fundamental divergence. While pricing pressure narratives are real, the market has responded by cutting the multiple to just 9.9x—less than half its historical average—despite 20% TTM growth and massive recent beats. The 23% long-term CAGR and high stability suggest the current 56% price collapse is a violent overreaction to sentiment rather than a fundamental impairment.

#### PANW Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
Palo Alto Networks (PANW) is trading at **44.5x**, which is **-22% below its historical average (56.8x)** and **-30% vs. 1Y ago (63.5x)**.

**2. What is the long-term earnings trend and volatility? (past 5 years)**
Strong long-term growth with a **5-year EPS CAGR of +30.8%**. Earnings have risen from $0.82 in 2019 to **$3.71 TTM** today. Stability is moderate with a CV of **0.44**.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term performance shows **+23.7% TTM growth**. The company has consistently beaten estimates, though recent beats have been more modest (+4% to +9%) compared to its hyper-growth history.

**4. What is the correlation between price and earnings?**
There is a **negative correlation of -0.53**. Price is contracting while earnings are continuing to grow, though growth is starting to decelerate relative to the 5-year CAGR.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$0.80** is a significant **-$0.23 Forward Delta** over the last reported actual ($1.03). This reflects management's "platformization" strategy, which involves sacrificing short-term billings/earnings to lock in enterprise customers.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **No**, but the **44.5x multiple** is extremely high for a business entering a period of decelerating growth and intentional earnings suppression.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Caution.** At 44.5x P/E, there is zero absolute Margin of Safety; the price remains speculative.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**FILTERED.** Speculative Multiple. While 24% TTM growth is robust, it does not justify a 44.5x P/E in an investment context. At 45x, the stock remains "priced for perfection," offering zero Margin of Safety. If growth decelerates further—which the -$0.23 Forward Delta and "platformization" strategy suggest is likely—the multiple could compress violently. Paying a high-growth premium for a business with a negative forward catalyst and decelerating CAGR fails the test of "Safety of Principal."

#### QCOM Earnings/Valuation Analysis

**1. How does the current P/E ratio compare to historical levels?**
QCOM's current P/E is **11.0x**, which is a **-24% below its historical average (14.5x)** and **-22% vs. 1Y ago (14.1x)**. It is trading at its lowest valuation levels in 5 years (down -52% from its 22.8x peak).

**2. What is the long-term earnings trend and volatility? (past 5 years)**
The long-term trend is positive but cyclical, with a **5-year EPS CAGR of +17.7%**. Stability is exceptional with a CV of **0.13**, the lowest in this batch.

**3. What is the short-term earnings trend and volatility? (past 12 months)**
Short-term growth is decent at **+11.5% TTM**, with consistent (though small) quarterly beats of **+1% to +4%**.

**4. What is the correlation between price and earnings?**
Correlation is **0.04**, meaning the price and earnings are moving independently. The price is driven by the "Apple defection" and "memory crunch" narratives rather than actual quarterly reports.

**5. How do the upcoming earnings estimates compare to the company’s past performance?**
The next estimate of **$2.57** is a massive **-$0.93 Forward Delta** over the last actual ($3.50). Analysts are pricing in a sharp fundamental hit from the loss of major smartphone customers.

**6. FOR [LOSER]-TAGGED TICKERS ONLY**
*   **Are earnings decreasing along with the price?**
    **Yes, looking forward.** While TTM earnings are up, the upcoming quarterly estimate projects a significant drop, which is the specific catalyst for the recent price weakness.
*   **What is the quality of the absolute valuation floor (Under 20x = Strong, 20-30x = Reasonable, Over 30x = Caution)?**
    **Strong Floor.** At 11x P/E, the absolute valuation provides a massive Margin of Safety for a stable incumbent.

**7. FOR [TAILWIND]-TAGGED TICKERS ONLY**
N/A - Not a tailwind stock

---
**Status & Earnings Summary**
**PASS.** Dislocated Narrative Play. Qualcomm is a classic "Loser" setup where a known negative catalyst (Apple defection) has triggered a price drop and an earnings downgrade. At 11x P/E, the stock is trading at a significant discount to its historically stable baseline (0.13 CV). We will PASS this to the Financials phase specifically to determine if the 11x multiple provides a sufficient "Margin of Safety floor" to absorb these known losses or if the economic reality of the customer defecton is worse than the GAAP estimates suggest.

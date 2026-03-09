# Ticker Tracker

## Recent Activity Log
- **2026-03-09:** Completed Price screening for SPGI, WDAY (PASS) and STLA, TTD, UPWK, VSCO, ZS (FILTERED).
- **2026-03-09:** Completed Price screening for AIG, SNOW (PASS) and PYPL, SDGR, SHOP (FILTERED).
- **2026-03-09:** Updated classifications for remaining PENDING tickers based on Discovery Context.
- **2026-03-09:** Completed Price screening for QCOM (PASS) and PINS, QVCGA, RXRX (FILTERED).
- **2026-03-09:** Completed Price screening for NFLX, NOW, NVO, PANW (PASS) and OWL (FILTERED).

## Tracker Update Instructions
When updating this file after receiving explicit user approval:
1.  **Recent Activity Log:** Prepend a new bullet point with today's date and the action taken. Maintain only the 5 most recent entries.
2.  **Ticker Dashboard:** 
    *   Update the `Last Run`, `Current Phase`, and `Status` columns for the target ticker in the Master Table. Use the **HIMS** entry as a formatting guide.
    *   **Sorting:** Always move tickers with `PASS` or `ACTIVE` status above the `PENDING` items, in order of their latest workflow step.
    *   **Filtering:** If a ticker is marked as `FILTERED`, remove its row from the Dashboard table entirely.
    *   **Tags:** Add the tag(s) assigned during the Discovery phase: [LOSER], [TAILWIND], [AI], [OTHER].
3.  **Analysis Summaries:** 
    *   Append the concise analysis summary to the ticker’s existing `### {TICKER}` block. Use the **HIMS** summary sections below as a formatting guide.
    *   If the ticker's Phase has changed (e.g., Screening → Deep Dive) or it was `FILTERED`, move its entire `### {TICKER}` block to the appropriate section (**Deep Dive**, **Screening**, or **Filtered Archive**).

**Workflow Steps:** Price → Earnings → Financials → Sentiment → Footnotes → Earnings Calls → Synthesis

## Ticker Dashboard

| Ticker | Last Run   | Current Phase | Status   | Tags           | Thesis File    |
|--------|------------|---------------|----------|----------------|----------------|
| **HIMS**| 2026-03-02 | Earnings Calls| PASS     | [LOSER]        | HIMS_Thesis.md |
| ADBE   | 2026-03-02 | Price         | PASS     | [LOSER]        | —              |
| ARM    | 2026-03-02 | Price         | PASS     | [LOSER]        | —              |
| CRM    | 2026-03-02 | Price         | PASS     | [LOSER]        | —              |
| CRWD   | 2026-03-02 | Price         | PASS     | [LOSER]        | —              |
| IBM    | 2026-03-06 | Price         | PASS     | [LOSER] [AI]   | —              |
| IT     | 2026-03-06 | Price         | PASS     | [LOSER]        | —              |
| KD     | 2026-03-06 | Price         | PASS     | [LOSER]        | —              |
| MAT    | 2026-03-06 | Price         | PASS     | [LOSER]        | —              |
| MSFT   | 2026-03-06 | Price         | PASS     | [LOSER] [AI]   | —              |
| NFLX   | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| NOW    | 2026-03-09 | Price         | PASS     | [LOSER] [AI]   | —              |
| NVO    | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| PANW   | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| QCOM   | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| AIG    | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| SNOW   | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| SPGI   | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| WDAY   | 2026-03-09 | Price         | PASS     | [LOSER]        | —              |
| AMD    | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| AMSC   | —          | —             | PENDING  | [TAILWIND]     | —              |
| ASML   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| AVGO   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| BSX    | —          | —             | PENDING  | [OTHER]        | —              |
| CEG    | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| CEK    | —          | —             | PENDING  | [TAILWIND]     | —              |
| CHKP   | —          | —             | PENDING  | [TAILWIND]     | —              |
| CLS    | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| CRWV   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| CSGP   | —          | —             | PENDING  | [TAILWIND]     | —              |
| CSU    | —          | —             | PENDING  | [TAILWIND]     | —              |
| DDOG   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| ENPH   | —          | —             | PENDING  | [TAILWIND]     | —              |
| EVVTY  | —          | —             | PENDING  | [OTHER]        | —              |
| FROG   | —          | —             | PENDING  | [TAILWIND]     | —              |
| GWRE   | —          | —             | PENDING  | [TAILWIND]     | —              |
| HUBS   | —          | —             | PENDING  | [TAILWIND]     | —              |
| ICHR   | —          | —             | PENDING  | [TAILWIND]     | —              |
| INTA   | —          | —             | PENDING  | [OTHER]        | —              |
| INTC   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| INTU   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| IOT    | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| LITE   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| LRCX   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| META   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| MU     | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| NET    | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| NIO    | —          | —             | PENDING  | [TAILWIND]     | —              |
| NSC    | —          | —             | PENDING  | [OTHER]        | —              |
| NVDA   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| OKTA   | —          | —             | PENDING  | [TAILWIND]     | —              |
| ORCL   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| OUST   | —          | —             | PENDING  | [TAILWIND] [AI]| —              |
| QTWO   | —          | —             | PENDING  | [TAILWIND]     | —              |
| RIVN   | —          | —             | PENDING  | [TAILWIND]     | —              |
| SNDK   | —          | —             | PENDING  | [OTHER]        | —              |
| TWLO   | —          | —             | PENDING  | [TAILWIND]     | —              |
| TYL    | —          | —             | PENDING  | [TAILWIND]     | —              |
| UNP    | —          | —             | PENDING  | [OTHER]        | —              |
| VEEV   | —          | —             | PENDING  | [TAILWIND]     | —              |
| VRT    | —          | —             | PENDING  | [TAILWIND] [AI]| —              |

---

## Deep Dive

### HIMS
**Price** | 2026-03-02 | PASS
HIMS is experiencing a violent capitulation, down 46% in the last month (Z-score -1.8) and 68% YoY. It sits at just 1% of its 52-week high. The current drop represents 53% of its maximum 5-year drawdown, and it requires a staggering 183% gain to revert to its 1-year average.

**Earnings** | 2026-03-02 | PASS
HIMS is a textbook mispricing candidate. While the price has collapsed, the P/E multiple has compressed 82% YoY and 70% below its historical average to 28.3x. Despite the stock's "loser" tag, the underlying business is showing explosive growth (EPS CAGR N/A but highly positive trajectory) with high stability.

**Financials** | 2026-03-02 | PASS
HIMS exhibits phenomenal scaling with a 71.4% 5-year CAGR, and a 2024 inflection point to positive operating margins (currently 4.6% TTM). Earnings quality is exceptionally high (OCF/Net Income 2.36x), confirming reported growth is backed by hard cash flow ($0.30B). While CapEx has surged and Debt/Assets jumped to 58.7%, the core asset-light economic engine remains robust despite the 68% stock price collapse.

**Sentiment** | 2026-03-02 | PASS
HIMS is the victim of a violent reflexive "bust" cycle as the market's "GLP-1 copycat" narrative has been inverted into a "regulatory death" narrative. Analyst targets have collapsed (Citi to $13.25) and retail sentiment (TikTok/YouTube) is deeply fractured following a Novo Nordisk lawsuit and FDA enforcement action on compounded semaglutide. This "misconception"—fixating on a withdrawn product while ignoring the company's $2.35B broader platform and 2M+ subscribers—is the primary driver of the current mispricing.

**Footnotes** | 2026-03-02 | PASS
Discovery of a **$1.0B war chest of 0% interest convertible debt** (issued May 2025) which funded the $1.15B Eucalyptus/Zava acquisition. This interest-free capital provides a massive 5-year runway. While filings confirm three federal investigations (DOJ, SEC, and Class Action), the company has already "moved the goalposts" globally (Canada, UK, Japan) to diversify away from US regulatory risk.

**Earnings Calls** | 2026-03-02 | PASS
Management is pivoting from adversary to distribution partner (re-engaging Novo Nordisk for branded Wegovy) while verticalizing 1M sq ft of proprietary pharmacies. CEO Andrew Dudum's tone is one of "Power, not Panic." The buyback signal from CFO Okupe at these valuations is a strong "Intrinsic Value" indicator. Final Verdict: CONVICTION BUY (High Risk).

---

## Screening

### ADBE
**Price** | 2026-03-02 | PASS
ADBE is a high-quality incumbent in a violent 'bust' cycle, down 41% YoY and trading at just 7% of its 52-week range ($259 vs $415 peak). Despite its stable history, it is now at 5-year lows. The 31% discount to its 1-year average price ($375) creates a significant margin of safety if its core enterprise moat remains intact.

### ARM
**Price** | 2026-03-02 | PASS
ARM is a dominant growth winner (+37.8% 5Y CAGR) currently undergoing a minor correction, down 7% YoY and trading at 41% of its 52-week range. The current price ($122) represents a rare 8% discount to its 12-month average, offering a high-quality entry point within a strong structural uptrend.

### CRM
**Price** | 2026-03-02 | PASS
CRM is a stable software giant experiencing a sharp YoY capitulation, down 35% and trading at just 14% of its 52-week range. Despite a flat long-term CAGR (-2.1%), the current dislocation is anomalous; trading at a 26% discount to its 1-year average ($191 vs $259 avg) provides a significant margin of safety for a high-quality incumbent.

### CRWD
**Price** | 2026-03-02 | PASS
CRWD is a high-quality performer (+11.6% 5Y CAGR) in a sudden 15.7% monthly correction, now trading at 31% of its 52-week range. The current price ($381) sits 20% below its 12-month average, representing a significant short-term dislocation for a stock that remains in a structural long-term uptrend.

### IBM
**Price** | 2026-03-06 | PASS
IBM is a strong long-term performer (+21.5% 5Y CAGR) that suffered a violent 21% monthly drop due to a narrative shock (Claude COBOL automation). Currently sitting at 39% of its 52-week range, it offers a 7% margin of safety relative to its 12-month average, presenting a classic temporary dislocation setup.

### IT
**Price** | 2026-03-06 | PASS
IT (Gartner) is experiencing a catastrophic, sentiment-driven collapse (-66% YoY) fueled by AI-disruption fears, currently trading at absolute 5-year lows (9% of 52w range). This violent capitulation has created a massive 67% discount to its 1-year mean, requiring a deep dive to determine if the core business model is permanently impaired or temporarily mispriced.

### KD
**Price** | 2026-03-06 | PASS
KD (Kyndryl) has suffered a catastrophic, sentiment-driven collapse, down 66% YoY and trading at absolute lows (9% of 52w range) following a massive 46% plunge in February due to executive exits and guidance cuts. This "perfect storm" has created a 54% discount to its 1-year mean (requiring a +118% reversion), making it a prime candidate for a deep dive to see if the core FCF remains intact beneath the panic.

### MAT
**Price** | 2026-03-06 | PASS
MAT is a historically low-volatility stock (CV 0.10) that suffered an anomalous 18.9% monthly drop following an earnings/guidance miss, driving it down to 22% of its 52-week range. The current price provides a clear 14% discount to its 1-year mean (requiring a +16% reversion), presenting a distinct "loser" setup compared to its soaring rival Hasbro.

### MSFT
**Price** | 2026-03-06 | PASS
MSFT is a premium long-term compounder (+12.5% 5Y CAGR) currently experiencing a sharp, sentiment-driven correction (-19% combined drop in early 2026) due to AI CapEx fears. Trading at 32% of its 52-week range, it offers a rare 12% discount to its 1-year average price, providing a clear margin of safety for a dominant incumbent.

### NFLX
**Price** | 2026-03-09 | PASS
NFLX has absorbed a significant 25% correction over the last quarter due to WB deal uncertainty and valuation fears. Trading 12% below its annual mean and sitting in the 39th percentile of its 52-week range, it offers a margin of safety for a business that remains a long-term compounder (+12.2% 5Y CAGR).

### NOW
**Price** | 2026-03-09 | PASS
NOW (ServiceNow) is a dominant workflow incumbent trading at a massive 26% discount to its 1-year mean following a violent 34% YoY correction. At just 22% of its 52-week range, the price reflects broad market panic over AI disruption which contradicts the company's positioning as an orchestrator of agentic AI.

### NVO
**Price** | 2026-03-09 | PASS
NVO (Novo Nordisk) has suffered a catastrophic 56% YoY loss of value, currently trading at absolute multi-year lows (7% of 52w range). While the pricing pressure narrative is real, the 29% discount to its annual mean suggests a potentially overdone reflexive "bust" cycle for a major pharmaceutical leader.

### PANW
**Price** | 2026-03-09 | PASS
PANW is a high-growth cybersecurity leader (+21.8% 5Y CAGR) currently offering a rare 11% discount to its annual average following a short-term correction. Trading at 31% of its 52-week range, it provides a high-quality entry point for a dominant incumbent within a structural uptrend.

### QCOM
**Price** | 2026-03-09 | PASS
QCOM is a historically stable incumbent (CV 0.17) currently undergoing a moderate correction due to a "memory crunch" narrative. Trading at just 17% of its 52-week range and offering a 14% discount to its 1-year mean, it presents a high-quality entry point for a dominant leader in a stagnant but essential market.

### AIG
**Price** | 2026-03-09 | PASS
AIG is a stable long-term compounder (+13.9% 5Y CAGR) currently experiencing a sentiment-driven pullback, trading at 34% of its 52-week range. While the statistical discount is modest (+4% to annual mean), the company's strong FCF generation and low-volatility history make this a high-quality "distressed price" setup for a business that is fundamentally healthy.

### SNOW
**Price** | 2026-03-09 | PASS
SNOW is experiencing a sharp, sentiment-driven capitulation (-35% over 3 months) that has driven the stock to 37% of its 52-week range. Despite a negative long-term CAGR, the recent violent drop has created a 19% discount to its annual mean, presenting a classic "beaten-down software" opportunity to investigate if the cloud moat remains intact.

### SPGI
**Price** | 2026-03-09 | PASS
SPGI is a dominant data/ratings incumbent (+6.8% 5Y CAGR) currently offering a 13% discount to its 1-year mean following AI-related sentiment fears. Trading at 32% of its 52-week range, the price represents an anomalous dislocation for a historically low-volatility business.

### WDAY
**Price** | 2026-03-09 | PASS
WDAY is a historically stable enterprise giant experiencing an extreme, sentiment-driven collapse (-44% YoY) due to broad AI disruption fears. Trading at just 19% of its 52-week range, the massive 44% discount to its 1-year mean provides a significant margin of safety to investigate if the core moat remains intact.

---

## Filtered Archive

### AAPL
**Price** | 2026-03-02 | FILTERED
AAPL is a long-term compounder (+16.9% 5Y CAGR) that has fully recovered from its recent dip, trading at 80% of its 52-week high ($264 vs $278 peak). It currently sits 8% above its 12-month average price, negating the 'temporary loser' thesis and offering no margin of safety for reversion.

### ABCL
**Price** | 2026-03-02 | FILTERED
ABCL is a 'permanent loser' in a terminal downtrend, down 91% over 5 years with a catastrophic -36.7% CAGR. While up 37% YoY, it remains trapped near historical lows (36% of 52w range) and lacks the stable long-term base required for a temporary mispricing thesis; recent volatility is noise within a structural decline.

### ABSI
**Price** | 2026-03-02 | FILTERED
ABSI is a 'permanent loser' experiencing persistent value destruction, down 30% YoY and 48% over 2 years (-39.2% 5Y CAGR). Trading at just 21% of its 52-week range and 11% below its annual average, the stock sits at all-time lows with no established support level or stable history to justify a reversion bet.

### CLVT
**Price** | 2026-03-02 | FILTERED
CLVT is a 'permanent loser' down 90% from 5-year highs with a terminal -35.4% CAGR. Although it trades at a massive 49% discount to its 1-year average, this statistical 'upside' is overshadowed by 5 years of consistent value destruction; the stock remains near all-time lows (23% of 52w range) with no signs of structural stabilization.

### CSCO
**Price** | 2026-03-02 | FILTERED
CSCO is a steady compounder (+14.5% 5Y CAGR) that has fully absorbed its recent 'AI tax' margin narrative, trading at 73% of its 52-week high ($78 vs $56 low). It now trades at a 9% premium to its 12-month average, negating the 'loser' thesis as the previous sentiment-driven discount has entirely evaporated.

### CVNA
**Price** | 2026-03-02 | FILTERED
CVNA is a highly volatile stock (+2.6% 5Y CAGR) that has recovered 39% YoY, currently trading near the midpoint (52%) of its 52-week range. While it trades at a 9% discount to its 1-year average, it lacks the deep 'temporary loser' profile of more stable peers; the current level is far removed from its catastrophic 2022 lows where the true margin of safety existed.

### DIS
**Price** | 2026-03-06 | FILTERED
While DIS offers a 10% reversion to its 12-month mean following recent CEO succession news, it behaves more like a structural underperformer (-11.1% 5Y CAGR, -45% over 5 years) than a high-quality business suffering a temporary, out-of-character dislocation.

### HOOD
**Price** | 2026-03-06 | FILTERED
Despite the sharp 24% February drop, HOOD remains up 56% YoY and 677% over 3 years (+18.4% 5Y CAGR); its extreme inherent volatility (CV 1.04) makes the current 28% discount to its mean a feature of its normal trading rather than a distinct, temporary mispricing.

### HUBG
**Price** | 2026-03-06 | FILTERED
Although HUBG suffered an anomalous -18% combined drop over the last two months due to a financial reporting error, the stock had previously run up so much that it is still trading 4% *above* its 12-month average, offering no statistical margin of safety for reversion.

### JD
**Price** | 2026-03-06 | FILTERED
JD is in a structural multi-year decline (-68% over 5 years, -19.9% CAGR). While it sits near 52-week lows (12%) and offers a 14% reversion to its annual average, the slow, grinding nature of the drawdown indicates persistent fundamental weakness rather than a sharp, temporary sentiment dislocation.

### LYFT
**Price** | 2026-03-06 | FILTERED
LYFT is a highly volatile stock (CV 0.71) that has suffered massive long-term structural impairment (-77% over 5 years, -24.5% CAGR). While the recent 18% drop offers a 28% reversion upside to its annual mean, the extreme historic volatility and existential "AV disruption" narrative make it a terminal risk rather than a high-quality temporary mispricing.

### OWL
**Price** | 2026-03-09 | FILTERED
OWL (Blue Owl) is in a terminal downward spiral, trading at absolute multi-year lows (0% of range) with a relentless 12-month grind. Despite the 60% reversion upside, the lack of any stabilization or positive catalysts suggests a structurally impaired business rather than a temporary sentiment dislocation.

### PINS
**Price** | 2026-03-09 | FILTERED
Permanent Loser. Despite a massive statistical discount to its annual mean, the terminal 5-year downtrend (-24.1% CAGR, -76% total loss) indicates structural impairment rather than a temporary sentiment-driven dip. The stock lacks the stable historical base required to justify a "mean reversion" thesis.

### QVCGA
**Price** | 2026-03-09 | FILTERED
QVCGA has suffered near-total value destruction (-81% YoY, -75% 5Y CAGR). The massive 72% plunge in February is indicative of terminal distress or restructuring risk rather than a high-quality temporary mispricing; the stock lacks the stable fundamental base required for a margin of safety thesis.

### RXRX
**Price** | 2026-03-09 | FILTERED
RXRX (Recursion) is in a terminal structural decline, down 90% over 5 years. While it offers a statistical 38% reversion upside, the consistent monthly bleeding and lack of any support level suggest permanent impairment driven by AI-pharma disruption fears rather than a temporary dislocation.

### PYPL
**Price** | 2026-03-09 | FILTERED
PYPL is in a terminal structural downtrend, having lost 82% of its value over 5 years (-28.5% CAGR). Despite a 37% statistical discount to its annual mean and recent Stripe acquisition rumors, the consistent monthly bleeding and lack of any established historical support justify treating the current "upside" as a value trap.

### SDGR
**Price** | 2026-03-09 | FILTERED
SDGR (Schrodinger) is experiencing persistent value destruction, down 44% YoY and 88% over 5 years (-33.5% CAGR). Trading at just 8% of its 52-week range with no sign of stabilization, the 49% discount to its annual mean reflects structural impairment rather than a temporary mispricing.

### SHOP
**Price** | 2026-03-09 | FILTERED
SHOP has fully recovered from its recent earnings pullback and now trades 1% above its 12-month average. Despite its "loser" tag from the January drop, the current price ($131) offers no statistical discount for mean reversion and sits at the midpoint of its 52-week range.

### STLA
**Price** | 2026-03-09 | FILTERED
STLA (Stellantis) is in a structural decline, down 40% over 5 years (-9.5% CAGR). Despite a 37% discount to its annual mean, the lack of a stable fundamental floor and the persistent multi-year downward grind justify treating this as a value trap.

### TTD
**Price** | 2026-03-09 | FILTERED
TTD (The Trade Desk) has suffered massive long-term structural impairment, losing 65% of its value over 5 years. Despite massive CEO insider buying and a 76% statistical discount to its annual mean, the catastrophic long-term trend makes this a high-risk falling knife rather than a temporary mispricing.

### UPWK
**Price** | 2026-03-09 | FILTERED
UPWK has lost 76% of its value over 5 years (-24% CAGR). While the 21% discount to its annual mean seems attractive, the consistent multi-year bleeding and extreme inherent volatility make it a structural risk rather than a temporary dislocation.

### VSCO
**Price** | 2026-03-09 | FILTERED
Although VSCO suffered a violent -24% earnings pullback in February, the stock had previously run up so much that it still trades 23% *above* its 12-month mean. Despite the "loser" tag, the current price offers no statistical margin of safety for reversion.

### ZS
**Price** | 2026-03-09 | FILTERED
ZS (Zscaler) is in a structural multi-year downtrend, currently trading at 5-year lows. Despite a massive 53% statistical discount to its annual mean, the persistent monthly bleeding and negative long-term CAGR justify treating the current price action as structural impairment rather than a temporary mispricing.

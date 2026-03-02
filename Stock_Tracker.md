# Ticker Tracker

## Recent Activity Log
- **2026-03-02:** Completed Price screening for 10 [LOSER] tickers; 4 PASS, 6 FILTERED.
- **2026-03-02:** Completed Deep Dive for **HIMS** (Conviction Buy).
- **2026-03-02:** Reset Ticker Tracker for new screening run.

## Tracker Update Instructions
When updating this file after receiving explicit user approval:
1.  **Recent Activity Log:** Prepend a new bullet point with today's date and the action taken. Maintain only the 5 most recent entries.
2.  **Ticker Dashboard:** 
    *   Update the `Last Run`, `Current Phase`, and `Status` columns for the target ticker in the Master Table. Use the **HIMS** entry as a formatting guide.
    *   **Sorting:** Always move tickers with `PASS` or `ACTIVE` status above the `PENDING` items, in order of their latest workflow step.
    *   **Filtering:** If a ticker is marked as `FILTERED`, remove its row from the Dashboard table entirely.
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
| AIG    | —          | —             | PENDING  |                | —              |
| AMD    | —          | —             | PENDING  | [AI]           | —              |
| AMSC   | —          | —             | PENDING  |                | —              |
| ASML   | —          | —             | PENDING  | [AI]           | —              |
| AVGO   | —          | —             | PENDING  | [AI]           | —              |
| BSX    | —          | —             | PENDING  |                | —              |
| CEG    | —          | —             | PENDING  | [AI]           | —              |
| CEK    | —          | —             | PENDING  |                | —              |
| CHKP   | —          | —             | PENDING  |                | —              |
| CLS    | —          | —             | PENDING  | [AI]           | —              |
| CSGP   | —          | —             | PENDING  |                | —              |
| CSU    | —          | —             | PENDING  |                | —              |
| DDOG   | —          | —             | PENDING  |                | —              |
| DIS    | —          | —             | PENDING  | [LOSER]        | —              |
| ENPH   | —          | —             | PENDING  |                | —              |
| EVVTY  | —          | —             | PENDING  |                | —              |
| FROG   | —          | —             | PENDING  |                | —              |
| GWRE   | —          | —             | PENDING  |                | —              |
| HOOD   | —          | —             | PENDING  | [LOSER]        | —              |
| HUBG   | —          | —             | PENDING  | [LOSER]        | —              |
| HUBS   | —          | —             | PENDING  |                | —              |
| IBM    | —          | —             | PENDING  | [LOSER] [AI]   | —              |
| ICHR   | —          | —             | PENDING  | [AI]           | —              |
| INTA   | —          | —             | PENDING  |                | —              |
| INTC   | —          | —             | PENDING  | [AI]           | —              |
| INTU   | —          | —             | PENDING  |                | —              |
| IOT    | —          | —             | PENDING  |                | —              |
| IT     | —          | —             | PENDING  | [LOSER]        | —              |
| KD     | —          | —             | PENDING  | [LOSER]        | —              |
| LITE   | —          | —             | PENDING  | [AI]           | —              |
| LRCX   | —          | —             | PENDING  | [AI]           | —              |
| LYFT   | —          | —             | PENDING  | [LOSER]        | —              |
| MAT    | —          | —             | PENDING  | [LOSER]        | —              |
| META   | —          | —             | PENDING  | [AI]           | —              |
| MSFT   | —          | —             | PENDING  | [LOSER] [AI]   | —              |
| MU     | —          | —             | PENDING  | [AI]           | —              |
| NET    | —          | —             | PENDING  |                | —              |
| NFLX   | —          | —             | PENDING  | [LOSER]        | —              |
| NIO    | —          | —             | PENDING  |                | —              |
| NOW    | —          | —             | PENDING  | [LOSER] [AI]   | —              |
| NSC    | —          | —             | PENDING  |                | —              |
| NVDA   | —          | —             | PENDING  | [AI]           | —              |
| NVO    | —          | —             | PENDING  | [LOSER]        | —              |
| OKTA   | —          | —             | PENDING  |                | —              |
| ORCL   | —          | —             | PENDING  | [AI]           | —              |
| OUST   | —          | —             | PENDING  | [AI]           | —              |
| OWL    | —          | —             | PENDING  | [LOSER]        | —              |
| PANW   | —          | —             | PENDING  | [LOSER]        | —              |
| PINS   | —          | —             | PENDING  | [LOSER]        | —              |
| PYPL   | —          | —             | PENDING  | [OTHER]        | —              |
| QCOM   | —          | —             | PENDING  | [LOSER]        | —              |
| QTWO   | —          | —             | PENDING  |                | —              |
| QVCGA  | —          | —             | PENDING  | [LOSER]        | —              |
| RIVN   | —          | —             | PENDING  |                | —              |
| RXRX   | —          | —             | PENDING  | [LOSER]        | —              |
| SDGR   | —          | —             | PENDING  | [LOSER]        | —              |
| SHOP   | —          | —             | PENDING  | [LOSER]        | —              |
| SNDK   | —          | —             | PENDING  | [AI]           | —              |
| SNOW   | —          | —             | PENDING  | [LOSER]        | —              |
| SPGI   | —          | —             | PENDING  | [LOSER]        | —              |
| STLA   | —          | —             | PENDING  | [LOSER]        | —              |
| TTD    | —          | —             | PENDING  |                | —              |
| TWLO   | —          | —             | PENDING  |                | —              |
| TYL    | —          | —             | PENDING  |                | —              |
| UNP    | —          | —             | PENDING  |                | —              |
| UPWK   | —          | —             | PENDING  | [LOSER]        | —              |
| VEEV   | —          | —             | PENDING  |                | —              |
| VRT    | —          | —             | PENDING  | [AI]           | —              |
| WDAY   | —          | —             | PENDING  | [LOSER]        | —              |
| ZS     | —          | —             | PENDING  | [LOSER]        | —              |

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

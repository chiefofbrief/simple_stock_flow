# Session Notes

## Stock Tracking

### Suggested (from Daily Digests)
CEK, CMI, DIS, ENPH, GOOGL, HUBG, IT, MRCY, MU, NIO, NVO, ORCL, QCOM, STLA

### Suggested (Other Sources)
AMSC, AVGO, BSX, CLS, CSU, CVNA, LITE

### Pre-Screening (Context Mentions)
ADBE, CRM, HUBS, INTA, META, NOW, NVDA, SNOW, TTD

### Screened
AMZN, MSFT, PYPL, UNH

### Under Analysis
PYPL (sentiment + statement analysis complete)

### Analyzed
AMZN

---

## Trades

| Date | Ticker | Action | Price | Amount | Notes |
|------|--------|--------|-------|--------|-------|
| 2026-02-05 | AMZN | Buy | $222.71 | $4,999.84 | Individual ***4222. CapEx pivot to hyper-investment ($123B run-rate). Strong OCF ($116B), exceptional credit quality (Debt/OCF < 0.5). |

---

## Stock Context

### Big Tech: AI Demand Quotes (Q1/Q2 2026 Context)
- **Amazon**: "Monetizing capacity as fast as we can install it." Backlog $244B (+40% YoY). $200B CapEx predominant in AWS.
- **Google**: "Supply constrained even as we’ve been ramping up capacity." Backlog $240B (+55% QoQ).
- **Microsoft**: "Demand continues to exceed our supply." GitHub Copilot paid subscribers at 4.7M (+75% YoY). Commercial RPO at $625B.
- **Meta**: "Continue to be capacity constrained." 2026 CapEx range $115-$135B for Superintelligence Labs and core business.

### HUBG (Hub Group)
- **Incident**: Shares fell ~18% after disclosing a $77M financial reporting error (understated accounts payable and transportation costs).
- **Status**: Potential "fat pitch" or value trap depending on whether this is an isolated accounting lapse or indicative of deeper internal control failures.

### UNH
- **Thesis**: Structural shift in healthcare economics. UNH and Medicare Advantage (MA) players facing "margin death" as CMS rate increases (~0.9%) fail to keep pace with sticky healthcare inflation (labor, drugs).
- **Key Insight**: CMS uses lagging formulas and is constrained by federal deficit math. Era of easy ~6% annual rate increases likely over.
- **Risk**: Traditional "spread pricing" models becoming unworkable. Success depends on flawless execution in cost control and risk adjustment, not policy tailwinds.

### PYPL
- **Thesis**: "Cannibal Stock" - market pricing it like a "melting ice cube," but math supports margin of safety.
- **Details**: Even if business shrinks -5% annually, ~12% FCF yield used for buybacks results in ~+7% EPS growth.
- **Key Metrics**: 8.5x earnings, 0.2x Debt/EBITDA, ~11-12% FCF yield. Play on disciplined capital allocation, not top-line growth.
- **Sentiment** (Feb 8): Near-universal bearishness. CEO fired, branded checkout grew 1% in Q4, guidance withdrawn, targets slashed to $41-51. "Cannibal stock" thesis absent from public discourse.
- **Statement Analysis — Key Questions**:
    1. Is OCF/FCF holding up despite the EPS miss? (If yes, bear case weakens)
    2. Branded vs. unbranded (Braintree) revenue mix and margin difference?
    3. Buyback pace and capital allocation — still compelling at these levels?

### MSFT
- **Context**: Transition from high-margin SaaS/Azure cash cows to massive GPU CapEx.
- **Risk**: LLM profitability unproven and currently unprofitable. Increased LLM efficiency could reduce anticipated demand for compute.
- **Bullish Sign**: Public admission of "Windows AI bloat" suggests focus on optimization and performance.

---

## Open Items
(none)

## Open Decisions
- **Data File Synchronization (TBD)**: Current .gitignore tracks Daily analysis files but ignores raw data (JSON, ticker subdirectories).
    - **Current State**: Daily_Digest and Daily_Screening files sync via git. Raw JSON data does NOT sync.
    - **Options**: (1) Keep current (2) Track all data files (3) Hybrid snapshots (4) External storage
    - **Decision needed**: Depends on workflow - single environment vs frequent platform switching.

# Session Notes

## Stock Tracking

### Suggested
BSX, CEK, CMI, CVNA, DIS, ENPH, GOOGL, IT, MRCY, MSFT, MU, NIO, NVO, ORCL, PYPL, QCOM, UNH

### Screened
AMZN, MSFT, PYPL, UNH

### Under Analysis
*(None currently)*

### Analyzed
AMZN

---

## Trades

| Date | Ticker | Action | Price | Amount | Notes |
|------|--------|--------|-------|--------|-------|
| 2026-02-05 | AMZN | Buy | $222.71 | $4,999.84 | Individual ***4222. CapEx pivot to hyper-investment ($123B run-rate). Strong OCF ($116B), exceptional credit quality (Debt/OCF < 0.5). |

---

## Stock Context

### UNH
- **Thesis**: Structural shift in healthcare economics. UNH and Medicare Advantage (MA) players facing "margin death" as CMS rate increases (~0.9%) fail to keep pace with sticky healthcare inflation (labor, drugs).
- **Key Insight**: CMS uses lagging formulas and is constrained by federal deficit math. Era of easy ~6% annual rate increases likely over.
- **Risk**: Traditional "spread pricing" models becoming unworkable. Success depends on flawless execution in cost control and risk adjustment, not policy tailwinds.

### PYPL
- **Thesis**: "Cannibal Stock" - market pricing it like a "melting ice cube," but math supports margin of safety.
- **Details**: Even if business shrinks -5% annually, ~12% FCF yield used for buybacks results in ~+7% EPS growth.
- **Key Metrics**: 8.5x earnings, 0.2x Debt/EBITDA, ~11-12% FCF yield. Play on disciplined capital allocation, not top-line growth.

### MSFT
- **Context**: Transition from high-margin SaaS/Azure cash cows to massive GPU CapEx.
- **Risk**: LLM profitability unproven and currently unprofitable. Increased LLM efficiency could reduce anticipated demand for compute.
- **Bullish Sign**: Public admission of "Windows AI bloat" suggests focus on optimization and performance.

---

## Open Decisions
- **Data File Synchronization (TBD)**: Current .gitignore tracks Daily analysis files but ignores raw data (JSON, ticker subdirectories).
    - **Current State**: Daily_Digest and Daily_Screening files sync via git. Raw JSON data does NOT sync.
    - **Options**: (1) Keep current (2) Track all data files (3) Hybrid snapshots (4) External storage
    - **Decision needed**: Depends on workflow - single environment vs frequent platform switching.

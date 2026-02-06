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

## Analysis Notes

### Best Practices
- **External Data Sourcing**: When citing external data in analysis (not from scripts), explicitly state the source.
- **Investigation Items**: Favor slightly broader categories ("review earnings calls," "notes to financial statements") over overly specific items (e.g., naming a specific manipulation type).

### Examples
- **News Analysis (Narrative vs. Rotation)**: Note the facts, but don't accept the explanation at face value. Example: If AI hardware companies drop when Wall Street is supposedly afraid of SaaS being replaced by AI, it might just be a narrative concocted by the media. Often it's just a rotation of money out of broader tech back into other sectors like mining.

---

## Workflow Reference

### Definitions
- **"Screening"**: Specifically refers to running `scripts/valuation.py` script.

### Analysis Workflow Patterns
- **Statement Analysis**: Append analysis to TOP of `{TICKER}_statements.md` (not separate `_ANALYSIS_` file)
- **Sentiment Analysis**: Append analysis to TOP of `{TICKER}_sentiment.md` (not separate `_ANALYSIS_` file)
- **Screening Analysis**: Append analysis to TOP of `Daily_Screening_YYYY-MM-DD.txt` (not separate file)

### Open Decisions
- **Data File Synchronization (TBD)**: Current .gitignore tracks Daily analysis files but ignores raw data (JSON, ticker subdirectories).
    - **Current State**: Daily_Digest and Daily_Screening files sync via git. Raw JSON data does NOT sync.
    - **Options**: (1) Keep current (2) Track all data files (3) Hybrid snapshots (4) External storage
    - **Decision needed**: Depends on workflow - single environment vs frequent platform switching.

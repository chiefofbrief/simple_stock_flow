# Session Notes

## Stock Tracking

### Suggested
AMSC, AVGO, BSX, CEK, CLS, CMI, CSU, CVNA, DIS, ENPH, GOOGL, HUBG, IT, LITE, MRCY, MSFT, MU, NIO, NVO, ORCL, PYPL, QCOM, STLA, UNH

### Pre-Screening (Context Mentions)
ADBE, CRM, HUBS, INTA, META, NOW, NVDA, SNOW, TTD

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

### Software: Debt & "Vibe-Coding" Moats (CRM, NOW, HUBS, ADBE, SNOW, INTA, TTD)
- **Credit Market Risk**: Narrative shift as software selloff spreads to the debt market. Concerns that AI coding tools disrupt long-term terminal value are making it harder to refinance loans (many maturing by 2028).
- **The "Vibe-Coding" Counter-Thesis**: "You aren’t going to AI vibe-code a CRM at scale. Period."
    - Enterprise value is in the network, infrastructure, and deep integrations, not just the UI/code.
    - Switching costs remain astronomical for embedded enterprise workflows.
- **Excerpts/Sentiment**: 
    - Bullish sentiment noted for $HUBS, $SNOW, $CRM, $INTA, $ADBE, $TTD. 
    - $NOW (ServiceNow) viewed as transformative for enterprises with exceptionally high switching costs.
- **Key Observation**: Despite the "disruption" narrative, SaaS margins remain high and numbers aren't showing slowing due to AI; many are using AI to enhance existing software.

### Data Center Construction & Physical Constraints
- **JE Dunn Construction Context**: Data-center projects are scaling from 15% to 40% of portfolios. 2026 is an "Execution Year" with a surge in massive projects.
- **Redesign Risk**: Chip advances (e.g., Nvidia's warm-water cooling) can spark sudden data center redesigns, causing delays.
- **The "Cascading Earnings" Warning (Flexnode CEO)**: Physical holdups don't just snag construction money—they snag the "billions and billions of dollars of revenue that come off of the operation of that facility."

### Big Tech: AI Demand Quotes (Q1/Q2 2026 Context)
- **Amazon**: "Monetizing capacity as fast as we can install it." Backlog $244B (+40% YoY). $200B CapEx predominant in AWS.
- **Google**: "Supply constrained even as we’ve been ramping up capacity." Backlog $240B (+55% QoQ).
- **Microsoft**: "Demand continues to exceed our supply." GitHub Copilot paid subscribers at 4.7M (+75% YoY). Commercial RPO at $625B.
- **Meta**: "Continue to be capacity constrained." 2026 CapEx range $115-$135B for Superintelligence Labs and core business.

### HUBG (Hub Group)
- **Incident**: Shares fell ~18% after disclosing a $77M financial reporting error (understated accounts payable and transportation costs).
- **Status**: Potential "fat pitch" or value trap depending on whether this is an isolated accounting lapse or indicative of deeper internal control failures.

### Memory & Storage Sector (MU, SK Hynix, WDC, STX)
- **Research Thesis**: Evaluate if AI-driven CapEx is shifting memory from a commodity cycle to a structural AI bottleneck.
- **Market Narratives (to validate)**:
    - **Bottleneck Theory**: Some market participants argue memory capacity and bandwidth are now as critical as GPU compute for next-gen LLMs.
    - **Supply Duration**: UBS (Timothy Arcuri) projects DRAM shortages through C4Q27 and NAND shortages through C1Q27.
    - **Technical Leadership**: Sentiment often favors SK Hynix (000660) for HBM maturity, while Micron (MU) is viewed as the primary US-based beneficiary of supply constraints.
- **Key Data Points**: 
    - High reported profit margins (e.g., SanDisk at 67%) and "sold out" inventory status for 2026.
    - Related strength in optics/photonics (LITE, CLS, AVGO) as clusters scale.
- **Risks & Counter-Arguments**:
    - **Historical Cyclicality**: Memory has historically crashed after capacity overbuilds. Does "this time is different" hold up to FCF analysis?
    - **Geopolitical Shift**: China's scaling of DDR4/DDR5/HBM3 could erode non-US demand for tier-1 suppliers.
    - **Demand Elasticity**: Could high component prices trigger a pullback in consumer electronics (PC/Smartphone) volume?

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

## Open Items
- **Prompt structure consistency**: Aim for consistent structure across all prompts (particularly `screening_analysis.md`).
- **Financial Statement Red Flags**: Good content in `stock_analysis_guidelines.md` but needs reframing/rewording (currently overly prescriptive).

## Open Decisions
- **Data File Synchronization (TBD)**: Current .gitignore tracks Daily analysis files but ignores raw data (JSON, ticker subdirectories).
    - **Current State**: Daily_Digest and Daily_Screening files sync via git. Raw JSON data does NOT sync.
    - **Options**: (1) Keep current (2) Track all data files (3) Hybrid snapshots (4) External storage
    - **Decision needed**: Depends on workflow - single environment vs frequent platform switching.

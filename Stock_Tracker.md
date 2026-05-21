<!-- PRIORITY_COMPLETE -->
## Daily Priority — 2026-05-15

### Analyze Now
- **NFLX**: LOSER — EPS+ | P/E 28.8x | vs_1Y -25.1% | EPS YoY +86.4% | A large-cap brand name with a significant price dislocation despite accelerating fundamentals (EPS +86.4%, FCF +91.4%) and excellent ROIC (38.9%).
- **GEV**: TAILWIND — AI SC L8 | P/E 29.9x | vs_1Y +127.7% | EPS YoY +1816.5% | Promote from WATCHLIST; a Tier 1 TAILWIND where earnings are exploding (Avg QoQ +208.4%, FCF +391.4%) far faster than the stock price, directly validating the AI power constraint thesis.
- **INTU**: LOSER — EPS+ | P/E 25.0x | vs_1Y -42.2% | EPS YoY +47.9% | Promote from WATCHLIST; a high-quality, large-cap brand suffering a massive price dislocation (-42.2%) despite strong, accelerating fundamentals and high ROIC (19.6%).

### Add to Position
- **ADBE**: Price ($247.16) is below entry ($250.00) and fundamentals remain solid (EPS YoY +11.4%, Rev YoY +12.0%) despite the stock-specific dip on AI narrative concerns.
- **CRM**: Price ($175.13) is below entry ($181.70) with intact fundamentals (EPS YoY +18.3%, Rev YoY +12.1%), making the dip an opportunity to add to a quality position.

### Remove
- **CAG**: Remove | ROIC -1.0%, Rev YoY -1.9%, Debt/OCF 5.3x | The positive EPS YoY appears to be an anomaly contradicted by broad-based fundamental weakness, making it a low-quality signal.
- **LRCX**: Remove | Spread +213% | Tier 4 TAILWIND; price has significantly outrun earnings growth, and declining FCF YoY (-20.7%) breaks the thesis.
- **ZM**: Remove | vs_1Y +16.6% | The LOSER thesis is resolved as the price dislocation has normalized; re-evaluate on SOTP basis separately.
- **UMAC**: Remove | vs_1Y +178.7% | Price has exhausted the pre-profitability thesis; fundamentals (0/5 Yrs Profitable, negative FCF/Op Margin) do not support the valuation.
- **HON**: Remove | EPS YoY -41.9%, FCF YoY -352.3% | Tier 4 TAILWIND with broad-based deterioration across earnings, revenue, and cash flow.
- **BE**: Remove | Spread >150% (vs_1Y +1313.2%) | Tier 4 TAILWIND; extreme price appreciation has exhausted the reflexive thesis, and high leverage (Debt/OCF 9.2x) increases risk.
- **Promote to PIPELINE: AIG** | LOSER — EPS+ | A Tier 1 candidate with a cheap P/E (13.7x) and massive FCF YoY growth (+376.8%).
- **Promote to PIPELINE: EOG** | TAILWIND | Spread -6.2%; a Tier 1 TAILWIND with a cheap P/E (14.3x), good ROIC (16.1%), and strong FCF YoY (+83.0%).
- **Promote to PIPELINE: IT** | LOSER — EPS+ | A Tier 1 candidate with a massive dislocation (-66.2%), cheap P/E (15.0x), and exceptional ROIC (47.8%).

---
<!-- SC_LAYER_COVERAGE -->
Pipeline count by AI SC layer. Updated by `prompt_tracker_review.md` each run. ⚠ = zero PIPELINE tickers in layer.

```
L1  Raw Materials          — 1  (FCX)
L2  EDA / Semi Equipment   — 1  (CDNS)
L3  Foundry / OSAT         — 0  ⚠
L4  Compute Silicon        — 1  (NVDA)
L5  Memory                 — 1  (MU)
L6  Custom Silicon / NICs  — 0  ⚠
L7  Optical / Connectivity — 0  ⚠
L8  Power / Energy         — 0  ⚠
L9  Data Center Infra      — 0  ⚠
L10 Hyperscalers           — 1  (MSFT)
L11 AI Cloud / Neocloud    — 0  ⚠
L12 Edge AI / Robotics     — 1  (NVDA)
L13 AI Software / Apps     — 1  (IBM)
non-AI                     — 5  (BR, NFLX, WDAY, SAP, CAG)
```
<!-- /SC_LAYER_COVERAGE -->

---

# Ticker Tracker

---

## PIPELINE

Stocks under active analysis. Work through three passes sequentially per `GEMINI.md`: Context → The Numbers → The Projection. Verdict (Status) written once, at end of The Projection. Market data columns updated daily by `Scripts/tracker_update.py` (automated via GitHub Actions).

**Tier 1 criteria (required for PIPELINE):** LOSER—EPS+ tag (EPS YoY > 0 AND vs_1Y < 0) OR TAILWIND with Spread ≤ 0% (EPS YoY ≥ vs_1Y). Anything below Tier 1 belongs in WATCHLIST.

**Column Guide**
- **Tag**: `LOSER` or `TAILWIND` — see `GEMINI.md`. `LOSER — EPS+` auto-applied by script when EPS YoY > 0 and vs_1Y < 0.
- **Mkt Cap**: Market capitalization (updated by script)
- **vs_1Y**: Price change vs. 1 year ago (updated by script)
- **P/E**: GAAP TTM P/E — diluted EPS from income statement (updated by script)
- **ROIC**: TTM return on invested capital — NOPAT / (Equity + Debt - Cash). Measures capital efficiency independent of leverage. >20% indicates strong competitive advantage; <10% may signal value destruction (updated by script)
- **Avg EPS QoQ (4Q)**: Average of last 4 quarters of EPS QoQ change (updated by script)
- **EPS YoY**: Most recent quarter diluted EPS vs. same quarter prior year (updated by script)
- **Yrs Profitable (5yr)**: Profitable years out of last 5 (updated by script)
- **Rev YoY**: Most recent quarter revenue vs. same quarter prior year (updated by script)
- **FCF YoY**: Free cash flow year-over-year change (updated by script)
- **Op Margin %**: Operating margin TTM (updated by script)
- **Debt/OCF**: Total debt / TTM operating cash flow (updated by script)
- **Next Earnings**: Next scheduled earnings date (updated by script)
- **Phase**: `Context` → `The Numbers` → `The Projection` → `Complete`
- **Last Run**: Date of last completed workflow step
- **Status**: `REMOVE` | `MONITOR` | `BUY — ACCUMULATE` | `BUY — MEASURED` | `BUY — CONVICTION` — written only when Phase = `Complete`
- **Added**: Date added to PIPELINE

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | ROIC | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Phase | Last Run | Status | Thesis | Added |
|--------|-----|---------|-------|-----|---|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|-------|----------|--------|--------|-------|
| BR | LOSER — EPS+ | $17.28B | -37.4% | 16.0x | 20.1% | +17.2% | +15.1% | 5/5 | +7.8% | -17.6% | 17.1% | 2.5x | 2026-08-04 | Complete | 2026-04-30 | MONITOR | Thesis_BR.md | 2026-04-28 |
| NFLX | LOSER — EPS+ | $376.15B | -25.1% | 28.8x | 38.9% | +26.4% | +86.4% | 5/5 | +16.2% | +91.4% | 29.7% | 1.3x | 2026-07-16 | — | — | — | — | 2026-04-28 |
| WDAY | LOSER — EPS+ | $34.29B | -52.8% | 50.1x | 7.6% | +44.5% | +57.1% | 4/5 | +14.5% | +18.7% | 8.9% | 1.3x | 2026-05-21 | Complete | 2026-05-10 | BUY — MEASURED | WDAY_Thesis.md | 2026-04-28 |
| SAP | LOSER — EPS+ | $208.34B | -39.5% | 28.1x | 23.1% | +2.8% | +9.3% | 5/5 | +6.0% | -9.4% | 26.9% | 0.0x | 2026-07-23 | Complete | 2026-05-06 | BUY — MEASURED | SAP_Thesis.md | 2026-04-28 |
| CAG | LOSER — EPS+ | $6.66B | -34.5% | — | -1.0% | -84.4% | +40.0% | 4/5 | -1.9% | -6.8% | 12.3% | 5.3x | 2026-07-09 | — | — | — | — | 2026-04-28 |
| MU | TAILWIND — AI SC L5 | $825.67B | +651.0% | 34.7x | 34.5% | +78.2% | +756.7% | 4/5 | +196.3% | -22.8% | 48.5% | 0.4x | 2026-06-24 | Complete | 2026-05-10 | MONITOR | MU_Thesis.md | 2026-04-28 |
| FCX | TAILWIND — AI SC L1 | $85.29B | +56.2% | 31.4x | 7.9% | +46.7% | +154.2% | 5/5 | +12.2% | +557.9% | 27.8% | 1.7x | 2026-07-22 | — | — | — | — | 2026-04-28 |
| MSFT | TAILWIND — AI SC L10 | $3.08T | -9.1% | 24.6x | 29.0% | +7.2% | +23.4% | 5/5 | +18.3% | -22.1% | 46.8% | 0.3x | 2026-07-29 | Complete | 2026-04-30 | MONITOR | MSFT_Thesis.md | 2026-04-28 |
| IBM | TAILWIND — AI SC L13 | $207.37B | -15.1% | 19.5x | 13.7% | +56.8% | +14.3% | 5/5 | +9.5% | +20.2% | 16.4% | 5.0x | 2026-07-22 | Complete | 2026-05-08 | BUY — MEASURED | IBM_Thesis.md | 2026-04-28 |
| NVDA | TAILWIND — AI SC L4/L12 | $5.37T | +65.0% | 45.2x | 76.1% | +20.8% | +97.8% | 5/5 | +73.2% | +124.4% | 60.4% | 0.1x | 2026-05-20 | — | — | — | — | 2026-04-28 |
| CDNS | TAILWIND — AI SC L2 | $93.08B | +4.6% | 78.2x | 15.3% | +14.7% | +23.0% | 5/5 | +18.7% | -33.8% | 31.1% | 1.9x | 2026-07-27 | — | — | — | — | 2026-04-28 |

---

## WATCHLIST

Stocks under continuous monitoring. Move to PIPELINE when Tier 1 criteria are met. Move to DROPPED if thesis fails.

**Column Guide** (market data columns same as PIPELINE; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (Tier 1 criteria now met — move to PIPELINE)
- **Notes**: Thesis context, entry signal criteria, and invalidation conditions

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | ROIC | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Status | Thesis | Notes | Added |
|--------|-----|---------|-------|-----|---|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|--------|--------|-------|-------|
| AMD | TAILWIND — AI SC L4 | ~$724B | +301.4% | 144.3x | 8.2% | ~+55% | +43.0% | 5/5 | +38.0% | ~+240% | 11.7% | 0.40x | 2026-08-04 | WATCHING | AMD_Thesis.md | **Full 3-pass analysis complete 2026-05-21. DOLLAR FOR A DOLLAR — slight downward skew. WATCHING.** Numbers: OCF $9.72B TTM, FCF $8.57B (23% margin), Debt/OCF 0.40x. Owner earnings (FCF−SBC) $6.81B → P/OE ~106x. ROIC 8.2% (below CoC; AMAT peer 36.3%). Amortization tail to mid-2030s ($16.2B remaining, $7.4B post-2030). Warrant vesting: 0 of 320M shares vested Mar 28, 2026 — dual conditions (GPU milestones + stock price targets); liability-classified, marks to market. Pass 2 key findings: (1) CPU TAM doubled to $120B by 2030 — AMD repositioned as CPU+GPU AI platform, additive TAMs; (2) Helios demand visibility "down to which data centers" — strongest demand language AMD has given for any product launch; (3) Stacy Rasgon Q1 Q&A evasion suggests ex-China AI GPU was flat-to-down sequentially in Q1 — H2 depends entirely on Helios executing; (4) Helios margins confirmed below corporate average, no timeline to convergence. Narrative STRONG; Catalyst PRESENT BUT BACK-LOADED — July 2026 Advancing AI event (nearest); Q3 2026 earnings (Oct/Nov) is first thesis-confirming data point (first Helios revenue). Conviction on business HIGH; conviction on investment at $444.50 LOW. **Promote to PIPELINE if:** vs_1Y ≤50% (price ~$270-300), OR ROIC >15% TTM AND warrant milestones confirmed commercially paced, OR FY2026 non-GAAP EPS ≥$7.00 AND ROIC crossing 10% TTM by Q3 2026. **Invalidation:** Q3 2026 Data Center revenue <$7.0B; non-GAAP GM <54% for 2 consecutive quarters; ROIC fails to cross 10% TTM by Q4 2026; warrant vesting surprise P&L charge; Meta/OpenAI GPU commitment reduction; Lisa Su or Jean Hu departure. | 2026-05-21 |
| TEAM | LOSER | $21.75B | -61.0% | — | -16.9% | -42.8% | -40.7% | 0/5 | +31.7% | -10.1% | -3.7% | 1.0x | 2026-08-06 | WATCHING | TEAM_Thesis.md | Full analysis complete 2026-05-08. MONITOR verdict. Owner earnings -$356M TTM (FCF-SBC); SBC 24-27% of revenue 4 consecutive years — no confirmed normalization. Revenue quality excellent (NRR >120%, RPO $4B +37%, 25.7% CAGR). Non-GAAP EPS beat amplified by restructuring add-back (~$0.86/share) absent from FY2025 comparisons. CEO explicit FY2027 GAAP profitability commitment (first in 11 public years). **Promote to PIPELINE if:** Aug 6 Q4 FY2026 shows SBC/Rev ≤21% AND organic cloud growth ≥20%. **Remove if:** SBC/Rev ≥25% in Q4 FY2026 OR FY2027 GAAP target deferred OR new restructuring plan in FY2027 Q1–Q2. | 2026-05-08 |
| ZM | LOSER | $28.38B | +16.6% | 15.6x | 22.1% | +24.0% | +91.4% | 5/5 | +5.3% | -18.7% | 23.1% | 0.0x | 2026-05-21 | WATCHING | ZM_Thesis.md | Synthesis complete 2026-05-06. MONITOR — SOTP: $7.8B cash + Anthropic stake (~0.6% est.; $3.6B at $600B Anthropic → core at 16.9x owner earnings). KEY WATCH: Q1 FY27 **2026-05-21** — beat+raise and Contact Center ARR disclosure is primary near-term catalyst test. Upgrade to BUY—MEASURED on: (1) price pullback to $85-90, OR (2) Anthropic IPO confirmed >$500B, OR (3) Contact Center $500M+ ARR at 50%+ growth. Invalidation: revenue <2% for 2+ qtrs, NRR below 95%, Anthropic IPO delayed past 2027. Counter-signal: insider selling (CEO -65.5%, COO -86.7%, CFO -24.8% in same 90-day window). | 2026-05-06 |
| AIG | LOSER — EPS+ | $41.14B | -5.7% | 13.7x | 7.2% | +16.8% | +21.6% | 4/5 | -1.8% | +376.8% | 14.7% | 2.6x | 2026-08-05 | WATCHING | — | FCF +408.8% diverging strongly from EPS — worth monitoring for earnings recovery confirmation. | — |
| CPB | LOSER | $5.93B | -40.2% | 11.0x | 7.7% | +16.8% | -17.2% | 5/5 | -4.5% | +56.4% | 12.1% | 6.2x | 2026-06-01 | WATCHING | — | FCF +56.4% and QoQ improving despite YoY decline — direction of travel improving. | — |
| INTU | LOSER — EPS+ | $105.76B | -42.2% | 25.0x | 19.6% | +121.6% | +47.9% | 5/5 | +17.4% | +46.8% | 27.1% | 1.1x | 2026-05-20 | WATCHING | INTU_Thesis.md | Synthesis complete 2026-04-23. MONITOR — entry signal: Q3 FY2026 (May 21) confirms TurboTax Live 35%+, revenue at high end of guidance, Credit Karma holds. Invalidation: TurboTax Live <20% growth, revenue <11%, IRS Direct File expansion. | — |
| IT | LOSER — EPS+ | $10.00B | -66.2% | 15.0x | 47.8% | +134.9% | +17.3% | 5/5 | -1.5% | +28.7% | 16.4% | 2.4x | 2026-08-04 | WATCHING | IT_Thesis.md | Synthesis complete 2026-04-24. MONITOR — BUY on entry conditions: (1) May 5 earnings confirms federal headwind peaking; (2) Post-May 18 litigation update favorable. Remove if either gate fails. | — |
| LULU | LOSER | $14.01B | -63.6% | 9.0x | 31.9% | +9.3% | -19.1% | 5/5 | +0.8% | -17.7% | 19.8% | 1.1x | 2026-06-04 | WATCHING | — | — | — |
| NOW | LOSER — EPS+ | $103.19B | -50.9% | 59.7x | 15.4% | +2.9% | +2.3% | 5/5 | +22.1% | +3.9% | 13.4% | 0.4x | 2026-07-22 | Complete | NOW_Thesis.md | **BUY — MEASURED** (2026-05-10). Owner earnings $2.60B; FCF P/FCF ~21x; forward P/S 6.1x — below historical fair value. Armis closed Apr 21; Now Assist raised to $1.5B target; sub gross margin FY2026 guide 81.5% (Q1 78% was partly one-time). Numbers STRONG. Catalyst: Q2 earnings ~Jul 22 (gross margin recovery, Now Assist pace, Armis contribution). Narrative building institutionally but not in price (−12% AH on beat-and-raise). **Upgrade to CONVICTION if Jul 22:** sub gross margin ≥79%, Now Assist H1 pace ≥$650M NNACV, Armis on guide. **Invalidation:** Q2 sub gross margin <77%; Now Assist cumulative implying <$1.0B FY; post-Armis ROIC <10% in H2 2027; organic growth <17% CC. | 2026-05-10 |
| NVO | LOSER — EPS+ | $198.77B | -32.3% | 1.6x | 39.2% | +20.4% | +67.1% | 5/5 | +24.0% | +20.4% | 45.3% | 1.2x | 2026-08-05 | WATCHING | — | P/E 1.8x and FCF -750.8% are almost certainly FMP data errors. Flag for manual audit before thesis decision. | — |
| DPZ | LOSER | $10.19B | -35.9% | 17.9x | 74.8% | +0.9% | -4.6% | 5/5 | +3.5% | -10.6% | 19.6% | 6.6x | 2026-07-20 | WATCHING | DPZ_Thesis.md | Demoted from PIPELINE 2026-04-28 — EPS YoY turned -5.0% (was +9.6%); lost LOSER—EPS+ tag. Debt/OCF 6.6x elevated. Promote back if next earnings recovers EPS. | 2026-04-15 |
| AXON | TAILWIND | $31.28B | -47.8% | 155.7x | 6.9% | +1693.8% | +89.8% | 5/5 | +33.7% | -5962.9% | 1.5% | 11.9x | 2026-08-03 | WATCHING | AXON_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; Financials phase analysis was in progress. Debt/OCF 9.0x and Op Margin 0.0% are concerns to resolve. | 2026-04-14 |
| META | TAILWIND — AI SC L10 | $1.53T | -5.3% | 21.9x | 23.4% | +172.1% | +62.4% | 5/5 | +33.1% | +19.3% | 41.2% | 0.7x | 2026-07-29 | Complete | META_Thesis.md | **BUY — ACCUMULATE (2026-05-10).** FoA quality exceptional (41% margins, 33% rev growth, OCF $124B TTM, GAAP P/E 21.8x vs. 28.3x 5yr avg). Muse Spark validated; value optimization suite $20B+ run rate (2×YoY); partnership ads $10B+ (2×YoY). Owner economics near-negative in 2026 (FCF ~$3B − SBC ~$22B ≈ −$19B at $135B capex midpoint). ROIC declining toward 16–19% by end-2026. $234.8B+ off-balance-sheet commitments. 2027 capex opaque — mgmt declined to guide, said they "continue to underestimate" compute needs. No discrete near-term catalyst; Q2 earnings is a data gate, not a re-rating event. Buy quality compounder at compressed multiple on weakness toward $580–600. **Invalidation:** ad rev growth <25% YoY for 2 qtrs; 2027 capex $150B+; ROIC TTM <15%; EU DSA fine >$5B; ad impression growth <10% YoY. | 2026-05-10 |
| RDDT | TAILWIND — AI SC L13 | $28.53B | +46.0% | 43.7x | 38.7% | +86.5% | +621.4% | 2/5 | +69.1% | +145.8% | 25.1% | 0.0x | 2026-07-30 | WATCHING | RDDT_Thesis.md | Filtered at Financials 2026-04-29 — 83× owner earnings (FCF−SBC) on 1/5 yrs profitability; 238.5% EPS growth is largely IPO SBC normalization artifact, not durable compounding. Re-entry: 2–3 consecutive profitable quarters surviving Q1 seasonal weakness + SBC/Rev declining toward 10% + data licensing revenue at material scale. | 2026-04-14 |
| UMAC | TAILWIND | $462.83M | +178.7% | — | -5.0% | -136.0% | +200.0% | 0/5 | +296.4% | -1417.3% | -168.9% | — | 2026-08-13 | WATCHING | UMAC_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; FCF -705.6%, Op Margin -224.6%. Price has outrun pre-profitability thesis. | 2026-04-14 |
| BKH | TAILWIND — AI SC L8 | $5.58B | +28.6% | 19.1x | 5.4% | +60.8% | -7.5% | 5/5 | -3.0% | -221.8% | 23.3% | 7.5x | 2026-07-29 | WATCHING | BKH_Thesis.md | Tier 2 spread +26.8%; FCF -67.8% and Debt/OCF 7.0x are concerns. | — |
| CCJ | TAILWIND — AI SC L1 | $45.34B | +97.9% | 69.0x | 14.2% | +37582.8% | +93.8% | 4/5 | +7.1% | -286.1% | 16.6% | 0.6x | 2026-07-31 | WATCHING | — | Tier 3 spread +111.9%; Avg QoQ is near-zero base noise. | — |
| CSCO | TAILWIND — AI SC L7 | $459.21B | +86.6% | 38.6x | 18.1% | +8.3% | +37.1% | 5/5 | +12.0% | -6.1% | 23.4% | 2.4x | 2026-08-12 | WATCHING | — | Tier 2 spread +23.6% — approaching Tier 1; clean fundamentals. | 2026-04-28 |
| GEV | TAILWIND — AI SC L8 | $274.45B | +127.7% | 29.9x | 121.0% | +208.4% | +1816.5% | 2/5 | +16.1% | +391.4% | 3.9% | 0.3x | 2026-07-22 | WATCHING | — | Tier 1 spread by math (-1623%) but base-effect distortion (prior EPS near-zero). QoQ +208.7% and FCF +391.4% are the real signals. Op Margin 3.9% is thin. | — |
| GOOGL | TAILWIND — AI SC L10 | $4.75T | +138.9% | 29.8x | 30.2% | +21.5% | +81.9% | 5/5 | +21.8% | -46.6% | 32.7% | 0.5x | 2026-07-22 | WATCHING | — | Tier 3 spread +87.2%; strong fundamentals but price has meaningfully outrun earnings. | — |
| KLAC | TAILWIND — AI SC L2 | $232.52B | +126.8% | 50.4x | 48.3% | +3.0% | +11.8% | 5/5 | +11.5% | -37.0% | 42.1% | 1.4x | 2026-07-30 | WATCHING | — | Tier 3 spread +121.4%; QoQ flat — deceleration signal. | — |
| LRCX | TAILWIND — AI SC L2 | $351.54B | +233.4% | 52.6x | 71.7% | +9.9% | +40.8% | 5/5 | +23.8% | -20.7% | 34.3% | 0.5x | 2026-07-29 | WATCHING | — | Tier 4 spread +213%; FCF declining. | — |
| MP | TAILWIND — AI SC L1 | $9.76B | +173.7% | — | -2.0% | -31.7% | +71.4% | 3/5 | +118.6% | +15.4% | -39.4% | — | 2026-08-06 | WATCHING | — | Tier 2 spread +10.4%; no GAAP earnings, FCF -877.9% — pre-profitability. | — |
| MRVL | TAILWIND — AI SC L6 | $163.96B | +198.8% | 59.6x | 17.7% | +203.4% | +100.0% | 1/5 | +22.1% | -41.5% | 16.3% | 2.6x | 2026-05-27 | WATCHING | — | Tier 3 spread +57.5%; Avg QoQ +194.7% strong but YoY masks recent deceleration. | — |
| QCOM | TAILWIND — AI SC L12 | $204.91B | +31.0% | 21.1x | 28.3% | +32.6% | +173.0% | 5/5 | -3.5% | -18.1% | 25.5% | 1.1x | 2026-07-29 | WATCHING | — | Tier 2 spread +5.7%; EPS barely negative, QoQ fading — approaching Tier 1 if EPS recovers. | — |
| SNPS | TAILWIND — AI SC L2 | $91.02B | -6.7% | 73.7x | 4.3% | -9.6% | -78.8% | 5/5 | +65.5% | +859.5% | 10.8% | 4.1x | 2026-05-27 | Complete | SNPS_Thesis.md | HOLD — FAIRLY VALUED. GAAP EPS depressed by Ansys amortization ($394M/qtr); honest owner earnings P/E ~42x vs. headline 34x non-GAAP. EDA duopoly moat confirmed; monetization gap real; joint solution revenue FY2027+. Q2 (May 27) is thesis-critical: IP sequential improvement required. EV ≈ $476 vs. $495 price. | 2026-05-15 |
| TSM | TAILWIND — AI SC L3 | $2.06T | +107.8% | 1.1x | 48.5% | +12.2% | +58.4% | 5/5 | +35.1% | +27.9% | 53.2% | 0.5x | 2026-07-16 | Complete | TSM_Thesis.md | BUY — MEASURED. Tier 3 spread +82.3%; P/E 1.0x is a confirmed FMP data error (correct: ~34.8x trailing). Upgrade to CONVICTION on Oct print if N3 margin crossover confirms or pricing shift signals. | 2026-05-08 |
| VRT | TAILWIND — AI SC L9 | $124.43B | +207.3% | 82.0x | 30.4% | +29.8% | +135.7% | 5/5 | +30.1% | +147.3% | 18.5% | 1.2x | 2026-07-29 | WATCHING | — | Tier 3 spread +117.3%; large run partially justified by earnings acceleration. | — |
| BE | TAILWIND — AI SC L8 | $75.55B | +1313.2% | — | 3.6% | +1394.8% | +330.0% | 2/5 | +130.4% | +138.0% | 8.2% | 9.2x | 2026-07-30 | WATCHING | — | Prior removal flag stale — EPS YoY reversed to +350.0% (was -99.1%). vs_1Y +1076.6% and Debt/OCF 9.1x remain concerns. Reassess from current data. | — |
| AMAT | TAILWIND — AI SC L2 | $332.66B | +154.1% | 39.2x | 36.3% | +9.2% | +33.5% | 5/5 | +11.4% | -21.6% | 29.5% | 0.8x | 2026-08-13 | WATCHING | — | Tier 3 spread +80.1%; earnings accelerating, FCF +91.2%. | 2026-04-28 |
| ANET | TAILWIND — AI SC L7 | $179.46B | +48.7% | 48.7x | 34.8% | +5.9% | +25.0% | 5/5 | +35.1% | +167.2% | 42.8% | 0.0x | 2026-08-04 | WATCHING | — | Tier 3 spread +92.3%; dominant AI networking, clean balance sheet. | 2026-04-28 |
| ARM | TAILWIND — AI SC L2/L4 | $257.88B | +73.4% | 270.5x | 15.1% | +19.2% | +45.0% | 4/5 | +20.1% | +1.1% | 18.3% | 0.3x | 2026-07-29 | WATCHING | — | Tier 4 — EPS declining at P/E 264.9x; architecture royalty thesis not yet in GAAP numbers. | 2026-04-28 |
| ASML | TAILWIND — AI SC L2 | $578.98B | +101.8% | 58.0x | 64.3% | +6.4% | +22.6% | 5/5 | +13.2% | -466.3% | 34.8% | 0.3x | 2026-07-15 | WATCHING | Complete | Tier 3 spread +85.0%; EUV monopoly structural premium; FCF YoY extreme negative likely one-time. | 2026-05-12 |
| AMKR | TAILWIND — AI SC L3 | $16.41B | +250.7% | 38.4x | 10.1% | +68.4% | +288.2% | 5/5 | +27.5% | -42.6% | 7.6% | 1.3x | 2026-07-27 | WATCHING | AMKR_Thesis.md | **Full thesis complete 2026-05-21. DOLLAR FOR A DOLLAR — marginally below parity. WATCHING.** CRITICAL L3 OSAT; adj P/E ~43.7x (useful life ext +$0.20 EPS). FCF ~-$1.4-1.9B in 2026; NOT self-funding. Apple 29.8% revenue (concentration risk). 5+ HDFO customers (broadening). Supply constraint $50-100M/quarter pushout risk. **Upgrade to BUY—MEASURED on:** (1) pullback to $48-55; OR (2) Q2 earnings Jul 27 confirms EPS ≥ $0.47 + computing growing share + GM ≥ 15%; OR (3) CHIPS Act first disbursement announced. **Invalidation:** AI packaging < 2× by Q3 Oct earnings; GM < 13% any H2 qtr; Apple diversifies sourcing; dilutive equity raise; ROIC < 8% TTM. Bear ~$28-31; Bull ~$70-75. | — |
| AVGO | TAILWIND — AI SC L6 | $1.96T | +80.0% | 80.8x | 21.2% | +15.9% | +31.6% | 5/5 | +29.5% | +33.2% | 40.9% | 2.2x | 2026-06-03 | WATCHING | — | Tier 3 estimated; data not yet pulled — run tracker_update.py to populate. | — |
| GLW | TAILWIND — AI SC L7 | $154.43B | +284.2% | 86.5x | 10.7% | +46.7% | +138.9% | 5/5 | +20.0% | +152.6% | 15.3% | 3.1x | 2026-08-04 | WATCHING | — | Tier 3 spread +113%; re-rating from depressed base; QoQ solid. | — |
| HON | TAILWIND — AI SC L9 | $137.15B | -1.4% | 30.8x | 12.3% | +30.9% | -41.9% | 5/5 | -6.9% | -352.3% | 14.9% | 6.6x | 2026-07-23 | WATCHING | — | Tier 4 — EPS declining -42.4%, FCF -352.3%. Thesis needs catalyst before promoting. | 2026-04-28 |
| JCI | TAILWIND — AI SC L9 | $83.57B | +41.6% | 24.4x | 16.3% | +36.9% | +38.9% | 5/5 | +8.2% | +19.6% | 13.6% | 5.4x | 2026-08-04 | WATCHING | — | Tier 3 spread +42.1%; earnings and FCF genuinely growing; Debt/OCF 5.4x borderline. | 2026-04-28 |
| ORCL | TAILWIND — AI SC L13 | $515.73B | +13.4% | 32.3x | 12.2% | +17.5% | +24.5% | 5/5 | +21.7% | -16274.6% | 30.8% | 6.9x | 2026-06-10 | WATCHING | — | Tier 2 spread +2.3% — near Tier 1; FCF YoY -16274.6% is almost certainly a data error; manual audit needed. | 2026-04-28 |
| SNOW | TAILWIND — AI SC L13 | $57.57B | -9.4% | — | -71.6% | -0.1% | +9.1% | 0/5 | +30.1% | +81.5% | -30.6% | 2.2x | 2026-05-27 | WATCHING | — | Spread -19.4% but EPS still deeply negative GAAP (0/5 profitable). Rev +30.1% and FCF +81.5% are the real signals. Promote only when GAAP turns positive. | 2026-04-28 |
| COP | TAILWIND | $152.71B | +44.4% | 21.3x | 9.8% | -1.0% | -20.2% | 5/5 | -2.5% | +56.9% | 18.3% | 1.3x | 2026-08-06 | WATCHING | — | ConocoPhillips — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| EOG | TAILWIND | $77.26B | +33.4% | 14.3x | 16.1% | +33.8% | +39.6% | 5/5 | +15.7% | +83.0% | 36.9% | 0.8x | 2026-08-06 | WATCHING | — | EOG Resources — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| LIN | TAILWIND — AI SC L1 | $234.18B | +11.8% | 33.7x | 12.1% | +4.4% | +13.4% | 5/5 | +8.2% | +0.8% | 28.8% | 2.4x | 2026-08-07 | WATCHING | — | Linde — industrial/process gases for semiconductor fabs. Run tracker_update.py to populate. | 2026-04-28 |
| APD | TAILWIND — AI SC L1 | $64.74B | +8.5% | 30.8x | 6.4% | +3441.2% | +141.1% | 5/5 | +8.8% | +250.6% | 18.4% | 4.5x | 2026-07-30 | WATCHING | — | Air Products and Chemicals — industrial gases, hydrogen. Run tracker_update.py to populate. | 2026-04-28 |
| INTC | TAILWIND — AI SC L3/L4 | $590.86B | +448.4% | — | -0.8% | -160.0% | -284.2% | 2/5 | +7.2% | +41.9% | -9.4% | 4.5x | 2026-07-23 | WATCHING | INTC_Thesis.md | Thesis complete 2026-05-14. MONITOR — dollar for $1.30 at $116.14; narrative STRONG, Numbers ABSENT, Catalyst MODERATE. Intel Products healthy (32% margins, six consecutive guidance beats, supply-constrained); Intel Foundry losing $2.4B/qtr (-45% margins). 18A yields ahead of schedule; advanced packaging demand upgraded to "billions/year"; Google LTA + multiple anonymous LTAs signed. ASIC business doubled YoY. Entry signal: pullback to $75-85 OR Apple confirmed at commercial scale (>$1B foundry revenue). Catalysts: Q2 earnings 2026-07-23, H2 2026 14A commitments, H2 Analyst Day. **Invalidation:** (1) 14A PDK 1.0 delayed past Q4 2026; (2) Apple absent from H2 2026 LTA announcements; (3) 18A yields stall below 60% by Q3 2026; (4) Foundry gross margin not neutral by Q4 2027; (5) Zinsner FCF/breakeven guidance materially withdrawn; (6) Lip-Bu Tan departure. Run tracker_update.py to populate market data. | 2026-05-14 |

---

## SC Layer Coverage

<!-- SC_LAYER_COVERAGE -->
Pipeline count by AI SC layer. Updated by `prompt_tracker_review.md` each run. ⚠ = zero PIPELINE tickers in layer.

```
L1  Raw Materials          — 1  (FCX)
L2  EDA / Semi Equipment   — 1  (CDNS)
L3  Foundry / OSAT         — 0  ⚠ (TSM, INTC in WATCHLIST)
L4  Compute Silicon        — 1  (NVDA)
L5  Memory                 — 1  (MU)
L6  Custom Silicon / NICs  — 0  ⚠ (MRVL, AVGO Tier 3 in WATCHLIST)
L7  Optical / Connectivity — 0  ⚠ (CSCO Tier 2, ANET Tier 3 in WATCHLIST)
L8  Power / Energy         — 0  ⚠ (BE reassessing, BKH/GEV Tier 2–3)
L9  Data Center Infra      — 0  ⚠ (VRT, JCI Tier 3 in WATCHLIST)
L10 Hyperscalers           — 1  (MSFT)
L11 AI Cloud / Neocloud    — 0  ⚠ No actionable candidates remaining
L12 Edge AI / Robotics     — 0  ⚠ (QCOM Tier 2 in WATCHLIST)
L13 AI Software / Apps     — 1  (IBM)
non-AI                     — 0  (AXON, UMAC in WATCHLIST)
```
<!-- /SC_LAYER_COVERAGE -->

---

## DROPPED

Thesis failed, dislocation resolved, or better alternatives found. No market data maintained.

| Ticker | Tag | Date | Reason |
|--------|-----|------|--------|
| AVAV | TAILWIND — AI SC L12 | 2026-04-28 | Dislocation reversed — vs_1Y +31.8%; EPS YoY -5150% disqualifies TAILWIND thesis. |
| TH | TAILWIND — AI SC L9 | 2026-04-28 | EPS YoY -215.4% AND Avg QoQ -487.1% — both horizons negative; thesis broken. |
| CC | TAILWIND | 2026-04-28 | EPS YoY -649.1%, Avg QoQ -2361.8%, Debt/OCF 17.4x — no thesis support. |
| USAR | TAILWIND — AI SC L1 | 2026-04-28 | Pre-revenue; EPS -1092%, FCF -8014.4% — beyond speculative threshold for this framework. |
| CARR | TAILWIND — AI SC L9 | 2026-04-28 | EPS YoY -97.8%, Avg QoQ -38.1% — both negative; FCF spike likely one-time working capital release. |
| VST | TAILWIND — AI SC L8 | 2026-04-28 | EPS YoY -52.6%, Rev YoY -68.2%, FCF -108.9% — earnings thesis broken across all measures. |
| CRWV | TAILWIND — AI SC L11 | 2026-04-28 | EPS YoY -423.5%, Avg QoQ -144.2% — both negative; L11 gap noted, no replacement identified. |
| LEN | LOSER | 2026-04-28 | EPS YoY -52.0%, Avg QoQ -12.0%, Debt/OCF 24.3x — both earnings horizons declining, extreme leverage. |
| PFE | TAILWIND | 2026-04-28 | Post-COVID earnings collapse — EPS YoY -500.6%, Rev -1.2%, FCF -22.4%. No AI thesis. |
| T | TAILWIND | 2026-04-28 | EPS YoY -11.5%, FCF -43.8%, revenue barely growing. No catalyst. |

---

## Trade Tracker

Market data columns updated daily by `Scripts/tracker_update.py`. Use Price vs. Entry Price to identify add-to-position opportunities.

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Price | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY | Rev YoY | Next Earnings | Thesis |
|--------|------------|-------------|--------|------------|-------|-------|-----|------------------|---------|---------|---------------|--------|
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | $247.16 | -40.8% | 14.4x | +2.8% | +11.4% | +12.0% | 2026-06-11 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | $260.46 | +27.6% | 31.2x | +16.1% | +74.8% | +16.6% | 2026-07-30 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | $175.13 | -38.7% | 22.5x | +5.1% | +18.3% | +12.1% | 2026-05-27 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | $738.44 | +25.5% | — | — | — | — | — | — |

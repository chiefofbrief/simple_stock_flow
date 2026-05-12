<!-- PRIORITY_COMPLETE -->
## Daily Priority — 2026-05-19

### Analyze Now
1.  **INTU | LOSER — EPS+ | P/E 25.5x | vs_1Y -40.1% | EPS YoY +47.9% | Phase —**: Promote from WATCHLIST; a high-quality business with a deep price dislocation, strong earnings growth, and an earnings report tomorrow (May 20) makes this the highest-priority analysis.
2.  **NVDA | TAILWIND — AI SC L4 | P/E 44.8x | vs_1Y +78.5% | EPS YoY +97.8% | Phase —**: Earnings are still outpacing the stock's significant run-up, and with the next report tomorrow (May 20), analyzing the central company in the AI thesis is non-negotiable.
3.  **GEV | TAILWIND — AI SC L8 | P/E 31.4x | vs_1Y +158.1% | EPS YoY +1816.5% | Phase —**: Promote from WATCHLIST; explosive earnings and FCF growth (+391.4%) provide the strongest quantitative signal yet that the power-as-bottleneck thesis is moving from narrative to financial reality.

### Add to Position
- **ADBE**: Price ($247.00) is below entry ($250.00) with earnings intact (EPS YoY +11.4%) and a clear deep-value narrative forming in the market; the price dip is a gift.
- **CRM**: Price ($177.49) is below entry ($181.70) with solid earnings (EPS YoY +18.3%) and positive fundamental developments (Agentforce launch); the thesis is holding.

### Remove
- **CAG**: Remove from PIPELINE. Trigger: Low quality (ROIC -1.0%, Rev/FCF declining) and high debt (Debt/OCF 5.3x) undermine the LOSER thesis despite EPS+ tag.
- **ZM**: Remove from WATCHLIST. Trigger: vs_1Y +29.6%. The price dislocation has resolved; it no longer fits the LOSER thesis.
- **LRCX**: Remove from WATCHLIST. Trigger: Spread +221.7%. Price has massively outrun earnings (Tier 4), and FCF is declining.
- **HON**: Remove from WATCHLIST. Trigger: EPS YoY -41.9% and FCF YoY -352.3%. The thesis is broken across multiple dimensions.
- **BE**: Remove from WATCHLIST. Trigger: Spread >150% (Tier 4) and Debt/OCF 9.2x. Extreme price move (+1401.4% vs_1Y) has inverted the risk/reward profile.
- **Promote to PIPELINE: AIG**. A LOSER—EPS+ candidate (vs_1Y -6.8%, EPS YoY +21.6%) with a powerful FCF YoY signal (+376.8%) that warrants deeper analysis.

---
<!-- SC_LAYER_COVERAGE -->
Pipeline count by AI SC layer. Updated by `prompt_tracker_review.md` each run. ⚠ = zero PIPELINE tickers in layer.

```
L1  Raw Materials          — 1  (FCX)
L2  EDA / Semi Equipment   — 1  (CDNS)
L3  Foundry / OSAT         — 0  ⚠
L4  Compute Silicon        — 1  (NVDA)
L5  Memory Silicon         — 1  (MU)
L6  Custom Silicon / NICs  — 0  ⚠
L7  Optical / Connectivity — 0  ⚠
L8  Power / Energy         — 1  (GEV)
L9  Data Center Infra      — 0  ⚠
L10 Hyperscalers           — 1  (MSFT)
L11 AI Cloud / Neocloud    — 0  ⚠
L12 Edge AI / Robotics     — 0  ⚠
L13 AI Software / Apps     — 1  (IBM)
non-AI                     — 6  (BR, NFLX, WDAY, SAP, INTU, AIG)
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
| BR | LOSER — EPS+ | $17.25B | -36.0% | 16.0x | 20.1% | +17.2% | +15.1% | 5/5 | +7.8% | -17.6% | 17.1% | 2.5x | 2026-08-04 | Complete | 2026-04-30 | MONITOR | Thesis_BR.md | 2026-04-28 |
| NFLX | LOSER — EPS+ | $359.81B | -23.0% | 27.6x | 38.9% | +26.4% | +86.4% | 5/5 | +16.2% | +91.4% | 29.7% | 1.3x | 2026-07-16 | — | — | — | — | 2026-04-28 |
| WDAY | LOSER — EPS+ | $32.19B | -54.5% | 47.1x | 7.6% | +44.5% | +57.1% | 4/5 | +14.5% | +18.7% | 8.9% | 1.3x | 2026-05-21 | Complete | 2026-05-10 | BUY — MEASURED | WDAY_Thesis.md | 2026-04-28 |
| SAP | LOSER — EPS+ | $198.21B | -40.8% | 26.7x | 23.1% | +2.8% | +9.3% | 5/5 | +6.0% | -9.4% | 26.9% | 0.0x | 2026-07-23 | Complete | 2026-05-06 | BUY — MEASURED | SAP_Thesis.md | 2026-04-28 |
| CAG | LOSER — EPS+ | $6.66B | -35.1% | — | -1.0% | -84.4% | +40.0% | 4/5 | -1.9% | -6.8% | 12.3% | 5.3x | 2026-07-09 | — | — | — | — | 2026-04-28 |
| MU | TAILWIND — AI SC L5 | $896.92B | +763.8% | 37.5x | 34.5% | +78.2% | +756.7% | 4/5 | +196.3% | -22.8% | 48.5% | 0.4x | 2026-06-24 | Complete | 2026-05-10 | MONITOR | MU_Thesis.md | 2026-04-28 |
| FCX | TAILWIND — AI SC L1 | $92.52B | +66.5% | 34.1x | 7.9% | +46.7% | +154.2% | 5/5 | +12.2% | +557.9% | 27.8% | 1.7x | 2026-07-22 | — | — | — | — | 2026-04-28 |
| MSFT | TAILWIND — AI SC L10 | $3.07T | -7.4% | 24.6x | 29.0% | +7.2% | +23.4% | 5/5 | +18.3% | -22.1% | 46.8% | 0.3x | 2026-07-29 | Complete | 2026-04-30 | MONITOR | MSFT_Thesis.md | 2026-04-28 |
| IBM | TAILWIND — AI SC L13 | $210.11B | -9.6% | 19.8x | 13.7% | +56.8% | +14.3% | 5/5 | +9.5% | +20.2% | 16.4% | 5.0x | 2026-07-22 | Complete | 2026-05-08 | BUY — MEASURED | IBM_Thesis.md | 2026-04-28 |
| NVDA | TAILWIND — AI SC L4/L12 | $5.33T | +78.5% | 44.8x | 76.1% | +20.8% | +97.8% | 5/5 | +73.2% | +124.4% | 60.4% | 0.1x | 2026-05-20 | — | — | — | — | 2026-04-28 |
| CDNS | TAILWIND — AI SC L2 | $100.45B | +16.8% | 84.9x | 15.3% | +14.7% | +23.0% | 5/5 | +18.7% | -33.8% | 31.1% | 1.9x | 2026-07-27 | — | — | — | — | 2026-04-28 |

---

## WATCHLIST

Stocks under continuous monitoring. Move to PIPELINE when Tier 1 criteria are met. Move to DROPPED if thesis fails.

**Column Guide** (market data columns same as PIPELINE; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (Tier 1 criteria now met — move to PIPELINE)
- **Notes**: Thesis context, entry signal criteria, and invalidation conditions

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | ROIC | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Status | Thesis | Notes | Added |
|--------|-----|---------|-------|-----|---|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|--------|--------|-------|-------|
| TEAM | LOSER | $22.93B | -61.0% | — | -16.9% | -42.8% | -40.7% | 0/5 | +31.7% | -10.1% | -3.7% | 1.0x | 2026-08-06 | WATCHING | TEAM_Thesis.md | Full analysis complete 2026-05-08. MONITOR verdict. Owner earnings -$356M TTM (FCF-SBC); SBC 24-27% of revenue 4 consecutive years — no confirmed normalization. Revenue quality excellent (NRR >120%, RPO $4B +37%, 25.7% CAGR). Non-GAAP EPS beat amplified by restructuring add-back (~$0.86/share) absent from FY2025 comparisons. CEO explicit FY2027 GAAP profitability commitment (first in 11 public years). **Promote to PIPELINE if:** Aug 6 Q4 FY2026 shows SBC/Rev ≤21% AND organic cloud growth ≥20%. **Remove if:** SBC/Rev ≥25% in Q4 FY2026 OR FY2027 GAAP target deferred OR new restructuring plan in FY2027 Q1–Q2. | 2026-05-08 |
| ZM | LOSER | $31.57B | +29.6% | 17.3x | 22.1% | +24.0% | +91.4% | 5/5 | +5.3% | -18.7% | 23.1% | 0.0x | 2026-05-21 | WATCHING | ZM_Thesis.md | Synthesis complete 2026-05-06. MONITOR — SOTP: $7.8B cash + Anthropic stake (~0.6% est.; $3.6B at $600B Anthropic → core at 16.9x owner earnings). KEY WATCH: Q1 FY27 **2026-05-21** — beat+raise and Contact Center ARR disclosure is primary near-term catalyst test. Upgrade to BUY—MEASURED on: (1) price pullback to $85-90, OR (2) Anthropic IPO confirmed >$500B, OR (3) Contact Center $500M+ ARR at 50%+ growth. Invalidation: revenue <2% for 2+ qtrs, NRR below 95%, Anthropic IPO delayed past 2027. Counter-signal: insider selling (CEO -65.5%, COO -86.7%, CFO -24.8% in same 90-day window). | 2026-05-06 |
| AIG | LOSER — EPS+ | $40.33B | -6.8% | 13.4x | 7.2% | +16.8% | +21.6% | 4/5 | -1.8% | +376.8% | 14.7% | 2.6x | 2026-08-05 | WATCHING | — | FCF +408.8% diverging strongly from EPS — worth monitoring for earnings recovery confirmation. | — |
| CPB | LOSER | $6.15B | -39.2% | 11.2x | 7.7% | +16.8% | -17.2% | 5/5 | -4.5% | +56.4% | 12.1% | 6.2x | 2026-06-01 | WATCHING | — | FCF +56.4% and QoQ improving despite YoY decline — direction of travel improving. | — |
| INTU | LOSER — EPS+ | $109.44B | -40.1% | 25.5x | 19.6% | +121.6% | +47.9% | 5/5 | +17.4% | +46.8% | 27.1% | 1.1x | 2026-05-20 | WATCHING | INTU_Thesis.md | Synthesis complete 2026-04-23. MONITOR — entry signal: Q3 FY2026 (May 21) confirms TurboTax Live 35%+, revenue at high end of guidance, Credit Karma holds. Invalidation: TurboTax Live <20% growth, revenue <11%, IRS Direct File expansion. | — |
| IT | LOSER — EPS+ | $10.30B | -65.6% | 15.2x | 47.8% | +134.9% | +17.3% | 5/5 | -1.5% | +28.7% | 16.4% | 2.4x | 2026-08-04 | WATCHING | IT_Thesis.md | Synthesis complete 2026-04-24. MONITOR — BUY on entry conditions: (1) May 5 earnings confirms federal headwind peaking; (2) Post-May 18 litigation update favorable. Remove if either gate fails. | — |
| LULU | LOSER | $14.82B | -58.5% | 9.5x | 31.9% | +9.3% | -19.1% | 5/5 | +0.8% | -17.7% | 19.8% | 1.1x | 2026-06-04 | WATCHING | — | — | — |
| NOW | LOSER — EPS+ | $94.35B | -55.0% | 54.5x | 15.4% | +2.9% | +2.3% | 5/5 | +22.1% | +3.9% | 13.4% | 0.4x | 2026-07-22 | Complete | NOW_Thesis.md | **BUY — MEASURED** (2026-05-10). Owner earnings $2.60B; FCF P/FCF ~21x; forward P/S 6.1x — below historical fair value. Armis closed Apr 21; Now Assist raised to $1.5B target; sub gross margin FY2026 guide 81.5% (Q1 78% was partly one-time). Numbers STRONG. Catalyst: Q2 earnings ~Jul 22 (gross margin recovery, Now Assist pace, Armis contribution). Narrative building institutionally but not in price (−12% AH on beat-and-raise). **Upgrade to CONVICTION if Jul 22:** sub gross margin ≥79%, Now Assist H1 pace ≥$650M NNACV, Armis on guide. **Invalidation:** Q2 sub gross margin <77%; Now Assist cumulative implying <$1.0B FY; post-Armis ROIC <10% in H2 2027; organic growth <17% CC. | 2026-05-10 |
| NVO | LOSER — EPS+ | $206.19B | -29.1% | 1.7x | 39.2% | +20.4% | +67.1% | 5/5 | +24.0% | +20.4% | 45.3% | 1.2x | 2026-08-05 | WATCHING | — | P/E 1.8x and FCF -750.8% are almost certainly FMP data errors. Flag for manual audit before thesis decision. | — |
| DPZ | LOSER | $10.42B | -33.9% | 18.0x | 74.8% | +0.9% | -4.6% | 5/5 | +3.5% | -10.6% | 19.6% | 6.6x | 2026-07-20 | WATCHING | DPZ_Thesis.md | Demoted from PIPELINE 2026-04-28 — EPS YoY turned -5.0% (was +9.6%); lost LOSER—EPS+ tag. Debt/OCF 6.6x elevated. Promote back if next earnings recovers EPS. | 2026-04-15 |
| AXON | TAILWIND | $31.79B | -43.1% | 158.2x | 6.9% | +1693.8% | +89.8% | 5/5 | +33.7% | -5962.9% | 1.5% | 11.9x | 2026-08-03 | WATCHING | AXON_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; Financials phase analysis was in progress. Debt/OCF 9.0x and Op Margin 0.0% are concerns to resolve. | 2026-04-14 |
| META | TAILWIND — AI SC L10 | $1.52T | -6.1% | 21.8x | 23.4% | +172.1% | +62.4% | 5/5 | +33.1% | +19.3% | 41.2% | 0.7x | 2026-07-29 | Complete | META_Thesis.md | **BUY — ACCUMULATE (2026-05-10).** FoA quality exceptional (41% margins, 33% rev growth, OCF $124B TTM, GAAP P/E 21.8x vs. 28.3x 5yr avg). Muse Spark validated; value optimization suite $20B+ run rate (2×YoY); partnership ads $10B+ (2×YoY). Owner economics near-negative in 2026 (FCF ~$3B − SBC ~$22B ≈ −$19B at $135B capex midpoint). ROIC declining toward 16–19% by end-2026. $234.8B+ off-balance-sheet commitments. 2027 capex opaque — mgmt declined to guide, said they "continue to underestimate" compute needs. No discrete near-term catalyst; Q2 earnings is a data gate, not a re-rating event. Buy quality compounder at compressed multiple on weakness toward $580–600. **Invalidation:** ad rev growth <25% YoY for 2 qtrs; 2027 capex $150B+; ROIC TTM <15%; EU DSA fine >$5B; ad impression growth <10% YoY. | 2026-05-10 |
| RDDT | TAILWIND — AI SC L13 | $30.71B | +43.4% | 45.2x | 38.7% | +86.5% | +621.4% | 2/5 | +69.1% | +145.8% | 25.1% | 0.0x | 2026-07-30 | WATCHING | RDDT_Thesis.md | Filtered at Financials 2026-04-29 — 83× owner earnings (FCF−SBC) on 1/5 yrs profitability; 238.5% EPS growth is largely IPO SBC normalization artifact, not durable compounding. Re-entry: 2–3 consecutive profitable quarters surviving Q1 seasonal weakness + SBC/Rev declining toward 10% + data licensing revenue at material scale. | 2026-04-14 |
| UMAC | TAILWIND | $596.50M | +187.8% | — | -25.8% | -152.7% | +88.6% | 1/5 | +144.4% | -705.6% | -224.6% | — | 2026-05-14 | WATCHING | UMAC_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; FCF -705.6%, Op Margin -224.6%. Price has outrun pre-profitability thesis. | 2026-04-14 |
| BKH | TAILWIND — AI SC L8 | $5.59B | +31.9% | 19.1x | 5.4% | +60.8% | -7.5% | 5/5 | -3.0% | -221.8% | 23.3% | 7.5x | 2026-07-29 | WATCHING | BKH_Thesis.md | Tier 2 spread +26.8%; FCF -67.8% and Debt/OCF 7.0x are concerns. | — |
| CCJ | TAILWIND — AI SC L1 | $52.32B | +135.3% | 80.1x | 14.2% | +37582.8% | +93.8% | 4/5 | +7.1% | -286.1% | 16.6% | 0.6x | 2026-07-31 | WATCHING | — | Tier 3 spread +111.9%; Avg QoQ is near-zero base noise. | — |
| CSCO | TAILWIND — AI SC L7 | $389.93B | +63.7% | 35.6x | 17.6% | +6.8% | +29.5% | 5/5 | +9.7% | +5.6% | 22.7% | 2.3x | 2026-05-13 | WATCHING | — | Tier 2 spread +23.6% — approaching Tier 1; clean fundamentals. | 2026-04-28 |
| GEV | TAILWIND — AI SC L8 | $288.36B | +158.1% | 31.4x | 121.0% | +208.4% | +1816.5% | 2/5 | +16.1% | +391.4% | 3.9% | 0.3x | 2026-07-22 | WATCHING | — | Tier 1 spread by math (-1623%) but base-effect distortion (prior EPS near-zero). QoQ +208.7% and FCF +391.4% are the real signals. Op Margin 3.9% is thin. | — |
| GOOGL | TAILWIND — AI SC L10 | $4.70T | +146.1% | 29.6x | 30.2% | +21.5% | +81.9% | 5/5 | +21.8% | -46.6% | 32.7% | 0.5x | 2026-07-22 | WATCHING | — | Tier 3 spread +87.2%; strong fundamentals but price has meaningfully outrun earnings. | — |
| KLAC | TAILWIND — AI SC L2 | $241.03B | +144.5% | 52.2x | 48.3% | +3.0% | +11.8% | 5/5 | +11.5% | -37.0% | 42.1% | 1.4x | 2026-07-30 | WATCHING | — | Tier 3 spread +121.4%; QoQ flat — deceleration signal. | — |
| LRCX | TAILWIND — AI SC L2 | $370.23B | +262.5% | 55.9x | 71.7% | +9.9% | +40.8% | 5/5 | +23.8% | -20.7% | 34.3% | 0.5x | 2026-07-29 | WATCHING | — | Tier 4 spread +213%; FCF declining. | — |
| MP | TAILWIND — AI SC L1 | $11.98B | +218.9% | — | -4.3% | -31.7% | +71.4% | 3/5 | +118.6% | +15.4% | -39.4% | — | 2026-08-06 | WATCHING | — | Tier 2 spread +10.4%; no GAAP earnings, FCF -877.9% — pre-profitability. | — |
| MRVL | TAILWIND — AI SC L6 | $149.39B | +165.6% | 55.6x | 17.7% | +203.4% | +100.0% | 1/5 | +22.1% | -41.5% | 16.3% | 2.6x | 2026-05-27 | WATCHING | — | Tier 3 spread +57.5%; Avg QoQ +194.7% strong but YoY masks recent deceleration. | — |
| QCOM | TAILWIND — AI SC L12 | $250.36B | +59.8% | 25.5x | 28.3% | +32.6% | +173.0% | 5/5 | -3.5% | -18.1% | 25.5% | 1.1x | 2026-07-29 | WATCHING | — | Tier 2 spread +5.7%; EPS barely negative, QoQ fading — approaching Tier 1 if EPS recovers. | — |
| SNPS | TAILWIND — AI SC L2 | $98.88B | +2.1% | 79.0x | 4.3% | -9.6% | -78.8% | 5/5 | +65.5% | +859.5% | 10.8% | 4.1x | 2026-05-27 | WATCHING | — | EPS collapsing (-79.1%) but FCF +859.5% — major divergence; determine if GAAP EPS is distorted by one-time items before removal. | — |
| TSM | TAILWIND — AI SC L3 | $2.10T | +118.4% | 1.1x | 49.5% | +12.2% | +58.4% | 5/5 | +35.1% | +27.9% | 53.2% | 0.4x | 2026-07-16 | Complete | TSM_Thesis.md | BUY — MEASURED. Tier 3 spread +82.3%; P/E 1.0x is a confirmed FMP data error (correct: ~34.8x trailing). Upgrade to CONVICTION on Oct print if N3 margin crossover confirms or pricing shift signals. | 2026-05-08 |
| VRT | TAILWIND — AI SC L9 | $141.32B | +264.6% | 92.4x | 30.4% | +29.8% | +135.7% | 5/5 | +30.1% | +147.3% | 18.5% | 1.2x | 2026-07-29 | WATCHING | — | Tier 3 spread +117.3%; large run partially justified by earnings acceleration. | — |
| BE | TAILWIND — AI SC L8 | $68.26B | +1401.4% | — | 3.6% | +1394.8% | +330.0% | 2/5 | +130.4% | +138.0% | 8.2% | 9.2x | 2026-07-30 | WATCHING | — | Prior removal flag stale — EPS YoY reversed to +350.0% (was -99.1%). vs_1Y +1076.6% and Debt/OCF 9.1x remain concerns. Reassess from current data. | — |
| AMAT | TAILWIND — AI SC L2 | $352.06B | +166.4% | 45.5x | 37.2% | +20.0% | +75.2% | 5/5 | -2.1% | +91.2% | 29.1% | 0.8x | 2026-05-14 | WATCHING | — | Tier 3 spread +80.1%; earnings accelerating, FCF +91.2%. | 2026-04-28 |
| ANET | TAILWIND — AI SC L7 | $171.79B | +47.8% | 46.7x | 34.8% | +5.9% | +25.0% | 5/5 | +35.1% | +167.2% | 42.8% | 0.0x | 2026-08-04 | WATCHING | — | Tier 3 spread +92.3%; dominant AI networking, clean balance sheet. | 2026-04-28 |
| ARM | TAILWIND — AI SC L2/L4 | $226.26B | +70.4% | 253.2x | 15.1% | +19.2% | +45.0% | 4/5 | +20.1% | +1.1% | 18.3% | 0.3x | 2026-07-29 | WATCHING | — | Tier 4 — EPS declining at P/E 264.9x; architecture royalty thesis not yet in GAAP numbers. | 2026-04-28 |
| ASML | TAILWIND — AI SC L2 | $603.49B | +110.4% | 60.5x | 64.3% | +6.4% | +22.6% | 5/5 | +13.2% | -466.3% | 34.8% | 0.3x | 2026-07-15 | WATCHING | Complete | Tier 3 spread +85.0%; EUV monopoly structural premium; FCF YoY extreme negative likely one-time. | 2026-05-12 |
| AMKR | TAILWIND — AI SC L3 | $19.01B | +295.5% | 43.8x | 10.1% | +68.4% | +288.2% | 5/5 | +27.5% | -42.6% | 7.6% | 1.3x | 2026-07-27 | WATCHING | — | Tier 2 spread +17.9% (vs_1Y +313.2% minus EPS YoY +295.3%); EPS, FCF, and Rev all genuinely strong. | — |
| AVGO | TAILWIND — AI SC L6 | $2.03T | +94.9% | 83.7x | 21.2% | +15.9% | +31.6% | 5/5 | +29.5% | +33.2% | 40.9% | 2.2x | 2026-06-03 | WATCHING | — | Tier 3 estimated; data not yet pulled — run tracker_update.py to populate. | — |
| GLW | TAILWIND — AI SC L7 | $175.97B | +340.9% | 97.1x | 10.7% | +46.7% | +138.9% | 5/5 | +20.0% | +152.6% | 15.3% | 3.1x | 2026-08-04 | WATCHING | — | Tier 3 spread +113%; re-rating from depressed base; QoQ solid. | — |
| HON | TAILWIND — AI SC L9 | $139.09B | +2.1% | 31.1x | 12.3% | +30.9% | -41.9% | 5/5 | -6.9% | -352.3% | 14.9% | 6.6x | 2026-07-23 | WATCHING | — | Tier 4 — EPS declining -42.4%, FCF -352.3%. Thesis needs catalyst before promoting. | 2026-04-28 |
| JCI | TAILWIND — AI SC L9 | $85.98B | +50.0% | 25.2x | 16.3% | +36.9% | +38.9% | 5/5 | +8.2% | +19.6% | 13.6% | 5.4x | 2026-08-04 | WATCHING | — | Tier 3 spread +42.1%; earnings and FCF genuinely growing; Debt/OCF 5.4x borderline. | 2026-04-28 |
| ORCL | TAILWIND — AI SC L13 | $553.41B | +23.5% | 34.5x | 12.2% | +17.5% | +24.5% | 5/5 | +21.7% | -16274.6% | 30.8% | 6.9x | 2026-06-10 | WATCHING | — | Tier 2 spread +2.3% — near Tier 1; FCF YoY -16274.6% is almost certainly a data error; manual audit needed. | 2026-04-28 |
| SNOW | TAILWIND — AI SC L13 | $53.13B | -14.9% | — | -71.6% | -0.1% | +9.1% | 0/5 | +30.1% | +81.5% | -30.6% | 2.2x | 2026-05-27 | WATCHING | — | Spread -19.4% but EPS still deeply negative GAAP (0/5 profitable). Rev +30.1% and FCF +81.5% are the real signals. Promote only when GAAP turns positive. | 2026-04-28 |
| COP | TAILWIND | $142.22B | +31.7% | 19.8x | 9.8% | -1.0% | -20.2% | 5/5 | -2.5% | +56.9% | 18.3% | 1.3x | 2026-08-06 | WATCHING | — | ConocoPhillips — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| EOG | TAILWIND | $71.05B | +21.0% | 13.1x | 16.1% | +33.8% | +39.6% | 5/5 | +15.7% | +83.0% | 36.9% | 0.8x | 2026-08-06 | WATCHING | — | EOG Resources — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| LIN | TAILWIND — AI SC L1 | $233.55B | +12.5% | 33.5x | 12.1% | +4.4% | +13.4% | 5/5 | +8.2% | +0.8% | 28.8% | 2.4x | 2026-08-07 | WATCHING | — | Linde — industrial/process gases for semiconductor fabs. Run tracker_update.py to populate. | 2026-04-28 |
| APD | TAILWIND — AI SC L1 | $67.83B | +13.2% | 32.2x | 6.4% | +3441.2% | +141.1% | 5/5 | +8.8% | +250.6% | 18.4% | 4.5x | 2026-07-30 | WATCHING | — | Air Products and Chemicals — industrial gases, hydrogen. Run tracker_update.py to populate. | 2026-04-28 |

---

## SC Layer Coverage

<!-- SC_LAYER_COVERAGE -->
Pipeline count by AI SC layer. Updated by `prompt_tracker_review.md` each run. ⚠ = zero PIPELINE tickers in layer.

```
L1  Raw Materials          — 1  (FCX)
L2  EDA / Semi Equipment   — 1  (CDNS)
L3  Foundry / OSAT         — 0  ⚠ (TSM Tier 3 in WATCHLIST)
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
| INTC | TAILWIND — AI SC L3/L4 | 2026-04-28 | EPS YoY -284.2%, Avg QoQ -160.0%, Op Margin -9.4%; price +312.1% — turnaround not in numbers. |
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
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | $247.00 | -37.6% | 14.4x | +2.8% | +11.4% | +12.0% | 2026-06-11 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | $266.06 | +27.5% | 31.8x | +16.1% | +74.8% | +16.6% | 2026-07-30 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | $177.49 | -38.1% | 22.8x | +5.1% | +18.3% | +12.1% | 2026-05-27 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | $740.30 | +28.0% | — | — | — | — | — | — |

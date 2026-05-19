<!-- PRIORITY_COMPLETE -->
## Daily Priority — 2026-05-15

### Analyze Now
- **NFLX** | LOSER — EPS+ | P/E 29.0x | ROIC 38.9% | vs_1Y -24.5% | EPS YoY +86.4% | Phase — | A high-quality large-cap with stellar fundamentals (ROIC 39%, FCF YoY +91%) whose price is dislocated -25% while EPS grew +86%.
- **Promote to PIPELINE: INTU** | LOSER — EPS+ | P/E 26.9x | ROIC 19.6% | vs_1Y -37.7% | EPS YoY +47.9% | WATCHING | A massive -38% dislocation in a high-quality business with strong EPS/FCF growth and earnings on May 20 makes analysis urgent.
- **FCX** | TAILWIND — AI SC L1 | P/E 31.4x | ROIC 7.9% | vs_1Y +54.8% | EPS YoY +154.2% | Phase — | A Tier 1 TAILWIND where earnings are massively outpacing price (EPS YoY +154% vs vs_1Y +55%) and confirmed by explosive FCF growth (+558%).

### Add to Position
None.

### Remove
- **CAG** | Broad fundamental decay (ROIC -1.0%, Rev YoY -1.9%, FCF YoY -6.8%) | Remove
- **ZM** | vs_1Y +18.6% | Remove — Dislocation has resolved; LOSER thesis no longer applies.
- **AXON** | FCF YoY -5962.9%, Debt/OCF 11.9x | Remove — Growth is not translating to cash and leverage is too high; TAILWIND thesis broken.
- **LRCX** | Spread +189.6% (Tier 4) | Remove — Price has significantly outrun decelerating earnings; thesis broken.
- **HON** | Broad deterioration (EPS YoY -41.9%, Rev YoY -6.9%, FCF YoY -352.3%) | Remove — TAILWIND thesis broken across multiple dimensions.
- **BE** | Spread >150% (vs_1Y +1242.2%), Debt/OCF 9.2x | Remove — Extreme price appreciation and high debt suggest reflexivity is exhausted.

**Promote to PIPELINE: AIG** — Meets Tier 1 LOSER—EPS+ criteria (vs_1Y -5.5%, EPS YoY +21.6%) with strong FCF YoY +376.8%.
**Promote to PIPELINE: IT** — Meets Tier 1 LOSER—EPS+ criteria with a massive dislocation (vs_1Y -64.6%) and excellent quality metrics (ROIC 47.8%).
**Promote to PIPELINE: AMKR** — Meets Tier 1 TAILWIND criteria with a spread of -51.5% (EPS YoY +288.2% vs. vs_1Y +236.7%).
**Promote to PIPELINE: ORCL** — Meets Tier 1 TAILWIND criteria with a spread of -6.4% (EPS YoY +24.5% vs. vs_1Y +18.1%) and earnings on June 10.

---
<!-- SC_LAYER_COVERAGE -->
Pipeline count by AI SC layer. Updated by `prompt_tracker_review.md` each run. ⚠ = zero PIPELINE tickers in layer.

```
L1  Raw Materials          — 1  (FCX)
L2  EDA / Semi Equipment   — 1  (CDNS)
L3  Foundry / OSAT         — 1  (AMKR)
L4  Compute Silicon        — 1  (NVDA)
L5  Memory                 — 1  (MU)
L6  Custom Silicon / NICs  — 0  ⚠
L7  Optical / Connectivity — 0  ⚠
L8  Power / Energy         — 0  ⚠
L9  Data Center Infra      — 0  ⚠
L10 Hyperscalers           — 1  (MSFT)
L11 AI Cloud / Neocloud    — 0  ⚠
L12 Edge AI / Robotics     — 1  (NVDA)
L13 AI Software / Apps     — 2  (IBM, ORCL)
non-AI                     — 7  (BR, NFLX, WDAY, SAP, AIG, IT, INTU)
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
| BR | LOSER — EPS+ | $17.34B | -37.2% | 16.1x | 20.1% | +17.2% | +15.1% | 5/5 | +7.8% | -17.6% | 17.1% | 2.5x | 2026-08-04 | Complete | 2026-04-30 | MONITOR | Thesis_BR.md | 2026-04-28 |
| NFLX | LOSER — EPS+ | $379.19B | -24.5% | 29.0x | 38.9% | +26.4% | +86.4% | 5/5 | +16.2% | +91.4% | 29.7% | 1.3x | 2026-07-16 | — | — | — | — | 2026-04-28 |
| WDAY | LOSER — EPS+ | $34.95B | -51.6% | 51.3x | 7.6% | +44.5% | +57.1% | 4/5 | +14.5% | +18.7% | 8.9% | 1.3x | 2026-05-21 | Complete | 2026-05-10 | BUY — MEASURED | WDAY_Thesis.md | 2026-04-28 |
| SAP | LOSER — EPS+ | $212.57B | -38.1% | 28.7x | 23.1% | +2.8% | +9.3% | 5/5 | +6.0% | -9.4% | 26.9% | 0.0x | 2026-07-23 | Complete | 2026-05-06 | BUY — MEASURED | SAP_Thesis.md | 2026-04-28 |
| CAG | LOSER — EPS+ | $6.62B | -34.7% | — | -1.0% | -84.4% | +40.0% | 4/5 | -1.9% | -6.8% | 12.3% | 5.3x | 2026-07-09 | — | — | — | — | 2026-04-28 |
| MU | TAILWIND — AI SC L5 | $774.12B | +604.4% | 32.7x | 34.5% | +78.2% | +756.7% | 4/5 | +196.3% | -22.8% | 48.5% | 0.4x | 2026-06-24 | Complete | 2026-05-10 | MONITOR | MU_Thesis.md | 2026-04-28 |
| FCX | TAILWIND — AI SC L1 | $84.99B | +54.8% | 31.4x | 7.9% | +46.7% | +154.2% | 5/5 | +12.2% | +557.9% | 27.8% | 1.7x | 2026-07-22 | — | — | — | — | 2026-04-28 |
| MSFT | TAILWIND — AI SC L10 | $3.16T | -6.8% | 25.3x | 29.0% | +7.2% | +23.4% | 5/5 | +18.3% | -22.1% | 46.8% | 0.3x | 2026-07-29 | Complete | 2026-04-30 | MONITOR | MSFT_Thesis.md | 2026-04-28 |
| IBM | TAILWIND — AI SC L13 | $210.06B | -14.3% | 19.8x | 13.7% | +56.8% | +14.3% | 5/5 | +9.5% | +20.2% | 16.4% | 5.0x | 2026-07-22 | Complete | 2026-05-08 | BUY — MEASURED | IBM_Thesis.md | 2026-04-28 |
| NVDA | TAILWIND — AI SC L4/L12 | $5.38T | +63.4% | 45.2x | 76.1% | +20.8% | +97.8% | 5/5 | +73.2% | +124.4% | 60.4% | 0.1x | 2026-05-20 | — | — | — | — | 2026-04-28 |
| CDNS | TAILWIND — AI SC L2 | $95.14B | +8.2% | 80.8x | 15.3% | +14.7% | +23.0% | 5/5 | +18.7% | -33.8% | 31.1% | 1.9x | 2026-07-27 | — | — | — | — | 2026-04-28 |

---

## WATCHLIST

Stocks under continuous monitoring. Move to PIPELINE when Tier 1 criteria are met. Move to DROPPED if thesis fails.

**Column Guide** (market data columns same as PIPELINE; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (Tier 1 criteria now met — move to PIPELINE)
- **Notes**: Thesis context, entry signal criteria, and invalidation conditions

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | ROIC | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Status | Thesis | Notes | Added |
|--------|-----|---------|-------|-----|---|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|--------|--------|-------|-------|
| TEAM | LOSER | $23.98B | -57.1% | — | -16.9% | -42.8% | -40.7% | 0/5 | +31.7% | -10.1% | -3.7% | 1.0x | 2026-08-06 | WATCHING | TEAM_Thesis.md | Full analysis complete 2026-05-08. MONITOR verdict. Owner earnings -$356M TTM (FCF-SBC); SBC 24-27% of revenue 4 consecutive years — no confirmed normalization. Revenue quality excellent (NRR >120%, RPO $4B +37%, 25.7% CAGR). Non-GAAP EPS beat amplified by restructuring add-back (~$0.86/share) absent from FY2025 comparisons. CEO explicit FY2027 GAAP profitability commitment (first in 11 public years). **Promote to PIPELINE if:** Aug 6 Q4 FY2026 shows SBC/Rev ≤21% AND organic cloud growth ≥20%. **Remove if:** SBC/Rev ≥25% in Q4 FY2026 OR FY2027 GAAP target deferred OR new restructuring plan in FY2027 Q1–Q2. | 2026-05-08 |
| ZM | LOSER | $28.95B | +18.6% | 16.0x | 22.1% | +24.0% | +91.4% | 5/5 | +5.3% | -18.7% | 23.1% | 0.0x | 2026-05-21 | WATCHING | ZM_Thesis.md | Synthesis complete 2026-05-06. MONITOR — SOTP: $7.8B cash + Anthropic stake (~0.6% est.; $3.6B at $600B Anthropic → core at 16.9x owner earnings). KEY WATCH: Q1 FY27 **2026-05-21** — beat+raise and Contact Center ARR disclosure is primary near-term catalyst test. Upgrade to BUY—MEASURED on: (1) price pullback to $85-90, OR (2) Anthropic IPO confirmed >$500B, OR (3) Contact Center $500M+ ARR at 50%+ growth. Invalidation: revenue <2% for 2+ qtrs, NRR below 95%, Anthropic IPO delayed past 2027. Counter-signal: insider selling (CEO -65.5%, COO -86.7%, CFO -24.8% in same 90-day window). | 2026-05-06 |
| AIG | LOSER — EPS+ | $41.30B | -5.5% | 13.7x | 7.2% | +16.8% | +21.6% | 4/5 | -1.8% | +376.8% | 14.7% | 2.6x | 2026-08-05 | WATCHING | — | FCF +408.8% diverging strongly from EPS — worth monitoring for earnings recovery confirmation. | — |
| CPB | LOSER | $6.08B | -39.2% | 11.1x | 7.7% | +16.8% | -17.2% | 5/5 | -4.5% | +56.4% | 12.1% | 6.2x | 2026-06-01 | WATCHING | — | FCF +56.4% and QoQ improving despite YoY decline — direction of travel improving. | — |
| INTU | LOSER — EPS+ | $114.83B | -37.7% | 26.9x | 19.6% | +121.6% | +47.9% | 5/5 | +17.4% | +46.8% | 27.1% | 1.1x | 2026-05-20 | WATCHING | INTU_Thesis.md | Synthesis complete 2026-04-23. MONITOR — entry signal: Q3 FY2026 (May 21) confirms TurboTax Live 35%+, revenue at high end of guidance, Credit Karma holds. Invalidation: TurboTax Live <20% growth, revenue <11%, IRS Direct File expansion. | — |
| IT | LOSER — EPS+ | $10.63B | -64.6% | 15.7x | 47.8% | +134.9% | +17.3% | 5/5 | -1.5% | +28.7% | 16.4% | 2.4x | 2026-08-04 | WATCHING | IT_Thesis.md | Synthesis complete 2026-04-24. MONITOR — BUY on entry conditions: (1) May 5 earnings confirms federal headwind peaking; (2) Post-May 18 litigation update favorable. Remove if either gate fails. | — |
| LULU | LOSER | $13.87B | -63.3% | 9.0x | 31.9% | +9.3% | -19.1% | 5/5 | +0.8% | -17.7% | 19.8% | 1.1x | 2026-06-04 | WATCHING | — | — | — |
| NOW | LOSER — EPS+ | $110.43B | -47.6% | 64.0x | 15.4% | +2.9% | +2.3% | 5/5 | +22.1% | +3.9% | 13.4% | 0.4x | 2026-07-22 | Complete | NOW_Thesis.md | **BUY — MEASURED** (2026-05-10). Owner earnings $2.60B; FCF P/FCF ~21x; forward P/S 6.1x — below historical fair value. Armis closed Apr 21; Now Assist raised to $1.5B target; sub gross margin FY2026 guide 81.5% (Q1 78% was partly one-time). Numbers STRONG. Catalyst: Q2 earnings ~Jul 22 (gross margin recovery, Now Assist pace, Armis contribution). Narrative building institutionally but not in price (−12% AH on beat-and-raise). **Upgrade to CONVICTION if Jul 22:** sub gross margin ≥79%, Now Assist H1 pace ≥$650M NNACV, Armis on guide. **Invalidation:** Q2 sub gross margin <77%; Now Assist cumulative implying <$1.0B FY; post-Armis ROIC <10% in H2 2027; organic growth <17% CC. | 2026-05-10 |
| NVO | LOSER — EPS+ | $196.86B | -31.5% | 1.6x | 39.2% | +20.4% | +67.1% | 5/5 | +24.0% | +20.4% | 45.3% | 1.2x | 2026-08-05 | WATCHING | — | P/E 1.8x and FCF -750.8% are almost certainly FMP data errors. Flag for manual audit before thesis decision. | — |
| DPZ | LOSER | $10.23B | -37.3% | 17.7x | 74.8% | +0.9% | -4.6% | 5/5 | +3.5% | -10.6% | 19.6% | 6.6x | 2026-07-20 | WATCHING | DPZ_Thesis.md | Demoted from PIPELINE 2026-04-28 — EPS YoY turned -5.0% (was +9.6%); lost LOSER—EPS+ tag. Debt/OCF 6.6x elevated. Promote back if next earnings recovers EPS. | 2026-04-15 |
| AXON | TAILWIND | $31.39B | -47.4% | 156.8x | 6.9% | +1693.8% | +89.8% | 5/5 | +33.7% | -5962.9% | 1.5% | 11.9x | 2026-08-03 | WATCHING | AXON_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; Financials phase analysis was in progress. Debt/OCF 9.0x and Op Margin 0.0% are concerns to resolve. | 2026-04-14 |
| META | TAILWIND — AI SC L10 | $1.54T | -4.8% | 22.1x | 23.4% | +172.1% | +62.4% | 5/5 | +33.1% | +19.3% | 41.2% | 0.7x | 2026-07-29 | Complete | META_Thesis.md | **BUY — ACCUMULATE (2026-05-10).** FoA quality exceptional (41% margins, 33% rev growth, OCF $124B TTM, GAAP P/E 21.8x vs. 28.3x 5yr avg). Muse Spark validated; value optimization suite $20B+ run rate (2×YoY); partnership ads $10B+ (2×YoY). Owner economics near-negative in 2026 (FCF ~$3B − SBC ~$22B ≈ −$19B at $135B capex midpoint). ROIC declining toward 16–19% by end-2026. $234.8B+ off-balance-sheet commitments. 2027 capex opaque — mgmt declined to guide, said they "continue to underestimate" compute needs. No discrete near-term catalyst; Q2 earnings is a data gate, not a re-rating event. Buy quality compounder at compressed multiple on weakness toward $580–600. **Invalidation:** ad rev growth <25% YoY for 2 qtrs; 2027 capex $150B+; ROIC TTM <15%; EU DSA fine >$5B; ad impression growth <10% YoY. | 2026-05-10 |
| RDDT | TAILWIND — AI SC L13 | $30.61B | +47.5% | 45.1x | 38.7% | +86.5% | +621.4% | 2/5 | +69.1% | +145.8% | 25.1% | 0.0x | 2026-07-30 | WATCHING | RDDT_Thesis.md | Filtered at Financials 2026-04-29 — 83× owner earnings (FCF−SBC) on 1/5 yrs profitability; 238.5% EPS growth is largely IPO SBC normalization artifact, not durable compounding. Re-entry: 2–3 consecutive profitable quarters surviving Q1 seasonal weakness + SBC/Rev declining toward 10% + data licensing revenue at material scale. | 2026-04-14 |
| UMAC | TAILWIND | $527.12M | +154.8% | — | -5.0% | -136.0% | +200.0% | 0/5 | +296.4% | -1417.3% | -168.9% | — | 2026-08-13 | WATCHING | UMAC_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; FCF -705.6%, Op Margin -224.6%. Price has outrun pre-profitability thesis. | 2026-04-14 |
| BKH | TAILWIND — AI SC L8 | $5.63B | +29.9% | 19.2x | 5.4% | +60.8% | -7.5% | 5/5 | -3.0% | -221.8% | 23.3% | 7.5x | 2026-07-29 | WATCHING | BKH_Thesis.md | Tier 2 spread +26.8%; FCF -67.8% and Debt/OCF 7.0x are concerns. | — |
| CCJ | TAILWIND — AI SC L1 | $44.56B | +102.2% | 68.9x | 14.2% | +37582.8% | +93.8% | 4/5 | +7.1% | -286.1% | 16.6% | 0.6x | 2026-07-31 | WATCHING | — | Tier 3 spread +111.9%; Avg QoQ is near-zero base noise. | — |
| CSCO | TAILWIND — AI SC L7 | $463.36B | +88.8% | 39.3x | 18.1% | +8.3% | +37.1% | 5/5 | +12.0% | -6.1% | 23.4% | 2.4x | 2026-08-12 | WATCHING | — | Tier 2 spread +23.6% — approaching Tier 1; clean fundamentals. | 2026-04-28 |
| GEV | TAILWIND — AI SC L8 | $269.66B | +126.0% | 29.4x | 121.0% | +208.4% | +1816.5% | 2/5 | +16.1% | +391.4% | 3.9% | 0.3x | 2026-07-22 | WATCHING | — | Tier 1 spread by math (-1623%) but base-effect distortion (prior EPS near-zero). QoQ +208.7% and FCF +391.4% are the real signals. Op Margin 3.9% is thin. | — |
| GOOGL | TAILWIND — AI SC L10 | $4.70T | +136.2% | 29.9x | 30.2% | +21.5% | +81.9% | 5/5 | +21.8% | -46.6% | 32.7% | 0.5x | 2026-07-22 | WATCHING | — | Tier 3 spread +87.2%; strong fundamentals but price has meaningfully outrun earnings. | — |
| KLAC | TAILWIND — AI SC L2 | $225.23B | +122.8% | 49.3x | 48.3% | +3.0% | +11.8% | 5/5 | +11.5% | -37.0% | 42.1% | 1.4x | 2026-07-30 | WATCHING | — | Tier 3 spread +121.4%; QoQ flat — deceleration signal. | — |
| LRCX | TAILWIND — AI SC L2 | $338.92B | +230.4% | 51.9x | 71.7% | +9.9% | +40.8% | 5/5 | +23.8% | -20.7% | 34.3% | 0.5x | 2026-07-29 | WATCHING | — | Tier 4 spread +213%; FCF declining. | — |
| MP | TAILWIND — AI SC L1 | $9.80B | +159.9% | — | -2.0% | -31.7% | +71.4% | 3/5 | +118.6% | +15.4% | -39.4% | — | 2026-08-06 | WATCHING | — | Tier 2 spread +10.4%; no GAAP earnings, FCF -877.9% — pre-profitability. | — |
| MRVL | TAILWIND — AI SC L6 | $148.39B | +174.4% | 55.8x | 17.7% | +203.4% | +100.0% | 1/5 | +22.1% | -41.5% | 16.3% | 2.6x | 2026-05-27 | WATCHING | — | Tier 3 spread +57.5%; Avg QoQ +194.7% strong but YoY masks recent deceleration. | — |
| QCOM | TAILWIND — AI SC L12 | $208.35B | +32.5% | 21.4x | 28.3% | +32.6% | +173.0% | 5/5 | -3.5% | -18.1% | 25.5% | 1.1x | 2026-07-29 | WATCHING | — | Tier 2 spread +5.7%; EPS barely negative, QoQ fading — approaching Tier 1 if EPS recovers. | — |
| SNPS | TAILWIND — AI SC L2 | $95.50B | -3.3% | 76.4x | 4.3% | -9.6% | -78.8% | 5/5 | +65.5% | +859.5% | 10.8% | 4.1x | 2026-05-27 | Complete | SNPS_Thesis.md | HOLD — FAIRLY VALUED. GAAP EPS depressed by Ansys amortization ($394M/qtr); honest owner earnings P/E ~42x vs. headline 34x non-GAAP. EDA duopoly moat confirmed; monetization gap real; joint solution revenue FY2027+. Q2 (May 27) is thesis-critical: IP sequential improvement required. EV ≈ $476 vs. $495 price. | 2026-05-15 |
| TSM | TAILWIND — AI SC L3 | $2.03T | +105.1% | 1.1x | 49.5% | +12.2% | +58.4% | 5/5 | +35.1% | +27.9% | 53.2% | 0.4x | 2026-07-16 | Complete | TSM_Thesis.md | BUY — MEASURED. Tier 3 spread +82.3%; P/E 1.0x is a confirmed FMP data error (correct: ~34.8x trailing). Upgrade to CONVICTION on Oct print if N3 margin crossover confirms or pricing shift signals. | 2026-05-08 |
| VRT | TAILWIND — AI SC L9 | $125.87B | +210.1% | 82.8x | 30.4% | +29.8% | +135.7% | 5/5 | +30.1% | +147.3% | 18.5% | 1.2x | 2026-07-29 | WATCHING | — | Tier 3 spread +117.3%; large run partially justified by earnings acceleration. | — |
| BE | TAILWIND — AI SC L8 | $61.24B | +1242.2% | — | 3.6% | +1394.8% | +330.0% | 2/5 | +130.4% | +138.0% | 8.2% | 9.2x | 2026-07-30 | WATCHING | — | Prior removal flag stale — EPS YoY reversed to +350.0% (was -99.1%). vs_1Y +1076.6% and Debt/OCF 9.1x remain concerns. Reassess from current data. | — |
| AMAT | TAILWIND — AI SC L2 | $322.56B | +150.2% | 38.7x | 36.3% | +9.2% | +33.5% | 5/5 | +11.4% | -21.6% | 29.5% | 0.8x | 2026-08-13 | WATCHING | — | Tier 3 spread +80.1%; earnings accelerating, FCF +91.2%. | 2026-04-28 |
| ANET | TAILWIND — AI SC L7 | $177.97B | +46.4% | 48.5x | 34.8% | +5.9% | +25.0% | 5/5 | +35.1% | +167.2% | 42.8% | 0.0x | 2026-08-04 | WATCHING | — | Tier 3 spread +92.3%; dominant AI networking, clean balance sheet. | 2026-04-28 |
| ARM | TAILWIND — AI SC L2/L4 | $230.61B | +65.0% | 259.4x | 15.1% | +19.2% | +45.0% | 4/5 | +20.1% | +1.1% | 18.3% | 0.3x | 2026-07-29 | WATCHING | — | Tier 4 — EPS declining at P/E 264.9x; architecture royalty thesis not yet in GAAP numbers. | 2026-04-28 |
| ASML | TAILWIND — AI SC L2 | $561.92B | +97.9% | 56.9x | 64.3% | +6.4% | +22.6% | 5/5 | +13.2% | -466.3% | 34.8% | 0.3x | 2026-07-15 | WATCHING | Complete | Tier 3 spread +85.0%; EUV monopoly structural premium; FCF YoY extreme negative likely one-time. | 2026-05-12 |
| AMKR | TAILWIND — AI SC L3 | $15.84B | +236.7% | 36.6x | 10.1% | +68.4% | +288.2% | 5/5 | +27.5% | -42.6% | 7.6% | 1.3x | 2026-07-27 | WATCHING | — | Tier 2 spread +17.9% (vs_1Y +313.2% minus EPS YoY +295.3%); EPS, FCF, and Rev all genuinely strong. | — |
| AVGO | TAILWIND — AI SC L6 | $1.95T | +79.6% | 80.2x | 21.2% | +15.9% | +31.6% | 5/5 | +29.5% | +33.2% | 40.9% | 2.2x | 2026-06-03 | WATCHING | — | Tier 3 estimated; data not yet pulled — run tracker_update.py to populate. | — |
| GLW | TAILWIND — AI SC L7 | $150.25B | +267.8% | 83.1x | 10.7% | +46.7% | +138.9% | 5/5 | +20.0% | +152.6% | 15.3% | 3.1x | 2026-08-04 | WATCHING | — | Tier 3 spread +113%; re-rating from depressed base; QoQ solid. | — |
| HON | TAILWIND — AI SC L9 | $137.06B | -1.8% | 30.6x | 12.3% | +30.9% | -41.9% | 5/5 | -6.9% | -352.3% | 14.9% | 6.6x | 2026-07-23 | WATCHING | — | Tier 4 — EPS declining -42.4%, FCF -352.3%. Thesis needs catalyst before promoting. | 2026-04-28 |
| JCI | TAILWIND — AI SC L9 | $82.21B | +39.3% | 24.0x | 16.3% | +36.9% | +38.9% | 5/5 | +8.2% | +19.6% | 13.6% | 5.4x | 2026-08-04 | WATCHING | — | Tier 3 spread +42.1%; earnings and FCF genuinely growing; Debt/OCF 5.4x borderline. | 2026-04-28 |
| ORCL | TAILWIND — AI SC L13 | $536.99B | +18.1% | 33.5x | 12.2% | +17.5% | +24.5% | 5/5 | +21.7% | -16274.6% | 30.8% | 6.9x | 2026-06-10 | WATCHING | — | Tier 2 spread +2.3% — near Tier 1; FCF YoY -16274.6% is almost certainly a data error; manual audit needed. | 2026-04-28 |
| SNOW | TAILWIND — AI SC L13 | $60.94B | -3.6% | — | -71.6% | -0.1% | +9.1% | 0/5 | +30.1% | +81.5% | -30.6% | 2.2x | 2026-05-27 | WATCHING | — | Spread -19.4% but EPS still deeply negative GAAP (0/5 profitable). Rev +30.1% and FCF +81.5% are the real signals. Promote only when GAAP turns positive. | 2026-04-28 |
| COP | TAILWIND | $152.76B | +43.4% | 21.3x | 9.8% | -1.0% | -20.2% | 5/5 | -2.5% | +56.9% | 18.3% | 1.3x | 2026-08-06 | WATCHING | — | ConocoPhillips — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| EOG | TAILWIND | $76.51B | +30.9% | 14.2x | 16.1% | +33.8% | +39.6% | 5/5 | +15.7% | +83.0% | 36.9% | 0.8x | 2026-08-06 | WATCHING | — | EOG Resources — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| LIN | TAILWIND — AI SC L1 | $234.11B | +11.4% | 33.6x | 12.1% | +4.4% | +13.4% | 5/5 | +8.2% | +0.8% | 28.8% | 2.4x | 2026-08-07 | WATCHING | — | Linde — industrial/process gases for semiconductor fabs. Run tracker_update.py to populate. | 2026-04-28 |
| APD | TAILWIND — AI SC L1 | $64.81B | +7.8% | 30.8x | 6.4% | +3441.2% | +141.1% | 5/5 | +8.8% | +250.6% | 18.4% | 4.5x | 2026-07-30 | WATCHING | — | Air Products and Chemicals — industrial gases, hydrogen. Run tracker_update.py to populate. | 2026-04-28 |
| INTC | TAILWIND — AI SC L3/L4 | $541.75B | +398.7% | — | -0.8% | -160.0% | -284.2% | 2/5 | +7.2% | +41.9% | -9.4% | 4.5x | 2026-07-23 | WATCHING | INTC_Thesis.md | Thesis complete 2026-05-14. MONITOR — dollar for $1.30 at $116.14; narrative STRONG, Numbers ABSENT, Catalyst MODERATE. Intel Products healthy (32% margins, six consecutive guidance beats, supply-constrained); Intel Foundry losing $2.4B/qtr (-45% margins). 18A yields ahead of schedule; advanced packaging demand upgraded to "billions/year"; Google LTA + multiple anonymous LTAs signed. ASIC business doubled YoY. Entry signal: pullback to $75-85 OR Apple confirmed at commercial scale (>$1B foundry revenue). Catalysts: Q2 earnings 2026-07-23, H2 2026 14A commitments, H2 Analyst Day. **Invalidation:** (1) 14A PDK 1.0 delayed past Q4 2026; (2) Apple absent from H2 2026 LTA announcements; (3) 18A yields stall below 60% by Q3 2026; (4) Foundry gross margin not neutral by Q4 2027; (5) Zinsner FCF/breakeven guidance materially withdrawn; (6) Lip-Bu Tan departure. Run tracker_update.py to populate market data. | 2026-05-14 |

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
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | $263.67 | -37.3% | 15.3x | +2.8% | +11.4% | +12.0% | 2026-06-11 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | $259.31 | +25.8% | 31.0x | +16.1% | +74.8% | +16.6% | 2026-07-30 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | $185.96 | -34.9% | 23.8x | +5.1% | +18.3% | +12.1% | 2026-05-27 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | $738.00 | +25.0% | — | — | — | — | — | — |

<!-- PRIORITY_COMPLETE -->
## Daily Priority — 2026-04-28

### Add to Position

**ADBE** — P/E 14.1x | $243.20 vs. $250.00 entry (-2.7%) | EPS YoY +11.1%, FCF YoY +18.9%, Op Margin 36.6%, Debt/OCF 0.6x
Below entry on no fundamental change. Every metric improving. Strongest add signal in the portfolio.

**CRM** — P/E 23.1x | $181.32 vs. $181.70 entry (-0.2%) | EPS YoY +16.9%, FCF YoY +39.5%, Op Margin 21.5%, Debt/OCF 1.1x
Marginally below entry with accelerating FCF. Lower conviction than ADBE but clean.

---

### Pipeline

**Promoted to PIPELINE this session:** BR, NFLX, WDAY, SAP, CAG (LOSER—EPS+); MU, FCX, MSFT, IBM, NVDA, CDNS (Tier 1 TAILWIND spread ≤ 0%)

**Demoted from PIPELINE this session:** DPZ (EPS YoY turned -5.0%), META (Tier 2 spread), AXON (Tier 3 spread), UMAC (Tier 3 spread, FCF -705.6%)

**Flagged for Removal this session:** TH, CC, INTC, USAR, CARR, VST, CRWV, LEN, TEAM — see DROPPED.

**BE — Data reversal:** Prior removal flag is stale. EPS YoY now +350.0% (was -99.1%). Reassess before any decision. vs_1Y +1076.6% and Debt/OCF 9.1x remain concerns.

**NVO — Data error:** P/E 1.8x and FCF -750.8% are almost certainly FMP data errors. Flag for manual audit before thesis decision.

**L11 (Neocloud) gap:** CRWV removed. No L11 replacement identified. Surface new candidates.

---

### SC Layer Coverage

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
L10 Hyperscalers           — 1  (MSFT) — META demoted to WATCHLIST
L11 AI Cloud / Neocloud    — 0  ⚠ No actionable candidates remaining
L12 Edge AI / Robotics     — 0  ⚠ (QCOM Tier 2 in WATCHLIST)
L13 AI Software / Apps     — 1  (IBM) — RDDT demoted to WATCHLIST (Financials FILTERED)
non-AI                     — 0  (AXON, UMAC demoted to WATCHLIST)
```

---

# Ticker Tracker

---

## PIPELINE

Stocks under active analysis. Work through phases sequentially per `GEMINI.md`. Consider an initial position after Earnings; scale/exit decision after Footnotes; full position after Synthesis. Market data columns updated daily by `Scripts/tracker_update.py` (automated via GitHub Actions).

**Tier 1 criteria (required for PIPELINE):** LOSER—EPS+ tag (EPS YoY > 0 AND vs_1Y < 0) OR TAILWIND with Spread ≤ 0% (EPS YoY ≥ vs_1Y). Anything below Tier 1 belongs in WATCHLIST.

**Column Guide**
- **Tag**: `LOSER` or `TAILWIND` — see `GEMINI.md`. `LOSER — EPS+` auto-applied by script when EPS YoY > 0 and vs_1Y < 0.
- **Mkt Cap**: Market capitalization (updated by script)
- **vs_1Y**: Price change vs. 1 year ago (updated by script)
- **P/E**: GAAP TTM P/E — diluted EPS from income statement (updated by script)
- **Avg EPS QoQ (4Q)**: Average of last 4 quarters of EPS QoQ change (updated by script)
- **EPS YoY**: Most recent quarter diluted EPS vs. same quarter prior year (updated by script)
- **Yrs Profitable (5yr)**: Profitable years out of last 5 (updated by script)
- **Rev YoY**: Most recent quarter revenue vs. same quarter prior year (updated by script)
- **FCF YoY**: Free cash flow year-over-year change (updated by script)
- **Op Margin %**: Operating margin TTM (updated by script)
- **Debt/OCF**: Total debt / TTM operating cash flow (updated by script)
- **Next Earnings**: Next scheduled earnings date (updated by script)
- **Phase**: `Price & Earnings` → `Financials` → `Footnotes` → `Earnings Calls` → `Research` → `Synthesis`
- **Last Run**: Date of last completed workflow step
- **Status**: `PASS` | `BUY` | `HOLD` | `FAIL`
- **Added**: Date added to PIPELINE

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Phase | Last Run | Status | Thesis | Added |
|--------|-----|---------|-------|-----|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|-------|----------|--------|--------|-------|
| BR | LOSER — EPS+ | $18.54B | -31.9% | 17.4x | +35.3% | +100.0% | 5/5 | +7.8% | +39.8% | 17.3% | 2.5x | 2026-08-04 | Synthesis | 2026-04-30 | MONITOR | Thesis_BR.md | 2026-04-28 |
| NFLX | LOSER — EPS+ | $388.82B | -16.9% | 29.2x | +26.1% | +83.8% | 5/5 | +16.2% | +91.4% | 29.7% | 1.3x | 2026-07-16 | Price & Earnings | — | PASS | — | 2026-04-28 |
| WDAY | LOSER — EPS+ | $32.12B | -49.5% | 46.4x | +42.7% | +57.1% | 4/5 | +14.5% | +18.7% | 8.9% | 1.3x | 2026-05-21 | Price & Earnings | — | PASS | — | 2026-04-28 |
| SAP | LOSER — EPS+ | $202.20B | -38.8% | 27.1x | +2.6% | +8.5% | 5/5 | +6.0% | -9.4% | 26.9% | 0.0x | 2026-07-23 | Price & Earnings | — | PASS | — | 2026-04-28 |
| CAG | LOSER — EPS+ | $6.83B | -37.2% | — | -83.9% | +40.0% | 4/5 | -1.9% | -6.8% | 12.3% | 5.3x | 2026-07-09 | Price & Earnings | — | PASS | — | 2026-04-28 |
| MU | TAILWIND — AI SC L5 | $568.70B | +543.5% | 23.5x | +78.5% | +762.7% | 4/5 | +196.3% | -22.8% | 48.5% | 0.4x | 2026-06-24 | Price & Earnings | — | PASS | — | 2026-04-28 |
| FCX | TAILWIND — AI SC L1 | $83.65B | +58.1% | 31.0x | +46.6% | +154.2% | 5/5 | +12.2% | +557.9% | 27.8% | 1.7x | 2026-07-22 | Price & Earnings | — | PASS | — | 2026-04-28 |
| MSFT | TAILWIND — AI SC L10 | $3.19T | +10.6% | 26.8x | +13.3% | +59.9% | 5/5 | +16.7% | -9.3% | 46.7% | 0.8x | 2026-04-29 | Synthesis | 2026-04-30 | MONITOR | MSFT_Thesis.md | 2026-04-28 |
| IBM | TAILWIND — AI SC L13 | $219.06B | +1.1% | 20.2x | +56.9% | +14.0% | 5/5 | +9.5% | +20.2% | 16.4% | 5.0x | 2026-07-22 | Price & Earnings | — | PASS | — | 2026-04-28 |
| NVDA | TAILWIND — AI SC L4/L12 | $5.18T | +96.1% | 43.2x | +20.6% | +96.7% | 5/5 | +73.2% | +124.4% | 60.4% | 0.1x | 2026-05-20 | Price & Earnings | — | PASS | — | 2026-04-28 |
| CDNS | TAILWIND — AI SC L2 | $89.82B | +13.8% | 75.5x | +14.7% | +21.8% | 5/5 | +18.7% | +26.8% | 31.1% | 1.4x | 2026-07-27 | Price & Earnings | — | PASS | — | 2026-04-28 |

---

## WATCHLIST

Stocks under continuous monitoring. Move to PIPELINE when Tier 1 criteria are met. Move to DROPPED if thesis fails.

**Column Guide** (market data columns same as PIPELINE; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (Tier 1 criteria now met — move to PIPELINE)
- **Notes**: Thesis context, entry signal criteria, and invalidation conditions

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Status | Thesis | Notes | Added |
|--------|-----|---------|-------|-----|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|--------|--------|-------|-------|
| AIG | LOSER | $39.79B | -7.5% | 13.5x | +9.7% | -10.5% | 4/5 | -8.6% | +408.8% | 14.5% | 2.8x | 2026-04-30 | WATCHING | — | FCF +408.8% diverging strongly from EPS — worth monitoring for earnings recovery confirmation. | — |
| CPB | LOSER | $6.12B | -39.3% | 11.1x | +17.2% | -15.5% | 5/5 | -4.5% | +56.4% | 12.1% | 6.2x | 2026-06-01 | WATCHING | — | FCF +56.4% and QoQ improving despite YoY decline — direction of travel improving. | — |
| INTU | LOSER — EPS+ | $111.42B | -34.7% | 25.8x | +121.8% | +48.2% | 5/5 | +17.4% | +46.8% | 27.1% | 1.1x | 2026-05-21 | WATCHING | INTU_Thesis.md | Synthesis complete 2026-04-23. MONITOR — entry signal: Q3 FY2026 (May 21) confirms TurboTax Live 35%+, revenue at high end of guidance, Credit Karma holds. Invalidation: TurboTax Live <20% growth, revenue <11%, IRS Direct File expansion. | — |
| IT | LOSER | $10.58B | -63.9% | 15.5x | +124.3% | -34.6% | 5/5 | +2.2% | -13.1% | 15.8% | 2.6x | 2026-05-05 | WATCHING | IT_Thesis.md | Synthesis complete 2026-04-24. MONITOR — BUY on entry conditions: (1) May 5 earnings confirms federal headwind peaking; (2) Post-May 18 litigation update favorable. Remove if either gate fails. | — |
| LULU | LOSER | $16.70B | -47.0% | 10.7x | +9.2% | -19.2% | 5/5 | +0.8% | -17.7% | 19.8% | 1.1x | 2026-06-04 | WATCHING | — | — | — |
| NOW | LOSER — EPS+ | $93.32B | -51.7% | 53.5x | +2.6% | +2.3% | 5/5 | +22.1% | +3.9% | 13.4% | 0.4x | 2026-07-22 | WATCHING | NOW_Thesis.md | Filtered 2026-04-21 — GAAP P/E ~61x, SBC $1.96B/yr, $9B pending acquisitions inflating debt. Revisit after Armis closes (H2 2026). | — |
| NVO | LOSER | $182.96B | -32.0% | 1.8x | +1.1% | -4.4% | 5/5 | -7.6% | -750.8% | 41.3% | 1.1x | 2026-05-06 | WATCHING | — | P/E 1.8x and FCF -750.8% are almost certainly FMP data errors. Flag for manual audit before thesis decision. | — |
| DPZ | LOSER | $11.45B | -29.4% | 19.5x | +0.7% | -5.0% | 5/5 | +3.5% | -10.6% | 19.6% | 6.6x | 2026-07-20 | WATCHING | DPZ_Thesis.md | Demoted from PIPELINE 2026-04-28 — EPS YoY turned -5.0% (was +9.6%); lost LOSER—EPS+ tag. Debt/OCF 6.6x elevated. Promote back if next earnings recovers EPS. | 2026-04-15 |
| AXON | TAILWIND | $32.67B | -32.6% | 252.0x | +10.5% | -97.7% | 4/5 | +38.5% | -31.0% | 0.0% | 9.0x | 2026-05-06 | WATCHING | AXON_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; Financials phase analysis was in progress. Debt/OCF 9.0x and Op Margin 0.0% are concerns to resolve. | 2026-04-14 |
| META | TAILWIND — AI SC L10 | $1.70T | +22.5% | 28.0x | +160.4% | +9.9% | 5/5 | +23.8% | +9.3% | 41.4% | 0.7x | 2026-04-29 | WATCHING | META_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 2 spread (+12.6%); exceptional quality. Promote when spread narrows to ≤ 0%. | 2026-04-14 |
| RDDT | TAILWIND — AI SC L13 | $28.26B | +22.1% | 52.6x | +77.9% | +238.5% | 1/5 | +69.7% | +195.7% | 20.1% | 0.0x | 2026-04-30 | WATCHING | RDDT_Thesis.md | Filtered at Financials 2026-04-29 — 83× owner earnings (FCF−SBC) on 1/5 yrs profitability; 238.5% EPS growth is largely IPO SBC normalization artifact, not durable compounding. Re-entry: 2–3 consecutive profitable quarters surviving Q1 seasonal weakness + SBC/Rev declining toward 10% + data licensing revenue at material scale. | 2026-04-14 |
| UMAC | TAILWIND | $563.45M | +137.5% | — | -149.5% | +88.6% | 1/5 | +144.4% | -705.6% | -224.6% | — | 2026-05-14 | WATCHING | UMAC_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; FCF -705.6%, Op Margin -224.6%. Price has outrun pre-profitability thesis. | 2026-04-14 |
| BKH | TAILWIND — AI SC L8 | $5.72B | +29.0% | 18.9x | +64.5% | +2.2% | 5/5 | +6.4% | -67.8% | 23.3% | 7.0x | 2026-05-06 | WATCHING | BKH_Thesis.md | Tier 2 spread +26.8%; FCF -67.8% and Debt/OCF 7.0x are concerns. | — |
| CCJ | TAILWIND — AI SC L1 | $50.65B | +157.2% | 86.2x | +37578.5% | +45.2% | 4/5 | +1.4% | +17.4% | 17.5% | 0.7x | 2026-05-05 | WATCHING | — | Tier 3 spread +111.9%; Avg QoQ is near-zero base noise. | — |
| CSCO | TAILWIND — AI SC L7 | $343.17B | +56.4% | 31.0x | +7.5% | +32.8% | 5/5 | +9.7% | +5.6% | 22.7% | 2.3x | 2026-05-13 | WATCHING | — | Tier 2 spread +23.6% — approaching Tier 1; clean fundamentals. | 2026-04-28 |
| GEV | TAILWIND — AI SC L8 | $292.62B | +194.9% | 31.4x | +208.7% | +1818.5% | 2/5 | +16.1% | +391.4% | 3.9% | 0.3x | 2026-07-22 | WATCHING | — | Tier 1 spread by math (-1623%) but base-effect distortion (prior EPS near-zero). QoQ +208.7% and FCF +391.4% are the real signals. Op Margin 3.9% is thin. | — |
| GOOGL | TAILWIND — AI SC L10 | $4.23T | +118.5% | 32.1x | +8.9% | +31.3% | 5/5 | +18.1% | -1.2% | 32.0% | 0.4x | 2026-04-29 | WATCHING | — | Tier 3 spread +87.2%; strong fundamentals but price has meaningfully outrun earnings. | — |
| KLAC | TAILWIND — AI SC L2 | $237.68B | +162.7% | 52.3x | +10.0% | +41.3% | 5/5 | +7.2% | +66.7% | 42.4% | 1.3x | 2026-07-23 | WATCHING | — | Tier 3 spread +121.4%; QoQ flat — deceleration signal. | — |
| LRCX | TAILWIND — AI SC L2 | $314.19B | +253.6% | 47.2x | +9.8% | +40.4% | 5/5 | +23.8% | -20.7% | 34.3% | 0.5x | 2026-07-29 | WATCHING | — | Tier 4 spread +213%; FCF declining. | — |
| MP | TAILWIND — AI SC L1 | $10.96B | +148.3% | — | +15.0% | +137.9% | 3/5 | +70.0% | -877.9% | -53.0% | — | 2026-05-07 | WATCHING | — | Tier 2 spread +10.4%; no GAAP earnings, FCF -877.9% — pre-profitability. | — |
| MRVL | TAILWIND — AI SC L6 | $134.01B | +161.8% | 49.3x | +194.7% | +104.3% | 1/5 | +22.1% | -41.5% | 16.3% | 2.6x | 2026-06-04 | WATCHING | — | Tier 3 spread +57.5%; Avg QoQ +194.7% strong but YoY masks recent deceleration. | — |
| QCOM | TAILWIND — AI SC L12 | $160.21B | +4.0% | 30.2x | -8.2% | -1.7% | 5/5 | +5.0% | +2.5% | 27.1% | 1.0x | 2026-04-29 | WATCHING | — | Tier 2 spread +5.7%; EPS barely negative, QoQ fading — approaching Tier 1 if EPS recovers. | — |
| SNPS | TAILWIND — AI SC L2 | $92.69B | +9.0% | 73.5x | -9.6% | -79.1% | 5/5 | +65.5% | +859.5% | 10.8% | 4.1x | 2026-05-27 | WATCHING | — | EPS collapsing (-79.1%) but FCF +859.5% — major divergence; determine if GAAP EPS is distorted by one-time items before removal. | — |
| TSM | TAILWIND — AI SC L3 | $2.03T | +142.3% | 1.0x | +12.5% | +60.0% | 5/5 | +36.5% | +27.9% | 53.3% | 0.4x | 2026-07-16 | WATCHING | TSM_Thesis.md | Tier 3 spread +82.3%; P/E 1.0x is a confirmed FMP data error — flag for correction. | — |
| VRT | TAILWIND — AI SC L9 | $117.16B | +254.5% | 74.8x | +29.9% | +137.2% | 5/5 | +30.1% | +147.3% | 18.5% | 1.2x | 2026-07-29 | WATCHING | — | Tier 3 spread +117.3%; large run partially justified by earnings acceleration. | — |
| BE | TAILWIND — AI SC L8 | $54.43B | +1076.6% | — | +1516.8% | +350.0% | 2/5 | +130.4% | +138.0% | 8.2% | 9.1x | — | WATCHING | — | Prior removal flag stale — EPS YoY reversed to +350.0% (was -99.1%). vs_1Y +1076.6% and Debt/OCF 9.1x remain concerns. Reassess from current data. | — |
| AMAT | TAILWIND — AI SC L2 | $302.25B | +154.8% | 38.9x | +19.8% | +74.7% | 5/5 | -2.1% | +91.2% | 29.1% | 0.8x | 2026-05-14 | WATCHING | — | Tier 3 spread +80.1%; earnings accelerating, FCF +91.2%. | 2026-04-28 |
| ANET | TAILWIND — AI SC L7 | $208.13B | +111.1% | 59.0x | +4.6% | +18.8% | 5/5 | +28.9% | +20.3% | 42.8% | 0.0x | 2026-05-05 | WATCHING | — | Tier 3 spread +92.3%; dominant AI networking, clean balance sheet. | 2026-04-28 |
| ARM | TAILWIND — AI SC L2/L4 | $210.97B | +77.2% | 264.9x | +5.5% | -12.5% | 3/5 | +26.3% | -48.3% | 18.6% | 0.6x | 2026-05-06 | WATCHING | — | Tier 4 — EPS declining at P/E 264.9x; architecture royalty thesis not yet in GAAP numbers. | 2026-04-28 |
| ASML | TAILWIND — AI SC L2 | $533.63B | +107.4% | 53.5x | +6.3% | +22.4% | 5/5 | +13.2% | -466.3% | 34.8% | 0.3x | 2026-07-15 | WATCHING | — | Tier 3 spread +85.0%; EUV monopoly structural premium; FCF YoY extreme negative likely one-time. | 2026-04-28 |
| AMKR | TAILWIND — AI SC L3 | $17.68B | +313.2% | 40.5x | +68.1% | +295.3% | 5/5 | +27.5% | +360.3% | 7.6% | 1.2x | 2026-07-27 | WATCHING | — | Tier 2 spread +17.9% (vs_1Y +313.2% minus EPS YoY +295.3%); EPS, FCF, and Rev all genuinely strong. | — |
| AVGO | TAILWIND — AI SC L6 | — | — | — | — | — | — | — | — | — | — | — | WATCHING | — | Tier 3 estimated; data not yet pulled — run tracker_update.py to populate. | — |
| GLW | TAILWIND — AI SC L7 | $131.47B | +252.2% | 72.5x | +47.7% | +138.9% | 5/5 | +20.0% | +152.6% | 15.3% | 3.1x | 2026-08-04 | WATCHING | — | Tier 3 spread +113%; re-rating from depressed base; QoQ solid. | — |
| HON | TAILWIND — AI SC L9 | $134.92B | +8.3% | 30.1x | +30.7% | -42.4% | 5/5 | -6.9% | -352.3% | 14.9% | 6.6x | 2026-07-23 | WATCHING | — | Tier 4 — EPS declining -42.4%, FCF -352.3%. Thesis needs catalyst before promoting. | 2026-04-28 |
| JCI | TAILWIND — AI SC L9 | $86.66B | +77.0% | 26.6x | +36.2% | +34.9% | 5/5 | +6.8% | +254.2% | 13.2% | 5.4x | 2026-05-06 | WATCHING | — | Tier 3 spread +42.1%; earnings and FCF genuinely growing; Debt/OCF 5.4x borderline. | 2026-04-28 |
| ORCL | TAILWIND — AI SC L13 | $477.19B | +19.6% | 29.2x | +16.9% | +21.9% | 5/5 | +21.7% | -16274.6% | 30.8% | 6.9x | 2026-06-10 | WATCHING | — | Tier 2 spread +2.3% — near Tier 1; FCF YoY -16274.6% is almost certainly a data error; manual audit needed. | 2026-04-28 |
| SNOW | TAILWIND — AI SC L13 | $49.28B | -10.3% | — | -0.1% | +9.1% | 0/5 | +30.1% | +81.5% | -30.6% | 2.2x | 2026-05-27 | WATCHING | — | Spread -19.4% but EPS still deeply negative GAAP (0/5 profitable). Rev +30.1% and FCF +81.5% are the real signals. Promote only when GAAP turns positive. | 2026-04-28 |
| COP | TAILWIND | — | — | — | — | — | — | — | — | — | — | — | WATCHING | — | ConocoPhillips — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| EOG | TAILWIND | — | — | — | — | — | — | — | — | — | — | — | WATCHING | — | EOG Resources — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| LIN | TAILWIND — AI SC L1 | — | — | — | — | — | — | — | — | — | — | — | WATCHING | — | Linde — industrial/process gases for semiconductor fabs. Run tracker_update.py to populate. | 2026-04-28 |
| APD | TAILWIND — AI SC L1 | — | — | — | — | — | — | — | — | — | — | — | WATCHING | — | Air Products and Chemicals — industrial gases, hydrogen. Run tracker_update.py to populate. | 2026-04-28 |

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
| TEAM | LOSER | 2026-04-28 | Yrs Profitable 0/5, EPS YoY -6.7%, Avg QoQ -28.4%, Op Margin -3.2% — structural unprofitability, not dislocation. |
| PFE | TAILWIND | 2026-04-28 | Post-COVID earnings collapse — EPS YoY -500.6%, Rev -1.2%, FCF -22.4%. No AI thesis. |
| T | TAILWIND | 2026-04-28 | EPS YoY -11.5%, FCF -43.8%, revenue barely growing. No catalyst. |

---

## Trade Tracker

Market data columns updated daily by `Scripts/tracker_update.py`. Use Price vs. Entry Price to identify add-to-position opportunities.

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Price | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY | Rev YoY | Next Earnings | Thesis |
|--------|------------|-------------|--------|------------|-------|-------|-----|------------------|---------|---------|---------------|--------|
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | $243.20 | -34.0% | 14.1x | +2.8% | +11.1% | +12.0% | 2026-06-11 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | $259.70 | +38.4% | 35.6x | +1.7% | +4.2% | +13.6% | 2026-04-29 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | $181.32 | -31.2% | 23.1x | +4.7% | +16.9% | +12.1% | 2026-05-27 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | $714.96 | +30.8% | — | — | — | — | — | — |

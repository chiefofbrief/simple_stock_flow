<!-- PRIORITY_COMPLETE -->
## Daily Priority — 2026-05-07

### Analyze Now
- **NFLX** | LOSER — EPS+ | P/E: 28.5x | vs_1Y: -22.9% | EPS YoY: +86.4% | A brand-name LOSER with a significant price dislocation despite stellar earnings and FCF growth (+91.4%), signaling a potential market overreaction to guidance.
- **FCX** | TAILWIND — AI SC L1 | P/E: 32.1x | vs_1Y: +63.6% | EPS YoY: +154.2% | A powerful TAILWIND where massive earnings growth is confirmed by explosive FCF YoY (+557.9%) and has not been fully priced in.
- **IBM** | TAILWIND — AI SC L13 | P/E: 20.5x | vs_1Y: -6.0% | EPS YoY: +14.3% | A rare TAILWIND-as-dislocation where the price is down while earnings and FCF are growing, creating a strong contrarian signal.

### Add to Position
None.

### Remove
- **CAG** | Avg EPS QoQ (4Q): -84.4% | Remove. Negative ROIC (-1.0%), high debt (5.3x), and collapsing QoQ earnings momentum suggest structural weakness, not a temporary dislocation.
- **LRCX** | Spread: +244.5% | Remove. Price has significantly outrun earnings (Tier 4 spread) and FCF YoY is declining (-20.7%); thesis is exhausted.
- **ARM** | EPS YoY: -12.5% | Remove. Tier 4 candidate with negative EPS YoY and an extreme P/E (284.4x); price has detached from fundamentals.
- **HON** | EPS YoY: -41.9% | Remove. Thesis is broken with broad-based deterioration across EPS YoY (-41.9%) and FCF YoY (-352.3%).
- **BE** | vs_1Y: +1400.2% | Remove. Extreme reflexivity and high debt (9.2x Debt/OCF) invert the risk/reward, breaking the TAILWIND thesis.
- **Promote to PIPELINE: AIG** | Tag: LOSER — EPS+ (vs_1Y -4.5%, EPS YoY +21.6%). Meets Tier 1 criteria.

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
| BR | LOSER — EPS+ | $17.68B | -34.1% | 16.4x | 20.1% | +17.2% | +15.1% | 5/5 | +7.8% | -17.6% | 17.1% | 2.5x | 2026-08-04 | Complete | 2026-04-30 | MONITOR | Thesis_BR.md | 2026-04-28 |
| NFLX | LOSER — EPS+ | $371.60B | -22.9% | 28.5x | 38.9% | +26.4% | +86.4% | 5/5 | +16.2% | +91.4% | 29.7% | 1.3x | 2026-07-16 | — | — | — | — | 2026-04-28 |
| WDAY | LOSER — EPS+ | $34.70B | -49.3% | 50.7x | 7.6% | +44.5% | +57.1% | 4/5 | +14.5% | +18.7% | 8.9% | 1.3x | 2026-05-21 | — | — | — | — | 2026-04-28 |
| SAP | LOSER — EPS+ | $203.58B | -39.3% | 27.4x | 23.1% | +2.8% | +9.3% | 5/5 | +6.0% | -9.4% | 26.9% | 0.0x | 2026-07-23 | Complete | 2026-05-06 | BUY — MEASURED | SAP_Thesis.md | 2026-04-28 |
| CAG | LOSER — EPS+ | $6.87B | -32.8% | — | -1.0% | -84.4% | +40.0% | 4/5 | -1.9% | -6.8% | 12.3% | 5.3x | 2026-07-09 | — | — | — | — | 2026-04-28 |
| MU | TAILWIND — AI SC L5 | $729.22B | +661.2% | 30.5x | 34.5% | +78.2% | +756.7% | 4/5 | +196.3% | -22.8% | 48.5% | 0.4x | 2026-06-24 | — | — | — | — | 2026-04-28 |
| FCX | TAILWIND — AI SC L1 | $87.11B | +63.6% | 32.1x | 7.9% | +46.7% | +154.2% | 5/5 | +12.2% | +557.9% | 27.8% | 1.7x | 2026-07-22 | — | — | — | — | 2026-04-28 |
| MSFT | TAILWIND — AI SC L10 | $3.13T | -3.2% | 25.0x | 29.0% | +7.2% | +23.4% | 5/5 | +18.3% | -22.1% | 46.8% | 0.3x | 2026-07-29 | Complete | 2026-04-30 | MONITOR | MSFT_Thesis.md | 2026-04-28 |
| IBM | TAILWIND — AI SC L13 | $217.40B | -6.0% | 20.5x | 13.7% | +56.8% | +14.3% | 5/5 | +9.5% | +20.2% | 16.4% | 5.0x | 2026-07-22 | — | — | — | — | 2026-04-28 |
| NVDA | TAILWIND — AI SC L4/L12 | $5.14T | +80.2% | 43.2x | 76.1% | +20.8% | +97.8% | 5/5 | +73.2% | +124.4% | 60.4% | 0.1x | 2026-05-20 | — | — | — | — | 2026-04-28 |
| CDNS | TAILWIND — AI SC L2 | $98.54B | +15.9% | 83.2x | 15.3% | +14.7% | +23.0% | 5/5 | +18.7% | -33.8% | 31.1% | 1.9x | 2026-07-27 | — | — | — | — | 2026-04-28 |

---

## WATCHLIST

Stocks under continuous monitoring. Move to PIPELINE when Tier 1 criteria are met. Move to DROPPED if thesis fails.

**Column Guide** (market data columns same as PIPELINE; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (Tier 1 criteria now met — move to PIPELINE)
- **Notes**: Thesis context, entry signal criteria, and invalidation conditions

| Ticker | Tag | Mkt Cap | vs_1Y | P/E | ROIC | Avg EPS QoQ (4Q) | EPS YoY | Yrs Profitable (5yr) | Rev YoY | FCF YoY | Op Margin % | Debt/OCF | Next Earnings | Status | Thesis | Notes | Added |
|--------|-----|---------|-------|-----|---|------------------|---------|----------------------|---------|---------|-------------|----------|---------------|--------|--------|-------|-------|
| ZM | LOSER | $31.94B | +35.0% | 17.5x | 22.1% | +24.0% | +91.4% | 5/5 | +5.3% | -18.7% | 23.1% | 0.0x | 2026-05-21 | WATCHING | ZM_Thesis.md | Synthesis complete 2026-05-06. MONITOR — SOTP: $7.8B cash + Anthropic stake (~0.6% est.; $3.6B at $600B Anthropic → core at 16.9x owner earnings). KEY WATCH: Q1 FY27 **2026-05-21** — beat+raise and Contact Center ARR disclosure is primary near-term catalyst test. Upgrade to BUY—MEASURED on: (1) price pullback to $85-90, OR (2) Anthropic IPO confirmed >$500B, OR (3) Contact Center $500M+ ARR at 50%+ growth. Invalidation: revenue <2% for 2+ qtrs, NRR below 95%, Anthropic IPO delayed past 2027. Counter-signal: insider selling (CEO -65.5%, COO -86.7%, CFO -24.8% in same 90-day window). | 2026-05-06 |
| AIG | LOSER — EPS+ | $40.52B | -4.5% | 13.5x | 7.3% | +16.8% | +21.6% | 4/5 | -1.8% | +376.8% | 14.7% | 2.6x | 2026-08-05 | WATCHING | — | FCF +408.8% diverging strongly from EPS — worth monitoring for earnings recovery confirmation. | — |
| CPB | LOSER | $6.34B | -36.8% | 11.5x | 7.7% | +16.8% | -17.2% | 5/5 | -4.5% | +56.4% | 12.1% | 6.2x | 2026-06-01 | WATCHING | — | FCF +56.4% and QoQ improving despite YoY decline — direction of travel improving. | — |
| INTU | LOSER — EPS+ | $113.20B | -37.5% | 26.4x | 19.6% | +121.6% | +47.9% | 5/5 | +17.4% | +46.8% | 27.1% | 1.1x | 2026-05-20 | WATCHING | INTU_Thesis.md | Synthesis complete 2026-04-23. MONITOR — entry signal: Q3 FY2026 (May 21) confirms TurboTax Live 35%+, revenue at high end of guidance, Credit Karma holds. Invalidation: TurboTax Live <20% growth, revenue <11%, IRS Direct File expansion. | — |
| IT | LOSER — EPS+ | $10.56B | -63.9% | 15.6x | 47.8% | +134.9% | +17.3% | 5/5 | -1.5% | +28.7% | 16.4% | 2.4x | 2026-08-04 | WATCHING | IT_Thesis.md | Synthesis complete 2026-04-24. MONITOR — BUY on entry conditions: (1) May 5 earnings confirms federal headwind peaking; (2) Post-May 18 litigation update favorable. Remove if either gate fails. | — |
| LULU | LOSER | $15.67B | -52.7% | 10.1x | 31.9% | +9.3% | -19.1% | 5/5 | +0.8% | -17.7% | 19.8% | 1.1x | 2026-06-04 | WATCHING | — | — | — |
| NOW | LOSER — EPS+ | $96.52B | -52.0% | 55.7x | 15.4% | +2.9% | +2.3% | 5/5 | +22.1% | +3.9% | 13.4% | 0.4x | 2026-07-22 | WATCHING | NOW_Thesis.md | Filtered 2026-04-21 — GAAP P/E ~61x, SBC $1.96B/yr, $9B pending acquisitions inflating debt. Revisit after Armis closes (H2 2026). | — |
| NVO | LOSER — EPS+ | $203.53B | -27.0% | 1.7x | 39.2% | +20.4% | +67.1% | 5/5 | +24.0% | +20.4% | 45.3% | 1.2x | 2026-08-05 | WATCHING | — | P/E 1.8x and FCF -750.8% are almost certainly FMP data errors. Flag for manual audit before thesis decision. | — |
| DPZ | LOSER | $11.06B | -29.1% | 19.1x | 74.8% | +0.9% | -4.6% | 5/5 | +3.5% | -10.6% | 19.6% | 6.6x | 2026-07-20 | WATCHING | DPZ_Thesis.md | Demoted from PIPELINE 2026-04-28 — EPS YoY turned -5.0% (was +9.6%); lost LOSER—EPS+ tag. Debt/OCF 6.6x elevated. Promote back if next earnings recovers EPS. | 2026-04-15 |
| AXON | TAILWIND | $34.40B | -37.8% | 171.3x | 5.5% | +1693.8% | +89.8% | 5/5 | +33.7% | -5962.9% | 1.3% | 11.9x | 2026-08-03 | WATCHING | AXON_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; Financials phase analysis was in progress. Debt/OCF 9.0x and Op Margin 0.0% are concerns to resolve. | 2026-04-14 |
| META | TAILWIND — AI SC L10 | $1.57T | +3.5% | 22.4x | 23.4% | +172.1% | +62.4% | 5/5 | +33.1% | +19.3% | 41.2% | 0.7x | 2026-07-29 | WATCHING | META_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 2 spread (+12.6%); exceptional quality. Promote when spread narrows to ≤ 0%. | 2026-04-14 |
| RDDT | TAILWIND — AI SC L13 | $31.56B | +52.0% | 46.4x | 38.7% | +86.5% | +621.4% | 2/5 | +69.1% | +145.8% | 25.1% | 0.0x | 2026-07-30 | WATCHING | RDDT_Thesis.md | Filtered at Financials 2026-04-29 — 83× owner earnings (FCF−SBC) on 1/5 yrs profitability; 238.5% EPS growth is largely IPO SBC normalization artifact, not durable compounding. Re-entry: 2–3 consecutive profitable quarters surviving Q1 seasonal weakness + SBC/Rev declining toward 10% + data licensing revenue at material scale. | 2026-04-14 |
| UMAC | TAILWIND | $524.95M | +149.1% | — | -25.8% | -152.7% | +88.6% | 1/5 | +144.4% | -705.6% | -224.6% | — | 2026-05-14 | WATCHING | UMAC_Thesis.md | Demoted from PIPELINE 2026-04-28 — Tier 3 spread; FCF -705.6%, Op Margin -224.6%. Price has outrun pre-profitability thesis. | 2026-04-14 |
| BKH | TAILWIND — AI SC L8 | $5.72B | +33.3% | 19.6x | — | +60.8% | -7.5% | 5/5 | -3.0% | +135.2% | 23.4% | 0.0x | 2026-07-29 | WATCHING | BKH_Thesis.md | Tier 2 spread +26.8%; FCF -67.8% and Debt/OCF 7.0x are concerns. | — |
| CCJ | TAILWIND — AI SC L1 | $51.69B | +141.5% | 79.2x | 13.8% | +37582.8% | +93.8% | 4/5 | +7.4% | +17.4% | 16.3% | 0.5x | 2026-07-31 | WATCHING | — | Tier 3 spread +111.9%; Avg QoQ is near-zero base noise. | — |
| CSCO | TAILWIND — AI SC L7 | $364.02B | +57.9% | 33.3x | 17.6% | +6.8% | +29.5% | 5/5 | +9.7% | +5.6% | 22.7% | 2.3x | 2026-05-13 | WATCHING | — | Tier 2 spread +23.6% — approaching Tier 1; clean fundamentals. | 2026-04-28 |
| GEV | TAILWIND — AI SC L8 | $280.98B | +166.0% | 30.6x | 121.0% | +208.4% | +1816.5% | 2/5 | +16.1% | +391.4% | 3.9% | 0.3x | 2026-07-29 | WATCHING | — | Tier 1 spread by math (-1623%) but base-effect distortion (prior EPS near-zero). QoQ +208.7% and FCF +391.4% are the real signals. Op Margin 3.9% is thin. | — |
| GOOGL | TAILWIND — AI SC L10 | $4.81T | +158.8% | 30.4x | 30.2% | +21.5% | +81.9% | 5/5 | +21.8% | -46.6% | 32.7% | 0.5x | 2026-07-22 | WATCHING | — | Tier 3 spread +87.2%; strong fundamentals but price has meaningfully outrun earnings. | — |
| KLAC | TAILWIND — AI SC L2 | $230.33B | +152.6% | 49.9x | 48.3% | +3.0% | +11.8% | 5/5 | +11.5% | -37.0% | 42.1% | 1.4x | 2026-07-30 | WATCHING | — | Tier 3 spread +121.4%; QoQ flat — deceleration signal. | — |
| LRCX | TAILWIND — AI SC L2 | $358.31B | +285.3% | 54.1x | 71.7% | +9.9% | +40.8% | 5/5 | +23.8% | -20.7% | 34.3% | 0.5x | 2026-07-29 | WATCHING | — | Tier 4 spread +213%; FCF declining. | — |
| MP | TAILWIND — AI SC L1 | $12.28B | +189.9% | — | -4.8% | -31.7% | +71.4% | 3/5 | +49.1% | +15.4% | -36.4% | — | 2026-08-06 | WATCHING | — | Tier 2 spread +10.4%; no GAAP earnings, FCF -877.9% — pre-profitability. | — |
| MRVL | TAILWIND — AI SC L6 | $139.92B | +178.4% | 52.1x | 17.7% | +203.4% | +100.0% | 1/5 | +22.1% | -41.5% | 16.3% | 2.6x | 2026-05-27 | WATCHING | — | Tier 3 spread +57.5%; Avg QoQ +194.7% strong but YoY masks recent deceleration. | — |
| QCOM | TAILWIND — AI SC L12 | $213.49B | +42.9% | 21.7x | 28.3% | +32.6% | +173.0% | 5/5 | -3.5% | -18.1% | 25.5% | 1.1x | 2026-07-29 | WATCHING | — | Tier 2 spread +5.7%; EPS barely negative, QoQ fading — approaching Tier 1 if EPS recovers. | — |
| SNPS | TAILWIND — AI SC L2 | $96.78B | +4.3% | 77.4x | 4.3% | -9.6% | -78.8% | 5/5 | +65.5% | +859.5% | 10.8% | 4.1x | 2026-05-27 | WATCHING | — | EPS collapsing (-79.1%) but FCF +859.5% — major divergence; determine if GAAP EPS is distorted by one-time items before removal. | — |
| TSM | TAILWIND — AI SC L3 | $2.15T | +138.6% | 1.1x | 49.7% | +12.5% | +60.0% | 5/5 | +36.5% | +27.9% | 53.3% | 0.4x | 2026-07-16 | WATCHING | TSM_Thesis.md | Tier 3 spread +82.3%; P/E 1.0x is a confirmed FMP data error — flag for correction. | — |
| VRT | TAILWIND — AI SC L9 | $130.60B | +255.6% | 85.4x | 30.4% | +29.8% | +135.7% | 5/5 | +30.1% | +147.3% | 18.5% | 1.2x | 2026-07-29 | WATCHING | — | Tier 3 spread +117.3%; large run partially justified by earnings acceleration. | — |
| BE | TAILWIND — AI SC L8 | $62.18B | +1400.2% | — | 3.6% | +1394.8% | +330.0% | 2/5 | +130.4% | +138.0% | 8.2% | 9.2x | 2026-07-30 | WATCHING | — | Prior removal flag stale — EPS YoY reversed to +350.0% (was -99.1%). vs_1Y +1076.6% and Debt/OCF 9.1x remain concerns. Reassess from current data. | — |
| AMAT | TAILWIND — AI SC L2 | $325.89B | +165.6% | 42.1x | 37.2% | +20.0% | +75.2% | 5/5 | -2.1% | +91.2% | 29.1% | 0.8x | 2026-05-14 | WATCHING | — | Tier 3 spread +80.1%; earnings accelerating, FCF +91.2%. | 2026-04-28 |
| ANET | TAILWIND — AI SC L7 | $178.49B | +62.4% | 48.5x | 34.8% | +5.9% | +25.0% | 5/5 | +35.1% | +167.2% | 42.8% | 0.0x | 2026-08-04 | WATCHING | — | Tier 3 spread +92.3%; dominant AI networking, clean balance sheet. | 2026-04-28 |
| ARM | TAILWIND — AI SC L2/L4 | $226.96B | +83.1% | 284.4x | 13.7% | +5.5% | -12.5% | 3/5 | +26.3% | -48.3% | 18.6% | 0.6x | 2026-07-29 | WATCHING | — | Tier 4 — EPS declining at P/E 264.9x; architecture royalty thesis not yet in GAAP numbers. | 2026-04-28 |
| ASML | TAILWIND — AI SC L2 | $584.52B | +115.9% | 58.6x | 64.3% | +6.4% | +22.6% | 5/5 | +13.2% | -466.3% | 34.8% | 0.3x | 2026-07-15 | WATCHING | — | Tier 3 spread +85.0%; EUV monopoly structural premium; FCF YoY extreme negative likely one-time. | 2026-04-28 |
| AMKR | TAILWIND — AI SC L3 | $17.91B | +306.5% | 41.3x | 10.1% | +68.4% | +288.2% | 5/5 | +27.5% | -42.6% | 7.6% | 1.3x | 2026-07-27 | WATCHING | — | Tier 2 spread +17.9% (vs_1Y +313.2% minus EPS YoY +295.3%); EPS, FCF, and Rev all genuinely strong. | — |
| AVGO | TAILWIND — AI SC L6 | $1.95T | +100.2% | 80.6x | 21.2% | +15.9% | +31.6% | 5/5 | +29.5% | +33.2% | 40.9% | 2.2x | 2026-06-03 | WATCHING | — | Tier 3 estimated; data not yet pulled — run tracker_update.py to populate. | — |
| GLW | TAILWIND — AI SC L7 | $156.70B | +311.0% | 86.9x | 10.7% | +46.7% | +138.9% | 5/5 | +20.0% | +152.6% | 15.3% | 3.1x | 2026-08-04 | WATCHING | — | Tier 3 spread +113%; re-rating from depressed base; QoQ solid. | — |
| HON | TAILWIND — AI SC L9 | $136.91B | +2.8% | 30.6x | 12.3% | +30.9% | -41.9% | 5/5 | -6.9% | -352.3% | 14.9% | 6.6x | 2026-07-23 | WATCHING | — | Tier 4 — EPS declining -42.4%, FCF -352.3%. Thesis needs catalyst before promoting. | 2026-04-28 |
| JCI | TAILWIND — AI SC L9 | $85.23B | +54.7% | 24.9x | 16.3% | +36.9% | +38.9% | 5/5 | +8.2% | +19.6% | 13.6% | 5.4x | 2026-08-04 | WATCHING | — | Tier 3 spread +42.1%; earnings and FCF genuinely growing; Debt/OCF 5.4x borderline. | 2026-04-28 |
| ORCL | TAILWIND — AI SC L13 | $559.48B | +30.8% | 34.9x | 12.2% | +17.5% | +24.5% | 5/5 | +21.7% | -16274.6% | 30.8% | 6.9x | 2026-06-10 | WATCHING | — | Tier 2 spread +2.3% — near Tier 1; FCF YoY -16274.6% is almost certainly a data error; manual audit needed. | 2026-04-28 |
| SNOW | TAILWIND — AI SC L13 | $53.14B | -11.6% | — | -71.6% | -0.1% | +9.1% | 0/5 | +30.1% | +81.5% | -30.6% | 2.2x | 2026-05-27 | WATCHING | — | Spread -19.4% but EPS still deeply negative GAAP (0/5 profitable). Rev +30.1% and FCF +81.5% are the real signals. Promote only when GAAP turns positive. | 2026-04-28 |
| COP | TAILWIND | $139.96B | +33.8% | 19.5x | 9.8% | -1.0% | -20.2% | 5/5 | -2.5% | +56.9% | 18.3% | 1.3x | 2026-08-06 | WATCHING | — | ConocoPhillips — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| EOG | TAILWIND | $69.72B | +23.6% | 12.9x | 16.1% | +33.8% | +39.6% | 5/5 | +15.7% | +83.0% | 36.9% | 0.8x | 2026-08-06 | WATCHING | — | EOG Resources — upstream E&P; AI data center power demand angle. Run tracker_update.py to populate. | 2026-04-28 |
| LIN | TAILWIND — AI SC L1 | $228.46B | +10.4% | 32.8x | 12.1% | +4.4% | +13.4% | 5/5 | +8.2% | +0.8% | 28.8% | 2.4x | 2026-08-07 | WATCHING | — | Linde — industrial/process gases for semiconductor fabs. Run tracker_update.py to populate. | 2026-04-28 |
| APD | TAILWIND — AI SC L1 | $65.69B | +12.3% | 31.2x | 6.4% | +3441.2% | +141.1% | 5/5 | +8.8% | +250.6% | 18.4% | 4.5x | 2026-07-30 | WATCHING | — | Air Products and Chemicals — industrial gases, hydrogen. Run tracker_update.py to populate. | 2026-04-28 |

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
| TEAM | LOSER | 2026-04-28 | Yrs Profitable 0/5, EPS YoY -6.7%, Avg QoQ -28.4%, Op Margin -3.2% — structural unprofitability, not dislocation. |
| PFE | TAILWIND | 2026-04-28 | Post-COVID earnings collapse — EPS YoY -500.6%, Rev -1.2%, FCF -22.4%. No AI thesis. |
| T | TAILWIND | 2026-04-28 | EPS YoY -11.5%, FCF -43.8%, revenue barely growing. No catalyst. |

---

## Trade Tracker

Market data columns updated daily by `Scripts/tracker_update.py`. Use Price vs. Entry Price to identify add-to-position opportunities.

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Price | vs_1Y | P/E | Avg EPS QoQ (4Q) | EPS YoY | Rev YoY | Next Earnings | Thesis |
|--------|------------|-------------|--------|------------|-------|-------|-----|------------------|---------|---------|---------------|--------|
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | $256.51 | -33.2% | 14.9x | +2.8% | +11.4% | +12.0% | 2026-06-11 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | $271.17 | +41.2% | 32.4x | +16.1% | +74.8% | +16.6% | 2026-07-30 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | $186.34 | -32.9% | 23.9x | +5.1% | +18.3% | +12.1% | 2026-05-27 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | $734.96 | +31.2% | — | — | — | — | — | — |

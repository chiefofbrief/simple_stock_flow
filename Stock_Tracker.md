# Ticker Tracker

---

## PIPELINE

Stocks under active analysis. Work through phases sequentially per `GEMINI.md`. Consider an initial position after Earnings; scale/exit decision after Footnotes; full position after Synthesis. Market data columns updated by `Scripts/tracker_update.py`.

**Column Guide**
- **Tag**: `LOSER` or `TAILWIND` — see `GEMINI.md` for the full definition and analytical framework for each type
- **Origin**: `Primary` = identified directly; `via [TICKER]` = added as peer of another stock
- **Sector Theme**: Maps to a sector in `context_sectors.md`. Blank for LOSERs unless a sector applies.
- **Mkt Cap**: Market capitalization — scale and liquidity indicator (updated by script)
- **Price**: Current price (updated by script)
- **vs_3M**: Price change vs. 3 months ago — short-term momentum or dip signal (updated by script)
- **vs_1Y**: Price change vs. 1 year ago — medium-term trend (updated by script)
- **52w_below**: % below 52-week high — how far off peak; larger = deeper dip (updated by script)
- **Price CAGR (5yr)**: 5-year annualized price growth rate — underlying trajectory. For recent IPOs with less than 5 years of history, reflects the available period only. (updated by script)
- **P/E**: Trailing twelve-month P/E ratio — current valuation based on actual earnings (updated by script)
- **EPS CAGR**: 5-year annualized EPS growth rate — fundamental momentum (updated by script)
- **Beats (4Q)**: Last 4 quarters vs. estimates, newest first — e.g. `+/+/-/+` (updated by script)
- **Fwd Delta**: Next quarter estimate minus last reported EPS; positive = growth expected (updated by script)
- **Next Earnings**: Date of next earnings report (updated by script)
- **Phase**: Current workflow step — `Price & Earnings` → `Financials` → `Footnotes` → `Earnings Calls` → `Research` → `Synthesis`
- **Last Run**: Date of last completed workflow step
- **Status**: `PASS` (advancing) | `BUY` | `HOLD` | `FAIL` (screened out)
- **Added**: Date added to PIPELINE

| Ticker | Tag | Origin | Sector Theme | Mkt Cap | Price | vs_3M | vs_1Y | 52w_below | Price CAGR (5yr) | P/E | EPS CAGR | Beats (4Q) | Fwd Delta | Next Earnings | Phase | Last Run | Status | Thesis | Added |
|--------|-----|--------|--------------|---------|-------|-------|-------|-----------|------------------|-----|----------|------------|-----------|---------------|-------|----------|--------|--------|-------|
| AXON | TAILWIND | Primary | Defense & Aerospace | $32.39B | $402.85 | -36.7% | -28.0% | 54.5% | +22.3% | 58.8x | +30.8% | +/-/+/+ | $-0.55 | 2026-05-06 | Financials | 2026-04-14 | PASS | AXON_Thesis.md | 2026-04-14 |
| META | TAILWIND | Primary | AI — Software & Disruption | $1.74T | $688.55 | +11.1% | +37.7% | 13.3% | +18.0% | 23.2x | +24.9% | +/+/+/+ | $-2.19 | 2026-04-29 | Earnings | 2026-04-14 | PASS | META_Thesis.md | 2026-04-14 |
| RDDT | TAILWIND | Primary | AI — Software & Disruption | $31.29B | $163.80 | -29.1% | +70.3% | 42.1% | +74.0% | 62.5x | — | +/-/+/+ | $-0.62 | 2026-04-30 | Earnings | 2026-04-14 | PASS | RDDT_Thesis.md | 2026-04-14 |
| UMAC | TAILWIND | Primary | Defense & Aerospace | $547.90M | $14.09 | -23.9% | +178.5% | 39.7% | +103.8% | — | — | -/-/-/- | $+0.20 | 2026-05-14 | Earnings | 2026-04-14 | PASS | UMAC_Thesis.md | 2026-04-14 |
| DPZ | LOSER | Primary | — | $12.51B | $372.06 | -6.6% | -18.9% | 24.2% | +1.5% | 21.2x | +7.2% | -/+/-/+ | $-1.01 | 2026-04-27 | Price & Earnings | 2026-04-15 | PASS | DPZ_Thesis.md | 2026-04-15 |
| MCD | LOSER | Primary | — | $221.32B | $311.36 | +1.8% | +2.3% | 8.4% | +8.9% | 25.5x | +15.1% | +/-/+/+ | $-0.36 | 2026-05-07 | Price & Earnings | 2026-04-15 | PASS | MCD_Thesis.md | 2026-04-15 |

---

## WATCHLIST

Stocks under continuous monitoring. Market data columns are populated by `Scripts/tracker_update.py` (run weekly). Move a stock to PIPELINE when an entry signal is triggered — price dislocation, earnings inflection, or P/E compression relative to the thesis. Move to DROPPED if the thesis no longer applies.

**Column Guide** (shared columns same as PIPELINE above; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (signal triggered, move to PIPELINE) | `DROPPED`

| Ticker | Tag | Origin | Sector Theme | Mkt Cap | Price | vs_3M | vs_1Y | 52w_below | Price CAGR (5yr) | P/E | EPS CAGR | Beats (4Q) | Fwd Delta | Next Earnings | Status | Thesis |
|--------|-----|--------|--------------|---------|-------|-------|-------|-----------|------------------|-----|----------|------------|-----------|---------------|--------|--------|
| GOOGL | TAILWIND | Primary | AI — Infrastructure & Power | $4.13T | $341.68 | +3.6% | +126.8% | 2.0% | +26.3% | 31.6x | +29.7% | +/+/+/+ | $-0.18 | 2026-04-29 | WATCHING | — |
| BKH | TAILWIND | Primary | AI — Infrastructure & Power | $5.74B | $76.07 | +4.7% | +30.9% | 3.3% | +6.6% | 18.5x | +2.6% | +/+/+/- | $+0.47 | 2026-05-06 | WATCHING | BKH_Thesis.md |
| TSM | TAILWIND | Primary | AI — Compute & Chips | $1.92T | $370.50 | +8.4% | +146.5% | 4.8% | +26.3% | 30.8x | +26.2% | +/+/+/+ | $+0.09 | 2026-07-16 | WATCHING | TSM_Thesis.md |
| AIG | LOSER | Primary | — | $42.22B | $78.68 | +8.5% | -0.9% | 9.3% | +13.3% | 11.0x | +23.2% | +/+/+/+ | $-0.05 | 2026-04-30 | WATCHING | — |
| AVAV | LOSER | Primary | — | $9.56B | $191.42 | -51.3% | +29.7% | 54.2% | +10.2% | 63.6x | +10.7% | -/-/-/+ | $+0.84 | 2026-06-23 | WATCHING | — |
| CNC | LOSER | Primary | — | $18.76B | $38.17 | -16.6% | -37.1% | 40.5% | -9.5% | 18.6x | -16.3% | +/+/-/+ | $+3.32 | 2026-04-28 | WATCHING | — |
| FICO | LOSER | Primary | — | $25.47B | $1073.52 | -31.5% | -43.8% | 51.6% | +16.6% | 34.1x | +24.0% | +/+/+/+ | $+3.57 | 2026-04-28 | WATCHING | — |
| GIS | LOSER | Primary | — | $18.95B | $35.50 | -18.9% | -34.8% | 35.8% | -6.6% | 10.6x | -3.4% | -/+/+/+ | $+0.19 | 2026-06-24 | WATCHING | — |
| IT | LOSER | Primary | — | $11.14B | $154.62 | -33.0% | -61.5% | 65.8% | -3.2% | 11.7x | +21.9% | +/+/+/+ | $-1.02 | 2026-05-05 | WATCHING | — |
| KD | LOSER | Primary | — | $3.30B | $14.40 | -42.9% | -50.7% | 67.4% | -15.7% | 8.0x | — | -/+/+/+ | $-0.09 | 2026-05-06 | WATCHING | — |
| MSFT | LOSER | Primary | — | $3.14T | $422.79 | -7.9% | +15.8% | 23.4% | +12.9% | 27.5x | +18.0% | +/+/+/+ | $-0.07 | 2026-04-29 | WATCHING | — |
| NFLX | LOSER | Primary | — | $412.78B | $97.31 | +10.6% | +0.0% | 27.4% | +12.8% | 31.4x | +30.2% | +/+/-/+ | $-0.40 | 2026-07-16 | WATCHING | — |
| NOW | LOSER | Primary | — | $101.11B | $96.66 | -24.1% | -37.4% | 54.3% | -0.7% | 27.5x | +97.1% | +/+/+/+ | $+0.03 | 2026-04-22 | WATCHING | — |
| NVO | LOSER | Primary | — | $180.07B | $40.52 | -33.3% | -27.8% | 48.5% | +5.4% | 10.4x | +23.2% | +/+/+/+ | $-0.13 | 2026-05-06 | WATCHING | — |
| QCOM | LOSER | Primary | — | $145.47B | $136.20 | -14.0% | +2.0% | 33.1% | +2.7% | 11.2x | +17.7% | +/+/+/+ | $-0.93 | 2026-04-29 | WATCHING | — |
| SPGI | LOSER | Primary | — | $132.24B | $442.57 | -18.8% | -3.6% | 23.1% | +5.3% | 24.8x | +8.8% | -/+/+/+ | $+0.54 | 2026-04-28 | WATCHING | — |
| SYK | LOSER | Primary | — | $131.38B | $343.32 | -5.4% | +0.0% | 14.6% | +7.9% | 25.2x | +12.9% | +/+/+/+ | $-1.47 | 2026-04-30 | WATCHING | — |
| VWAGY | LOSER | Primary | — | $55.39B | $11.05 | -5.5% | +10.5% | 13.9% | -16.7% | 7.4x | -5.1% | +/-/-/+ | $-0.17 | 2026-04-29 | WATCHING | — |
| WDAY | LOSER | Primary | — | $32.83B | $123.83 | -33.7% | -44.0% | 55.1% | -12.6% | 13.4x | +26.3% | +/+/+/+ | $+0.02 | 2026-05-28 | WATCHING | — |

---

## Trade Tracker

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Thesis |
|--------|------------|-------------|--------|------------|--------|
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | — |

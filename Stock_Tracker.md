# Ticker Tracker

---

## PIPELINE

Stocks under active analysis. Work through phases sequentially per `GEMINI.md`. Consider an initial position after Earnings; scale/exit decision after Footnotes; full position after Synthesis. Market data columns updated by `Scripts/tracker_update.py`.

**Column Guide**
- **Tag**: `LOSER` or `TAILWIND` — see `GEMINI.md` for the full definition and analytical framework for each type
- **Origin**: `Primary` = identified directly; `via [TICKER]` = added as peer of another stock
- **Sector Theme**: Maps to a layer in `context_ai_supply_chain.md` (e.g., `AI SC — Layer 4`). Blank for LOSERs unless a layer applies.
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
| AXON | TAILWIND | Primary | — | $32.46B | $403.75 | -34.9% | -27.8% | 54.4% | +22.3% | 58.9x | +30.8% | +/-/+/+ | $-0.55 | 2026-05-06 | Financials | 2026-04-14 | PASS | AXON_Thesis.md | 2026-04-14 |
| META | TAILWIND | Primary | AI SC — Layer 10 | $1.70T | $670.91 | +11.1% | +34.2% | 15.5% | +17.5% | 22.6x | +24.9% | +/+/+/+ | $-2.17 | 2026-04-29 | Earnings | 2026-04-14 | PASS | META_Thesis.md | 2026-04-14 |
| RDDT | TAILWIND | Primary | — | $31.77B | $166.30 | -26.2% | +72.9% | 41.2% | +75.2% | 63.5x | — | +/-/+/+ | $-0.62 | 2026-04-30 | Earnings | 2026-04-14 | PASS | RDDT_Thesis.md | 2026-04-14 |
| UMAC | TAILWIND | Primary | — | $600.39M | $15.44 | -17.3% | +205.1% | 34.0% | +112.2% | — | — | -/-/-/- | $+0.20 | 2026-05-14 | Earnings | 2026-04-14 | PASS | UMAC_Thesis.md | 2026-04-14 |
| DPZ | LOSER | Primary | — | $12.42B | $369.46 | -4.2% | -19.5% | 24.7% | +1.4% | 21.0x | +7.2% | -/+/-/+ | $-1.05 | 2026-04-27 | Price & Earnings | 2026-04-15 | PASS | DPZ_Thesis.md | 2026-04-15 |
| MCD | LOSER | Primary | — | $218.18B | $306.94 | +1.9% | +0.9% | 9.7% | +8.6% | 25.2x | +15.1% | +/-/+/+ | $-0.37 | 2026-05-07 | Price & Earnings | 2026-04-15 | PASS | MCD_Thesis.md | 2026-04-15 |

---

## WATCHLIST

Stocks under continuous monitoring. Market data columns are populated by `Scripts/tracker_update.py` (run weekly). Move a stock to PIPELINE when an entry signal is triggered — price dislocation, earnings inflection, or P/E compression relative to the thesis. Move to DROPPED if the thesis no longer applies.

**Column Guide** (shared columns same as PIPELINE above; WATCHLIST-specific below)
- **Status**: `WATCHING` | `READY` (signal triggered, move to PIPELINE) | `DROPPED`

| Ticker | Tag | Origin | Sector Theme | Mkt Cap | Price | vs_3M | vs_1Y | 52w_below | Price CAGR (5yr) | P/E | EPS CAGR | Beats (4Q) | Fwd Delta | Next Earnings | Status | Thesis | Notes |
|--------|-----|--------|--------------|---------|-------|-------|-------|-----------|------------------|-----|----------|------------|-----------|---------------|--------|--------|-------|
| GOOGL | TAILWIND | Primary | AI SC — Layer 10 | $4.08T | $337.42 | +4.9% | +124.0% | 3.2% | +26.0% | 31.2x | +29.7% | +/+/+/+ | $-0.19 | 2026-04-29 | WATCHING | — | — |
| BKH | TAILWIND | Primary | AI SC — Layer 8 | $5.75B | $75.60 | +5.2% | +30.1% | 3.9% | +6.5% | 18.4x | +2.6% | +/+/+/- | $+0.47 | 2026-05-06 | WATCHING | BKH_Thesis.md | — |
| TSM | TAILWIND | Primary | AI SC — Layer 3 | $1.90T | $366.24 | +12.2% | +143.7% | 5.9% | +26.0% | 30.4x | +26.2% | +/+/+/+ | $+0.11 | 2026-07-16 | WATCHING | TSM_Thesis.md | — |
| AIG | LOSER | Primary | — | $42.15B | $78.56 | +9.1% | -1.0% | 9.5% | +13.3% | 11.0x | +23.2% | +/+/+/+ | $-0.05 | 2026-04-30 | WATCHING | — | — |
| AVAV | LOSER | Primary | — | $9.85B | $197.23 | -40.4% | +33.6% | 52.8% | +10.8% | 65.5x | +10.7% | -/-/-/+ | $+0.84 | 2026-06-23 | WATCHING | — | — |
| CNC | LOSER | Primary | — | $18.84B | $38.31 | -16.3% | -36.9% | 40.3% | -9.4% | 18.7x | -16.3% | +/+/-/+ | $+3.31 | 2026-04-28 | WATCHING | — | — |
| FICO | LOSER | Primary | — | $25.23B | $1063.41 | -28.8% | -44.3% | 52.0% | +16.4% | 33.8x | +24.0% | +/+/+/+ | $+3.57 | 2026-04-28 | WATCHING | — | — |
| GIS | LOSER | Primary | — | $18.83B | $35.28 | -19.3% | -35.2% | 36.2% | -6.7% | 10.6x | -3.4% | -/+/+/+ | $+0.19 | 2026-06-24 | WATCHING | — | — |
| IT | LOSER | Primary | — | $11.01B | $156.23 | -29.6% | -61.1% | 65.4% | -3.0% | 11.8x | +21.9% | +/+/+/+ | $-1.02 | 2026-05-05 | WATCHING | — | — |
| KD | LOSER | Primary | — | $3.36B | $14.64 | -39.8% | -49.9% | 66.9% | -15.4% | 8.2x | — | -/+/+/+ | $-0.09 | 2026-05-06 | WATCHING | — | — |
| MSFT | LOSER | Primary | AI SC — Layer 10 | $3.10T | $418.07 | -7.8% | +14.5% | 24.3% | +12.6% | 27.2x | +18.0% | +/+/+/+ | $-0.07 | 2026-04-29 | WATCHING | — | — |
| NFLX | LOSER | Primary | — | $400.39B | $94.83 | +8.7% | -2.5% | 29.3% | +12.3% | 30.6x | +30.2% | +/+/-/+ | $-0.39 | 2026-07-16 | WATCHING | — | — |
| NOW | LOSER | Primary | — | $104.31B | $99.72 | -20.5% | -35.4% | 52.8% | -0.1% | 28.4x | +97.1% | +/+/+/+ | $+0.03 | 2026-04-22 | WATCHING | NOW_Thesis.md | Filtered 2026-04-21 after full analysis (P&E → Financials → Footnotes). GAAP P/E ~61x vs. non-GAAP 29x (SBC $1.96B/yr = 15% of rev). $9B pending cash acquisitions (Armis $7.75B + Veza $1.25B) require major new debt — Debt/OCF rising from 0.59x to ~2-2.5x post-close. Armis is a strategic pivot to cybersecurity; rationale unproven. Operating leverage decelerating (4.81x→1.61x). Revisit after Armis closes (H2 2026) and organic growth rate is established. |
| NVO | LOSER | Primary | — | $179.81B | $40.46 | -31.6% | -27.9% | 48.6% | +5.3% | 10.3x | +23.2% | +/+/+/+ | $-0.13 | 2026-05-06 | WATCHING | — | — |
| QCOM | LOSER | Primary | AI SC — Layer 12 | $146.88B | $137.52 | -10.2% | +3.0% | 32.5% | +2.9% | 11.3x | +17.7% | +/+/+/+ | $-0.93 | 2026-04-29 | WATCHING | — | — |
| SPGI | LOSER | Primary | — | $132.29B | $442.74 | -14.5% | -3.6% | 23.1% | +5.3% | 24.8x | +8.8% | -/+/+/+ | $+0.52 | 2026-04-28 | WATCHING | — | — |
| SYK | LOSER | Primary | — | $129.58B | $338.34 | -5.7% | -1.4% | 15.8% | +7.6% | 24.8x | +12.9% | +/+/+/+ | $-1.48 | 2026-04-30 | WATCHING | — | — |
| VWAGY | LOSER | Primary | — | $54.49B | $10.87 | -4.6% | +8.7% | 15.3% | -17.0% | 7.3x | -5.1% | +/-/-/+ | $-0.17 | 2026-04-30 | WATCHING | — | — |
| WDAY | LOSER | Primary | — | $33.92B | $127.94 | -30.1% | -42.1% | 53.6% | -12.1% | 13.9x | +26.3% | +/+/+/+ | $+0.02 | 2026-05-21 | WATCHING | — | — |
| AMKR | TAILWIND | Primary | AI SC — Layer 3 | $17.21B | $69.44 | +41.8% | +340.1% | 0.4% | +24.8% | 46.0x | +1.7% | +/+/+/+ | $-0.46 | 2026-04-27 | WATCHING | — | — |
| AVGO | TAILWIND | Primary | AI SC — Layer 6 | $1.89T | $399.63 | +20.4% | +135.6% | 3.2% | +54.7% | 55.0x | +25.3% | +/+/+/+ | $+0.35 | 2026-06-03 | WATCHING | — | — |
| BE | TAILWIND | Primary | AI SC — Layer 8 | $52.47B | $218.27 | +43.8% | +1183.9% | 4.9% | +49.8% | 299.0x | — | +/+/+/+ | $-0.36 | 2026-04-28 | WATCHING | — | — |
| CCJ | TAILWIND | Primary | AI SC — Layer 1 | $53.83B | $123.62 | +6.8% | +200.8% | 8.6% | +47.8% | 120.0x | — | +/-/+/+ | $-0.10 | 2026-05-05 | WATCHING | — | — |
| CDNS | TAILWIND | Primary | AI SC — Layer 2 | $87.95B | $318.54 | +3.8% | +22.4% | 15.4% | +17.7% | 44.6x | +20.7% | +/+/+/+ | $-0.08 | 2026-04-27 | WATCHING | — | — |
| CEG | TAILWIND | Primary | AI SC — Layer 8 | $89.80B | $287.56 | -2.5% | +39.8% | 30.1% | +52.4% | 30.6x | +39.1% | +/-/+/- | $+0.26 | 2026-05-11 | WATCHING | — | — |
| COHR | TAILWIND | Primary | AI SC — Layer 7 | $55.11B | $347.51 | +79.6% | +528.5% | 0.3% | +37.0% | 79.7x | +4.1% | +/+/+/+ | $+0.12 | 2026-05-06 | WATCHING | — | — |
| CRWV | TAILWIND | Primary | AI SC — Layer 11 | $61.73B | $117.43 | +23.3% | +200.4% | 37.2% | +168.6% | — | — | -/+/-/? | $-0.01 | 2026-05-13 | WATCHING | — | — |
| FCX | TAILWIND | Primary | AI SC — Layer 1 | $100.86B | $70.18 | +17.1% | +115.8% | 1.1% | +17.4% | 40.1x | +26.0% | +/+/+/+ | $+0.00 | 2026-04-23 | WATCHING | — | — |
| GEV | TAILWIND | Primary | AI SC — Layer 8 | $266.88B | $990.18 | +44.7% | +206.7% | 2.0% | +149.8% | 55.6x | — | +/-/+/+ | $-11.60 | 2026-04-22 | WATCHING | — | — |
| GLW | TAILWIND | Primary | AI SC — Layer 7 | $142.06B | $165.38 | +79.0% | +304.3% | 6.4% | +32.9% | 65.4x | +12.6% | +/+/+/+ | $-0.02 | 2026-04-28 | WATCHING | — | — |
| KLAC | TAILWIND | Primary | AI SC — Layer 2 | $237.21B | $1805.32 | +21.6% | +186.7% | 0.1% | +40.3% | 50.9x | +25.3% | +/+/+/+ | $+0.31 | 2026-04-29 | WATCHING | — | — |
| LRCX | TAILWIND | Primary | AI SC — Layer 2 | $328.63B | $263.16 | +18.5% | +315.7% | 3.8% | +34.7% | 53.7x | +19.0% | +/+/+/+ | $+0.09 | 2026-04-22 | WATCHING | — | — |
| MP | TAILWIND | Primary | AI SC — Layer 1 | $11.77B | $66.23 | -3.1% | +151.3% | 33.9% | +12.6% | — | — | +/+/+/- | $-0.11 | 2026-05-07 | WATCHING | — | — |
| MRVL | TAILWIND | Primary | AI SC — Layer 6 | $129.28B | $147.84 | +85.4% | +186.7% | 1.2% | +24.3% | 51.9x | +25.1% | +/+/-/+ | $+0.00 | 2026-06-04 | WATCHING | — | — |
| MU | TAILWIND | Primary | AI SC — Layer 5 | $505.70B | $448.42 | +22.9% | +553.3% | 4.8% | +37.7% | 20.5x | +43.0% | +/+/+/+ | $+7.10 | 2026-06-24 | WATCHING | — | — |
| SNPS | TAILWIND | Primary | AI SC — Layer 2 | $88.30B | $460.95 | -9.8% | +11.5% | 29.3% | +12.8% | 33.6x | +17.8% | +/+/-/+ | $-0.60 | 2026-05-27 | WATCHING | — | — |
| TH | TAILWIND | Primary | AI SC — Layer 9 | $1.56B | $15.61 | +107.6% | +134.7% | 0.2% | +42.4% | — | — | -/+/-/- | $+0.04 | 2026-05-11 | WATCHING | — | — |
| VRT | TAILWIND | Primary | AI SC — Layer 9 | $120.29B | $314.41 | +79.5% | +330.0% | 0.4% | +70.6% | 75.0x | +39.3% | +/+/+/+ | $-0.34 | 2026-04-22 | WATCHING | — | — |
| VST | TAILWIND | Primary | AI SC — Layer 8 | $54.03B | $159.60 | +1.9% | +39.0% | 27.2% | +56.1% | 73.4x | +6.7% | -/-/-/- | $+0.74 | 2026-05-07 | WATCHING | — | — |
| FIG | LOSER | Primary | — | $9.27B | $19.01 | -31.5% | — | 86.7% | -88.5% | 50.3x | — | +/+/+/? | $-0.02 | 2026-04-21 | WATCHING | — | — |
| INTU | LOSER | Primary | — | $112.65B | $404.83 | -23.2% | -30.3% | 49.9% | +1.8% | 18.5x | +22.5% | +/+/+/+ | $+8.33 | 2026-05-21 | WATCHING | — | — |

---

## Trade Tracker

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Thesis |
|--------|------------|-------------|--------|------------|--------|
| ADBE | 2026-04-17 | $250.00 | 20 | $5,000.00 | ADBE_Thesis.md |
| AMZN | 2026-02-05 | $214.89 | 46.535 | $9,999.78 | — |
| CRM | 2026-04-17 | $181.70 | 27.517 | $4,999.84 | — |
| IVV | — | $586.94 | 36.91 | $21,664.06 | — |

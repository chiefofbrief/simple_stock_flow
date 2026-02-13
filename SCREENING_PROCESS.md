# Screening Process

## Overview

Three-category screening list (Losers, AI, Other) with a two-step screening funnel. Each step has a data script and an LLM analysis prompt:

1. **Price** — price context for all tickers → LLM triage (cut/prioritize)
2. **Earnings** — earnings + valuation for survivors → LLM full assessment

---

## Categories

| Category | Purpose | Price Step | Earnings Step |
|----------|---------|-----------|---------------|
| **Losers** | Beaten-down stocks | Filter + context (cut non-candidates) | P/E, EPS trend, price-earnings correlation |
| **AI** | AI upside plays | Context + prioritize (pullbacks > ATHs) | P/E, EPS trend, price-earnings correlation |
| **Other** | Watch list | Context (promote, demote, or prune) | Only if promoted |

All tickers get the same data and table output from the script. The category distinction matters in the LLM analysis step (see prompt sections below).

---

## Step 1: Price

### Script: `scripts/price.py`

No AI. Fetches price data, computes metrics, outputs a comparison table.

**Input**: Tickers from CLI args or parsed from SESSION_NOTES by category.

```
python scripts/price.py NOW CRM ADBE KD MAT
python scripts/price.py --category losers
python scripts/price.py --all
```

**Data Source**: FMP API (replacing AlphaVantage). One API call per ticker (monthly adjusted close, 5 years).

**Output**:
- Summary table to stdout
- Per-ticker JSON: `data/tickers/{TICKER}/raw/{TICKER}_price.json`
- Batch summary: `data/screening/Price_YYYY-MM-DD.txt`

#### Metrics

Two core questions drive the metrics:

**"How does the current price compare to historical levels?"**

| Metric | Description |
|--------|-------------|
| `vs_1yr` | Current price vs. close 1 year ago (%) |
| `vs_2yr` | Current price vs. close 2 years ago (%) |
| `vs_3yr` | Current price vs. close 3 years ago (%) |
| `vs_4yr` | Current price vs. close 4 years ago (%) |
| `vs_5yr` | Current price vs. close 5 years ago (%) |
| `price_vs_5yr_avg` | Current price vs. 5-year average price (%) |
| `52w_high` | 52-week high |
| `52w_low` | 52-week low |
| `52w_position` | Position in 52-week range (0% = at low, 100% = at high) |
| `cagr_5yr` | 5-year compound annual growth rate |
| `upside_if_revert` | Return if price reverted to 1-year average (%) |

**"How volatile is the price?"**

| Metric | Description |
|--------|-------------|
| `cv` | Coefficient of Variation — overall price volatility over 5 years |
| `z_score` | How many standard deviations is the recent 1-month move from the mean monthly return. Flags anomalous drops (or spikes). |
| `drop_vs_max_drawdown` | Recent 1-month drop as % of worst drawdown in past 5 years. High % = approaching historical worst. Low % = routine. |
| `max_drawdown_5yr` | Worst peak-to-trough drawdown over 5 years (%) |

#### Per-Ticker JSON (supplementary, not in table)

These are computed and saved to the per-ticker JSON for the LLM to reference during analysis, but not shown in the summary table:

- `trend_slope_1yr`: Linear regression slope of monthly prices over 12 months
- `trend_slope_5yr`: Linear regression slope of monthly prices over 5 years
- `monthly_returns`: Full array of monthly returns (for LLM to inspect distribution)

#### Output Table

```
| Ticker | Price  | vs1Y  | vs2Y  | vs3Y  | vs5Y  | CV   | Z-Score | 52w Pos | Drop/MaxDD | Revert↑ | 5yr CAGR |
|--------|--------|-------|-------|-------|-------|------|---------|---------|------------|---------|----------|
| NOW    | $106   | -33%  | -20%  | +15%  | +180% | 0.38 | -2.8    | 12%     | 55%        | +28%    | +22.8%   |
| KD     | $24.50 | -52%  | -48%  | -45%  | -30%  | 0.52 | -4.2    | 3%      | 92%        | +45%    | -5.1%    |
| MAT    | $16.43 | -22%  | -10%  | -5%   | +5%   | 0.31 | -3.1    | 8%      | 78%        | +18%    | +1.0%    |
```

### Prompt: `guidance/prompts/price.md`

LLM reviews the price context table + SESSION_NOTES context.

#### All tickers — two core questions:

1. **"How does the current price compare to historical levels?"** — The vs1Y–vs5Y columns, 52w position, CAGR, and reversion upside tell this story. Is the stock actually cheap, or just cheaper than a recent peak?
2. **"How volatile is the price?"** — CV, z-score, and drop/max drawdown. A 20% drop in a stock with 0.15 CV is a different signal than a 20% drop in a stock with 0.50 CV.

#### Losers — additional question:

3. **"How does the recent drop compare to historical drops and volatility?"** — This is the key Losers-specific question. Is this drop a big deal, normal volatility, or a long-overdue pullback? Specifically:
   - Is the drop anomalous for this stock? (z-score)
   - Has the stock experienced similar or worse drops before? (drop/max drawdown)
   - Is the stock in a prolonged multi-year decline, or is this a sudden break from an uptrend? (vs1Y–vs5Y pattern)
   - Should this stock be removed from the Losers list? Reasons to cut:
     - Not actually a loser — all timeframes positive, just a minor dip
     - Price too high — still well above historical averages despite the "drop"
     - Prolonged decline — down across all 5 years, no recovery pattern, likely structural
     - Normal volatility — high CV stock doing what it always does

#### AI tickers:

No filtering — these are structural/momentum plays. The LLM uses price context to **prioritize**: an AI stock that's pulled back from highs is a more interesting entry point than one at all-time highs. Flag any that look overextended.

#### Other tickers:

The LLM recommends: **promote** (to Losers or AI if the price pattern fits), **keep** (on watch list), or **prune** (remove — no clear reason to track).

#### Output

List of tickers advancing to Step 2, organized by category. Brief rationale for any cuts or category changes.

---

## Step 2: Earnings

### Script: `scripts/earnings.py`

Fetches earnings data, computes P/E and valuation metrics. Runs only on survivors from Step 1.

**Input**: Tickers from CLI args.

```
python scripts/earnings.py NOW CRM ADBE
```

**Data Source**: FMP API.

**Output**:
- Per-ticker JSON: `data/tickers/{TICKER}/raw/{TICKER}_earnings.json`
- Per-ticker text summary: `data/tickers/{TICKER}/raw/{TICKER}_earnings.txt`
- Batch summary: `data/screening/Earnings_YYYY-MM-DD.txt`

#### Metrics

- Trailing P/E (TTM EPS)
- P/E vs. 5-year average P/E
- EPS trend (5-year CAGR, quarterly trajectory)
- Price-EPS correlation (5-year)
- EPS vs. analyst consensus (recent quarters)

### Prompt: `guidance/prompts/earnings.md`

LLM reviews earnings data **combined with the price context from Step 1**. Full screening assessment addressing:

- Price-earnings relationship (does price track fundamentals?)
- Valuation vs. historical norms
- Earnings quality and trajectory
- Whether to advance to deep analysis (financial statements) or drop

Output: Screening assessment per ticker + updated Pipeline recommendations.

---

## SESSION_NOTES Integration

The `--category` flag parses `SESSION_NOTES.md` to extract tickers:

- `--category losers` → reads `### Screening Candidates — Losers` section
- `--category ai` → reads `### Screening Candidates — AI` section
- `--category other` → reads `### Screening Candidates — Other` section
- `--all` → reads all three sections

Extracts bold ticker symbols (e.g., `**NOW**`) via regex. Simple text parsing, no automation infrastructure required.

---

## Data Source: FMP

Replacing AlphaVantage due to pricing. Existing AlphaVantage scripts archived in `scripts/archive/` with `_alphavantage` suffix.

| | AlphaVantage (Archived) | FMP (Active) |
|---|---|---|
| **Free tier** | 25 calls/day | 250 calls/day |
| **Paid tier** | $50/mo for 75/min | ~$20/mo for higher limits |
| **Price (Step 1)** | TIME_SERIES_MONTHLY_ADJUSTED | `/stable/historical-price-eod/dividend-adjusted` (daily, split+dividend adjusted) |
| **Earnings (Step 2)** | EARNINGS endpoint | TBD (user to provide endpoints) |

---

## Workflow

### Weekly (30-60 min)
1. Run price context on all tickers: `python scripts/price.py --all`
2. Feed price table to LLM (`price.md` prompt) → get triage results
3. Run earnings on survivors: `python scripts/earnings.py NOW CRM ADBE ...`
4. Feed earnings + price context to LLM (`earnings.md` prompt) → get screening assessment
5. Update Pipeline in SESSION_NOTES based on results

### As-needed
- Re-run price context after significant market moves
- Run individual tickers as new candidates are added to SESSION_NOTES

---

## Implementation Status

| # | Item | Status |
|---|------|--------|
| 1 | Update `SCREENING_PROCESS.md` | Done |
| 2 | Archive existing scripts to `scripts/archive/` | Done — `prices_alphavantage.py`, `earnings_alphavantage.py`, `valuation_alphavantage.py` |
| 3 | Create `scripts/price.py` — price context script with FMP API | Done — tested with AAPL, TSLA |
| 4 | Create `guidance/prompts/price.md` — price triage prompt | Not started |
| 5 | Create `scripts/earnings.py` — earnings/valuation script with FMP API | Not started — needs FMP earnings endpoints |
| 6 | Create `guidance/prompts/earnings.md` — combined screening prompt | Not started |

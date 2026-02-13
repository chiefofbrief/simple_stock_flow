# Screening Process

## Overview

Three-category screening list (Losers, AI, Other) with a two-step funnel for prioritization: **price context first**, then **P/E analysis** for shortlisted candidates.

---

## Categories & Screening Approach

| Category | Count | Primary Screen | Secondary Screen |
|----------|-------|---------------|-----------------|
| **Losers** | ~34 | Price context (filter + context) | P/E analysis for survivors |
| **AI** | ~16 | Price context (context only) | Earnings growth / thesis validation |
| **Other** | ~26 | Price context (context only, as-needed) | Promote to Losers or AI, or prune |

**Losers** get the most aggressive screening — price context is used to *filter out* stocks that aren't actually cheap (e.g., down 20% this month but up 50% over 6 months). Survivors proceed to P/E analysis.

**AI stocks** don't get filtered on price — they're momentum/structural plays. But price context helps *prioritize* (e.g., an AI stock that's pulled back is more interesting than one at all-time highs).

**Other stocks** are a watch list. Price context is added periodically to determine if they should be promoted to Losers or AI, or pruned.

---

## Step 1: Price Context

### What We're Really Asking

The price analysis should answer three human-level questions:

**1. Severity — How bad is the recent drop, relative to this stock's normal behavior?**

A 20% drop in a low-volatility stock is very different from a 20% drop in a stock that regularly swings 15% monthly. Raw delta isn't enough — we need volatility-adjusted severity.

Metrics:
- `recent_drop`: Price change over 1 month (%)
- `monthly_volatility`: Standard deviation of monthly returns over 12 months
- `drop_z_score`: How many standard deviations is the recent drop from the mean monthly return? Higher absolute value = more anomalous.
- `drop_vs_max_drawdown`: Recent drop as a % of the worst drawdown in the past 5 years. If the stock has dropped 20% and its worst-ever 5yr drawdown was 25%, that's concerning. If worst was 60%, 20% is routine.

**2. Trend Context — Is this drop an anomaly, or part of a larger pattern?**

Is the stock pulling back within an uptrend (potential opportunity), continuing a long decline (falling knife), or just doing what it always does (noisy/sideways)?

Metrics:
- `return_1mo`, `return_6mo`, `return_1yr`, `return_5yr`: Returns at multiple timeframes.
- `trend_direction`: Derived from comparing timeframes. Possible values:
  - **"Pullback in uptrend"**: 1mo negative, 6mo+ positive. Most interesting for Losers.
  - **"Accelerating decline"**: 1mo negative, 6mo negative, 1yr negative. Falling knife risk.
  - **"Sustained decline"**: 1yr negative, 5yr negative. Structural problem.
  - **"Bounce in downtrend"**: 1mo positive, 6mo+ negative. Possibly a dead cat bounce.
  - **"Steady growth"**: All timeframes positive. Not a loser — filter out or deprioritize.
  - **"Sideways/choppy"**: Mixed signals, low magnitude across timeframes.
- `trend_slope_1yr`: Linear regression slope of monthly prices over 12 months (direction + steepness).
- `trend_slope_5yr`: Same over 5 years.

**3. Recovery Potential — Does this stock historically bounce back, or does it stay down?**

Even if the price has dropped, can we reasonably expect a rebound? Does the stock show long-term appreciation, or does it trade sideways / steadily decline?

Metrics:
- `cagr_5yr`: 5-year compound annual growth rate. Positive = stock has historically grown. Negative or near-zero = stuck.
- `recovery_history`: Of the stock's past significant drawdowns (>15%), what % of the time did it recover to pre-drawdown levels within 12 months?
- `price_vs_5yr_avg`: Current price relative to 5-year average price (%). Below average = potentially undervalued on a historical basis. But context matters — a stock in secular decline will always be "below average."
- `upside_if_revert`: If price reverted to 1-year average, what would the return be? Simple mean-reversion signal.

### What's NOT Useful

- **Delta with 52-week high**: Misleading for volatile stocks that spike and crash. A stock that briefly hit $200 on a meme rally and now trades at $100 shows "-50% from 52w high" but that's noise, not signal.
- **Raw price levels without volatility context**: A 10% drop means nothing without knowing if the stock normally moves 2% or 15% monthly.

### Output: Price Context Table

One table per batch, sorted by most actionable (for Losers: highest severity + pullback-in-uptrend pattern):

```
| Ticker | Price  | 1mo   | 6mo   | 1yr   | 5yr   | Z-Score | Trend Pattern          | 5yr CAGR | Recovery |
|--------|--------|-------|-------|-------|-------|---------|------------------------|----------|----------|
| KD     | $24.50 | -55%  | -48%  | -52%  | -30%  | -4.2    | Accelerating decline   | -5.1%    | Low      |
| NOW    | $106   | -12%  | -28%  | -33%  | +180% | -2.8    | Pullback in uptrend    | +22.8%   | High     |
| MAT    | $16.43 | -22%  | -15%  | -18%  | +5%   | -3.1    | Sustained decline      | +1.0%    | Medium   |
```

This table is the triage tool. It doesn't make decisions — it gives you the context to quickly prioritize which 5-10 stocks deserve the full P/E analysis.

---

## Step 2: P/E Analysis (Valuation)

For stocks that survive price context triage, run the full valuation analysis:

- **Script**: `valuation.py` (existing, already combines price + earnings)
- **Key Metrics**: Trailing P/E, P/E vs. 5-year average, Price-EPS correlation, EPS trend
- **Output**: Per-ticker valuation report + aggregated Daily_Screening report

The existing valuation script already does this well. No changes needed to the P/E step — the improvement is all in the price context step that filters *before* we get here.

---

## Wrapper Script Design

**Location**: `scripts/screen.py` (or similar)

**What it does**: No AI. Just a normal Python script that fetches price data, calculates the metrics above, and outputs the price context table.

### How it works:

```
1. INPUT: List of tickers (from CLI args, or reads SESSION_NOTES.md, or a tickers file)
   Example: python screen.py NOW CRM ADBE KD MAT
   Example: python screen.py --category losers  (reads from SESSION_NOTES)

2. FETCH: For each ticker, pull monthly price history (5 years)
   - Source: FMP API (or AlphaVantage as fallback)
   - This is ONE API call per ticker — monthly adjusted close prices
   - With FMP: 34 tickers = 34 API calls, completes in seconds
   - With AlphaVantage free tier: 25/day limit, so batch over 2 days

3. CALCULATE: For each ticker, compute all price context metrics
   - Returns at 1mo, 6mo, 1yr, 5yr
   - Monthly volatility (std dev of monthly returns)
   - Z-score of recent drop
   - Trend classification (pullback/decline/sustained/etc.)
   - 5yr CAGR
   - Recovery stats (historical drawdown analysis)
   - Price vs. 5yr average
   - All pure math — no AI, no LLM, no external analysis

4. OUTPUT:
   - Summary table to stdout (for quick review)
   - Per-ticker JSON: data/tickers/{TICKER}/raw/{TICKER}_price_context.json
   - Batch summary: data/screening/Price_Context_YYYY-MM-DD.txt
   - Optionally append price context to SESSION_NOTES entries (TBD)
```

### Key design points:

- **No AI in the script itself.** It's pure data fetch + math. The AI analysis happens separately — you feed the formatted output to an LLM for interpretation alongside the SESSION_NOTES context.
- **Reuses existing `prices.py` logic** where possible (same API calls, same data format). The wrapper adds the new metrics (z-score, trend classification, recovery) on top.
- **Batch-first design.** Takes multiple tickers and outputs a comparison table. The whole point is to see stocks side-by-side for triage.
- **Idempotent.** Can re-run daily. Overwrites previous price context files. No state to manage.

---

## Data Source: AlphaVantage vs. FMP

| | AlphaVantage (Current) | FMP (Proposed) |
|---|---|---|
| **Free tier** | 25 calls/day | 250 calls/day |
| **Paid tier** | $50/mo for 75/min | ~$20/mo for higher limits |
| **Data quality** | Good for US equities | Good, wider coverage |
| **Monthly prices** | TIME_SERIES_MONTHLY_ADJUSTED | /historical-price-full |
| **Earnings** | EARNINGS endpoint | /income-statement, /earnings |
| **Migration effort** | N/A (current) | Moderate — new API format, response parsing |

**Recommendation**: FMP paid tier is the practical path if screening 30+ tickers regularly. At 25 calls/day on AV free tier, screening all 34 Losers takes 2 days just for price data (before earnings). FMP's 250/day free tier could handle the full pipeline in one session.

**Migration scope**: `prices.py` and `earnings.py` would need FMP API adapters. The calculation logic stays the same — only the data fetch layer changes. `valuation.py` and everything downstream is unaffected (they read cached JSON, not APIs).

---

## Workflow

### Daily (5-10 min)
1. Daily Digest runs automatically (existing GitHub Action)
2. Review digest, update SESSION_NOTES with new candidates (session_notes_update prompt)

### Weekly (30-60 min)
1. Run price context on all Losers: `python screen.py --category losers`
2. Review price context table → pick 5-10 for P/E analysis
3. Run valuation on shortlist: `python valuation.py TICK1 TICK2 TICK3 ...`
4. Feed price context + valuation output to AI for analysis
5. Update Pipeline in SESSION_NOTES based on results

### Monthly
1. Run price context on AI + Other: `python screen.py --category ai other`
2. Promote, demote, or prune stocks based on updated context
3. Clean up SESSION_NOTES screening lists

---

## Implementation Priority

1. **Create `screen.py` wrapper** — price context batch script with new metrics
2. **Migrate to FMP API** — unblock daily batch runs (or pay for AV)
3. **Add `--category` flag** — auto-read tickers from SESSION_NOTES by category
4. **Integrate with session_notes_update prompt** — price context informs Digest analysis

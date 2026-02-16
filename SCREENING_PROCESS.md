# Screening Process

## Overview
A two-step screening funnel designed to filter and prioritize stock candidates from the Losers, AI, and Other categories.

1.  **Price Screening**: Contextualizes price action and volatility.
2.  **Earnings Screening**: Evaluates fundamental trends and valuation alignment.

---

## Step 1: Price Context
**Script**: `scripts/price.py`
**Status**: Completed. Fetches 5 years of daily adjusted prices from FMP.

### Outputs
- **Batch Summary**: `data/screening/Price_YYYY-MM-DD.txt` (Main table + 12-month trend details).
- **Per-Ticker JSON**: `data/tickers/{TICKER}/raw/{TICKER}_price.json`.

### Finalized Screening Questions (to be used in `price_screening.md`):
1. How does the current price compare to its historical levels (both past 12 months and past 5 years)?
2. What is the price trend (both past 12 months and past 5 years)?
3. FOR LOSERS ONLY: How does the current drop compare to the biggest drawdowns in the stock's history (typical, outlier, etc.), and how much room is there for a return to its 1-year average?

---

## Step 2: Earnings & Valuation
**Script**: `scripts/earnings.py`
**Status**: Completed. Combines FMP earnings history with local price context.

### Outputs
- **Batch Summary**: `data/screening/Earnings_YYYY-MM-DD.txt` (Comparison table + detailed TTM/Surprise history).
- **Per-Ticker JSON**: `data/tickers/{TICKER}/raw/{TICKER}_earnings.json`.

### Finalized Screening Questions (to be used in `earnings_screening.md`):
1. How does the current P/E ratio compare to its historical levels (both past 12 months and past 5 years)?
2. What has been the trend in EPS (both past 12 months and past 5 years)?
3. What is the correlation between price and earnings (both recent range and historical levels)?
4. How do the upcoming estimates compare to the company’s past performance and its recent track record of surprises?

---

## Next Steps
- [ ] Create `guidance/prompts/price_screening.md` using the finalized questions.
- [ ] Create `guidance/prompts/earnings_screening.md` using the finalized questions.

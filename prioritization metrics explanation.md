# Prioritization Metrics Explanation

Reference spec for the growth-oriented stock screen: what each column is, which FMP
endpoint feeds it, the exact formula, and brief rationale. Intended for a system/agent
that needs to fetch and reproduce the screen correctly.

---

## Purpose

Rank companies on **sales-anchored growth, quality, and value**, with separate
**cyclicality and timing context flags**. Built to catch high-growth names without
being fooled by low-margin "cheapness" or peak-cycle earnings.

---

## Data source & global conventions

- **API:** FMP **stable** base — `https://financialmodelingprep.com/stable`. Key in env var `FMP_API_KEY`.
  The `v3` API returns 403 on this key; use `stable` only.
- **Price:** always use `historical-price-eod/dividend-adjusted` → latest `adjClose`.
  Do **not** use `profile.price` for returns (it can be stale/unadjusted).
- **Market cap:** `adjClose × sharesOutstanding`, where `sharesOutstanding = profile.marketCap ÷ profile.price`.
  This share count is ADR-consistent (correct for TSM/ASML), and pairing it with the live `adjClose`
  avoids the stale profile price.
- **Currency:** statements report in local currency (`reportedCurrency`). Convert EUR→USD (`× EURUSD`)
  and TWD→USD (`÷ USDTWD`) using `quote?symbol=EURUSD` / `USDTWD`. Prices are already USD (US listings / ADRs).
  Ratios are currency-neutral, but convert absolute values before combining USD market cap with local financials.
- **TTM** = sum of the last 4 reported quarters. All levels and valuation multiples use TTM.
- **Multiples use market-cap ÷ total** (never per-share) — split-, currency-, and ADR-proof.
- Each company is measured on **its own latest fiscal year / latest reported quarter**.

---

## Endpoints used (per ticker)

| Endpoint | Params | Fields used |
|---|---|---|
| `profile` | `symbol` | `marketCap`, `price`, `ipoDate`, `sector`, `industry`, `description` |
| `historical-price-eod/dividend-adjusted` | `symbol` | `date`, `adjClose` (latest + ~90 days prior) |
| `income-statement` | `symbol&period=quarter&limit=8` | `revenue`, `grossProfit`, `netIncome`, `reportedCurrency` |
| `income-statement` | `symbol&period=annual&limit=8` | `revenue`, `netIncome` (7-year flags) |
| `cash-flow-statement` | `symbol&period=quarter&limit=4` | `operatingCashFlow`, `capitalExpenditure` |
| `balance-sheet-statement` | `symbol&period=quarter&limit=1` | `totalDebt`, `cashAndCashEquivalents` |
| `quote` | `symbol=EURUSD` / `USDTWD` | `price` (FX) |

---

## Columns

Legend: **TTM0** = latest 4 quarters, **TTM-1** = the 4 quarters ending one year earlier;
**Q0** = latest quarter, **Q-4** = same quarter one year ago; **FY** = fiscal year (annual).

| # | Column | Endpoint(s) | Formula | Description / rationale |
|---|---|---|---|---|
| 1 | Ticker / Company / Industry / Description | `profile` | — | Identity + business context. Industry allows scoring/filtering within peer groups. (Sector also available; included in the triage pass.) |
| 1b | Market Cap ($B) | `profile` + EOD price | `adjClose × sharesOutstanding` (full run); `profile.marketCap` (triage) | Size reference / filter. Not scored. |
| 2 | Sales growth: TTM vs prior-year TTM (%) | income (quarter) | TTM0 revenue / TTM-1 revenue − 1 | Structural growth rate, smoothed (no seasonality, not a one-quarter blip). **Scored.** |
| 3 | Sales growth: latest Q vs year-ago Q (%) | income (quarter) | Q0 revenue / Q-4 revenue − 1 | Current momentum / inflection detector. **Scored.** |
| 4 | Gross profit / Sales (%) | income (quarter) | TTM grossProfit / TTM revenue | Unit economics — can the growth ever become profit. **Scored.** |
| 5 | FCF / Sales (%) | cash-flow (quarter) + income (quarter) | (TTM operatingCashFlow − TTM \|capitalExpenditure\|) / TTM revenue | Cash generation & quality; catches capex-heavy names whose earnings don't convert to cash. **Scored.** |
| 6 | EV / Sales (x) | profile + balance + income | (marketCap + totalDebt − cashAndCashEquivalents) / TTM revenue | Valuation, sales-anchored so it still works when a company is unprofitable. **Scored.** |
| 7 | Price vs. 3 months ago (%) | EOD price | adjClose(latest) / adjClose(first close ≥90 days earlier) − 1 | Timing / momentum. **Context flag — not scored.** |
| 8 | Years since IPO (yrs) | `profile.ipoDate` | (today − ipoDate) / 365.25 | Upside runway / newness / risk. **Context flag — not scored.** |
| 9 | Worst annual sales growth, last 7y (%) | income (annual) | min over last 7 FY of (revenue[FY] / revenue[FY-1] − 1) | Revenue durability: does the top line ever crash? Positive worst-year = recurring/durable demand; deeply negative = cyclical/transactional. **Context flag — not scored.** |
| 10 | Worst net profit / Sales, last 7y (%) | income (annual) | min over last 7 FY of (netIncome[FY] / revenue[FY]) | Cyclicality tell: does it lose money at the cycle bottom (commodity, no moat) or stay profitable (structural pricing power)? Net line is used because it goes negative at troughs; gross rarely does. **Context flag — not scored.** |

---

## Scoring

- **Five scored metrics:** columns 2, 3, 4, 5, 6.
- Convert each to a **percentile 0–100 across the universe** (higher = better).
  EV/Sales is **inverted** (cheaper = higher score).
- **Combine the two sales windows** (cols 2 & 3) into one **Growth** factor = average of their percentiles.
  This prevents growth from being silently double-weighted. Result: 4 factors —
  Growth, Gross profit/Sales, FCF/Sales, EV/Sales.
- **Two composite scores (both reported):**
  - **Equal:** 25% each of the 4 factors.
  - **Growth-weighted:** Growth 40%, other three 20% each.
- Higher composite = better. Keep both: the gap shows *why* a name ranks
  (growth-driven vs. quality/value-driven).

---

## Context flags (not scored)

Columns 7–10. These are judgment overlays, deliberately kept out of the score:

- **Price vs. 3 months ago** and **Years since IPO** are timing/risk context, not business quality.
- **Cyclicality flags (9 & 10)** use a **7-year annual lookback** — long enough to contain a full
  down-cycle (a 3-year window can sit entirely in an up-leg and miss the trough).
- Blank the two 7-year flags when **years since IPO < 7** (insufficient real history —
  note pre-IPO S-1 years may exist in the feed but contain no genuine down-cycle).

---

## Data-quality rules

- Use dividend-adjusted EOD close for price; never `profile.price` for returns.
- **Sanity guardrail (important at scale):** the 4 quarters should sum to ≈ the annual figure,
  and no single quarter should exceed its own full year. If violated, the quarterly feed is
  likely cumulative/restated (observed on some tickers) and the TTM-based metrics are unreliable
  for that name — flag rather than trust.
- **Negative ≠ missing.** FCF/Sales, margins, and growth can be legitimately negative — those are
  real low scores, not NM. Only leave a cell blank when the underlying data genuinely does not exist.

---

## Rationale summary (why this set)

- **Everything anchored to sales** so metrics are comparable across different business models.
- **EV multiples over price multiples:** they rank companies near-identically (0.97–1.00 correlation);
  EV is preferred because it includes debt. Price multiples were dropped as redundant.
- **Gross profit/Sales + FCF/Sales together defuse the EV/Sales trap:** a low-margin business looks
  "cheap" on EV/Sales but isn't — pairing it with margin and cash exposes that (e.g., value traps
  score low on FCF/Sales).
- **Worst-margin / worst-sales-growth flags catch "cheap because at cycle peak"** — e.g., a memory
  company shows the lowest multiples exactly when earnings are most inflated; the trough flags reveal it.

---

## Running the script (`Scripts/prioritization metrics.py`)

Implements this spec. Per-ticker `stable` calls only (no bulk). `FMP_API_KEY` env var required.

**Arguments**
- **`<TICKERS|@file>` (required, no default):** either a comma-separated list (`NVDA,TSM,MU`)
  or `@path` to a file (tickers one-per-line or comma-separated). The screen is always run on a
  supplied batch.
- **`[out.csv]` (optional):** output path. Defaults: `prioritization metrics.csv` (full run) or
  `prioritization triage.csv` (`--profile-only`).
- **`--profile-only` (optional flag):** triage pass.

**Two modes**
- **Full run (default):** ~6 calls/ticker (profile, EOD price, income quarter+annual, cashflow
  quarter, balance quarter). Outputs all columns above + both scores. Scores are **percentiles
  within the batch supplied** — a ticker's rank depends on what else is in the run.
- **`--profile-only` (triage):** **1 call/ticker** (profile only). Outputs Ticker, Company,
  Market Cap, Sector, Industry, Description — no metrics or scores. Use it to classify/narrow a
  large universe, then feed the survivors back into a full run.

**Behavior at scale**
- **Rate limiting:** self-throttled to **≤290 call-starts per rolling 60s** (margin under the
  300/min plan), enforced across all calls including retries.
- **Failure handling:** each call retries 4× with backoff (1/2/4/8s); a ticker that still fails is
  skipped and logged, so a large batch completes.
- **Progress** printed as it runs; failed tickers summarized at the end.

**Rough runtimes** (at ~290 calls/min)
- Triage (`--profile-only`, 1 call/ticker): ~290 tickers/min → **~10 min for 3,000**.
- Full run (~6 calls/ticker): ~48 tickers/min → **~60 min for 3,000**.

**Data note on the 5-year price cap:** the plan caps *daily price history* at 5 years — this only
feeds the 3-month momentum column (needs ~3 months), so it does not affect the 7-year trough flags,
which come from *annual statements* (8 years available).

**Not yet implemented (future robustness for very large runs):** checkpoint/resume (a total crash
loses in-progress fetches) and the automated data-sanity guardrail described above.

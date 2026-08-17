# Stock Scripts Documentation

Seven data-fetch scripts for single-ticker stock analysis, plus one shared helper module.
Each script fetches from public APIs and writes Markdown summaries (for reading) and raw
JSON/HTML (for reference or grep).

## Environment

- **API keys (env vars):** `FMP_API_KEY` (Financial Modeling Prep), `ALPHAVANTAGE_API_KEY`
  (Alpha Vantage), `PERIGON_API_KEY` (Perigon). SEC EDGAR needs no key (a User-Agent header only).
- **FMP base URL:** `https://financialmodelingprep.com/stable`. Every FMP call also takes `&apikey=$FMP_API_KEY`.
- `shared_utils.py` must sit in the same folder as the scripts (all imports are flat).

## Output layout

All output goes under a `Stock Data/` folder created in the working directory:

- `Stock Data/{TICKER}/` — Markdown summaries and full-text files.
- `Stock Data/{TICKER}/raw/` — raw JSON and HTML. Peer raw files nest here under the TARGET
  ticker, prefixed by the peer ticker (e.g. `Stock Data/AAPL/raw/MSFT_inc_a.json`).

## Run order

`profile.py` runs first (it produces the peer candidate list and the profile JSON that
`numbers.py`, `management.py`, and `sec_filings.py` read for peers/ipoDate/CIK). After picking a
peer manually, run `numbers.py --peers`. The rest can run in any order.

---

## profile.py

**Run:** `python profile.py TICKER`

**Endpoints / data sources (FMP):**
- `GET /profile?symbol={TICKER}`
- `GET /stock-peers?symbol={TICKER}`

**Output:**
- `Stock Data/{TICKER}/{TICKER}_profile.md` — Snapshot table (exchange + full exchange name,
  sector, industry, country, ADR yes/no, market cap, reporting currency, full-time employees,
  CEO, IPO date + years public, website), full company description, and a Suggested Peers table
  (symbol, company name, market cap) for manual peer selection.
- `Stock Data/{TICKER}/raw/{TICKER}_profile.json` — full FMP profile response (includes `cik`,
  `ipoDate`, `country`, `isAdr`, `marketCap`, `sector`, `industry`, `description`, etc.).
- `Stock Data/{TICKER}/raw/{TICKER}_peers.json` — raw FMP stock-peers list (reference only; peers
  are chosen manually, not auto-applied).

---

## numbers.py

**Run:** `python numbers.py TICKER --peers PEER [PEER2]`  (at least one peer is required; max two used)

**Endpoints / data sources (FMP) — every one is called for the TARGET and for EACH peer:**
- `GET /income-statement?symbol={T}&period=annual&limit=10`
- `GET /income-statement?symbol={T}&period=quarter&limit=20`
- `GET /balance-sheet-statement?symbol={T}&period=annual&limit=10`
- `GET /balance-sheet-statement?symbol={T}&period=quarter&limit=8`
- `GET /cash-flow-statement?symbol={T}&period=annual&limit=10`
- `GET /cash-flow-statement?symbol={T}&period=quarter&limit=8`
- `GET /revenue-product-segmentation?symbol={T}`  (annual FY segments)
- `GET /earnings?symbol={T}&limit=8`  (epsActual → adjusted P/E)
- `GET /quote?symbol={T}`  (current price + market cap)
- `GET /historical-price-eod/dividend-adjusted?symbol={T}&from={today-760d}`  (→ 24 monthly closes)

**Output:**
- `Stock Data/{TICKER}/{TICKER}_numbers.md` — one report, four sections plus peer comparison:
  1. **Sales** — TTM sales and TTM YoY growth; Annual acceleration table (3 years, TTM
     4-quarter-sum basis: YoY growth + pp acceleration); Quarterly acceleration table (4 quarters,
     single-quarter YoY: YoY growth + pp acceleration); Product segmentation table (segment,
     latest-FY revenue, % of total, prior-FY revenue, YoY).
  2. **Key Metrics** — Gross Margin, FCF/Sales, ROIC, Debt/Sales, each with the 5-year trough and
     Δ-vs-trough (troughs computed for Gross Margin and FCF/Sales).
  3. **Valuation** — EV/Sales, GAAP P/E, Adjusted P/E; current price, 24-month trough, Δ-vs-trough;
     24-row monthly close table.
  4. **Detailed Financials** — Annual wide table (last 5 fiscal years with Δ%, TTM, 5yr avg, 5yr
     CAGR, CV) and Recent Quarterly table. Rows: Revenue, Gross Margin, Operating Margin, R&D,
     R&D/Sales, S&M or SG&A, S&M/Sales, Op Cash Flow, Free Cash Flow, FCF/Sales, OCF/Net Income,
     SBC, SBC/Sales, Working Capital, Operating Leverage, CapEx, D&A, CapEx/D&A, D&A/Sales, Total
     Debt, Cash, Net Debt, Debt/Sales, Debt/Assets, Debt/OCF, Interest Coverage, Goodwill/Sales, ROIC.
  - **Peer Comparison** table (target vs peers: TTM Sales, TTM Sales Growth, Gross Margin,
    FCF/Sales, R&D/Sales, ROIC, Debt/Sales, EV/Sales, GAAP P/E, Adjusted P/E), followed by each
    peer's full Annual + Quarterly detailed tables.
- `Stock Data/{TICKER}/raw/{TICKER}_inc_a.json`, `_inc_q.json`, `_bal_a.json`, `_bal_q.json`,
  `_cf_a.json`, `_cf_q.json`, `_seg.json`, `_earn.json`, `_quote.json`, `_price.json` — one raw
  file per endpoint above. Peer raw files use the same suffixes prefixed by the peer ticker,
  nested in the target's `raw/` folder.

Notes: S&M vs SG&A is chosen once per ticker (whichever the company reports consistently) and
applied uniformly. Debt metrics use gross debt; Cash and Net Debt are shown for context.

---

## analyst.py

**Run:** `python analyst.py TICKER [TICKER2 ...]`

**Endpoints / data sources (FMP):**
- `GET /grades-consensus?symbol={TICKER}`  (current buy/hold/sell distribution)
- `GET /grades?symbol={TICKER}&limit=100`  (grade actions; filtered to the last 90 days)

**Output:**
- `Stock Data/{TICKER}/{TICKER}_analyst.md` — Consensus Distribution table (Strong Buy, Buy, Hold,
  Sell, Strong Sell counts and percentages; total analysts; Sell % = Sell + Strong Sell; consensus
  label); Grade Movement — Last 90 Days (summary counts of upgrades / downgrades / initiations /
  maintained, then a table of the actual upgrades, downgrades, and initiations with date, firm,
  action, previous → new grade). Maintained ratings are counted but not listed.
- `Stock Data/{TICKER}/raw/{TICKER}_analyst.json` — `{consensus, grades_recent, grades_all}`.

---

## news.py

**Run:** `python news.py TICKER [--months N]`  (default `--months 3`)

Both sources are fetched per 30-day window across the lookback (N windows).

**Endpoints / data sources:**
- **Perigon** — `GET https://api.goperigon.com/v1/stories/all`, called TWICE per window and merged
  (deduped by story id): once with `sortBy=relevance&size=12` (significant, on-topic stories) and
  once with `sortBy=createdAt&size=8` (freshest). Params: `apiKey`, `companySymbol={TICKER}`,
  `sortBy`, `size`, `showReprints=false`, `from`, `to`.
- **FMP** — `GET /news/stock` once per window. Params: `symbols={TICKER}`, `from`, `to`,
  `limit=16`, `apikey`.

**Output:**
- `Stock Data/{TICKER}/{TICKER}_news.md` — Summary (Perigon story count + aggregated article count,
  FMP article count + distinct sources, total); Coverage by Window table (rolling 30-day windows ×
  Perigon/FMP counts); Perigon Stories (each: date, cluster article count, summary, up to 3 key
  points); FMP Articles (each: date, source, URL, article text).
- `Stock Data/{TICKER}/raw/{TICKER}_news_perigon.json` — `{date_range, stories}`.
- `Stock Data/{TICKER}/raw/{TICKER}_news_fmp.json` — `{date_range, articles}`.

---

## management.py

**Run:** `python management.py TICKER [TICKER2 ...]`

**Endpoints / data sources (FMP):**
- `GET /key-executives?symbol={TICKER}`
- `GET /insider-trading/search?symbol={TICKER}&page={0..5}&limit=100`  (paginated up to 6 pages,
  stopping once transactions pass the 6-month cutoff)
- Reads `Stock Data/{TICKER}/raw/{TICKER}_profile.json` for `ipoDate`; if absent, falls back to
  `GET /profile?symbol={TICKER}`.

**Output:**
- `Stock Data/{TICKER}/{TICKER}_management.md` — Track Record (IPO date and years public); Key
  Executives table (name, title, pay, year born, gender; active officers, sorted by pay); Insider
  Trading — Open-Market, Last 6 Months: a takeaway line ($ bought across N buys vs $ sold across M
  sells, net $) and a transaction table (date, insider, role, transaction type, shares, price,
  value). Only open-market purchases (P) and sales (S) are included; option exercises, grants,
  tax-withholding, and gifts are excluded.
- `Stock Data/{TICKER}/raw/{TICKER}_management.json` — `{ipoDate, executives, insider_raw,
  insider_open_market, insider_totals}`.

---

## earnings_calls.py

**Run:** `python earnings_calls.py TICKER`

**Endpoints / data sources (Alpha Vantage; base `https://www.alphavantage.co/query`):**
- `?function=OVERVIEW&symbol={TICKER}`  (fiscal-year-end month, for quarter labeling)
- `?function=EARNINGS&symbol={TICKER}`  (quarter list + `reportedDate`; latest 2 quarters used)
- `?function=EARNINGS_CALL_TRANSCRIPT&symbol={TICKER}&quarter={YYYYQN}`  (one call per quarter, 2 total)

**Output:**
- `Stock Data/{TICKER}/{TICKER}_earnings_{QUARTER}.md` — one file per quarter (latest 2, e.g.
  `{TICKER}_earnings_2026Q3.md`), each containing a Prepared Remarks section and a Q&A section.
  Every turn is labeled `**Speaker** (Title)`; in Q&A, Analyst-titled turns are the questions and
  management turns are the answers.
- `Stock Data/{TICKER}/{TICKER}_earnings_report.md` — summary table: quarter, call/report date
  (EARNINGS `reportedDate`), transcript entry count, analyst-question count.
- `Stock Data/{TICKER}/raw/{TICKER}_ecall_{QUARTER}.json` — raw transcript JSON per quarter.

Note: Alpha Vantage free tier is rate-limited (≈25 requests/day, 1/sec); the script waits between
calls.

---

## sec_filings.py

**Run:** `python sec_filings.py TICKER [TICKER2 ...]`

**Data source: SEC EDGAR only** (User-Agent header required, no API key).

**Endpoints:**
- `GET https://www.sec.gov/files/company_tickers.json`  (CIK lookup — used only if
  `Stock Data/{TICKER}/raw/{TICKER}_profile.json` is absent; otherwise CIK is read from there)
- `GET https://data.sec.gov/submissions/CIK{cik10}.json`  (filing enumeration: form types, filing
  dates, accession numbers, primary document names, 8-K item codes, document descriptions)
- `GET https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{document}`  (full filing HTML —
  fetched for the annual filing and, for US filers, the latest 10-Q)

**Regime detection:** the most recent annual form the company files determines the path —
`10-K` → US (annual 10-K + latest 10-Q + 8-K list), `20-F` → foreign (annual 20-F + 6-K list, no
10-Q), `40-F` → Canadian (annual 40-F + 6-K list, no 10-Q).

**Output:**
- Full annual filing text — `Stock Data/{TICKER}/{TICKER}_10k.txt` **or** `{TICKER}_20f.txt` **or**
  `{TICKER}_40f.txt` (whichever the company files).
- `Stock Data/{TICKER}/{TICKER}_10q.txt` — full latest 10-Q text (US filers only).
- `Stock Data/{TICKER}/{TICKER}_filings_report.md` — Regime line; Filings Fetched table (form,
  filing date, full-document word count, Fetch OK? based on a word-count floor); Current Reports —
  Last 6 Months: for US, an 8-K table (date, item codes, item-code description, Recommend pull? —
  ✓ for high-signal items 1.01/1.02/2.01/4.01/4.02/5.01/5.02; 2.02 earnings suppressed); for
  foreign/Canadian, a 6-K table (date, filename, inferred type, Recommend pull? — routine
  monthly-revenue/dividend/board/AGM suppressed, financials and unclassified named events flagged);
  Notes.
- `Stock Data/{TICKER}/raw/{TICKER}_10k.htm` (or `_20f.htm` / `_40f.htm`) and
  `Stock Data/{TICKER}/raw/{TICKER}_10q.htm` — raw filing HTML.

Notes: filings are fetched whole (no section extraction); the MD&A and footnote passages are
obtained by grepping the full `.txt` files during analysis, not by this script. 8-K/6-K bodies are
not auto-pulled — the report flags which to fetch on demand. 6-K types are inferred from
(often generic) filenames, so classification errs toward flagging anything non-routine for review.

---

## shared_utils.py

Imported by all scripts. Provides: output-path helpers (`get_writeup_directory`,
`get_data_directory` → `Stock Data/{TICKER}[/raw]`), `ensure_directory_exists`, `save_json`,
`load_json`, `fetch_alpha_vantage`, `make_request_with_retry`, `get_date_range_months_back`,
`get_company_name`, `fmt_market_cap`, `years_since`. Not run directly.

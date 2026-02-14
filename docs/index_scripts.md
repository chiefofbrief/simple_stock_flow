# Scripts Index

Comprehensive catalog of all Python scripts: orchestrators, data collectors, analyzers, and utilities.

## 1. Master Scripts
Orchestration scripts that wrap individual modules for specific workflows.

| File | Purpose |
| :--- | :--- |
| `scripts/peters_digest.py` | Generates Peter's Market Digest (Daily/Weekly). Supports `--daily`, `--weekly`, and individual module flags. Prioritizes Movers, Barron's, Reddit, AI News, Intrigue. |
| `scripts/sentiment.py` | Aggregates sentiment analysis from news and social media sources. Outputs to `data/tickers/{TICKER}/{TICKER}_sentiment.md`. Supports `--all` or individual source flags with timeline overrides. |
| `scripts/price.py` | Screening Step 1: Batch price context for triage. Fetches 5yr dividend-adjusted daily prices from FMP, computes metrics (vs1Y–vs5Y, CV, z-score, 52w position, max drawdown, CAGR). Supports `--category losers/ai/other`, `--all`, or positional tickers. Outputs summary table + per-ticker JSON. |
| `scripts/earnings.py` | Screening Step 2: Earnings + P/E for survivors of price triage. *Not yet implemented.* |
| `scripts/financial_statements.py` | Orchestrates financial statements analysis: fetches raw data, calculates seeds and metrics, generates comparison tables. Outputs to `data/tickers/{TICKER}/{TICKER}_statements.md`. Supports optional `--compare PEER1 PEER2` for peer comparison. |

## 2. Market Scripts (`scripts/market/`)
Broad market scans used for discovery and trend identification.

| File | Data Source | Purpose |
| :--- | :--- | :--- |
| `movers.py` | FMP / AlphaVantage | Identifies biggest losers and most active stocks. |
| `macro.py` | FMP / AlphaVantage | Health check of indices, treasury yields, and economic indicators (CPI, etc). |
| `barrons.py` | Perigon API | Fetches latest articles from Barron's. |
| `wsj.py` | WSJ RSS | Fetches latest market news from the Wall Street Journal. |
| `intrigue.py` | Web Scraping | Fetches the latest "International Intrigue" newsletter briefing. |
| `reddit.py` | SociaVault API | Top posts from r/ValueInvesting, r/stocks, and r/options. |

## 3. Ticker Scripts (`scripts/ticker/`)
Deep-dive analysis tools for individual stocks. Outputs are saved to `data/tickers/{TICKER}/`.

### Fundamentals & Valuation
| File | Purpose | Key Outputs |
| :--- | :--- | :--- |
| `fetch_financials.py` | Fetches raw financial statements (income, balance, cashflow). | `_financial_raw.json` |
| `calc_seeds.py` | Extracts 8 projection seeds (Revenue, COGS%, SG&A%, R&D%, D&A, CapEx, Debt, WC) from raw data. | `_seeds.json` |
| `calc_metrics.py` | Calculates 30+ metrics (13 priority + 17 secondary) for undervaluation and risk analysis. | `_metrics.json` |
| `prices.py` | **Archived** → `scripts/archive/prices_alphavantage.py`. Replaced by `scripts/price.py`. | `_prices.json`, `_prices.txt` |
| `earnings.py` | **Archived** → `scripts/archive/earnings_alphavantage.py`. Replaced by `scripts/earnings.py` (not yet implemented). | `_earnings.json`, `_earnings.txt` |
| `compare_financials.py` | Standalone peer comparison tool (also integrated into `financial_statements.py` master script). | Markdown table |
| `sec_filings.py` | Fetches latest 10-K and 10-Q from SEC EDGAR, extracts MD&A and Notes sections, generates consolidated markdown. | `_10k_mda.txt`, `_10k_notes.txt`, `_10q_mda.txt`, `_10q_notes.txt`, `_filings_metadata.json`, `_notes_mda.md` |

**Note:** `valuation.py` has been archived to `scripts/archive/valuation_alphavantage.py`. Replaced by the two-step screening process (`scripts/price.py` + `scripts/earnings.py`).

### Sentiment & Social
Individual scripts save raw JSON data to `data/tickers/{TICKER}/`. Use with `--markdown` flag for master script aggregation. Timeline defaults: news (3 months), reddit (30 days), social media (this-month).

#### News Scripts (Modular)
| File | Data Source | Purpose | Output | Default Lookback |
| :--- | :--- | :--- | :--- | :--- |
| `news.py` | Wrapper | Orchestrates Perigon + AlphaVantage news collection. Calls individual API scripts and generates combined markdown. **Production script.** | `_news_perigon.json`, `_news_alphavantage.json` | 3 months |
| `news_perigon.py` | Perigon API | Standalone Perigon news fetcher. Can run independently or via wrapper. | `_news_perigon.json` | 3 months |
| `news_alphavantage.py` | AlphaVantage API | Standalone AlphaVantage news fetcher. Can run independently or via wrapper. | `_news_alphavantage.json` | 3 months |

**Note:** Modular architecture enables running individual news sources independently. Production `news.py` is now the wrapper that orchestrates both APIs.

#### Social Media Scripts
| File | Data Source | Purpose | Default Lookback |
| :--- | :--- | :--- | :--- |
| `reddit.py` | SociaVault API | Reddit discussion from r/stocks, r/ValueInvesting, r/options. Configurable with `--days`. | 30 days |
| `tiktok.py` | SociaVault API | TikTok trend analysis. Configurable with `--time-period`. | this-month |
| `youtube.py` | SociaVault API | YouTube video metadata and analysis. Configurable with `--time-period`. | this_month |

## 4. Shared Infrastructure
| File | Purpose |
| :--- | :--- |
| `scripts/shared_utils.py` | Shared logic for API retries, directory management, and date utilities. |
| `requirements.txt` | Project dependencies. |
| `docs/COMMANDS.md` | Runbook for all valid CLI commands. |

## 5. Archived Scripts (`scripts/archive/`)
Previous AlphaVantage-based scripts, preserved in case of provider switch-back.

| File | Replaced By |
| :--- | :--- |
| `prices_alphavantage.py` | `scripts/price.py` (FMP) |
| `earnings_alphavantage.py` | `scripts/earnings.py` (FMP, not yet implemented) |
| `valuation_alphavantage.py` | `scripts/earnings.py` (FMP, not yet implemented) |

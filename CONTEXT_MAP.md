# Project Context Map: LLM Stock Analysis

This document serves as an index for the Gemini CLI to understand the repository structure and the purpose of each script.

## 1. Master Scripts
Orchestration scripts that wrap individual modules for specific workflows.

| File | Purpose |
| :--- | :--- |
| `scripts/discovery.py` | Generates Market Discovery digests (Daily/Weekly). Supports `--daily`, `--weekly`, and individual module flags. |
| `scripts/sentiment.py` | Aggregates sentiment analysis from news and social media sources. Outputs to `data/analysis/{TICKER}/{TICKER}_sentiment.md`. Supports `--all` or individual source flags with timeline overrides. |
| `scripts/financial_statements.py` | Orchestrates financial statements analysis: fetches raw data, calculates seeds and metrics, generates comparison tables. Outputs to `data/analysis/{TICKER}/{TICKER}_statements.md`. Supports optional `--compare PEER1 PEER2` for peer comparison. |

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
Deep-dive analysis tools for individual stocks. Outputs are saved to `data/stocks/{TICKER}/`.

### Fundamentals & Valuation
| File | Purpose | Key Outputs |
| :--- | :--- | :--- |
| `fetch_financials.py` | Fetches raw financial statements (income, balance, cashflow). | `_financial_raw.json` |
| `calc_seeds.py` | Extracts 8 projection seeds (Revenue, COGS%, SG&A%, R&D%, D&A, CapEx, Debt, WC) from raw data. | `_seeds.json` |
| `calc_metrics.py` | Calculates 30+ metrics (13 priority + 17 secondary) for undervaluation and risk analysis. | `_metrics.json` |
| `prices.py` | Fetches price history; calculates 1-mo/1-yr returns, 5-yr CAGR, and Price vs 5-yr Avg. Supports batch processing. | `_prices.json`, `_prices.txt` |
| `earnings.py` | Fetches EPS history and consensus; calculates "Forward Delta" and "Stability (CV)". Supports batch processing. | `_earnings.json`, `_earnings.txt` |
| `compare_financials.py` | Standalone peer comparison tool (also integrated into `financial_statements.py` master script). | Markdown table |

**Note:** `valuation.py` is located in `scripts/` (master script level) as it's used for preliminary screening.

### Sentiment & Social
Individual scripts save raw JSON data to `data/stocks/{TICKER}/`. Use with `--markdown` flag for master script aggregation. Timeline defaults: news (3 months), reddit (30 days), social media (this-month).

| File | Data Source | Purpose | Default Lookback |
| :--- | :--- | :--- | :--- |
| `news.py` | Perigon / AlphaVantage | Ticker-specific news and sentiment. Configurable with `--months`. | 3 months |
| `reddit.py` | SociaVault API | Reddit discussion from r/stocks, r/ValueInvesting, r/options. Configurable with `--days`. | 30 days |
| `tiktok.py` | SociaVault API | TikTok trend analysis. Configurable with `--time-period`. | this-month |
| `youtube.py` | SociaVault API | YouTube video metadata and analysis. Configurable with `--time-period`. | this_month |

## 4. Shared Infrastructure
| File | Purpose |
| :--- | :--- |
| `scripts/shared_utils.py` | Shared logic for API retries, directory management, and date utilities. |
| `setup/requirements.txt` | Project dependencies. |
| `setup/COMMANDS.md` | Runbook for all valid CLI commands. |

# Project Context Map: LLM Stock Analysis

This document serves as an index for the Gemini CLI to understand the repository structure and the purpose of each script.

## 1. Master Scripts
Orchestration scripts that wrap individual modules for specific workflows.

| File | Purpose |
| :--- | :--- |
| `scripts/discovery.py` | Generates Market Discovery digests (Daily/Weekly). Supports `--daily`, `--weekly`, and individual module flags. |

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
Deep-dive analysis tools for individual stocks. Outputs are saved to `data/analysis/{TICKER}/`.

### Fundamentals & Valuation
| File | Purpose | Key Outputs |
| :--- | :--- | :--- |
| `fetch_financials.py` | Fetches raw statements (IS, BS, CF) and Overview. | `_financial_raw.json` |
| `calc_seeds.py` | Extracts 8 projection seeds (Revenue, COGS%, etc) from raw data. | `_seeds.json` |
| `calc_metrics.py` | Calculates 30+ metrics for undervaluation and risk. | `_metrics.json` |
| `prices.py` | Fetches price history; calculates 1-mo/1-yr returns, 5-yr CAGR, and Price vs 5-yr Avg. Supports batch processing. | `_prices.json`, `_prices.txt` |
| `earnings.py` | Fetches EPS history and consensus; calculates "Forward Delta" and "Stability (CV)". Supports batch processing. | `_earnings.json`, `_earnings.txt` |
| `valuation.py` | Primary Screener. Combines Price/Earnings for P/E vs 5-yr Avg and Price-EPS correlation. Supports batch processing. | `_valuation.json`, `_valuation.txt` |
| `compare_financials.py` | Compares fundamental metrics across multiple tickers. | Markdown table |

### Sentiment & Social
| File | Data Source | Purpose |
| :--- | :--- | :--- |
| `news.py` | Perigon / AlphaVantage | Aggregates and formats ticker-specific news and sentiment. |
| `reddit.py` | SociaVault API | Ticker-specific Reddit discussion analysis. |
| `tiktok.py` | SociaVault API | Ticker-specific TikTok trend analysis. |
| `youtube.py` | SociaVault API | Ticker-specific YouTube video metadata and analysis. |

## 4. Shared Infrastructure
| File | Purpose |
| :--- | :--- |
| `scripts/shared_utils.py` | Shared logic for API retries, directory management, and date utilities. |
| `setup/requirements.txt` | Project dependencies. |
| `setup/COMMANDS.md` | Runbook for all valid CLI commands. |

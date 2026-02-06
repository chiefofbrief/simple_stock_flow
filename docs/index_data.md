# Data Index

Script outputs and analysis artifacts. Directory structure and file naming conventions.

## Directory Structure

```
data/
├── discovery/               # Market discovery digests
├── screening/               # Multi-ticker screening outputs
└── analysis/{TICKER}/       # Ticker-specific analysis and raw data
```

---

## Discovery Outputs (`data/discovery/`)

| File Pattern | Source Script | Description |
|--------------|---------------|-------------|
| `Daily_Digest_YYYY-MM-DD.md` | `discovery.py --daily` | Market movers, macro indicators, news headlines (Barron's, WSJ, Intrigue), Reddit posts |
| `Weekly_Digest_YYYY-MM-DD.md` | `discovery.py --weekly` | Same components as daily, with expanded lookback periods |

---

## Screening Outputs (`data/screening/`)

| File Pattern | Source Script | Description |
|--------------|---------------|-------------|
| `Daily_Screening_YYYY-MM-DD.txt` | `valuation.py` | Multi-ticker screening results from daily workflow |

---

## Ticker Raw Data (`data/analysis/{TICKER}/`)

### Fundamentals & Valuation

| File Pattern | Source Script | Format | Description |
|--------------|---------------|--------|-------------|
| `{TICKER}_financial_raw.json` | `fetch_financials.py` | JSON | Raw financial statements: income, balance sheet, cash flow (10 years) |
| `{TICKER}_seeds.json` | `calc_seeds.py` | JSON | 8 projection seeds: Revenue, COGS%, SG&A%, R&D%, D&A, CapEx, Total Debt, Working Capital |
| `{TICKER}_metrics.json` | `calc_metrics.py` | JSON | 30+ metrics: 13 priority (undervaluation + risk), 17 secondary |
| `{TICKER}_prices.json` | `prices.py` | JSON | Price history, returns (1-mo, 1-yr, 5-yr CAGR), price vs 5-yr avg |
| `{TICKER}_prices.txt` | `prices.py` | Text | Human-readable price summary |
| `{TICKER}_earnings.json` | `earnings.py` | JSON | EPS history, consensus estimates, Forward Delta, Stability (CV) |
| `{TICKER}_earnings.txt` | `earnings.py` | Text | Human-readable earnings summary |

### Sentiment & Social

Individual source files (raw JSON). Use `--markdown` flag for formatted intermediate outputs.

| File Pattern | Source Script | Format | Description | Default Lookback |
|--------------|---------------|--------|-------------|------------------|
| `{TICKER}_news_perigon.json` | `news.py` | JSON | Aggregated news stories from Perigon API | 3 months |
| `{TICKER}_news_alphavantage.json` | `news.py` | JSON | Individual articles with sentiment scores from AlphaVantage | 3 months |
| `{TICKER}_reddit.json` | `reddit.py` | JSON | Reddit posts from r/stocks, r/ValueInvesting, r/options | 30 days |
| `{TICKER}_tiktok.json` | `tiktok.py` | JSON | TikTok video metadata and trends | this-month |
| `{TICKER}_youtube.json` | `youtube.py` | JSON | YouTube video metadata | this-month |

---

## Analysis Outputs (`data/analysis/{TICKER}/`)

Master script outputs and LLM analysis documents.

| File Pattern | Source | Format | Description |
|--------------|--------|--------|-------------|
| `{TICKER}_statements.md` | `financial_statements.py` | Markdown | Consolidated financial analysis: seeds, metrics, comparison tables, peer analysis (if `--compare` used) |
| `{TICKER}_sentiment.md` | `sentiment.py` | Markdown | Aggregated sentiment from all sources: news, Reddit, TikTok, YouTube |
| `{TICKER}_tracking.md` | Manual/LLM | Markdown | Investigation items flagged during analysis, cross-referenced across data sources |
| `{TICKER}_ANALYSIS_screening.md` | LLM analysis | Markdown | Screening analysis output (typically not saved, terminal display) |
| `{TICKER}_ANALYSIS_statement.md` | LLM analysis | Markdown | Deep financial statement analysis |
| `{TICKER}_ANALYSIS_news.md` | LLM analysis | Markdown | News coverage analysis |
| `{TICKER}_ANALYSIS_sentiment.md` | LLM analysis | Markdown | Multi-source sentiment analysis |

---

## File Naming Conventions

- **Tickers:** Always uppercase (e.g., `AAPL`, `MSFT`)
- **Dates:** ISO format `YYYY-MM-DD`
- **Suffixes:**
  - `_raw.json` - Unprocessed API responses
  - `.json` - Structured data
  - `.txt` - Human-readable summaries
  - `.md` - Formatted reports and analysis
  - `_ANALYSIS_` - LLM-generated analysis documents

---

## Data Flow

```
Individual Scripts → data/analysis/{TICKER}/   (raw JSON/text)
Master Scripts     → data/analysis/{TICKER}/   (consolidated markdown)
LLM Analysis       → data/analysis/{TICKER}/   (analysis markdown)
Screening Scripts  → data/screening/           (multi-ticker results)
```

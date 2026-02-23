# Data Index

Script outputs and analysis artifacts. Directory structure and file naming conventions.

## Directory Structure

```
data/
├── discovery/               # Market discovery digests
├── screening/               # Multi-ticker screening outputs
└── tickers/{TICKER}/        # Ticker-specific write-ups and raw data
    ├── *.md                 #   Analysis write-ups (top level)
    └── raw/                 #   Raw script outputs (JSON, txt)
```

---

## Discovery Outputs (`data/discovery/`)

| File Pattern | Source Script | Description |
|--------------|---------------|-------------|
| `Daily_Digest_YYYY-MM-DD.md` | `peters_digest.py --daily` | Market movers, macro indicators, news headlines (Barron's, WSJ, Intrigue), Reddit posts |
| `Weekly_Digest_YYYY-MM-DD.md` | `peters_digest.py --weekly` | Same components as daily, with expanded lookback periods |

---

## Screening Outputs (`data/screening/`)

| File Pattern | Source Script | Description |
|--------------|---------------|-------------|
| `Daily_Screening_YYYY-MM-DD.txt` | `valuation.py` | Multi-ticker screening results from daily workflow |

---

## Ticker Raw Data (`data/tickers/{TICKER}/raw/`)

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

### SEC Filings

| File Pattern | Source Script | Format | Description |
|--------------|---------------|--------|-------------|
| `{TICKER}_10k_latest.html` | `sec_filings.py` | HTML | Full 10-K annual report |
| `{TICKER}_10q_latest.html` | `sec_filings.py` | HTML | Full 10-Q quarterly report |
| `{TICKER}_10k_mda.txt` | `sec_filings.py` | Text | MD&A section extracted from 10-K |
| `{TICKER}_10k_notes.txt` | `sec_filings.py` | Text | Notes to Financial Statements from 10-K |
| `{TICKER}_10q_mda.txt` | `sec_filings.py` | Text | MD&A section extracted from 10-Q |
| `{TICKER}_10q_notes.txt` | `sec_filings.py` | Text | Notes to Financial Statements from 10-Q |
| `{TICKER}_filings_metadata.json` | `sec_filings.py` | JSON | Filing dates, accession numbers, section statistics |

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

## Analysis Outputs (`data/tickers/{TICKER}/`)

Master script outputs and LLM analysis documents.

| File Pattern | Source | Format | Description |
|--------------|--------|--------|-------------|
| `{TICKER}_statements.md` | `financial_statements.py` | Markdown | Consolidated financial analysis: seeds, metrics, comparison tables, peer analysis (if `--compare` used) |
| `{TICKER}_sentiment.md` | `sentiment.py` | Markdown | Aggregated sentiment from all sources: news, Reddit, TikTok, YouTube |
| `{TICKER}_notes_mda.md` | `sec_filings.py` | Markdown | Consolidated SEC filing text: MD&A + Notes from 10-K and 10-Q with section summary |
| `{TICKER}_tracking.md` | Manual/LLM | Markdown | Investigation items flagged during analysis, cross-referenced across data sources |

LLM analyses are prepended to their corresponding data files (e.g., statement analysis is prepended to `{TICKER}_statements.md`). Screening analysis is prepended to `data/screening/Daily_Screening_YYYY-MM-DD.txt`.

---

## File Naming Conventions

- **Tickers:** Always uppercase (e.g., `AAPL`, `MSFT`)
- **Dates:** ISO format `YYYY-MM-DD`
- **Suffixes:**
  - `_raw.json` - Unprocessed API responses
  - `.json` - Structured data
  - `.txt` - Human-readable summaries
  - `.md` - Formatted reports and analysis
  - LLM analyses are prepended to their data files (no separate `_ANALYSIS_` files)

---

## Data Flow

```
Individual Scripts → data/tickers/{TICKER}/raw/  (raw JSON/text)
Master Scripts     → data/tickers/{TICKER}/     (consolidated markdown)
LLM Analysis       → data/tickers/{TICKER}/     (analysis markdown)
Screening Scripts  → data/screening/           (multi-ticker results)
```

# Command Reference

Quick reference for running scripts. See `docs/index_scripts.md` for detailed script documentation.

---

## Installation

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install manually
pip install requests tabulate rich python-dateutil beautifulsoup4 html2text lxml curl_cffi
```

**Environment Variables Required:**
- `PERIGON_API_KEY` - Perigon news API
- `ALPHAVANTAGE_API_KEY` - AlphaVantage market data
- `FMP_API_KEY` - Financial Modeling Prep
- `SOCIAVAULT_API_KEY` - SociaVault social media data

---

## Master Scripts

Orchestration scripts that run complete workflows.

### Market Discovery

Generate daily or weekly market digests.

```bash
# Peter's Daily Digest (Movers, Barron's, Reddit, AI News, Intrigue - 1 day lookback)
python scripts/peters_digest.py --daily > "data/discovery/Daily_Digest_$(date +%Y-%m-%d).md"

# Weekly digest (Macro, AI News, Movers, Reddit - 7 day lookback)
python scripts/peters_digest.py --weekly > "data/discovery/Weekly_Digest_$(date +%Y-%m-%d).md"

# Run specific modules only
python scripts/peters_digest.py --barrons --ai-news
python scripts/peters_digest.py --macro
```

### Financial Statements Analysis

Fetch statements, calculate seeds and metrics, generate markdown report.

```bash
# Single ticker - outputs to data/tickers/{TICKER}/{TICKER}_statements.md
python scripts/financial_statements.py AAPL

# With peer comparison (3-ticker tables)
python scripts/financial_statements.py AAPL --compare MSFT GOOGL
```

### Sentiment Analysis

Aggregate news and social media sentiment into single report.

```bash
# All sources with default lookbacks (news: 3mo, reddit: 30d, social: this-month)
python scripts/sentiment.py AAPL --all

# Specific sources only
python scripts/sentiment.py AAPL --news --reddit

# Override timelines
python scripts/sentiment.py AAPL --all --news-months 1 --reddit-days 7
```

### Screening — Price Context (Step 1)

Batch price context for screening triage. See `SCREENING_PROCESS.md` for full process.

```bash
# Specific tickers
python scripts/price.py NOW CRM ADBE KD MAT

# By category (reads tickers from SESSION_NOTES.md)
python scripts/price.py --category losers
python scripts/price.py --category ai other

# All screening candidates
python scripts/price.py --all
```

### Screening — Earnings (Step 2)

Earnings + valuation for survivors of price triage. *Not yet implemented — pending FMP earnings endpoints.*

```bash
# Screen survivors from Step 1
python scripts/earnings.py NOW CRM ADBE
```

---

## Individual Scripts

Individual scripts can be run independently. See `docs/index_scripts.md` for complete documentation.

### Common Individual Script Usage

```bash
# Prices (archived — use scripts/price.py instead)
# python scripts/ticker/prices.py AAPL MSFT

# Earnings (archived — use scripts/earnings.py instead, when implemented)
# python scripts/ticker/earnings.py AAPL MSFT

# News - modular (Perigon + AlphaVantage wrapper)
python scripts/ticker/news.py AAPL --months 3

# AI Infrastructure News (Perigon Stories)
python scripts/market/ai_news.py                 # Default: 1 day, 30 stories
python scripts/market/ai_news.py --markdown      # Raw markdown output
python scripts/market/ai_news.py --days 7        # Past 7 days
python scripts/market/ai_news.py --count 30      # Explicitly set cap (default is 30)

# News - individual sources
python scripts/ticker/news_perigon.py AAPL --months 3
python scripts/ticker/news_alphavantage.py AAPL --months 3

# Social media
python scripts/ticker/reddit.py --ticker AAPL --days 30
python scripts/ticker/tiktok.py AAPL --time-period this-month
python scripts/ticker/youtube.py AAPL --time-period this_month

# Financial statement components
python scripts/ticker/fetch_financials.py AAPL
python scripts/ticker/calc_seeds.py AAPL
python scripts/ticker/calc_metrics.py AAPL
python scripts/ticker/compare_financials.py AAPL MSFT GOOGL

# SEC filings (10-K and 10-Q from EDGAR)
python scripts/ticker/sec_filings.py AAPL
```

**Note:** Master scripts are recommended for standard workflows. Individual scripts provide flexibility for custom analysis pipelines.

# Command Reference

Quick reference for running scripts. See `index_scripts.md` for detailed script documentation.

---

## Installation

```bash
# Install all dependencies
pip install -r setup/requirements.txt

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
# Daily digest (movers, news, reddit - 1 day lookback)
python scripts/discovery.py --daily > "data/discovery/Daily_Digest_$(date +%Y-%m-%d).md"

# Weekly digest (macro, movers, news, reddit - 7 day lookback)
python scripts/discovery.py --weekly > "data/discovery/Weekly_Digest_$(date +%Y-%m-%d).md"

# Run specific modules only
python scripts/discovery.py --barrons --wsj
python scripts/discovery.py --macro
```

### Financial Statements Analysis

Fetch statements, calculate seeds and metrics, generate markdown report.

```bash
# Single ticker - outputs to data/analysis/{TICKER}/{TICKER}_statements.md
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

### Screening / Valuation

Quick multi-ticker screening using P/E vs history and price-earnings correlation.

```bash
# Screen multiple tickers (auto-fetches missing price/earnings data)
python scripts/valuation.py AAPL MSFT GOOGL
```

---

## Individual Scripts

Individual scripts can be run independently. See `index_scripts.md` for complete documentation.

### Common Individual Script Usage

```bash
# Prices (batch supported)
python scripts/ticker/prices.py AAPL MSFT

# Earnings (batch supported)
python scripts/ticker/earnings.py AAPL MSFT

# News - modular (Perigon + AlphaVantage wrapper)
python scripts/ticker/news.py AAPL --months 3

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
```

**Note:** Master scripts are recommended for standard workflows. Individual scripts provide flexibility for custom analysis pipelines.

---

## Analysis Workflow

See `CLAUDE.md` for workflow overview and `index_guidance.md` for analysis prompts.

**Typical sequence:**
1. **Identify** - Run market discovery to find candidates
2. **Screen** - Run valuation script to filter opportunities
3. **Analyze** - Run financial_statements.py and sentiment.py for deep dive
4. **Iterate** - Use indexes to navigate sources, data, and additional tools

**Analysis Prompts:** Use `Guidance/*Analysis Prompt.md` files with script outputs:
- `Screening Analysis Prompt.md` - Price/earnings screening
- `Statement Analysis Prompt.md` - Financial statement deep dive
- `Sentiment Analysis Prompt.md` - Multi-source sentiment synthesis
- `News Analysis Prompt.md` - Market news synthesis

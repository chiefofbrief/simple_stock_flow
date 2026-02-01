# Runbook

## Setup

```bash
pip install tabulate requests rich curl_cffi beautifulsoup4 html2text lxml python-dateutil
```

---

## 1. Discovery (Market Scan)
Broad market scans to find stocks worth investigating.

### Daily Digest
Runs movers, Barron's, WSJ, International Intrigue, and Reddit. Saves to `data/discovery/`.
```bash
(echo "# Peter's Digest" && echo "Generated: $(date)" && echo "---" && python scripts/market/movers.py && python scripts/market/barrons.py --days 1 --markdown && python scripts/market/wsj.py --days 1 --markdown && python scripts/market/intrigue.py --markdown && python scripts/market/reddit.py --timeframe day --markdown) > "data/discovery/Digest_$(date +%Y-%m-%d).md"
```

### Individual Market Scripts
- **Movers:** `python scripts/market/movers.py` (FMP, AlphaVantage)
- **Macro:** `python scripts/market/macro.py`
- **Barron's:** `python scripts/market/barrons.py`
- **WSJ:** `python scripts/market/wsj.py`
- **Reddit Trends:** `python scripts/market/reddit.py`

---

## 2. Screening (The Bridge)
Preliminary fundamental screening for specific tickers before a deep dive.

### Multi-Ticker Screener
Fetches Price, EPS, Revenue, and Margins for up to 5 tickers. Saves to `screening_YYYY-MM-DD.md`.
```bash
python scripts/ticker/screener.py AAPL MSFT GOOGL
```

---

## 3. Analysis (Deep Dive)

In-depth data collection and report generation for a specific stock. 

Data is cached in `data/analysis/{TICKER}/`.



### Step 1: Fetch Data (Choose any/all)



- **Fundamentals (Price):** `python scripts/ticker/prices.py AAPL`



  *(Outputs: `AAPL_prices.json` + `AAPL_prices.txt`)*



- **Fundamentals (Earnings):** `python scripts/ticker/earnings.py AAPL`



  *(Outputs: `AAPL_earnings.json` + `AAPL_earnings.txt`)*



- **Fundamentals (Valuation):** `python scripts/ticker/valuation.py AAPL`



  *(Combines Price+Earnings. Outputs: `AAPL_valuation.json` + `AAPL_valuation.txt`)*



- **Fundamentals (Financial Statements):** `python scripts/ticker/fetch_financials.py AAPL`



  *(Fetches raw statements. Outputs: `AAPL_financial_raw.json`)*







### Step 2: Financial Calculations



Process the raw financial data into modular components.



- **Calculate Seeds:** `python scripts/ticker/calc_seeds.py AAPL`



- **Calculate Metrics:** `python scripts/ticker/calc_metrics.py AAPL`



- **Compare Peers:** `python scripts/ticker/compare_financials.py AAPL MSFT GOOGL`







### Step 3: Sentiment Analysis



- **Sentiment (News):** `python scripts/ticker/news.py AAPL`



- **Sentiment (Social):** `python scripts/ticker/reddit.py --ticker AAPL`



- **Sentiment (TikTok):** `python scripts/ticker/tiktok.py AAPL`



- **Sentiment (YouTube):** `python scripts/ticker/youtube.py AAPL`







### Step 4: LLM Analysis



Copy the contents of `PROMPTS.md` to analyze the generated JSON files.









# Runbook

## Setup

```bash
pip install tabulate requests rich curl_cffi beautifulsoup4 html2text lxml python-dateutil
```

---

## 1. Discovery (Market Scan)
Broad market scans to find stocks worth investigating.

### Daily Digest
Runs movers, Barron's (1 day), WSJ (1 day), International Intrigue, and Reddit (1 day).
```bash
python scripts/discovery.py --daily > "data/discovery/Daily_Digest_$(date +%Y-%m-%d).md"
```

### Weekly Digest
Runs Macro analysis, movers, Barron's (7 days), WSJ (7 days), International Intrigue, and Reddit (7 days).
```bash
python scripts/discovery.py --weekly > "data/discovery/Weekly_Digest_$(date +%Y-%m-%d).md"
```

### Individual Market Scripts
Run specific modules individually.
```bash
python scripts/discovery.py --barrons --wsj    # Run only Barron's and WSJ
python scripts/discovery.py --macro            # Run only Macro health check
```

---

## 2. Screening (The Bridge)
Preliminary fundamental screening for one or more tickers.

### Multi-Ticker Screener
Uses the valuation model to check P/E vs history and Price-EPS correlation. Automatically fetches missing Price/Earnings data.
```bash
python scripts/ticker/valuation.py AAPL MSFT GOOGL
```

---

## 3. Analysis (Deep Dive)
In-depth data collection for specific stocks. Data is saved in `data/analysis/{TICKER}/`.

### Step 1: Batch Fetch Fundamentals
Fetch Price, Earnings, and Valuation for a list of stocks.
```bash
python scripts/ticker/prices.py AAPL MSFT
python scripts/ticker/earnings.py AAPL MSFT
python scripts/ticker/valuation.py AAPL MSFT
```

### Step 2: Fetch Financial Statements
Fetches raw statements (Income, Balance, Cash Flow) for downstream calculations.
```bash
python scripts/ticker/fetch_financials.py AAPL
```

### Step 3: Financial Calculations
Process raw data into projection seeds and priority metrics.
```bash
python scripts/ticker/calc_seeds.py AAPL
python scripts/ticker/calc_metrics.py AAPL
```

### Step 4: Comparative Analysis
Compare the target ticker side-by-side with two peers.
```bash
python scripts/ticker/compare_financials.py AAPL MSFT GOOGL
```

### Step 5: Sentiment Analysis
```bash
python scripts/ticker/news.py AAPL
python scripts/ticker/reddit.py --ticker AAPL
python scripts/ticker/tiktok.py AAPL
python scripts/ticker/youtube.py AAPL
```







### Step 4: LLM Analysis



Copy the contents of `PROMPTS.md` to analyze the generated JSON files.









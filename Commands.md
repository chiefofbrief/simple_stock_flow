# Gemini CLI Commands

This document contains copy-and-paste commands for the Gemini CLI to execute the core workflow scripts and their associated prompts. Replace `{TICKER}` with the actual stock symbol (e.g., `AAPL`).

---

## 0. Digest Generation

**Markets Digest**
```text
Run `python "Scripts/Digest Scripts/markets_digest.py"`. Then read `Prompts/prompt_digest_markets.md` and execute its instructions to analyze the generated digest.
```

**Sectors Digest**
```text
Run `python "Scripts/Digest Scripts/sectors_digest.py"`. Then read `Prompts/prompt_digest_sectors.md` and execute its instructions to analyze the generated digest.
```

---

## 1. Daily Screening

```text
Read `Prompts/prompt_daily_screening.md` and execute its instructions to compile today's candidates into `Screening_{DATE}.md`.
```

---

## Phase 1: Screening

### Step 1. Price Context
```text
Run `python Scripts/price.py {TICKER}`. Then, read `Prompts/prompt_price.md` and execute its instructions for {TICKER}.
```
*Note: You can batch screen multiple tickers by providing a space-separated list: `python Scripts/price.py AAPL MSFT GOOGL`*

### Step 2. Earnings & Valuation
```text
Run `python Scripts/earnings.py {TICKER}`. Then, read `Prompts/prompt_earnings.md` and execute its instructions for {TICKER}.
```
*Note: You must run Step 1 (Price) for a ticker before running Step 2.*

### Step 2b. Screening Bridge
```text
Read `Prompts/prompt_screening_bridge.md` and execute its instructions to update `Screening_{DATE}.md` with screening results.
```
*Note: Run after Step 1 (Price) and again after Step 2 (Earnings).*

### Step 2c. Screening Completion
```text
Read `Prompts/prompt_screening_completion.md` and execute its instructions for {TICKER}.
```
*Note: Run once per passed candidate after the final Screening Bridge.*

---

## Phase 2: Deep Dive

### Step 3. Financials
```text
Run `python Scripts/financials.py {TICKER}`. Then, read `Prompts/prompt_financials.md` and execute its instructions for {TICKER}.
```

### Step 4. Sentiment
```text
Run `python Scripts/sentiment.py {TICKER} --all`. Then, read `Prompts/prompt_sentiment.md` and execute its instructions for {TICKER}.
```

### Step 5. Footnotes & MD&A
```text
Run `python Scripts/footnotes.py {TICKER}`. Then, read `Prompts/prompt_footnotes.md` and execute its instructions for {TICKER}.
```

### Step 6. Earnings Calls
```text
Run `python Scripts/earnings_calls.py {TICKER}`. Then, read `Prompts/prompt_earnings_calls.md` and execute its instructions for {TICKER}.
```

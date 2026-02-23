# Gemini CLI Commands

This document contains copy-and-paste commands for the Gemini CLI to execute the core workflow scripts and their associated prompts. Replace `{TICKER}` with the actual stock symbol (e.g., `AAPL`).

---

## 0. Market Discovery

**Peter's Daily Digest**
```text
Run `Scripts/peters_digest.py --daily`. Then read `Prompts/prompt_digest.md` and execute its instructions to analyze the generated digest.
```

**Peter's Weekly Digest**
```text
Run `Scripts/peters_digest.py --weekly`. Then read `Prompts/prompt_digest.md` and execute its instructions to analyze the generated digest.
```

---

## Phase 1: Screening

### Step 1. Price Context
```text
Run `Scripts/price.py {TICKER}`. Then, read `Prompts/prompt_price.md` and execute its instructions for {TICKER}.
```
*Note: You can batch screen multiple tickers by providing a space-separated list: `price.py AAPL MSFT GOOGL`*

### Step 2. Earnings & Valuation
```text
Run `Scripts/earnings.py {TICKER}`. Then, read `Prompts/prompt_earnings.md` and execute its instructions for {TICKER}.
```
*Note: You must run Step 1 (Price) for a ticker before running Step 2.*

---

## Phase 2: Deep Dive

### Step 3. Financials
```text
Run `Scripts/financials.py {TICKER}`. Then, read `Prompts/prompt_financials.md` and execute its instructions for {TICKER}.
```

### Step 4. Sentiment
```text
Run `Scripts/sentiment.py {TICKER}`. Then, read `Prompts/prompt_sentiment.md` and execute its instructions for {TICKER}.
```

### Step 5. Footnotes & MD&A
```text
Run `Scripts/footnotes.py {TICKER}`. Then, read `Prompts/prompt_footnotes.md` and execute its instructions for {TICKER}.
```

### Step 6. Earnings Calls
```text
Run `Scripts/earnings_calls.py {TICKER}`. Then, read `Prompts/prompt_earnings_calls.md` and execute its instructions for {TICKER}.
```
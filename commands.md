# Commands

Copy-and-paste commands for the Gemini CLI to execute the core workflow scripts and prompts. Replace `{TICKER}` with the actual stock symbol (e.g., `AAPL`).

---

## Digest

**Markets Digest**
```text
Run `python "Scripts/Digest Scripts/markets_digest.py"`. Then read `Prompts/prompt_digest_markets.md` and execute its instructions.
```

**Sectors Digest**
```text
Run `python "Scripts/Digest Scripts/sectors_digest.py"`. Then read `Prompts/prompt_digest_sectors.md` and execute its instructions.
```

---

## Screening

### Daily Screening
```text
Read `Prompts/prompt_daily_screening.md` and execute its instructions to compile today's candidates into `Screening_{DATE}.md`.
```

### Price & Earnings

**Standalone**
```text
Run `python Scripts/price.py {TICKER}` and `python Scripts/earnings.py {TICKER}` simultaneously. Then read `Prompts/prompt_price_earnings.md` and execute its instructions for {TICKER}. Note: no Screening_{DATE}.md is available — classification context will be provided directly in chat.
```

**Digest Workflow**
```text
Identify all [LOSER] and [TAILWIND] tickers from `Screening_{DATE}.md`. Run `python Scripts/price.py {ALL_TICKERS}` and `python Scripts/earnings.py {ALL_TICKERS}` simultaneously to fetch data for all candidates. Then read `Prompts/prompt_price_earnings.md` and execute its instructions — process all [LOSER] tickers first, then all [TAILWIND] tickers.
```
*Supports batch screening: `python Scripts/price.py AAPL MSFT GOOGL` and `python Scripts/earnings.py AAPL MSFT GOOGL`*

### Screening Completion
```text
Read `Prompts/prompt_screening_completion.md` and execute its instructions for {TICKER}.
```
*Run once per passed candidate after the final Screening Bridge.*

---

## Deep Dive

### Financials
```text
Run `python Scripts/financials.py {TICKER}`. Then read `Prompts/prompt_financials.md` and execute its instructions for {TICKER}.
```
*Optional peer comparison: `python Scripts/financials.py {TICKER} --peers {PEER1} {PEER2}`*

### Footnotes & MD&A
```text
Run `python Scripts/footnotes.py {TICKER}`. Then read `Prompts/prompt_footnotes.md` and execute its instructions for {TICKER}.
```

### Earnings Calls
```text
Run `python Scripts/earnings_calls.py {TICKER}`. Then read `Prompts/prompt_earnings_calls.md` and execute its instructions for {TICKER}.
```

### Research
```text
Run `python Scripts/research.py {TICKER}`. Then read `Prompts/prompt_research.md` and execute its instructions for {TICKER}.
```
*Optional lookback override: `python Scripts/research.py {TICKER} --months 6`*

### Synthesis
```text
Read `Prompts/prompt_synthesis.md` and execute its instructions for {TICKER}.
```

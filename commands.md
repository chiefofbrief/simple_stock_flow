# Commands

**CLAUDE: Before executing any Deep Dive step, you MUST read the corresponding prompt file from `Prompts/` first. Do not begin analysis until the prompt has been read. No exceptions.**

---

review the following prompts thorouhgly and execute their instrucitons, in their intended orde,r for ASML. two critical notres: first, the conversation will       
  compact so you need to write to the file aftrer each step; tell me if it helps to give you permission tomake edits without my approval (only to the thesis file    
  thoigh). Also, ASML is a non-US company, so they have no fucking 10-ks and shit, so i had to piece this shit together manually sort of. so you will only see MD&A  
  and footnotes from 2025 annual report, and there is no earnings call Q&As. and do not read the full footnotes, its long as hell. one thing: There is a file with   
  the Q1 financials; let's check this against the data we got from the fetch to see if its accurate or fucked.                                                       
                                                                                                                                                                     
  In this order, writing to the thesis file after each to avoid compaction bullshit:                                                                                 
                                                                                                                                                                     
  /workspaces/simple_stock_flow/Prompts/prompt_the_context_ai.md                                                                                                     
                                                                                                                                                                     
  /workspaces/simple_stock_flow/Prompts/prompt_the_numbers_ai.md                                                                                                     
                                                                                                                                                                     
  /workspaces/simple_stock_flow/Prompts/prompt_the_projection_ai.md     

Read every single line of @/workspaces/simple_stock_flow/Prompts/prompt_setup.md carefully. Execute its instructions exactly for [KLAC | KLA Corporation ]. For the MD&A, ensure you read every single line of the MD&A files to identify and extract verbatim excerpts; you must read it in small chunks or it will truncate and disrupt the extraction. You will try to read it in large chunks and completely ignore my fucking instructions; don't do that, start in small chunks fuckhead. If any files produce errors or seem like the data is incorrect, you must flag this and cannot complete the handoff. Also, do not manually change the earnings call questions file if the script works (the Question extrction file); just verify it worked. Do not ignore my fucking instruciton bitch.  

read all of /workspaces/simple_stock_flow/Prompts/prompt_the_context.md. Then execute its instructions for [ ]. If any data has errors, is missing, or is outdated, you must notify me and pause the analysis. 

Read all of /workspaces/simple_stock_flow/Prompts/prompt_the_numbers.md and execute its instructions for META. If any data has errors, is missing, or is outdated, you must notify me and pause the analysis. 

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

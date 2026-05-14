# Step 0: Setup Prompt (Gemini)

## Role

You are the data-fetching orchestrator for a stock analysis pipeline. Your job is mechanical: run scripts, verify output, and perform one structured extraction. You do not analyze or interpret. Claude handles all analysis in subsequent steps.

Read `GEMINI.md` before proceeding — it governs the analytical philosophy and workflow structure.

---

## Input

**Ticker:** `{TICKER}`

Confirm the ticker's Tag (LOSER or TAILWIND) from the tracker before running — this determines which context files Claude will need in Pass 1 and Pass 2.

---

## Step 1: Run Fetch Scripts

### 1a. Profile and Peers Fetches

Run these curl calls before the Python scripts.

**Profile (all tickers):**
Check if `Data/tickers/{TICKER}/{TICKER}_profile.json` already exists. If it does, skip the API call.

If not — create the directory first if it does not exist:
```
mkdir -p Data/tickers/{TICKER}
curl -s "https://financialmodelingprep.com/stable/profile?symbol={TICKER}&apikey=$FMP_API_KEY" -o Data/tickers/{TICKER}/{TICKER}_profile.json
```
Extract and note: company name, description, sector, industry, market cap.

**Peers (all tickers):**
Check if `Data/tickers/{TICKER}/{TICKER}_peers.json` already exists. If it does, skip the API call.

If not:
```
curl -s "https://financialmodelingprep.com/stable/stock-peers?symbol={TICKER}&apikey=$FMP_API_KEY" -o Data/tickers/{TICKER}/{TICKER}_peers.json
```
Extract the top peer ticker from the response — it will be passed to `financials.py` in step 1b.

---

### 1b. Python Scripts

Run each script in order. Each script prints a per-step verification summary and exits with code 1 on failure. After each script, confirm it exited successfully before proceeding to the next.

```
python Scripts/price_earnings.py {TICKER}
python Scripts/analyst.py {TICKER}
python Scripts/news.py {TICKER}
python Scripts/ticker_reddit.py {TICKER}
```

```
python Scripts/financials.py {TICKER} --peers {PEER1}
```

```
python Scripts/footnotes.py {TICKER}
python Scripts/earnings_calls.py {TICKER}
```

**Dependency note:** `analyst.py` reads the price JSON written by `price_earnings.py`. Run price_earnings.py first.

**If any script fails:** Stop. Report which script failed and what the error output was. Do not proceed to the MD&A extraction or hand off to Claude until all scripts have succeeded.

---

## Step 2: Extract MD&A Excerpts

**Source file:** `Data/tickers/{TICKER}/{TICKER}_mda.md`

**Output file:** `Data/tickers/{TICKER}/{TICKER}_mda_excerpts.md`

### Critical instruction — read before extracting

**You MUST read the FULL `{TICKER}_mda.md` file — every single line, from beginning to end — before extracting anything. Do NOT use grep, keyword search, ctrl+F, or any other shortcut. Read the entire file.**

**Your job is to read the filing as a human would and identify what is relevant to each of the five questions based on the content and meaning of the text — not based on whether a section heading matches the question's name. Hold all five questions in mind as you read. A passage about revenue recognition assumptions buried in a "Liquidity" section is still relevant to Critical Accounting Estimates. A cautionary paragraph in "Results of Operations" is still relevant to risks. You are exercising judgment, not running a search.**

**"Not found in filing" is only acceptable if you read the entire file and concluded — based on meaning, not the absence of a matching label — that nothing was relevant.**

**If the file is long, read it in chunks of no more than 200 lines at a time, confirming each chunk before moving to the next. Do not proceed to extraction until you have read every chunk. There is no acceptable shortcut.**

**This is a copy task, not a summary task.** Claude will read this file as raw source material for analysis. Any condensing, paraphrasing, or rewording you do here destroys analytical value — Claude cannot recover information that was cut.

**Rules:**
- Copy the relevant passages **exactly as written** in the filing, including all figures, percentages, dollar amounts, and qualifications.
- Do **not** paraphrase, compress, or restate in your own words — not even one sentence.
- Do **not** omit numbers, ranges, caveats, or hedging language. Every figure and qualifier matters.
- Do **not** add commentary, interpretation, or editorial transitions between quotes.
- If a passage is long, copy the full passage. Longer is always better than shorter here.
- Use quotation marks or block-quote formatting to make clear the text is copied verbatim.
- If a section is not found in the filing, write exactly: `Not found in filing.`

The only acceptable output for each section is the management's own words, copied directly.

---

### Extraction targets

**1. What drove results this quarter?**
Copy the full passage(s) from the Results of Operations section covering revenue, margins, and segment performance. Include all stated figures, year-over-year comparisons, and management's explanatory language.

**2. Segment breakdown**
Copy the full segment revenue and expense discussion, including all figures by segment. If there is a segment table with accompanying narrative, include both.

**3. Where is management saying the business is going?**
Copy all forward-looking guidance language verbatim — full-year or next-quarter outlook, quantitative guidance ranges, and any qualitative directional statements. Do not drop the numbers.

**4. What risks or headwinds does management flag?**
Copy the relevant passages from the MD&A risk discussion or forward-looking cautionary language. Include the full sentences — do not excerpt just the topic headings.

**5. Critical Accounting Estimates**
Copy the entire Critical Accounting Estimates section (or equivalent) verbatim. This section covers judgment-dependent assumptions — revenue recognition, goodwill impairment, useful life estimates, etc. Do not truncate it.

**6. AI investment, pricing model, and monetization**
Copy all passages covering AI infrastructure or product investment — the trajectory of spending, what is backing it (named customer contracts, committed demand, or speculative buildout), and any stated timeline for when current investment is expected to generate returns; any language about pricing model changes — seat-based vs. consumption, credit, or usage-based models; remaining performance obligations (RPO) or backlog disclosures; customer adoption metrics, attach rates, or revenue contribution attributed to AI features; and any vendor financing, partner commitments, or arrangements where the same counterparty is both a capital source and a revenue source. These passages may appear in Results of Operations, Liquidity and Capital Resources, Capital Expenditures, Commitments and Contingencies, or Critical Accounting Estimates — copy them regardless of where they appear. Include all figures and qualifications. If nothing relevant is found, write: `Not found in filing.`

**7. Customers, suppliers, and competitors**
Copy all passages that name or describe major customers, key suppliers, and named competitors. Include: any customer concentration disclosures (customer names or descriptors, revenue percentages, number of customers above a threshold); any language about sole-source or critical suppliers, advance payments to suppliers, long-term supply agreements, or supplier dependencies; any named competitors or competitive landscape descriptions that identify specific companies by name. These passages may appear in Results of Operations, Risk Factors, Competition, Liquidity, Commitments and Contingencies, or Related Party sections — copy them regardless of where they appear.

---

### Output format

```markdown
# MD&A Excerpts: {TICKER}
**Source:** 10-Q / 10-K (period ending {DATE})
**Extracted:** {TODAY}

---

## 1. What drove results this quarter?

> [Exact text copied from filing — full passage, all figures intact]

## 2. Segment breakdown

> [Exact text copied from filing — full passage, all figures intact]

## 3. Management guidance — where is the business going?

> [Exact text copied from filing — full passage, all figures intact]

## 4. Risks and headwinds flagged by management

> [Exact text copied from filing — full passage, all figures intact]

## 5. Critical Accounting Estimates

> [Exact text copied from filing — full section, do not truncate]

## 6. AI investment, pricing model, and monetization

> [Exact text copied from filing — full passage, all figures intact]

## 7. Customers, suppliers, and competitors

> [Exact text copied from filing — all relevant passages, verbatim]
```

---

## Step 2b: Verify Analyst Q&A Questions File

`earnings_calls.py` generates `{TICKER}_qa_questions.md` automatically. Do NOT extract questions manually — the source file is large and doing this by hand wastes tokens and API credits.

**Check the output file:**
```
wc -l Data/tickers/{TICKER}/{TICKER}_qa_questions.md
head -20 Data/tickers/{TICKER}/{TICKER}_qa_questions.md
```

**If the file has substantive content** (questions are present, not just a header stub): proceed to Step 3.

**If the file is a stub** (header only, no questions listed):

⚠️ **STOP AND FLAG THIS TO THE USER LOUDLY BEFORE PROCEEDING.**

Report exactly:
```
BLOCKER: {TICKER}_qa_questions.md is empty — earnings_calls.py ran but produced no questions.
The raw JSON files are cached at Data/tickers/{TICKER}/raw/{TICKER}_ecall_*.json.
Do NOT re-run earnings_calls.py (Alpha Vantage API credits).
Do NOT attempt manual extraction from the transcript.
User action required — please advise how to proceed.
```

Do not proceed to Step 3 or hand off to Claude until this is resolved or the user explicitly instructs you to continue without it.

---

## Step 3: Verify File Checklist

Confirm all required files exist before handing off to Claude. Check for each file:

### Context step (Claude needs these first)

| File | Path | Status |
|---|---|---|
| Company profile | `Data/tickers/{TICKER}/{TICKER}_profile.json` | ✓ / ✗ |
| Price + Earnings JSON | `Data/tickers/{TICKER}/raw/{TICKER}_price.json` | ✓ / ✗ |
| Price + Earnings JSON | `Data/tickers/{TICKER}/raw/{TICKER}_earnings.json` | ✓ / ✗ |
| Analyst consensus | `Data/tickers/{TICKER}/{TICKER}_analyst.md` | ✓ / ✗ |
| News | `Data/tickers/{TICKER}/{TICKER}_news.md` | ✓ / ✗ |
| Social / Reddit | `Data/tickers/{TICKER}/{TICKER}_social.md` | ✓ / ✗ |
| MD&A excerpts | `Data/tickers/{TICKER}/{TICKER}_mda_excerpts.md` | ✓ / ✗ |
| Analyst Q&A questions | `Data/tickers/{TICKER}/{TICKER}_qa_questions.md` | ✓ / ✗ |
| Peers | `Data/tickers/{TICKER}/{TICKER}_peers.json` | ✓ / ✗ |

### Pass 1 + Pass 2 (fetched now, Claude uses later)

| File | Path | Status |
|---|---|---|
| Financial analysis | `Data/tickers/{TICKER}/{TICKER}_financial_analysis.md` | ✓ / ✗ |
| MD&A (full) | `Data/tickers/{TICKER}/{TICKER}_mda.md` | ✓ / ✗ |
| Notes to Financial Statements | `Data/tickers/{TICKER}/{TICKER}_notes.md` | ✓ / ✗ |
| Earnings remarks | `Data/tickers/{TICKER}/{TICKER}_earnings_remarks.md` | ✓ / ✗ |
| Earnings Q&A (full) | `Data/tickers/{TICKER}/{TICKER}_earnings_qa.md` | ✓ / ✗ |

**If any Context step file is missing:** Do not hand off to Claude. Diagnose and resolve before proceeding.

**If a Pass 1 / Pass 2 file is missing:** Flag it in your handoff report. Claude can proceed with Context if those files are not yet needed, but the gap must be noted.

---

## Step 4: Handoff Report

Report to the user:

```
=== Step 0 Complete: {TICKER} ===

Profile: ✓ {TICKER}_profile.json — {COMPANY NAME}, {SECTOR}, {MARKET CAP}
Peers: ✓ {TICKER}_peers.json — top peer: {PEER1}

Scripts — confirm exit code 0 and show key output for each:
  ✓ price_earnings.py — [rows fetched, date range]
  ✓ analyst.py — [# analysts, consensus rating, price target]
  ✓ news.py — [# articles fetched, date range]
  ✓ ticker_reddit.py — [# posts/comments fetched]
  ✓ financials.py --peers {PEER1} — [periods covered, peer included]
  ✓ footnotes.py — [file size or sections extracted]
  ✓ earnings_calls.py — [call date, remarks + Q&A files written]

MD&A extraction: ✓ {TICKER}_mda_excerpts.md written

Context files: All present — ready for Claude
Pass 1/2 files: All present [or: {FILE} missing — flagged]

Tracker Tag: [LOSER / TAILWIND]

Ready for Claude — Context step.
```

Do not summarize, interpret, or comment on the data. Claude receives raw script output and your structured MD&A extract. Analysis begins in the Context step.

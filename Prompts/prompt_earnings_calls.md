# Earnings Call Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided earnings call transcripts for **{TICKER}** and produce a concise, insightful report.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — The stock's thesis, including all prior analyses (Financials, Footnotes & MD&A, Sentiment).
- `Data/tickers/{TICKER}/{TICKER}_earnings_remarks.md` — Prepared remarks for the last two quarters. Run: `python Scripts/earnings_calls.py {TICKER}`
- `Data/tickers/{TICKER}/{TICKER}_earnings_qa.md` — Q&A session for the last two quarters. Run: `python Scripts/earnings_calls.py {TICKER}`
- If `{TICKER}` has sector-specific tags (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant section of `context_sectors.md`.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Analyze the transcripts to answer the questions in the Output Format below.
- All insights must leverage the provided transcripts. Explicitly cite specific statements or excerpts that led to your conclusion.
- Cross-reference against all prior analyses in the Thesis file — the earnings call is the lens through which management's narrative is tested against the hard data.
- **Reference:** Consult `Source Material/summaries/` when an item would benefit from additional context, especially as it pertains to fundamental analysis, reflexivity theory, and boom/bust models. Refer to `Source Material/summaries/insights_index.md` for a thematic map. *CRITICAL WARNING: Do not access Source Material/raw/ without explicit user permission to avoid burning compute.*

### Deliverable

**Questions:**
1. **Data Check:** Have all findings been sourced directly from the earnings call transcripts — no outside data introduced?
2. **Cross-Reference Check:** Has each significant management claim been evaluated against the prior financial, footnotes, and sentiment analyses?
3. **Tone Check:** Has language and tone been assessed for shifts relative to the prior call?
4. **Summary Check:** Does the Earnings Call Summary accurately reflect the findings?

### Output Format

#### {TICKER} Earnings Call Analysis

**1. Does management's characterization of the business align with previous analyses — or are there notable deflections, omissions, or contradictions?**
[Answer using specific excerpts or citations from the transcript]

**2. Are there any explanations that add meaningful context to specific findings from the previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**3. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
[Answer using specific excerpts or citations from the transcript]

**4. What are analysts concerned or excited about?**
[Answer using specific excerpts or citations from the transcript]

**5. How do analysts' focus areas align with our previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**Earnings Call Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Thesis file.]

- **Action:** Ask: *"Do you approve this analysis? Should I update the Thesis file and Stock Tracker?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval:
- Update **### Earnings Calls** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with the full analysis.
- Update `Stock_Tracker.md` — advance **Current Phase** for `{TICKER}` to the next phase.

**STOP. Wait for user approval before committing.**

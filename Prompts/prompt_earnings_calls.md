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
- If `{TICKER}` has an `AI SC` Sector Theme (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant layer section of `context_ai_supply_chain.md`.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Analyze the transcripts to answer the questions in the Output Format below.
- All insights must leverage the provided transcripts. Explicitly cite specific statements or excerpts that led to your conclusion.
- Cross-reference against all prior analyses in the Thesis file — the earnings call is the lens through which management's narrative is tested against the hard data.
- **Call Weighting:** The two calls are not equal in strategic weight. The call covering full-year results and annual guidance typically contains the more material disclosures — long-term targets reiterated or revised, annual segment performance, and the strategic reset for the coming year. The more recent call is usually incremental. Identify which call carries more weight before beginning the analysis, and ensure both are read with equal care. Where the two calls diverge in tone, data, or emphasis, note it explicitly.
- **Open Questions Check:** Before answering the output questions, return to the **Footnotes & MD&A** section of the Thesis. List every item explicitly flagged for Earnings Call investigation. For each, state: (a) whether management addressed it on either call, (b) what was said (with citation), and (c) whether the answer strengthens, weakens, or leaves the thesis unchanged. Items not addressed should be flagged as unresolved and carried forward to the Research phase.
- **Reference:** Consult `Source Material/summaries/` when an item would benefit from additional context, especially as it pertains to fundamental analysis, reflexivity theory, and boom/bust models. Refer to `Source Material/summaries/insights_index.md` for a thematic map. *CRITICAL WARNING: Do not access Source Material/raw/ without explicit user permission to avoid burning compute.*

### Deliverable

**Questions:**
1. **Data Check:** Have all findings been sourced directly from the earnings call transcripts — no outside data introduced?
2. **Call Weighting Check:** Has the more strategically material call been identified, and have both calls been read with equal care?
3. **Cross-Reference Check:** Has each significant management claim been evaluated against the prior financial, footnotes, and sentiment analyses?
4. **Open Questions Check:** Has every item flagged in the Footnotes phase for Earnings Call investigation been explicitly addressed or flagged as unresolved?
5. **Tone Check:** Has language and tone been assessed for shifts relative to the prior call?
6. **Summary Check:** Does the Earnings Call Summary accurately reflect the findings?

### Output Format

#### {TICKER} Earnings Call Analysis

**Call Orientation**
[1–2 sentences identifying which of the two calls carries more strategic weight and why — e.g., full-year results + annual guidance vs. incremental quarterly update. This frames the weighting applied throughout the analysis.]

**1. Does management's characterization of the business align with previous analyses — or are there notable deflections, omissions, or contradictions?**
[Answer using specific excerpts or citations from the transcript. Draw from both calls; note where they differ.]

**2. Are there any explanations that add meaningful context to specific findings from the previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**3. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
[Answer using specific excerpts or citations from the transcript]

**4. What are analysts concerned or excited about?**
[Answer using specific excerpts or citations from the transcript]

**5. How do analysts' focus areas align with our previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**6. Were the open questions from the Footnotes phase resolved?**
[List each item flagged for Earnings Call investigation in the Footnotes & MD&A section. For each: state whether it was addressed, cite what was said, and assess whether the answer strengthens, weakens, or leaves the thesis unchanged. Flag any items that remain unresolved and should carry into the Research phase.]

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

# Research Analysis Prompt

## Role
You are an expert financial analyst. Your task is to investigate open questions from prior analyses of **{TICKER}** using recent news data and targeted web research.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — The stock's thesis, including all prior analyses (Financials, Footnotes & MD&A, Earnings Calls).
- `Data/tickers/{TICKER}/{TICKER}_research.md` — Recent news data (Perigon + FMP). Run: `python Scripts/research.py {TICKER}`
- If `{TICKER}` has an `AI SC` Sector Theme (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant layer section of `context_ai_supply_chain.md`.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- **Compile open questions first:** Before consulting the news data, review all prior analyses in the Thesis file and identify every flagged uncertainty, unresolved concern, or item explicitly marked for further investigation. These become your research agenda.
- **Match questions to news:** For each open question, search the news data for relevant articles, statements, or developments. Cite specific headlines, sources, and dates.
- **Targeted web fetches:** For open questions that remain unresolved after reviewing the news data, you may perform up to **3 targeted web fetches** to find material information. Use this budget selectively — only for questions that are material to the investment thesis and genuinely unresolved.
- **New material:** Flag any significant news items that were not anticipated by the prior analyses but are relevant to the thesis.
- **Source citation (required):** Every finding must cite a specific article, headline, date, and source. "Per recent news" is not acceptable. Analyst estimates and third-party forecasts are forward-looking — label them as such and do not blend them with confirmed historical data from prior analyses.
- **Epistemic tagging (required):** Tag all claims. News reports are `[CONFIRMED: source, date]` for what the article says, but `[INFERRED]` for the underlying claim if the article itself is making an inference. Distinguish between what is directly reported and what is being concluded from the report.
- **Cross-section consistency (required):** Any figure cited in the Research section that also appears in a prior Thesis section must be consistent. Where news sources cite figures that conflict with prior analyses, investigate — do not silently adopt the news figure over the filing figure.

### Deliverable

**Questions:**
1. **Open Questions Check:** Have all flagged uncertainties and unresolved items from the prior analyses been compiled as the research agenda?
2. **Data Check:** Have all findings been sourced directly from the news data or cited web sources — no outside knowledge introduced?
3. **Web Fetch Check:** Were web fetches used selectively (max 3), only for material unresolved questions?
4. **Summary Check:** Does the Research Summary accurately reflect the findings?
5. **Tagging Check:** Are all claims tagged `[CONFIRMED]`, `[ESTIMATED]`, or `[INFERRED]` with specific source citations (headline, date, outlet)?
6. **Labeling Check:** Are analyst estimates and third-party forecasts labeled as forward-looking? Are news-cited figures verified against prior Thesis sections for consistency?

### Output Format

#### {TICKER} Research Analysis

**Open Questions**
[Bulleted list of uncertainties and unresolved items identified from prior analyses, with a brief note on which analysis flagged each one]

**Findings**

[For each open question: restate the question, then provide findings from the news data and/or web research. Cite specific headlines, sources, and dates. If a question remains unresolved, state that explicitly.]

**New Material**
[Any significant developments from the news data that were not anticipated by prior analyses but are relevant to the thesis. If none, state "None identified."]

**Research Summary**
[A concise paragraph summarizing what was resolved, what remains open, and any new material developments. This text will be copied to the Thesis file.]

- **Action:** Ask: *"Do you approve this analysis? Should I update the Thesis file and Stock Tracker?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval:
- Update **### Research** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with the full analysis.
- Update `Stock_Tracker.md` — advance **Current Phase** for `{TICKER}` to the next phase.

**STOP. Wait for user approval before committing.**

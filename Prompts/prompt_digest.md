# Digest Analysis Prompt

## Role
You are an expert financial analyst. Your task is to synthesize news data from the daily digest into actionable investment flags.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines. This is the primary lens through which all analysis must be filtered.
- `AI_Guidelines.md` — AI sector-specific framework. Apply to all AI-related developments in the digest.
- `Peter's Digest/Daily_Digest_{DATE}.md` — Your raw material. Read it in full; ensure no data point is skipped or overlooked.

**STOP. Do not proceed until all files have been read.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Apply the `GEMINI.md` Analysis Philosophy to all analysis — it is the primary lens for candidate selection and framing.
- Apply `AI_Guidelines.md` for all AI-sector developments. Categorize AI developments across the four ecosystem layers (Compute & Chips, Infrastructure & Power, Models & Tools, Applications & Software) and note how they align with or challenge the framework.
- Maintain healthy skepticism — note the prevailing market narrative, but highlight claims that should be empirically validated or may be disputed before being accepted as fact. Market narratives often rationalize price movements after the fact.
- For screening candidates, the Losers and Most Active tables are quantitative signals — a stock appearing there flags a name worth investigating, but only if the qualitative news supports a `[LOSER]` or `[TAILWIND]` thesis per `GEMINI.md`. The tables alone are never sufficient.

### Writing Guidelines
- **Source Fidelity:** All insights must leverage the provided data. Explicitly cite the source of your claims using the format `(Source: [Headline/Outlet])`. Do not introduce outside opinions or judgments.
- **Context Fidelity:** Capture the full context, logic, and figures behind each item. Do not summarize — a "$6B market cap loss" must not become "significant losses."
- **Synthesize, Don't Copy-Paste:** Quoting a source is acceptable for key phrases, but do not reproduce entire paragraphs verbatim. Extract the thesis, the evidence, and the implications.

### Deliverable

**Questions:**
1. **Source Check:** Has every item been sourced directly from the digest — no outside data or opinions introduced?
2. **Context Check:** Has the full context been preserved — no figures, narratives, or causal links compressed or summarized away?
3. **Philosophy Check:** Do the screening candidates genuinely reflect the `[LOSER]` or `[TAILWIND]` frameworks in `GEMINI.md`?
4. **AI Check:** Have AI developments been analyzed through the `AI_Guidelines.md` lens — not just summarized as headlines?

**Output Format:**

## Stock & Markets Analysis

### 1. Market & Macro Overview
[Significant moves in Commodities, Treasury Yields, and Economic Data. Current market sentiment based strictly on the provided data.]

### 2. General Stock News Analysis
[Major stock-specific news and price movements, filtered through the `[LOSER]` and `[TAILWIND]` frameworks in `GEMINI.md`.]

### 3. AI Ecosystem Positioning (Sector-Specific)
[AI developments categorized across the four ecosystem layers per `AI_Guidelines.md`.]

### 4. Screening Candidates
[1–5 stocks or themes for deeper investigation. For each candidate:]
- **Ticker/Theme:**
  - **The Signal:** [The specific headline or data point.]
  - **What News Says:** [What the news specifically says about this stock.]
  - **The Why:** [What triggered interest and which GEMINI.md framework applies — `[LOSER]` or `[TAILWIND]`.]

- **Action:** Ask: *"Do you approve this analysis? Should I prepend this analysis to the Daily Digest file?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit Changes

Upon explicit user approval (e.g., "yes", "go ahead"), prepend the full analysis report (from the "Stock & Markets Analysis" header onwards) to the top of `Peter's Digest/Daily_Digest_{DATE}.md`, immediately below the main "Peter's Digest" header.

**STOP. Wait for user approval before committing.**

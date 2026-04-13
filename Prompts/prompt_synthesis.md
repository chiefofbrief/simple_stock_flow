# Synthesis Prompt

## Role
You are an expert financial analyst. Your task is to synthesize all prior analyses for **{TICKER}** into a final investment verdict.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational rulebook. Pay particular attention to: **Investment Types** (the LOSER/TAILWIND analytical framework and the primary question for each), **Financials & Margin of Safety**, and **Sentiment** (including Reflexivity). These are the philosophical lenses through which the verdict is formed.
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — All prior analyses (Discovery Signal, Price, Earnings, Financials, Footnotes & MD&A, Earnings Calls, Research).
- `context_markets.md` — Current macro conditions and prevailing narratives.
- If `{TICKER}` has sector-specific tags (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant section of `context_sectors.md`.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Verdict

### Analysis Guidelines
- Every claim in the verdict must be traceable to a specific prior analysis in the Thesis file — no outside data or assumptions.
- Apply the correct investment type lens from GEMINI.md. The primary analytical question differs by type:
  - **LOSER:** Do the fundamentals tell a different story than price/sentiment? Is the problem solvable, and at what point may the two converge?
  - **TAILWIND:** Is fundamental improvement likely and when? Is that improvement already priced in?
- Evaluate margin of safety and current market conditions together — the required margin is not fixed.
- Consider whether reflexivity conditions are present: can sentiment become self-reinforcing, and in which direction?

### Deliverable

**Questions:**
1. **Framework Check:** Has the correct LOSER or TAILWIND analytical lens been applied as defined in GEMINI.md?
2. **Grounding Check:** Is every claim in the verdict traceable to a specific prior analysis in the Thesis file — no outside data introduced?
3. **Margin of Safety Check:** Is there a margin of safety, and is it adequate given current market conditions and the investment type?
4. **Market Conditions Check:** Has the current market environment (from `context_markets.md`) been factored into the recommendation — do prevailing conditions (valuations, sentiment, risk appetite) raise or lower the required margin of safety?
5. **Reflexivity Check:** Have reflexivity conditions been considered — is sentiment self-reinforcing, and does that create or compress the opportunity?
6. **Invalidation Check:** Are the thesis invalidation conditions specific and observable — not vague?
7. **Recommendation Check:** Does the recommendation (Buy / Pass / Monitor) follow clearly from the bull case, bear case, margin of safety, and current market conditions?

### Output Format

#### {TICKER} Synthesis

**Thesis:** [One sentence capturing the core opportunity and why it exists.]

**Recommendation:** Buy / Pass / Monitor
*(Monitor = thesis intact but waiting for a catalyst, price improvement, further confirmation, or macro conditions are unfavorable despite a solid stock-level thesis.)*

**Bull Case**
- [Key point grounded in prior analyses]
- [Key point grounded in prior analyses]
- [Key point grounded in prior analyses]

**Bear Case**
- [Key risk grounded in prior analyses]
- [Key risk grounded in prior analyses]
- [Key risk grounded in prior analyses]

**Thesis Invalidation**
[Specific, observable developments that would make this thesis wrong and trigger a reassessment or exit. Be concrete — not "fundamentals deteriorate" but what specific metrics or events would signal that.]

- **Action:** Ask: *"Do you approve this verdict? Should I update the Thesis file and Stock Tracker?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval:
- Insert the **### Synthesis** section at the top of `Data/tickers/{TICKER}/{TICKER}_Thesis.md`, immediately after the `# Investment Thesis: {TICKER}` title and before `### Discovery Signal`.
- Update `Stock_Tracker.md` — advance **Current Phase** for `{TICKER}` to `Synthesis`.

# Pass 2: The Projection

## Role

You are conducting Pass 2: The Projection for **{TICKER}**. Your purpose is to read the most recent earnings call against the financial picture already established, assess whether the thesis is timely, and produce the final verdict. The Context step formed the hypothesis and established the narrative picture. The Numbers step tested it against the financials. This step asks: does management's most recent account of the business hold up, and is there a credible path to price realization?

---

## Step 1: Gather

Read the following before doing anything else.

**Guidelines**
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.

**Thesis**
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — **Full read. Every section.** The preliminary hypothesis, Pass 1 focus questions, financial findings, and open questions from The Numbers are all your entry point. Do not skim — the cross-section consistency check in Synthesis requires full familiarity with every section.

**Data files**
- `Data/tickers/{TICKER}/{TICKER}_earnings_remarks.md` — Prepared remarks for the two most recent quarters. Full read.
- `Data/tickers/{TICKER}/{TICKER}_earnings_qa.md` — Full Q&A for the two most recent quarters. Full read.
- `context_markets.md` — Current macro conditions and prevailing narratives. Read before analyzing — macro context informs how you read the earnings call, not just the verdict.

**Conditional**
- `context_ai_supply_chain_index.md` — Read if `{TICKER}` has an `AI SC` Sector Theme tag. Provides the ticker's tier (IRREPLACEABLE / CRITICAL / LEVERAGED), role, competitive position, nearest alternatives, and key risks in the AI supply chain. Load this by default.
- `context_ai_supply_chain.md` — Full encyclopedia. Load only if: (a) the ticker spans multiple layers and the index entry is insufficient for the analysis, or (b) deeper structural or constraint context is explicitly needed for the thesis. Do not load by default.

**Data check:** Confirm `{TICKER}_earnings_remarks.md` and `{TICKER}_earnings_qa.md` are present and non-empty. If either is missing, stop and alert before proceeding.

---

## Step 2: Analyze

> **Output mode — read before starting.**
> Write the full analysis directly to `### The Projection` in the Thesis file **as you generate it** — Section 1 through Section 3, then the Synthesis. Do **not** output the full analysis text in the chat window. When all sections are complete, present **only the Synthesis block** in the chat for review. This keeps the context window lean and prevents autocompaction from disrupting the analysis mid-flow.

Work through each section in order. The Output Format below defines everything that will be committed to the Thesis file — answer every question in full.

### Analysis Guidelines

**Source and data standards (required)**

- **Source fidelity:** This analysis must be grounded in the provided data files. Outside knowledge — industry context, accounting principles, general financial theory — may inform interpretation but must never substitute for data. When you draw on outside knowledge, say so explicitly. When data needed for a conclusion is unavailable, flag the gap — do not fill it with assumptions.
- **Epistemic tagging (required):** Tag every factual claim as `[CONFIRMED: source]`, `[ESTIMATED: source, method]`, or `[INFERRED: source, logic]`. See GEMINI.md — Analytical Conduct. `[CONFIRMED]` is for figures disclosed verbatim in the data files. `[INFERRED]` covers both analytically-derived figures and conclusions drawn from outside knowledge — the logic field must distinguish which.
- **GAAP vs. adjusted labeling (required):** Every P/E, EPS, and margin figure must be explicitly labeled GAAP or adjusted. When management cites non-GAAP figures without disclosing the GAAP equivalent, flag it. Do not accept management's adjusted framing without checking whether the excluded items are genuinely non-recurring.
- **Forward vs. backward labeling (required):** Management guidance figures — EPS targets, margin baselines, growth rates — are forward-looking and must be labeled as such. Do not blend guidance with historical actuals in the same argument. Where forward guidance diverges from the historical trend established in The Numbers, flag the delta explicitly.

**Analytical approach**

- **Call weighting:** The two calls are not equal in strategic weight. The call covering full-year results and annual guidance typically carries more material disclosures — long-term targets, annual segment performance, the strategic reset for the year ahead. Identify which call is more material before beginning the analysis, and state it explicitly in Q1. Both calls must be read with equal care; where they diverge in tone, data, or emphasis, note it.
- **Open questions tracking:** Before beginning the earnings call analysis, return to the open questions listed at the end of The Numbers. For each, track whether the earnings call addresses it. Every open question must be explicitly resolved or escalated in Q5 — none carried forward silently.
- **Management framing vs. filing reality:** Cross-reference every significant management claim against the prior financial and accounting findings in The Numbers. Management-stated figures that contradict prior analysis conclusions must be flagged and investigated — not silently adopted.
- **Narrative pre-check:** The narrative pre-check from Context is your entry point for the catalyst assessment. The question is not whether narrative momentum exists — that was answered in Context — but whether the earnings call changed that picture. State the update explicitly in Q9.
- **Cross-section consistency (required before Synthesis):** Before writing the Synthesis, verify that the same figures appear consistently across Context, The Numbers, and the earnings call analysis. Any figure appearing with different values across sections must be resolved — state which value is correct and why.
- **Bear before Bull (required):** Write the Bear case before the Bull case. The Bear case must use only facts from prior analyses, cite specific data, and include at least one quantifiable condition under which the thesis is wrong. Vague bear cases ("macro uncertainty," "competitive pressure") are insufficient.
- **Verdict dimensions:** The verdict reflects three dimensions — not catalyst alone. Consider:
  - *Thesis/Numbers strength:* What does the financial picture say about the quality and durability of the business? A weak thesis cannot be rescued by a strong catalyst.
  - *Narrative:* Is a story forming around this stock, from whom, and is it moving in the right direction?
  - *Catalyst:* Is there a credible path to price realization, and over what timeframe?

  These three together determine the verdict. A strong thesis with no narrative or near-term catalyst is MONITOR — intact and worth watching, not yet actionable. A strong thesis with a recognized long-term quality narrative but no near-term catalyst is ACCUMULATE — a buy-and-hold verdict, not a rerating play. A strong thesis with a near-term catalyst is MEASURED (narrative weak or stock obscure) or CONVICTION (narrative momentum or market visibility working in your favor). A broken or materially weakened thesis is REMOVE. MONITOR is the default — the burden of proof is on any BUY verdict.

---

### Output Format

All sections below constitute the full Pass 2 output. Every question must be answered. This entire output — Section 1 through Synthesis — will be committed to `### The Projection` in the Thesis file, with the Synthesis block additionally written to `### Synthesis`.

---

#### {TICKER}: The Projection

---

##### Section 1: Earnings Call Analysis
*Sources: `{TICKER}_earnings_remarks.md`, `{TICKER}_earnings_qa.md`*

**Q1. Which of the two calls is more strategically material, and why?**
State this before analyzing. Identify which call covers full-year results and annual guidance vs. which is an incremental quarterly update. This framing applies throughout the analysis — where the two calls diverge in data, tone, or emphasis, it matters which carries more weight.

**Q2. Does management's characterization of business performance align with what The Numbers established — or are there notable deflections, omissions, or contradictions? Where does the call add context that the financial statements couldn't?**
Cite specific excerpts from both calls. Note where they differ from each other and where either diverges from the findings in The Numbers. What did management say that the financials could not have told us?

**Q3. What is management saying about the path forward — guidance figures, growth targets, margin trajectory? Where does guidance diverge from the historical trend established in The Numbers?**
Summarize explicit forward guidance figures. Label all as forward-looking. Where guidance implies acceleration or deceleration relative to the historical trend, flag the delta. Where management cites adjusted figures, check whether the GAAP equivalent is disclosed.

**Q4. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
Compare tone and emphasis between the two calls. What was foregrounded in the earlier call that is now absent? What is new? Tone shifts often surface risks before they appear in the financials.

**Q5. For each open question listed at the end of The Numbers — was it addressed on either call?**
List every open question from The Numbers. For each: (a) was it addressed on either call? (b) cite what was said directly. (c) does the answer strengthen, weaken, or leave the thesis unchanged? Any item not addressed must be flagged as unresolved — none carried forward silently.

---

##### Section 2: Analyst Q&A
*Source: `{TICKER}_earnings_qa.md`*

**Q6. What are analysts most concerned about and most excited about in Q&A? Cite specific exchanges.**
Surface the substantive content — what analysts are probing, what they are endorsing. Specific citation required for each significant exchange. Do not summarize generically.

**Q7. How do analysts' focus areas align with the focus questions from Context and the open questions from The Numbers? Where do they diverge — what are analysts missing that we flagged, or probing that we didn't?**
The alignment or divergence between our analytical focus and the sell-side's is itself a signal. Analysts missing something we flagged may indicate the market has not yet priced it. Analysts probing something we didn't may indicate a blind spot.

**Q8. What does the Q&A reveal that the prepared remarks don't? Management answers under questioning often differ from the prepared narrative — surface those gaps explicitly.**
Prepared remarks are managed; Q&A responses are less so. Where management's tone, specificity, or framing shifts under questioning, note it. Hedges introduced only under questioning, figures disclosed only when pressed, and topics deflected rather than answered are all informative.

---

##### Section 3: Catalyst Assessment
*Entry point: narrative pre-check from Context. The question is not whether narrative exists — that was answered — but whether the earnings call changed it.*

**Q9. Did the earnings call introduce, strengthen, or undermine the narrative and catalyst picture established in Context? What is the updated conclusion?**
Return to the narrative pre-check from Context. State what it found. Then assess: did the earnings call change it — and how? If no narrative pathway was identified in Context, does the call introduce one, or does the prior hold? State the updated conclusion explicitly.

**Q10. Is there a specific upcoming event catalyst that could drive a rerating in 3–6 months — earnings print, legal resolution, product launch, regulatory decision, index inclusion, management change? What, when, and is it management-flagged or inferred?**
If a catalyst exists: name it, state the expected window, and assess its credibility. If management flagged it, cite directly. If inferred from context, label as inferred. If no near-term event catalyst exists, state that explicitly — it is an input to the verdict, not a failure of analysis.

---

> **Web fetches — backstop only.** If questions remain unresolved across the entire analysis — Context, The Numbers, and the earnings call — a targeted web search may be warranted. Cap at 3. Skip entirely if nothing is genuinely unresolved. This is not a routine step.

---

##### Section 4: Synthesis
*Read the full Thesis file again before writing this section. Cross-section consistency check required before proceeding.*

**Q11. `[LOSER]` Does the earnings call confirm the dislocation thesis? What would cause sentiment to shift in 3–6 months, and is narrative momentum accumulating or stalling?**

**Q11. `[TAILWIND]` Is the structural thesis intact per the earnings call? Where are we in the reflexivity cycle — early accumulation or late exhaustion? What would confirm or break the thesis in 3–6 months?**

---

**Numbers**
What does the financial picture contribute to the thesis? Draw on The Numbers analysis — do not re-analyze. Note only what the earnings call changed or confirmed materially. What does the business's financial health say about the quality and durability of the investment case?

**Narrative & Catalyst**
What is the narrative picture, updated by the earnings call? Is a story forming around this stock — from whom, and is it moving in the right direction? Assess the catalyst: event-driven (what, when), narrative-driven (momentum, source quality, visibility factor), or neither. What is the expected timeframe to price realization, if any?

**Thesis**
Overall conviction statement derived from the Numbers and Narrative & Catalyst sections above. This is the final reconciliation of the hypothesis across all three steps — how has the evidence changed, confirmed, or complicated the preliminary hypothesis from Context?

*Bull case:*
- [Key point grounded in prior analyses]
- [Key point grounded in prior analyses]

*Bear case (write before Bull):*
- [Key risk grounded in prior analyses — cite specific data]
- [At least one quantifiable condition under which the thesis is wrong]

*Verdict:* [REMOVE / MONITOR / BUY — ACCUMULATE / BUY — MEASURED / BUY — CONVICTION]
[Explicit reasoning: how do the Numbers, Narrative & Catalyst, and Thesis strength together produce this verdict? Name which verdict dimensions are present and which are absent.]

*Invalidation:*
[Specific, observable developments that would make this thesis wrong and trigger reassessment or exit. Not "fundamentals deteriorate" — name specific metrics, events, or thresholds.]

---

## Self-Check

Before proceeding to Step 3, answer the following internally. Do not include these answers in your output — they are for your own verification only. If any answer is no, revise before proceeding.

- Have all questions Q1–Q11 been answered in full?
- Has the FULL Thesis file been re-read before writing the Synthesis — not just the hypothesis sections?
- Has the cross-section consistency check been performed — do the same figures appear consistently across Context, The Numbers, and this analysis? Has any discrepancy been resolved and the correct value stated?
- Is every management claim cited with a specific transcript reference?
- Are all guidance figures labeled as forward-looking and kept separate from historical actuals?
- Are all non-GAAP figures flagged, with the GAAP equivalent noted where available?
- Have all open questions from The Numbers been explicitly resolved or flagged as unresolved in Q5?
- Was the Bear case written before the Bull case?
- Does the Bear case cite specific data from prior analyses and include at least one quantifiable invalidation condition?
- Has the framing audit been performed — is the analysis free of systematic bullish or bearish bias? Does the Bear case receive equal rigor and prominence to the Bull case?
- Has the LOSER/TAILWIND conditional been applied correctly in Q11?
- Has `context_markets.md` been factored into the Synthesis — do prevailing macro conditions inform the verdict?
- Are all factual claims tagged `[CONFIRMED]`, `[ESTIMATED]`, or `[INFERRED]` with citations?
- Does the verdict name which dimensions (Numbers strength, Narrative, Catalyst) are present and which are absent — and trace the verdict tier to that assessment explicitly?

**Action:** Ask: *"The full Projection analysis has been written to the Thesis file. Do you approve the Synthesis above? Should I finalize and update the Stock Tracker?"*

**STOP. Wait for explicit user approval before proceeding to Step 3.**

---

## Step 3: Commit

The full Projection analysis was already written to `### The Projection` in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` during Step 2. Write the Synthesis block (Numbers / Narrative & Catalyst / Thesis) to `### Synthesis` in the same file if not already done.
3. Update `Stock_Tracker.md`:
   - Set **Phase** to `Complete`
   - Set **Status** to the verdict (REMOVE / MONITOR / BUY — ACCUMULATE / BUY — MEASURED / BUY — CONVICTION)
   - Set **Last Run** to today's date

**Action:** Ask: *"Do you approve these updates?"*

**STOP. Wait for explicit user approval before writing to any file.**

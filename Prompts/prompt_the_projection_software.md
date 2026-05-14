# Pass 2: The Projection — Software

## Role

You are conducting Pass 2: The Projection for **{TICKER}**, a software company navigating AI disruption. Your purpose is to read the most recent earnings call against the financial picture already established, assess whether the thesis is timely, and produce the final assessment. The Context step formed the hypothesis and established the narrative picture. The Numbers step tested it against the financials. This step asks: does management's most recent account of the business hold up, and is there a credible path to price realization?

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
- `context_markets.md` — Current macro conditions and prevailing narratives. Read before analyzing — macro context informs how you read the earnings call, not just the assessment.

**Conditional**
- `context_ai_supply_chain_index.md` — Read if `{TICKER}` has an `AI SC` Sector Theme tag. Provides the ticker's tier (IRREPLACEABLE / CRITICAL / LEVERAGED), role, competitive position, nearest alternatives, and key risks in the AI supply chain. Load this by default.
- `context_ai_supply_chain.md` — Full encyclopedia. Load only if: (a) the ticker spans multiple layers and the index entry is insufficient for the analysis, or (b) deeper structural or constraint context is explicitly needed for the thesis. Do not load by default.

**Data check:** Confirm `{TICKER}_earnings_remarks.md` and `{TICKER}_earnings_qa.md` are present and non-empty. If either is missing, stop and alert before proceeding.

---

## Step 2: Analyze

> **Output mode — read before starting.**
> Write the full analysis directly to `### The Projection` in the Thesis file **as you generate it** — Q1 through Q7, then the Synthesis. Do **not** output the full analysis text in the chat window. When all sections are complete, present **only the Synthesis block** in the chat for review. This keeps the context window lean and prevents autocompaction from disrupting the analysis mid-flow.

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
- **Narrative pre-check:** The narrative pre-check from Context is your entry point for the catalyst assessment. The question is not whether narrative momentum exists — that was answered in Context — but whether the earnings call changed that picture. State the update explicitly in Q7.
- **Cross-section consistency (required before Synthesis):** Before writing the Synthesis, verify that the same figures appear consistently across Context, The Numbers, and the earnings call analysis. Any figure appearing with different values across sections must be resolved — state which value is correct and why.
- **Bear before Bull (required):** Write the Bear scenario before the Bull scenario. The Bear scenario must use only facts from prior analyses, cite specific data, and include at least one quantifiable condition under which the thesis is wrong. Vague bear cases ("macro uncertainty," "competitive pressure") are insufficient.
- **Assessment dimensions:** The expected value assessment draws on three dimensions — not catalyst alone. Consider:
  - *Thesis/Numbers strength:* What does the financial picture say about the quality and durability of the business? A weak thesis cannot rescue an unattractive price.
  - *Narrative:* Is a story forming around this stock, from whom, and is it moving in the right direction?
  - *Catalyst:* Is there a credible path to price realization, and over what timeframe?

  These three together inform the Expected Value assessment — expressed as a narrative framing: is this a dollar for 70 cents, a dollar for a dollar, or a dollar for 120 cents? A strong thesis with no narrative or near-term catalyst means the value may be real but unrealized for an extended period — name that honestly. A broken or materially weakened thesis means the price likely overstates intrinsic value — name that too. When genuine uncertainty makes a confident conclusion impossible, say so explicitly and name the specific reasons why. "We have no idea" is a valid answer.

---

### Output Format

All questions below constitute the full Pass 2 output. Every question must be answered. Q1 through Q7 will be committed to `### The Projection` in the Thesis file. The Synthesis block will be committed to `### Synthesis`.

---

#### {TICKER}: The Projection

*Sources: `{TICKER}_earnings_remarks.md`, `{TICKER}_earnings_qa.md`*

**Q1. Which of the two calls is more strategically material, and why?**
State this before analyzing. Identify which call covers full-year results and annual guidance vs. which is an incremental quarterly update. This framing applies throughout the analysis — where the two calls diverge in data, tone, or emphasis, it matters which carries more weight.

**Q2. Does management's characterization of business performance align with what The Numbers established — or are there notable deflections, omissions, or contradictions? Where does the call add context that the financial statements couldn't?**
Cite specific excerpts from both calls. Note where they differ from each other and where either diverges from the findings in The Numbers. What did management say that the financials could not have told us? Pay particular attention to: (a) how management characterizes AI's impact on the business — threat, opportunity, or both — and whether this is backed by specific metrics or framed in general terms; (b) any AI monetization or adoption progress not visible in the financial statements — pricing changes, customer wins, product adoption rates.

**Q3. What is management saying about the path forward — guidance figures, growth targets, margin trajectory? Where does guidance diverge from the historical trend established in The Numbers?**
Summarize explicit forward guidance figures. Label all as forward-looking. Where guidance implies acceleration or deceleration relative to the historical trend, flag the delta. Where management cites adjusted figures, check whether the GAAP equivalent is disclosed. On AI investment specifically: is spending expected to compress or expand margins near-term, and over what timeframe does management expect a return?

**Q4. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
Compare tone and emphasis between the two calls. What was foregrounded in the earlier call that is now absent? What is new? Tone shifts often surface risks before they appear in the financials.

**Q5. For each open question listed at the end of The Numbers — was it addressed on either call?**
List every open question from The Numbers. For each: (a) was it addressed on either call? (b) cite what was said directly. (c) does the answer strengthen, weaken, or leave the thesis unchanged? Any item not addressed must be flagged as unresolved — none carried forward silently.

In addition, the following must be explicitly tracked regardless of whether they appeared in the open questions list:

*Risk side:* (a) Is AI disrupting the core business in ways management is not fully disclosing — seat reductions, churn, or pricing pressure from consumption/agent-based alternatives? (b) Is AI investment compressing margins with no demonstrated ROI timeline?

*Upside side:* (c) Are AI features driving measurable revenue uplift — new pricing tiers, attach rates, or expansion revenue? (d) Is net revenue retention improving, or does management's account suggest AI monetization is accelerating ahead of current financials?

**Q6. What are analysts most concerned about and most excited about — and what does the Q&A reveal that the prepared remarks don't?**
Surface the substantive content — what analysts are probing, what they are endorsing. Specific citation required for each significant exchange. Do not summarize generically. Prepared remarks are managed; Q&A responses are less so. Where management's tone, specificity, or framing shifts under questioning, note it. Hedges introduced only under questioning, figures disclosed only when pressed, and topics deflected rather than answered are all informative.

**Q7. Did the earnings calls strengthen or undermine the narrative and catalyst picture established in Context? What is the specific upcoming event catalyst that could drive a rerating in 3–6 months — what is it, when does it occur, and is it management-flagged or inferred?**
Referencing the narrative pre-check from Context, assess: did the earnings call change it — and how? If no narrative pathway was identified in Context, does the call introduce one, or does the prior hold? State the updated conclusion explicitly.

If a catalyst exists: name it, state the expected window, and assess its credibility. If management flagged it, cite directly. If inferred from context, label as inferred. If no near-term event catalyst exists, state that explicitly — it is an input to the assessment, not a failure of analysis.

**On earnings as a catalyst:** The next scheduled earnings print qualifies as a catalyst only if it will specifically resolve something — a turnaround quarter whose results will confirm or deny the thesis, a metric management explicitly committed to disclose, a product ramp whose first revenue will appear in those results, or a situation where the trend has been so volatile that the next data point is genuinely thesis-critical. It does not qualify simply because it will provide more data in the same direction. If the picture is unlikely to change materially in the next quarter — the business keeps doing what it does, the overhang persists, guidance will still be opaque — then next earnings is a data gate, not a catalyst, and should not be used to justify a BUY assessment.

---

> **Web fetches — backstop only.** If questions remain unresolved across the entire analysis — Context, The Numbers, and the earnings call — a targeted web search may be warranted. Cap at 3. Skip entirely if nothing is genuinely unresolved. This is not a routine step.

---

##### Synthesis
*Read the full Thesis file again before writing this section. Cross-section consistency check required before proceeding.*

**Numbers**
What does the financial picture contribute to the thesis? Draw on The Numbers analysis — do not re-analyze. Note only what the earnings call changed or confirmed materially. 2–3 sentences: what the financial analysis conclusively established about earnings quality, durability, and risk.

**Narrative & Catalyst**
What is the narrative picture, updated by the earnings call? Is a story forming around this stock — from whom, and is it moving in the right direction? Assess the catalyst: event-driven (what, when), narrative-driven (momentum, source quality, visibility factor), or neither. 2–3 sentences: narrative strength, what is recognized vs. what isn't, catalyst timing.

**Scenario**
What scenario does the current price appear to embed across all three passes — and does the final picture confirm, deny, or complicate it?

**Reflexivity**
Where does this company sit in the reflexivity cycle (Soros)? Assess the negative loop explicitly: AI fear → price drop → multiple compression → talent/customer confidence erosion → weaker results → more fear. Is this loop already in motion — and if so, how far has it progressed? Is there evidence of reversal, or is it self-reinforcing?

**AI Disruption Position**
Where does this company sit on the AI disruption spectrum — defending a legacy moat, actively transforming via AI, or both? What evidence from all three passes supports that position, and what would signal that the disruption risk is accelerating or that the monetization opportunity is materializing?

**Thesis**
Final reconciliation of the hypothesis across all three steps — how has the evidence changed, confirmed, or complicated the preliminary hypothesis from Context?

*Bear scenario (write before Bull):*
- [Key risk grounded in prior analyses — cite specific data]
- [At least one quantifiable condition under which the thesis is wrong]

*Bull scenario:*
- [Key point grounded in prior analyses — cite specific data]
- [At least one quantifiable condition under which the thesis is right]

*Expected Value:*
Is this a dollar for 70 cents, a dollar for a dollar, or a dollar for 120 cents? Name which assessment dimensions (Numbers strength, Narrative, Catalyst) are present and which are absent, and explain how they together produce this conclusion. Support with figures but the conclusion is qualitative. If the honest answer is "we have no idea," state it explicitly with specific reasons why.

*Pre-profitability note (if applicable):* Frame the expected value around the probability of the business model working — what is the path to self-sustaining profit, and how much of that path is already reflected in the current price? Do not anchor the EV on EPS-derived targets.

**Invalidation**
Specific, observable developments that would make this thesis wrong and trigger reassessment or exit. Not "fundamentals deteriorate" — name specific metrics, events, or thresholds.

---

## Self-Check

Before proceeding to Step 3, answer the following internally. Do not include these answers in your output — they are for your own verification only. If any answer is no, revise before proceeding.

- Have all questions Q1–Q7 been answered in full, and has the Synthesis been completed?
- Has the FULL Thesis file been re-read before writing the Synthesis — not just the hypothesis sections?
- Has the cross-section consistency check been performed — do the same figures appear consistently across Context, The Numbers, and this analysis? Has any discrepancy been resolved and the correct value stated?
- Is every management claim cited with a specific transcript reference?
- Are all guidance figures labeled as forward-looking and kept separate from historical actuals?
- Are all non-GAAP figures flagged, with the GAAP equivalent noted where available?
- Have all open questions from The Numbers been explicitly resolved or flagged as unresolved in Q5?
- Was the Bear scenario written before the Bull scenario?
- Do the Bear and Bull scenarios receive equal rigor, equal data citation standards, and equal specificity?
- Has the framing audit been performed — is the analysis free of systematic bullish or bearish bias?
- Has `context_markets.md` been factored into the Synthesis — do prevailing macro conditions inform the assessment?
- Are all factual claims tagged `[CONFIRMED]`, `[ESTIMATED]`, or `[INFERRED]` with citations?
- Is the Synthesis complete across all dimensions — Numbers, Narrative & Catalyst, Scenario, Reflexivity, AI Disruption Position, and Thesis?
- Does the Expected Value assessment name which dimensions (Numbers strength, Narrative, Catalyst) are present and which are absent — and explain how they together produce the conclusion?
- Have the Reflexivity and AI Disruption Position dimensions been answered with specific evidence from all three passes — not generic assertions?
- Have the Q5 risk-side and upside-side tracking items been explicitly addressed?

**Action:** Ask: *"The full Projection analysis has been written to the Thesis file. Do you approve the Synthesis above? Should I finalize and update the Stock Tracker?"*

**STOP. Wait for explicit user approval before proceeding to Step 3.**

---

## Step 3: Commit

The full Projection analysis was already written during Step 2 — Q1–Q7 to `### The Projection` and the Synthesis block to `### Synthesis`. No further writing to the Thesis file is needed.

Update `Stock_Tracker.md`:
   - Set **Phase** to `Complete`
   - Set **Last Run** to today's date

**Action:** Ask: *"Do you approve these updates?"*

**STOP. Wait for explicit user approval before writing to any file.**

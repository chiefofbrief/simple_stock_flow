# Prompt Rewrite Session — AI Versions
**Session date:** 2026-05-13
**Files edited:** 
- `Prompts/prompt_the_context_ai.md` — COMPLETE
- `Prompts/prompt_the_numbers_ai.md` — COMPLETE
- `Prompts/prompt_the_projection_ai.md` — COMPLETE

**Status:** All three AI prompt files fully edited and verified.

---

## ABSOLUTE RULES

- NO edits that were not explicitly agreed in this session
- Supply chain candidates: compact list at end of each relevant section — `Company (Ticker) — Role` — NO tracker cross-referencing, NO commentary on whether tracked, NOT embedded in thesis prose
- Every question below is verbatim unless marked REWRITTEN
- Where a question is marked KEEP, copy it exactly from the current prompt
- Do NOT touch non-AI prompt files — changes to those are a separate session

---

## CONSISTENT THESIS STRUCTURE ACROSS ALL THREE PASSES

This is the single most important structural decision. The thesis block uses the same four dimensions across all three passes. What changes is the *depth* of each dimension, not the structure.

**Four dimensions (all passes):**
1. **Numbers** — financial picture (anticipated / established / confirmed)
2. **Narrative & Catalyst** — narrative picture and path to price realization
3. **Scenario** — what scenario does the current price embed, and does the evidence confirm it?
4. **Thesis** — conviction statement (preliminary / updated / final EV verdict)

**How "Thesis" evolves across passes:**
- Context: preliminary conviction statement — what evidence would confirm or break it?
- Numbers: updated conviction statement — strengthened, complicated, or weakened? What remains unresolved?
- Projection: final EV verdict — Bear scenario → Bull scenario → *Expected Value:* (the "dollar for dollar" verdict). Bear and Bull are sub-components feeding the EV.

**"Open questions" is NOT a thesis dimension.** It is a handoff item that follows the thesis block as a standalone item — analogous to Q20 following Q19 in Context.

**Additional blocks in Projection Synthesis only:**
- **Reflexivity + AI Lifecycle** — sits BEFORE Thesis (it informs the EV judgment)
- **Invalidation** — sits AFTER Thesis

**The label "Expected Value" lives INSIDE the Thesis block** (as the verdict sub-section: `*Expected Value:*`), NOT as a section header. The section header is "Thesis" across all passes.

---

## CONTEXT PASS — `prompt_the_context_ai.md`

### Section 1: Sentiment Landscape
**Status: KEEP ALL — no changes**

- Q1: What is the mainstream narrative?
- Q2: What is the counter-narrative from Reddit/retail?
- Q3: Where does sentiment sit in the cycle?

---

### Section 2: Analyst Consensus
**Status: KEEP ALL — no changes**

- Q4: Where does analyst consensus sit relative to current price, and how has conviction trended?
- Q5: What does recent grade action signal?

---

### Section 3: Price & Earnings
**Status: Q6–Q9 KEEP, Q10 REMOVED**

- Q6: How does the current price compare to historical levels? *(KEEP verbatim)*
- Q7: What are the long-term price and earnings trends and volatility? *(KEEP verbatim)*
- Q8: What are the short-term price and earnings trends? *(KEEP verbatim)*
- Q9: Has price appreciation been validated by earnings growth, or is price running ahead of fundamentals? *(KEEP verbatim)*
- ~~Q10: What scenario does the current price appear to embed?~~ **REMOVED**

---

### Section 4: MD&A
**Status: REVERTED — Q13+Q15 combination was reconsidered and rejected. All body texts kept verbatim. Old Q16 becomes new Q15 — output format changed. Q10 removed from Section 3 shifts all Section 4 numbers by one.**

Final numbering:
- Q10 *(was Q11)*: What drove results this quarter? *(KEEP verbatim)*
- Q11 *(was Q12)*: What was the segment breakdown? *(KEEP verbatim)*
- Q12 *(was Q13)*: Where is management guiding the business? *(KEEP verbatim)*
- Q13 *(was Q14)*: What risks and headwinds does management flag? *(KEEP verbatim)*
- Q14 *(was Q15)*: What is management saying about the path from investment to revenue? *(KEEP verbatim)*
- Q15 *(was Q16 — output format changed)*: Who are the major customers, suppliers, and competitors?
  - Keep the analytical body text from original Q16 (who are customers/concentration, suppliers/sole-source, competitors)
  - DROP the "flag those explicitly / is it publicly traded / AI SC candidate" language
  - ADD output format block embedded within the question (not a separate section header):
    ```
    Company (Ticker) — Role
    Company (Ticker) — Role
    ```
  - "No commentary. No tracker cross-referencing."

---

### Section 5: Narrative Pre-check
**Status: REWRITTEN. Old Q17–Q23 replaced by 3 questions. AI question goes LAST. Final numbering Q16–Q18.**

- Q16 *(was Q18)*: Is there a near-term catalyst narrative? *(body verbatim from old Q18)* + tail: "If no near-term catalyst exists, state that explicitly."
- Q17 *(was Q19)*: Is there a long-term quality narrative? *(body verbatim from old Q19)* + tail: "If no long-term narrative exists, state that explicitly."
- Q18 *(was Q17, AI version only)*: Is the AI tailwind structural or narrative-driven, and is that position already priced in?
  - **Body text:** Keep ONLY: "These are two different questions — thesis confidence and investment attractiveness are not the same thing."
  - No sub-bullets.

**Absence check (old Q23):** Folded into Q16 and Q17 as one-line tails. NOT a standalone question.

**REMOVED from this section** (moved to Synthesis in The Projection):
- ~~Reflexivity cycle~~
- ~~Perez AI lifecycle~~
- ~~Bubble lens~~
- ~~Underestimation lens~~

---

### Section 6: Preliminary Hypothesis
**Status: Four dimensions. "Thesis Strength" → "Thesis". No SC Candidates block — SC list is in Q15. Final numbering Q19–Q20.**

Four dimensions of the preliminary thesis:
1. Numbers
2. Narrative & Catalyst
3. Scenario
4. Thesis *(was "Thesis Strength")*

- Q19 *(was Q24)*: State the preliminary hypothesis. *(across the four dimensions above)*
- Q20 *(was Q25)*: What are the Pass 1 focus questions? *(separate question, not a dimension)*

---

## THE NUMBERS PASS — `prompt_the_numbers_ai.md`

### Section naming
- **Part A** renamed to **Metrics**
- **Part B** renamed to **Synthesis**
- These renamings apply throughout the prompt including Analytical Guidelines

### Section Order
**New order:**
1. Metrics (10 metrics — with TL;DR instruction)
2. Targeted Searches (includes SC network grep — always run)
3. Accounting (merged single section — checklist + 3 questions)
4. Synthesis (4 questions for AI, 3 for non-AI)
5. Updated Thesis (one block — four dimensions)
6. Open questions for Pass 2 (standalone, follows Updated Thesis — NOT a dimension)

---

### Metrics (was Part A)
**TL;DR: ONE instruction in the Metrics section header — applied to all metrics, not repeated per-metric.**

Instruction text: *"Close each metric with a TL;DR of two sentences: (1) what this metric confirms or flags about the business; (2) the investment implication."*

Do NOT add this instruction individually at the bottom of each metric block.

Metrics (all 10, order unchanged):
1. Revenue
2. Operating Margin
3. Operating Cash Flow
4. Free Cash Flow
5. OCF / Net Income
6. Working Capital
7. Operating Leverage
8. Capital Expenditures & D&A
9. Debt Profile
10. ROIC

---

### Targeted Searches
**Status: Replaces both old "Targeted Searches" and "Mandatory Supply Chain Network Search" (which is removed as a separate section). Now one combined section with two parts:**

**Part 1 — Flag-driven searches:** Driven by flags raised in Metrics. Not a predetermined list. Run for each flag. State explicitly if no flags warranted investigation.

**Part 2 — Supply chain network (always run regardless of Metrics flags):** Grep `{TICKER}_notes.md` and `{TICKER}_mda.md` for:
- `customer` / `concentration`
- `supplier` / `vendor` / `sole source` / `sole-source`
- `advance payment` / `purchase commitment`
- `related party`
- `competi`

**Why this lives in Targeted Searches (not a standalone question):** `{TICKER}_notes.md` and `{TICKER}_mda.md` are GREPPED not read in full. Without an explicit always-run block in Targeted Searches, the LLM will not search them for SC entities. A standalone question at the end of the pass is insufficient because those files are never opened holistically.

**Output format for SC entities found:**
```
Company (Ticker) — Role
Company (Ticker) — Role
```
No commentary. No tracker cross-referencing.

---

### Accounting — MERGED SINGLE SECTION
**Status: Replaces both "Mandatory Accounting Checklist" and "Accounting Analysis." One section.**

**Five-category checklist — KEEP VERBATIM AS IS:**
1. Revenue Recognition
2. Expense Recognition & Cost Capitalization
3. Balance Sheet & Asset Valuation
4. Cash Flow & Working Capital
5. Non-GAAP & Adjusted Earnings

*(Each category retains its existing assessment instruction and format. No changes to the checklist itself.)*

**Three questions — ADDED after the checklist (replaces old 4 Accounting Analysis questions):**
1. What do the footnotes/MD&A reveal that is material and not captured in the financial statements?
2. How do these findings impact the analysis — do they confirm, complicate, or contradict any conclusion from Metrics?
3. What is materially missing or unverifiable from available disclosures — and what is the risk of that gap?

---

### Synthesis (was Part B)
**Status: MOVED to after Accounting. REPLACES old Part B (10 questions). 4 questions for AI, 3 for non-AI.**

Synthesis synthesizes BOTH Metrics AND Accounting findings together. This is why it sits after Accounting.

**Questions:**
1. Do the financials indicate that earnings/net income as a valuation anchor (P/E) is fair or misleading — and if misleading, what metric better captures economic reality?
2. What do the metrics and accounting findings together reveal about the quantifiable downside — what breaks the earnings case and at what price does the stock reprice?
3. What structural upside is not yet visible in reported financials or priced into the current multiple?
4. *(AI version only)* Is the investment cycle self-sustaining without external capital, and what does the answer imply for durability of the thesis?

---

### Updated Thesis
**Status: ONE block. Four dimensions — same structure as Context Q19 and Projection Synthesis. "Thesis" not "Thesis Strength." Followed by Open questions as a standalone item.**

Instruction: *"First state whether the financial data confirms, contradicts, or complicates the preliminary thesis and where specifically. Then state the updated thesis across the same four dimensions: Numbers / Narrative & Catalyst / Scenario / Thesis. Close with an explicit statement on whether earnings growth is real, durable, and sustainable, and at what price and under what scenario the thesis breaks."*

**Four dimensions:**
1. Numbers — what the financial picture now establishes
2. Narrative & Catalyst — updated or carried forward (say explicitly if unchanged)
3. Scenario — what scenario do the financials support, and does it match the price?
4. Thesis — updated conviction statement (strengthened/complicated/weakened, what remains unresolved)

**Open questions for Pass 2** — standalone item, follows Updated Thesis, separated by `---`. NOT a dimension of the thesis. Format:
> **Open questions for Pass 2:** [specific unresolved questions the earnings call must address]

---

## THE PROJECTION PASS — `prompt_the_projection_ai.md`

### Section Structure
**New structure:** ONE section, 8 questions in logical sequence. No sub-section headers.

**The 8 questions:**
1. Which of the two calls is more strategically material, and why?
2. Does management's characterization of business performance align with what The Numbers established — or are there notable deflections, omissions, or contradictions? What do the calls add that the financial statements couldn't?
3. What is management saying about the path forward — guidance figures, growth targets, margin trajectory — and where does this diverge from the historical trend established in The Numbers?
4. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?
5. For each open question from The Numbers — was it addressed on either call? *(Answer each open question explicitly: addressed / partially addressed / not addressed, and what was revealed.)*
6. What are analysts most concerned about and most excited about — and what does the Q&A reveal that the prepared remarks don't?
7. Did the earnings calls strengthen or undermine the narrative and catalyst picture established in Context? What is the specific upcoming event catalyst that could drive a rerating in 3–6 months — what is it, when does it occur, and is it management-flagged or inferred?
8. Who are the major customers, suppliers, and competitors surfacing in the earnings calls? *(Compact list format — same as other passes. Sources: transcripts, which are read in full.)*

**Q5 risk/upside tracking block:** KEPT verbatim — it is doing useful analytical work. Always-run regardless of open questions list.

**"On earnings as a catalyst" note:** KEPT verbatim under Q7.

**Q8 — SC candidates in Projection:** Standalone question placed after Q7, before Synthesis. Sources are earnings call transcripts which are READ IN FULL (different from Numbers where footnotes are grepped). Same compact list format:
```
Company (Ticker) — Role
Company (Ticker) — Role
```
No commentary. No tracker cross-referencing.

---

### SC Question Mechanism — Summary Across All Passes (AI prompts only)

SC candidates are an AI supply chain concept and do not appear in the non-AI prompts at any pass.

| Pass | Mechanism | Why |
|---|---|---|
| Context Q15 | Standalone question | MD&A excerpts are read in full |
| Numbers Targeted Searches | Always-run grep block within Targeted Searches | Notes/MDA files are grepped not read — standalone question at end would be missed |
| Projection Q8 | Standalone question | Transcripts are read in full |

---

### Synthesis — end of Projection
**Status: KEEP structure. Five blocks plus Reflexivity + AI Lifecycle (AI only). "Supply chain candidates" block REMOVED.**

**Six blocks (AI version):**

**1. Numbers**
What does the financial picture contribute to the thesis? Draw on The Numbers — do not re-analyze. Note only what the earnings call changed or confirmed materially. 2–3 sentences.

**2. Narrative & Catalyst**
Narrative picture updated by the call. Catalyst assessment. 2–3 sentences.

**3. Scenario**
What scenario does the current price appear to embed across all three passes — and does the final picture confirm, deny, or complicate it?

**4. Reflexivity + AI Lifecycle** *(AI version only)*
Where does this company sit in the reflexivity cycle (Soros) and the AI technology lifecycle (Perez)? What evidence from all three passes supports that position, and what would signal a reversal in either framework?
*(These were two separate subsections. Now one block, two lenses, one answer. No "(AI supply chain version only)" annotation needed — this IS the AI prompt.)*

**5. Thesis**
Final reconciliation across all three steps.
- Bear case written FIRST
- Bull case
- *Expected Value:* verdict — "dollar for dollar" framing (is this a dollar for 70 cents, a dollar for a dollar, or a dollar for 120 cents?)
- Pre-profitability note (if applicable)

**6. Invalidation**
Specific, observable, dated conditions that make the thesis wrong and trigger reassessment. Not "fundamentals deteriorate" — name specific metrics, events, or thresholds.

---

## WHAT IS NOT CHANGING

- The overall thesis header format (Classification, Phase, Last Updated, source note)
- Section 1 questions (verbatim, no touch)
- Section 2 questions (verbatim, no touch)
- Section 3 questions Q6–Q9 (verbatim, Q10 deleted only)
- Section 4 Q11 and Q12 (verbatim, no touch)
- Section 4 Q14 (verbatim, no touch)
- The five accounting checklist category names and their assessment format
- The Preliminary Hypothesis section structure (just "Thesis Strength" → "Thesis")
- The Synthesis "dollar for dollar" expected value framing
- The Invalidation section format
- The GEMINI.md workflow references and source file instructions
- Any instructions about CONFIRMED/INFERRED/ESTIMATED tagging
- Any instructions about peer comparison (AMAT etc.) in Numbers
- "Expected Value" as the LABEL for the verdict — it lives inside the Thesis block as `*Expected Value:*`, not as a section header

---

## SEQUENCE FOR WRITING

1. ~~Edit `prompt_the_context_ai.md` first~~ **COMPLETE**
2. ~~Edit `prompt_the_numbers_ai.md` second~~ **COMPLETE**
3. ~~Edit `prompt_the_projection_ai.md` third~~ **COMPLETE**
4. Do NOT touch non-AI prompt files in this session

---

## NON-AI PROMPT CHANGES — `prompt_the_context.md`

### Section 3: Price & Earnings — Q10/Q11 redundancy fix

**Problem:** Q10 `[TAILWIND]` and Q11 (both types) both ask the same core question — compare price trajectory against earnings trajectory. For a TAILWIND stock they are identical in substance. For a LOSER stock, Q10 is skipped and Q11 handles it alone.

**Decision:** Remove Q10. Fold TAILWIND-specific framing into Q11 as a conditional one-liner. Keep Q11's existing body text verbatim — it is neutral and strong. Only update the question title and add symmetric TAILWIND/LOSER conditionals that do not assume a direction.

**New Q11 (replaces both Q10 and Q11):**

> **Q11. What does the price/earnings relationship reveal?**
> Compare the price trajectory against the earnings trajectory directly — where are they diverging, converging, or moving in sync, and by how much? `[TAILWIND]` Has earnings growth validated the price appreciation — or is price running ahead of what the business has delivered? `[LOSER]` Is the price decline tracking real earnings deterioration — or is there a disconnect between the market's judgment and the underlying business? This is the central conclusion the preceding questions build toward.

**Note:** The `[TAILWIND]` and `[LOSER]` conditionals are symmetric and open — neither assumes an answer. The correlation note that follows Q11 in the current prompt should be kept verbatim.

**Renumbering effect:** Q10 removed; old Q11 becomes new Q10. All subsequent questions in Section 3 (if any) shift down by one. Section 4 onwards is unaffected — check numbering on edit.

---

## GENERAL PRINCIPLES ESTABLISHED DURING THIS SESSION

**Question body text:** Acceptable — even long — if it helps apply the question (adds analytical direction, flags edge cases, calibrates interpretation). Bad when it limits the question (narrows to specific mechanisms, lists exhaustive sub-questions that crowd out other valid interpretations). When reviewing other prompts: flag any body text that looks like it limits rather than opens the question.

**No AI-only annotations within the AI prompt:** Do not add `*(AI supply chain version only)*` or similar labels within the AI prompt files — the prompt IS the AI version. Such labels belong only in shared/combined prompt files if they exist.

**Naming consistency:** Section names used in Analytical Guidelines, Self-Check, and Output Format must match the actual section headers. When a section is renamed, grep the full prompt for stale references.

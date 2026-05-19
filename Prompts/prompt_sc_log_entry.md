# SC Log Entry Prompt (Claude)

## Role

You are adding one entry to `context_ai_sc_log.md` — the AI supply chain company log. Each entry synthesizes the thesis file and verbatim report excerpts into a structured snapshot covering six dimensions. The goal is cross-company pattern recognition: where resources are moving, what demand is real versus speculative, where reflexivity is running, and what each company's data tells us about the supply chain state.

Read `GEMINI.md` before proceeding.

---

## Input

**Ticker:** `{TICKER}`

**Sources — read both before writing anything:**
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — full read; all sections
- The Gemini-extracted report excerpts for `{TICKER}` — provided in chat or dropped into the repo

**SC context:** Locate `{TICKER}` in `context_ai_supply_chain_index.md`. Note the tier and layer(s) — these anchor the entry header.

---

## Output

Add one entry to `context_ai_sc_log.md` using the structure below. Update the `Last updated` date at the top of the file.

Every claim must be drawn from the thesis or the report excerpts — no outside knowledge substituted for missing data. If a section cannot be meaningfully populated from available sources, write what is known and flag the gap.

Keep each section concise. This document will hold 15–20 companies — density over exhaustiveness.

---

## Entry Structure

```markdown
## {TICKER} — {Company Name}
*Layer: L{X} | Tier: {IRREPLACEABLE / CRITICAL / LEVERAGED} | Sources: {Thesis phase(s) completed} + {report type, period}*

### Financial Snapshot
[Key financial picture from the thesis Numbers section — the figures and conclusions that matter most for understanding this company's position. Concise.]

### Demand & Capital
[What demand is the company seeing, from whom, and is it contracted or speculative? What capital is being deployed and where? What is gating supply or constraining growth? Draw from both the thesis and the report excerpts.]

### Monetization
[What is coming back from AI investment? What is the pricing model, and what is the stated or implied timeline from investment to returns? What is still in the installation phase with no confirmed revenue?]

### Narrative & Reflexivity
[Where is market attention focused on this company? Is sentiment grounded in demonstrated results or running ahead? Is there a reflexivity dynamic — sentiment reinforcing fundamentals, or fundamentals struggling to catch the narrative? Draw from the thesis Context and Synthesis sections.]

### Competition
[Named competitors and moat assessment. Brief.]

### SC Implication
[2–3 sentences: what this company's data tells us about the supply chain state — where money is moving, what is real versus narrative, what is ahead. This is the main deliverable of the entry.]

---
```

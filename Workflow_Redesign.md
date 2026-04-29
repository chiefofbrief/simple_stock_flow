# Workflow Redesign — Planning Notes

## Agreed Principles

1. **Core analytical questions stay mostly verbatim** — restructure the workflow and update framing where needed; high-leverage changes only.
2. **Two passes: The Numbers + The Narrative** — plus a Thesis Init step. Framing is directionally correct but permeable (earnings calls straddle both).
3. **LOSER vs. TAILWIND distinction is load-bearing** — primary analytical question differs by type and must be preserved in each pass.
4. **Catalyst check is mandatory in Synthesis** — two types: event catalyst (specific upcoming event) and narrative catalyst (frequency/framing of mentions can itself signal a rerating).
5. **ADVANCE / MONITOR / REMOVE** — MONITOR is default; burden of proof is on ADVANCE.
6. **Tracker updated once at end** — track current phase for navigation; verdict only written when full analysis is complete.
7. **No go/no-go gate at P&E** — stock is already in PIPELINE (Tier 1 criteria met); P&E is context-setting, not re-screening.

---

## Proposed Structure — Three Steps

---

### Step 0: Thesis Init
**Purpose**: Initialize the thesis file and run all data fetches.

**What happens:**
1. **Fetch everything first** — run all scripts before any analysis begins. Keep scripts separate (already built); orchestrate via a master script or prompt instruction. Scripts: `price.py`, `earnings.py`, `financials.py`, `footnotes.py`, `earnings_calls.py`, `research.py`.
2. **Create thesis file** — new 4-section structure (see below). No screening file; source is the PIPELINE row in the tracker.
3. **No user approval gate between fetch and analysis** — runs as one continuous session.

**Thesis file structure (new):**
```
# Investment Thesis: {TICKER}

### Synthesis          ← inserted at completion of Pass 2
### Context            ← from Step 0 (combines Discovery Signal + Price & Earnings)
### The Numbers        ← from Pass 1
### The Narrative      ← from Pass 2
```

**Context section — what it covers:**

Two things combined into one opening section:

1. **Discovery Signal** (from tracker row): Tag (LOSER/TAILWIND), tier signal, key metrics that triggered PIPELINE entry (vs_1Y, EPS YoY, spread, P/E, FCF), any notes from WATCHLIST, Added date. This is why we're analyzing this stock.

2. **Price & Earnings framing** (from price.py + earnings.py data): Not a gate — context-setting only. No PASS/FILTERED output. The questions need revisiting from the existing 9 (written for a standalone gate step) toward a more integrated, context-oriented set. Core content to preserve:
   - Price position and dislocation depth vs. history
   - Long-term and short-term trends — price AND earnings together (correlation is the signal for LOSERs)
   - **LOSER**: Is price tracking fundamental deterioration or overreacting? (correlation analysis = core question)
   - **TAILWIND**: Is the tailwind already priced in? Does current earnings justify price? (spread = core question)
   - P/E analysis (absolute floor; GAAP vs. adj gap if material)
   - Earnings reliability (pre-profitability, CV, beat/miss history, forward delta)
   - What does this frame for Pass 1? (closing question — what should we focus on?)

---

### Pass 1 — The Numbers
**Purpose**: Determine how the business's value aligns with its EPS and stock price. Understand what the business actually earns and whether those earnings are real.

**Data sources (all fetched in Step 0):**
- Financial statements: `{TICKER}_financial_analysis.md`
- Footnotes/MD&A: `{TICKER}_notes_mda.md`
- Earnings call prepared remarks (for targeted reference in step 2 only): `{TICKER}_earnings_remarks.md`
- `context_ai_supply_chain.md` — required for TAILWINDs with AI SC tag (supply chain thesis affects whether earnings growth is sustainable — this is a Numbers question, not only a Narrative question)

**Sequence within Pass 1:**
1. **Financials analysis** — full Part A metric analysis + Part B synthesis from `prompt_financials.md`, verbatim. Revenue, Op Margin, OCF, FCF, OCF/NI, Working Capital, Op Leverage, Capex/D&A, Debt profile.
2. **Targeted searches** — items flagged in step 1 that need explanation: search footnotes/MD&A and earnings call prepared remarks specifically for those items. Directed by what the financials raised, not a predetermined list.
3. **Independent footnotes analysis** — mandatory accounting checklist, regardless of what financials showed. Five categories from `prompt_footnotes.md` (verbatim):
   - Revenue Recognition
   - Expense Recognition & Cost Capitalization
   - Balance Sheet & Asset Valuation (goodwill, off-balance sheet, related party, Level 3)
   - Cash Flow & Working Capital
   - Non-GAAP Metrics & Adjusted Earnings (SBC, segment reporting, reclassifications)
4. **Wrap-up** — Bull case, Bear case, open questions for Pass 2.

**Primary question (differs by type):**
- **LOSER**: Does the business's financial health tell a different story than the price? Are earnings and FCF intact while price has dislocated? Is the decline in any metric temporary or structural?
- **TAILWIND**: Is earnings growth real, durable, and sustainable given the supply chain dynamics? Does what the company earns justify the price trajectory, and is that trajectory accelerating or decelerating?

---

### Pass 2 — The Narrative + Synthesis
**Purpose**: Understand how the world perceives this business, whether the thesis is timely, and produce the final verdict.

**Data sources (all fetched in Step 0):**
- Full earnings call (prepared remarks AND Q&A): `{TICKER}_earnings_remarks.md` + `{TICKER}_earnings_qa.md`
- News: `{TICKER}_research.md` (Perigon + FMP)
- Targeted web fetches (up to 3) for unresolved open questions
- `context_markets.md`
- `context_ai_supply_chain.md` (TAILWINDs with AI SC tag)
- All prior thesis sections (Context + Pass 1)

**Why the full earnings call belongs in Pass 2:**
Management's prepared remarks contain both financial commentary (referenced as needed in Pass 1) AND catalyst signals, forward guidance, narrative framing. Analyst Q&A is pure external perception. Both serve The Narrative. The full call is analyzed here — not split.

**Sequence within Pass 2:**
1. **Earnings call analysis** — from `prompt_earnings_calls.md`, verbatim:
   - Call weighting (which call is more strategically material)
   - Management characterization vs. prior analyses
   - Tone and language shifts; what's gone quiet
   - Catalyst signals and forward guidance language in prepared remarks
   - What analysts are probing and excited about (Q&A)
   - Open questions from Pass 1 — addressed or unresolved?
2. **News analysis** — driven by open questions from Pass 1 + earnings call. "News" is the right name here (cleaner than "Research"). From `prompt_research.md`, verbatim. Specific articles, sources, dates required. New material flagged.
3. **Web fetches** — for questions unresolved by news. Up to 3. Can be treated as a final sub-step.
4. **Synthesis** — from `prompt_synthesis.md`, verbatim, plus mandatory Catalyst Check (see below).

**Primary question (differs by type):**
- **LOSER**: Does the external picture confirm the dislocation? What specifically would cause sentiment to shift in 3–6 months? Is the stock accumulating narrative momentum that could itself trigger a rerating?
- **TAILWIND**: Is the AI/structural thesis intact per `context_ai_supply_chain.md`? Where are we in the reflexivity cycle — early accumulation or late exhaustion? What confirms or breaks the thesis in 3–6 months?

**Catalyst Check (mandatory addition to Synthesis):**

1. **Event catalyst**: Specific upcoming event — earnings print, legal resolution, product launch, regulatory decision, index inclusion, management change. Note the date or expected window.

2. **Narrative catalyst**: Is the stock accumulating narrative momentum that could itself drive a sentiment shift without a discrete event?
   - Frequency and trend of mentions in financial media and social channels
   - Framing alignment — does the dominant narrative match the thesis?
   - Source quality — retail noise vs. institutional interest vs. analyst initiation/upgrade
   - A stock appearing repeatedly in "undervalued/turnaround" narratives is accumulating conditions for a reflexive rerating even without a specific event.

If neither type yields something plausible in 3–6 months → **MONITOR**, not ADVANCE.

---

## Verdict System

Replaces PASS/BUY/HOLD/FAIL in tracker Status column. **Written once, at end of Pass 2 Synthesis.**

| Verdict | Meaning |
|---------|---------|
| **ADVANCE** | Affirmative case with evidence; catalyst identified within 3–6 months |
| **MONITOR** | Thesis intact but no near-term catalyst; stay in PIPELINE |
| **REMOVE** | Bear case dominates or thesis invalidated → DROPPED |

Tracker Phase column tracks current step (Thesis Init / The Numbers / The Narrative). Status (ADVANCE/MONITOR/REMOVE) only written when Pass 2 completes.

---

## What Changes vs. Old Structure

| Old | New |
|-----|-----|
| 6 steps | 3 steps |
| 6 thesis file sections | 4 sections (Context, The Numbers, The Narrative, Synthesis) |
| Separate Discovery Signal + P&E sections | Combined into single Context section |
| P&E is a go/no-go gate | P&E is context-setting; no gate |
| Footnotes = standalone step after Financials | Integrated into Pass 1 (targeted searches first, then mandatory checklist) |
| Earnings calls = standalone step | Full call in Pass 2 |
| Research = standalone step | News integrated into Pass 2 |
| Tracker updated after each step | Phase tracked throughout; verdict written once at end |
| Buy/Pass/Monitor | ADVANCE/MONITOR/REMOVE (MONITOR is default) |
| AI SC context = Pass 2 only | AI SC context required in both passes for TAILWINDs |

---

## Open Questions (to resolve in implementation)

- [ ] **Context section questions**: Finalize revised P&E question set. Start from existing 9, consolidate toward integrated context-oriented questions. LOSER/TAILWIND conditionals preserved; output framing shifts from PASS/FILTERED to analytical framing only.
- [ ] **Master fetch orchestration**: Shell script vs. prompt instruction? Shell script more reliable for error handling; prompt instruction requires no new code.
- [ ] **Tracker schema**: Phase column values (Thesis Init / The Numbers / The Narrative / Complete). "Last Run" column → rename "Last Updated"?
- [ ] **GEMINI.md Architecture table**: Update to reflect 3-step structure and new phase/section names.
- [ ] **Thesis Init prompt**: Full rewrite of `prompt_screening_completion.md`. Discovery Signal now pulls from tracker row; P&E questions revised.
- [ ] **Streamlining within prompts**: Which questions can be condensed without losing depth? Don't touch the accounting checklist. Synthesis checklist (11 questions) may be tightened.

---

## What Does NOT Change

- Core analytical questions in financials, footnotes, earnings calls, news/research, synthesis (verbatim or near-verbatim)
- The five-section Accounting Checklist in footnotes (mandatory checks stay mandatory)
- GEMINI.md analytical philosophy (Graham/Dodd/Soros, epistemic tagging, source citation, Devil's Advocate)
- PIPELINE/WATCHLIST/DROPPED tracker structure
- LOSER/TAILWIND investment types and their distinct analytical burdens
- Individual fetch scripts (price.py, earnings.py, financials.py, footnotes.py, earnings_calls.py, research.py)
- context_markets.md and context_ai_supply_chain.md as required context

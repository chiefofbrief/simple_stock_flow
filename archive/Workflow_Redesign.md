# Workflow Redesign

## Agreed Principles

1. **Core analytical questions stay mostly verbatim** — restructure the workflow and update framing where needed; high-leverage changes only.
2. **Three steps: Context + The Numbers + The Projection** — each step has a distinct purpose and data diet.
3. **LOSER vs. TAILWIND distinction is load-bearing** — primary analytical question differs by type and must be preserved in each step.
4. **Hypothesis-first** — Context step produces a preliminary, testable thesis. Pass 1 and Pass 2 stress-test it. The thesis is updated at each step; verdict written only at the end.
5. **Catalyst check is mandatory in Synthesis** — two types: event catalyst and narrative catalyst. No plausible catalyst in 3–6 months → MONITOR, not BUY.
6. **Verdict written once, at end of Pass 2** — Phase column tracks current step throughout.
7. **No go/no-go gate at Context** — stock is already in PIPELINE (Tier 1 criteria met); Context is framing, not re-screening. Narrative pre-check in Context sets a prior but does not end analysis.
8. **Token discipline** — footnotes and MD&A never fully loaded into Claude's context unless explicitly warranted. Targeted grep only.

---

## Model Division of Labor

| Task | Model |
|---|---|
| All data fetching (scripts) | Python scripts (run by Gemini in Step 0) |
| MD&A structured extraction | Gemini — only remaining extraction task |
| Reddit/social fetch | Script (`ticker_reddit.py`) |
| Earnings call Q&A questions extraction | Script (`earnings_calls.py`) |
| Analyst consensus fetch | Script (`analyst.py`) |
| All analysis and synthesis | Claude |
| Targeted grep searches (Pass 1) | Claude via bash tool |

Gemini's role in Step 0 is to run scripts and review verification output, plus one extraction task (MD&A excerpts). No open-ended analysis. Claude does all reasoning.

---

## Step 0: Setup (Gemini-led)

**Purpose**: Fetch all data and prepare files for Claude. No analysis.

**What Gemini does:**

1. **Run all fetch scripts** in order. Each script includes verification — it will fail loudly and print a per-ticker summary if any data does not come through. Gemini reviews the output and reports any failures before proceeding.

   | Script | Output | Notes |
   |---|---|---|
   | `price_earnings.py {TICKER}` | `{TICKER}_price.json` + `{TICKER}_earnings.json` | Run first; analyst.py loads price JSON |
   | `analyst.py {TICKER}` | `{TICKER}_analyst.md` | Price targets + grade actions |
   | `news.py {TICKER}` | `{TICKER}_news.md` | Perigon + FMP news combined |
   | `ticker_reddit.py {TICKER}` | `{TICKER}_social.md` | SocialVault ticker search |
   | `financials.py {TICKER}` | `{TICKER}_financial_analysis.md` | Pass 1 input |
   | `footnotes.py {TICKER}` | `{TICKER}_mda.md` + `{TICKER}_notes.md` | Pass 1 + MD&A extraction input |
   | `earnings_calls.py {TICKER}` | `{TICKER}_earnings_remarks.md` + `{TICKER}_earnings_qa.md` + `{TICKER}_qa_questions.md` | Analyst questions extracted automatically |

2. **Extract MD&A excerpts** — the one remaining Gemini extraction task. Structured extraction only, verbatim quotes with exact figures. No paraphrasing, no interpretation. Answer these five questions using direct quotes from `{TICKER}_mda.md`:
   - What drove results this quarter? (revenue, margins, segment performance — exact figures)
   - Segment breakdown — revenue and expenses by segment, verbatim with figures
   - Where is management saying the business is going? (guidance language, verbatim)
   - What risks or headwinds do they flag?
   - Critical Accounting Estimates section — verbatim extract
   - Output: `{TICKER}_mda_excerpts.md`

3. **Verification review**: Report which scripts succeeded and which failed. Do not hand off to Claude until all Context step files are confirmed present: `{TICKER}_price.json`, `{TICKER}_earnings.json`, `{TICKER}_analyst.md`, `{TICKER}_news.md`, `{TICKER}_social.md`, `{TICKER}_mda_excerpts.md`, `{TICKER}_qa_questions.md`.

**Output**: All data files on disk, ready for Claude. Gemini passes no analysis to Claude — only structured extracts and raw script outputs.

---

## Step 1: Context (Claude)

**Purpose**: Form a preliminary hypothesis before touching the financial statements. By this point the analyst has seen headlines, price action, and sentiment — the financial statements are used to verify or complicate that picture, not to build it from scratch.

**What Claude reads** (token load: low-medium):
- Discovery signal from tracker row: Tag (LOSER/TAILWIND), tier metrics that triggered PIPELINE entry, added date, any WATCHLIST notes
- `{TICKER}_mda_excerpts.md` — Gemini-extracted MD&A (excerpts only)
- `{TICKER}_qa_questions.md` — analyst Q&A questions only (what analysts are probing)
- `{TICKER}_news.md` — full read (already headlines and summaries by design)
- `{TICKER}_social.md` — Reddit/social extraction
- Price & earnings data from `price.py` / `earnings.py` outputs — includes EPS actuals, forward estimates, and beat/miss history
- Analyst consensus from `{TICKER}_analyst.md` — price targets (consensus, median, range, trend across time windows), analyst coverage count, recent grade actions (upgrades, downgrades, initiations)

**Analytical sequence:**

1. **Sentiment landscape**: News and analyst Q&A questions represent mainstream narrative — what the market is focused on and concerned about. Reddit typically carries a counter-narrative. Note the gap between the two explicitly.

2. **Analyst consensus**: Explicit standalone section — not buried in price/earnings framing.
   - Consensus price target vs. current price (implied upside/downside %) — use median as primary anchor; flag if coverage is thin or targets are stale
   - Target trend across time windows (last month vs. last quarter vs. last year avg) — direction of analyst conviction
   - Recent grade actions (upgrades, downgrades, initiations, maintains) — the momentum signal
   - This is the professional community's verdict. It feeds directly into the narrative pre-check and hypothesis.

3. **Price & earnings framing**: Context only, not a gate.
   - Price position and dislocation depth vs. history
   - Long-term and short-term price and earnings trends together
   - Overarching question for both types: **are actual earnings outpacing the price?**
     - **LOSER**: Is price tracking fundamental deterioration, or overreacting? Correlation between price and earnings is the core signal.
     - **TAILWIND**: Is the tailwind already priced in? Is there still spread between earnings trajectory and price?
   - P/E framing (absolute; GAAP vs. adj if gap is material)
   - Earnings reliability (pre-profitability, beat/miss history, forward delta)

4. **MD&A framing**: What does management say drove results and where are they going? What risks are foregrounded? Cross-reference segment breakdown against the price/earnings picture.

5. **Narrative pre-check**: Before forming the hypothesis — is there any narrative in news, Reddit, or analyst focus that supports or could support the thesis? Narrative support can take two forms, both valid:
   - **Near-term catalyst narrative**: An upcoming event or accumulating sentiment momentum that could drive a rerating in 3–6 months (retail, social, analyst initiation, event-driven)
   - **Long-term quality narrative**: Institutional consensus around undervaluation, dividend growth, or compounder thesis — no urgency, but a recognized investment case exists

   A stock with either form of narrative support passes the pre-check. What gets flagged is a stock with no narrative support of any kind — no analyst thesis, no Reddit interest, no institutional case. That is a true dead end and sets a strong prior toward MONITOR. Flag it explicitly if found; it does not end the analysis but is a significant prior entering Pass 1.

6. **Preliminary hypothesis**: Three-part structure — **Numbers** (anticipated financial picture based on price/earnings framing), **Narrative & Catalyst** (narrative pre-check conclusion and plausible path to price realization), **Thesis Strength** (overall conviction statement: what would confirm it and what would break it). Updated at each step; final reconciliation in Synthesis.

7. **Focus questions for Pass 1**: What specific things should the financials answer or challenge? Name them. These drive targeted searches in Pass 1.

**Output**: Context section of thesis file. Preliminary hypothesis stated explicitly. Pass 1 focus questions listed.

---

## Pass 1: The Numbers (Claude)

**Purpose**: Determine whether the business's financial health confirms or disputes the preliminary hypothesis. Understand what the business actually earns and whether those earnings are real.

**What Claude reads** (token load: medium):
- `{TICKER}_financial_analysis.md` — full read
- Targeted grep excerpts from `{TICKER}_notes.md` — Claude executes grep; only matched lines enter context
- Targeted grep excerpts from `{TICKER}_mda.md` — Claude executes grep; only matched lines enter context
- `context_ai_supply_chain.md` — required for TAILWINDs with AI SC tag

**Important**: The full footnotes file and full MD&A file are never loaded into Claude's context. Claude runs bash grep searches and receives only matching excerpts. This is the primary mechanism for controlling token load while preserving analytical depth.

**Analytical sequence:**

1. **Financials analysis** — full metric analysis from `prompt_financials.md` (verbatim). Revenue, Op Margin, OCF, FCF, OCF/NI, Working Capital, Op Leverage, Capex/D&A, Debt profile. At each flag or anomaly, note the specific term to grep in footnotes/MD&A.

2. **Targeted searches** — driven entirely by what the financials raised. Claude runs grep on footnotes and MD&A for flagged items. Not a predetermined list — directed by step 1 findings. Examples: goodwill impairment assumptions, revenue recognition policy, SBC treatment, off-balance sheet items, segment reclassifications, deferred revenue.

3. **Mandatory footnotes accounting checklist** — from `prompt_footnotes.md` (verbatim). Five categories checked regardless of what the financials showed. Each category addressed via targeted search, not full file read:
   - Revenue Recognition
   - Expense Recognition & Cost Capitalization
   - Balance Sheet & Asset Valuation (goodwill, off-balance sheet, related party, Level 3)
   - Cash Flow & Working Capital
   - Non-GAAP Metrics & Adjusted Earnings (SBC, segment reporting, reclassifications)

4. **Hypothesis check**: Does the financial picture confirm, dispute, or complicate the preliminary hypothesis from Context? Be explicit. Update the thesis.

5. **Wrap-up**: Bull case, Bear case, open questions for Pass 2.

**Primary question (differs by type):**
- **LOSER**: Does financial health tell a different story than the price? Are earnings and FCF intact while price has dislocated? Is any deterioration temporary or structural?
- **TAILWIND**: Is earnings growth real, durable, and sustainable? Does what the company earns justify the price trajectory, and is that trajectory accelerating or decelerating?

**Output**: The Numbers section of thesis file. Updated hypothesis. Explicit open questions for Pass 2.

---

## Pass 2: The Projection + Synthesis (Claude)

**Purpose**: Read the full earnings call against the financial picture already established. Assess whether the thesis is timely. Produce the final verdict.

**What Claude reads** (token load: medium-high):
- Full earnings call: `{TICKER}_earnings_remarks.md` + `{TICKER}_earnings_qa.md` — prepared remarks AND management Q&A responses, full read
- `context_markets.md`
- `context_ai_supply_chain.md` (TAILWINDs with AI SC tag)
- All prior thesis sections (Context + Pass 1)
- `{TICKER}_mda.md` — **optional full read** if significant open questions from Pass 1 require it and token budget permits; otherwise targeted grep only. Focus on Results of Operations and Liquidity; the file contains only MD&A (no footnotes boilerplate).

**News and Reddit**: Fully analyzed in Context step. Not repeated here. Pass 2 focuses on the earnings call and synthesis.

**Analytical sequence:**

1. **Earnings call analysis** — from `prompt_earnings_calls.md` (verbatim):
   - Call weighting (which quarter is more strategically material)
   - Management characterization vs. what financials showed
   - Tone and language shifts; what's been emphasized vs. gone quiet
   - Compare prepared remarks framing against MD&A excerpts from Context — where does the call emphasis diverge from the official filing?
   - Catalyst signals and forward guidance language
   - What analysts are probing in Q&A — cross-reference with questions noted in Context. Are analysts focused on the same things? What does that tell us?
   - Open questions from Pass 1 — addressed or unresolved?

2. **Web fetches** — backstop only, not a routine step. For questions unresolved across the entire analysis (Context + Pass 1 + earnings call). Cap at 3. Skip if nothing is unresolved.

3. **Synthesis + Catalyst Check** — from `prompt_synthesis.md` (verbatim), plus mandatory catalyst assessment:

   **Catalyst Check — two types:**

   - **Event catalyst**: Specific upcoming event — earnings print, legal resolution, product launch, regulatory decision, index inclusion, management change. Note the date or expected window. These are typically flagged in the earnings call or known from the calendar.

   - **Narrative catalyst**: Is narrative momentum accumulating that could itself drive a sentiment shift without a discrete event? Frequency and trend of mentions in news and Reddit, framing alignment with the thesis, source quality (retail noise vs. institutional vs. analyst initiation/upgrade). A stock appearing repeatedly in undervalued or turnaround narratives is accumulating conditions for a reflexive rerating. Note also: major, widely-followed stocks have higher narrative reactivity — positive news moves them faster and further than equally good news on an obscure name. This is itself a factor in timing.

   - The narrative pre-check from Context feeds directly here. If no narrative pathway was identified in Context, that prior holds unless the earnings call changed it.

   - No plausible catalyst of either type in 3–6 months → **MONITOR**, not BUY.

4. **Final hypothesis reconciliation**: How did the evidence across all three steps change, confirm, or complicate the preliminary hypothesis from Context? The verdict must follow from this explicitly — not from any single step in isolation.

**Primary question (differs by type):**
- **LOSER**: Does the external picture confirm the dislocation? What specifically would cause sentiment to shift in 3–6 months? Is narrative momentum accumulating?
- **TAILWIND**: Is the AI/structural thesis intact per `context_ai_supply_chain.md`? Where are we in the reflexivity cycle — early accumulation or late exhaustion? What confirms or breaks the thesis in 3–6 months?

**Output**: The Projection section + Synthesis section of thesis file. Verdict written. Tracker updated.

---

## Thesis File Structure

```
# Investment Thesis: {TICKER}

### Synthesis          ← written at end of Pass 2
### Context            ← written at end of Step 1
### The Numbers        ← written at end of Pass 1
### The Projection      ← written at end of Pass 2
```

Thesis is updated at the end of each step. Verdict is written only when Pass 2 is complete.

---

## Verdict System

Written once, at end of Pass 2 Synthesis only. Gate logic flows from catalyst check.

| Verdict | Meaning | Gate |
|---|---|---|
| **REMOVE** | Thesis invalidated; bear case dominates | Thesis broken at any point |
| **MONITOR** | Thesis intact; no narrative support of any kind and no near-term catalyst | No narrative, no catalyst |
| **BUY — ACCUMULATE** | Quality business at attractive price; long-term compounding thesis supported by institutional/analyst narrative; no near-term catalyst required | Long-term quality narrative present; financials confirm compounder characteristics |
| **BUY — MEASURED** | Thesis strong, near-term catalyst present; limited narrative momentum or stock visibility | Near-term catalyst present; narrative weak or stock obscure |
| **BUY — CONVICTION** | Thesis strong, near-term catalyst present, narrative momentum or market visibility aligned | Near-term catalyst + narrative or visibility working in our favor |

**Notes:**
- MONITOR is the default. Burden of proof is on any BUY verdict.
- Financial quality alone is not sufficient for a BUY. A strong financial picture with no narrative support of any kind → MONITOR.
- ACCUMULATE does not require a near-term catalyst but does require both confirmed financial quality (Pass 1) and an existing long-term narrative case (institutional consensus, undervaluation thesis, dividend compounder recognition). It is a buy-and-hold verdict, not a rerating play. Size accordingly — accumulate gradually, hold for years.
- MEASURED vs. CONVICTION is determined by market visibility and narrative reactivity. An obscure stock with a valid thesis and a near-term catalyst gets MEASURED. A widely-followed stock with the same picture gets CONVICTION because the machinery for sentiment response already exists and positive news will move it faster.
- Broadridge example: has institutional undervaluation narrative + compounder characteristics + analyst consensus → BUY — ACCUMULATE, not MONITOR. CRM with a near-term catalyst and the same financial picture → BUY — CONVICTION.

---

## Tracker Phase Column

| Phase value | Meaning |
|---|---|
| `Context` | Step 1 in progress or complete |
| `The Numbers` | Pass 1 in progress or complete |
| `The Projection` | Pass 2 in progress |
| `Complete` | Pass 2 done; verdict written |

Status column (REMOVE / MONITOR / BUY — ACCUMULATE / BUY — MEASURED / BUY — CONVICTION) written only when Phase = Complete.

---

## Token Strategy Summary

| File | How it enters Claude's context |
|---|---|
| `{TICKER}_financial_analysis.md` | Full read (Pass 1) |
| `{TICKER}_notes.md` | Targeted grep only — never full read |
| `{TICKER}_mda.md` | Gemini excerpts (Step 0); targeted grep (Pass 1); optional full read (Pass 2) — MD&A only, no footnotes boilerplate |
| `{TICKER}_mda_excerpts.md` | Full read (Context) — small by design |
| `{TICKER}_earnings_remarks.md` | Full read (Pass 2) |
| `{TICKER}_analyst.md` | Full read (Context) — small by design |
| `{TICKER}_earnings_qa.md` | Questions only via `{TICKER}_qa_questions.md` (Context); full responses in Pass 2 |
| `{TICKER}_qa_questions.md` | Full read (Context) — analyst questions only, extracted by earnings_calls.py |
| `{TICKER}_news.md` | Full read (Context) — headlines and summaries by design |
| `{TICKER}_social.md` | Full read (Context) — top posts + top 3 comments per post |
| `context_markets.md` | Full read (Pass 2) |
| `context_ai_supply_chain.md` | Full read (Pass 1 + Pass 2 for TAILWINDs) |

---

## What Changes vs. Old Structure

| Old | New |
|---|---|
| 6 steps | 3 steps |
| 6 thesis file sections | 4 sections (Context, The Numbers, The Projection, Synthesis) |
| Separate Discovery Signal + P&E sections | Combined into Context |
| P&E is a go/no-go gate | P&E is context-setting; no gate |
| Footnotes = standalone step after Financials | Integrated into Pass 1 via targeted grep |
| Earnings calls = standalone step | Full call in Pass 2 |
| Research = standalone step | News + Reddit fully analyzed in Context |
| Tracker updated after each step | Phase tracked throughout; verdict written once at end |
| ADVANCE / MONITOR / REMOVE | REMOVE / MONITOR / BUY — MEASURED / BUY — CONVICTION |
| AI SC context = Pass 2 only | AI SC context in both Pass 1 and Pass 2 for TAILWINDs |
| Claude handles all steps | Gemini handles Step 0 fetching and extraction; Claude handles all analysis |
| Full footnotes and MD&A loaded | Footnotes targeted grep only; MD&A excerpted by Gemini + targeted grep |

---

## What Does NOT Change

- Core analytical questions in financials, footnotes, earnings calls, synthesis (verbatim or near-verbatim, updated as we build each prompt)
- The five-category accounting checklist in footnotes (mandatory checks stay mandatory)
- GEMINI.md analytical philosophy (Graham/Dodd/Soros, epistemic tagging, source citation, Devil's Advocate)
- PIPELINE/WATCHLIST/DROPPED tracker structure
- LOSER/TAILWIND investment types and their distinct analytical burdens
- Individual fetch scripts (`price_earnings.py`, `financials.py`, `footnotes.py`, `earnings_calls.py`, `analyst.py`, `news.py`, `ticker_reddit.py`) — logic unchanged, verification added; `price.py` + `earnings.py` merged into `price_earnings.py`; `research.py` renamed to `news.py`
- context_markets.md and context_ai_supply_chain.md as required context

---

## Implementation Status

### Scripts — Step 0 fetch pipeline

| Script | Status | Notes |
|---|---|---|
| `price_earnings.py` | ✅ Done | Combines price + earnings; in-memory pass; outlier detection; replaces `price.py` + `earnings.py` |
| `analyst.py` | ✅ Done | Price targets + grades; outputs `{TICKER}_analyst.md`; verification added |
| `ticker_reddit.py` | ✅ Done | SocialVault ticker search; outputs `{TICKER}_social.md` |
| `news.py` (renamed from `research.py`) | ✅ Done | New script; output is `{TICKER}_news.md`; `research.py` archived |
| `earnings_calls.py` — Q&A extraction + verification | ✅ Done | Extracts analyst questions → `{TICKER}_qa_questions.md`; per-quarter ✓/✗ tracking |
| Verification — `financials.py` | ✅ Done | Per-ticker try/except; ✓/✗ summary; exit 1 on failure |
| Verification — `footnotes.py` | ✅ Done | Per-section word-count validation; PASS/FAIL table; exit 1 |
| Old scripts archived | ✅ Done | `price.py`, `earnings.py`, `research.py` → `archive/scripts/` |

### Prompts

| Prompt | Status | Notes |
|---|---|---|
| Step 0 Gemini prompt | ✅ Done | `prompt_step0_setup.md` — runs all scripts, extracts MD&A excerpts verbatim, verifies file checklist |
| Context step prompt | ✅ Done | `prompt_context.md` — 20 questions across 6 sections; full Q&A committed to thesis file |
| Thesis initialization (4-section template) | ✅ Done | Embedded in `prompt_context.md` Step 3 — Context / The Numbers / The Projection / Synthesis |
| Pass 1 prompt (`prompt_the_numbers.md`) | ✅ Done | Integrates financials + footnotes; `prompt_financials.md` + `prompt_footnotes.md` ready to archive |
| Pass 2 prompt (`prompt_the_projection.md`) | ✅ Done | Replaces `prompt_earnings_calls.md` + `prompt_synthesis.md`; earnings call analysis + catalyst assessment + synthesis in one prompt |

### Other

| Item | Status | Notes |
|---|---|---|
| Tracker schema — rename Status/Phase values | ✅ Done | Column Guide + data rows updated; ROIC column added; SC Layer Coverage made permanent section |
| GEMINI.md architecture table | ✅ Done | 3-step workflow, model division of labor, lean table |
| Archive old prompts | ✅ Done | All old prompts archived; `prompt_tracker_review.md` added; `index.md` updated |

### Decisions locked

- **Step 0 orchestration**: Gemini prompt (not shell script). Simple, no new code.
- **Q&A questions extraction**: Script (`earnings_calls.py`), not Gemini. Transcript is structured; analyst entries are filterable by title.
- **Reddit**: Script (`ticker_reddit.py`), not Gemini.
- **Analyst consensus**: 3 FMP endpoints — price-target-summary, price-target-consensus, grades. No EPS estimates (price targets embed analyst earnings models; grades capture conviction direction; forward delta already in earnings.py output).
- **Analyst consensus display**: Median target as primary anchor (robust to outliers). Flag when coverage count ≤ 2 in any time window.
- **EPS estimates from analyst-estimates endpoint**: Not available on current FMP subscription (402). Not needed.
- **Prompt preservation**: Core analytical questions kept verbatim where possible. Old prompts archived, not modified.
- **Context prompt structure**: Single integrated prompt (not sub-prompts per data source). Full Q&A committed to thesis file — no separate summary. Self-check is internal only (not output). Section-to-file mapping explicit in each section header.
- **Context analytical sequence**: Sentiment → Analyst Consensus → Price & Earnings → MD&A → Narrative Pre-check → Hypothesis. Narrative established before numbers interrogated.
- **P/E rubric**: Kept as guidance (under 20x / 20–30x / over 30x) but not a gate — Context has no pass/fail verdict.
- **Central question**: "Are earnings outpacing the price?" — applies to both LOSER and TAILWIND. LOSER/TAILWIND conditional questions (Q8–Q10) are the type-specific lens; Q11 is the unified conclusion.
- **Pass 1 prompt structure**: Single integrated prompt (`prompt_the_numbers.md`) combining financials analysis and footnotes/accounting checklist. Output format block contains all deliverables (Part A → Part B → Central Question → Targeted Searches → Accounting Checklist → Accounting Analysis → Hypothesis Check); self-check is internal only. Full output committed to `### The Numbers` in thesis file.
- **Pass 1 analytical sequence**: Part A metrics → Part B synthesis → Central Question (LOSER/TAILWIND) → Targeted Searches (grep, driven by Part A flags) → Mandatory Accounting Checklist (5 categories, grep only) → Accounting Analysis (4 synthesis questions) → Hypothesis Check (updated hypothesis + bull/bear + open questions for Pass 2).
- **Footnotes/MD&A token discipline**: `{TICKER}_notes.md` and `{TICKER}_mda.md` never read in full in Pass 1 — targeted grep only. Grep terms flagged during Part A, executed after Part B.
- **Central Question**: Explicit named question at end of Part B — LOSER/TAILWIND conditional. Mirrors Q11 structure in Context step. Answers the investment-relevant synthesis before pivoting to accounting searches.
- **Example analyses**: Selected examples only (not complete analyses) — 3 Part A metrics, 2 Part B questions for financials; 2 of 4 accounting questions. Central Question and Hypothesis Check examples deferred until first real Pass 1 run produces validated output.

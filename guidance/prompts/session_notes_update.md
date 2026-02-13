# Session Notes Updater

**Objective:** Synthesize raw user text with the System's own analysis of the Daily Digest to propose organized updates for `SESSION_NOTES.md`.

**Inputs:**
1.  **User Text:** Unstructured excerpts/notes pasted in the chat. May arrive across multiple messages — each message may contain new excerpts to process. **Important:** When the user copy-pastes excerpts from social media, articles, or Reddit posts, first-person language ("I," "my," "I'm") refers to the *original author of the excerpt*, NOT the user. Do not attribute these opinions to the user. Treat them as third-party source material.
2.  **Daily Digest:** The current `data/discovery/Daily_Digest_*.md`.
3.  **Current Notes:** `SESSION_NOTES.md`.

---

## Workflow Model

This is a **multi-turn, user-driven session**, not a single-pass operation.

1.  **The system proposes, the user decides.** **NEVER call any file-editing tool (Edit, Write, or equivalent) on `SESSION_NOTES.md` until the user has explicitly approved the final version of all proposed changes.** "Approved" means the user says something like "write it," "go ahead," "looks good, apply it," or "done." A user saying "yes, but..." or providing corrections is NOT approval to write — it means the proposal needs revision. Present all proposed additions as plain text in the chat. Do not touch the file until the session is complete and the user gives unambiguous final approval.
2.  **Accumulate across messages.** The user may paste excerpts across multiple messages. Each message should be processed as new input — extract tickers and context, propose additions, and wait for feedback. Do not treat each message as a fresh invocation; carry forward the running state of what has been proposed and approved so far.
3.  **The user signals when done.** Keep processing new inputs until the user confirms the session notes update is complete (e.g., "that's everything," "go ahead and write it," "done"). Do not wrap up or write to the file after a single round unless explicitly told to.
4.  **Batch the writes.** Once the user confirms completion, apply all approved changes to `SESSION_NOTES.md` in a single pass. This avoids partial updates and gives the user a clean before/after.
5.  **Corrections are permanent.** If the user tells you to remove, change, or recategorize something, that correction applies for the rest of the session. Do not revert to a previous version of the proposal. Do not re-add items the user removed. Each iteration must incorporate ALL prior feedback.

---

## Procedure

### 1. Digest Scan (Auto-Add)

*   **Action:** Read the current Daily Digest.
*   **Extract:** Identify ALL "Screening Candidates" from **Section 4 of the Digest ONLY.** Stocks mentioned elsewhere in the Digest (Sections 1-3: Market Overview, AI Ecosystem, Applied Investment Flags) are NOT screening candidates for auto-add purposes — even if they are discussed in detail, even if they dropped significantly, even if they seem like obvious candidates. If a ticker does not appear in a Section 4 candidate block, it does not get auto-added. Period.
*   **Cross-Reference:** Compare these candidates against `SESSION_NOTES.md` — check ALL sections (screening lists, pipeline, trades) to avoid duplicates.
*   **Auto-Add:** Every Digest screening candidate that isn't already tracked MUST be proposed for addition to the appropriate screening section. No filtering or judgment — the user can reject later.
*   **Categorize:** Assign each new candidate to either:
    *   **Losers / Dislocation** — price dropped, earnings miss, scandal, accounting issue, selloff, etc.
    *   **Momentum / Other** — price surged, earnings beat, structural tailwind, thematic play, etc.
*   **Format:** Each entry must follow: `- **TICKER** (Company Name) — 1-sentence reason [Date]`

> **Common Error — DO NOT do this:**
> Do not scan the entire Digest for interesting stocks and add them to the auto-add list. The Digest's Section 1 (Market Overview), Section 2 (AI Ecosystem), and Section 3 (Applied Investment Flags) contain many tickers discussed for thematic context — these are NOT screening candidates unless they also appear in Section 4. If the user wants to track a stock that is only in Sections 1-3, they will add it manually via User Input.

**Mapping to SESSION_NOTES.md sections:** The file uses three screening sections:
- `Screening Candidates — Losers` → maps to Losers / Dislocation
- `Screening Candidates — AI` → maps to Momentum/Other when the stock is an AI play
- `Screening Candidates — Other` → maps to Momentum/Other for non-AI plays

Use the actual section names from SESSION_NOTES.md in your proposals (not "Daily Digests" or "Momentum").

### 2. User Input Analysis

*   **Extract Tickers:** Identify symbols mentioned in the user's text.
*   **Extract Context:** Pull out specific metrics, thesis points, catalysts, red flags, or open questions. See Context Quality section below.
*   **Categorize Sources:**
    *   If a ticker is a Digest Screening Candidate → it goes in the appropriate screening section per the mapping above.
    *   If a ticker is only in User Text → it goes in `Screening Candidates — Other`.
    *   Other Sources entries should also be categorized as Losers/Dislocation or Thematic/Infrastructure.

### 3. Context Updates

Context entries go in **Stock Context** (for individual tickers) or **Market & Thematic Context** (for macro themes, analyst screens, sector dynamics).

*   Propose context from BOTH the user's text AND the Digest analysis. If the Digest contains rich detail about a screening candidate (specific numbers, catalysts, risks), capture it — don't wait for the user to repeat it.
*   If a stock already has a context entry, propose appending new information (with date) rather than overwriting.
*   If the user provides an excerpt about a stock that has no context entry yet, create one.

### 4. Output Format

Present a consolidated plan for approval:

> **Digest Auto-Add (Section 4 only):**
> *   [Ticker] → Losers: "[reason]" [Date]
> *   [Ticker] → Other: "[reason]" [Date]
>
> **User Input — Screening Additions:**
> *   [Ticker] → Other Sources (Losers / Thematic): "[reason]"
>
> **Context Updates:**
> *   **Stock Context → [Ticker]:** [What will be added/created]
> *   **Market Context → [Theme]:** [What will be added/created]
>
> **Proceed with these updates?**

---

## Context Quality Guidance

### Purpose

The Stock Context section is a research bank. It provides orientation and recent context for prioritizing screening candidates and informing later analysis. It is NOT the analysis itself — no decisions are made from this file alone.

The goal is rich orientation: enough to understand *what happened*, *why it matters*, *what the sentiment is*, and *what the open questions are*. Think: "briefing notes that save 30 minutes of research." The existing entries in SESSION_NOTES set the quality bar — look at the depth of entries like PYPL, NOW, CRM, and KD before writing new ones. Match that level of detail when the source material supports it.

### Source Fidelity (Critical)

**Only write what is sourced from the inputs (User Text, Daily Digest, or prior Session Notes).** Do not:
- Introduce financial opinions, interpretations, or judgments not present in the source material
- Fill in figures, ratios, or metrics that aren't explicitly stated in the inputs
- Extrapolate or speculate beyond what the sources say
- Add "analysis" framing (e.g., "this suggests undervaluation") unless the source said it

Basic gap-filling is OK — e.g., expanding a ticker to its company name, or noting that a -55% drop is "significant." But if a claim requires domain knowledge that isn't in the inputs, leave it out. The value of this file depends on it reflecting what was actually reported and discussed, not what the system thinks about it.

**When in doubt, quote or closely paraphrase the source rather than rewriting it.**

### What makes context useful
- The specific catalyst or event (what happened)
- Numbers from the source where available (%, $, ratios)
- Sentiment signal (what the market/analysts/Reddit are saying)
- Open questions worth investigating later

### Context Depth Rules

1. **Preserve ALL numbers.** Every dollar figure, percentage, ratio, valuation multiple, account count, revenue figure, and date mentioned in the source material MUST appear in the context entry. Do not summarize "$26.5B expected 2026 revenue" as "large revenue base." The number IS the value.
2. **Structure over summary.** Do not compress a multi-paragraph excerpt into a single bullet. Use labeled sub-sections (bold headers) to organize different aspects: the event, the mechanics, the counter-argument, the investigation items.
3. **Synthesize, don't copy-paste.** Quoting a source is acceptable for key phrases, but do not reproduce entire paragraphs verbatim. Extract the thesis, the evidence, and the implications. Organize them so a reader can scan and orient quickly.
4. **When multiple viewpoints exist, present both.** If Reddit comments contain a bull case and a bear case, present BOTH with clear labels. Do not flatten two opposing views into a single bullet.
5. **Minimum depth for rich sources.** If the user provides 3+ sentences about a stock or theme, the context entry should have at least 3-4 structured bullets with sub-points. One-liner entries are only acceptable when the source material is itself a headline with no supporting detail.

### Examples

**Good** — sourced facts, specific, orients the reader:
```
### KD (Kyndryl)
- **Collapse (-55%)**: "Perfect Storm" of bad news triggering a massive confidence loss.
- **Triggers**: Simultaneous departure of CFO, General Counsel, and Global Controller + SEC voluntary document request regarding accounting.
- **Fundamentals**: Guidance flipped from growth (+1%) to decline (-2% to -3%). FCF forecast slashed from $550M to $350M.
```

**Better** — richer source material produces richer entry:
```
### NFLX (Netflix)
- **Valuation Fragility**: At 35x P/E, "you're basically pricing in perfection." Down 25%+ YoY; fell another 4.72% on Feb 12. Consistent margin growth YoY; trading close to book value.
- **The WB Deal Paradox**:
  - **Bear**: "A lot of turbulence with the WB deal. Feels like everyone is just waiting for that to finalize. If the DOJ blocks the deal, or if they choose Paramount, the stock could slip even further."
  - **Bull**: "NFLX would be looking for a reason to get out of the deal... When the deal falls through, NFLX's stock would soar with all of that debt coming off their balance sheet." Argues next growth frontier is YouTube competition, not VOD consolidation.
- **Investigation Items**: What is the WB deal specifically? Debt impact? Current subscriber metrics and FCF yield at $75.86?
```
Note: The KD example above is a **minimum** — 3 bullets for a stock with limited source material. When the source material is richer (as with NFLX above), the entry should be proportionally deeper. Do not compress rich sources into KD-length entries.

**Bad** — vague, no specifics, useless for prioritization:
```
### KD (Kyndryl)
- Stock fell significantly on bad news.
- Multiple executives departed.
```

**Also bad** — system injecting unsourced opinion:
```
### KD (Kyndryl)
- Stock fell 55% which likely represents an overreaction given Kyndryl's stable recurring revenue base and IBM heritage.
- The executive departures may be a positive sign of a governance reset.
```
The "overreaction" judgment and "positive sign" spin aren't from the sources — they're the system editorializing. This kind of addition actively degrades the file by mixing source material with fabricated analysis.

**Also bad** — copy-pasting source text without structuring it:
```
### PYPL (PayPal)
- "Honestly I'll probably tap out at 3x, and find a new hated stock."
- "The models I've looked at are 3 to 5 percent growth, all free cash flow goes to financial engineering buying back shares, and it tops out at 180 dollars."
- "I'm in big bc I don't need to believe in maybes. Just buybacks and math."
```
This is just pasting Reddit quotes with no structure. The reader still has to do the work of extracting the thesis. Instead, synthesize: identify the thesis (buyback-driven return with a $180 ceiling), the exit plan (~$120 / 3x), and the optionality (agentic AI, banking license, ad network) — then use key quotes as evidence within that structure.

**Flexibility:** Not every stock will have deep context available. A 2-line entry based on a headline is fine if that's all the data there is. The point is: capture what IS available from the sources without watering it down or padding it out.

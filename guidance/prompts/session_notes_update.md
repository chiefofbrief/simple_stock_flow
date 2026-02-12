# Session Notes Updater

**Objective:** Synthesize raw user text with the System's own analysis of the Daily Digest to propose organized updates for `SESSION_NOTES.md`.

**Inputs:**
1.  **User Text:** Unstructured excerpts/notes pasted in the chat. May arrive across multiple messages — each message may contain new excerpts to process.
2.  **Daily Digest:** The current `data/discovery/Daily_Digest_*.md`.
3.  **Current Notes:** `SESSION_NOTES.md`.

---

## Workflow Model

This is a **multi-turn, user-driven session**, not a single-pass operation.

1.  **The system proposes, the user decides.** Never write to `SESSION_NOTES.md` until the user explicitly approves. Present all proposed additions in the chat first.
2.  **Accumulate across messages.** The user may paste excerpts across multiple messages. Each message should be processed as new input — extract tickers and context, propose additions, and wait for feedback. Do not treat each message as a fresh invocation; carry forward the running state of what has been proposed and approved so far.
3.  **The user signals when done.** Keep processing new inputs until the user confirms the session notes update is complete (e.g., "that's everything," "go ahead and write it," "done"). Do not wrap up or write to the file after a single round unless explicitly told to.
4.  **Batch the writes.** Once the user confirms completion, apply all approved changes to `SESSION_NOTES.md` in a single pass. This avoids partial updates and gives the user a clean before/after.

---

## Procedure

### 1. Digest Scan (Auto-Add)

*   **Action:** Read the current Daily Digest.
*   **Extract:** Identify ALL "Screening Candidates" (Section 4 of the Digest).
*   **Cross-Reference:** Compare these candidates against `SESSION_NOTES.md` — check ALL sections (screening lists, pipeline, trades) to avoid duplicates.
*   **Auto-Add:** Every Digest screening candidate that isn't already tracked MUST be proposed for addition to `Screening Candidates — Daily Digests`. No filtering or judgment — the user can reject later.
*   **Categorize:** Assign each new candidate to either:
    *   **Losers / Dislocation** — price dropped, earnings miss, scandal, accounting issue, selloff, etc.
    *   **Momentum / Other** — price surged, earnings beat, structural tailwind, thematic play, etc.
*   **Format:** Each entry must follow: `- **TICKER** (Company Name) — 1-sentence reason [Date]`

### 2. User Input Analysis

*   **Extract Tickers:** Identify symbols mentioned in the user's text.
*   **Extract Context:** Pull out specific metrics, thesis points, catalysts, red flags, or open questions. See Context Quality section below.
*   **Categorize Sources:**
    *   If a ticker is a Digest Screening Candidate → it goes in `Screening Candidates — Daily Digests`.
    *   If a ticker is only in User Text → it goes in `Screening Candidates — Other Sources`.
    *   Other Sources entries should also be categorized as Losers/Dislocation or Thematic/Infrastructure.

### 3. Context Updates

Context entries go in **Stock Context** (for individual tickers) or **Market & Thematic Context** (for macro themes, analyst screens, sector dynamics).

*   Propose context from BOTH the user's text AND the Digest analysis. If the Digest contains rich detail about a screening candidate (specific numbers, catalysts, risks), capture it — don't wait for the user to repeat it.
*   If a stock already has a context entry, propose appending new information (with date) rather than overwriting.
*   If the user provides an excerpt about a stock that has no context entry yet, create one.

### 4. Output Format

Present a consolidated plan for approval:

> **Digest Auto-Add:**
> *   [Ticker] → Losers: "[reason]" [Date]
> *   [Ticker] → Momentum: "[reason]" [Date]
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

The goal is a middle ground: enough to understand *what happened*, *why it matters*, and *what the sentiment is* — not enough to form a complete investment thesis. Think: "briefing notes before the real work starts."

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

### Examples

**Good** — sourced facts, specific, orients the reader:
```
### KD (Kyndryl)
- **Collapse (-55%)**: "Perfect Storm" of bad news triggering a massive confidence loss.
- **Triggers**: Simultaneous departure of CFO, General Counsel, and Global Controller + SEC voluntary document request regarding accounting.
- **Fundamentals**: Guidance flipped from growth (+1%) to decline (-2% to -3%). FCF forecast slashed from $550M to $350M.
```

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

**Flexibility:** Not every stock will have deep context available. A 2-line entry based on a headline is fine if that's all the data there is. The point is: capture what IS available from the sources without watering it down or padding it out.

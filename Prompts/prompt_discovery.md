# Discovery & Tracker Update Prompt

**Objective:** Bridge the gap between daily research (Peter's Digest, User Inputs) and the system's tracking files (`Stock_Tracker.md` and `Discovery_Context.md`). Synthesize inputs into structured, actionable updates.

**Inputs:**
1.  **Daily Digest:** The latest market digest (specifically Section 4: Screening Candidates).
2.  **User Input:** Raw tickers, notes, or excerpts pasted in chat.
3.  **Current Tracker:** `Stock_Tracker.md`.
4.  **Current Context:** `Discovery_Context.md`.

---

## Workflow Model

**1. The system proposes, the user decides.**
Never edit files directly. Present all proposed additions as a structured plan in the chat. Wait for explicit user approval (e.g., "add them," "looks good") before applying changes.

**2. Screening Candidates (Auto-Add):**
*   **Source:** Read **Section 4** of the latest Daily Digest.
*   **Action:** For each candidate in Section 4, propose adding it to `Stock_Tracker.md` if not already present.
*   **Tagging Logic:**
    *   If the "Signal" or "Why" involves significant drops/weakness -> `[LOSER]`
    *   If related to Artificial Intelligence/Hardware/Data Centers -> `[AI]`
    *   Otherwise -> `[OTHER]`

**3. User Input Analysis:**
*   **Source:** Tickers mentioned in the user's chat message.
*   **Action:** Propose adding them to `Stock_Tracker.md`.
*   **Tagging:** Infer tags based on the user's context (e.g., "add this AI play" -> `[AI]`). Default to `[OTHER]` if unclear.
*   **Context Generation:** Extract *rich* context (preserving numbers, dates, specifics). See "Context Quality Guidance" below.

**4. Consistency Check (Missing Tracker Entries):**
*   **Source:** Scan `Discovery_Context.md` for tickers that are NOT in `Stock_Tracker.md`.
*   **Action:** Propose adding these missing tickers to `Stock_Tracker.md`.
*   **Tagging:** Infer tags based on the existing context entry.

---

## Context Quality Guidance (CRITICAL)

**Purpose:** The Context file is a research bank. It provides orientation and recent context for prioritizing candidates. It is NOT the analysis itself—no decisions are made from this file alone.

**Source Fidelity:**
*   **Only write what is sourced from the inputs.** Do not introduce outside opinions or judgments.
*   **Preserve ALL numbers.** Every dollar figure, percentage, ratio, valuation multiple, and date mentioned in the source material MUST appear in the context entry. Do not summarize "$26.5B expected 2026 revenue" as "large revenue base." The number IS the value.
*   **Structure over summary.** Do not compress a multi-paragraph excerpt into a single bullet. Use labeled sub-sections (bold headers) to organize different aspects: the event, the mechanics, the counter-argument, the investigation items.
*   **Synthesize, don't copy-paste.** Quoting a source is acceptable for key phrases, but do not reproduce entire paragraphs verbatim. Extract the thesis, the evidence, and the implications. Organize them so a reader can scan and orient quickly.

**Examples:**
*   **Bad:** "Stock fell significantly on bad news." (Vague)
*   **Good:** "**Collapse (-55%)**: 'Perfect Storm' of bad news triggering massive confidence loss. Triggers: Simultaneous departure of CFO, General Counsel, and Global Controller + SEC voluntary document request regarding accounting." (Specific, sourced)

---

## Output Format

Present the proposal in this exact format:

### 1. Proposed Tracker Updates
| Source | Ticker | Proposed Tags | Reason (Brief) |
| :--- | :--- | :--- | :--- |
| Digest | **TICKER** | `[TAG]` | *Brief reason from Digest* |
| User | **TICKER** | `[TAG]` | *Brief reason from User* |
| Context | **TICKER** | `[TAG]` | *Existing context suggests addition* |

### 2. Proposed Context Updates
**Ticker-Specific Context:**
- **TICKER** (Company Name) — *[Signal/Reason]. [The Why]. [Investigation Items]. [Date]*
- **TICKER** (Company Name) — *[User's Context - Structured per Guidelines]. [Date]*

**Market/Thematic Context (if applicable):**
- **Title** — *Summary of theme from Digest/User*

---

**Instructions for the Assistant:**
1.  **Check Duplicates:** Do not propose adding tickers that are already in `Stock_Tracker.md`.
2.  **Context Matching:** Ensure every proposed Tracker addition has a corresponding Context entry.
3.  **Wait for Approval:** Ask "Do you want to apply these updates?" after the proposal.

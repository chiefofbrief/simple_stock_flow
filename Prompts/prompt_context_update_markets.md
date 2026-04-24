# Prompt — Context Update — Markets

## Role
You are an expert financial analyst. Your task is to synthesize the past week's analyzed Markets Digests into a structured update to `context_markets.md`, the rolling markets context file, and surface any new screening candidates not yet in the stock tracker.

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:

*   `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
*   `context_markets.md` — The current markets rolling context. Read in full before proposing any changes.
*   `Stock_Tracker.md` — The stock tracker. Read now to prepare for the Tracker Bridge in Step 4.
*   **All analyzed Markets Digests since the last context update** — Check the `*Last updated*` date at the top of `context_markets.md`. Find every `Peter's Digest/Markets Digest/Markets_Digest_{DATE}.md` file dated after that date that contains a `## Markets Analysis` section (i.e., has been analyzed by automation). On a typical Monday run this will be Tuesday–Friday of the prior week. State which files you are using before proceeding.

    For each digest, read only:
    1. The `## Markets Analysis` section — everything from that header down to the first `---` separator. This is the synthesized analysis; the raw articles below it have already been processed and should be ignored.
    2. The **Macro Dashboard** tables (Key Levels and Sector Discovery) — used to populate the Recent Log entry for that day.

**STOP. Do not proceed until all files have been read.**

---

## Step 2: Propose Context Update

Re-read `context_markets.md`. Compare it against the analyzed digests and propose the following:

*   **Current State changes:** For each section under Current State, note only what has changed materially from what is already captured. If nothing has changed in a section, do not include it. If nothing has changed anywhere, state "No Current State updates." When proposing a section update, write out the full proposed section text — do not summarize or condense existing prose, only incorporate the new developments. Frame each update as a progression from the prior state: explicitly reference what was noted before and how today's developments confirm, contradict, or escalate it. Do not produce a clean snapshot as if the prior state didn't exist — produce an evolution.
*   **New Recent Log entries:** One structured entry per digest, ordered most recent first, using the following fields:
    *   **Key Levels:** SPY [price] | VIX [level] | 10Y [yield] | Brent [price] — pulled directly from the Macro Dashboard.
    *   **Sector Performance — Top:** [sector +%], [sector +%], [sector +%] | **Bottom:** [sector -%], [sector -%], [sector -%] — pulled directly from the Sector Discovery table.
    *   **Market Posture:** [1 sentence on risk-on/off stance and why].
    *   **Prevailing Narratives:** [2–3 themes driving the session].
    *   [Optional: 1–2 additional bullets for notable macro developments not captured above.]
*   **Screening Candidates updates:** List any new Loser or Tailwind candidates from the digests not already present in the Screening Candidates lists in `context_markets.md`. Present them in the same inline format as existing entries: **TICKER** (brief context).

Present the full proposed update to the user before writing anything.

**Action:** Ask: "Do you approve this context update? Should I apply it to context_markets.md?"

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit Context Update

Upon explicit user approval, apply the following changes to `context_markets.md`:

1.  Update the `*Last updated*` date at the top of the file.
2.  Rewrite only the Current State sections that were flagged as changed in Step 2. Leave unchanged sections as-is. When rewriting a section, preserve the instructive text block (the bracketed description in square brackets beneath each section heading) exactly as-is. Frame each rewrite as a progression from the prior state, not a fresh snapshot.
3.  Prepend the new Recent Log entries at the top of the Recent Log section (most recent first).
4.  If the Recent Log now contains more than 20 entries, remove the oldest entries until only 20 remain.
5.  Append any new Screening Candidates to the appropriate list in the Current State section.

**STOP. Proceed to Step 4.**

---

## Step 4: Tracker Bridge

Using the data already read in Step 1, perform the following diff:

*   Extract every ticker from **Screening Candidates — Losers** and **Screening Candidates — Tailwinds** in `context_markets.md`.
*   Cross-reference against all tickers in the **PIPELINE** and **WATCHLIST** sections of `Stock_Tracker.md`.
*   Present two lists of tickers that appear in the Screening Candidates but **not** in the tracker:

**Losers not in tracker:**
| Ticker | Context (from context_markets.md) |
|--------|-----------------------------------|

**Tailwinds not in tracker:**
| Ticker | Context (from context_markets.md) |
|--------|-----------------------------------|

If all candidates are already in the tracker, state "All candidates are currently in the tracker."

**Action:** Ask: "For each ticker, reply **Add** (flag for tracker addition), **Ignore** (leave on list), or **Remove** (remove from Screening Candidates)."

**STOP. Wait for user response.**

---

## Step 5: Apply Tracker Bridge Decisions

For each ticker marked **Remove**: delete it from the appropriate Screening Candidates list in `context_markets.md`.

Tickers marked **Add** or **Ignore** are left in the list as-is. For any **Add** tickers, remind the user to add them to `Stock_Tracker.md` manually — do not modify `Stock_Tracker.md`.

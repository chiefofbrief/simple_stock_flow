# Discovery Enrichment Prompt

## Role
You are an expert financial analyst. Your task is to bridge the gap between the daily digest analysis and the discovery file (`Discovery_{DATE}.md`), synthesizing the digest's signals with research inputs into a structured, actionable document.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational investment philosophy. Governs candidate selection and classification throughout.
- `AI_Guidelines.md` — AI-specific investment criteria. Apply where applicable.
- `Peter's Digest/Daily_Digest_{DATE}.md` — Read in full. The prepended analysis (Sectors, Tailwinds, Losers) is the starting point for candidates and themes.

**STOP. Do not proceed until all files have been read.**

---

## Step 2: Synthesize & Propose

### What this step does
This prompt takes two inputs — the digest analysis and research paste-ins — and merges them into a single proposed `Discovery_{DATE}.md`. It does not simply transcribe; it re-examines classifications in light of new context, drops candidates where the additional context contradicts or weakens the thesis, adds new candidates from the research inputs, and deepens the macro/thematic picture.

### Input Handling
- **Digest analysis:** The Sectors, Tailwinds, and Losers sections from the prepended digest analysis are the baseline candidate list. Every entry is a candidate for inclusion unless the research notes contradict or weaken the thesis.
- **Research paste-ins:** Treat these as the authoritative enrichment layer. Where the notes conflict with or supersede the digest's framing, the notes take precedence. Where they add context, merge it into the existing entry. Where they introduce new candidates not in the digest, add them.
- **Candidate inclusion:** Lean toward inclusion. A candidate should only be dropped if the additional context explicitly contradicts or materially weakens the thesis under `GEMINI.md`. Absence of paste-in context alone is not sufficient reason to drop a candidate.
- **Dropped candidates:** If a candidate is dropped, flag it explicitly with a one-line reason in the Dropped section. Do not silently omit any digest candidate.

### Analysis Guidelines
- **Re-examine classifications:** The digest classifications (`[LOSER]`, `[TAILWIND]`) are provisional. Re-evaluate them in light of the paste-in context. If the classification changes, note why.
- **Thematic Identification:** Identify recurring macro themes across both inputs, even if not yet tied to a specific candidate. These feed the Macro/Thematic Findings section.
- **Flexible Identification:** If a candidate lacks an explicit ticker, use the Company Name as a placeholder.

### Writing Guidelines
- **Source Fidelity:** Only write what is sourced from the digest or paste-ins. Do not introduce outside opinions or judgments.
- **Context Fidelity:** Capture the entire context for each candidate, including all catalysts and numerical figures. Do not summarize — "$500M in savings" must not become "cost reductions."
- **Synthesize, Don't Copy-Paste:** Quoting a source is acceptable for key phrases, but do not reproduce entire paragraphs verbatim. Extract the thesis, the evidence, and the implications.
- **Prose Over Bullets:** Each candidate entry should naturally weave together what happened, why it matters, and the key numbers. The logic of the trade must be legible without supporting materials.
- **Date Integrity:** Every entry must be anchored with the current session date.

### Deliverable

**Questions:**
1. **Source Check:** Is every candidate and data point sourced directly from the digest or paste-ins — no outside opinions introduced?
2. **Context Check:** Has the full context for each candidate been preserved — no figures or catalysts summarized away?
3. **Synthesis Check:** Does each entry capture the logic of the trade as coherent prose — not a compressed list of facts?
4. **Philosophy Check:** Does each classification genuinely reflect the logic in `GEMINI.md` and `AI_Guidelines.md` where applicable?
5. **Coverage Check:** Have all digest candidates been explicitly included, dropped, or reclassified — none silently omitted?
6. **Thematic Check:** Do the Macro/Thematic Findings connect forces across candidates and inputs — not just restate individual headlines?

**Proposed Output Format:**
```
## Candidates — [DATE]

### LOSERS
- **TICKER** (Company Name) `[LOSER]` — [Full enriched context 
  prose weaving together digest signals and paste-in research. 
  Include all catalysts, figures, and the logic of the thesis. 
  Philosophy relevance should be woven into the prose, not 
  listed separately.] [Date]

### TAILWINDS
- **TICKER** (Company Name) `[TAILWIND]` — Sector: [theme]. 
  [Full enriched context prose weaving together digest signals 
  and paste-in research. Include all catalysts, figures, and 
  the logic of the thesis.] [Date]

### DROPPED
- **TICKER** — [One-line reason for dropping.]

## Macro/Thematic Findings — [DATE]
- **[THEME]** — [Prose narrative connecting macro forces, sector 
  drivers, and implications. Connect themes across candidates 
  where relevant.] [Date]
```

- **Action:** Ask: *"Do you approve this proposed `Discovery_{DATE}.md`? Any candidates to add, drop, or reclassify before I write the file?"*

**STOP. Wait for explicit user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval, write the complete proposed content to `Discovery_{DATE}.md`.

**STOP. Wait for user approval before committing.**

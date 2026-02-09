# Role: Notes & Disclosure Analyst

**Objective:** Investigate SEC filing disclosures (MD&A and Notes to Financial Statements) to address open questions from prior analyses and surface disclosure-level risks. This is a follow-up investigation, not a standalone analysis.

---

## Preparation

**Required Reading:**
- `Stock Analysis Guidelines.md` - Core investment principles and framework

**Available Data:**
- `{TICKER}_notes_mda.md` - Consolidated SEC filing text (MD&A + Notes from latest 10-K and 10-Q)

**Prior Analyses (read before starting):**
- `{TICKER}_statements.md` - Financial statement analysis (if exists — analysis is prepended to the data file)
- `{TICKER}_sentiment.md` - Sentiment analysis (if exists — analysis is prepended to the data file)

Review prior analyses to identify investigation items, gaps, and open questions. These drive Pass 1.

**Glossary:**
- `guidance/glossaries/notes.md` - Search terms, red flag patterns, and interpretation guidance for disclosure analysis

---

## Pass 1: Investigation-Driven Search

**Objective:** What do the filings reveal about questions raised by prior analyses?

**Action:**
1. Read prior analyses and extract investigation items, gaps, and open questions
2. For each item, search the filing text (MD&A and Notes sections) for relevant disclosures
3. Extract supporting quotes with source citations (specify: 10-K MD&A, 10-K Notes, 10-Q MD&A, 10-Q Notes)
4. Assess whether the filing disclosure addresses, partially addresses, or is silent on each item

If no prior analyses exist, skip to Pass 2.

**Begin writing** the analysis — see Output section for format and file location.

---

## Pass 2: Red Flags & Disclosure Scan

**Objective:** Proactively search for disclosure risks that prior analyses wouldn't have surfaced.

**Action:**
1. Read `guidance/glossaries/notes.md` for search terms and red flag categories
2. Search the filing text for each category
3. Include only findings that exist or where absence is notably positive
4. Skip items with no indication and no notable absence — don't catalog empty searches

**Key areas** (see glossary for specific terms and interpretation):
- Contingent liabilities and legal proceedings
- Related party transactions
- Off-balance-sheet arrangements
- Revenue recognition changes or unusual policies
- Goodwill impairment risk indicators
- Debt covenants and refinancing risk
- Management tone shifts between 10-K and 10-Q MD&A

**Continue updating** the analysis.

---

## Pass 3: Synthesis

**Objective:** What do the disclosures mean for the broader analysis?

**Action:**
1. Summarize what the filings revealed about prior investigation items
2. Identify new questions or concerns raised by the disclosures
3. Assess net impact on the analysis — did disclosures strengthen, weaken, or leave the picture unchanged?
4. Tag all open items appropriately

**Finalize** the analysis — complete the TLDR and synthesis sections.

---

## Output

**Append to TOP of:** `data/tickers/{TICKER}/{TICKER}_notes_mda.md`

Read the existing file first, then prepend your analysis with a date header separator:

```
---
# NOTES & MD&A ANALYSIS - [DATE]
---

[Your analysis here]

---
```

Then append the existing file content (consolidated filing text) below.

### Output Structure

```markdown
## TLDR

**Key Findings:**
- [What the disclosures revealed about prior investigation items]
- [Notable red flags or positive signals]

**Impact on Analysis:** [Strengthened / Weakened / Neutral — with brief explanation]

**Filings Analyzed:** 10-K (FY {YYYY}), 10-Q (Q{X} {YYYY})

---

## Investigation Items Addressed

For each item from prior analyses:

**{Item description}**
- **Source:** {Which prior analysis raised this}
- **Finding:** {What the filings disclosed, or silence}
- **Supporting Quotes:**
  > {Source}: "{quote}" — or "Not addressed in filings"
- **Status:** [Resolved / Partially addressed / Unresolved]

---

## Disclosure Findings

Findings from the red flag and disclosure scan (Pass 2). Include only material findings.

**{Finding category}**
- **Key Findings:** {What was disclosed}
- **Supporting Quotes:**
  > {Source}: "{quote}"
- **Significance:** {Why this matters for the analysis}

---

## Open Items

New or unresolved items tagged for follow-up:

- [INVESTIGATE] {Description} | Source: Notes Analysis ({DATE})
- [GAP] {Description — source was silent} | Source: Notes Analysis ({DATE})
- [NEW] {Description — discovered during this analysis} | Source: Notes Analysis ({DATE})

**Tag definitions:**
- [INVESTIGATE]: Anomaly or question requiring follow-up
- [GAP]: Filing was silent on a topic where disclosure would be expected
- [NEW]: New item discovered during this analysis, not raised by prior work

---

## Synthesis

**Disclosures vs. Prior Analysis:**
- Where did filings confirm prior findings?
- Where did filings contradict or complicate the picture?
- What remains unanswered?

**Net Assessment:**
- {Overall impact on the analysis and key takeaways}
```

**Flexibility:** Let materiality drive depth. Elaborate on critical or anomalous findings; be brief on standard disclosures. If prior analyses raised 2 major items and 10 minor ones, spend most of the analysis on the 2 major items.

---

## Notes

**Remember:**
- This analysis builds on prior work — it's not starting from scratch
- Filing text is long; focus on relevance, not completeness
- MD&A contains management's narrative; Notes contain accounting detail — both matter but for different reasons
- Agents are useful for searching across the filing text, but avoid running multiple agents simultaneously — token cost doesn't scale with proportional value
- Compare 10-K and 10-Q disclosures where both exist — changes in tone or detail between filings can be informative
- **External Data:** If citing data not from the script outputs, explicitly state the source

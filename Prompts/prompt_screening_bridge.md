# Screening Bridge Prompt

## Role
You are an expert financial analyst. Your task is to extract screening verdicts from the price and earnings data files and append a structured Screening Results section to `Discovery_{DATE}.md`.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `Discovery_{DATE}.md` — The current discovery file. Identifies all candidates and their tags. The Tailwind Research section contains peer lists for TAILWIND candidates.
- `Data/screening/Price_Data_{DATE}.txt` — Contains the Status & Price Summary for each screened ticker.
- `Data/screening/Earnings_{DATE}.txt` — Contains the Status & Earnings Summary for each screened ticker.

---

## Step 2: Extract & Propose

For each ticker identified in `Discovery_{DATE}.md`, locate the following in the data files:

- **Status & Price Summary** — the full paragraph verbatim from `Price_Data_{DATE}.txt`
- **Status & Earnings Summary** — the full paragraph verbatim from `Earnings_{DATE}.txt`
- **Overall verdict** — PASS only if both price and earnings returned PASS. If either returned FILTERED, the overall verdict is FILTERED.

For TAILWIND passes, the peer list is available in the Tailwind Research section of `Discovery_{DATE}.md` — do not duplicate it here, simply reference its location.

### Proposed Output Format
```
## Screening Results — [DATE]

### LOSERS

#### TICKER (Company Name)
**Price:** PASS / FILTERED
**Price Summary:** [Verbatim Status & Price Summary paragraph]

**Earnings:** PASS / FILTERED
**Earnings Summary:** [Verbatim Status & Earnings Summary paragraph]

**Overall:** PASS / FILTERED

---

### TAILWINDS

#### TICKER (Company Name)
**Price:** PASS / FILTERED
**Price Summary:** [Verbatim Status & Price Summary paragraph]

**Earnings:** PASS / FILTERED
**Earnings Summary:** [Verbatim Status & Earnings Summary paragraph]

**Overall:** PASS / FILTERED
**Peers:** See Tailwind Research section above.

---
```

### Confirmation

Before appending, present the extracted verdicts in a compact summary:
```
Extracted verdicts:
- TICKER1 — Price: PASS, Earnings: PASS, Overall: PASS
- TICKER2 — Price: PASS, Earnings: FILTERED, Overall: FILTERED

Ready to append Screening Results to Discovery_{DATE}.md. Confirm?
```

**STOP. Wait for explicit confirmation before proceeding to Step 3.**

---

## Step 3: Commit

Upon confirmation, append the full Screening Results section to `Discovery_{DATE}.md` immediately after the Tailwind Research section.

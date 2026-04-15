# Prompt — Screening Bridge

## Role
You are an expert financial analyst. Your task is to update the daily screening file with price and earnings verdicts. This prompt is run twice — once after `price.py` and once after `earnings.py`. It detects which stage to run based on the current Status in the screening file.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:

*   `Screening_{DATE}.md` — The current screening file. Read the Status section to determine which stage to run, and the Candidates section to identify all tickers.

Then, based on the Status section:
*   If **Price Screening: Pending** — also read `Data/screening/Price_Data_{DATE}.txt`
*   If **Price Screening: Complete** and **Earnings Screening: Pending** — also read `Data/screening/Earnings_{DATE}.txt`

**STOP. Do not proceed until the relevant files have been read.**

---

## Step 2: Determine Stage & Extract Verdicts

### Price Stage
*Applies when Price Screening: Pending*

For each candidate in the Candidates section of `Screening_{DATE}.md`:
*   Locate their entry in `Price_Data_{DATE}.txt`
*   Extract the PASS / FILTERED verdict and the verbatim Status & Price Summary paragraph
*   For any candidate that is FILTERED, their Earnings field will be set to "N/A — did not pass price screening"

### Earnings Stage
*Applies when Price Screening: Complete and Earnings Screening: Pending*

For each candidate whose Price verdict is PASS:
*   Locate their entry in `Earnings_{DATE}.txt`
*   Extract the PASS / FILTERED verdict and the verbatim Status & Earnings Summary paragraph
*   Set Overall verdict: PASS only if both price and earnings returned PASS; FILTERED if either returned FILTERED

**Multi-tag tickers:** A ticker may carry both `[LOSER]` and `[TAILWIND]` tags. Preserve all category memberships when updating the screening file — do not remove a ticker from a category because it also appears in another.

---

## Step 3: Propose Updates

Present a compact summary of proposed updates before writing anything:

**Price Stage:**
```
Price screening verdicts:
- TICKER1 — PASS
- TICKER2 — FILTERED
...
Ready to update Screening_{DATE}.md. Confirm?
```

**Earnings Stage:**
```
Earnings screening verdicts:
- TICKER1 — Price: PASS, Earnings: PASS, Overall: PASS
- TICKER2 — Price: PASS, Earnings: FILTERED, Overall: FILTERED
...
Ready to update Screening_{DATE}.md. Confirm?
```

**STOP. Wait for explicit confirmation before proceeding to Step 4.**

---

## Step 4: Commit

Upon explicit confirmation, update `Screening_{DATE}.md` as follows:

### Price Stage
1.  Populate the Screening Results section with the price verdict and verbatim Price Summary for each candidate.
2.  Set Earnings to "N/A — did not pass price screening" for any FILTERED candidates.
3.  Update the Status section: `Price Screening: Complete`.

### Earnings Stage
1.  Populate the Earnings verdict and verbatim Earnings Summary for each price-passed candidate.
2.  Set the Overall verdict for each candidate.
3.  Update the Status section: `Earnings Screening: Complete`.
4.  After committing, present a final summary of candidates that passed screening overall:

```
Screening complete. The following candidates passed:
- TICKER1 (LOSER)
- TICKER2 (TAILWIND)
...
Run prompt_screening_completion.md for each to initialize thesis files and update the tracker.
```

**STOP. Wait for user confirmation before committing.**

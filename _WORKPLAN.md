# Tracker Redesign — Work Plan
_Temporary file. Delete when all items are complete and committed._

---

## Context
Full redesign of the screening and tracker workflow. Two tools: screen.py (triage) → tracker (monitor + surface daily top 3 for thesis). All changes go on branch `claude/quirky-volta-cLSC6` (PR #12).

**New prompts cutoff: May 14, 2026** — theses run before this date use old format (no EV framework, no $/Dollar synthesis).

---

## Thesis Archive Format (agreed)

```
TICKER — $/Dollar — Date
  Numbers:    one sentence
  Narrative:  one sentence
  Projection: one sentence
  Catalyst:   one sentence (includes entry criteria, what to watch, invalidation signal)
```

---

## Done

- [x] `Scripts/screen.py` — 25 metrics including Mkt Cap and Debt/OCF; tested against AAPL
- [x] `Prompts/prompt_screen.md` — updated with Mkt Cap and Debt/OCF guidance (verbatim from prompt_the_numbers.md where possible)
- [x] Test run: 9-ticker batch (MELI, ACM, NU, FIS, ACN, VALE, CMCSA, M, DAL) appended to `Data/screening/Screen_2026-05-27.txt`
- [x] Fix: spread sign convention (Price−EPS, ≤0 = good signal)
- [x] `Stock_Tracker_backup_2026-05-28.md` — unified table (27 columns), all data populated via tracker_update_v2.py run against all 55 tickers
  - Column rename: vs_1Y → Price vs_1Y, vs_2Y → Price vs_2Y
  - Thesis Archive: 16 entries in 4-field format (IT, NFLX, BR, MU, NVDA, CDNS, SNPS, AMD, AMKR, AVGO, INTC, INTU, MRVL, KLAC, TSM, ASML)
  - Dropped (approved): LULU, CPB, BKH, MP, COP, CAG, UMAC
  - Restored (were dropped without approval): HON, LRCX, BE
  - Kept with monitoring rationale: INTC, SNPS (AI SC indicators), TEAM (accounting losses not operational), HON (restructuring noise), LRCX, BE
- [x] `Scripts/tracker_update_v2.py` — new script targeting backup file, 27-column unified table, all formulas matched to screen.py

---

## In Progress

- [ ] **`Prompts/prompt_tracker_review.md`** — full rewrite to new structure (approved direction)
  - Structure: Role → Step 0 → Step 1 → Step 2 (Analyze Now / Add to Position / Remove) → Step 3 → Metric Interpretations → AUTOMATION OVERRIDE
  - File/script refs stay as Stock_Tracker.md / tracker_update.py (backup→main rename pending)
  - Step 0: update column list to 27-column set
  - Step 1: remove Pipeline/Watchlist language; read unified # Ticker Tracker table
  - Analyze Now: unified ranking (no LOSER/TAILWIND split); Spread is primary, ROIC is #2, full table informs conviction holistically; output = Ticker | one sentence; earnings date tiebreaker when otherwise equal
  - Remove SC Layer Coverage entirely
  - Remove: no demote-to-watchlist; just Remove or Keep with caveat
  - Metric Interpretations: verbatim from prompt_screen.md (Spread, P/E Corr, Price, Earnings, P/E, P/OE, ROIC, OCF/NI, FCF, Revenue, Mkt Cap, Debt/OCF)
  - AUTOMATION OVERRIDE: keep verbatim
  - **CRITICAL: show full draft to user BEFORE editing file**

---

## Pending

### 1. Rename Stock_Tracker_backup → Stock_Tracker
- Once prompt is updated and tested
- Archive or delete original Stock_Tracker.md

### 2. Update `Prompts/prompt_screen.md` — ranking hierarchy
- Spread is primary but not the only ranking signal; ROIC is #2, full table informs conviction
- Current screen prompt language implies quality metrics only "confirm or disqualify" — needs to reflect holistic ranking (same correction applied to prompt_tracker_review.md)

---

## Column Reference (final agreed set)

### Screener (23 data columns)
Mkt Cap | Spread | P/E Corr | Price | Price vs_1Y | Price vs_2Y | EPS TTM | EPS vs_1Y | EPS vs_2Y | EPS QoQ (4Q) | P/E | P/OE | ROIC | ROIC Δ1Y | ROIC Δ2Y | OCF/NI | FCF TTM | FCF vs_1Y | FCF vs_2Y | Rev TTM | Rev vs_1Y | Rev vs_2Y | Debt/OCF

### Tracker (27 columns = screener + Next Earn + Tag + Thesis + $/Dollar)
All screener columns above + Next Earn | Tag | Thesis | $/Dollar

---

## Key Rules (session-specific)
- NO edits of any kind without explicit written user approval first
- Scripts: show output after running; do not commit test artifacts
- Prompts: show proposed changes in full before touching the file
- Commits: only after explicit user approval

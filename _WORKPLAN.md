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

- [x] `Scripts/screen.py` — new standalone screening script (23 metrics, writes `Data/screening/Screen_{DATE}.txt`)
- [x] `Prompts/prompt_screen.md` — new screening prompt (table → priority ranking → narratives → append to file)
- [x] Test run: 9-ticker batch (MELI, ACM, NU, FIS, ACN, VALE, CMCSA, M, DAL) with analysis appended to `Data/screening/Screen_2026-05-27.txt`
- [x] Fix: spread sign convention (Price−EPS, ≤0 = good signal)
- [x] Fix: stale header text in screen.py
- [x] `Stock_Tracker_backup_2026-05-28.md` — new tracker structure drafted (unified table, 27 columns, Thesis Archive section)

---

## In Progress

- [ ] **Thesis Archive cleanup** — `Stock_Tracker_backup_2026-05-28.md`
  - Flip `Thesis=—` and `$/Dollar=—` for 12 tickers: IBM, TEAM, ZM, NOW, META, WDAY, SAP, DPZ, AXON, BKH, RDDT, ORCL
  - Remove those 12 entries from Thesis Archive section
  - Reformat 16 kept entries to new 4-field format (Numbers / Narrative / Projection / Catalyst)
  - Populate 16 entries from actual thesis files

  **Keep (16):**
  - Post-May 14: IT, NFLX, CDNS, SNPS, AMD, AMKR, MU, NVDA, INTU, MRVL, AVGO, INTC
  - Pre-May 14 (kept): BR, TSM, KLAC, ASML

  **Remove (12):**
  - Re-run later: IBM, TEAM, ZM, NOW, META, WDAY, SAP
  - Stubs (never run): DPZ, AXON, BKH, RDDT, ORCL

---

## Pending

### 1. screen.py — add Mkt Cap and Debt/OCF
- Add `Mkt Cap` to script output (already fetched via profile endpoint)
- Add `Debt/OCF` to script output (total debt from balance sheet / OCF TTM)
- Add to SIGNAL section header in output file, or new section
- Update `prompt_screen.md` column guide and metric interpretations:
  - Mkt Cap: below $10B warrants more scrutiny (slower normalization, liquidity risk)
  - Debt/OCF: below 3x safe; above 5x distress risk; above 7x serious scrutiny

### 2. tracker_update.py — new column set
Current columns to REMOVE: `Yrs Profitable (5yr)`, `Op Margin %`, `Phase`, `Last Run`, `Status`, `Added`, `Thesis` (old file-link format)

New columns to ADD:
- `Spread` (Price vs_1Y − EPS vs_1Y) — primary signal
- `P/E Corr` (P/E Correlation 1Y — Pearson, monthly price vs TTM EPS)
- `vs_2Y` (price)
- `EPS TTM`
- `EPS vs_2Y`
- `P/OE` (P/Owner Earnings = Mkt Cap / (FCF TTM − SBC TTM))
- `ROIC Δ1Y` (pp)
- `ROIC Δ2Y` (pp)
- `OCF/NI`
- `FCF TTM`
- `FCF vs_2Y`
- `Rev TTM`
- `Rev vs_2Y`
- `Mkt Cap`
- `Debt/OCF`
- `Thesis` (Y / —)
- `$/Dollar` (manual, not computed by script)

Columns carried over unchanged: `vs_1Y`, `P/E`, `ROIC`, `EPS vs_1Y` (rename from EPS YoY), `EPS QoQ (4Q)`, `Rev vs_1Y`, `FCF vs_1Y`, `Next Earn`

**Note:** `P/E Corr` requires 12 months of daily prices + quarterly EPS — expensive but already computed in screen.py. Reuse same logic.

### 3. prompt_tracker_review.md — update to new structure
- Remove all Pipeline/Watchlist/Phase references — unified table now
- Update column names throughout (EPS YoY → EPS vs_1Y, etc.)
- Update LOSER/TAILWIND ranking criteria to reference `Spread` column directly
- Update SC Layer Coverage section to reflect unified table
- Remove `Status` references; replace with `$/Dollar` and `Thesis` columns
- Update "Analyze Now" output format to include Spread and $/Dollar
- Update "Remove" section — no more demote-to-watchlist, just Remove or keep

### 4. Rename Stock_Tracker_backup → Stock_Tracker
- Once tracker_update.py and prompt are updated and tested
- Archive or delete original Stock_Tracker.md

---

## Column Reference (final agreed set)

### Screener (23 data columns)
Mkt Cap | Spread | P/E Corr | Price | vs_1Y | vs_2Y | EPS TTM | EPS vs_1Y | EPS vs_2Y | EPS QoQ (4Q) | P/E | P/OE | ROIC | ROIC Δ1Y | ROIC Δ2Y | OCF/NI | FCF TTM | FCF vs_1Y | FCF vs_2Y | Rev TTM | Rev vs_1Y | Rev vs_2Y | Debt/OCF

### Tracker (27 columns = screener + Next Earn + Tag + Thesis + $/Dollar)
All screener columns above + Next Earn | Tag | Thesis | $/Dollar

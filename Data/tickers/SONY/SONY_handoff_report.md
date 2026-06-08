# Step 0 Handoff Report: SONY
**Date:** 2026-06-05

---

## Profile
**Company:** Sony Group Corporation
**Sector:** Technology / Consumer Electronics
**Market Cap:** ~$130B USD (NYSE ADR)
**CEO:** Hiroki Totoki
**Country:** JP
**Exchange:** NYSE (ADR)

---

## Peers
FMP returned: ACN, ADBE, AMAT, ARM, INTC, INTU, KLAC, QCOM, TXN
Note: These are generic Technology sector peers — not comparable entertainment/hardware conglomerates. Top peer used for financials.py: ACN.

---

## Scripts

| Script | Status | Output |
|---|---|---|
| price_earnings.py | ✓ | $22.03, vs1Y: -16%, GAAP P/E: n/a, EPS CAGR: -33.1% |
| analyst.py | ✓ | 1 analyst only (low coverage, treat as unreliable), median target $30.00 (+36% implied), 1 downgrade in 90d |
| news.py | ✓ | 10 Perigon stories + 30 FMP articles, ~3 months |
| ticker_reddit.py | ✓ | 12 posts fetched (r/stocks + r/ValueInvesting) |
| financials.py --peers ACN | ✓ | 5 annual + 5 quarterly periods; ACN peer included |
| footnotes.py | ✗ FAILED | Sony has no SEC 10-K/10-Q; files Form 20-F. No SONY_notes.md generated. |
| earnings_calls.py | ✓ | 2026Q4 (current) + 2026Q3 (prior); remarks + Q&A files written via Alpha Vantage |

---

## Source Material (International Company Adaptations)

| File | Status | Notes |
|---|---|---|
| SONY_mda.md | ✓ | Copied from user-provided SONY_MD&A2026.txt (FY2025 Consolidated Financial Results, May 8, 2026, IFRS basis, yen-denominated) |
| SONY_MD&A2026.txt | ✓ | Original source file, retained in SONY folder |
| SONY_mda_excerpts.md | ✓ | All 7 targets extracted via grep from SONY_MD&A2026.txt |
| SONY_notes.md | ✗ NOT AVAILABLE | Sony files Form 20-F. Footnotes and notes to financial statements are not in local files. |
| SONY_earnings_remarks.md | ✓ | Full transcript via Alpha Vantage (2026Q4 + Q3) |
| SONY_earnings_qa.md | ✓ | Full Q&A via Alpha Vantage |
| SONY_qa_questions.md | ✓ | 78 lines, substantive questions present |

---

## File Checklist

### Context Step
| File | Status |
|---|---|
| SONY_profile.json | ✓ |
| raw/SONY_price.json | ✓ |
| raw/SONY_earnings.json | ✓ |
| SONY_analyst.md | ✓ |
| SONY_news.md | ✓ |
| SONY_social.md | ✓ |
| SONY_mda_excerpts.md | ✓ |
| SONY_qa_questions.md | ✓ |
| SONY_peers.json | ✓ |

### Pass 1 / Pass 2
| File | Status |
|---|---|
| SONY_financial_analysis.md | ✓ |
| SONY_mda.md | ✓ |
| SONY_notes.md | ✗ Permanently absent (Form 20-F filer) |
| SONY_earnings_remarks.md | ✓ |
| SONY_earnings_qa.md | ✓ |

---

## Key Flags for Claude

1. **No notes.md** — Accounting footnotes unavailable. Revenue recognition policies, goodwill impairment assumptions, and segment accounting detail cannot be verified against primary source. Flag any conclusions that would normally require footnote verification.

2. **GAAP P/E shows n/a / EPS CAGR -33%** — Sony's reported EPS is suppressed by significant one-time items in FY25: Bungie impairments ¥120.1B, Pixomondo impairment/shutdown ¥27.1B, Sony Honda Mobility equity losses ¥44.9B, and a tax rate normalization (19%→26%) from absence of FY24 one-time tax benefits. Underlying operating earnings are materially higher. Use operating income and operating income margin as the primary earnings quality metrics.

3. **Reporting currency: yen** — All MD&A figures are in billions of yen (Bln Yen). FX rate assumption for FY26 forecast: ~¥150/$1. FX impact is disclosed by segment and is material — always note whether figures are reported or constant-currency.

4. **IFRS not US GAAP** — Financial statements follow IFRS Accounting Standards, not US GAAP. Segment operating income excludes unallocated corporate expenses and intersegment eliminations. "Adjusted OIBDA" is a non-IFRS metric used by management.

5. **Financial Services discontinued** — Sony spun off Sony Financial Group Inc. (SFGI) effective October 1, 2025. All continuing operations figures exclude this segment. FY24 comparatives have been restated. From Q3 FY25 onward, SFGI results flow through as equity method income/loss in operating income.

6. **Analyst coverage: 1 analyst only** — Consensus data is not reliable for SONY ADR via FMP. Treat the $30.00 target and any consensus ratings as unreliable.

7. **TSMC JV** — Sony announced a joint venture with TSMC around earnings day (referenced in analyst Q&A). This relates to the I&SS semiconductor business and is not detailed in the financial results document. Relevant for Pass 2 / catalyst assessment.

8. **Peers mismatch** — ACN was used as the financial comparison peer (FMP default). It is not a meaningful operational comparable. Peer financial analysis should be treated with low weight; use it for baseline financial structure reference only.

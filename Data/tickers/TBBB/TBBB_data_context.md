# Data Context: TBBB (BBB Foods Inc. / Tiendas 3B)
**Prepared:** 2026-08-12

---

## 1. Social / Reddit data

No social data is available for this ticker. `TBBB_social.md` was not produced. The SocialVault API returned posts for TBBB but encountered a null-body error on comment fetching that prevented the file from being written. The underlying posts found across r/stocks and r/ValueInvesting were limited (4 qualifying posts after date and score filtering). There is no Reddit sentiment signal to draw on for this analysis.

---

## 2. Filings — source and structure

TBBB (BBB Foods Inc.) is a **foreign private issuer** incorporated in the British Virgin Islands, listed on the NYSE. It files with the SEC under foreign issuer form types:

- **20-F** — annual report (equivalent to 10-K). The filing used here covers the **year ended December 31, 2025**, filed April 2, 2026.
- **6-K** — interim/current report (equivalent to 10-Q). The filing used here contains **Q1 2026 interim financials and MD&A** for the three-month period ended March 31, 2026.

The standard `footnotes.py` script only searches SEC EDGAR for 10-K and 10-Q form types and returned nothing for TBBB. Both filings were provided manually. The MD&A section was extracted from the 20-F (Item 5, lines 1708–2068) and from the 6-K (MD&A section, lines 1298–1750) using `sed`, without reading the full files. Notes to financial statements were extracted from the 20-F (Item 18, lines 3815–5960). These extracted files are at their standard paths:

- `TBBB_mda.md` — Item 5 of the 20-F (FY2025 annual MD&A, 361 lines)
- `TBBB_notes.md` — Item 18 of the 20-F (financial statements and notes, 2,146 lines)
- `TBBB_mda_6k.md` — Q1 2026 MD&A from the 6-K (431 lines, supplementary)
- `TBBB_mda_excerpts.md` — verbatim grep excerpts compiled across both filings

The original source files are at:
- `Data/tickers/TBBB/20-F.txt`
- `Data/tickers/TBBB/6-K June.txt`

---

## 3. Currency and accounting standard

All financial figures in TBBB's filings are denominated in **thousands of Mexican pesos (Ps.)** unless explicitly stated otherwise. USD equivalents are occasionally provided by management (e.g., "Ps.78.2 billion (US$4.4 billion)") but are not the primary unit.

TBBB reports under **IFRS**, not US GAAP. Key implications for analysis:

- **Leases:** IFRS 16 requires operating leases to be capitalized on the balance sheet as right-of-use assets with corresponding lease liabilities. This inflates both assets and financial costs (interest on leases) relative to US GAAP treatment. Financial costs in Q1 2026 were Ps.457,303 thousand, of which Ps.427,632 thousand was interest on leases — directly tied to store expansion, not debt financing.
- **Share-based compensation:** Non-cash. The Liquidity Event Share Plan (adopted February 2024, granted June 2025, quarterly vesting) drove a Ps.721,505 thousand charge in Q1 2026 vs. Ps.213,290 thousand in Q1 2025. Management presents adjusted EBITDA excluding this item.
- **No segment reporting:** TBBB operates as a single segment. No segment breakdown is disclosed.
- **Earnings calls:** Figures quoted by management in earnings calls are in billions of Mexican pesos (e.g., "$23 billion pesos" = Ps.23,000,000 thousand). These are consistent with the 6-K financials.

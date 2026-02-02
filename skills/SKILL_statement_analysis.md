# Financial Statement Analysis Skill

**⚠️ DRAFT - This skill file is a preliminary draft and may require refinement based on actual usage patterns.**

## Context

**Purpose:** Deep financial statement analysis to assess undervaluation and risk, establish projection baseline.

**Available Data:**
- `{TICKER}_statements.md` - Statement comparison tables (8 seeds, 13 priority metrics, note about 17 secondary)
- `GLOSSARY_seeds.md` - Baseline analysis guidance for 8 projection seeds
- `GLOSSARY_priority_metrics.md` - Interpretation guidance for 13 priority metrics
- `GLOSSARY_secondary_metrics.md` - Interpretation guidance for 17 secondary metrics
- Optional: `{TICKER}_tracking.md` if this is a follow-up analysis

---

## Analysis Framework

**Three-Dimension Analysis:** Apply to all metrics:
1. **Absolute Level & Peer Positioning** - Current value vs. historical average and vs. peers
2. **Trends & Divergences** - CAGR, slope, recent deltas
3. **Volatility & Outliers** - Consistency (CV) and anomalies

---

## Key Questions to Address

Analyze the statements markdown and address the following, using glossaries for interpretation guidance:

### 1. Projection Seeds Baseline (8 seeds)
Review `GLOSSARY_seeds.md` and the **Projection Seeds** section in statements markdown.

For each seed, apply three-dimension analysis:
- Revenue, COGS %, SG&A %, R&D %, D&A, CapEx, Total Debt, Working Capital Components
- What are the baseline patterns? (5-yr avg, CAGR, trends, volatility)
- Peer context? Concerning patterns?

### 2. Undervaluation Assessment (8 priority metrics)
Review `GLOSSARY_priority_metrics.md` and the **Priority Metrics: Undervaluation** section.

**Question:** Based solely on financials, is the stock potentially undervalued?

Analyze: Revenue trends, Operating Margin, Operating Cash Flow, Free Cash Flow, NCAV, ROTC, ROE, Operating Leverage

Apply three-dimension framework to each. What's the undervaluation case?

### 3. Risk Assessment (5 priority metrics)
Review `GLOSSARY_priority_metrics.md` and the **Priority Metrics: Risk** section.

**Question:** Is it risky?

Analyze: Debt/OCF, OCF/Net Income, Accruals Gap, D&A (peer comparison), Working Capital

Apply three-dimension framework to each. What are the key risks?

### 4. Secondary Metrics (if warranted)
Review `GLOSSARY_secondary_metrics.md` and JSON files if needed.

17 metrics grouped by: Operations (4), Financial Health (8), Efficiency (5)

Brief scan for anomalies - detail only if warranted.

### 5. Synthesis
- Is the stock undervalued? Is it risky? What's the verdict?
- What requires further investigation?
  - **Seed-linked items:** Affect projection confidence
  - **Non-seed items:** Other concerns (governance, competitive, regulatory, etc.)
  - Mark **[CRITICAL]** if high priority

---

## Output Guidance

Write `{TICKER}_ANALYSIS_statement.md` addressing the questions above. Consider this structure:

**TLDR: Investment Assessment**
- Undervaluation case (strong/moderate/weak - why?)
- Risk assessment (high/moderate/low - why?)
- Verdict and what's still unclear

**Analysis Sections:**
- Projection Seeds Baseline (address each of 8 seeds with three-dimension framework)
- Undervaluation Analysis (address each of 8 metrics - what's the case?)
- Risk Analysis (address each of 5 metrics - what are the concerns?)
- Secondary Metrics (brief scan - only detail anomalies)

**Investigation Items:**
- Seed-linked: Items affecting projection confidence (Seeds: X, Y) - mark [CRITICAL] if needed
- Non-seed: Other concerns (governance, competitive, etc.) - mark [CRITICAL] if needed

**Flexibility:** Let materiality drive depth. Elaborate on critical items, brief on standard items. Use evidence from the data.

---

## Notes

**Available Data:**
- Statements markdown: 8 seeds, 13 priority metrics (tables with historical data, statistics, peer comparison if available)
- Statistical fields: Current, 5-yr avg, CAGR, slope, recent Δ%, CV, outliers, YTD annualized
- Glossaries: Interpretation guidance for all metrics

**Remember:**
- This is qualitative interpretation of already-calculated metrics
- Three-dimension framework applies to all metrics
- Peer context (if available) is valuable
- Investigation items enable tracking and follow-up

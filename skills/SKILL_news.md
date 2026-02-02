# News Analysis Skill

**⚠️ DRAFT - This skill file is a preliminary draft and may require refinement based on actual usage patterns.**

## Prerequisites

**Before executing this skill, you must:**
1. Read this entire skill file - Contains workflow steps and output format requirements
2. Have completed statement analysis (projection seeds and investigation items established)

**Required Files:**
- `{TICKER}_tracking.md` - Analysis tracking (statement analysis must be complete)
- `{TICKER}_news_perigon.json` - Perigon Stories results (default: 3-month lookback)
- `{TICKER}_news_alphavantage.json` - AlphaVantage NEWS_SENTIMENT results (default: 3-month lookback)

**How to Generate News Files:**
```bash
# Default: 3 months
python scripts/ticker/news.py {TICKER}

# Custom lookback period
python scripts/ticker/news.py {TICKER} --months 6
```

**Data Location:** `data/stocks/{TICKER}/{TICKER}_news_*.json`

**Context Sources:**
- Primary: `{TICKER}_tracking.md` (projection seeds baseline & investigation items)
- Additional detail: `{TICKER}_ANALYSIS_statement.md` if needed for context

---

## Analysis Methodology

**Tool Guidance:**

News data is in JSON format (may be large files with many articles).

**Tool hierarchy:**
1. **Explore agent** (Task tool, subagent_type=Explore) - **Start here.** Best for processing large JSON files, extracting relevant articles, synthesizing across both sources
2. **Read tool** - For targeted reading of specific portions if Explore identifies something needing closer review

**Avoid:** Grep (not effective for JSON) and reading entire large JSON files directly (may hit context limits).

**Framework:**
Focus on three objectives:
1. **Projection seeds** - Extract material events affecting projection confidence for each seed
2. **Investigation items** - Address specific items flagged in prior analyses (both seed-linked and non-seed)
3. **Material events & sentiment** - Identify risks/catalysts and assess institutional sentiment

**Materiality Filtering:**
Script returns top articles from each API. Determine materiality during analysis based on impact on investigation items or projection seeds.

**Search Process:**
1. Use Explore agent to read and synthesize `{TICKER}_news_perigon.json` (aggregated stories)
2. Use Explore agent to read and synthesize `{TICKER}_news_alphavantage.json` (individual articles with sentiment scores)
3. Identify material events by impact on investigation items or projection seeds
4. Extract headlines, summaries, dates, sources with context

---

## Workflow

The analysis is conducted in 3 passes with pauses between key sections.

**Analysis Period:**
- Default: Last 3 months (or since most recent 10-K filing date, whichever is shorter)
- Sentiment focus: Last 30 days for current sentiment + full period for trend

**Tone/Length Guidance:** Elaborate on critical or anomalous items; be brief on standard items. Include evidence (headlines, dates, sources). Let importance drive length.

---

### Pass 1: Seed-First Review (External Perspective on Projection Seeds)

**Objective:** What external news validates or challenges projection confidence for each seed, and does news address seed-linked investigation items?

**Action:**
1. Read `{TICKER}_tracking.md` "Projection Seeds Baseline & Status" section (includes seed-linked investigation items)
2. Use Explore agent to read both JSON files and identify events affecting each projection seed
3. Extract material headlines/summaries with dates and sources
4. Note if seed-linked investigation items were addressed

**The 8 Projection Seeds:**
1. Revenue
2. COGS %
3. SG&A %
4. R&D %
5. Depreciation & Amortization
6. Capital Expenditures
7. Total Debt
8. Working Capital Components

**Begin writing** `{TICKER}_ANALYSIS_news.md`:
See Required Output Format section for structure.

**PAUSE** - User reviews

---

### Pass 2: Non-Seed Items, Material Events & Sentiment

**Objective:** Address non-seed investigation items and proactively identify material events and market sentiment

**Action:**
1. Read `{TICKER}_tracking.md` "Open Investigation Items - Non-Seed Items" section
2. Use Explore agent to search both JSON files for commentary addressing non-seed investigation items
3. Proactive search for material events (focus on external-only information not in company filings):
   - **M&A/Strategic:** Unannounced deals, rumors, partnerships (not yet disclosed)
   - **Competitive Dynamics:** Competitor moves, market disruption, industry trends
   - **Market Reaction:** Analyst upgrades/downgrades, significant price movements
   - **Regulatory/Legal:** External developments (not already in filings)

   *Skip items already covered by company disclosures (litigation, management changes in filings).*

4. Sentiment analysis (Perigon + AlphaVantage):
   - **Last 30 days:** Current sentiment (average score, trend direction)
   - **Full period trend:** Show monthly scores to identify improving/stable/deteriorating pattern
   - **Outlier events:** Identify extreme sentiment shifts with dates and causes
   - Note article count and source diversity

**Continue updating** `{TICKER}_ANALYSIS_news.md`:
See Required Output Format section for structure.

**PAUSE** - User reviews

---

### Pass 3: Synthesis & Thesis Impact

**Objective:** How does external news perspective affect the undervaluation thesis and projection confidence?

**Action:**
1. Synthesize findings from Passes 1-2
2. Assess overall narrative validation (where news validates vs contradicts company statements from filings/calls)
3. Identify key risks and catalysts
4. Assess projection confidence per seed based on all news findings

**Finalize** `{TICKER}_ANALYSIS_news.md`:
See Required Output Format section for structure.

**Update** `{TICKER}_tracking.md`:
- Mark resolved investigation items as [RESOLVED] (or remove if fully addressed)
- Add new investigation items discovered during analysis
- Update "Projection Seeds Baseline & Status" section with news insights

**PAUSE** - User reviews

---

## Required Output Format

`{TICKER}_ANALYSIS_news.md` structure (built progressively through Passes 1-3):

```markdown
# {TICKER} News Analysis

## TLDR
[Written in Pass 3]

**Key Findings:**
- [Material events affecting thesis with dates]
- [Where news validates vs. contradicts company narrative]

**Unresolved Items:**
- [Items not addressed by news coverage]

**Market Sentiment:** [Bullish/Neutral/Bearish] (Score: X, Trend: Improving/Stable/Deteriorating)

**Analysis Period:** {START_DATE} to {END_DATE}

---

## External Perspective on Projection Seeds

For each projection seed:

### {Seed Name}
**Projection Confidence:** [High/Medium/Low]
**Change from Prior:** [↑/↓/—] {Reason}
**Key Findings:** {Impact on projections; vs. historical baseline from tracking.md}
**Seed-Linked Investigation Items:** {Addressed/Still unresolved}

**Supporting News:**
> [{DATE}] - {Source}: {headline/summary}
> [{DATE}] - {Source}: {headline/summary or "No material news"}

---

## Open Items

### New Investigation Items
- [INVESTIGATE] Item description | Seeds: X, Y | Source: News Analysis (YYYY-MM-DD)
- [GAP] Item description (news silent) | Seeds: Z | Source: News Analysis (YYYY-MM-DD)
- [NEW] Material event description | [NON-SEED] Category | Source: News Analysis (YYYY-MM-DD)

### Material Events
[Only include material events not already captured in seed analysis - categories: M&A/Strategic, Competitive, Market Reaction, Regulatory/Legal]

**Event Title**
- **Date:** {DATE}
- **Source:** {Publication/API}
- **Description:** {Summary with context}
- **Impact on Thesis:** {Assessment}

> [{DATE}] - {Source}: {headline/summary}

---

## Sentiment Analysis

**Current Sentiment (Last 30 Days):**
- Average sentiment score: {score from -1 to +1}
- Trend: {Improving/Stable/Deteriorating}
- Article count: {N articles}
- Source diversity: {Count of unique sources}

**Full Period Sentiment Trend:**
| Month | Avg Score | Article Count | Notable Events |
|-------|-----------|---------------|----------------|
| {Month} | {score} | {count} | {event if applicable} |

**Outlier Events:**
[Events causing extreme sentiment shifts with dates and scores]

> [{DATE}] - {Source}: {headline causing outlier sentiment}

**Sentiment Breakdown by Source:**
- Perigon (aggregated stories): {Tone summary}
- AlphaVantage (individual articles): {Tone summary}
- Convergence/Divergence: {Where sources align or differ}

---

## Narrative Validation

**Where News Validates Company Statements:**
- [Area 1]: {Specific validation with citations}
- [Area 2]: {Specific validation with citations}

**Where News Contradicts or Challenges:**
- [Area 1]: {Specific contradiction with citations}
- [Area 2]: {Specific contradiction with citations}

**Gaps in Coverage:**
- [Topic 1]: {Where news is silent despite relevance}
- [Topic 2]: {Where news is silent despite relevance}

---

## Unresolved Items
{Detailed breakdown of Open Items - gaps in news coverage, areas where news was silent, items carried forward from tracking.md}

---

## Projection Confidence Assessment

**Per-Seed Confidence:**
| Seed | Prior Confidence | News Impact | This Analysis | Change | Key Factor |
|------|------------------|-------------|---------------|--------|------------|
| Revenue | Medium | Validates | High | ↑ | Analyst reports confirm growth |
| COGS | Medium | Silent | Medium | — | No news coverage |
| ... | ... | ... | ... | ... | ... |

**Impact on Investment Thesis:**
- **Strengths:** [Positive signals, catalysts, validation from news]
- **Weaknesses:** [Risks, contradictions, concerns from news]
- **Net Assessment:** [Overall impact on thesis - does news support undervaluation case?]

**Key Risks Identified:**
1. {Risk with citation}
2. {Risk with citation}

**Key Catalysts Identified:**
1. {Catalyst with citation}
2. {Catalyst with citation}
```

---

## Notes

**Data Sources:**
- Perigon API: Aggregated stories with source clustering
- AlphaVantage NEWS_SENTIMENT: Individual articles with sentiment scores (-1 to +1)
- Both sources provide: headline, summary, date, source, sentiment (AlphaVantage only)

**Materiality Thresholds:**
- Focus on events affecting fundamentals, not just price movements
- Require multiple sources for unconfirmed rumors
- Prioritize analyst commentary on financial metrics
- External events (not in filings) take precedence

**Tool Usage Best Practices:**
- Use Explore agent for initial synthesis across large JSON files
- Extract specific quotes/headlines for evidence
- Cross-reference between Perigon and AlphaVantage for validation
- Note when sources agree vs. diverge on sentiment

**News vs. Company Narrative:**
- News provides external validation or challenge
- Contradictions warrant investigation (who's right?)
- Gaps in coverage may indicate areas where company narrative is unchallenged
- Analyst perspective (in news) vs. management perspective (in filings/calls)

**Integration with Other Analyses:**
- Statement analysis establishes baseline and investigation items
- News analysis addresses those items from external perspective
- Sentiment analysis (multi-source) adds social media context
- Tracking document ties everything together

**Flexibility:**
- Adjust analysis period based on significant events (e.g., recent earnings release, merger announcement)
- Weight sentiment based on source credibility and relevance
- Some seeds may have little to no news coverage (that's informative too)

---

**⚠️ DRAFT NOTICE:** This skill file is a preliminary draft. Expected refinements:
- Materiality threshold calibration for different types of news
- Source reliability weighting (established publications vs. smaller outlets)
- Sentiment score interpretation guidelines
- Integration patterns with statement and sentiment analyses

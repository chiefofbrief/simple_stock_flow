# Skills Directory

This directory contains analysis skill files for stock analysis workflows. Each skill file provides structured guidance for a specific analysis type.

**⚠️ All skill files are currently in DRAFT status and may require refinement based on actual usage patterns.**

---

## Skill Files Overview

| Skill File | Purpose | Prerequisites | Output |
|------------|---------|---------------|---------|
| `SKILL_screening.md` | Preliminary fundamental screening | Price + earnings data | Screening decision (PASS/MAYBE/FAIL) |
| `SKILL_statement_analysis.md` | Deep financial statement analysis | Statements markdown | Qualitative analysis + investigation items |
| `SKILL_news.md` | News sentiment and validation | News JSON files | News analysis + narrative validation |
| `SKILL_sentiment_analysis.md` | Multi-source sentiment synthesis | Sentiment markdown | Cross-source sentiment analysis |

---

## Analysis Workflow

### Recommended Sequence

```
1. Discovery (scripts/discovery.py)
   └─ Identify candidates from market scan

2. Screening (SKILL_screening.md)
   └─ Quick filter: Price behavior + earnings trends + P/E analysis
   └─ Decision: PASS / MAYBE / FAIL

3. Statement Analysis (SKILL_statement_analysis.md)
   └─ Deep dive: 8 projection seeds + 13 priority metrics
   └─ Output: Investigation items + projection confidence

4. News Analysis (SKILL_news.md) [Optional]
   └─ Standalone: Institutional perspective from news
   └─ Output: Narrative validation + sentiment

   OR

   Sentiment Analysis (SKILL_sentiment_analysis.md)
   └─ Comprehensive: News + Reddit + Social media
   └─ Output: Multi-source sentiment + cross-source analysis

5. Synthesis
   └─ Combine all analyses for investment thesis
```

---

## Skill File Structure

Each skill file follows a consistent structure:

```markdown
# {Skill Name}

**⚠️ DRAFT**

## Prerequisites
- Required files
- How to generate data
- Context sources

## Analysis Methodology
- Framework
- Tool guidance
- Materiality filtering

## Workflow
- Pass-by-pass structure
- PAUSE points for review
- Progressive output building

## Required Output Format
- Detailed markdown template
- Sections and structure

## Notes
- Best practices
- Tool usage
- Flexibility guidance
```

---

## Data Flow

### Screening Phase
```
prices.py → {TICKER}_prices.json
earnings.py → {TICKER}_earnings.json
valuation.py → Terminal output
                     ↓
              SKILL_screening.md
                     ↓
              Screening Decision
```

### Statement Analysis Phase
```
financial_statements.py → {TICKER}_statements.md
                                    ↓
                         SKILL_statement_analysis.md
                                    ↓
                         {TICKER}_ANALYSIS_statement.md
                         {TICKER}_tracking.md (created/updated)
```

### Sentiment Phase (Option A: News Only)
```
news.py → {TICKER}_news_*.json
                 ↓
          SKILL_news.md
                 ↓
          {TICKER}_ANALYSIS_news.md
          {TICKER}_tracking.md (updated)
```

### Sentiment Phase (Option B: Multi-Source)
```
sentiment.py → {TICKER}_sentiment.md
                      ↓
           SKILL_sentiment_analysis.md
                      ↓
           {TICKER}_ANALYSIS_sentiment.md
           {TICKER}_tracking.md (updated)
```

---

## Key Concepts

### Projection Seeds
8 fundamental metrics used for forward projections:
1. Revenue
2. COGS %
3. SG&A %
4. R&D %
5. Depreciation & Amortization
6. Capital Expenditures
7. Total Debt
8. Working Capital Components

### Investigation Items
Flagged questions or concerns from analysis, tracked in `{TICKER}_tracking.md`:
- **Seed-Linked:** Items affecting specific projection seeds
- **Non-Seed:** General concerns (governance, competitive, regulatory, etc.)
- **Critical:** High-priority items requiring resolution

### Three-Dimension Analysis Framework
Applied to all financial metrics:
1. **Absolute Level & Peer Positioning** - Current value vs. historical and vs. peers
2. **Trends & Divergences** - CAGR, slope, recent changes
3. **Volatility & Outliers** - Consistency (CV) and anomalies

---

## Usage Guidelines

### When to Use Each Skill

**SKILL_screening.md:**
- Screening multiple candidates quickly
- Before committing to deep analysis
- When you need a go/no-go decision

**SKILL_statement_analysis.md:**
- After passing screening
- When you need projection baseline
- Core analysis for any stock

**SKILL_news.md:**
- When news is the primary external source
- For institutional perspective only
- Faster than multi-source sentiment

**SKILL_sentiment_analysis.md:**
- When you need comprehensive sentiment view
- Cross-source validation important
- Retail + institutional + consumer perspective

### Skill File Flexibility

These are **guidance documents**, not rigid scripts:
- Adapt workflows to the specific situation
- Skip sections if not applicable
- Adjust depth based on materiality
- Combine insights across skills

### Tool Recommendations

**For JSON files (news data):**
- Start with Explore agent (Task tool)
- Use Read tool only for targeted sections

**For markdown files (statements, sentiment):**
- Read tool is sufficient
- Direct reading of structured content

**For analysis:**
- Focus on materiality, not completeness
- Cite specific evidence
- Let importance drive length

---

## Output Locations

| Output Type | Location | Filename Pattern |
|-------------|----------|------------------|
| Screening | Not saved to file | Terminal or redirected |
| Statement Analysis | `data/analysis/{TICKER}/` | `{TICKER}_ANALYSIS_statement.md` |
| News Analysis | `data/analysis/{TICKER}/` | `{TICKER}_ANALYSIS_news.md` |
| Sentiment Analysis | `data/analysis/{TICKER}/` | `{TICKER}_ANALYSIS_sentiment.md` |
| Tracking Document | `data/analysis/{TICKER}/` | `{TICKER}_tracking.md` |

---

## Draft Status & Feedback

**All skill files are in DRAFT status.**

Expected refinements:
- Materiality thresholds
- Decision criteria calibration
- Tool usage patterns
- Output format optimization
- Cross-skill integration

Feedback on actual usage will inform future versions.

---

## Related Documentation

- `CONTEXT_MAP.md` - Repository structure and script purposes
- `setup/COMMANDS.md` - CLI commands and usage examples
- Individual skill files - Detailed workflow guidance

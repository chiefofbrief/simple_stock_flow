# Skills Directory

Analysis skill files provide structured guidance for stock analysis workflows. Think of these as prompts with context rather than rigid instructions.

**⚠️ All skill files are currently in DRAFT status and may require refinement based on actual usage patterns.**

---

## Skill Files Overview

| Skill File | Purpose | Key Questions |
|------------|---------|---------------|
| `SKILL_screening.md` | Preliminary screening | Price behavior, earnings trends, P/E positioning, price-earnings correlation |
| `SKILL_statement_analysis.md` | Deep financial analysis | 8 projection seeds, 8 undervaluation metrics, 5 risk metrics |
| `SKILL_news.md` | News coverage analysis | Material events, investigation items, narrative validation, sentiment |
| `SKILL_sentiment_analysis.md` | Multi-source sentiment | Cross-source synthesis, material themes, brand perception |

---

## Analysis Workflow

**Recommended Sequence:**

```
Discovery → Screening → Statement Analysis → Sentiment/News → Synthesis
```

1. **Discovery** (`scripts/discovery.py`) - Identify candidates from market scan
2. **Screening** (`SKILL_screening.md`) - Quick filter: Is this worth deeper analysis?
3. **Statement Analysis** (`SKILL_statement_analysis.md`) - Deep dive on financials
4. **Sentiment/News** - External perspective:
   - `SKILL_news.md` - News only (institutional perspective)
   - OR `SKILL_sentiment_analysis.md` - Multi-source (news + social media)
5. **Synthesis** - Combine analyses for investment thesis

---

## Design Philosophy

**Flexibility over Prescription:**
- Skill files provide questions to address, not rigid steps
- Let materiality drive depth of analysis
- Adapt format to the situation
- Trust the LLM to handle nuance

**Context over Instructions:**
- Reference external resources (glossaries, tracking docs)
- Provide framework, not deterministic rules
- Guidelines, not hard requirements

**Key Concepts:**
- **Projection Seeds**: 8 fundamental metrics for forward projections
- **Investigation Items**: Flagged questions tracked in `{TICKER}_tracking.md`
- **Three-Dimension Analysis**: Absolute level, trends, volatility (for statement metrics)

---

## Data Flow

### Screening
```
prices.py + earnings.py + valuation.py → SKILL_screening.md
```

### Statement Analysis
```
financial_statements.py → {TICKER}_statements.md + Glossaries → SKILL_statement_analysis.md
```

### Sentiment Analysis
```
sentiment.py → {TICKER}_sentiment.md → SKILL_sentiment_analysis.md
OR
news.py → {TICKER}_news_*.json → SKILL_news.md
```

---

## Output Locations

| Analysis Type | Output Location | Filename |
|---------------|-----------------|----------|
| Screening | Not saved | Terminal or redirected |
| Statement Analysis | `data/analysis/{TICKER}/` | `{TICKER}_ANALYSIS_statement.md` |
| News Analysis | `data/analysis/{TICKER}/` | `{TICKER}_ANALYSIS_news.md` |
| Sentiment Analysis | `data/analysis/{TICKER}/` | `{TICKER}_ANALYSIS_sentiment.md` |
| Tracking Document | `data/analysis/{TICKER}/` | `{TICKER}_tracking.md` |

---

## Related Documentation

- `CONTEXT_MAP.md` - Repository structure and script purposes
- `setup/COMMANDS.md` - CLI commands and usage examples
- Glossaries (to be added) - Interpretation guidance for metrics

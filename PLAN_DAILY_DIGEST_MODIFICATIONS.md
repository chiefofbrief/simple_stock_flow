# Daily Digest Modifications — Implementation Plan

## Agreed Changes

### 1. Remove r/options from Reddit module
- **Status:** NOT DONE (previous session froze before saving)
- **File:** `scripts/market/reddit.py`
- **Change:** Line 83 — change `SUBREDDITS = ["ValueInvesting", "stocks", "options"]` to `SUBREDDITS = ["ValueInvesting", "stocks"]`
- **Also update:** Docstring lines 9-12 (remove r/options mention), line 40 (API cost from 3 to 2 credits)
- **Rationale:** r/options is strategy/education focused, not useful for identifying stocks to screen

### 2. Drop WSJ entirely
- **Status:** NOT DONE
- **Files affected:**
  - `scripts/discovery.py` — Remove `'wsj'` from `DAILY_ORDER` (line 30) and `WEEKLY_ORDER` (line 33). Remove `'wsj'` from `cmds` dict (line 46). Remove `'wsj'` from the `if module == 'barrons' or module == 'wsj'` block (line 53). Remove `--wsj` argparse flag (line 101).
  - `scripts/market/wsj.py` — Leave file in place (no deletion needed), just disconnect from discovery.py
- **Rationale:** WSJ Markets is redundant with Barron's (both Dow Jones properties). The new Perigon AI module with `sourceGroup=top50tech` covers 50 tech sources including WSJ, making standalone WSJ fully redundant.

### 3. Create new ai_news.py module (Perigon Articles + Vector Search)
- **Status:** NOT DONE (file was never written despite todo saying "completed")
- **File to create:** `scripts/market/ai_news.py`
- **API Budget:** 2 Perigon queries max (1 Articles/Stories boolean + 1 Vector semantic). Combined with 1 existing Barron's query = 3 total daily Perigon calls (well within 150/month free tier: 3/day * 30 days = 90).
- **Pattern:** Follow `scripts/market/barrons.py` structure (same retry logic, --markdown flag, --days flag, rich terminal output)
- **Output limiting:** Match Barron's approach — default 10 results max per query, configurable with --count

#### Query 1: Perigon Articles endpoint (boolean search)
- **Endpoint:** `GET https://api.goperigon.com/v1/all`
- **Key params:**
  - `sourceGroup=top50tech` (50 major tech publications)
  - `category=Tech,Business`
  - `excludeLabel=Opinion,Paid News`
  - `showReprints=false`
  - `sortBy=date`
  - `size=10`
- **Boolean query (q param):**
  ```
  ("artificial intelligence" OR "AI" OR "machine learning" OR "GPU" OR "data center" OR "generative AI" OR "large language model" OR "HBM" OR "custom silicon") AND ("revenue" OR "contract" OR "partnership" OR "earnings" OR "growth" OR "deployment" OR "investment" OR "CapEx" OR "infrastructure")
  ```
- **Query rationale:** Terms drawn from SESSION_NOTES.md and ai_stock_analysis.md:
  - AI ecosystem layers: compute/chips, infrastructure/power, models/tools, applications
  - Key themes: HBM memory constraints, custom silicon (TPUs/Trainium), data center buildout, CapEx spending
  - Business-focused AND clause filters out pure research/opinion, targets actionable business developments

#### Query 2: Perigon Vector Search endpoint (semantic)
- **Endpoint:** `POST https://api.goperigon.com/v1/vector/news/all`
- **Payload:**
  ```json
  {
    "prompt": "publicly traded companies with growing AI revenue, new AI product launches, AI infrastructure investments, data center expansion, GPU and memory chip demand, or significant AI-related business developments",
    "size": 10
  }
  ```
- **Vector rationale:** Catches emerging companies and themes the boolean query misses. From SESSION_NOTES: wafer bidding wars, optical interconnects, physical AI, AI agent traffic — themes that don't map cleanly to boolean keywords.

#### Output format (--markdown mode):
```markdown
## AI & Tech News (Perigon)
_Top articles from {date range} across 50+ tech sources_

### Articles Search
#### 1. {title}
_{date}_
<{url}>
{description}
**Source:** {source domain} | **Topics:** {topics}

---

### Semantic Search
#### 1. {title}
...
```

### 4. Keep International Intrigue
- **Status:** DONE (no changes needed)

### 5. Update discovery.py to integrate ai_news
- **Status:** NOT DONE
- **File:** `scripts/discovery.py`
- **Changes:**
  - `DAILY_ORDER`: Change from `['movers', 'barrons', 'wsj', 'intrigue', 'reddit']` to `['movers', 'barrons', 'ai_news', 'intrigue', 'reddit']`
  - `WEEKLY_ORDER`: Change from `['macro', 'movers', 'barrons', 'wsj', 'intrigue', 'reddit']` to `['macro', 'movers', 'barrons', 'ai_news', 'intrigue', 'reddit']`
  - `cmds` dict: Replace `'wsj'` entry with `'ai_news': [sys.executable, 'scripts/market/ai_news.py', '--markdown']`
  - Timeframe logic: `ai_news` should use `--days` like barrons (1 for daily, 7 for weekly)
  - argparse: Replace `--wsj` flag with `--ai-news` flag
  - Remove any remaining references to wsj in the module

### 6. Commit and push
- **Branch:** `claude/daily-digest-modifications-iSCYm`

---

## Implementation Order
1. Edit `scripts/market/reddit.py` (remove r/options)
2. Create `scripts/market/ai_news.py` (new module)
3. Edit `scripts/discovery.py` (drop WSJ, add ai_news)
4. Test: `python scripts/market/ai_news.py --markdown` (requires PERIGON_API_KEY)
5. Test: `python scripts/discovery.py --daily` (full integration test, requires all API keys)
6. Commit all changes and push to branch

## Decisions Made (for context)
- **DeepLearning.AI newsletter:** Skipped. Weekly cadence doesn't fit daily digest. User reads it manually.
- **WSJ Tech RSS swap:** Rejected in favor of Perigon AI module, which queries 50+ tech sources (including WSJ) with precise filtering.
- **Perigon query approach:** Query-based (boolean + semantic), NOT ticker-based. More flexible, catches emerging companies without maintaining a ticker list.
- **API budget:** Hard limit of 3 Perigon queries/day total (1 Barron's + 2 AI news). 90/month well within 150 free tier.

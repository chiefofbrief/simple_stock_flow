# Commands

## Setup

```bash
pip install tabulate requests rich curl_cffi beautifulsoup4 html2text lxml python-dateutil
```

---

## Quick Workflow

### 1. News

Runs losers, Barron's, WSJ, International Intrigue, and Reddit. Saves to "News_YYYY-MM-DD.md" with "Peter's Digest" header.

```bash
(echo "# Peter's Digest" && echo "Generated: $(date)" && echo "---" && python SCRIPT_losers_actives.py && python SCRIPT_barrons_news.py --days 1 --markdown && python SCRIPT_wsj_markets.py --days 1 --markdown && python SCRIPT_intl_intrigue.py --markdown && python SCRIPT_reddit_top_posts.py --timeframe day --markdown) > "News_$(date +%Y-%m-%d).md"
```

---

## Individual Scripts

### SCRIPT_losers_actives.py
Biggest stock losers and most active stocks.
```bash
python SCRIPT_losers_actives.py
```
Requires: `FMP_API_KEY`, `ALPHAVANTAGE_API_KEY`

### SCRIPT_barrons_news.py
Latest Barron's articles via Perigon API.
```bash
python SCRIPT_barrons_news.py [--count N] [--days N] [--all] [--markdown]
```
- `--count N` — Number of articles (default: 50)
- `--days N` — Days back (default: 1)
- `--all` — Show all articles
- `--markdown` — Output raw Markdown (useful for saving to file)

Requires: `PERIGON_API_KEY`

### SCRIPT_wsj_markets.py
WSJ Markets news via RSS.
```bash
python SCRIPT_wsj_markets.py [--summary] [--count N] [--days N] [--markdown]
```
- `--summary` — Headlines only
- `--count N` — Limit articles (default: 50)
- `--days N` — Filter to articles from past N days (default: 1 for today + yesterday)
- `--markdown` — Output raw Markdown

### SCRIPT_intl_intrigue.py
International Intrigue newsletter.
```bash
python SCRIPT_intl_intrigue.py [--summary] [--markdown]
```
- `--summary` — Show brief summary only
- `--markdown` — Output raw Markdown

### SCRIPT_reddit_top_posts.py
Top posts from finance subreddits.
```bash
python SCRIPT_reddit_top_posts.py [--count N] [--timeframe T] [--markdown]
```
- `--count N` — Posts per subreddit (default: 15)
- `--timeframe` — hour, day, week, month, year, all (default: day)
- `--markdown` — Output raw Markdown

Requires: `SOCIAVAULT_API_KEY`

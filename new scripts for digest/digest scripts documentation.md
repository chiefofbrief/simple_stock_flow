# Digest Scripts Documentation

All scripts live in `new scripts for digest/`. Output goes to `data/digest/`.

---

## peters_digest_2026.py — Orchestrator

Runs all section scripts in sequence (macro → intrigue → barrons → wsj → tech_feeds), assembles their stdout into a single markdown file, and writes it to disk.

**Run:**
```
python "new scripts for digest/peters_digest_2026.py"
```

**Output:** `data/digest/Peters_Digest_YYYY-MM-DD.md`

**Env vars required:** `FMP_API_KEY`, `PERIGON_API_KEY`

**External endpoints:** None (subprocess orchestrator only)

---

## macro.py — Macro Dashboard

Fetches market data, treasury yields, economic indicators, sector performance, and upcoming high-impact economic events.

**Run:**
```
python "new scripts for digest/macro.py" --markdown
```

**Output:** Markdown printed to stdout:
- `## Macro Dashboard` — SPY + commodities table (Level, 1D%, MoM%, vs 50-SMA)
- `### Treasury Yields` — 10-Year and 2-Year yields with 1D and MoM delta
- `### Last Reported Economic Data` — Unemployment rate and CPI index
- `### Upcoming High-Impact Events (7 Days)` — Up to 5 events
- `## Sector Discovery` — Top 3 and Bottom 3 sectors by average daily change

**Env vars required:** `FMP_API_KEY`

**Endpoints:**
| Endpoint | Purpose |
|:---|:---|
| `https://financialmodelingprep.com/stable/quote` | Current price/change for SPY and commodities (GCUSD, BZUSD, CPER, UNG) |
| `https://financialmodelingprep.com/stable/technical-indicators/sma` | 50-day SMA and historical prices for MoM change |
| `https://financialmodelingprep.com/stable/treasury-rates` | 10-Year and 2-Year Treasury yields |
| `https://financialmodelingprep.com/stable/sector-performance-snapshot` | Sector average daily performance |
| `https://financialmodelingprep.com/stable/economic-calendar` | Upcoming 7-day high-impact economic events |
| `https://financialmodelingprep.com/stable/economic-indicators` | `unemploymentRate` and `CPI` most recent readings |

---

## intrigue.py — International Intrigue Newsletter

Scrapes the International Intrigue archive and fetches the most recent newsletter post.

**Run:**
```
python "new scripts for digest/intrigue.py"
python "new scripts for digest/intrigue.py" --date YYYY-MM-DD
```

Without `--date`: fetches the most recent post. With `--date`: fetches that date; falls back to most recent if no match.

**Output:** Markdown printed to stdout:
- `## International Intrigue`
- `### [Post Title]` with date and full article body (HTML converted to markdown, links/images stripped)

**Env vars required:** None

**Endpoints (scraped, no API key):**
| URL | Purpose |
|:---|:---|
| `https://archives.internationalintrigue.io/` | Archive index |
| `https://archives.internationalintrigue.io/p/[slug]` | Individual post pages |

**Dependencies:** `curl_cffi`, `beautifulsoup4`, `html2text`

---

## barrons.py — Barron's News

Fetches Barron's articles published in the last 24 hours via Perigon API. Deduplicates by URL path and description. Timestamps converted to ET.

**Run:**
```
python "new scripts for digest/barrons.py"
python "new scripts for digest/barrons.py" --count 25
```

**Output:** Markdown printed to stdout:
- `## Barron's`
- Numbered list: title, ET timestamp, link, description (truncated to 300 chars)

**Env vars required:** `PERIGON_API_KEY`

**Endpoints:**
| Endpoint | Purpose |
|:---|:---|
| `https://api.goperigon.com/v1/all` | `source: barrons.com`, `sortBy: pubDate`, `from: 24h ago`, `size: 100` |

---

## wsj.py — Wall Street Journal News

Fetches WSJ articles published in the last 24 hours via Perigon API. Deduplicates by URL path and description. Timestamps converted to ET.

**Run:**
```
python "new scripts for digest/wsj.py"
python "new scripts for digest/wsj.py" --count 25
```

**Output:** Markdown printed to stdout:
- `## Wall Street Journal`
- Numbered list: title, ET timestamp, link, description (truncated to 300 chars)

**Env vars required:** `PERIGON_API_KEY`

**Endpoints:**
| Endpoint | Purpose |
|:---|:---|
| `https://api.goperigon.com/v1/all` | `source: wsj.com`, `sortBy: pubDate`, `from: 24h ago`, `size: 100` |

---

## tech_feeds.py — Tech & Industry Aggregator

Runs all six tech source scripts and outputs a combined `## Tech & Industry` section. Each source is a `###` subsection.

**Run:**
```
python "new scripts for digest/tech_feeds.py"
```

**Output:** Markdown printed to stdout:
- `## Tech & Industry`
- `### TrendForce`, `### Data Center Dynamics`, `### SiliconAngle`, `### The Robot Report`, `### Power Magazine`, `### Fierce Network`
- Each source: numbered list of articles with title, ET timestamp, link, description
- Sources with no articles in the last 24 hours are skipped

**Env vars required:** `PERIGON_API_KEY` (for TrendForce only)

**External endpoints:** None (subprocess aggregator only)

---

## trendforce.py — TrendForce

Scrapes TrendForce news articles published in the last 24 hours directly from their website.

**Run:**
```
python "new scripts for digest/trendforce.py" [--count 20]
```

**Output:** `### TrendForce` — numbered article list with title, date, and link (default 20; no descriptions, TrendForce doesn't expose them on the listing page)

**Env vars required:** None

**Endpoints:**
| URL | Purpose |
|:---|:---|
| `https://www.trendforce.com/news/` | News listing page — scrapes `div.insight-list-item` containers |

**Dependencies:** `curl_cffi`, `beautifulsoup4`

---

## dcd.py — Data Center Dynamics

Fetches DCD articles published in the last 24 hours via RSS.

**Run:**
```
python "new scripts for digest/dcd.py" [--count 20]
```

**Output:** `### Data Center Dynamics` — numbered article list (default 20)

**Env vars required:** None

**Dependencies:** `feedparser`

**Endpoints:**
| URL | Purpose |
|:---|:---|
| `https://www.datacenterdynamics.com/en/rss/` | RSS feed |

---

## siliconangle.py — SiliconAngle

Fetches SiliconAngle articles published in the last 24 hours via RSS.

**Run:**
```
python "new scripts for digest/siliconangle.py" [--count 20]
```

**Output:** `### SiliconAngle` — numbered article list (default 20)

**Env vars required:** None

**Dependencies:** `feedparser`

**Endpoints:**
| URL | Purpose |
|:---|:---|
| `https://siliconangle.com/rss/` | RSS feed |

---

## robotreport.py — The Robot Report

Fetches Robot Report articles published in the last 24 hours via RSS.

**Run:**
```
python "new scripts for digest/robotreport.py" [--count 10]
```

**Output:** `### The Robot Report` — numbered article list (default 10)

**Env vars required:** None

**Dependencies:** `feedparser`

**Endpoints:**
| URL | Purpose |
|:---|:---|
| `https://www.therobotreport.com/rss/` | RSS feed |

---

## powermag.py — Power Magazine

Fetches Power Magazine articles published in the last 24 hours via RSS.

**Run:**
```
python "new scripts for digest/powermag.py" [--count 10]
```

**Output:** `### Power Magazine` — numbered article list (default 10)

**Env vars required:** None

**Dependencies:** `feedparser`

**Endpoints:**
| URL | Purpose |
|:---|:---|
| `https://www.powermag.com/rss/` | RSS feed |

---

## fierce.py — Fierce Network

Fetches Fierce Network newsletter editions published in the last 24 hours via Kill the Newsletter Atom feed. Skips confirmation/welcome emails. Headlines only (no body content).

**Run:**
```
python "new scripts for digest/fierce.py" [--count 10]
```

**Output:** `### Fierce Network` — numbered list of newsletter titles with ET timestamp and link (default 10)

**Env vars required:** None

**Endpoints:**
| URL | Purpose |
|:---|:---|
| `https://kill-the-newsletter.com/feeds/y10af23zprp47havfsqx.xml` | Kill the Newsletter Atom feed |

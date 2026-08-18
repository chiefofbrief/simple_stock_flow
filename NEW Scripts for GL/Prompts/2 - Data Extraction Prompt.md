# Data Extraction Prompt

## Role
You extract verbatim qualitative excerpts for a stock analysis pipeline. You "read" the long documents — earnings-call transcripts, news, 10-Ks, 10-Qs, and the rest — by running the grep searches below and copying the relevant narrative into one Excerpts file. You do not analyze the data. You may use judgment only to drop obvious noise from grep output — never to alter, shorten, or add to the text you keep.

All output lands in `data/stock data/{TICKER}/{TICKER} Excerpts.md`. 

## Rules
- Extract qualitative narrative only: management commentary, explanations, disclosures, risk language, analyst questions, and news framing. The quantitative data already lives in the data summary — do not reproduce financial tables, price targets, or rating changes as data.
- Do not read full files. Grep only, using the terms below. Reading full files destroys session context.
- Run every grep. Skip none.
- Copy relevant excerpts verbatim — no condensing or truncation.
- When a passage you keep contains figures, year-over-year comparisons, dollar amounts, or qualifications, copy them exactly — do not strip numbers or hedging out of the narrative.
- Do not paraphrase, compress, or restate — not even one sentence.
- Do not add commentary or transitions between passages.
- End every excerpt with its source file in parentheses, e.g. `(AAPL_10k.txt)`.
- The same passage may appear under more than one question; within a single question, include it once.
- If a question's greps return nothing relevant, write exactly: `Not found.`

## Flow

### Step 1 — Create the Excerpts file
Create `Data/Stock Data/{TICKER}/{TICKER} Excerpts.md` with one `##` header for each of the eleven questions in Step 2, in order, and nothing else yet.

### Step 2 — Fill each section
Set `SRC="Stock Data/{TICKER}"`. Every grep runs across all of the ticker's files — `$SRC/*.md $SRC/*.txt`. Do not narrow to specific documents. Work one question at a time: run its grep(s), write the relevant verbatim excerpts into that question's section, then move to the next.

**How does the company make money?**
```bash
grep -niE -A8 "reportable segment|operating segment|revenue by segment|segment revenue|disaggregation of revenue|net (sales|revenue) by|principal products|products and services|sources of revenue|we (generate|derive|earn) .*revenue|we (sell|offer|provide)|business line|product line|recurring revenue|subscription|transaction-based|license revenue" $SRC/*.md $SRC/*.txt
```

**What are its competitive advantages?**
```bash
grep -niE -A5 "competit|advantage|differentiat|patent|intellectual property|proprietary|trade secret|trademark|brand|market leader|leading provider|market share|economies of scale|barrier to entry|switching cost|network effect|moat|pricing power|dominant|scale advantage|first[- ]mover" $SRC/*.md $SRC/*.txt
```

**How and why are sales growing?**
```bash
grep -niE -B1 -A6 "(revenue|sales) (increased|decreased|grew|declined)|increased? .*due to|driven (primarily )?by|primarily due to|attributable to|growth .*driven by|partially offset|organic|acquisition|acquired|unit price|volume|pricing|price increase|market share|segment|new (product|service|offering|customer|contract)|product launch|introduc|new market|expansion into" $SRC/*.md $SRC/*.txt
```

**Is there a reasonable expectation of accelerated or continued future sales growth?**
```bash
grep -niE -A6 "market share|addressable market|total addressable|penetration|growth opportunity|invest(ing)? .*growth|demand|expand|scale|adoption|artificial intelligence|machine learning|generative|automation|long[- ]term|multi-year|new (product|service|offering)|product launch|introduc|pipeline|innovation|road ?map|new market" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A2 "annual recurring revenue|recurring revenue|\bARR\b|net (dollar )?retention|net revenue retention|\bNRR\b|\bDBNRR\b|retention rate|bookings|remaining performance obligation|\bRPO\b|backlog|deferred revenue|billings|renewal|churn|subscriber|subscription" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A4 "headwind|challenge|pressure|uncertainty|slowdown|soft(ness)?|weak(ness|er)?|macroeconomic|adverse|unfavorable|negatively|constrain|investigation|antitrust|lawsuit|litigation|probe|regulatory" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A8 "guidance|outlook|forecast|we (expect|anticipate|believe|plan|intend|estimate)|target|full[ -]year|next quarter|for (the remainder of )?fiscal|going forward|reaffirm|raise[d]? .*guidance|lower[ed]? .*guidance" $SRC/*.md $SRC/*.txt
```

**Is it highly dependent on a small number of customers?**
```bash
grep -niE -B1 -A8 "significant customer|major customer|customer concentration|no (single|one) customer|largest customer|(one|two|three) customers?|top .*customers|(accounted for|represented) .*% of .*(revenue|sales)|concentration of credit|dependence on|reliance on" $SRC/*.md $SRC/*.txt
```

**Does it have a worthwhile gross margin? If not, is there a good reason why the margin is low?**
```bash
grep -niE -B1 -A5 "margin|gross margin|gross profit|cost of (revenue|sales|goods)|margin (expansion|compression|pressure|improve|decline)" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A8 "guidance|outlook|forecast|we (expect|anticipate|believe|plan|intend|estimate)|target|full[ -]year|next quarter|for (the remainder of )?fiscal|going forward|reaffirm|raise[d]? .*guidance|lower[ed]? .*guidance" $SRC/*.md $SRC/*.txt
```

**Is it generating FCF? If not, is there a good reason why?**
```bash
grep -niE -B1 -A5 "free cash flow|cash flow|cash from operations|cash (provided|used) (by|in) operating|cash generation|cash conversion|capital allocation|return .*capital|repurchase|buyback|accelerated share repurchase|\bASR\b|dividend|debt paydown" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A8 "guidance|outlook|forecast|we (expect|anticipate|believe|plan|intend|estimate)|target|full[ -]year|next quarter|for (the remainder of )?fiscal|going forward|reaffirm|raise[d]? .*guidance|lower[ed]? .*guidance" $SRC/*.md $SRC/*.txt
```

**Are liabilities and expenses reasonable and manageable?**
```bash
grep -niE -A8 "liquidity|capital resources|debt|indebtedness|borrowings|notes payable|credit facility|revolving|term loan|senior notes|covenant|leverage ratio|interest expense|maturit|refinanc|commitments and contingencies|purchase obligation|(operating|finance) lease|contingent liabilit|off-balance" $SRC/*.md $SRC/*.txt
```

**Do accounting choices appear to be inflating or depressing reported earnings?**
```bash
grep -niE -A15 "critical accounting (estimate|polic)|significant accounting polic|use of estimates|change(s|d)? (in|to) .*(estimate|accounting|policy)|newly adopted|recently (adopted|issued) accounting|accounting standards update|\bASU\b" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A6 "revenue recognition|recognize(d)? revenue|point-in-time|ratably|ASC 606|performance obligation|deferred revenue|unearned|unbilled|days sales outstanding|allowance for (doubtful|credit)|accounts receivable|inventor|channel" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A5 "accru(e|ed|al)|reserve|provision|allowance|expense recognition|cookie.jar" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A5 "capitaliz|useful li(fe|ves)|depreciat|amortiz|impair" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A5 "one-time|one time|non-recurring|nonrecurring|unusual|infrequent|extraordinary|special (charge|item)|certain (charges|items)|discrete|write-?off|write-?down|impairment (charge|loss)|restructuring|severance|workforce reduction|reduction in force|facility (closure|exit)|exit cost" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A5 "non-gaap|adjusted (ebitda|earnings|net income|eps|operating income)|core earnings|excluding|add-?back|stock-based compensation|share-based|rebate" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A5 "circular|round.trip|vendor financing|customer financing|counterparty|reciprocal|factor(ing|ed)|securitiz|reclassif" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A8 "off-balance|unconsolidated|variable interest entit|\bVIE\b|letter of credit|(operating|finance) lease|related.party|contingent|contingencies|guarantee|pension|post.?retirement|OPEB|goodwill|auditor|independent registered public accounting|audit fee" $SRC/*.md $SRC/*.txt
```

**What is the financial community's current appraisal of the company and its growth prospects?**
```bash
grep -niE -A15 "\(Analyst" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A3 "bullish|bearish|optimistic|pessimistic|skeptic|sentiment|narrative|thesis|momentum|overhang|out of favor|priced (in|for)|undervalued|overvalued|attractive|compelling|on sale|compounder|Wall Street|the Street|analysts?|investors?|the market|concern|caution|worried|fears?|doubt|conviction" $SRC/*.md $SRC/*.txt
```

**What catalyst(s) may force the financial community's appraisal to converge with ours?**
```bash
grep -niE -A6 "look forward|upcoming|later this year|next (fiscal|generation)|launch|introduc|rollout|roll out|new product|road ?map|pipeline|on track|will begin|ramp|milestone|catalyst|coming (months|quarters)|approval|certif|partnership|go[- ]live" $SRC/*.md $SRC/*.txt
grep -niE -B1 -A8 "guidance|outlook|forecast|we (expect|anticipate|believe|plan|intend|estimate)|target|full[ -]year|next quarter|for (the remainder of )?fiscal|going forward|reaffirm|raise[d]? .*guidance|lower[ed]? .*guidance" $SRC/*.md $SRC/*.txt
```

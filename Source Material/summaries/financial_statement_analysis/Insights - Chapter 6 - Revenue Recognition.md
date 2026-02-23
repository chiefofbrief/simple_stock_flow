# Chapter 6: Revenue Recognition

## OBJECTIVE

Revenue recognition is where management's creativity most dangerously manifests. Experience teaches that accepting reported revenues at face value—even audited ones—can be perilous. Companies employ aggressive recognition practices that comply with GAAP yet distort economic reality, and sometimes cross into fraud. **The central paradox: outward signs of exceptional success often indicate higher probability of future downward revisions.** Companies with extremely rapid sales growth face intense pressure to maintain stock prices, creating powerful incentives to manipulate.

## The Success Theater Paradox

Companies characterized by rapid sales growth know that the first indication of a slowdown will crush their stock price. This creates greater manipulation incentive than for companies where investors expect moderate growth. **The analyst's challenge: the more impressive the reported success, the more skeptical you should be.**

## The Beneish M-Score: Quantitative Fraud Detection

Professor Messod Beneish developed a model that uses seven financial ratios to detect earnings manipulation. Before Gowex's collapse, his model indicated 71.3% probability of fraud—meaning the company was **103.3 times more likely to be a manipulator than the average firm.** The model is available free at https://apps.kelley.iu.edu/Beneish/MScore/mscore/MScoreInput.

### The Seven Detection Variables

**1. Days' Sales in Receivables Index** (Current ÷ Prior year DSO): Sharp increase may indicate fictitious sales not converting to cash.

**2. Gross Margin Index** (Prior ÷ Current year margin): Ratio >1x means deteriorating margins, suggesting worsening prospects that tempt manipulation.

**3. Asset Quality Index** (Current ÷ Prior year ratio of non-PP&E assets to total assets): Rising ratio hints at deferring costs rather than expensing them.

**4. Sales Growth Index** (Current ÷ Prior year sales): High growth doesn't automatically imply manipulation, but creates intense pressure to meet targets.

**5. SG&A Index** (Current ÷ Prior year SG&A/sales ratio): High level suggests poor prospects, hence strong manipulation incentive.

**6. Leverage Index** (Current ÷ Prior year debt/assets): Rising leverage creates incentive to manipulate to avoid covenant violations.

**7. Total Accruals to Total Assets** (Change in working capital less depreciation ÷ total assets): High ratio indicates discretionary accounting choices.

**Critical interpretation**: Any single variable may have innocent explanation. **Multiple red flags together suggest fire, not just smoke.** For variables 3, 4, and 7, compare company to industry peers—statistical outliers on multiple metrics warrant deep scrutiny.

## Channel-Stuffing: The Inventory Acceleration Game

**The mechanism**: Company offers distributors discounts large enough to cover carrying costs, incentivizing them to hold excess inventory. Sales inflate temporarily; when distributors work down inventory, sales collapse.

**Bristol-Myers Squibb** gave wholesalers discounts in 2001 to induce ordering far above pharmacy prescription rates. In 2002, wholesalers worked down bloated inventories instead of reordering. The company eventually restated 1999-2001 earnings, cutting profits by ~$900M. Stock fell from $70 peak to $22.

**Why management does it**: CEO had promised 12% annual earnings growth. When competition escalated and drug pipeline dried up, pressure mounted. CEO replaced medicines head known for "speaking candidly about declining sales prospects"—signal that quotas must be met at all costs.

### Detecting Channel-Stuffing: The Third-Party Data Method

Merrill Lynch analyst detected Bristol-Myers' problem days before announcement by comparing company-reported sales to IMS Health pharmacy-level data:
- **Pravachol**: IMS showed 14% retail growth (8% volume + 6% price); Bristol-Myers reported 21% = 7% gap
- **Glucophage**: IMS showed flat (8% prescription decline offset by 8% price increase); Bristol-Myers reported 18% gain
- Estimated wholesale inventories at 2.42x average weekly sales (abnormally high)

**Detection principle**: Test reported earnings against independently available industry data (pharmaceuticals, autos, casinos). Subscription data costs tens of thousands annually, but principle applies wherever third-party metrics exist.

**Simpler signal**: Watch for rising **days sales outstanding** coinciding with revenue recognition method changes. M/A-Com switched from "sell-through" (revenue when distributors sold to end users) to "sell-in" (revenue when selling to distributors) just as company needed to meet Street expectations. DSO rose from 57 to 65 days. Stock later plunged 70% over two years while tech index rose 34%.

## Detecting Fictitious Revenues

When revenues are largely fabricated, multiple red flags appear simultaneously. Analysts who spot the pattern can avoid total losses.

### Core Red Flags That Cluster Together

**Audit relationship anomalies**:
- Absurdly low audit fees relative to company size (Gowex: 0.04-0.06% of revenues vs. peer average 0.77-0.94%—implied business 1/10th reported size)
- Obscure auditor for sizable public company (Gowex's $1-2B market cap used auditor operating from apartment with Gmail address)
- Auditor firing with Section 519 statement citing scope disagreements (Globo fired BDO, which stated it couldn't get sufficient component auditor access)

**Operational inconsistencies**:
- Reported infrastructure doesn't match claimed scale (Gowex claimed 200,000 hotspots; map showed 5,530)
- Download counts wildly inconsistent with reported user base (Globo claimed 250,000+ licensees; Google Play showed 1,000-5,000 downloads vs. competitor's 500,000-1,000,000)
- Contradictory revenue statements to different audiences (Gowex told analysts NYC contract worth €7.5M, then €2M; actual was $245K)

**Peer comparison outliers** (Globo vs. industry):

| Metric | Red Flag Pattern |
|--------|------------------|
| Operating margin | Profitable (32%) while direct competitors deeply negative (-36%, -67%) |
| Days sales outstanding | 164 days vs. peers' 83-90 days (bloated receivables = classic fraud signal) |
| Accrued income | 263% of revenue vs. peers' 83-109% (revenue recognized but not yet billed) |
| Unearned income | 4% vs. peers' 43-201% (software companies typically have large prepaid balances) |
| Working capital | Required +56% funding vs. peers generating -67% to -70% from operations |

**The cash paradox**: Company reports large cash balance yet draws down credit lines. Why incur interest costs when supposedly holding ample cash? This was major red flag before Parmalat bankruptcy—applies to Globo claiming €82M cash while drawing €25M revolver.

## Round-Trip Transactions and Related Parties

**The principle**: Money flows from company to counterparty, then immediately back and gets booked as revenue. Management manufactures earnings "by taking money out of one pocket and putting it into another."

**Krispy Kreme** repurchased struggling franchises, structured transactions so money paid for store-closing costs and overdue interest flowed back as "interest income." Closed stores became intangible assets (no amortization) rather than expenses, despite creating no future economic value. Strung together 13 consecutive quarters exceeding EPS guidance by exactly $0.01 after revising executive comp to pay bonuses only if beating guidance by that amount.

**Detection signals**:
- **Exceptionally long streak of beating guidance** (businesses grow unevenly; smooth performance rarely natural)
- **Related-party transactions** (Krispy Kreme CEO held 6% of franchise being repurchased—disclosed as 3% in 10-K, blamed "proofreading error")
- **Implausible valuations**: Paid $67.5M for 5 stores + 1 commissary owned by two former directors; simultaneously declined $80M offer for 22-store franchise
- **Management excuse that doesn't withstand scrutiny** (blamed low-carb fad; Dunkin' Donuts showed no such impact)

**The special committee finding**: "The number, nature, and timing of accounting errors strongly suggest they resulted from intent to manage earnings." But all interviewed employees denied deliberately distorting earnings—**absence of confession doesn't mean absence of manipulation.**

## Percentage-of-Completion Abuse

GAAP permits recognizing revenue proportional to work completed rather than billing schedule, solving legitimate timing mismatches at construction firms, defense contractors, and capital goods manufacturers. But involves considerable subjectivity—management can accelerate revenue recognition with liberal assumptions auditors struggle to reject objectively. **Taking liberties borrows future revenues, making surprise shortfall inevitable.**

**Detection difficulty**: Hard to catch without deep industry expertise and project-level visibility. Watch for aggressive revenue ahead of billing, especially in quarters where company needs to hit targets.

## Rainy Day Reserves: Manufacturing Smooth Growth

Equity investors reward smooth earnings growth with high P/E multiples. Since steady growth rarely occurs naturally, companies create artificial smoothness by delaying revenue recognition when profits run above expectations, then pulling earnings from storage when needed.

**W.R. Grace** allegedly received $10-20M Medicare reimbursement windfall at dialysis subsidiary but didn't report it, reasoning it wouldn't help stock price since earnings already meeting forecasts. Might even hurt by creating unsustainable 30% profit spike. Placed revenue in reserve, then drew on it 1993-1995 to boost corporate earnings. By end of 1992, rainy day reserve grew to ~$55M. CFO testified: "We believed it was prudent to reduce growth rates" because unit couldn't maintain pace.

**Auditor objection**: Price Waterhouse pointed out (1991) that GAAP allows reserves only for foreseeable and quantifiable liabilities, not discretionary rainy day funds. But allowed it to stand based on immateriality from corporate-wide standpoint.

**The standard script**: Company's response to allegations followed formulaic pattern—vehement denial, claim auditors raised no objections, eventual settlement without admitting guilt. **Analysts should take protests of innocence with grain of salt**—record doesn't suggest companies that bray loudest are vindicated.

## The Systemic Problem: Budget-Gaming is Structural

Harvard Professor Michael Jensen: Misrepresenting revenues is inevitable consequence of using budget targets in compensation. "Tell a manager he'll get a bonus when targets are realized and two things happen: managers will attempt to set easy targets, and once set, will do their best to see they are met **even if it damages the company.**"

**Real examples of managers "doing their best"**:
- Shipping fruit baskets weighing same as product, booking as sales
- Announcing January 2 price increase to induce year-end orders, putting company out of line with competition
- Shipping unfinished equipment from England to Netherlands for revenue recognition, then completing assembly in warehouse at considerable cost

**Customer collusion**: SEC administrator: "All too often, companies wouldn't be able to accomplish frauds without assistance of their customers." Ikon executive Ron Davies: "It's very common for a manufacturer to call and say, 'I need to hit my quarterly number, would you mind giving me a purchase order for $100,000?'"

**W.R. Grace CFO attorney's defense**: "Any CFO anywhere has managed earnings in a way the SEC is now jumping up and down and calling fraud."

**Jensen's conclusion**: "Almost every company uses a budget system that rewards employees for lying and punishes them for telling the truth." He proposes severing link between targets and compensation—but realistically, radical reforms unlikely soon. **"Budget-gaming is rife, and in most corporate cultures, much of this is expected, even praised." Let the analyst beware.**

## Detection Protocol: Standard Operating Procedures

Regardless of company pedigree or management reputation, analysts should routinely watch for:

**Balance sheet warning patterns**:
- Rising DSO (accounts receivable relative to sales)
- Rising inventory relative to sales
- Conspicuous surges in unbilled/accrued receivables
- Unusually low unearned income for subscription/service businesses
- Working capital funding patterns diverging from industry peers

**Earnings quality patterns**:
- Consistently beating EPS consensus by exactly $0.01-$0.02 (aggressive earnings targeting)
- Exceptionally long streak of meeting/beating guidance (unnatural smoothness)
- Revenue growth substantially exceeding competitors without satisfactory explanation
- Revenue recognition policy changes coinciding with pressure periods

**Governance red flags**:
- Auditor firing/resignation, especially with scope disagreement disclosure
- Audit fees absurdly low relative to size and peers
- Obscure auditor for sizable public company
- Related-party transactions involving executives/directors
- Conflicting revenue statements to different audiences
- Management offering implausible excuses for performance changes

**Third-party validation mismatches**:
- Industry statistics inconsistent with reported growth
- Customer confirmations contradicting claimed relationships
- Download counts/physical infrastructure inconsistent with reported scale
- Peer operating metrics (margins, DSO, working capital) wildly divergent

## Investment Application: Practical Due Diligence

When evaluating any company's reported revenues:

**1. Run systematic checks**:
- Beneish M-Score (free online tool)—multiple high scores = major red flag
- DSO trend analysis vs. industry peers
- Working capital patterns vs. peers
- Audit fee reasonableness check

**2. Peer comparison discipline**:
- Operating margins (profitable while peers losing money = suspicious)
- All seven Beneish variables relative to industry averages
- Accrued/unearned income patterns (consistent with business model?)

**3. Third-party validation** (when available):
- Industry statistics (pharmaceuticals, autos, casinos, app downloads)
- Customer verification of claimed relationships
- Physical infrastructure checks

**4. Pattern recognition**:
- Beating guidance consistency (too perfect = red flag)
- Related-party transaction disclosure quality
- Management turnover (especially CFO departures)
- Quality of management explanations for surprises

**5. The accumulation principle**: Don't wait for smoking gun. When multiple yellow flags accumulate—even if each has potential innocent explanation—probability of manipulation rises dramatically. Better to miss upside than suffer devastating fraud loss.

**Above all**: Never automatically rule out manipulation just because earnings look strong during rough patch, auditors approved accounting, or prestigious individuals lead company. Professional skepticism is not optional—it's fiduciary duty.

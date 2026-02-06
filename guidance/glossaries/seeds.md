# Projection Seeds Glossary

This glossary covers the projection seeds—the fundamental inputs required to rebuild financial statements with forward estimates. For context on what these seeds are and why they were selected, see the README Projection Seeds section.

---

## INCOME STATEMENT DRIVERS

### 1. Revenue

**Projection Methodology:**

Revenue drives all percentage-of-sales projections. Use bottom-up approach for established industries: build segment-by-segment forecasts using industry data. For technology/consumer sectors, focus on company-specific product cycles rather than industry-wide forecasts.

**Forward-Looking Information:**

- **Industry Growth Rates:** Total market size and growth trajectory provide ceiling for company growth without market share gains
- **Market Share Trends:** Revenue growth substantially above industry with maintained margins indicates strengthening position; growth above industry with compressing margins suggests buying share through price cuts
- **Volume vs. Price Components:** Companies maintaining price increases through downturns demonstrate pricing power; those forced to cut prices reveal commodity-like competition
- **Customer Concentration:** Projection difficulty requiring individual customer forecasting signals dangerous concentration risk

**Key Considerations:**

Historical revenue growth patterns establish baseline growth rates. Material deviations require operational explanations: competitive position changes, new product success, market expansion, or industry structural shifts. Revenue projection difficulty itself reveals business model characteristics—thousands of small customers project more reliably than dependence on handful of large buyers.

---

### 2. Cost of Goods Sold (as % of Revenue)

**Projection Methodology:**
```
Projected COGS = Projected Sales × Historical COGS %
```

Maintain historical COGS percentage unless specific factors indicate change. Historical gross margin (Revenue - COGS / Revenue) provides baseline.

**Forward-Looking Information:**

- **Input Cost Changes:** Raw material, labor, freight, energy cost expectations directly impact COGS percentage
- **Competitive Intensity:** Ability to pass cost increases to customers or retain cost decreases; strong pricing power maintains margins during input inflation
- **Capacity Utilization:** At full capacity with all producers running flat, cost increases pass through fully and margins expand; declining utilization compresses margins as fixed costs spread over fewer units
- **Product Mix Shifts:** Portfolio composition changes toward higher or lower margin products alter COGS percentage independent of operational efficiency

**Key Considerations:**

Historical gross margin stability during different capacity utilization periods reveals competitive position. Companies maintaining margins during industry gluts have genuine advantages—superior products, service, or switching costs. Those with compressing margins during slack periods are price takers. High-fixed-cost businesses show dramatic margin leverage to volume changes; variable-cost businesses show more stable margins but less upside.

---

### 3. Selling, General & Administrative (as % of Revenue)

**Projection Methodology:**
```
Projected SG&A = Projected Sales × Historical SG&A %
```

Historical ratio continues unless management indicates strategy changes.

**Forward-Looking Information:**

- **Cost Structure:** Which expenses scale with revenue (commissions, shipping) versus remain constant (headquarters overhead, salaries) determines operating leverage
- **Efficiency Initiatives:** Cost reduction program specifics, expected savings magnitude, timing of realization versus upfront costs
- **Investment Spending:** Sales force expansion, marketing campaigns, infrastructure additions increasing SG&A percentage temporarily ahead of revenue

**Key Considerations:**

Historical SG&A leverage patterns reveal scalability. Companies showing declining SG&A percentage during growth periods demonstrate operational leverage—spreading fixed overhead efficiently. Rising SG&A percentage during growth indicates lack of scalability. Material deviations from historical patterns require explanations: efficiency programs, investment cycles, business model shifts. Note: Many cuts possible without disrupting short-run operations impair long-term competitiveness (advertising, training).

---

### 4. Research & Development (as % of Revenue)

**Projection Methodology:**
```
Projected R&D = Projected Sales × Historical R&D %
```

Typically budgeted as percentage of sales, similar to advertising.

**Forward-Looking Information:**

- **Investment Plans:** Spending levels, major projects, commercialization timing
- **Competitive Requirements:** Industry norms for R&D intensity; technology-driven industries require sustained R&D to maintain position

**Key Considerations:**

Historical R&D stability in technology businesses indicates maintaining competitive position. Declining percentage may signal maturing business with reduced innovation needs or dangerous underinvestment. Peer comparison reveals whether spending aligns with competitive requirements. Business model determines appropriate intensity: B2B industrials show higher R&D, consumer products show higher advertising.

---

### 5. Depreciation & Amortization

**Projection Methodology:**
```
Projected Depreciation = Prior Year-End PP&E × Historical Depreciation %
```

If company writes off assets over 10 years straight-line, depreciation equals 10% of PP&E annually.

**Forward-Looking Information:**

- **Capex Plans:** New asset additions generate future depreciation based on useful lives and methods
- **Policy Changes:** Changes to useful life assumptions or depreciation methods; verify consistency with historical policy

**Key Considerations:**

Historical depreciation rate (as % of PP&E) reveals asset intensity. High rates (8-10%) signal asset-heavy business requiring continuous reinvestment; low rates (2-3%) indicate asset-light model with better cash conversion. Peer comparison identifies potential manipulation—rates materially below peers may understate expenses. Historical capex/depreciation relationship shows growth trajectory: capex consistently exceeding depreciation by wide margin indicates growth requiring external funding; capex approximating depreciation signals self-funding maturity.

---

## CASH FLOW & BALANCE SHEET DRIVERS

### 6. Capital Expenditures

**Projection Methodology:**

Use management guidance as starting point. Verify reasonableness against:
- Historical capex as % of sales
- Historical capex/depreciation ratio
- Stated growth plans and capacity needs

**Forward-Looking Information:**

- **Management Plans:** Total amount, timing, maintenance versus growth split
- **Capacity Utilization:** Full capacity means sales growth requires proportional asset expansion; excess capacity allows sales growth without proportional capex
- **Competitive Requirements:** Whether spending maintains, loses, or gains ground versus competitors; technology change rates requiring ongoing modernization

**Key Considerations:**

Historical capex/depreciation relationship reveals growth trajectory and capital intensity. Ratio ≈1.0 indicates mature business self-funding maintenance. Ratio >1.5 indicates growth investment beyond replacement. Ratio <1.0 may signal asset-light transition (positive) or underinvestment (negative). Industry context critical: software grows with minimal capex; manufacturing requires proportional capex to sales. Historical patterns during different growth phases show capital requirements for incremental revenue.

---

### 7. Debt

**Projection Methodology:**

Use management guidance on debt management strategy. Project debt balance based on:
- Stated paydown schedules or target leverage ratios
- Expected new issuances for growth or refinancing
- FCF generation available for debt reduction

**Forward-Looking Information:**

- **Debt Management Plans:** Paydown schedules, refinancing timing, new issuance, target leverage ratios
- **Covenant Restrictions:** Borrowing capacity limits; headroom under covenant restrictions
- **Capital Allocation:** Priority between debt reduction, dividends, buybacks, and growth investment

**Key Considerations:**

Historical Debt/OCF trends reveal deleveraging or leveraging trajectory. Companies with strong FCF generation and stated deleveraging targets provide clearer projection visibility. Covenant-constrained companies face limited flexibility. Calculate embedded interest rate (Total Interest Expense ÷ Average Debt) for the Interest Rate assumption—see README Projection Assumptions section.

---

### 8. Working Capital Components

**Projection Methodology:**
```
Projected A/R = Projected Sales × (Historical A/R ÷ Historical Sales)
Projected Inventory = Projected Sales × (Historical Inventory ÷ Historical Sales)  
Projected A/P = Projected Sales × (Historical A/P ÷ Historical Sales)
```

Verify most recent year's ratios representative of multi-year experience.

**Forward-Looking Information:**

- **Collection Efficiency:** Days Sales Outstanding expectations, payment term changes, receivables credit quality
- **Inventory Management:** Days Inventory Outstanding, production planning efficiency, obsolescence risk
- **Payables Management:** Days Payable Outstanding, supplier terms, trade credit availability

**Key Considerations:**

Historical working capital as percentage of revenue establishes baseline requirements. Stable percentages indicate consistent operational efficiency. Material increases signal cash consumption requiring investigation: receivables rising faster than sales indicates collection deterioration or loosened credit terms; inventory rising faster than sales suggests demand weakness or planning failures. Fast-growing companies consume cash building working capital—this isn't necessarily problematic if returns exceed capital cost. Historical working capital changes validate income statement—balance sheet harder to manipulate than flow variables.
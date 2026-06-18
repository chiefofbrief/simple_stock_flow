#!/usr/bin/env python3
"""Format Peer_Compare_TSM_<date>.json into 'TSM ANALYSIS.md' (3 sections)."""
import json, os
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
base = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(base, "..", "Data", "screening",
                                f"Peer_Compare_TSM_{date}.json")))
TICKERS = ["TSM", "NVDA", "AVGO", "ASML", "KLAC", "AMKR"]
FY_END = {"TSM": "Dec", "NVDA": "Jan", "AVGO": "Nov", "ASML": "Dec",
          "KLAC": "Jun", "AMKR": "Dec"}

# key, label, kind, in_trend, has_cagr, direction(better)
ROWS = [
    ("gaap_pe",    "GAAP P/E",               "x",  True,  False, "low"),
    ("nongaap_pe", "Non-GAAP P/E",           "x",  False, False, "low"),
    ("poe",        "Price / Owner Earnings", "x",  True,  False, "low"),
    ("roic",       "ROIC",                   "%",  True,  True,  "high"),
    ("op_margin",  "Operating margin",       "%",  True,  True,  "high"),
    ("revenue",    "Revenue",                "$B", True,  True,  "high"),
    ("ocf",        "OCF",                    "$B", True,  True,  "high"),
    ("fcf",        "FCF",                    "$B", True,  True,  "high"),
    ("capex",      "Capex",                  "$B", True,  True,  "na"),
    ("capex_rev",  "Capex / Revenue",        "%",  True,  True,  "low"),
    ("fcf_ocf",    "FCF / OCF",              "%",  True,  True,  "high"),
]
THRESH = 20  # bold when peer beats TSM by >= 20% (snapshot) / 20pp (CAGR)

# Cells the Section-4 notes flag as potentially misleading. Scope letters:
# C = Current table, T = TTM table, Y = trend (3yr) block. Numbers are NOT changed;
# an asterisk is appended so the reader checks the matching Section-4 note.
FLAGS = {
    "TSM":  {"op_margin": "CTY", "roic": "CTY", "fcf": "CTY", "fcf_ocf": "CTY"},
    "NVDA": {"gaap_pe": "CT", "roic": "CTY", "revenue": "CT"},
    "AVGO": {"gaap_pe": "CT", "fcf": "CTY", "fcf_ocf": "CTY", "revenue": "CTY",
             "roic": "CTY", "op_margin": "Y"},
    "ASML": {"ocf": "C", "fcf": "C", "revenue": "CT", "roic": "CTY"},
    "KLAC": {"nongaap_pe": "CT", "ocf": "CT", "fcf": "CT", "fcf_ocf": "CT"},
    "AMKR": {"gaap_pe": "CT", "nongaap_pe": "CT", "poe": "CT", "roic": "CTY",
             "op_margin": "CTY", "fcf": "CTY", "fcf_ocf": "CTY", "capex": "CTY",
             "revenue": "CTY"},
}


def star(ticker, key, scope):
    return "*" if scope in FLAGS.get(ticker, {}).get(key, "") else ""


def fmt(v, kind):
    if v is None:
        return "NM"
    if kind == "x":  return f"{v:.1f}x"
    if kind == "%":  return f"{v*100:.1f}%"
    if kind == "$B": return f"${v/1e9:,.1f}B"
    return str(v)


def snap_cell(peer, tsm, direction):
    """value + (% gap vs TSM); bold the delta when peer beats TSM by >=THRESH%."""
    if peer is None:
        return "NM"
    base_kind = None  # set by caller via fmt; here just delta
    if tsm is None or tsm == 0 or peer < 0 or tsm < 0:
        return None  # signal: caller prints value + ' (NM)'
    pct = (peer - tsm) / abs(tsm) * 100
    beat = (direction == "high" and pct >= THRESH) or (direction == "low" and pct <= -THRESH)
    s = f"({pct:+.0f}%)"
    return f"**{s}**" if beat else s


def section_snapshot(which, title):
    L = [f"## {title}", "",
         "| Metric | " + " | ".join(TICKERS) + " |",
         "|" + "---|" * (len(TICKERS) + 1)]
    sc = "C" if which == "current" else "T"
    for key, label, kind, *_rest, direction in ROWS:
        tsm = d["TSM"][which].get(key)
        cells = [fmt(tsm, kind) + star("TSM", key, sc)]
        for t in TICKERS[1:]:
            v = d[t][which].get(key)
            delta = snap_cell(v, tsm, direction)
            s = star(t, key, sc)
            if v is None:
                cells.append("NM" + s)
            elif delta is None:
                cells.append(f"{fmt(v, kind)}{s} (NM)")
            else:
                cells.append(f"{fmt(v, kind)}{s} {delta}")
        L.append(f"| {label} | " + " | ".join(cells) + " |")
    return "\n".join(L)


def cagr3(a, key):
    """3-year CAGR using FY[0] (latest) and FY[3] (base); needs 4 yrs, both >0."""
    if len(a) < 4:
        return None
    latest, basev = a[0].get(key), a[3].get(key)
    if latest is None or basev is None or basev <= 0 or latest <= 0:
        return None
    return (latest / basev) ** (1 / 3) - 1


def section_trend():
    tsm_cagr = {k: cagr3(d["TSM"]["annual"], k) for k, *_ in ROWS}
    out = ["## Section 3 — Last 3 Fiscal Years (USD)"]
    for t in TICKERS:
        a = d[t]["annual"]
        yrs = [x["fy"] for x in a[:3]]
        L = [f"\n### {t}  (FY ends {FY_END[t]})", "",
             "| Metric | " + " | ".join(f"FY{y}" for y in yrs) + " | 3yr CAGR | Δ CAGR vs TSM |",
             "|" + "---|" * (len(yrs) + 3)]
        for key, label, kind, in_trend, has_cagr, direction in ROWS:
            if not in_trend:
                continue
            vals = [fmt(x.get(key), kind) for x in a[:3]]
            if has_cagr:
                c = cagr3(a, key)
                cstr = fmt(c, "%") if c is not None else "NM"
                if t == "TSM":
                    dstr = "—"
                else:
                    tc = tsm_cagr.get(key)
                    if c is None or tc is None:
                        dstr = "NM"
                    else:
                        pp = (c - tc) * 100
                        beat = (direction == "high" and pp >= THRESH) or \
                               (direction == "low" and pp <= -THRESH)
                        dstr = f"**{pp:+.0f}pp**" if beat else f"{pp:+.0f}pp"
            else:
                cstr, dstr = "—", "—"
            lbl = label + star(t, key, "Y")
            L.append(f"| {lbl} | " + " | ".join(vals) + f" | {cstr} | {dstr} |")
        out.append("\n".join(L))
    return "\n".join(out)


GLOSSARY = f"""## Glossary

- **Companies:** TSM (anchor) vs NVDA, AVGO, ASML, KLAC (KLA), AMKR.
- **Currency:** all figures USD. FX [ESTIMATED, FMP spot {date}]: EUR/USD 1.16128, USD/TWD 31.496. Ratios (P/E, ROIC, margins, Capex/Rev, FCF/OCF) are currency-neutral.
- **% gap:** each peer cell shows (peer - TSM) / |TSM|. **Bold** = peer beats TSM by >= {THRESH}% (snapshot) or {THRESH}pp (CAGR). "Beats" = lower for P/E, P/Owner Earnings, Capex, Capex/Revenue; higher for ROIC, Operating margin, Revenue, OCF, FCF, FCF/OCF.
- **Current:** latest reported quarter, annualized x4 (run-rate). Noisy for lumpy quarters.
- **TTM:** trailing four quarters. (Matches the trailing P/E shown on Google Finance.)
- **GAAP P/E** = market cap / net income (split- & currency-proof; does not use per-share).
- **Non-GAAP P/E** = price / adjusted diluted EPS (FMP earnings-calendar epsActual). NM for KLAC: its epsActual straddles the Jun-11 10:1 split. TSM reports no non-GAAP, so its non-GAAP = GAAP.
- **Price / Owner Earnings** = market cap / (FCF - stock-based comp).
- **ROIC** = NOPAT / (equity + debt - cash); NOPAT = net income + after-tax interest.
- **Operating margin** = operating income / revenue.
- **Revenue / OCF / FCF / Capex** = totals in USD. Capex = capital expenditure (cash-flow statement).
- **Capex / Revenue**, **FCF / OCF** = ratios. (Absolute Capex is shown but not bolded — it is a scale figure; capital intensity is scored via Capex / Revenue.)
- **3yr CAGR** = (latest FY / FY three years earlier)^(1/3) - 1; uses a 4th (base) year not displayed.
- **NM** = not meaningful (negative earnings/cash/returns, a % gap on a negative base, or a split-distorted source).
- Source: FMP (financialmodelingprep.com), {date}. P/E and P/Owner Earnings carry no CAGR (valuation multiples, not growth)."""

DATA_QUALITY = """## Section 4 — Data-Quality Notes

How to read and trust the figures above. Each item opens with a plain-English explanation, then the technical detail with citations (`{TICKER}_Thesis.md:line`).

### Cross-cutting — the "Current" column
**Plain:** The "Current" column annualizes only the most recent quarter (x4). For a few companies, a single quarter's cash flow is unusually high or low purely because money arrives in lumps, so that snapshot can look alarming when nothing is actually wrong.
**Technical:** For ASML, KLAC, and AMKR, read operating and free cash flow off the TTM column, not Current, because their quarterly cash flow swings on the timing of customer deposits, inventory purchases, and capital spending.

### TSM (anchor) — cleanest in the set

**1. Depreciation timing slightly flatters profit, ROIC, and margins.**
Plain: When TSM finishes building a new factory, it chooses when to start counting that factory's cost as a yearly expense. Pushing that start date out makes today's profit look a little bigger than it really is.
Technical: Management has discretion over when newly installed equipment ("EUI/CIP") begins depreciating, and depreciation as a share of revenue has fallen from 26.6% to 16.5% partly for this reason; the effect is bounded at roughly 2-4.5 percentage points of operating margin [`TSM_Thesis.md:432,615`]. This reverses soon: 2026 depreciation is guided up by a high-teens percentage as new 2nm equipment starts depreciating [`TSM_Thesis.md:718`].

**2. The FCF/OCF ratio (46%) makes TSM look more cash-starved than it is.**
Plain: Some of TSM's spending just keeps existing factories running, while the rest builds brand-new factories for growth. The "free cash" figure lumps both together, so it penalizes TSM for spending that is really optional growth, not survival.
Technical: Reported free cash flow of about $35B is struck after heavy growth capital expenditure; maintenance free cash flow (operating cash flow minus depreciation as a proxy for upkeep) is roughly $55B [`TSM_Thesis.md:389,456`].

**3. Almost all pay is cash, not stock.**
Plain: Many tech companies pay staff partly in shares, a real but hidden cost because it dilutes existing owners. TSM barely does this, so its reported profit is not flattered by leaving that cost out.
Technical: Stock-based compensation is approximately 0% of revenue, so GAAP and non-GAAP earnings are essentially the same [`TSM_Thesis.md:412`].

**4. No acquisitions means no amortization distortion.**
Plain: TSM does not buy other companies, so it carries none of the paper "purchase-price" charges that artificially depress other firms' reported profits.
Technical: There is no goodwill on the balance sheet [`TSM_Thesis.md:599`].

### NVDA — GAAP P/E flattered, ROIC understated

**1. GAAP P/E (31x) understates the true multiple.**
Plain: NVDA owns stakes in other companies, and when those stocks rise, the accounting counts the paper gain as "profit" even though NVDA sold nothing and received no cash. That inflates reported earnings, which makes the stock look cheaper than it really is.
Technical: GAAP net income is inflated by roughly $15.9B per quarter of unrealized gains on equity investments, so the non-GAAP figure of about 35x is the truer multiple [`NVDA_Thesis.md:383-393,705`].

**2. ROIC (82%) is understated.**
Plain: Return on invested capital measures profit earned per dollar tied up in the business. NVDA is sitting on a huge pile of investments that produce no business profit, yet that pile still counts as "money tied up," which drags the score down.
Technical: A $73.6B equity portfolio sits inside invested capital while generating no operating profit; excluding it, operational ROIC is roughly 117% [`NVDA_Thesis.md:476`].

**3. Some of the demand is partly self-funded (circular).**
Plain: NVDA gives money to small AI startups, and those startups turn around and use it to buy NVDA chips, so part of NVDA's "sales" is effectively funded by NVDA's own cash.
Technical: NVDA invested about $18.6B in a single quarter into AI companies (roughly 23% of free cash flow), and the revenue this generates cannot be separated out from the totals [`NVDA_Thesis.md:329`].

**4. Revenue is concentrated in a few giant customers.**
Plain: A small number of huge customers make up most of the sales, so if any one of them pulls back, it hurts a lot.
Technical: Three direct customers accounted for 54% of revenue, up from 36% from two customers a year earlier [`NVDA_Thesis.md:555`].

**5. Old non-GAAP figures are not comparable to new ones.**
Plain: NVDA recently changed what counts in its "adjusted" profit, so comparing this year's adjusted number to older ones is apples-to-oranges unless the old ones are restated.
Technical: Beginning Q1 FY2027, stock-based compensation is now included in non-GAAP earnings and prior periods were restated, so any pre-FY2027 non-GAAP EPS is on a different basis [`NVDA_Thesis.md:661`].

### AVGO — GAAP P/E overstated, FCF overstates owner economics

**1. GAAP P/E (64x) is inflated by amortization, which will fade.**
Plain: When AVGO bought VMware, the accounting forces it to spread that purchase price across future years as a paper expense, not real cash going out. That paper charge shrinks reported profit and makes the P/E look higher than the cash reality. The charge gets smaller every year on a fixed schedule, so reported profit will rise on its own.
Technical: Intangible amortization of about $8.2B per year is burning off on a disclosed schedule ($7.9B in FY2026 declining to about $3.2B), which adds roughly $0.98 per share per year to GAAP EPS with no business improvement and pulls the GAAP P/E (64x) toward the non-GAAP figure (48x) [`AVGO_Thesis.md:431,487,703`].

**2. The strong FCF and FCF/OCF (97%) overstate true owner economics.**
Plain: AVGO pays employees heavily in stock rather than cash. Because that is not a cash cost, "free cash flow" looks excellent, but issuing all those shares dilutes owners, so it is a real cost. Once you subtract it, AVGO is far less cheap.
Technical: Stock-based compensation runs about $7.6B per year, or 12.4% of revenue (four to five times peers like ADI at 2.7%), so owner earnings (free cash flow minus SBC) are $20.5B, putting the honest multiple near 96x rather than the headline cash yield [`AVGO_Thesis.md:419,441,689`].

**3. The three-year trend is measured off a beaten-down year.**
Plain: The VMware purchase wrecked one year's numbers, so growth rates measured from that low starting point look better than the underlying trend.
Technical: FY2024 operating margin fell to 26% and ROIC to 6.6% on acquisition charges, so CAGRs that start in FY2024 are flattered [`AVGO_Thesis.md:384,524`].

**4. Sales are dangerously funneled through one middleman.**
Plain: Almost half of AVGO's revenue flows through a single distributor, so if that one relationship hiccups, a large chunk of revenue is exposed at once.
Technical: One distributor accounted for 42% of revenue, up from 29% a year earlier, and the top five end customers are roughly 50% of revenue [`AVGO_Thesis.md:573`].

**5. Most of AVGO's "assets" are goodwill, which is an impairment risk.**
Plain: A big part of AVGO's balance sheet is "goodwill," an accounting placeholder for what it overpaid for VMware that cannot be sold to pay debt. If VMware's business slips, AVGO may have to write a chunk of that off.
Technical: Goodwill is $97.8B (about 56% of assets), of which $71.8B sits in the VMware software segment; on a tangible basis leverage is roughly 139% debt-to-tangible-assets even though headline Debt/OCF of 2.2x looks fine, and a 20% software-goodwill write-down would be a ~$14.4B hit to equity [`AVGO_Thesis.md:646,650,661`].

**6. Collection quality on receivables bears watching.**
Plain: AVGO is increasingly booking sales it has earned but has not yet billed or collected, is taking longer to get paid, and is setting aside less cushion for bad debts; it also sells some invoices to banks for fast cash, which flatters the picture.
Technical: Contract assets (unbilled revenue) doubled from $4.4B to $8.9B, days-sales-outstanding rose from about 31 to 41, and the bad-debt reserve fell from $101M to $74M (about 1.0% of a $7.1B receivable balance) even as receivables grew 62%; an active receivables-factoring program modestly inflates reported operating cash flow [`AVGO_Thesis.md:616,618,620,705`].

**7. A coming tax change is a real headwind to reported profit.**
Plain: A new global minimum tax will likely raise AVGO's tax bill, lowering reported earnings per share, though management has not put a number on it yet.
Technical: The prior tax benefit was $2.709B (about $0.56 per share), so losing half to all of it would cut GAAP EPS by roughly $0.28-$0.56, about a 5-11% headwind on ~$5.27 TTM GAAP EPS [`AVGO_Thesis.md:725`].

**8. A large rumored financing is not in the filings.**
Plain: News reports mention a big new borrowing that does not appear in any official document yet; if it turns out to be real, AVGO's debt load would jump a lot.
Technical: A reported $35B Apollo/Blackstone financing is absent from filings as of February 1, 2026; if executed it would lift gross debt from about $65B toward $100B and raise Debt/OCF from 2.2x to roughly 5.6x [`AVGO_Thesis.md:721`].

### ASML — quarterly cash flow is timing noise

**1. The negative "Current" OCF/FCF is a timing artifact, not a problem.**
Plain: ASML's customers put down large deposits before machines ship. Depending on which quarter those deposits land in, a single quarter's cash flow can lurch, even go negative, while the full year is strongly positive.
Technical: Operating cash flow was -$2.2B in Q1 2026 versus +$11B in Q4 2025, so only the TTM or annual figure is meaningful [`ASML_Thesis.md:302,370`].

**2. Revenue is getting lumpier because units are fewer but far pricier.**
Plain: ASML now sells fewer machines, but each one costs much more, so a single delayed delivery can swing an entire quarter's results.
Technical: Unit shipments fell from 449 in 2023 to 327 in 2025 while average selling price rose roughly 48%, concentrating revenue in a small number of very high-value systems [`ASML_Thesis.md:284`].

**3. Future revenue is unusually locked in (a strength).**
Plain: Customers have already paid in advance for a large share of next year's sales, so ASML's future revenue is more certain than most companies'.
Technical: Contract liabilities (customer prepayments) were EUR 19.4B at year-end, about 59% of annual revenue, and remaining performance obligations stood at EUR 46.5B [`ASML_Thesis.md:286,288`].

**4. The ROIC drop is capital being deployed, not the business weakening.**
Plain: ASML's return-on-capital fell mainly because it parked money in a new investment and new buildings that have not started paying off yet, not because the core business got worse.
Technical: ROIC declined from 102% (FY2025) to 64% TTM, driven by the EUR 1.3B Mistral AI equity stake and a growing property base, not margin erosion [`ASML_Thesis.md:354`].

**5. Strong China sales are hiding weak demand elsewhere.**
Plain: ASML's sales of older-generation machines outside China are actually soft, but unexpectedly strong China sales are covering that up. If export rules cut off China, the underlying weakness would show.
Technical: The annual report disclosed that non-China DUV demand was "marginally lower than anticipated," offset by stronger-than-expected China DUV, so tightening export restrictions would expose the pre-existing softness [`ASML_Thesis.md:290`].

### KLAC — cash understated this quarter; split glitch

**1. TTM operating and free cash flow are temporarily understated.**
Plain: KLAC deliberately stockpiled inventory to prepare for a big upcoming sales ramp. Paying for that inventory used cash now, so its cash flow looks weak this period, but that is a deliberate choice, not a problem.
Technical: Q4 operating cash flow fell to $0.71B (OCF/net income of 0.59x) as working capital rose $986M and purchase commitments grew from $2.42B to $4.83B; normalized for the build, OCF/net income is about 1.10x [`KLAC_Thesis.md:262,440`].

**2. The non-GAAP P/E shows "NM" because of a recent stock split.**
Plain: KLAC split its stock 10-for-1 a few days ago. The data feed has the new, smaller share price but the old, larger per-share earnings, so the automatic non-GAAP P/E came out about ten times too cheap, which is garbage. We use the reliable, market-cap-based version instead.
Technical: The 10-for-1 split on June 11 broke the per-share earnings feed; the GAAP P/E (computed from market cap and net income) is unaffected, and KLAC's normal non-GAAP adjustments are only about 3% [`KLAC_Thesis.md:472`].

**3. The order backlog shrank, but it is normalization, not lost demand.**
Plain: "Backlog" is the pile of orders customers have placed but KLAC has not shipped yet, a preview of future sales. During the chip shortage, customers had to order far in advance because wait times were long, which made the backlog balloon. Now that wait times are back to normal, customers order closer to when they actually need the tools, so the backlog shrank on its own. Nobody cancelled. The catch is that a smaller backlog is a thinner cushion, so if demand did soften, it would show up in sales sooner.
Technical: Backlog fell about 20%, from $9.83B (June 2024) to $7.86B (June 2025), and forward coverage compressed from roughly 3.9x to 2.5x quarterly revenue; management attributes this to supply-chain normalization and reverting lead times rather than cancellations, with 71-76% expected to convert to revenue within 12 months [`KLAC_Thesis.md:222`].

**4. Returns are exceptional and clean through a full cycle (a reassurance).**
Plain: Even in its worst recent year, KLAC earned very high returns on the money invested in the business, which is strong evidence of a durable competitive advantage.
Technical: ROIC averaged about 46% over five years and stayed at 36.9% even in the FY2024 downturn, with no accounting distortions in the core process-control segment [`KLAC_Thesis.md:404`].

### AMKR — the most caveated; numbers flatter a weak base

**1. Profit is partly flattered by an accounting change.**
Plain: AMKR decided its test machines now last 7 years instead of 5, which lets it charge less wear-and-tear each year and makes annual profit look bigger without anything actually improving.
Technical: The 2024 useful-life extension cut depreciation and added about $0.20 to 2024 EPS (roughly 14% of it), so underlying 2024 EPS was nearer $1.27 than the reported $1.47, and the effect continues [`AMKR_Thesis.md:441,496`].

**2. Free cash flow is turning deeply negative.**
Plain: AMKR is about to spend roughly three times its normal amount building a plant in Arizona, far more than the cash the business generates, so it will burn cash and need to borrow. A "price-to-free-cash-flow" multiple is meaningless when free cash flow is negative.
Technical: 2026 capital expenditure is guided to $2.5-3.0B against operating cash flow of about $1.1B, implying free cash flow of roughly -$1.4B to -$1.9B and a need for further external financing [`AMKR_Thesis.md:378,446`].

**3. The "cash quality" ratio is misleading.**
Plain: A high cash-versus-profit ratio usually signals healthy earnings, but AMKR's is high only because it books huge machinery wear-and-tear charges. Once you account for the cash it must spend to replace those machines, it is actually consuming cash.
Technical: OCF/net income of 2.79x is an artifact of heavy depreciation on an $11.3B asset base, and true owner cash (free cash flow versus net income) is only about 0.39x [`AMKR_Thesis.md:388,392`].

**4. Profit margins are permanently lower, with more pressure coming.**
Plain: AMKR's profit margin dropped for good, from about 12% to about 7%, because its work shifted toward lower-value, material-heavy packaging, and the new Arizona plant will squeeze margins again.
Technical: Operating margin compressed from roughly 12% to 7% on mix shift, and management guided a further 1-2 percentage-point gross-margin headwind from the Arizona ramp in 2027 [`AMKR_Thesis.md:354,358`].

**5. Returns barely clear the bar, and will fall further.**
Plain: AMKR earns only a little more than its cost of money, and the Arizona spending will push that return lower for a while.
Technical: ROIC is 10.1% TTM, just above the level that signals value destruction, and adding billions of Arizona capital before revenue arrives is expected to compress it further [`AMKR_Thesis.md:472,474`].

**6. One customer is a very large share of sales.**
Plain: Nearly a third of AMKR's revenue comes from a single customer, almost certainly Apple, so that one relationship drives the business.
Technical: One customer was 29.8% of 2025 revenue and the top two were 40.9% combined [`AMKR_Thesis.md:489`].

**7. The Arizona buildout is not backed by signed orders.**
Plain: AMKR is building the Arizona plant before it has firm customer commitments for it, which makes it a bet rather than a sure thing.
Technical: The 10-K states capital expenditure is "generally made in advance of expected revenues and without firm customer commitments," which contradicts the narrative that Arizona is de-risked by Apple and Nvidia [`AMKR_Thesis.md:590`].

**8. Selling invoices to banks flatters the receivables picture.**
Plain: AMKR sells some of its unpaid customer invoices to banks for quick cash, which makes its receivables and cash timing look better than they really are.
Technical: Non-recourse factoring removes receivables from the balance sheet, so reported AR understates the true economic receivables outstanding and pulls forward operating cash flow [`AMKR_Thesis.md:502`].

**9. A one-off tax break flattered the latest quarter.**
Plain: AMKR paid an unusually low tax rate last quarter, which boosted its earnings in a way that will not repeat.
Technical: The Q1 2026 effective tax rate was 12.8% versus a 20% full-year target, so at a normal rate Q1 EPS would have been roughly $0.27-$0.29 rather than the reported $0.33 [`AMKR_Thesis.md:578`]."""

doc = (f"# TSM ANALYSIS\n\n*Financials only. Generated {date}. All figures USD.*\n\n"
       + "> Read **Section 4 — Data-Quality Notes** before drawing conclusions. An asterisk (\\*) marks a figure the notes flag as potentially misleading.\n\n"
       + section_snapshot("current", "Section 1 — Current (latest quarter, annualized x4)") + "\n\n"
       + section_snapshot("ttm", "Section 2 — TTM (trailing four quarters)") + "\n\n"
       + section_trend() + "\n\n"
       + DATA_QUALITY + "\n\n"
       + GLOSSARY + "\n")

with open(os.path.join(base, "..", "TSM ANALYSIS.md"), "w") as f:
    f.write(doc)
print(doc)

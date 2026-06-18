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

DETERMINATION = """## Part 1 — Financial Determination (financials only)

**Question:** On the financials alone, is TSM priced below what its quality and growth warrant? Peers are benchmarks only. Figures below are note-adjusted (Section 4); raw values are in the tables, flagged with an asterisk.

**Honest figures used:** TSM's ~36x P/E is clean (GAAP = non-GAAP), and its FCF/owner-earnings are if anything conservative because reported FCF understates owner earnings (maintenance FCF ~$55B vs reported ~$35B). NVDA's flattered 31x GAAP is read at its truer ~35x, ROIC ~117%. AVGO's amortization-inflated 64x GAAP is read toward ~48x, with a true owner-earnings multiple ~96x after stock comp. KLAC's split-broken non-GAAP is replaced by GAAP ~67x. AMKR's 49x is flattered (useful-life + tax), real worse. ASML cash is read off TTM.

**Where TSM ranks:**
- **Valuation — 2nd-cheapest.** Honest P/E: NVDA ~35x ≈ TSM ~36x < AVGO ~48x < ASML ~62-67x ≈ KLAC ~67x. P/Owner-Earnings (TTM): NVDA 44x < TSM 64x < ASML 73x < AVGO 78x < KLAC 84x < AMKR 128x. Correcting TSM's understated FCF to maintenance owner earnings pulls its multiple toward ~41x, roughly level with or below NVDA.
- **Quality — top-tier.** Operating margin 53% is #2 (only NVDA higher); ROIC ~49% is #3, tied with KLAC, behind only NVDA and a temporarily-depressed ASML. The one weak spot is FCF/OCF conversion at 46%, second-worst in the set.
- **Growth — #2, not slow.** 3-yr revenue CAGR 19.3% and OCF CAGR 14.0% trail only NVDA and beat ASML, KLAC, AMKR (and AVGO once its VMware-distorted base is set aside). TSM's ROIC trend is rising while most peers' are flat-to-negative.
- **Earnings honesty — cleanest.** TSM needed essentially no downward adjustment; every higher-multiple peer did.

**Financial reason a lower multiple is deserved (capital intensity):** TSM spends 31% of revenue on capex (vs 1-6% for the asset-light peers) and converts only 46% of operating cash into free cash (vs 80-97%). A dollar of TSM earnings becomes far less distributable cash. This correctly explains why TSM screens cheaper on P/E than on P/Owner-Earnings — moving from earnings to owner-cash re-rates TSM from 2nd-cheapest (36x) toward mid-pack (64x). That re-rating is the market pricing the capex penalty properly, not a mispricing.

**Determination — mixed, leaning toward an unexplained residual cheapness:** The capex penalty fully accounts for why TSM is not the cheapest on a pure earnings multiple, and that part is earned. But it does not close the gap. Even on the capex-neutral measure (P/Owner-Earnings 64x, and ~41x once TSM's FCF understatement is corrected), TSM still trades below ASML (73x), AVGO (78x), KLAC (84x), and AMKR (128x) — every one of which has lower ROIC, lower margins, and slower growth than TSM, on less clean earnings. After accounting for the only financial knock against it, TSM is still priced under demonstrably lower-quality, slower-growing peers. On the financials alone, that residual gap is unexplained, which is the financial signature of possible undervaluation.

**Scope:** Financials only. Whatever explains the residual is for later parts, not here."""


NARRATIVE = """## Part 2 — Narrative

### Analyst Grades

*Manually pulled 2026-06-18. The FMP analyst feed was unreliable (thin coverage for TSM/ASML/AMKR; split-distorted price targets for KLAC), so this hand-collected rating distribution replaces it. "% Bullish" = (Buy + Overweight) / Total; the trend column shows % Bullish three months ago to now.*

| Company | Buy | OW | Hold | UW | Sell | Total | % Bullish (Buy+OW) | % Bullish 3mo->now |
|---|---|---|---|---|---|---|---|---|
| TSM | 38 | 8 | 1 | 0 | 0 | 47 | 98% | 98% -> 98% |
| NVDA | 57 | 7 | 3 | 0 | 1 | 68 | 94% | 93% -> 94% |
| AVGO | 41 | 10 | 4 | 0 | 0 | 55 | 93% | 96% -> 93% |
| ASML | 28 | 6 | 5 | 3 | 0 | 42 | 81% | 81% -> 81% |
| KLAC | 15 | 4 | 11 | 1 | 1 | 32 | 59% | n/a -> 59% |
| AMKR | 5 | 0 | 7 | 2 | 0 | 14 | 36% | n/a -> 36% |

*Data notes: KLAC and AMKR had no rating distribution three months ago (source coverage begins ~1 month ago). AMKR's source "consensus" label reads Overweight, but its mix (5 Buy / 7 Hold / 2 Underweight) is more cautious than that implies.*"""


EARNINGS_QA = """### Earnings-Call Q&A (latest call)

*Every analyst question from each company's most recent earnings call, compressed to one row, with management's response and a tone tag (confident / measured / hedged / declined). Latest call per company: TSM Q1 2026 (Apr 16), NVDA Q1 FY2027 (May 20), AVGO Q2 FY2026 (Jun 3), KLAC Q3 FY2026 (Apr 29), AMKR Q1 2026 (Apr 29). ASML is excluded — its earnings-call Q&A was not captured in any available source (transcripts are prepared-remarks only).*

#### TSM (Q1 2026)

| # | Analyst (firm) | Question — thrust | Management response — substance + tone |
|---|---|---|---|
| 1 | Haas Liu (BofA) | What sustains multi-year 3nm demand, and where does 3nm margin go after full depreciation? | HPC/AI is the driver; N3 crosses corporate GM in H2'26, post-depreciation "generally very high" — no number. **Declined/confident** |
| 2 | Haas Liu (BofA) | What gives confidence to take CapEx to the high end ($56B)? | Demand "very robust" (HPC/AI), pulling equipment in, supply still tight. **Confident** |
| 3 | Gokul Hariharan (JPM) | How long does the shortage last; build clean-room space first? | 2–3 yrs to build a fab; '27 stays "very tight"; building 3 new N3 fabs. **Confident** |
| 4 | Gokul Hariharan (JPM) | View on Tesla Terafab / Samsung; can you win it back? | Intel & Tesla are customers and competitors; Intel "formidable," but "no shortcuts." **Confident** |
| 5 | Charlie Chan (MS) | Threat from larger-reticle/EMIB; open your die to Intel for packaging? | Already supplies largest-reticle CoWoS; building bigger packaging (CoPoS pilot, ~2yrs); "don't leave business on the table." **Confident** |
| 6 | Charlie Chan (MS) | Give a 3-year dollar CapEx guide (like 2021); is EUV a constraint? | No number, but next 3 yrs "significantly higher" than the prior $101B. **Confident/declined number** |
| 7 | Sunny Lin (UBS) | Revenue growth vs CapEx growth / capital intensity ahead? | Revenue keeps outpacing CapEx; "no sudden surge in capital intensity." **Confident** |
| 8 | Sunny Lin (UBS) | Spend extra CapEx so customers don't diversify? | Capacity set by customer demand, "not because of our competitor." **Measured** |
| 9 | Sunny Lin (UBS) | Upside above +30% 2026; memory-price hit to phone/PC? | Slight softening in price-sensitive PC/phone (high-end fine); precise number in July. **Measured/deferred** |
| 10 | Jim Fontanelli (Arete) | Has your long-term margin/return view changed as peers print super-normal returns? | Holds 56%+ GM, high-20s ROE "through the cycle"; "ongoing process." **Measured/holds line** |
| 11 | Jim Fontanelli (Arete) | Arizona's strategic role; will US fab economics match Taiwan? | Bought 2nd land to build more fabs for multiyear US demand; "much more confidence" on cost. **Confident** |
| 12 | Bruce Lu (Goldman) | Does current profitability fully reflect TSMC's value? | Deflects to "customers are partners," won't price dramatically. **Measured/non-denial** |
| 13 | Bruce Lu (Goldman) | Change to the mid-to-high-50s AI-accelerator CAGR given token growth? | Nudges up to "toward higher 50s." **Confident** |
| 14 | Laura Chen (Citi) | Advanced-packaging strategy and model with OSAT partners? | Priority is customers; own packaging "very tight," working with OSATs to add capacity. **Measured** |
| 15 | Laura Chen (Citi) | Can SoIC/CoPoS solve warpage at large die sizes? | Yes those are the challenges; deep experience, "the harder the better." **Confident** |
| 16 | Laura Chen (Citi) | Introduce SoIC earlier given your learning curve? | "We work with customers to meet demand" — no speed-up/slow-down. **Measured/deflect** |
| 17 | Charles Shi (Needham) | Include data-center CPUs in AI revenue; restate history? | Can't separate conventional vs AI server CPU; still excludes CPUs; "someday later might consider." **Declined** |
| 18 | Charles Shi (Needham) | Nvidia's LPU at Samsung = Samsung's first AI inroad; win it back? | Working with the customer on next-gen LPU; confident in position. **Confident** |

#### NVDA (Q1 FY2027)

| # | Analyst (firm) | Question — thrust | Management response — substance + tone |
|---|---|---|---|
| 1 | Joseph Moore (Morgan Stanley) | Why the new segmentation, and the surprising CPU number? | Explains AI/computing diversity; 3 segments (hyperscale / AI-natives+enterprise+sovereign / robotic edge). **Confident/expansive** |
| 2 | Ben Reitzes (Melius) | Keep growing faster than hyperscaler CapEx; still $3–4T by 2030? | Yes — two engines (hyperscalers + huge fragmented 2nd category); endorses it. **Confident** |
| 3 | C.J. Muse (Cantor) | Vera Rubin + co-design impact on inference share into '26/'27? | Gaining inference share fast; Vera Rubin "more successful than Grace Blackwell." **Confident** |
| 4 | Tim Arcuri (UBS) | Traction for merchant CPX/LPX? | LPX is niche (low-latency, high token-rate, limited context); GB/Vera Rubin cover the full lifecycle. **Measured** |
| 5 | Vivek Arya (BofA) | Agentic CPUs incremental or cannibalistic; is $20B standalone Vera? | $20B is standalone CPU; agents need CPUs; Vera is the "agentic CPU"; supply-constrained. **Confident** |
| 6 | Stacy Rasgon (Bernstein) | Where do neoclouds sit; does ACIE grow faster than hyperscale? | AI-native clouds = 2nd category; both grow fast, 2nd faster over time. **Confident** |
| 7 | Jim Schneider (Goldman) | Is Vera the biggest upside above the $1T Rubin/Blackwell visibility? | Upside = growing frontier share, standalone Vera (2nd-largest), LPX (niche). **Confident** |
| 8 | Joshua Buchalter (TD Cowen) | Will Vera Rubin ramp as fast as the record GB300 ramp? | Starts Q3, ramps Q4; POs and nearly all customers ready; "early to say" exact slope. **Measured** |

#### AVGO (Q2 FY2026)

| # | Analyst (firm) | Question — thrust | Management response — substance + tone |
|---|---|---|---|
| 1 | Harlan Sur (JPM) | Square the AI math ($56B H2); is the 18-month backlog now $200B+? | Math ties (2× $19B H1); 2027 "easily" >$100B, "if anything stronger." **Confident** |
| 2 | Blayne Curtis (Jefferies) | Google LTA — share risk, fixed vs variable, upside? | "Very strong," "substantial dollar" commitment; expects "some diversity of sources" at Google. **Confident/mild hedge** |
| 3 | Ross Seymore (Deutsche) | Why is gross margin falling harder; continue next year? | Semis mix dilutes consolidated GM (TPUs/ASICs lower, networking rich); operating leverage holds op margins. **Measured/dilution acknowledged** |
| 4 | Ross Seymore (Deutsche) | Rack vs chip dynamics? | "No racks. It is all chip business only." **Blunt/confident** |
| 5 | Ben Reitzes (Melius) | Is TAM-per-gigawatt rising (per Jensen); an accelerant? | $/GW "relatively stable" (more power, fewer chips, higher ASP); gigawatts accelerating; 2028 substantial growth. **Confident** |
| 6 | Tim Arcuri (UBS) | Secure incremental wafers/HBM; add other foundries? | "Comfortable" — supply secured for '26/'27, working '28/'29. **Confident** |
| 7 | Stacy Rasgon (Bernstein) | Any change to the ~10GW 2027 shipment target? | ~10GW "intact," back-half loaded; more in 2028. **Confident** |
| 8 | Jim Schneider (Goldman) | Will networking (40% of AI rev) fall as XPUs ramp; optical/CPO timing? | 40% is "high end," trends toward ~30%; optical/CPO increasingly meaningful. **Measured** |
| 9 | Tom O'Malley (Barclays) | Is the Anthropic deal a chip "backstop"; more such deals? | Corrects framing — TPUs provide compute (not backstop); building a funded-compute XPU vehicle. **Corrective/measured** |
| 10 | C.J. Muse (Cantor) | Any niche XPU-attached programs of interest? | "No" — straightforward model (XPUs + components) plus the funded-compute vehicle. **Measured** |
| 11 | Atif Malik (Citi) | Is AI hurting Infrastructure Software growth/renewals? | No — higher-core servers accelerate VMware; expects tailwinds. **Confident** |
| 12 | Edward Snyder (Charter) | A second wave of enterprise AI demand coming? | Enterprise AI early; mostly consumed via frontier-model platforms → demand returns to AVGO compute. **Measured** |
| 13 | Joe Moore (Morgan Stanley) | Why $30B AI bookings vs much smaller shipments? | Customers order far ahead for lead times; visibility now into 2028. **Confident** |
| 14 | Joshua Buchalter (TD Cowen) | How does revenue-per-gigawatt evolve? | Content/GW rises over generations (more HBM, CPU cores, multi-die). **Confident** |

#### KLAC (Q3 FY2026)

| # | Analyst (firm) | Question — thrust | Management response — substance + tone |
|---|---|---|---|
| 1 | C.J. Muse (Cantor) | Where is the extended lead-time / '27 visibility coming from? | Broad-based, backlogs building, urgency to secure slots; '27 a "massive buildup." **Confident** |
| 2 | C.J. Muse (Cantor) | Does high-teens H2 imply ~$15B for cal-2026? | Yes, ~15-ish (15–20% H2 sequential). **Confident** |
| 3 | Stacy Rasgon (Bernstein) | Why isn't the 2030 model higher given current strength? | Semi-revenue piece rising on memory-pricing elasticity; would push up if redone today. **Confident** |
| 4 | Stacy Rasgon (Bernstein) | Impact of the new China/Huahong ban letter? | Immaterial to guidance (affiliated-fab focus); China grows slower than WFE. **Measured** |
| 5 | Harlan Sur (JPM) | WFE upside — greenfield vs migrations vs yield; which segments drive '27? | Urgency across segments; '27 greenfield logic+memory+flash+packaging — broad-based. **Confident** |
| 6 | Harlan Sur (JPM) | Services growth vs the 13–15% target? | In range, trending to the higher end as shipments flow into service. **Confident** |
| 7 | Krish Sankar (TD Cowen) | How much visibility is true demand vs customers reserving capacity? | Real — customers are opening these fabs, large committed investments. **Confident** |
| 8 | Krish Sankar (TD Cowen) | Does CPU demand on Intel 3/7 prior nodes benefit KLA? | Yes — broadening leading-edge + yield focus plays to KLA. **Confident** |
| 9 | Joe Quatrochi (Wells Fargo) | Yield drive = process-control sales or service? | Drives process-control sales (esp. die-size changes); Intel publicly adding metrology. **Confident** |
| 10 | Joe Quatrochi (Wells Fargo) | KLA's own supply-chain capacity to support the ramp into '27? | H1'26 was supply-constrained (ramp slope "surprised us"); better for '27; hiring. **Measured/acknowledges constraint** |
| 11 | Tim Arcuri (UBS) | You guide high-teens vs consensus mid-20s WFE — is WFE too high? | Baseline ~$120B→$140B+ (high-teens); KLA systems business grows >20%. **Measured** |
| 12 | Tim Arcuri (UBS) | High-NA pushout — net puts/takes for KLA? | No change to the model; a "push"; intensity driven by more than litho (2nm > 3nm). **Measured** |
| 13 | Jim Schneider (Goldman) | Advanced-packaging revenue growth this year? | >$1B (from $635M in '25) — one of the fastest-growing markets. **Confident** |
| 14 | Jim Schneider (Goldman) | When does process-control intensity materially outgrow WFE? | +160bps share/5yr (6.5% above market); targeting +150bps more (~4.5% above ~12% WFE). **Confident** |
| 15 | Charles Shi (Needham) | X-ray vs optical metrology — who wins? | Highest-capability tool, then cost-of-ownership; x-ray slow (cost/throughput), ~$75–100M market, KLA ~60%. **Measured/technical** |
| 16 | Charles Shi (Needham) | What drove the advanced-packaging upward revision in 60–90 days? | Was >30% growth, now upper-50s%; packaging short lead-time, momentum picked up. **Confident/notable revision** |
| 17 | Srini Pajjuri (RBC) | WFE $140B+ but guide still high-teens — reconcile? | Small upward adjustment; slightly stronger '26 view. **Measured** |
| 18 | Srini Pajjuri (RBC) | '27 by end-market (memory vs logic); China base case? | More memory-weighted next year (greenfield DRAM/flash); China grows slower than WFE. **Measured** |
| 19 | Shane Brett (Morgan Stanley) | Use slot scarcity to raise margin / pass DRAM cost faster? | "We don't price on scarcity" — value-based pricing; memory headwind normalizes eventually. **Measured/disciplined** |
| 20 | Shane Brett (Morgan Stanley) | Advanced packaging $13–14B vs the $12B guide? | KLA process-control high-50s% growth; overall packaging market ~$13B (~30%). **Confident** |
| 21 | Edward Yang (Oppenheimer) | DRAM chips procured through '26 or longer? | "Longer" — comfortable through next year. **Confident** |
| 22 | Edward Yang (Oppenheimer) | Bridge WFE to hyperscaler CapEx — some came in light? | Demand "way underserving"; can't draw a straight line; "massive shortage through 2030." **Very confident/rebuts CapEx fear** |
| 23 | Chris Caso (Wolfe) | Does demand>supply cap what KLA can ship in '26 (clean-room limits)? | Yes — ecosystem-constrained; can't jump $140B→$200B in '26; fabs must be built now. **Confident** |
| 24 | Chris Caso (Wolfe) | Gross-margin 62% puts/takes? | Memory headwind worse (~100bps), DDR4/DDR5, tariffs; 62% ±50bps still appropriate. **Measured/margin headwind** |

#### AMKR (Q1 2026)

| # | Analyst (firm) | Question — thrust | Management response — substance + tone |
|---|---|---|---|
| 1 | Jim Schneider (Goldman) | H2 gross-margin puts/takes from the Q2 baseline? | Pricing covers most cost increases; GM to mid-high teens H2 on utilization/mix/pricing. **Measured/confident** |
| 2 | Jim Schneider (Goldman) | Does the compute ramp inflect in Q3 or Q4? | CPE ramp starts this quarter, meaningful in Q3, continues into '27. **Confident** |
| 3 | Ben Reitzes (Melius) | Timing of the 1–2pt Arizona margin hit in '27 + offsetting revenue? | Early to be precise; ~1–2% full-year op-margin hit; meaningful Arizona revenue end-'29, full impact 2030. **Hedged on timing** |
| 4 | Ben Reitzes (Melius) | CPU ramp — one win or a category (ARM/x86)? | One device ramps first; >5 customers engaged on HDFO; broadening. **Measured** |
| 5 | Randy Abrams (UBS) | Utilization/headroom in Korea/Vietnam ahead of Arizona? | Q1 utilization "low 70s" (vs 50s yr-ago); building Korea facility; Vietnam headroom. **Confident** |
| 6 | Randy Abrams (UBS) | Arizona scale + Intel EMIB + CoWoS-L? | Arizona ~$1B run-rate (>10% of '25 rev); EMIB collaboration continuing; CoWoS-L a 2027 story. **Measured** |
| 7 | Peter Peng (JPM) | AI advanced packaging — demand-driven or supply-constrained? | Still on track to triple, could exceed; silicon/memory supply + ramp timing are the swing factors. **Confident** |
| 8 | Peter Peng (JPM) | Is low-single-digit assumed for the rest of the business; comms H2? | Comms stronger (low-double-digit possible); cautious on the usual H2 boost. **Measured** |
| 9 | Craig Ellis (B. Riley) | Comms better; why are notebooks/PCs soft? | A customer is rebalancing its supply chain (prioritizing non-PC); not signaling strong PC. **Measured** |
| 10 | Craig Ellis (B. Riley) | CapEx linearity for the $2.75B? | ~30% H1 / 70% H2. **Confident** |
| 11 | Denis Pyatchanin (Needham) | Rank-order end-market growth; memory-price impact on demand? | Compute +20%, auto/industrial strong on advanced, comms ~double-digit; ~$50–100M material pushout. **Measured** |
| 12 | Denis Pyatchanin (Needham) | Arizona margin into '28 + financing mix for the $7B? | Arizona "meaningfully higher" margin; CHIPS $400M + 35% ITC ≈ $2.8B; ample '26 liquidity. **Measured/confident** |
| 13 | Joe Moore (Morgan Stanley) | Export-control variables to watch? | Two: Middle-East/oil commodity pressure + US-China AI export rules; "normalized," no big impact today. **Measured** |"""


NEWS = """### News (last ~90 days, through 2026-06-18)

*Organic themes from each company's news file (Perigon + FMP). Headlines are verbatim, cited [source, date]. "Lean" (Bull / Concern / Neutral) is tagged to triangulate with the Analyst Grades and the Q&A. All six included (ASML has news; only its call Q&A was missing).*

#### TSM

| Theme | Lean | Verbatim headline(s) [source, date] |
|---|---|---|
| AI/HPC demand, record results & capacity buildout | Bull | "TSMC reports May revenue up 30% on AI" [Perigon, 2026-06-14]; "TSMC Reports Record Profit, Beats Q1 Estimates" [Perigon, 2026-04-19]; "TSMC approves $20B Arizona expansion" [Perigon, 2026-05-17] |
| Customers seeking Samsung as backup (concentration/competition) | Concern | "Google, Tesla, BYD seek Samsung amid TSMC crunch" [Perigon, 2026-06-18]; "Samsung draws advanced chipmaking interest as TSMC capacity tightens" [FMP, 2026-06-18]; "AMD reported advanced talks with Samsung for 2nm" [Perigon, 2026-05-07] |
| Advanced-packaging race (CoPoS / panel-level; Amkor pact) | Bull | "TSMC reported panel-level packaging push against Samsung" [Perigon, 2026-06-18]; "Amkor shares jump on 10-year TSMC partnership" [Perigon, 2026-06-18] |
| Valuation debate (cheap vs bubble) | Neutral | "Taiwan Semiconductor: Not Expensive When You Run The Numbers On AI Demand" [FMP, 2026-06-18]; "TSM at $426: Bubble Territory or a Buy for the Next AI Supercycle?" [FMP, 2026-06-17] |
| Taiwan/geopolitical constraints (talent, water, US-China) | Concern | "TSMC CEO warns Taiwan talent, water shortages" [Perigon, 2026-06-14]; "Did the US-China Summit Make TSMC More Vulnerable?" [FMP, 2026-05-19] |

#### NVDA

| Theme | Lean | Verbatim headline(s) [source, date] |
|---|---|---|
| Demand momentum / "buy the dip" | Bull | "NVIDIA CEO Jensen Huang on AI Stock Dips: "Everybody Should Be Very Excited to Buy Stock at a Cheaper Price"…" [FMP, 2026-06-18]; "Nvidia Stock Gains as the Chip Maker Looks to Growth Outside the U.S." [FMP, 2026-06-18] |
| Debt-funded AI expansion | Neutral | "Nvidia to Sell $20 Billion in Bonds" [Perigon, 2026-06-18]; "Nvidia Sells $25B Bonds to Fund AI Expansion" [Perigon, 2026-06-18] |
| Competition (AMD/Intel, custom ASICs, AWS/Qualcomm) | Concern | "11 Words From Nvidia CFO Colette Kress That Should Have AMD and Intel Investors Worried" [FMP, 2026-06-18]; "AWS, Qualcomm plan AI200 accelerators to cut inference costs" [Perigon, 2026-06-18] |
| Valuation / "mispriced" upside | Bull | "Why Nvidia's stock is mispriced, and Wall Street is underestimating its earnings power." [FMP, 2026-05-19]; "Will Nvidia Be Worth $6 Trillion a Year From Now? Wall Street Has a Clear Answer." [FMP, 2026-04-19] |
| Physical AI / ecosystem expansion | Bull | "Nvidia says "Physical AI is here". Is Your Blue Collar Job in Danger?" [FMP, 2026-05-19] |

#### AVGO

| Theme | Lean | Verbatim headline(s) [source, date] |
|---|---|---|
| AI-guidance disappointment / post-earnings slide | Concern | "Broadcom shares plunge after AI guidance" [Perigon, 2026-06-13]; "Broadcom shares slide after earnings AI outlook" [Perigon, 2026-06-14] |
| VMware backlash / customer exits | Concern | "Tesco plans 40,000-workload VMware exit, sues Broadcom" [Perigon, 2026-06-18] |
| Custom-ASIC / funded-compute deals | Bull | "Apollo, Blackstone $35B AI deal for Anthropic" [Perigon, 2026-06-12] |
| Street support despite the miss | Bull | "Broadcom Stock Pops After JPMorgan Calls For Aggressive Buying" [FMP, 2026-06-17]; "Good News for Broadcom Stock Fans" [FMP, 2026-06-18] |
| AI-bubble / valuation skepticism | Concern | "Legendary Short Seller Jim Chanos Issues Dire Prediction: "We Have the Same Setup" As the Dot-Com Crash…" [FMP, 2026-06-17] |

#### ASML

| Theme | Lean | Verbatim headline(s) [source, date] |
|---|---|---|
| Record valuation / Europe's most valuable | Bull | "ASML becomes Europe's most valuable listed company" [Perigon, 2026-06-12]; "ASML Stock Surges on Record $700B Market Cap" [Perigon, 2026-06-11] |
| China export-control / MATCH Act risk | Concern | "China warns MATCH Act chip export curbs" [Perigon, 2026-04-26]; "ASML faces proposed US China export curbs" [Perigon, 2026-04-08] |
| Restructuring / layoffs | Concern | "ASML plans 1,700 layoffs amid restructure" [Perigon, 2026-04-24]; "ASML finalizes social plan, delays 1,700 job cuts" [Perigon, 2026-06-13] |
| High-NA EUV ramp + raised guidance | Bull | "ASML Expects First High-NA Chip Products Within Months" [FMP, 2026-05-19]; "ASML Raises 2026 Net Sales Guidance on Strong Q1" [Perigon, 2026-04-18] |
| Valuation debate (overvalued?) | Neutral | "Is ASML Overvalued? DCF Says Worth $1075" [FMP, 2026-05-18]; "ASML Premium Shrinks To Decade Low As Shares Rise 36% YTD" [FMP, 2026-04-16] |

#### KLAC

| Theme | Lean | Verbatim headline(s) [source, date] |
|---|---|---|
| 10-for-1 stock split | Neutral | "KLA completes 10-for-1 stock split" [Perigon, 2026-06-16]; "KLA announces 10-for-1 stock split, dividend" [Perigon, 2026-05-15] |
| Earnings + AI chip-equipment rally | Bull | "KLA shares jump 10% after earnings, split" [Perigon, 2026-06-12]; "Applied Materials, KLA stocks gain as AI boom lifts chip equipment outlook" [FMP, 2026-06-11] |
| Process-control / 2nm & yield positioning | Bull | "KLA Corporation: Quietly Dominating The 2nm Hyperscaler Race" [FMP, 2026-05-15]; "Is KLA Becoming the Biggest Beneficiary of AI Semiconductor Spending?" [FMP, 2026-05-14] |
| China chip-tool restrictions | Concern | "US orders multiple chip-tool halts, Hua Hong" [Perigon, 2026-05-01]; "KLA stock drops 3.35% on Samsung-strike fears" [Perigon, 2026-05-17] |
| Valuation / post-split warning & buyback | Neutral | "After a 45% Rally, This Post-Split Stock May Be Sending a Warning Signal" [FMP, 2026-06-16]; "KLAC DCF Analysis: Intrinsic Value $1108 vs Price $1737" [FMP, 2026-04-13] |

#### AMKR

| Theme | Lean | Verbatim headline(s) [source, date] |
|---|---|---|
| TSMC 10-year advanced-packaging partnership | Bull | "Amkor shares jump on 10-year TSMC partnership" [Perigon, 2026-06-18]; "TSMC and Amkor Technology Announce Long Term Partnership to Accelerate Advanced Packaging in the United States" [FMP, 2026-06-16] |
| Arizona $7B expansion / re-rating | Bull | "Amkor $7B Arizona advanced packaging expansion plans" [Perigon, 2026-05-25]; "Amkor Technology: The Arizona Re-Rating Has More Room To Run" [FMP, 2026-05-12] |
| Earnings beat but stock dipped | Neutral | "Amkor Q1 Beats; Issues Q2 and 2026 Guidance" [Perigon, 2026-04-29]; "Amkor Shares Dip After Q1 2026 Earnings Beat" [Perigon, 2026-05-01] |
| Debt financing ($1.15B convertible) | Concern | "Amkor stock rise after $1.15 billion debt deal" [Perigon, 2026-05-12]; "Amkor plans $1B convertible notes offering" [Perigon, 2026-05-02] |
| AI packaging / HDFO / smartphone demand | Bull | "Amkor shares surge 7.6% amid packaging targets" [Perigon, 2026-06-12]; "Can HDFO Adoption Strengthen Amkor's Compute Growth Opportunity?" [FMP, 2026-06-12] |"""


doc = (f"# TSM ANALYSIS\n\n*Generated {date}. All figures USD. Part 1 = financials; Part 2 = narrative.*\n\n"
       + "> Read **Section 4 — Data-Quality Notes** before drawing conclusions. An asterisk (\\*) marks a figure the notes flag as potentially misleading.\n\n"
       + DETERMINATION + "\n\n"
       + section_snapshot("current", "Section 1 — Current (latest quarter, annualized x4)") + "\n\n"
       + section_snapshot("ttm", "Section 2 — TTM (trailing four quarters)") + "\n\n"
       + section_trend() + "\n\n"
       + DATA_QUALITY + "\n\n"
       + GLOSSARY + "\n\n"
       + NARRATIVE + "\n\n"
       + EARNINGS_QA + "\n\n"
       + NEWS + "\n")

with open(os.path.join(base, "..", "TSM ANALYSIS.md"), "w") as f:
    f.write(doc)
print(doc)

#!/usr/bin/env python3
"""Format Peer_Compare_TSM_<date>.json into 'TSM ANALYSIS.md' (3 sections)."""
import json, os
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
base = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(base, "..", "Data", "screening",
                                f"Peer_Compare_TSM_{date}.json")))
TICKERS = ["TSM", "ASML", "KLAC", "NVDA", "AMD", "INTC", "AMKR"]
FY_END = {"TSM": "Dec", "ASML": "Dec", "KLAC": "Jun", "NVDA": "Jan",
          "AMD": "Dec", "INTC": "Dec", "AMKR": "Dec"}

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
    for key, label, kind, *_rest, direction in ROWS:
        tsm = d["TSM"][which].get(key)
        cells = [fmt(tsm, kind)]
        for t in TICKERS[1:]:
            v = d[t][which].get(key)
            delta = snap_cell(v, tsm, direction)
            if v is None:
                cells.append("NM")
            elif delta is None:
                cells.append(f"{fmt(v, kind)} (NM)")
            else:
                cells.append(f"{fmt(v, kind)} {delta}")
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
            L.append(f"| {label} | " + " | ".join(vals) + f" | {cstr} | {dstr} |")
        out.append("\n".join(L))
    return "\n".join(out)


GLOSSARY = f"""## Glossary

- **Companies:** TSM (anchor) vs ASML, KLAC (KLA), NVDA, AMD, INTC, AMKR.
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

doc = (f"# TSM ANALYSIS\n\n*Financials only. Generated {date}. All figures USD.*\n\n"
       + section_snapshot("current", "Section 1 — Current (latest quarter, annualized x4)") + "\n\n"
       + section_snapshot("ttm", "Section 2 — TTM (trailing four quarters)") + "\n\n"
       + section_trend() + "\n\n"
       + GLOSSARY + "\n")

with open(os.path.join(base, "..", "TSM ANALYSIS.md"), "w") as f:
    f.write(doc)
print(doc)

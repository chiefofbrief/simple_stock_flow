#!/usr/bin/env python3
"""
SEC Filings Script  (full-fetch + grep, US + foreign)
=====================================================

Fetches full SEC filings as TEXT (no section extraction — nothing is carved out, so
nothing can be truncated) and writes a triage report. The execution prompt greps the
full text for MD&A / footnote passages; this script just delivers the documents.

Regime is detected from which ANNUAL form the company actually files:
    10-K  -> US domestic : annual=10-K, periodic=10-Q (latest),  current list=8-K (w/ item codes)
    20-F  -> foreign     : annual=20-F, periodic=none,            current list=6-K (filename-tagged)
    40-F  -> Canadian    : annual=40-F, periodic=none,            current list=6-K

Source: SEC EDGAR only (submissions JSON gives forms, dates, accession/doc, 8-K item
codes, and doc descriptions in one call). No FMP dependency.

Outputs (Stock Data/{T}/):
    {T}_10k.txt | {T}_20f.txt | {T}_40f.txt   full annual filing text
    {T}_10q.txt                               full latest 10-Q (US only)
    {T}_filings_report.md                     triage summary (filings + 8-K/6-K list)
    raw/{T}_*.htm                             raw filing HTML

Usage:
    python sec_filings.py AAPL
"""

import sys
import os
import re
import json
import time
import argparse
import urllib.request
from datetime import datetime, timedelta
from html.parser import HTMLParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    get_writeup_directory,
    ensure_directory_exists,
    load_json,
)

USER_AGENT = "GL Research research@example.com"
SEC_DELAY = 0.2                    # SEC asks <=10 req/s
CURRENT_REPORT_DAYS = 182         # ~6 months
ANNUAL_MIN_WORDS = 10000          # full annual filing should be large
QUARTERLY_MIN_WORDS = 2500

ANNUAL_FORMS = ["10-K", "20-F", "40-F"]

# 8-K item codes -> short label. High-signal ones are recommended for a body pull.
ITEM_LABELS = {
    "1.01": "Entry into Material Agreement", "1.02": "Termination of Material Agreement",
    "1.03": "Bankruptcy", "2.01": "Completion of Acquisition/Disposition",
    "2.02": "Results of Operations (earnings)", "2.03": "Direct Financial Obligation",
    "2.04": "Triggering Events on Obligations", "3.01": "Delisting/Listing Standards",
    "3.02": "Unregistered Equity Sales", "4.01": "Change in Auditor",
    "4.02": "Non-Reliance on Prior Financials", "5.01": "Change in Control",
    "5.02": "Departure/Election of Directors or Officers", "5.03": "Amendments to Bylaws/Fiscal Year",
    "7.01": "Regulation FD", "8.01": "Other Events", "9.01": "Financial Statements & Exhibits",
}
HIGH_SIGNAL_ITEMS = {"1.01", "1.02", "2.01", "4.01", "4.02", "5.01", "5.02"}


# ---------------------------------------------------------------------------
# SEC requests
# ---------------------------------------------------------------------------

def sec_get(url, as_json=False):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    time.sleep(SEC_DELAY)
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read()
    return json.loads(raw) if as_json else raw.decode("utf-8", "ignore")


def get_cik(ticker):
    """CIK from profile.json (profile.py) if present, else SEC's company_tickers.json."""
    prof = load_json(os.path.join(get_data_directory(ticker), f"{ticker}_profile.json"))
    if prof and prof.get("cik"):
        return str(prof["cik"]).zfill(10)
    print("  Looking up CIK from SEC company_tickers.json...")
    data = sec_get("https://www.sec.gov/files/company_tickers.json", as_json=True)
    for entry in data.values():
        if (entry.get("ticker") or "").upper() == ticker.upper():
            return str(entry.get("cik_str", "")).zfill(10)
    return None


# ---------------------------------------------------------------------------
# HTML -> text
# ---------------------------------------------------------------------------

class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() in ("script", "style"):
            self._skip = True

    def handle_endtag(self, tag):
        if tag.lower() in ("script", "style"):
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            t = data.strip()
            if t:
                self.parts.append(t)


def html_to_text(html):
    html = re.sub(r"</?(ix|xbrli):[^>]*>", "", html)
    p = _TextExtractor()
    try:
        p.feed(html)
    except Exception:
        pass
    return "\n".join(p.parts)


# ---------------------------------------------------------------------------
# Filing enumeration
# ---------------------------------------------------------------------------

def parse_filings(submissions):
    r = submissions.get("filings", {}).get("recent", {})
    n = len(r.get("form", []))
    def col(k):
        v = r.get(k, [])
        return v + [""] * (n - len(v))
    forms, dates, rdates = col("form"), col("filingDate"), col("reportDate")
    accns, docs, descs, items = col("accessionNumber"), col("primaryDocument"), col("primaryDocDescription"), col("items")
    out = []
    for i in range(n):
        out.append({"form": forms[i], "filingDate": dates[i], "reportDate": rdates[i],
                    "accession": accns[i], "doc": docs[i], "desc": descs[i], "items": items[i]})
    return out


def latest_of(filings, form):
    cands = [f for f in filings if f["form"] == form and f["doc"]]
    return max(cands, key=lambda f: f["filingDate"]) if cands else None


def detect_regime(filings):
    """The most recent annual form (10-K / 20-F / 40-F) decides the regime."""
    annuals = [f for f in filings if f["form"] in ANNUAL_FORMS and f["doc"]]
    if not annuals:
        return None
    annual = max(annuals, key=lambda f: f["filingDate"])
    form = annual["form"]
    if form == "10-K":
        return {"regime": "US", "annual": annual, "periodic_form": "10-Q", "current_form": "8-K"}
    return {"regime": "Foreign" if form == "20-F" else "Canadian",
            "annual": annual, "periodic_form": None, "current_form": "6-K"}


def doc_url(cik, accession, doc):
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/{doc}"


# ---------------------------------------------------------------------------
# Current-report (8-K / 6-K) triage
# ---------------------------------------------------------------------------

def classify_8k(items_str):
    codes = [c.strip() for c in (items_str or "").split(",") if c.strip()]
    labels = [f"{c} {ITEM_LABELS.get(c, '')}".strip() for c in codes]
    high = any(c in HIGH_SIGNAL_ITEMS for c in codes)
    return codes, "; ".join(labels) if labels else "(no item codes)", high


def classify_6k(doc):
    """Classify a 6-K by its (often generic) primary-document filename.

    6-K filenames are unreliable — the meaningful content is frequently in an exhibit,
    not the cover doc — so we can't positively identify every type. Strategy: suppress
    the clearly-routine recurring filings (monthly revenue / dividend / board / AGM) and
    FLAG everything else — financials and unclassified named events — for a look.
    """
    d = (doc or "").lower()
    if any(w in d for w in ("consolidatedreport", "results", "earnings", "quarterlyreport", "fsx", "-fs", "financialstatement")):
        return "Results / Financials", True
    if any(w in d for w in ("revenue", "monthend", "monthly")):
        return "Monthly revenue", False
    if "dividend" in d:
        return "Dividend", False
    if any(w in d for w in ("agm", "annualgeneral", "shareholders", "meeting")):
        return "AGM / Shareholders", False
    if "board" in d:
        return "Board", False
    return "Other (review)", True   # unclassified named event — flag so material items surface


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def build_report(ticker, info, fetched, current_rows, notes):
    lines = [f"# SEC Filings Report: {ticker}",
             f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*",
             f"**Regime:** {info['regime']} "
             f"({info['annual']['form']}" + (f" / {info['periodic_form']}" if info['periodic_form'] else "")
             + f" / {info['current_form']})", ""]

    lines += ["## Filings Fetched", "", "| Form | Filing Date | Full-doc words | Fetch OK? |",
              "|---|---|---|---|"]
    for f in fetched:
        ok = "✓" if f["ok"] else "⚠ suspect"
        lines.append(f"| {f['form']} | {f['filingDate']} | {f['words']:,} | {ok} |")
    lines.append("")

    cur_form = info["current_form"]
    lines += [f"## Current Reports — Last 6 Months ({cur_form})", ""]
    if current_rows:
        if cur_form == "8-K":
            lines += ["| Date | Item codes | Description | Recommend pull? |", "|---|---|---|---|"]
        else:
            lines += ["| Date | Filename | Likely type | Recommend pull? |", "|---|---|---|---|"]
        # flagged rows first, then by date desc
        for row in sorted(current_rows, key=lambda x: (not x["high"], x["date"]), reverse=False):
            rec = "✓" if row["high"] else ""
            if cur_form == "8-K":
                lines.append(f"| {row['date']} | {row['codes']} | {row['desc']} | {rec} |")
            else:
                lines.append(f"| {row['date']} | {row['doc']} | {row['type']} | {rec} |")
        lines.append("")
        lines.append("*Bodies are not auto-pulled — flagged (✓) rows are the high-signal ones to fetch on demand.*")
    else:
        lines.append(f"*No {cur_form} filings in the last 6 months.*")
    lines.append("")

    lines += ["## Notes", ""]
    lines += [f"- {n}" for n in notes] if notes else ["- None."]
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def fetch_full(cik, filing, ticker, out_name, min_words, raw_dir, writeup_dir, notes):
    """Fetch a filing's full text, save .txt + raw .htm. Returns a fetched-row dict."""
    url = doc_url(cik, filing["accession"], filing["doc"])
    try:
        html = sec_get(url)
    except Exception as e:
        notes.append(f"{filing['form']} fetch failed: {e}")
        return {"form": filing["form"], "filingDate": filing["filingDate"], "words": 0, "ok": False}
    text = html_to_text(html)
    words = len(text.split())
    ok = words >= min_words
    with open(os.path.join(writeup_dir, f"{ticker}_{out_name}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(raw_dir, f"{ticker}_{out_name}.htm"), "w", encoding="utf-8") as f:
        f.write(html)
    if not ok:
        notes.append(f"{filing['form']} only {words:,} words (< {min_words:,}) — verify the fetch.")
    return {"form": filing["form"], "filingDate": filing["filingDate"], "words": words, "ok": ok}


def process(ticker):
    print(f"\n=== SEC Filings: {ticker} ===")
    cik = get_cik(ticker)
    if not cik:
        raise ValueError("could not resolve CIK")
    print(f"  CIK: {cik}")

    submissions = sec_get(f"https://data.sec.gov/submissions/CIK{cik}.json", as_json=True)
    filings = parse_filings(submissions)
    info = detect_regime(filings)
    if not info:
        raise ValueError("no annual filing (10-K/20-F/40-F) found on EDGAR")
    print(f"  Regime: {info['regime']} — annual {info['annual']['form']} ({info['annual']['filingDate']})")

    raw_dir = get_data_directory(ticker)
    writeup_dir = get_writeup_directory(ticker)
    ensure_directory_exists(raw_dir)
    ensure_directory_exists(writeup_dir)

    notes, fetched = [], []
    # annual
    annual_name = info["annual"]["form"].lower().replace("-", "")  # 10-K -> 10k, 20-F -> 20f
    fetched.append(fetch_full(cik, info["annual"], ticker, annual_name, ANNUAL_MIN_WORDS,
                              raw_dir, writeup_dir, notes))
    # periodic (US only)
    if info["periodic_form"]:
        pf = latest_of(filings, info["periodic_form"])
        if pf:
            fetched.append(fetch_full(cik, pf, ticker, "10q", QUARTERLY_MIN_WORDS,
                                      raw_dir, writeup_dir, notes))
        else:
            notes.append(f"No {info['periodic_form']} found on EDGAR.")

    # current reports (8-K / 6-K) last 6 months
    cutoff = (datetime.now() - timedelta(days=CURRENT_REPORT_DAYS)).strftime("%Y-%m-%d")
    current_rows = []
    for f in filings:
        if f["form"] != info["current_form"] or f["filingDate"] < cutoff:
            continue
        if info["current_form"] == "8-K":
            codes, desc, high = classify_8k(f["items"])
            current_rows.append({"date": f["filingDate"], "codes": ", ".join(codes) or "—",
                                 "desc": desc, "high": high})
        else:
            typ, high = classify_6k(f["doc"])
            current_rows.append({"date": f["filingDate"], "doc": f["doc"], "type": typ, "high": high})

    if info["current_form"] == "6-K" and current_rows:
        notes.append("6-K types are inferred from (often generic) filenames; routine monthly-revenue/"
                     "dividend/board/AGM filings are suppressed and everything else is flagged for "
                     "review. Foreign quarterly numbers come from numbers.py + the earnings call.")

    report = build_report(ticker, info, fetched, current_rows, notes)
    with open(os.path.join(writeup_dir, f"{ticker}_filings_report.md"), "w", encoding="utf-8") as f:
        f.write(report)

    print("  Fetched: " + ", ".join(f"{x['form']} ({x['words']:,}w)" for x in fetched))
    print(f"  {info['current_form']} last 6mo: {len(current_rows)} "
          f"({sum(1 for r in current_rows if r['high'])} flagged)")
    print(f"  ✓ Report: {os.path.join(writeup_dir, f'{ticker}_filings_report.md')}")


def main():
    ap = argparse.ArgumentParser(description="SEC filings — full-fetch + triage report (US + foreign)")
    ap.add_argument("tickers", nargs="+")
    args = ap.parse_args()
    failures = []
    for t in [x.upper() for x in args.tickers]:
        try:
            process(t)
        except Exception as e:
            print(f"  ✗ {t} FAILED: {e}")
            failures.append(t)
    if failures:
        print(f"\nFailed: {', '.join(failures)}")
        sys.exit(1)
    print("\nDone.")


if __name__ == "__main__":
    main()

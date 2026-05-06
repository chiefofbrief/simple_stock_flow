#!/usr/bin/env python3
"""
Financial Statements Analysis (FMP Version)
===========================================

Fetches financial statements from FMP (Annual & Quarterly) and calculates:
1. Earnings Risk
2. Earnings Quality
3. ROI

Includes detailed statistical analysis (CAGR, CV, Slope, Deltas).
Calculates TTM manually from quarterly data if TTM endpoints are unavailable.

Outputs:
- Raw JSON files in data/tickers/{TICKER}/raw/
- Aggregated metrics JSON in data/tickers/{TICKER}/
- Markdown report in data/tickers/{TICKER}/

Usage:
    python financials.py TICKER
"""

import sys
import os
import argparse
import requests
import statistics
import math
from datetime import datetime

# Ensure shared_utils can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
    load_json
)

FMP_BASE_URL = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")

# ============================================================================
# Math / Stat Helpers
# ============================================================================

def safe_float(val):
    if val is None: return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def safe_div(n, d):
    if n is None or d is None or d == 0:
        return None
    return n / d

def pct_change(curr, prev):
    if curr is None or prev is None or prev == 0:
        return None
    return (curr - prev) / abs(prev)

def calculate_cagr(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2 or clean[0] <= 0 or clean[-1] <= 0:
        return None
    years = len(clean) - 1
    try:
        return (clean[-1] / clean[0]) ** (1 / years) - 1
    except:
        return None

def calculate_cv(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2: return None
    mean = statistics.mean(clean)
    if abs(mean) < 1e-9: return None
    stdev = statistics.stdev(clean)
    return stdev / abs(mean)

def calculate_slope(values):
    y = [v for v in values if v is not None]
    n = len(y)
    if n < 2: return None
    x = list(range(n))
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = sum((xi - mean_x) ** 2 for xi in x)
    if denominator == 0: return None
    return numerator / denominator

def calculate_recent_delta(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2: return None
    return pct_change(clean[-1], clean[-2])

# ============================================================================
# Data Fetching
# ============================================================================

def fetch_endpoint(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        # Check for 402/403 which means plan limit
        if "402" in str(e) or "403" in str(e):
            print(f"  Plan restriction for {url}")
        else:
            print(f"  Error fetching {url}: {e}")
        return None

def fetch_all_financials(ticker):
    print(f"Fetching financial statements for {ticker} from FMP...")
    
    data = {"annual": {}, "quarterly": {}}
    
    # Fetch Annual (Limit 10)
    data['annual']['income'] = fetch_endpoint(f"{FMP_BASE_URL}/income-statement?symbol={ticker}&limit=10&apikey={FMP_API_KEY}")
    data['annual']['balance'] = fetch_endpoint(f"{FMP_BASE_URL}/balance-sheet-statement?symbol={ticker}&limit=10&apikey={FMP_API_KEY}")
    data['annual']['cash_flow'] = fetch_endpoint(f"{FMP_BASE_URL}/cash-flow-statement?symbol={ticker}&limit=10&apikey={FMP_API_KEY}")
    
    # Fetch Quarterly (Limit 6 for TTM calculation and recent trend)
    data['quarterly']['income'] = fetch_endpoint(f"{FMP_BASE_URL}/income-statement?symbol={ticker}&period=quarter&limit=6&apikey={FMP_API_KEY}")
    data['quarterly']['balance'] = fetch_endpoint(f"{FMP_BASE_URL}/balance-sheet-statement?symbol={ticker}&period=quarter&limit=6&apikey={FMP_API_KEY}")
    data['quarterly']['cash_flow'] = fetch_endpoint(f"{FMP_BASE_URL}/cash-flow-statement?symbol={ticker}&period=quarter&limit=6&apikey={FMP_API_KEY}")

    # Validate minimal data presence
    if not all(data['annual'].values()) or not all(data['quarterly'].values()):
        print("Failed to fetch required statements (Annual or Quarterly).")
        return None
        
    return data

# ============================================================================
# Metric Processing
# ============================================================================

def calculate_ttm_metrics(quarterly_data):
    """Calculates TTM metrics from the last 4 quarters."""
    # Quarters are newest first
    q_inc = quarterly_data['income'][:4]
    q_bal = quarterly_data['balance'][:4]
    q_cf = quarterly_data['cash_flow'][:4]
    
    if len(q_inc) < 4 or len(q_cf) < 4:
        return None

    # Helper to sum 4 quarters
    def sum_q(dataset, key):
        return sum(safe_float(x.get(key)) or 0 for x in dataset)

    # Helper to get latest quarter value (for Balance Sheet)
    def latest(dataset, key):
        return safe_float(dataset[0].get(key))

    # TTM Values
    rev = sum_q(q_inc, 'revenue')
    oi = sum_q(q_inc, 'operatingIncome')
    ni = sum_q(q_inc, 'netIncome')
    
    ocf = sum_q(q_cf, 'operatingCashFlow')
    capex = sum_q(q_cf, 'capitalExpenditure')
    da = sum_q(q_cf, 'depreciationAndAmortization')
    sbc = sum_q(q_cf, 'stockBasedCompensation')
    
    # Balance Sheet (Point in Time - use latest)
    assets = latest(q_bal, 'totalAssets')
    ca = latest(q_bal, 'totalCurrentAssets')
    cl = latest(q_bal, 'totalCurrentLiabilities')
    debt = latest(q_bal, 'totalDebt')
    equity = latest(q_bal, 'totalEquity')
    cash = latest(q_bal, 'cashAndCashEquivalents')

    # ROIC inputs (sum 4 quarters for income statement items)
    interest_exp = sum_q(q_inc, 'interestExpense')
    pretax_income = sum_q(q_inc, 'incomeBeforeTax')
    tax_expense = sum_q(q_inc, 'incomeTaxExpense')

    # Calculate Metrics
    # Note: Capex is usually negative in CF statement
    abs_capex = abs(capex) if capex is not None else 0

    # ROIC = NOPAT / Invested Capital
    # NOPAT = Net Income + Interest Expense × (1 - Tax Rate)
    # Invested Capital = Total Equity + Total Debt - Cash
    tax_rate = safe_div(tax_expense, pretax_income)
    interest_paid = abs(interest_exp) if interest_exp else 0
    if ni is not None and tax_rate is not None and equity is not None and debt is not None:
        nopat = ni + interest_paid * (1 - tax_rate)
        invested_capital = equity + debt - (cash or 0)
        roic = safe_div(nopat, invested_capital)
    else:
        roic = None

    return {
        "revenue": rev,
        "operating_margin": safe_div(oi, rev),
        "ocf": ocf,
        "fcf": (ocf - abs_capex) if ocf is not None else None,
        "ocf_to_ni": safe_div(ocf, ni),
        "sbc": sbc,
        "sbc_to_rev": safe_div(sbc, rev),
        "working_capital": (ca - cl) if ca is not None and cl is not None else None,
        # Operating Leverage is calculated via deltas in process_metrics, not here directly for TTM usually,
        # but we need a placeholder or calculation if possible. TTM Op Lev is tricky without TTM-1.
        # We will handle Op Lev in process_metrics.
        "capex": capex,
        "da": da,
        "capex_to_dep": safe_div(abs_capex, da),
        "dep_to_rev": safe_div(da, rev),
        "debt_to_assets": safe_div(debt, assets),
        "debt_to_ocf": safe_div(debt, ocf),
        "roic": roic,

        "_oi": oi, "_rev": rev # internal use
    }

def extract_period_metrics(inc, bal, cf):
    """Extracts metrics for a single period (annual or quarterly)."""
    def get(d, k): return safe_float(d.get(k))
    
    rev = get(inc, 'revenue')
    oi = get(inc, 'operatingIncome')
    ni = get(inc, 'netIncome')
    
    assets = get(bal, 'totalAssets')
    ca = get(bal, 'totalCurrentAssets')
    cl = get(bal, 'totalCurrentLiabilities')
    debt = get(bal, 'totalDebt')
    equity = get(bal, 'totalEquity')
    cash = get(bal, 'cashAndCashEquivalents')

    ocf = get(cf, 'operatingCashFlow')
    capex = get(cf, 'capitalExpenditure')
    da = get(cf, 'depreciationAndAmortization')
    sbc = get(cf, 'stockBasedCompensation')

    interest_exp = get(inc, 'interestExpense')
    pretax_income = get(inc, 'incomeBeforeTax')
    tax_expense = get(inc, 'incomeTaxExpense')

    abs_capex = abs(capex) if capex is not None else 0

    # ROIC = NOPAT / Invested Capital
    tax_rate = safe_div(tax_expense, pretax_income)
    interest_paid = abs(interest_exp) if interest_exp else 0
    if ni is not None and tax_rate is not None and equity is not None and debt is not None:
        nopat = ni + interest_paid * (1 - tax_rate)
        invested_capital = equity + debt - (cash or 0)
        roic = safe_div(nopat, invested_capital)
    else:
        roic = None

    return {
        "revenue": rev,
        "operating_margin": safe_div(oi, rev),
        "ocf": ocf,
        "fcf": (ocf - abs_capex) if ocf is not None else None,
        "ocf_to_ni": safe_div(ocf, ni),
        "sbc": sbc,
        "sbc_to_rev": safe_div(sbc, rev),
        "working_capital": (ca - cl) if ca is not None and cl is not None else None,
        "capex": capex,
        "da": da,
        "capex_to_dep": safe_div(abs_capex, da),
        "dep_to_rev": safe_div(da, rev),
        "debt_to_assets": safe_div(debt, assets),
        "debt_to_ocf": safe_div(debt, ocf),
        "roic": roic,

        "_oi": oi, "_rev": rev
    }

def process_metrics(raw_data):
    """Process Annual, Quarterly, and TTM metrics."""
    
    # --- 1. Annual Processing ---
    # Sort oldest first
    ann_inc = sorted(raw_data['annual']['income'], key=lambda x: x['date'])
    ann_bal = sorted(raw_data['annual']['balance'], key=lambda x: x['date'])
    ann_cf = sorted(raw_data['annual']['cash_flow'], key=lambda x: x['date'])
    
    aligned_annual = []
    for inc in ann_inc:
        date = inc['date']
        bal = next((x for x in ann_bal if x['date'] == date), None)
        cf = next((x for x in ann_cf if x['date'] == date), None)
        if bal and cf:
            aligned_annual.append({"year": date[:4], "inc": inc, "bal": bal, "cf": cf})
    
    # Last 5 years
    aligned_annual = aligned_annual[-5:]
    annual_dates = [x['year'] for x in aligned_annual]
    
    annual_metrics = [extract_period_metrics(x['inc'], x['bal'], x['cf']) for x in aligned_annual]
    
    # Annual Op Leverage
    ann_op_lev = []
    for i in range(len(annual_metrics)):
        if i == 0:
            ann_op_lev.append(None)
        else:
            cur = annual_metrics[i]
            prev = annual_metrics[i-1]
            oi_chg = pct_change(cur['_oi'], prev['_oi'])
            rev_chg = pct_change(cur['_rev'], prev['_rev'])
            if rev_chg and rev_chg != 0 and oi_chg is not None:
                ann_op_lev.append(oi_chg / rev_chg)
            else:
                ann_op_lev.append(None)
                
    # --- 2. Quarterly Processing ---
    q_inc = sorted(raw_data['quarterly']['income'], key=lambda x: x['date'])
    q_bal = sorted(raw_data['quarterly']['balance'], key=lambda x: x['date'])
    q_cf = sorted(raw_data['quarterly']['cash_flow'], key=lambda x: x['date'])
    
    aligned_quarterly = []
    for inc in q_inc:
        date = inc['date']
        bal = next((x for x in q_bal if x['date'] == date), None)
        cf = next((x for x in q_cf if x['date'] == date), None)
        if bal and cf:
            aligned_quarterly.append({"date": date, "inc": inc, "bal": bal, "cf": cf})
            
    # Need last 5 quarters to show 4 with deltas
    recent_quarters = aligned_quarterly[-5:]
    quarterly_dates = [x['date'] for x in recent_quarters]
    
    quarterly_metrics = [extract_period_metrics(x['inc'], x['bal'], x['cf']) for x in recent_quarters]
    
    # Quarterly Op Leverage
    quart_op_lev = []
    for i in range(len(quarterly_metrics)):
        if i == 0:
            quart_op_lev.append(None)
        else:
            cur = quarterly_metrics[i]
            prev = quarterly_metrics[i-1]
            oi_chg = pct_change(cur['_oi'], prev['_oi'])
            rev_chg = pct_change(cur['_rev'], prev['_rev'])
            if rev_chg and rev_chg != 0 and oi_chg is not None:
                quart_op_lev.append(oi_chg / rev_chg)
            else:
                quart_op_lev.append(None)

    # --- 3. TTM Processing ---
    ttm_metrics = calculate_ttm_metrics(raw_data['quarterly'])
    
    # --- 4. Series Construction ---
    final_data = {
        "dates": annual_dates,
        "quarterly_dates": quarterly_dates,
        "financials": {}
    }
    
    # Flattened list of metrics
    metric_keys = [
        'revenue',
        'operating_margin',
        'ocf',
        'fcf',
        'ocf_to_ni',
        'sbc',
        'sbc_to_rev',
        'working_capital',
        'operating_leverage',
        'capex',
        'da',
        'capex_to_dep',
        'dep_to_rev',
        'debt_to_assets',
        'debt_to_ocf',
        'roic'
    ]
    
    for key in metric_keys:
        # -- Annual Values --
        if key == 'operating_leverage':
            vals = ann_op_lev
            ttm_val = None 
        else:
            vals = [m[key] for m in annual_metrics]
            ttm_val = ttm_metrics[key] if ttm_metrics else None
        
        clean_vals = [v for v in vals if v is not None]
        
        stats = {
            "cagr_5yr": calculate_cagr(vals),
            "cv": calculate_cv(vals),
            "slope": calculate_slope(vals),
            "recent_delta": calculate_recent_delta(vals),
            "mean_5yr": statistics.mean(clean_vals) if clean_vals else None
        }
        
        # -- Quarterly Values --
        if key == 'operating_leverage':
            q_vals = quart_op_lev
        else:
            q_vals = [m[key] for m in quarterly_metrics]
        
        final_data['financials'][key] = {
            "annual_values": vals,
            "quarterly_values": q_vals,
            "ttm_value": ttm_val,
            "stats": stats
        }
            
    return final_data

# ============================================================================
# Markdown Generation
# ============================================================================

def format_cell(val, fmt, div=1, is_delta=False):
    if val is None: return "-"
    try:
        if div != 1: val /= div
        formatted = fmt.format(val)
        if is_delta and val > 0: formatted = "+" + formatted
        return formatted
    except:
        return str(val)

def generate_markdown(ticker, data, role=None):
    dates = data['dates']
    q_dates = data['quarterly_dates']
    
    # Pad dates if < 5
    display_dates = ["-"] * (5 - len(dates)) + dates
    
    role_label = f" [{role}]" if role else ""
    md = f"# Financial Statement Analysis: {ticker}{role_label}\n\n"
    md += f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
    
    # --- Annual Header ---
    # Y1 | Y2 | Δ% | Y3 | Δ% | Y4 | Δ% | Y5 | Δ% | TTM | ...
    header_cols = [display_dates[0]]
    for d in display_dates[1:]:
        header_cols.extend([d, "Δ%"])
        
    ann_header = f"| Metric | {' | '.join(header_cols)} | TTM | 5yr Avg | 5yr CAGR | CV |\n"
    ann_sep = f"|---|{'---|'*len(header_cols)}---|---|---|---|\n"
    
    # --- Quarterly Header ---
    # Display: Q(N-3) | Δ | Q(N-2) | Δ | Q(N-1) | Δ | Q(N) | Δ
    
    # Identify displayable quarters (exclude the very first one used for delta only)
    disp_q_dates = q_dates[1:] if len(q_dates) > 1 else q_dates
    # Pad if needed
    if len(disp_q_dates) < 4:
        disp_q_dates = ["-"] * (4 - len(disp_q_dates)) + disp_q_dates
        
    q_header_cols = []
    for d in disp_q_dates:
        q_header_cols.extend([d, "Δ%"])
    
    q_header = f"| Metric | {' | '.join(q_header_cols)} |\n"
    q_sep = f"|---|{'---|'*len(q_header_cols)}\n"

    def build_table_rows(category_key, rows):
        table_md_annual = ""
        table_md_quarterly = ""
        
        for label, key, fmt, *divisor in rows:
            div = divisor[0] if divisor else 1
            metric_data = data[category_key][key]
            
            # --- Annual Row ---
            vals = metric_data['annual_values']
            
            # Display absolute values for CapEx (since label is "Expenditure")
            if key == 'capex':
                vals = [abs(v) if v is not None else None for v in vals]
                
            d_vals = [None]*(5 - len(vals)) + vals
            ttm = metric_data['ttm_value']
            if key == 'capex' and ttm is not None: ttm = abs(ttm)
            
            stats = metric_data['stats']
            mean_5yr = stats['mean_5yr']
            if key == 'capex' and mean_5yr is not None: mean_5yr = abs(mean_5yr)
            
            row_a = f"| {label} |"
            
            # Y1
            row_a += f" {format_cell(d_vals[0], fmt, div)} |"
            
            # Y2-Y5 (Val | Delta)
            for i in range(1, 5):
                curr = d_vals[i]
                prev = d_vals[i-1]
                row_a += f" {format_cell(curr, fmt, div)} |"
                
                # Suppress Delta for Operating Leverage (meaningless ratio of ratios)
                if key != 'operating_leverage' and curr is not None and prev is not None and prev != 0:
                    delta = (curr - prev) / abs(prev)
                    row_a += f" {format_cell(delta, '{:.1%}', 1, True)} |"
                else:
                    row_a += " - |"
            
            # Stats
            row_a += f" {format_cell(ttm, fmt, div)} |"
            row_a += f" {format_cell(mean_5yr, fmt, div)} |"
            row_a += f" {format_cell(stats['cagr_5yr'], '{:.1%}')} |"
            row_a += f" {format_cell(stats['cv'], '{:.2f}')} |"
            
            table_md_annual += row_a + "\n"
            
            # --- Quarterly Row ---
            q_vals = metric_data['quarterly_values']
            if key == 'capex':
                q_vals = [abs(v) if v is not None else None for v in q_vals]
                
            if len(q_vals) < 5:
                q_vals = [None]*(5 - len(q_vals)) + q_vals
            
            row_q = f"| {label} |"
            for i in range(1, 5):
                curr = q_vals[i]
                prev = q_vals[i-1]
                
                row_q += f" {format_cell(curr, fmt, div)} |"
                
                # Suppress Delta for Operating Leverage
                if key != 'operating_leverage' and curr is not None and prev is not None and prev != 0:
                    delta = (curr - prev) / abs(prev)
                    row_q += f" {format_cell(delta, '{:.1%}', 1, True)} |"
                else:
                    row_q += " - |"
            table_md_quarterly += row_q + "\n"
            
        return table_md_annual, table_md_quarterly

    # Define the rows in specific order
    metric_rows = [
        ("Revenue ($B)", "revenue", "${:,.2f}", 1e9),
        ("Operating Margin", "operating_margin", "{:.1%}"),
        ("Op Cash Flow ($B)", "ocf", "${:,.2f}", 1e9),
        ("Free Cash Flow ($B)", "fcf", "${:,.2f}", 1e9),
        ("OCF / Net Income", "ocf_to_ni", "{:.2f}x"),
        ("SBC ($B)", "sbc", "${:,.2f}", 1e9),
        ("  ↳ SBC / Revenue", "sbc_to_rev", "{:.1%}"),
        ("Working Capital ($B)", "working_capital", "${:,.2f}", 1e9),
        ("Operating Leverage", "operating_leverage", "{:.2f}"),
        ("CapEx ($B)", "capex", "${:,.2f}", 1e9),
        ("D&A ($B)", "da", "${:,.2f}", 1e9),
        ("  ↳ Capex / D&A", "capex_to_dep", "{:.1%}"),
        ("  ↳ D&A / Revenue", "dep_to_rev", "{:.1%}"),
        ("Debt / Assets", "debt_to_assets", "{:.1%}"),
        ("Debt / OCF", "debt_to_ocf", "{:.2f}x"),
        ("ROIC", "roic", "{:.1%}"),
    ]

    ann_rows, quart_rows = build_table_rows("financials", metric_rows)

    md += "## Financial Analysis\n\n"
    
    md += "### Annual & Long-Term Trends\n"
    md += ann_header + ann_sep + ann_rows + "\n"
    
    md += "### Recent Quarterly Trends\n"
    md += q_header + q_sep + quart_rows + "\n"
    
    md += "---\n*TTM = Trailing Twelve Months. CV = Coefficient of Variation.*\n"
    return md

# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Financial Statements Analysis")
    parser.add_argument("ticker", help="Primary ticker symbol")
    parser.add_argument("--peers", nargs="*", metavar="PEER", help="Optional peer tickers (max 2)")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    peers = [p.upper() for p in (args.peers or [])][:2]

    if not FMP_API_KEY:
        print("Error: FMP_API_KEY not set.")
        sys.exit(1)

    all_tickers = [(ticker, "Target")] + [(p, f"Peer {i+1}") for i, p in enumerate(peers)]
    combined_md = ""
    failures = []

    for t, role in all_tickers:
        print(f"\nProcessing {t} ({role})...")
        try:
            raw_data = fetch_all_financials(t)
            if not raw_data:
                raise ValueError("Failed to fetch required financial statements")

            # Save raw (peers nest under target ticker's directory)
            target = ticker if t != ticker else None
            raw_dir = get_data_directory(t, target)
            ensure_directory_exists(raw_dir)
            save_json(raw_data['annual']['income'], os.path.join(raw_dir, f"{t}_income_annual.json"))
            save_json(raw_data['annual']['balance'], os.path.join(raw_dir, f"{t}_balance_annual.json"))
            save_json(raw_data['annual']['cash_flow'], os.path.join(raw_dir, f"{t}_cashflow_annual.json"))
            save_json(raw_data['quarterly']['income'], os.path.join(raw_dir, f"{t}_income_quarterly.json"))
            save_json(raw_data['quarterly']['balance'], os.path.join(raw_dir, f"{t}_balance_quarterly.json"))
            save_json(raw_data['quarterly']['cash_flow'], os.path.join(raw_dir, f"{t}_cashflow_quarterly.json"))
            print(f"  Raw data saved to {raw_dir}")

            # Process & save metrics
            metrics = process_metrics(raw_data)
            if not metrics or not metrics.get("financials"):
                raise ValueError("Metrics processing returned empty result")

            ticker_dir = os.path.dirname(raw_dir)
            save_json(metrics, os.path.join(ticker_dir, f"{t}_financial_metrics.json"))
            print(f"  ✓ Metrics saved — {len(metrics['dates'])} annual periods, {len(metrics['quarterly_dates'])} quarters")

            combined_md += generate_markdown(t, metrics, role=role) + "\n\n---\n\n"
        except Exception as e:
            print(f"  ✗ FAILED: {e}")
            failures.append(t)

    # Write combined report to primary ticker's directory
    if combined_md:
        primary_dir = os.path.dirname(get_data_directory(ticker))
        report_path = os.path.join(primary_dir, f"{ticker}_financial_analysis.md")
        with open(report_path, "w") as f:
            f.write(combined_md)
        print(f"\nReport saved to {report_path}")

    # --- Summary ---
    print("\n--- Summary ---")
    for t, role in all_tickers:
        status = "✗ FAILED" if t in failures else "✓"
        print(f"  {status}  {t} ({role})")

    if failures:
        print(f"\nFailed: {', '.join(failures)}")
        sys.exit(1)
    print("\nDone.")

if __name__ == "__main__":
    main()

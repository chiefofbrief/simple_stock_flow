#!/usr/bin/env python3
"""
Projection Seeds Calculator
===========================

Calculates the 8 projection seeds from raw financial data.
Isolates historical trends and averages for LLM interpretation.

Seeds Calculated:
1. Revenue
2. COGS %
3. SG&A %
4. R&D %
5. D&A
6. CapEx
7. Total Debt
8. Working Capital Components (A/R, Inventory, A/P)

Usage:
    python calc_seeds.py TICKER
"""

import sys
import os
import argparse
from datetime import datetime

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
    load_json
)

# Constants from original script
YEARS_TO_ANALYZE = 5

def safe_float(value, default=None):
    if value is None or value == 'None' or value == '':
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def pct(num, denom):
    if num is None or denom is None or denom == 0:
        return None
    return round((num / denom) * 100, 2)

def calculate_5yr_avg(values):
    clean = [v for v in values if v is not None]
    return round(sum(clean) / len(clean), 2) if clean else None

def calculate_cagr(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2 or clean[0] <= 0 or clean[-1] <= 0:
        return None
    years = len(clean) - 1
    return round((((clean[-1] / clean[0]) ** (1 / years)) - 1) * 100, 2)

def calculate_cv(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2: return None
    avg = sum(clean) / len(clean)
    if avg == 0: return None
    variance = sum((x - avg) ** 2 for x in clean) / len(clean)
    return round((variance ** 0.5 / abs(avg)) * 100, 2)

def calculate_slope(values):
    clean = [(i, v) for i, v in enumerate(values) if v is not None]
    if len(clean) < 2: return None
    n = len(clean)
    sum_x = sum(i for i, _ in clean)
    sum_y = sum(v for _, v in clean)
    sum_xy = sum(i * v for i, v in clean)
    sum_x2 = sum(i * i for i, _ in clean)
    denominator = n * sum_x2 - sum_x * sum_x
    if denominator == 0: return None
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    return round(slope, 2)

def calculate_recent_delta(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 2:
        return {'absolute': None, 'percent': None}
    recent, prior = clean[-1], clean[-2]
    absolute = round(recent - prior, 2)
    percent = round(((recent - prior) / prior * 100), 2) if prior != 0 else None
    return {'absolute': absolute, 'percent': percent}

def detect_outliers(values):
    clean = [v for v in values if v is not None]
    if len(clean) < 3: return []
    mean = sum(clean) / len(clean)
    variance = sum((x - mean) ** 2 for x in clean) / len(clean)
    std_dev = variance ** 0.5
    lower, upper = mean - 2*std_dev, mean + 2*std_dev
    return [i for i, v in enumerate(values) if v is not None and (v < lower or v > upper)]

def add_stats(values, years, unit, include_cagr=False):
    stats = {
        'values': values,
        'unit': unit,
        'current': values[-1] if values else None,
        'avg_5yr': calculate_5yr_avg(values),
        'cv': calculate_cv(values),
        'slope': calculate_slope(values),
        'recent_delta': calculate_recent_delta(values),
        'outlier_years': [years[i] for i in detect_outliers(values)]
    }
    if include_cagr:
        stats['cagr'] = calculate_cagr(values)
    return stats

def extract_annual_reports(data, years=YEARS_TO_ANALYZE):
    fiscal_years = sorted(list(set(
        r.get('fiscalDateEnding', '')[:4]
        for r in data['income'].get('annualReports', [])[:years]
        if r.get('fiscalDateEnding')
    )))[-years:]

    def get_report(reports, year):
        return next((r for r in reports if r.get('fiscalDateEnding', '').startswith(year)), {})

    return {
        'years': fiscal_years,
        'income': [get_report(data['income'].get('annualReports', []), y) for y in fiscal_years],
        'balance': [get_report(data['balance'].get('annualReports', []), y) for y in fiscal_years],
        'cashflow': [get_report(data['cashflow'].get('annualReports', []), y) for y in fiscal_years]
    }

def calculate_ytd_annualized(data):
    current_year = '2025'
    income_qtrs = [r for r in data.get('income', {}).get('quarterlyReports', [])
                   if r.get('fiscalDateEnding', '').startswith(current_year)]
    if not income_qtrs: return None
    
    num_q = len(income_qtrs)
    multiplier = 4 / num_q

    def annualize(statement, field):
        q_data = data.get(statement, {}).get('quarterlyReports', [])
        current_q = [r for r in q_data if r.get('fiscalDateEnding', '').startswith(current_year)]
        val = sum(safe_float(r.get(field, 0)) or 0 for r in current_q)
        return val * multiplier

    return {
        'num_quarters': num_q,
        'income': {f: annualize('income', f) for f in ['totalRevenue', 'costOfRevenue', 'sellingGeneralAndAdministrative', 'researchAndDevelopment', 'depreciationAndAmortization']},
        'cashflow': {f: annualize('cashflow', f) for f in ['operatingCashflow', 'capitalExpenditures', 'depreciationDepletionAndAmortization']},
        'balance': data.get('balance', {}).get('quarterlyReports', [{}])[0] # Use latest BS
    }

def calculate_projection_seeds(aligned_data, ytd_data=None):
    years, income, balance, cashflow = aligned_data['years'], aligned_data['income'], aligned_data['balance'], aligned_data['cashflow']

    def get_ytd(statement, field):
        return safe_float(ytd_data[statement].get(field)) if ytd_data else None

    def calc_debt(report):
        return sum(safe_float(report.get(k, 0)) or 0 for k in
                   ['shortTermDebt', 'currentLongTermDebt', 'longTermDebt']) or None

    revenue = [safe_float(r.get('totalRevenue')) for r in income]
    cogs = [safe_float(r.get('costOfRevenue')) for r in income]

    ytd_revenue = get_ytd('income', 'totalRevenue')
    ytd_cogs = get_ytd('income', 'costOfRevenue')

    seeds = {
        'revenue': {
            **add_stats(revenue, years, 'dollars', include_cagr=True),
            'ytd_value': ytd_revenue,
            'description': 'Total Revenue'
        },
        'cogs_pct': {
            **add_stats([pct(c, r) for c, r in zip(cogs, revenue)], years, 'percent'),
            'ytd_value': pct(ytd_cogs, ytd_revenue) if ytd_data and ytd_revenue else None,
            'description': 'COGS as % of Revenue'
        },
        'sga_pct': {
            **add_stats([pct(safe_float(r.get('sellingGeneralAndAdministrative')), revenue[i])
                        for i, r in enumerate(income)], years, 'percent'),
            'ytd_value': pct(get_ytd('income', 'sellingGeneralAndAdministrative'), ytd_revenue) if ytd_revenue else None,
            'description': 'SG&A as % of Revenue'
        },
        'rd_pct': {
            **add_stats([pct(safe_float(r.get('researchAndDevelopment', 0)) or 0, revenue[i])
                        for i, r in enumerate(income)], years, 'percent'),
            'ytd_value': pct(get_ytd('income', 'researchAndDevelopment') or 0, ytd_revenue) if ytd_revenue else None,
            'description': 'R&D as % of Revenue'
        },
        'depreciation_amortization': {
            **add_stats([safe_float(r.get('depreciationAndAmortization')) or
                        safe_float(cashflow[i].get('depreciationDepletionAndAmortization'))
                        for i, r in enumerate(income)], years, 'dollars'),
            'ytd_value': get_ytd('income', 'depreciationAndAmortization') or get_ytd('cashflow', 'depreciationDepletionAndAmortization'),
            'description': 'Depreciation & Amortization'
        },
        'capex': {
            **add_stats([safe_float(r.get('capitalExpenditures')) for r in cashflow], years, 'dollars'),
            'ytd_value': get_ytd('cashflow', 'capitalExpenditures'),
            'description': 'Capital Expenditures'
        },
        'total_debt': {
            **add_stats([calc_debt(r) for r in balance], years, 'dollars'),
            'ytd_value': calc_debt(ytd_data['balance']) if ytd_data else None,
            'description': 'Total Debt'
        },
        'working_capital_components': {
            'ar_pct_revenue': {
                **add_stats([pct(safe_float(r.get('currentNetReceivables')), revenue[i])
                            for i, r in enumerate(balance)], years, 'percent'),
                'ytd_value': pct(get_ytd('balance', 'currentNetReceivables'), ytd_revenue) if ytd_revenue else None,
                'description': 'A/R as % of Revenue'
            },
            'inventory_pct_cogs': {
                **add_stats([pct(safe_float(r.get('inventory')), cogs[i])
                            for i, r in enumerate(balance)], years, 'percent'),
                'ytd_value': pct(get_ytd('balance', 'inventory'), ytd_cogs) if ytd_cogs else None,
                'description': 'Inventory as % of COGS'
            },
            'ap_pct_cogs': {
                **add_stats([pct(safe_float(r.get('currentAccountsPayable')), cogs[i])
                            for i, r in enumerate(balance)], years, 'percent'),
                'ytd_value': pct(get_ytd('balance', 'currentAccountsPayable'), ytd_cogs) if ytd_cogs else None,
                'description': 'A/P as % of COGS'
            }
        }
    }
    return seeds

def main():
    parser = argparse.ArgumentParser(description="Calculate projection seeds")
    parser.add_argument("ticker", help="Stock ticker symbol")
    args = parser.parse_args()
    
    ticker = args.ticker.upper()
    data_dir = get_data_directory(ticker)
    raw_path = os.path.join(data_dir, f"{ticker}_financial_raw.json")
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw data file not found at {raw_path}. Run fetch_financials.py first.")
        sys.exit(1)
        
    raw_data = load_json(raw_path)
    aligned = extract_annual_reports(raw_data)
    ytd = calculate_ytd_annualized(raw_data)
    
    seeds = calculate_projection_seeds(aligned, ytd)
    
    output = {
        'ticker': ticker,
        'fiscal_years': aligned['years'],
        'ytd_info': {
            'num_quarters': ytd['num_quarters'] if ytd else 0,
            'is_annualized': True if ytd else False
        },
        'projection_seeds': seeds
    }
    
    # Save JSON
    output_path = os.path.join(data_dir, f"{ticker}_seeds.json")
    save_json(output, output_path)
    print(f"✓ Saved seeds to {output_path}")

if __name__ == "__main__":
    main()

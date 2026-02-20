#!/usr/bin/env python3
"""
Financial Metrics Calculator
============================

Calculates 13 priority metrics (undervaluation & risk) and 17 secondary metrics.
Implements the exact math from the original financial statements analysis script.

Metrics Categories:
- Undervaluation (OCF, FCF, NCAV, ROTC, ROE, Op Leverage, etc.)
- Risk (Debt/OCF, Accruals Gap, etc.)
- Operations (Gross/Net Margins, etc.)
- Financial Health (Debt/Assets, Tangible Equity, etc.)

Usage:
    python calc_metrics.py TICKER
"""

import sys
import os
import argparse
import subprocess

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    save_json,
    load_json
)

# Shared math helpers (duplicated from calc_seeds for modularity/independence)
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

# Specific calc_metrics functions
def calculate_priority_metrics(aligned_data, seeds, ytd_data=None):
    years, income, balance, cashflow = aligned_data['years'], aligned_data['income'], aligned_data['balance'], aligned_data['cashflow']
    
    def get_ytd(statement, field):
        return safe_float(ytd_data[statement].get(field)) if ytd_data else None

    revenue = seeds['revenue']['values']
    da = seeds['depreciation_amortization']['values']
    capex = seeds['capex']['values']
    debt = seeds['total_debt']['values']

    ytd_revenue = seeds['revenue'].get('ytd_value')
    ytd_da = seeds['depreciation_amortization'].get('ytd_value')
    ytd_capex = seeds['capex'].get('ytd_value')
    ytd_debt = seeds['total_debt'].get('ytd_value')

    ocf = [safe_float(r.get('operatingCashflow')) for r in cashflow]
    ni = [safe_float(r.get('netIncome')) for r in income]
    oi = [safe_float(r.get('operatingIncome')) for r in income]
    assets = [safe_float(r.get('totalAssets')) for r in balance]
    equity = [safe_float(r.get('totalShareholderEquity')) for r in balance]
    current_assets = [safe_float(r.get('totalCurrentAssets')) for r in balance]
    current_liab = [safe_float(r.get('totalCurrentLiabilities')) for r in balance]
    total_liab = [safe_float(r.get('totalLiabilities')) for r in balance]

    ytd_ocf = get_ytd('cashflow', 'operatingCashflow')
    ytd_ni = get_ytd('income', 'netIncome')
    ytd_oi = get_ytd('income', 'operatingIncome')
    ytd_assets = get_ytd('balance', 'totalAssets')
    ytd_equity = get_ytd('balance', 'totalShareholderEquity')
    ytd_current_assets = get_ytd('balance', 'totalCurrentAssets')
    ytd_current_liab = get_ytd('balance', 'totalCurrentLiabilities')
    ytd_total_liab = get_ytd('balance', 'totalLiabilities')
    ytd_interest = get_ytd('income', 'interestExpense')
    ytd_tax = get_ytd('income', 'incomeTaxExpense')

    return {
        'operating_cashflow': {
            **add_stats(ocf, years, 'dollars', include_cagr=True),
            'ytd_value': ytd_ocf,
            'category': 'undervaluation',
            'description': 'Operating Cash Flow'
        },
        'free_cashflow': {
            **add_stats([o - abs(c) if o and c else None for o, c in zip(ocf, capex)],
                       years, 'dollars', include_cagr=True),
            'ytd_value': ytd_ocf - abs(ytd_capex) if ytd_ocf and ytd_capex else None,
            'category': 'undervaluation',
            'description': 'Free Cash Flow'
        },
        'ncav': {
            **add_stats([ca - tl if ca and tl else None for ca, tl in zip(current_assets, total_liab)],
                       years, 'dollars'),
            'ytd_value': ytd_current_assets - ytd_total_liab if ytd_current_assets and ytd_total_liab else None,
            'category': 'undervaluation',
            'description': 'Net Current Asset Value'
        },
        'rotc': {
            **add_stats([pct((n or 0) + (safe_float(income[i].get('interestExpense', 0)) or 0) +
                            (safe_float(income[i].get('incomeTaxExpense', 0)) or 0),
                            (equity[i] or 0) + (debt[i] or 0)) if n is not None else None
                        for i, n in enumerate(ni)], years, 'percent'),
            'ytd_value': pct((ytd_ni or 0) + (ytd_interest or 0) + (ytd_tax or 0),
                            (ytd_equity or 0) + (ytd_debt or 0)) if ytd_ni is not None and ytd_equity and ytd_debt else None,
            'category': 'undervaluation',
            'description': 'Return on Total Capital'
        },
        'roe': {
            **add_stats([pct(n, equity[i]) for i, n in enumerate(ni)], years, 'percent'),
            'ytd_value': pct(ytd_ni, ytd_equity),
            'category': 'undervaluation',
            'description': 'Return on Equity'
        },
        'operating_leverage': {
            **add_stats([None] + [round((((oi[i]-oi[i-1])/oi[i-1]*100) / ((revenue[i]-revenue[i-1])/revenue[i-1]*100)), 2)
                                  if all(v is not None and v != 0 for v in [oi[i], oi[i-1], revenue[i], revenue[i-1]]) and
                                     ((revenue[i]-revenue[i-1])/revenue[i-1]*100) != 0 else None
                                  for i in range(1, len(years))],
                       years, 'ratio'),
            'ytd_value': None,
            'category': 'undervaluation',
            'description': 'Operating Leverage'
        },
        'revenue_trends': {
            **add_stats(revenue, years, 'dollars', include_cagr=True),
            'ytd_value': ytd_revenue,
            'category': 'undervaluation',
            'description': 'Revenue (trend analysis)'
        },
        'operating_margin': {
            **add_stats([pct(o, revenue[i]) for i, o in enumerate(oi)], years, 'percent'),
            'ytd_value': pct(ytd_oi, ytd_revenue),
            'category': 'undervaluation',
            'description': 'Operating Margin'
        },
        'debt_to_ocf': {
            **add_stats([round(d/o, 2) if d and o and o > 0 else None for d, o in zip(debt, ocf)],
                       years, 'years'),
            'ytd_value': round(ytd_debt/ytd_ocf, 2) if ytd_debt and ytd_ocf and ytd_ocf > 0 else None,
            'category': 'risk',
            'description': 'Debt / OCF (years to repay)'
        },
        'ocf_to_ni': {
            **add_stats([round(o/n, 2) if o and n and n != 0 else None for o, n in zip(ocf, ni)],
                       years, 'ratio'),
            'ytd_value': round(ytd_ocf/ytd_ni, 2) if ytd_ocf and ytd_ni and ytd_ni != 0 else None,
            'category': 'risk',
            'description': 'OCF / Net Income'
        },
        'accruals_gap': {
            **add_stats([pct(n - o, assets[i]) for i, (n, o) in enumerate(zip(ni, ocf))],
                       years, 'percent'),
            'ytd_value': pct(ytd_ni - ytd_ocf, ytd_assets) if ytd_ni and ytd_ocf and ytd_assets else None,
            'category': 'risk',
            'description': 'Accruals Gap (% of assets)'
        },
        'depreciation_amortization_risk': {
            **add_stats(da, years, 'dollars'),
            'ytd_value': ytd_da,
            'category': 'risk',
            'description': 'D&A (for peer comparison)'
        },
        'working_capital': {
            **add_stats([ca - cl if ca and cl else None for ca, cl in zip(current_assets, current_liab)],
                       years, 'dollars', include_cagr=True),
            'ytd_value': ytd_current_assets - ytd_current_liab if ytd_current_assets and ytd_current_liab else None,
            'category': 'risk',
            'description': 'Working Capital (trend analysis)'
        }
    }

def calculate_secondary_metrics(aligned_data, seeds, priority_metrics):
    years, income, balance, cashflow = aligned_data['years'], aligned_data['income'], aligned_data['balance'], aligned_data['cashflow']
    revenue = seeds['revenue']['values']
    da = seeds['depreciation_amortization']['values']
    ocf = priority_metrics['operating_cashflow']['values']
    ni = [safe_float(r.get('netIncome')) for r in income]
    assets = [safe_float(r.get('totalAssets')) for r in balance]
    equity = [safe_float(r.get('totalShareholderEquity')) for r in balance]
    debt = seeds['total_debt']['values']

    inv = [safe_float(r.get('inventory')) for r in balance]
    cash = [safe_float(r.get('cashAndCashEquivalentsAtCarryingValue')) for r in balance]
    total_liab = [safe_float(r.get('totalLiabilities')) for r in balance]
    cogs = [safe_float(r.get('costOfRevenue')) for r in income]
    ar = [safe_float(r.get('currentNetReceivables')) for r in balance]
    capex = seeds['capex']['values']
    current_assets = [safe_float(r.get('totalCurrentAssets')) for r in balance]
    current_liab = [safe_float(r.get('totalCurrentLiabilities')) for r in balance]

    # Helper for growth comparisons
    def growth_diff(val1, val2):
        result = [None]
        for i in range(1, len(years)):
            if all(v is not None and v != 0 for v in [val1[i], val1[i-1], val2[i], val2[i-1]]):
                g1 = ((val1[i] - val1[i-1]) / val1[i-1]) * 100
                g2 = ((val2[i] - val2[i-1]) / val2[i-1]) * 100
                result.append(round(g1 - g2, 2))
            else:
                result.append(None)
        return result

    return {
        # Operations (4)
        'gross_margin': {
            **add_stats([pct(safe_float(r.get('grossProfit')), revenue[i]) for i, r in enumerate(income)],
                       years, 'percent'),
            'category': 'operations', 'description': 'Gross Margin'
        },
        'net_margin': {
            **add_stats([pct(n, revenue[i]) for i, n in enumerate(ni)], years, 'percent'),
            'category': 'operations', 'description': 'Net Margin'
        },
        'da_pct_revenue': {
            **add_stats([pct(d, revenue[i]) for i, d in enumerate(da)], years, 'percent'),
            'category': 'operations', 'description': 'D&A % of Revenue'
        },
        'da_pct_ocf': {
            **add_stats([pct(d, ocf[i]) for i, d in enumerate(da)], years, 'percent'),
            'category': 'operations', 'description': 'D&A % of OCF'
        },

        # Financial Health (8)
        'debt_to_assets': {
            **add_stats([pct(d, assets[i]) for i, d in enumerate(debt)], years, 'percent'),
            'category': 'financial_health', 'description': 'Debt / Total Assets'
        },
        'tangible_equity_to_assets': {
            **add_stats([pct(equity[i] - (safe_float(balance[i].get('goodwill', 0)) or 0) -
                            (safe_float(balance[i].get('intangibleAssets', 0)) or 0), assets[i])
                        for i in range(len(years))], years, 'percent'),
            'category': 'financial_health', 'description': 'Tangible Equity / Assets'
        },
        'current_ratio': {
            **add_stats([round(ca/cl, 2) if cl and cl > 0 else None
                        for ca, cl in zip(current_assets, current_liab)], years, 'ratio'),
            'category': 'financial_health', 'description': 'Current Ratio'
        },
        'quick_ratio': {
            **add_stats([round((ca-(inv[i] or 0))/cl, 2) if cl and cl > 0 else None
                        for i, (ca, cl) in enumerate(zip(current_assets, current_liab))], years, 'ratio'),
            'category': 'financial_health', 'description': 'Quick Ratio'
        },
        'ebit_coverage': {
            **add_stats([round((safe_float(r.get('ebit')) or safe_float(r.get('operatingIncome'))) /
                              (safe_float(r.get('interestExpense')) or 1), 2)
                        if safe_float(r.get('interestExpense')) and safe_float(r.get('interestExpense')) > 0 else None
                        for r in income], years, 'ratio'),
            'category': 'financial_health', 'description': 'EBIT Coverage'
        },
        'debt_to_tangible_equity': {
            **add_stats([pct(debt[i], equity[i] - (safe_float(balance[i].get('goodwill', 0)) or 0) -
                            (safe_float(balance[i].get('intangibleAssets', 0)) or 0))
                        for i in range(len(years))], years, 'percent'),
            'category': 'financial_health', 'description': 'Debt to Tangible Equity'
        },
        'std_pct_current_liabilities': {
            **add_stats([pct(safe_float(r.get('shortTermDebt', 0)) or 0, current_liab[i])
                        for i, r in enumerate(balance)], years, 'percent'),
            'category': 'financial_health', 'description': 'Short-Term Debt % of Current Liab'
        },
        'cash_pct_assets': {
            **add_stats([pct(c, assets[i]) for i, c in enumerate(cash)], years, 'percent'),
            'category': 'financial_health', 'description': 'Cash % of Assets'
        },

        # Efficiency (5)
        'receivables_vs_revenue_growth': {
            **add_stats(growth_diff(ar, revenue), years, 'percent'),
            'category': 'efficiency', 'description': 'Receivables Growth - Revenue Growth'
        },
        'dso': {
            **add_stats([round((a/r)*365, 2) if r and r > 0 else None
                        for a, r in zip(ar, revenue)], years, 'days'),
            'category': 'efficiency', 'description': 'Days Sales Outstanding'
        },
        'inventory_vs_cogs_growth': {
            **add_stats(growth_diff(inv, cogs), years, 'percent'),
            'category': 'efficiency', 'description': 'Inventory Growth - COGS Growth'
        },
        'inventory_turnover': {
            **add_stats([round(c/i, 2) if i and i > 0 else None
                        for c, i in zip(cogs, inv)], years, 'ratio'),
            'category': 'efficiency', 'description': 'Inventory Turnover'
        },
        'capex_to_depreciation': {
            **add_stats([round(abs(c)/d, 2) if d and d > 0 else None
                        for c, d in zip(capex, da)], years, 'ratio'),
            'category': 'efficiency', 'description': 'Capex / Depreciation'
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Calculate financial metrics")
    parser.add_argument("ticker", help="Stock ticker symbol")
    args = parser.parse_args()
    
    ticker = args.ticker.upper()
    data_dir = get_data_directory(ticker)
    raw_path = os.path.join(data_dir, f"{ticker}_financial_raw.json")
    seeds_path = os.path.join(data_dir, f"{ticker}_seeds.json")
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw data file not found at {raw_path}.")
        sys.exit(1)
        
    if not os.path.exists(seeds_path):
        print(f"🔄 Missing seeds, running calc_seeds.py...")
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "calc_seeds.py"), ticker], check=True)
        
    raw_data = load_json(raw_path)
    seeds_data = load_json(seeds_path)

    # Import logic for alignment and YTD (duplicated or move to shared_utils if frequent)
    from calc_seeds import extract_annual_reports, calculate_ytd_annualized

    aligned = extract_annual_reports(raw_data)
    ytd = calculate_ytd_annualized(raw_data)

    # Extract projection_seeds from the full seeds file structure
    seeds = seeds_data.get('projection_seeds', {})

    priority = calculate_priority_metrics(aligned, seeds, ytd)
    secondary = calculate_secondary_metrics(aligned, seeds, priority)
    
    output = {
        'priority': priority,
        'secondary': secondary
    }
    
    output_path = os.path.join(data_dir, f"{ticker}_metrics.json")
    save_json(output, output_path)
    print(f"✓ Saved metrics to {output_path}")

if __name__ == "__main__":
    main()

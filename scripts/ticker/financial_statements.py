#!/usr/bin/env python3
"""
Financial Statement Data Preparation Script
===========================================

Fetches financial statement data from AlphaVantage API and calculates:
- 8 Projection Seeds (baseline analysis)
- 13 Priority Metrics (8 undervaluation + 5 risk)
- 17 Secondary Metrics (operations, financial health, efficiency context)

Outputs:
- {TICKER}_financial_data.json - Complete metrics with statistics
- {TICKER}_statement_data.md - Comparison table (target + 2 peers)
- Updates {TICKER}_tracking.md

Usage:
    python SCRIPT_statements.py TICKER PEER1 PEER2
    python SCRIPT_statements.py IBM MSFT AAPL
"""

import sys
import os
import json
import time
from datetime import datetime
from shared_utils import (
    fetch_alpha_vantage,
    get_data_directory,
    ensure_directory_exists,
    save_json,
    load_json
)

# ============================================================================
# CONFIGURATION
# ============================================================================

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY', 'demo')
YEARS_TO_ANALYZE = 5

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def safe_float(value, default=None):
    """Convert value to float, return default if None or 'None' string"""
    if value is None or value == 'None' or value == '':
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def safe_divide(num, denom, default=None):
    """Safely divide, return default if denom is 0 or None"""
    if num is None or denom is None or denom == 0:
        return default
    return num / denom

def pct(num, denom, default=None):
    """Calculate percentage: (num / denom) × 100"""
    result = safe_divide(num, denom, default)
    return round(result * 100, 2) if result is not None else default

def calculate_cagr(values):
    """Calculate Compound Annual Growth Rate"""
    clean = [v for v in values if v is not None]
    if len(clean) < 2 or clean[0] <= 0 or clean[-1] <= 0:
        return None
    years = len(clean) - 1
    return round((((clean[-1] / clean[0]) ** (1 / years)) - 1) * 100, 2)

def calculate_avg(values):
    """Average of non-None values"""
    clean = [v for v in values if v is not None]
    return round(sum(clean) / len(clean), 2) if clean else None

def calculate_5yr_avg(values):
    """5-year average (all values in dataset)"""
    return calculate_avg(values)

def calculate_cv(values):
    """Coefficient of variation (volatility measure)"""
    clean = [v for v in values if v is not None]
    if len(clean) < 2:
        return None
    avg = sum(clean) / len(clean)
    if avg == 0:
        return None
    variance = sum((x - avg) ** 2 for x in clean) / len(clean)
    return round((variance ** 0.5 / abs(avg)) * 100, 2)

def detect_outliers(values):
    """Detect outliers using 2 standard deviations from mean"""
    clean = [(i, v) for i, v in enumerate(values) if v is not None]
    if len(clean) < 3:
        return []
    vals = [v for _, v in clean]
    mean = sum(vals) / len(vals)
    variance = sum((x - mean) ** 2 for x in vals) / len(vals)
    std_dev = variance ** 0.5
    lower, upper = mean - 2*std_dev, mean + 2*std_dev
    return [i for i, v in clean if v < lower or v > upper]

def calculate_slope(values):
    """Calculate linear regression slope for trend direction"""
    clean = [(i, v) for i, v in enumerate(values) if v is not None]
    if len(clean) < 2:
        return None
    n = len(clean)
    sum_x = sum(i for i, _ in clean)
    sum_y = sum(v for _, v in clean)
    sum_xy = sum(i * v for i, v in clean)
    sum_x2 = sum(i * i for i, _ in clean)
    denominator = n * sum_x2 - sum_x * sum_x
    if denominator == 0:
        return None
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    return round(slope, 2)

def calculate_recent_delta(values):
    """Calculate YoY change (most recent vs prior year)"""
    clean = [v for v in values if v is not None]
    if len(clean) < 2:
        return {'absolute': None, 'percent': None}
    recent, prior = clean[-1], clean[-2]
    absolute = round(recent - prior, 2)
    percent = round(((recent - prior) / prior * 100), 2) if prior != 0 else None
    return {'absolute': absolute, 'percent': percent}

def add_stats(values, years, unit, include_cagr=False):
    """Add statistics to metric dict per Three-Dimension Analysis Framework"""
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

# ============================================================================
# MARKET DATA STATISTICS
# ============================================================================

def calculate_price_statistics(price_monthly_data):
    """Calculate price statistics from monthly price history

    Args:
        price_monthly_data: Raw TIME_SERIES_MONTHLY API response

    Returns:
        dict with price statistics, or None if insufficient data
    """
    if not price_monthly_data:
        return None

    time_series = price_monthly_data.get('Monthly Time Series', {})
    if not time_series:
        return None

    # Extract and sort monthly closes (newest first in API)
    monthly_data = []
    for date_str, values in time_series.items():
        close = safe_float(values.get('4. close'))
        if close is not None:
            monthly_data.append((date_str, close))

    # Sort by date descending (most recent first)
    monthly_data.sort(key=lambda x: x[0], reverse=True)

    if len(monthly_data) < 2:
        return None

    # Get up to 60 months (5 years)
    monthly_data = monthly_data[:60]
    closes = [close for _, close in monthly_data]

    current = closes[0]

    # Calculate vs 3mo delta (current vs 3 months ago)
    vs_3mo_pct = None
    if len(closes) > 3 and closes[3] != 0:
        vs_3mo_pct = round(((current - closes[3]) / closes[3]) * 100, 2)

    # Calculate vs YoY delta (current vs 12 months ago)
    vs_yoy_pct = None
    if len(closes) > 12 and closes[12] != 0:
        vs_yoy_pct = round(((current - closes[12]) / closes[12]) * 100, 2)

    # For CAGR and other stats, reverse to oldest-first (matches existing helper expectations)
    closes_chronological = list(reversed(closes))

    return {
        'current': current,
        'mean_5yr': calculate_5yr_avg(closes_chronological),
        'cagr_5yr': calculate_cagr(closes_chronological),
        'cv': calculate_cv(closes_chronological),
        'vs_3mo_pct': vs_3mo_pct,
        'vs_yoy_pct': vs_yoy_pct,
        'months_of_data': len(closes)
    }

def calculate_earnings_statistics(earnings_data):
    """Calculate earnings/EPS statistics from earnings history

    Args:
        earnings_data: Raw EARNINGS API response

    Returns:
        dict with earnings statistics, or None if insufficient data
    """
    if not earnings_data:
        return None

    quarterly = earnings_data.get('quarterlyEarnings', [])
    annual = earnings_data.get('annualEarnings', [])

    if not quarterly or len(quarterly) < 2:
        return None

    # Get latest quarterly EPS
    latest_eps = safe_float(quarterly[0].get('reportedEPS'))
    if latest_eps is None:
        return None

    # vs 3mo (prior quarter)
    vs_3mo_pct = None
    if len(quarterly) > 1:
        prior_eps = safe_float(quarterly[1].get('reportedEPS'))
        if prior_eps is not None and prior_eps != 0:
            vs_3mo_pct = round(((latest_eps - prior_eps) / abs(prior_eps)) * 100, 2)

    # vs YoY (same quarter last year - 4 quarters ago)
    vs_yoy_pct = None
    if len(quarterly) > 4:
        yoy_eps = safe_float(quarterly[4].get('reportedEPS'))
        if yoy_eps is not None and yoy_eps != 0:
            vs_yoy_pct = round(((latest_eps - yoy_eps) / abs(yoy_eps)) * 100, 2)

    # 5yr mean and CAGR from annual data
    mean_5yr = None
    cagr_5yr = None
    cv = None
    years_of_data = 0

    if annual:
        # Get up to 5 years of annual EPS
        annual_eps = []
        for entry in annual[:5]:
            eps = safe_float(entry.get('reportedEPS'))
            if eps is not None:
                annual_eps.append(eps)

        years_of_data = len(annual_eps)
        if annual_eps:
            # Reverse to chronological order (oldest first)
            annual_eps_chrono = list(reversed(annual_eps))
            mean_5yr = calculate_5yr_avg(annual_eps_chrono)
            cagr_5yr = calculate_cagr(annual_eps_chrono)
            cv = calculate_cv(annual_eps_chrono)

    return {
        'latest': latest_eps,
        'mean_5yr': mean_5yr,
        'cagr_5yr': cagr_5yr,
        'cv': cv,
        'vs_3mo_pct': vs_3mo_pct,
        'vs_yoy_pct': vs_yoy_pct,
        'years_of_data': years_of_data
    }

def calculate_trailing_pe(price_statistics, earnings_data):
    """Calculate trailing 12-month P/E ratio

    Args:
        price_statistics: Output from calculate_price_statistics()
        earnings_data: Raw EARNINGS API response

    Returns:
        float: Trailing P/E ratio, or None if insufficient data
    """
    if not price_statistics or not earnings_data:
        return None

    current_price = price_statistics.get('current')
    if not current_price:
        return None

    # Calculate TTM EPS (sum of last 4 quarters)
    quarterly = earnings_data.get('quarterlyEarnings', [])
    if len(quarterly) < 4:
        return None

    ttm_eps = 0
    for q in quarterly[:4]:
        eps = safe_float(q.get('reportedEPS'))
        if eps is None:
            return None
        ttm_eps += eps

    if ttm_eps <= 0:
        return None  # Negative or zero earnings - P/E not meaningful

    return round(current_price / ttm_eps, 2)

def calculate_pe_comparison(target_data, peer1_data, peer2_data):
    """Calculate P/E comparison between target and peers

    Args:
        target_data: dict with 'price_statistics' and 'earnings' for target
        peer1_data: dict with 'price_statistics' and 'earnings' for peer1
        peer2_data: dict with 'price_statistics' and 'earnings' for peer2

    Returns:
        dict with P/E comparison data
    """
    target_pe = calculate_trailing_pe(
        target_data.get('price_statistics'),
        target_data.get('earnings')
    )

    peer1_pe = calculate_trailing_pe(
        peer1_data.get('price_statistics'),
        peer1_data.get('earnings')
    ) if peer1_data else None

    peer2_pe = calculate_trailing_pe(
        peer2_data.get('price_statistics'),
        peer2_data.get('earnings')
    ) if peer2_data else None

    # Calculate peer average (only include valid P/Es)
    peer_pes = [p for p in [peer1_pe, peer2_pe] if p is not None]
    peer_avg_pe = round(sum(peer_pes) / len(peer_pes), 2) if peer_pes else None

    # Calculate vs peer avg
    vs_peer_avg_pct = None
    if target_pe and peer_avg_pe:
        vs_peer_avg_pct = round(((target_pe - peer_avg_pe) / peer_avg_pe) * 100, 2)

    return {
        'target_pe': target_pe,
        'peer1_pe': peer1_pe,
        'peer2_pe': peer2_pe,
        'peer_avg_pe': peer_avg_pe,
        'vs_peer_avg_pct': vs_peer_avg_pct
    }

# ============================================================================
# DATA FETCHING & EXTRACTION
# ============================================================================

def fetch_statement_data(ticker, target_ticker=None):
    """Fetch all financial statement data (with caching)"""
    print(f"\n{'='*60}\nFetching data for {ticker}\n{'='*60}")

    data_dir = get_data_directory(ticker, target_ticker)
    ensure_directory_exists(data_dir)

    endpoints = {
        'income': 'INCOME_STATEMENT',
        'balance': 'BALANCE_SHEET',
        'cashflow': 'CASH_FLOW',
        'overview': 'OVERVIEW'
    }

    data = {}
    for key, function in endpoints.items():
        cache_file = os.path.join(data_dir, f"{ticker}_{key}.json")

        if os.path.exists(cache_file):
            print(f"  ✓ Loading {key} from cache...")
            data[key] = load_json(cache_file)
        else:
            print(f"  → Fetching {key} from API...")
            url = f"https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={API_KEY}"
            api_data = fetch_alpha_vantage(url)

            if api_data:
                data[key] = api_data
                save_json(api_data, cache_file)
                print(f"  ✓ Saved to cache")
                time.sleep(12)  # Rate limiting
            else:
                print(f"  ✗ Failed to fetch {key}")
                return None

    return data

def fetch_market_data(ticker, target_ticker=None):
    """Fetch market data: shares outstanding, earnings, price history (with caching)"""
    data_dir = get_data_directory(ticker, target_ticker)

    # Define endpoints to fetch
    # Only fetch shares_outstanding for target (needed for projections)
    # Peers only need earnings and price for P/E comparison
    is_target = (target_ticker is None)
    endpoints = {
        'earnings': 'EARNINGS',
        'price_monthly': 'TIME_SERIES_MONTHLY'
    }
    if is_target:
        endpoints['shares'] = 'SHARES_OUTSTANDING'

    market_data = {}
    for key, function in endpoints.items():
        cache_file = os.path.join(data_dir, f"{ticker}_{key}.json")

        if os.path.exists(cache_file):
            print(f"  ✓ Loading {key} from cache...")
            market_data[key] = load_json(cache_file)
        else:
            print(f"  → Fetching {key} from API...")
            url = f"https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={API_KEY}"
            api_data = fetch_alpha_vantage(url)

            if api_data:
                market_data[key] = api_data
                save_json(api_data, cache_file)
                print(f"  ✓ Saved to cache")
                time.sleep(12)  # Rate limiting
            else:
                print(f"  ✗ Failed to fetch {key}")
                market_data[key] = None

    return market_data

def extract_annual_reports(data, years=YEARS_TO_ANALYZE):
    """Extract and align annual reports by fiscal year"""
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
    """Calculate YTD annualized values from quarterly data for 2025"""
    current_year = '2025'

    # Get all 2025 quarterly reports
    income_qtrs = [r for r in data.get('income', {}).get('quarterlyReports', [])
                   if r.get('fiscalDateEnding', '').startswith(current_year)]
    balance_qtrs = [r for r in data.get('balance', {}).get('quarterlyReports', [])
                    if r.get('fiscalDateEnding', '').startswith(current_year)]
    cashflow_qtrs = [r for r in data.get('cashflow', {}).get('quarterlyReports', [])
                     if r.get('fiscalDateEnding', '').startswith(current_year)]

    if not income_qtrs:
        return None  # No YTD data available

    num_quarters = len(income_qtrs)
    annualization_factor = 4 / num_quarters

    # Sum YTD for flow items, use latest for stock items
    def sum_and_annualize(reports, field):
        values = [safe_float(r.get(field, 0)) or 0 for r in reports]
        total = sum(values) if values else None
        return total * annualization_factor if total is not None else None

    def latest_qtr(reports, field):
        return safe_float(reports[0].get(field)) if reports else None

    # Income statement (flows - annualized)
    ytd_income = {
        'totalRevenue': sum_and_annualize(income_qtrs, 'totalRevenue'),
        'costOfRevenue': sum_and_annualize(income_qtrs, 'costOfRevenue'),
        'sellingGeneralAndAdministrative': sum_and_annualize(income_qtrs, 'sellingGeneralAndAdministrative'),
        'researchAndDevelopment': sum_and_annualize(income_qtrs, 'researchAndDevelopment'),
        'operatingIncome': sum_and_annualize(income_qtrs, 'operatingIncome'),
        'netIncome': sum_and_annualize(income_qtrs, 'netIncome'),
        'interestExpense': sum_and_annualize(income_qtrs, 'interestExpense'),
        'incomeTaxExpense': sum_and_annualize(income_qtrs, 'incomeTaxExpense'),
        'depreciationAndAmortization': sum_and_annualize(income_qtrs, 'depreciationAndAmortization')
    }

    # Balance sheet (stocks - most recent quarter, not annualized)
    ytd_balance = {
        'totalAssets': latest_qtr(balance_qtrs, 'totalAssets'),
        'totalCurrentAssets': latest_qtr(balance_qtrs, 'totalCurrentAssets'),
        'totalCurrentLiabilities': latest_qtr(balance_qtrs, 'totalCurrentLiabilities'),
        'totalLiabilities': latest_qtr(balance_qtrs, 'totalLiabilities'),
        'totalShareholderEquity': latest_qtr(balance_qtrs, 'totalShareholderEquity'),
        'currentNetReceivables': latest_qtr(balance_qtrs, 'currentNetReceivables'),
        'inventory': latest_qtr(balance_qtrs, 'inventory'),
        'currentAccountsPayable': latest_qtr(balance_qtrs, 'currentAccountsPayable'),
        'shortTermDebt': latest_qtr(balance_qtrs, 'shortTermDebt'),
        'currentLongTermDebt': latest_qtr(balance_qtrs, 'currentLongTermDebt'),
        'longTermDebt': latest_qtr(balance_qtrs, 'longTermDebt')
    }

    # Cash flow (flows - annualized)
    ytd_cashflow = {
        'operatingCashflow': sum_and_annualize(cashflow_qtrs, 'operatingCashflow'),
        'capitalExpenditures': sum_and_annualize(cashflow_qtrs, 'capitalExpenditures'),
        'depreciationDepletionAndAmortization': sum_and_annualize(cashflow_qtrs, 'depreciationDepletionAndAmortization')
    }

    return {
        'num_quarters': num_quarters,
        'annualization_factor': annualization_factor,
        'income': ytd_income,
        'balance': ytd_balance,
        'cashflow': ytd_cashflow
    }

# ============================================================================
# METRIC CALCULATIONS
# ============================================================================

def calculate_projection_seeds(aligned_data, ytd_data=None):
    """Calculate 8 projection seeds"""
    years, income, balance, cashflow = aligned_data['years'], aligned_data['income'], aligned_data['balance'], aligned_data['cashflow']

    # Helper to extract YTD values
    def get_ytd(statement, field):
        return safe_float(ytd_data[statement].get(field)) if ytd_data else None

    # Helper to calculate total debt
    def calc_debt(report):
        return sum(safe_float(report.get(k, 0)) or 0 for k in
                   ['shortTermDebt', 'currentLongTermDebt', 'longTermDebt']) or None

    # Extract base values
    revenue = [safe_float(r.get('totalRevenue')) for r in income]
    cogs = [safe_float(r.get('costOfRevenue')) for r in income]

    # YTD values
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

def calculate_priority_metrics(aligned_data, seeds, ytd_data=None):
    """Calculate 13 priority metrics"""
    years, income, balance, cashflow = aligned_data['years'], aligned_data['income'], aligned_data['balance'], aligned_data['cashflow']

    # Helper to extract YTD values
    def get_ytd(statement, field):
        return safe_float(ytd_data[statement].get(field)) if ytd_data else None

    revenue = seeds['revenue']['values']
    da = seeds['depreciation_amortization']['values']
    capex = seeds['capex']['values']
    debt = seeds['total_debt']['values']

    # YTD values from seeds
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

    # YTD values
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

    # Helper for YoY calculations
    def calc_yoy(values, calc_fn):
        result = [None]
        for i in range(1, len(years)):
            if values[i] is not None and values[i-1] is not None and values[i-1] != 0:
                result.append(calc_fn(values[i], values[i-1]))
            else:
                result.append(None)
        return result

    return {
        # Undervaluation (8)
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
            'ytd_value': None,  # Operating leverage requires YoY comparison, not applicable for YTD
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

        # Risk (5)
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
    """Calculate 17 secondary metrics"""
    years, income, balance, cashflow = aligned_data['years'], aligned_data['income'], aligned_data['balance'], aligned_data['cashflow']

    revenue = seeds['revenue']['values']
    da = seeds['depreciation_amortization']['values']
    capex = seeds['capex']['values']
    debt = seeds['total_debt']['values']
    ocf = priority_metrics['operating_cashflow']['values']

    ni = [safe_float(r.get('netIncome')) for r in income]
    cogs = [safe_float(r.get('costOfRevenue')) for r in income]
    assets = [safe_float(r.get('totalAssets')) for r in balance]
    equity = [safe_float(r.get('totalShareholderEquity')) for r in balance]
    current_assets = [safe_float(r.get('totalCurrentAssets')) for r in balance]
    current_liab = [safe_float(r.get('totalCurrentLiabilities')) for r in balance]
    ar = [safe_float(r.get('currentNetReceivables')) for r in balance]
    inv = [safe_float(r.get('inventory')) for r in balance]
    cash = [safe_float(r.get('cashAndCashEquivalentsAtCarryingValue')) for r in balance]

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

def extract_projection_assumptions(aligned_data, overview_data, shares_data):
    """Extract projection assumptions from most recent year

    Args:
        aligned_data: Aligned financial statement data
        overview_data: Overview API response (unused, kept for compatibility)
        shares_data: SHARES_OUTSTANDING API response

    Returns:
        dict: {
            'shares_outstanding': float (diluted),
            'total_assets': float,
            'equity': float,
            'embedded_interest_rate': float,
            'effective_tax_rate': float
        }
    """
    income, balance = aligned_data['income'], aligned_data['balance']

    # Get most recent year (last in arrays)
    most_recent_income = income[-1]
    most_recent_balance = balance[-1]

    # Extract diluted shares from SHARES_OUTSTANDING API
    shares_outstanding = None
    if shares_data and 'data' in shares_data and shares_data['data']:
        most_recent_fiscal = most_recent_balance.get('fiscalDateEnding')

        # Find matching date in shares data
        for entry in shares_data['data']:
            if entry.get('date') == most_recent_fiscal:
                shares_outstanding = safe_float(entry.get('shares_outstanding_diluted'))
                break

        # If no exact match, use most recent
        if shares_outstanding is None:
            shares_outstanding = safe_float(shares_data['data'][0].get('shares_outstanding_diluted'))

    total_assets = safe_float(most_recent_balance.get('totalAssets'))
    equity = safe_float(most_recent_balance.get('totalShareholderEquity'))

    # Calculate embedded interest rate (most recent year)
    interest_expense = safe_float(most_recent_income.get('interestExpense'))
    total_debt = sum(safe_float(most_recent_balance.get(k, 0)) or 0 for k in
                     ['shortTermDebt', 'currentLongTermDebt', 'longTermDebt']) or None
    embedded_interest_rate = safe_divide(interest_expense, total_debt)

    # Calculate effective tax rate (most recent year)
    tax_expense = safe_float(most_recent_income.get('incomeTaxExpense'))
    income_before_tax = safe_float(most_recent_income.get('incomeBeforeTax'))
    effective_tax_rate = safe_divide(tax_expense, income_before_tax)

    return {
        'shares_outstanding': shares_outstanding,
        'total_assets': total_assets,
        'equity': equity,
        'embedded_interest_rate': embedded_interest_rate,
        'effective_tax_rate': effective_tax_rate
    }

# ============================================================================
# OUTPUT GENERATION
# ============================================================================

def generate_financial_data_json(ticker, years, seeds, priority_metrics, secondary_metrics, projection_assumptions, market_data, output_path, ytd_data=None):
    """Generate {TICKER}_financial_data.json"""
    output = {
        'ticker': ticker,
        'data_date': datetime.now().strftime('%Y-%m-%d'),
        'fiscal_years': years,
        'ytd_info': {
            'has_ytd': ytd_data is not None,
            'num_quarters': ytd_data['num_quarters'] if ytd_data else None,
            'annualization_factor': ytd_data['annualization_factor'] if ytd_data else None
        } if ytd_data else {'has_ytd': False},
        'projection_assumptions': projection_assumptions,
        'projection_seeds': seeds,
        'market_data': market_data,
        'priority_metrics': {
            'undervaluation': {k: v for k, v in priority_metrics.items() if v.get('category') == 'undervaluation'},
            'risk': {k: v for k, v in priority_metrics.items() if v.get('category') == 'risk'}
        },
        'secondary_metrics': {
            'operations': {k: v for k, v in secondary_metrics.items() if v.get('category') == 'operations'},
            'financial_health': {k: v for k, v in secondary_metrics.items() if v.get('category') == 'financial_health'},
            'efficiency': {k: v for k, v in secondary_metrics.items() if v.get('category') == 'efficiency'}
        }
    }

    save_json(output, output_path)
    print(f"✓ Generated: {output_path}")

def generate_comparison_table(target_ticker, peer1_ticker, peer2_ticker, output_path):
    """Generate {TICKER}_statement_data.md with comparison table"""

    # Load data
    target_data = load_json(os.path.join(target_ticker, f"{target_ticker}_financial_data.json"))
    peer1_data = load_json(os.path.join(target_ticker, peer1_ticker, f"{peer1_ticker}_financial_data.json"))
    peer2_data = load_json(os.path.join(target_ticker, peer2_ticker, f"{peer2_ticker}_financial_data.json"))

    if not all([target_data, peer1_data, peer2_data]):
        print("✗ Error: Missing financial data for comparison")
        return

    years = target_data['fiscal_years']

    # Format helper
    def fmt(val, unit, is_delta=False):
        if val is None:
            return "—"
        prefix = "+" if is_delta and val > 0 else ""
        formats = {
            'dollars': f"{prefix}${val:,.0f}",
            'percent': f"{prefix}{val:.1f}%",
            'ratio': f"{prefix}{val:.2f}",
            'years': f"{prefix}{val:.2f}",
            'days': f"{prefix}{val:.0f}"
        }
        return formats.get(unit, str(val))

    # Get metric data helper
    def get_metric(data, section, key):
        if section == 'seeds':
            return data['projection_seeds'].get(key, {})
        for subsection in data.get(section, {}).values():
            if key in subsection:
                return subsection[key]
        return {}

    # Build metric table with inline deltas
    def metric_table(metric_name, target_key, section, unit):
        t_metric = get_metric(target_data, section, target_key)
        p1_metric = get_metric(peer1_data, section, target_key)
        p2_metric = get_metric(peer2_data, section, target_key)

        t_vals = t_metric.get('values', [])
        p1_vals = p1_metric.get('values', [])
        p2_vals = p2_metric.get('values', [])

        # Check for YTD data
        t_ytd = t_metric.get('ytd_value')
        p1_ytd = p1_metric.get('ytd_value')
        p2_ytd = p2_metric.get('ytd_value')
        has_ytd = any([t_ytd is not None, p1_ytd is not None, p2_ytd is not None])

        # Get YTD quarters info
        ytd_qtrs = target_data.get('ytd_info', {}).get('num_quarters')

        md = f"#### {metric_name}\n\n"

        # Build header with years and Δ% columns interleaved, plus YTD column if available
        header_cols = [years[0]]
        for i in range(1, len(years)):
            header_cols.extend(["Δ%", years[i]])
        if has_ytd:
            header_cols.extend(["Δ%*", f"2025 YTD*"])

        md += "| Ticker | " + " | ".join(header_cols) + " |\n"
        md += "|--------|" + "|".join(["------" for _ in header_cols]) + "|\n"

        # Helper to build row with inline deltas
        def build_row(ticker_name, vals, ytd_val):
            row_cells = [fmt(vals[0] if len(vals) > 0 else None, unit)]
            for i in range(1, len(years)):
                # Calculate delta
                if i < len(vals) and vals[i] is not None and vals[i-1] is not None and vals[i-1] != 0:
                    delta_pct = ((vals[i] - vals[i-1]) / vals[i-1]) * 100
                    delta_str = fmt(delta_pct, 'percent', is_delta=True)
                else:
                    delta_str = "—"
                # Add delta, then value
                row_cells.extend([delta_str, fmt(vals[i] if i < len(vals) else None, unit)])

            # Add YTD column if present
            if has_ytd:
                # Calculate YTD delta vs most recent year
                if ytd_val is not None and len(vals) > 0 and vals[-1] is not None and vals[-1] != 0:
                    ytd_delta_pct = ((ytd_val - vals[-1]) / vals[-1]) * 100
                    ytd_delta_str = fmt(ytd_delta_pct, 'percent', is_delta=True)
                else:
                    ytd_delta_str = "—"
                row_cells.extend([ytd_delta_str, fmt(ytd_val, unit)])

            return f"| {ticker_name} | " + " | ".join(row_cells) + " |\n"

        # Add rows for each ticker
        md += build_row(target_ticker, t_vals, t_ytd)
        md += build_row(peer1_ticker, p1_vals, p1_ytd)
        md += build_row(peer2_ticker, p2_vals, p2_ytd)

        # Add footnote if YTD data present
        if has_ytd:
            md += f"\n*YTD through Q{ytd_qtrs} 2025, annualized. Δ%* shows change vs. 2024 full year. Not included in 5-yr statistics below.*\n"
        md += "\n"

        # Statistics summary table
        md += f"**Statistical Summary:**\n\n"
        md += "| Ticker | Current | 5-Yr Avg | CAGR | Slope | Recent Δ% | CV | Outliers |\n"
        md += "|--------|---------|----------|------|-------|-----------|-----|----------|\n"

        for ticker_name, metric in [(target_ticker, t_metric), (peer1_ticker, p1_metric), (peer2_ticker, p2_metric)]:
            current = fmt(metric.get('current'), unit)
            avg_5yr = fmt(metric.get('avg_5yr'), unit)
            cagr = fmt(metric.get('cagr'), 'percent') if metric.get('cagr') is not None else "—"
            slope = fmt(metric.get('slope'), unit)
            recent_delta = fmt(metric.get('recent_delta', {}).get('percent'), 'percent', is_delta=True) if metric.get('recent_delta', {}).get('percent') is not None else "—"
            cv = fmt(metric.get('cv'), 'percent') if metric.get('cv') is not None else "—"
            outliers = ", ".join(metric.get('outlier_years', [])) if metric.get('outlier_years') else "None"

            md += f"| {ticker_name} | {current} | {avg_5yr} | {cagr} | {slope} | {recent_delta} | {cv} | {outliers} |\n"

        md += "\n---\n\n"
        return md

    # Build working capital components table
    def wc_table():
        md = "#### Working Capital Components\n\n"

        # Check if any ticker has YTD data
        has_ytd_wc = any([
            target_data['projection_seeds'].get('working_capital_components', {}).get(key, {}).get('ytd_value') is not None
            for key in ['ar_pct_revenue', 'inventory_pct_cogs', 'ap_pct_cogs']
        ])
        ytd_qtrs = target_data.get('ytd_info', {}).get('num_quarters')

        for comp_key, comp_name in [('ar_pct_revenue', 'A/R % of Revenue'),
                                      ('inventory_pct_cogs', 'Inventory % of COGS'),
                                      ('ap_pct_cogs', 'A/P % of COGS')]:
            t_comp = target_data['projection_seeds'].get('working_capital_components', {}).get(comp_key, {})
            p1_comp = peer1_data['projection_seeds'].get('working_capital_components', {}).get(comp_key, {})
            p2_comp = peer2_data['projection_seeds'].get('working_capital_components', {}).get(comp_key, {})

            t_vals = t_comp.get('values', [])
            p1_vals = p1_comp.get('values', [])
            p2_vals = p2_comp.get('values', [])

            t_ytd = t_comp.get('ytd_value')
            p1_ytd = p1_comp.get('ytd_value')
            p2_ytd = p2_comp.get('ytd_value')

            md += f"**{comp_name}:**\n\n"

            # Build header
            header_cols = [f"{year}" for year in years]
            if has_ytd_wc:
                header_cols.append("2025 YTD*")

            md += "| Ticker | " + " | ".join(header_cols) + " |\n"
            md += "|--------|" + "|".join(["------" for _ in header_cols]) + "|\n"

            # Build rows
            def wc_row(ticker_name, vals, ytd_val):
                cells = [fmt(vals[i] if i < len(vals) else None, 'percent') for i in range(len(years))]
                if has_ytd_wc:
                    cells.append(fmt(ytd_val, 'percent'))
                return f"| {ticker_name} | " + " | ".join(cells) + " |\n"

            md += wc_row(target_ticker, t_vals, t_ytd)
            md += wc_row(peer1_ticker, p1_vals, p1_ytd)
            md += wc_row(peer2_ticker, p2_vals, p2_ytd)
            md += "\n"

        if has_ytd_wc:
            md += f"*YTD through Q{ytd_qtrs} 2025 (most recent quarter). Not included in 5-yr statistics.*\n\n"

        md += "---\n\n"
        return md

    # Build markdown
    md = f"# Financial Statement Comparison\n\n**Target:** {target_ticker} | **Peers:** {peer1_ticker}, {peer2_ticker} | **Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n---\n\n"

    # Projection Seeds (8)
    md += "## Projection Seeds (8)\n\n"
    md += metric_table("1. Revenue", "revenue", "seeds", "dollars")
    md += metric_table("2. COGS %", "cogs_pct", "seeds", "percent")
    md += metric_table("3. SG&A %", "sga_pct", "seeds", "percent")
    md += metric_table("4. R&D %", "rd_pct", "seeds", "percent")
    md += metric_table("5. Depreciation & Amortization", "depreciation_amortization", "seeds", "dollars")
    md += metric_table("6. Capital Expenditures", "capex", "seeds", "dollars")
    md += metric_table("7. Total Debt", "total_debt", "seeds", "dollars")
    md += "### 8. Working Capital Components\n\n"
    md += wc_table()

    # Priority Metrics - Undervaluation (8)
    md += "## Priority Metrics: Undervaluation (8)\n\n"
    md += metric_table("1. Revenue (trends)", "revenue_trends", "priority_metrics", "dollars")
    md += metric_table("2. Operating Margin", "operating_margin", "priority_metrics", "percent")
    md += metric_table("3. Operating Cash Flow", "operating_cashflow", "priority_metrics", "dollars")
    md += metric_table("4. Free Cash Flow", "free_cashflow", "priority_metrics", "dollars")
    md += metric_table("5. NCAV", "ncav", "priority_metrics", "dollars")
    md += metric_table("6. ROTC", "rotc", "priority_metrics", "percent")
    md += metric_table("7. ROE", "roe", "priority_metrics", "percent")
    md += metric_table("8. Operating Leverage", "operating_leverage", "priority_metrics", "ratio")

    # Priority Metrics - Risk (5)
    md += "## Priority Metrics: Risk (5)\n\n"
    md += metric_table("1. Debt / Operating Cash Flow", "debt_to_ocf", "priority_metrics", "years")
    md += metric_table("2. OCF / Net Income", "ocf_to_ni", "priority_metrics", "ratio")
    md += metric_table("3. Accruals Gap", "accruals_gap", "priority_metrics", "percent")
    md += metric_table("4. Depreciation & Amortization", "depreciation_amortization_risk", "priority_metrics", "dollars")
    md += metric_table("5. Working Capital", "working_capital", "priority_metrics", "dollars")

    md += "\n*Note: 17 Secondary metrics available in individual {TICKER}_financial_data.json files*\n"

    with open(output_path, 'w') as f:
        f.write(md)
    print(f"✓ Generated: {output_path}")

def generate_overview_json(ticker, data, output_path):
    """Generate {TICKER}_overview.json with market data snapshot"""
    overview = data.get('overview', {})

    # Extract key fields
    market_cap = safe_float(overview.get('MarketCapitalization'))
    shares_outstanding = safe_float(overview.get('SharesOutstanding'))
    week_52_high = safe_float(overview.get('52WeekHigh'))
    week_52_low = safe_float(overview.get('52WeekLow'))
    ma_50day = safe_float(overview.get('50DayMovingAverage'))

    # Calculate current price
    current_price = None
    if market_cap and shares_outstanding and shares_outstanding > 0:
        current_price = round(market_cap / shares_outstanding, 2)

    # Calculate price positioning percentages
    vs_52wk_high_pct = None
    vs_52wk_low_pct = None
    vs_50day_ma_pct = None

    if current_price:
        if week_52_high and week_52_high > 0:
            vs_52wk_high_pct = round(((current_price - week_52_high) / week_52_high) * 100, 1)
        if week_52_low and week_52_low > 0:
            vs_52wk_low_pct = round(((current_price - week_52_low) / week_52_low) * 100, 1)
        if ma_50day and ma_50day > 0:
            vs_50day_ma_pct = round(((current_price - ma_50day) / ma_50day) * 100, 1)

    # Build output
    output = {
        'ticker': ticker,
        'data_date': datetime.now().strftime('%Y-%m-%d'),
        'as_of_quarter': overview.get('LatestQuarter'),
        'price_data': {
            'current_price': current_price,
            'calculation': 'MarketCapitalization / SharesOutstanding',
            '52_week_high': week_52_high,
            '52_week_low': week_52_low,
            '50_day_ma': ma_50day,
            'vs_52wk_high_pct': vs_52wk_high_pct,
            'vs_52wk_low_pct': vs_52wk_low_pct,
            'vs_50day_ma_pct': vs_50day_ma_pct
        },
        'valuation_data': {
            'market_cap': market_cap,
            'shares_outstanding': shares_outstanding,
            'pe_ratio': safe_float(overview.get('PERatio')),
            'trailing_pe': safe_float(overview.get('TrailingPE'))
        },
        'company_info': {
            'name': overview.get('Name'),
            'sector': overview.get('Sector'),
            'industry': overview.get('Industry'),
            'exchange': overview.get('Exchange')
        }
    }

    save_json(output, output_path)
    print(f"✓ Generated: {output_path}")

def update_tracking(ticker, target_ticker):
    """Update tracking.md (target only)"""
    if ticker != target_ticker:
        return

    data_dir = get_data_directory(ticker, target_ticker)
    tracking_file = os.path.join(data_dir, f"{ticker}_tracking.md")

    if not os.path.exists(tracking_file):
        ensure_directory_exists(data_dir)
        with open(tracking_file, 'w') as f:
            f.write(f"# {ticker} Analysis Tracking\n\n")
            f.write("This document tracks all analyses and data preparation activities.\n\n---\n\n")

    with open(tracking_file, 'a') as f:
        f.write(f"## [{datetime.now().strftime('%Y-%m-%d')}] - Statement Data Preparation\n\n")
        f.write("**Data Sources:** AlphaVantage API (Income Statement, Balance Sheet, Cash Flow, Overview)\n")
        f.write(f"**Years Analyzed:** Last {YEARS_TO_ANALYZE} fiscal years\n\n")
        f.write("**Files Generated:**\n")
        f.write(f"- `{ticker}_financial_data.json` - Complete metrics with statistics\n")
        f.write(f"- `{ticker}_overview.json` - Market data snapshot\n")
        f.write(f"- `{ticker}_statement_data.md` - Comparison table with peers\n\n")
        f.write("**Next Steps:** Run statement analysis workflow (see ANALYST_statements.md)\n\n---\n\n")

    print(f"✓ Updated: {tracking_file}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    if len(sys.argv) != 4:
        print("Usage: python SCRIPT_statements.py TICKER PEER1 PEER2")
        print("Example: python SCRIPT_statements.py IBM MSFT AAPL")
        sys.exit(1)

    target, peer1, peer2 = [t.upper() for t in sys.argv[1:4]]

    print(f"\n{'='*60}\nFinancial Statement Data Preparation\n{'='*60}")
    print(f"Target: {target} | Peers: {peer1}, {peer2}\n{'='*60}\n")

    # Step 1: Fetch all data (statements + market) for all tickers
    all_data = {}
    all_market_data = {}

    for ticker, target_ref in [(target, None), (peer1, target), (peer2, target)]:
        data = fetch_statement_data(ticker, target_ref)
        if not data:
            print(f"✗ Failed to fetch data for {ticker}")
            continue
        all_data[ticker] = (data, target_ref)

        # Fetch market data
        market_data = fetch_market_data(ticker, target_ref)
        all_market_data[ticker] = market_data

    # Step 2: Pre-calculate all market statistics once
    all_stats = {}
    for ticker in [target, peer1, peer2]:
        if ticker in all_market_data:
            all_stats[ticker] = {
                'price_statistics': calculate_price_statistics(all_market_data[ticker].get('price_monthly')),
                'earnings_statistics': calculate_earnings_statistics(all_market_data[ticker].get('earnings'))
            }

    # Helper to build ticker market data structure
    def build_ticker_market_data(ticker, include_shares=False):
        if ticker not in all_market_data:
            return None
        data = {
            'ticker': ticker,
            'earnings': all_market_data[ticker].get('earnings'),
            'price_history': all_market_data[ticker].get('price_monthly'),
            'price_statistics': all_stats[ticker]['price_statistics'],
            'earnings_statistics': all_stats[ticker]['earnings_statistics']
        }
        if include_shares:
            data['shares_outstanding'] = all_market_data[ticker].get('shares')
        return data

    # Step 3: Process each ticker and generate outputs
    for ticker, target_ref in [(target, None), (peer1, target), (peer2, target)]:
        if ticker not in all_data:
            continue

        data, _ = all_data[ticker]
        market_data = all_market_data[ticker]

        aligned = extract_annual_reports(data)
        ytd = calculate_ytd_annualized(data)

        if ytd:
            print(f"\nCalculating metrics for {ticker} (including {ytd['num_quarters']}Q YTD 2025, annualized)...")
        else:
            print(f"\nCalculating metrics for {ticker} (no YTD data available)...")

        seeds = calculate_projection_seeds(aligned, ytd)
        priority = calculate_priority_metrics(aligned, seeds, ytd)
        secondary = calculate_secondary_metrics(aligned, seeds, priority)
        assumptions = extract_projection_assumptions(aligned, data.get('overview'), market_data.get('shares'))

        data_dir = get_data_directory(ticker, target_ref)
        json_path = os.path.join(data_dir, f"{ticker}_financial_data.json")

        # Build market_data structure
        if ticker == target:
            # Helper to build pe_comparison input (needs stats + raw earnings)
            def pe_input(t):
                if t not in all_stats:
                    return None
                return {
                    'price_statistics': all_stats[t].get('price_statistics'),
                    'earnings': all_market_data[t].get('earnings')
                }

            # Target gets full comparison structure with target + peers
            complete_market_data = {
                'target': build_ticker_market_data(target, include_shares=True),
                'peers': [build_ticker_market_data(p) for p in [peer1, peer2]],
                'pe_comparison': calculate_pe_comparison(
                    pe_input(target),
                    pe_input(peer1),
                    pe_input(peer2)
                )
            }
        else:
            # Peers get their own market data (not the comparison structure)
            complete_market_data = build_ticker_market_data(ticker)

        generate_financial_data_json(ticker, aligned['years'], seeds, priority, secondary, assumptions, complete_market_data, json_path, ytd)

        # Generate overview.json for all tickers
        overview_path = os.path.join(data_dir, f"{ticker}_overview.json")
        generate_overview_json(ticker, data, overview_path)

        update_tracking(ticker, target)

    # Generate comparison table
    print(f"\n{'='*60}\nGenerating comparison table...\n{'='*60}\n")
    comparison_path = os.path.join(target, f"{target}_statement_data.md")
    generate_comparison_table(target, peer1, peer2, comparison_path)

    print(f"\n{'='*60}\n✓ Statement data preparation complete!\n{'='*60}")
    print(f"\nNext steps:")
    print(f"1. Review {target}_financial_data.json and {target}_statement_data.md")
    print(f"2. Run statement analysis: See ANALYST_statements.md for workflow\n{'='*60}\n")

if __name__ == '__main__':
    main()

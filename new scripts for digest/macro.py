#!/usr/bin/env python3
"""
Macro & Sector Discovery Digest (Refined)
=========================================

Fetches macroeconomic indicators, commodities, and sector performance.
Uses FMP Stable APIs.

Usage:
    python Scripts/Digest Scripts/macro.py --markdown
"""

import requests
import os
import sys
import argparse
from datetime import datetime, timedelta

# ============================================================================
# CONFIGURATION
# ============================================================================

FMP_STABLE_URL = "https://financialmodelingprep.com/stable"

# Mapping to allowed Raw symbols or ETF proxies
COMMODITIES = {
    'Gold': 'GCUSD',
    'Oil (Brent)': 'BZUSD',
    'Copper': 'CPER',
    'Natural Gas': 'UNG'
}

# ============================================================================
# UTILITIES
# ============================================================================

def get_date_n_days_ago(days):
    return (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

def fetch_fmp_stable(endpoint, params=None):
    api_key = os.getenv('FMP_API_KEY')
    if not params: params = {}
    params['apikey'] = api_key
    url = f"{FMP_STABLE_URL}/{endpoint}"
    
    try:
        r = requests.get(url, params=params, timeout=15)
        if r.status_code != 200:
            print(f"Error {r.status_code} for {endpoint}: {r.text}", file=sys.stderr)
            return None
        return r.json()
    except Exception as e:
        print(f"Exception fetching FMP {endpoint}: {e}", file=sys.stderr)
        return None

# ============================================================================
# DATA GATHERING
# ============================================================================

def get_asset_metrics(symbol, label):
    """Fetches Level, 1D %, MoM %, and vs 50-SMA."""
    # 1. Current Quote
    quote_data = fetch_fmp_stable("quote", {'symbol': symbol})
    if not quote_data: return None
    q = quote_data[0]
    
    # 2. 50-day SMA
    sma_data = fetch_fmp_stable("technical-indicators/sma", {
        'symbol': symbol,
        'periodLength': 50,
        'timeframe': '1day',
        'from': get_date_n_days_ago(7),
        'to': datetime.now().strftime('%Y-%m-%d')
    })
    
    # 3. MoM Price (approx 30 days ago)
    hist_data = fetch_fmp_stable("technical-indicators/sma", {
        'symbol': symbol,
        'periodLength': 1,
        'timeframe': '1day',
        'from': get_date_n_days_ago(35),
        'to': get_date_n_days_ago(25)
    })
    
    curr_price = q.get('price', 0)
    sma_50 = sma_data[0].get('sma', curr_price) if sma_data else curr_price
    
    mom_change = 0
    if hist_data and len(hist_data) > 0:
        prev_price = hist_data[-1].get('open', curr_price)
        if prev_price != 0:
            mom_change = ((curr_price - prev_price) / prev_price) * 100

    return {
        'label': label,
        'symbol': symbol,
        'price': curr_price,
        'change_1d': q.get('changePercentage', 0),
        'change_1m': mom_change,
        'vs_sma50': ((curr_price - sma_50) / sma_50) * 100 if sma_50 != 0 else 0
    }

def get_treasuries():
    """Get 10Y and 2Y Treasury rates."""
    data = fetch_fmp_stable("treasury-rates", {
        'from': get_date_n_days_ago(40),
        'to': datetime.now().strftime('%Y-%m-%d')
    })
    if not data or not isinstance(data, list) or len(data) < 2: return None
    
    curr = data[0]
    prev_day = data[1]
    prev_month = data[-1]
    
    results = []
    for mat, label in [('year10', '10-Year'), ('year2', '2-Year')]:
        if mat in curr:
            results.append({
                'label': label,
                'yield': curr[mat],
                'change_1d': curr[mat] - prev_day[mat],
                'change_1m': curr[mat] - prev_month[mat]
            })
    return results

def get_sector_discovery():
    """Get Top and Bottom 3 sectors."""
    today = datetime.now().strftime('%Y-%m-%d')
    data = fetch_fmp_stable("sector-performance-snapshot", {'date': today})
    
    if not data:
        yesterday = get_date_n_days_ago(1)
        data = fetch_fmp_stable("sector-performance-snapshot", {'date': yesterday})

    if not data: return None
    
    sectors = {}
    for item in data:
        name = item.get('sector')
        change = item.get('averageChange')
        if name and change is not None:
            if name not in sectors:
                sectors[name] = change
    
    sorted_list = sorted([{'name': k, 'change': v} for k, v in sectors.items()], key=lambda x: x['change'], reverse=True)
    return {
        'top': sorted_list[:3],
        'bottom': sorted_list[-3:]
    }

def get_economic_calendar():
    """Upcoming High-Impact events."""
    data = fetch_fmp_stable("economic-calendar", {
        'from': datetime.now().strftime('%Y-%m-%d'),
        'to': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    })
    if not data: return []
    return [e for e in data if e.get('impact') == 'High']

def get_economic_anchors():
    """Last reported CPI and Unemployment."""
    unemp = fetch_fmp_stable("economic-indicators", {
        'name': 'unemploymentRate',
        'from': get_date_n_days_ago(120),
        'to': datetime.now().strftime('%Y-%m-%d')
    })
    cpi = fetch_fmp_stable("economic-indicators", {
        'name': 'CPI',
        'from': get_date_n_days_ago(120),
        'to': datetime.now().strftime('%Y-%m-%d')
    })
    
    anchors = []
    if unemp and len(unemp) > 1:
        anchors.append({'label': 'Unemployment', 'val': unemp[0]['value'], 'unit': '%', 'delta': unemp[0]['value'] - unemp[1]['value']})
    if cpi and len(cpi) > 1:
        cpi_change = ((cpi[0]['value'] - cpi[1]['value']) / cpi[1]['value']) * 100
        anchors.append({'label': 'CPI Index', 'val': cpi[0]['value'], 'unit': '', 'delta_pct': cpi_change})
    return anchors

# ============================================================================
# MAIN OUTPUT
# ============================================================================

def main():
    # 1. Gather all data
    spy = get_asset_metrics('SPY', 'SPY')
    commodities = []
    for label, sym in COMMODITIES.items():
        res = get_asset_metrics(sym, label)
        if res: commodities.append(res)
    
    treasuries = get_treasuries()
    sectors = get_sector_discovery()
    calendar = get_economic_calendar()
    anchors = get_economic_anchors()

    # 2. Print Output
    print("## Macro Dashboard")
    
    print("\n### Market & Commodities")
    print("| Asset | Level | 1D % | MoM % | vs 50-SMA |")
    print("|:---|:---|:---|:---|:---|")
    if spy:
        print(f"| **{spy['label']}** | {spy['price']:.2f} | {spy['change_1d']:+.2f}% | {spy['change_1m']:+.2f}% | {spy['vs_sma50']:+.2f}% |")
    for c in commodities:
        print(f"| {c['label']} | {c['price']:.2f} | {c['change_1d']:+.2f}% | {c['change_1m']:+.2f}% | {c['vs_sma50']:+.2f}% |")

    if treasuries:
        print("\n### Treasury Yields")
        print("| Maturity | Yield | 1D Δ | MoM Δ |")
        print("|:---|:---|:---|:---|")
        for t in treasuries:
            print(f"| {t['label']} | {t['yield']:.2f}% | {t['change_1d']:+.3f} | {t['change_1m']:+.3f} |")

    if anchors:
        print("\n### Last Reported Economic Data")
        for a in anchors:
            if 'delta' in a:
                print(f"- **{a['label']}:** {a['val']}{a['unit']} ({a['delta']:+.2f} Δ)")
            else:
                print(f"- **{a['label']}:** {a['val']}{a['unit']} ({a['delta_pct']:+.2f}% MoM)")

    print("\n### Upcoming High-Impact Events (7 Days)")
    if calendar:
        for e in calendar[:5]:
            dt = e.get('date', '')[:10]
            print(f"- **{dt}:** {e.get('event')} ({e.get('country')})")
    else:
        print("_No major events found._")

    print("\n## Sector Discovery")
    if sectors:
        print("\n**Top Performing Sectors:**")
        for s in sectors['top']:
            print(f"- {s['name']}: {s['change']:+.2f}%")
        print("\n**Bottom Performing Sectors:**")
        for s in sectors['bottom']:
            print(f"- {s['name']}: {s['change']:+.2f}%")
    else:
        print("_Sector performance data unavailable._")

if __name__ == "__main__":
    main()

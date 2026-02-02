#!/usr/bin/env python3
"""
Financial Statements Analysis - Master Script
==============================================

Orchestrates the complete financial statements analysis pipeline:
1. Fetches raw financial data (income, balance, cashflow statements)
2. Calculates 8 projection seeds
3. Calculates 30+ financial metrics (13 priority + 17 secondary)
4. Generates markdown comparison tables

Outputs structured markdown analysis to data/analysis/{TICKER}/{TICKER}_statements.md

Usage:
    python financial_statements.py TICKER
    python financial_statements.py TICKER --compare PEER1 PEER2

Examples:
    python financial_statements.py AMZN
    python financial_statements.py AMZN --compare GOOG MSFT
"""

import sys
import os
import argparse
import subprocess
from datetime import datetime

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared_utils import (
    get_data_directory,
    ensure_directory_exists,
    load_json
)

# ============================================================================
# FORMATTING HELPERS
# ============================================================================

def fmt(val, unit, is_delta=False):
    """Format values based on unit type"""
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

def get_metric(data, metric_key):
    """Extract metric from seeds or metrics data structure"""
    # Check if it's in projection_seeds
    if 'projection_seeds' in data and metric_key in data['projection_seeds']:
        return data['projection_seeds'][metric_key]

    # Check in priority metrics
    if 'priority' in data and metric_key in data['priority']:
        return data['priority'][metric_key]

    # Check in secondary metrics
    if 'secondary' in data and metric_key in data['secondary']:
        return data['secondary'][metric_key]

    return {}

# ============================================================================
# MARKDOWN TABLE GENERATION
# ============================================================================

def build_metric_table(metric_name, metric_key, target_ticker, target_data, peer_data_list=None):
    """
    Build a metric comparison table with inline deltas and statistical summary.

    Args:
        metric_name: Display name for the metric
        metric_key: Key to look up metric in data structure
        target_ticker: Target ticker symbol
        target_data: Target ticker's data dict
        peer_data_list: List of (peer_ticker, peer_data) tuples, or None for single-ticker

    Returns:
        Markdown string
    """
    # Extract target metric
    t_metric = get_metric(target_data, metric_key)
    years = target_data.get('fiscal_years', [])
    unit = t_metric.get('unit', 'dollars')

    t_vals = t_metric.get('values', [])
    t_ytd = t_metric.get('ytd_value')

    # Extract peer metrics if provided
    peer_metrics = []
    has_ytd = t_ytd is not None

    if peer_data_list:
        for peer_ticker, peer_data in peer_data_list:
            p_metric = get_metric(peer_data, metric_key)
            p_vals = p_metric.get('values', [])
            p_ytd = p_metric.get('ytd_value')
            peer_metrics.append((peer_ticker, p_metric, p_vals, p_ytd))
            if p_ytd is not None:
                has_ytd = True

    # Get YTD quarters info
    ytd_qtrs = target_data.get('ytd_info', {}).get('num_quarters', 0)

    md = f"#### {metric_name}\n\n"

    # Build header with years and Δ% columns interleaved, plus YTD if applicable
    header_cols = [years[0]] if years else []
    for i in range(1, len(years)):
        header_cols.extend(["Δ%", years[i]])
    if has_ytd:
        header_cols.extend(["Δ%*", "2025 YTD*"])

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
            if ytd_val is not None and len(vals) > 0 and vals[-1] is not None and vals[-1] != 0:
                ytd_delta_pct = ((ytd_val - vals[-1]) / vals[-1]) * 100
                ytd_delta_str = fmt(ytd_delta_pct, 'percent', is_delta=True)
            else:
                ytd_delta_str = "—"
            row_cells.extend([ytd_delta_str, fmt(ytd_val, unit)])

        return f"| {ticker_name} | " + " | ".join(row_cells) + " |\n"

    # Add target row
    md += build_row(target_ticker, t_vals, t_ytd)

    # Add peer rows
    for peer_ticker, _, p_vals, p_ytd in peer_metrics:
        md += build_row(peer_ticker, p_vals, p_ytd)

    # Add footnote if YTD data present
    if has_ytd and ytd_qtrs:
        md += f"\n*YTD through Q{ytd_qtrs} 2025, annualized. Δ%* shows change vs. 2024 full year. Not included in 5-yr statistics below.*\n"

    md += "\n**Statistical Summary:**\n\n"
    md += "| Ticker | Current | 5-Yr Avg | CAGR | Slope | Recent Δ% | CV | Outliers |\n"
    md += "|--------|---------|----------|------|-------|-----------|-----|----------|\n"

    # Helper for stats row
    def stats_row(ticker_name, metric):
        current = fmt(metric.get('current'), unit)
        avg_5yr = fmt(metric.get('avg_5yr'), unit)
        cagr = fmt(metric.get('cagr'), 'percent') if metric.get('cagr') is not None else "—"
        slope = fmt(metric.get('slope'), unit)
        recent_delta = fmt(metric.get('recent_delta', {}).get('percent'), 'percent', is_delta=True) if metric.get('recent_delta', {}).get('percent') is not None else "—"
        cv = fmt(metric.get('cv'), 'percent') if metric.get('cv') is not None else "—"
        outliers = ", ".join(metric.get('outlier_years', [])) if metric.get('outlier_years') else "None"
        return f"| {ticker_name} | {current} | {avg_5yr} | {cagr} | {slope} | {recent_delta} | {cv} | {outliers} |\n"

    md += stats_row(target_ticker, t_metric)
    for peer_ticker, p_metric, _, _ in peer_metrics:
        md += stats_row(peer_ticker, p_metric)

    md += "\n---\n\n"
    return md

def build_wc_components_table(target_ticker, target_data, peer_data_list=None):
    """Build working capital components nested table"""
    years = target_data.get('fiscal_years', [])

    # Check if any ticker has YTD data for WC components
    wc_seeds = target_data.get('projection_seeds', {}).get('working_capital_components', {})
    has_ytd_wc = any([
        wc_seeds.get(key, {}).get('ytd_value') is not None
        for key in ['ar_pct_revenue', 'inventory_pct_cogs', 'ap_pct_cogs']
    ])

    if peer_data_list:
        for _, peer_data in peer_data_list:
            peer_wc = peer_data.get('projection_seeds', {}).get('working_capital_components', {})
            if any([peer_wc.get(key, {}).get('ytd_value') is not None for key in ['ar_pct_revenue', 'inventory_pct_cogs', 'ap_pct_cogs']]):
                has_ytd_wc = True
                break

    ytd_qtrs = target_data.get('ytd_info', {}).get('num_quarters', 0)

    md = "#### Working Capital Components\n\n"

    for comp_key, comp_name in [('ar_pct_revenue', 'A/R % of Revenue'),
                                  ('inventory_pct_cogs', 'Inventory % of COGS'),
                                  ('ap_pct_cogs', 'A/P % of COGS')]:
        t_comp = wc_seeds.get(comp_key, {})
        t_vals = t_comp.get('values', [])
        t_ytd = t_comp.get('ytd_value')

        # Extract peer components
        peer_comps = []
        if peer_data_list:
            for peer_ticker, peer_data in peer_data_list:
                peer_wc = peer_data.get('projection_seeds', {}).get('working_capital_components', {})
                p_comp = peer_wc.get(comp_key, {})
                p_vals = p_comp.get('values', [])
                p_ytd = p_comp.get('ytd_value')
                peer_comps.append((peer_ticker, p_vals, p_ytd))

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
        for peer_ticker, p_vals, p_ytd in peer_comps:
            md += wc_row(peer_ticker, p_vals, p_ytd)
        md += "\n"

    if has_ytd_wc and ytd_qtrs:
        md += f"*YTD through Q{ytd_qtrs} 2025 (most recent quarter). Not included in 5-yr statistics.*\n\n"

    md += "---\n\n"
    return md

# ============================================================================
# ORCHESTRATION
# ============================================================================

def run_script(script_name, args):
    """Run a script from scripts/ticker/ directory"""
    script_path = os.path.join(os.path.dirname(__file__), 'ticker', script_name)
    cmd = [sys.executable, script_path] + args

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error running {script_name}:")
        print(result.stderr)
        return False
    return True

def ensure_data_fetched(ticker):
    """Ensure raw financial data exists, fetch if missing"""
    data_dir = get_data_directory(ticker)
    raw_path = os.path.join(data_dir, f"{ticker}_financial_raw.json")

    if os.path.exists(raw_path):
        print(f"✓ Raw data exists for {ticker}")
        return True

    print(f"→ Fetching raw data for {ticker}...")
    if not run_script('fetch_financials.py', [ticker]):
        print(f"✗ Failed to fetch data for {ticker}")
        return False
    return True

def ensure_seeds_calculated(ticker):
    """Ensure projection seeds calculated, run if missing"""
    data_dir = get_data_directory(ticker)
    seeds_path = os.path.join(data_dir, f"{ticker}_seeds.json")

    if os.path.exists(seeds_path):
        print(f"✓ Seeds exist for {ticker}")
        return True

    print(f"→ Calculating seeds for {ticker}...")
    if not run_script('calc_seeds.py', [ticker]):
        print(f"✗ Failed to calculate seeds for {ticker}")
        return False
    return True

def ensure_metrics_calculated(ticker):
    """Ensure metrics calculated, run if missing"""
    data_dir = get_data_directory(ticker)
    metrics_path = os.path.join(data_dir, f"{ticker}_metrics.json")

    if os.path.exists(metrics_path):
        print(f"✓ Metrics exist for {ticker}")
        return True

    print(f"→ Calculating metrics for {ticker}...")
    if not run_script('calc_metrics.py', [ticker]):
        print(f"✗ Failed to calculate metrics for {ticker}")
        return False
    return True

def load_ticker_data(ticker):
    """Load seeds and metrics for a ticker"""
    data_dir = get_data_directory(ticker)

    seeds_data = load_json(os.path.join(data_dir, f"{ticker}_seeds.json"))
    metrics_data = load_json(os.path.join(data_dir, f"{ticker}_metrics.json"))

    if not seeds_data or not metrics_data:
        return None

    # Merge into single structure for easier access
    return {
        'ticker': ticker,
        'fiscal_years': seeds_data.get('fiscal_years', []),
        'ytd_info': seeds_data.get('ytd_info', {}),
        'projection_seeds': seeds_data.get('projection_seeds', {}),
        'priority': metrics_data.get('priority', {}),
        'secondary': metrics_data.get('secondary', {})
    }

def generate_markdown(target_ticker, target_data, peer_data_list=None):
    """Generate complete markdown document"""

    # Build header
    if peer_data_list:
        peer_names = ", ".join([p[0] for p in peer_data_list])
        md = f"# Financial Statement Comparison\n\n"
        md += f"**Target:** {target_ticker} | **Peers:** {peer_names} | **Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n---\n\n"
    else:
        md = f"# Financial Statement Analysis: {target_ticker}\n\n"
        md += f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n---\n\n"

    # Projection Seeds (8)
    md += "## Projection Seeds (8)\n\n"
    md += build_metric_table("1. Revenue", "revenue", target_ticker, target_data, peer_data_list)
    md += build_metric_table("2. COGS %", "cogs_pct", target_ticker, target_data, peer_data_list)
    md += build_metric_table("3. SG&A %", "sga_pct", target_ticker, target_data, peer_data_list)
    md += build_metric_table("4. R&D %", "rd_pct", target_ticker, target_data, peer_data_list)
    md += build_metric_table("5. Depreciation & Amortization", "depreciation_amortization", target_ticker, target_data, peer_data_list)
    md += build_metric_table("6. Capital Expenditures", "capex", target_ticker, target_data, peer_data_list)
    md += build_metric_table("7. Total Debt", "total_debt", target_ticker, target_data, peer_data_list)
    md += "### 8. Working Capital Components\n\n"
    md += build_wc_components_table(target_ticker, target_data, peer_data_list)

    # Priority Metrics - Undervaluation (8)
    md += "## Priority Metrics: Undervaluation (8)\n\n"
    md += build_metric_table("1. Revenue (trends)", "revenue_trends", target_ticker, target_data, peer_data_list)
    md += build_metric_table("2. Operating Margin", "operating_margin", target_ticker, target_data, peer_data_list)
    md += build_metric_table("3. Operating Cash Flow", "operating_cashflow", target_ticker, target_data, peer_data_list)
    md += build_metric_table("4. Free Cash Flow", "free_cashflow", target_ticker, target_data, peer_data_list)
    md += build_metric_table("5. NCAV", "ncav", target_ticker, target_data, peer_data_list)
    md += build_metric_table("6. ROTC", "rotc", target_ticker, target_data, peer_data_list)
    md += build_metric_table("7. ROE", "roe", target_ticker, target_data, peer_data_list)
    md += build_metric_table("8. Operating Leverage", "operating_leverage", target_ticker, target_data, peer_data_list)

    # Priority Metrics - Risk (5)
    md += "## Priority Metrics: Risk (5)\n\n"
    md += build_metric_table("1. Debt / Operating Cash Flow", "debt_to_ocf", target_ticker, target_data, peer_data_list)
    md += build_metric_table("2. OCF / Net Income", "ocf_to_ni", target_ticker, target_data, peer_data_list)
    md += build_metric_table("3. Accruals Gap", "accruals_gap", target_ticker, target_data, peer_data_list)
    md += build_metric_table("4. Depreciation & Amortization", "depreciation_amortization_risk", target_ticker, target_data, peer_data_list)
    md += build_metric_table("5. Working Capital", "working_capital", target_ticker, target_data, peer_data_list)

    # Footer
    md += "\n*Note: 17 Secondary metrics available in individual {TICKER}_metrics.json files*\n"

    return md

# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Financial Statements Analysis - Master Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python financial_statements.py AMZN
  python financial_statements.py AMZN --compare GOOG MSFT
        """
    )
    parser.add_argument("ticker", help="Target ticker symbol")
    parser.add_argument("--compare", nargs=2, metavar=("PEER1", "PEER2"),
                       help="Optional: Compare with two peer tickers")

    args = parser.parse_args()

    target = args.ticker.upper()
    peers = [p.upper() for p in args.compare] if args.compare else []

    print(f"\n{'='*60}")
    print(f"Financial Statements Analysis")
    print(f"{'='*60}")
    if peers:
        print(f"Target: {target} | Peers: {', '.join(peers)}")
    else:
        print(f"Target: {target} (no peer comparison)")
    print(f"{'='*60}\n")

    # Process target
    all_tickers = [target] + peers

    for ticker in all_tickers:
        print(f"\nProcessing {ticker}...")
        print("-" * 40)

        if not ensure_data_fetched(ticker):
            sys.exit(1)

        if not ensure_seeds_calculated(ticker):
            sys.exit(1)

        if not ensure_metrics_calculated(ticker):
            sys.exit(1)

        print(f"✓ {ticker} data ready\n")

    # Load all data
    print(f"\n{'='*60}")
    print("Loading data and generating markdown...")
    print(f"{'='*60}\n")

    target_data = load_ticker_data(target)
    if not target_data:
        print(f"✗ Failed to load data for {target}")
        sys.exit(1)

    peer_data_list = []
    if peers:
        for peer in peers:
            peer_data = load_ticker_data(peer)
            if not peer_data:
                print(f"✗ Failed to load data for {peer}")
                sys.exit(1)
            peer_data_list.append((peer, peer_data))

    # Generate markdown
    markdown = generate_markdown(target, target_data, peer_data_list if peer_data_list else None)

    # Save to data/analysis/{TICKER}/{TICKER}_statements.md
    analysis_dir = os.path.join(get_data_directory(target), '..', '..', 'analysis', target)
    ensure_directory_exists(analysis_dir)

    output_path = os.path.join(analysis_dir, f"{target}_statements.md")
    with open(output_path, 'w') as f:
        f.write(markdown)

    print(f"\n{'='*60}")
    print("✓ Financial statements analysis complete!")
    print(f"{'='*60}")
    print(f"\nOutput saved to: {output_path}")
    print(f"\nNext steps:")
    print(f"  - Review the statements markdown file")
    print(f"  - Use for LLM-based qualitative analysis\n")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

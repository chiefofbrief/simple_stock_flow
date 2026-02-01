#!/usr/bin/env python3
"""
Financial Comparison Tool
=========================

Generates a side-by-side comparison report for a target stock and two peers.
Uses data from _seeds.json and _metrics.json.

Usage:
    python compare_financials.py TARGET PEER1 PEER2
"""

import sys
import os
import argparse
from datetime import datetime

# Add parent directory to path for shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_utils import (
    get_data_directory,
    load_json
)

def fmt(val, unit, is_delta=False):
    if val is None: return "—"
    prefix = "+" if is_delta and val > 0 else ""
    if unit == 'dollars': return f"{prefix}${val:,0f}"
    if unit == 'percent': return f"{prefix}{val:.1f}%"
    if unit == 'ratio' or unit == 'years': return f"{prefix}{val:.2f}"
    if unit == 'days': return f"{prefix}{val:.0f}"
    return f"{prefix}{val}"

def get_metric(data, section, key):
    """Helper to find a metric in seeds or metrics data"""
    if section == 'seeds':
        return data.get('projection_seeds', {}).get(key, {})
    
    # Check priority then secondary
    metrics = data.get('priority', {})
    if key in metrics: return metrics[key]
    
    metrics = data.get('secondary', {})
    if key in metrics: return metrics[key]
    
    return {}

def build_metric_table(target_name, p1_name, p2_name, t_data, p1_data, p2_data, metric_name, target_key, section, unit):
    years = t_data['seeds'].get('fiscal_years', [])
    
    t_m = get_metric(t_data[section], section, target_key)
    p1_m = get_metric(p1_data[section], section, target_key)
    p2_m = get_metric(p2_data[section], section, target_key)

    t_vals = t_m.get('values', [])
    p1_vals = p1_m.get('values', [])
    p2_vals = p2_m.get('values', [])

    t_ytd = t_m.get('ytd_value')
    p1_ytd = p1_m.get('ytd_value')
    p2_ytd = p2_m.get('ytd_value')
    has_ytd = any([v is not None for v in [t_ytd, p1_ytd, p2_ytd]])
    ytd_qtrs = t_data['seeds'].get('ytd_info', {}).get('num_quarters', 0)

    md = f"#### {metric_name}\n\n"
    
    header = [years[0]]
    for i in range(1, len(years)):
        header.extend(["Δ%", years[i]])
    if has_ytd:
        header.extend(["Δ%*", "2025 YTD*"])

    md += "| Ticker | " + " | ".join(header) + " |\n"
    md += "|--------|" + "|".join(["------" for _ in header]) + "|\n"

    def build_row(name, vals, ytd_val):
        row = [fmt(vals[0] if len(vals) > 0 else None, unit)]
        for i in range(1, len(years)):
            if i < len(vals) and vals[i] is not None and vals[i-1] is not None and vals[i-1] != 0:
                delta = ((vals[i] - vals[i-1]) / vals[i-1]) * 100
                delta_str = fmt(delta, 'percent', is_delta=True)
            else:
                delta_str = "—"
            row.extend([delta_str, fmt(vals[i] if i < len(vals) else None, unit)])
        
        if has_ytd:
            if ytd_val is not None and len(vals) > 0 and vals[-1] is not None and vals[-1] != 0:
                delta = ((ytd_val - vals[-1]) / vals[-1]) * 100
                delta_str = fmt(delta, 'percent', is_delta=True)
            else:
                delta_str = "—"
            row.extend([delta_str, fmt(ytd_val, unit)])
        return f"| {name} | " + " | ".join(row) + " |\n"

    md += build_row(target_name, t_vals, t_ytd)
    md += build_row(p1_name, p1_vals, p1_ytd)
    md += build_row(p2_name, p2_vals, p2_ytd)

    if has_ytd:
        md += f"\n*YTD through Q{ytd_qtrs} 2025, annualized.*\n"
    
    md += "\n**Statistical Summary:**\n\n"
    md += "| Ticker | Current | 5-Yr Avg | CAGR | Slope | Recent Δ% | CV |\n"
    md += "|--------|---------|----------|------|-------|-----------|-----|\n"

    for name, m in [(target_name, t_m), (p1_name, p1_m), (p2_name, p2_m)]:
        curr = fmt(m.get('current'), unit)
        avg = fmt(m.get('avg_5yr'), unit)
        cagr = fmt(m.get('cagr'), 'percent') if m.get('cagr') is not None else "—"
        slope = fmt(m.get('slope'), unit)
        delta = fmt(m.get('recent_delta', {}).get('percent'), 'percent', is_delta=True)
        cv = fmt(m.get('cv'), 'percent')
        md += f"| {name} | {curr} | {avg} | {cagr} | {slope} | {delta} | {cv} |\n"

    md += "\n---\n\n"
    return md

def main():
    parser = argparse.ArgumentParser(description="Compare financial data")
    parser.add_argument("target", help="Target ticker")
    parser.add_argument("peer1", help="Peer 1 ticker")
    parser.add_argument("peer2", help="Peer 2 ticker")
    args = parser.parse_args()

    target, p1, p2 = args.target.upper(), args.peer1.upper(), args.peer2.upper()
    
    def load_ticker_data(t):
        d_dir = get_data_directory(t)
        return {
            'seeds': load_json(os.path.join(d_dir, f"{t}_seeds.json")),
            'metrics': load_json(os.path.join(d_dir, f"{t}_metrics.json"))
        }

    t_data = load_ticker_data(target)
    p1_data = load_ticker_data(p1)
    p2_data = load_ticker_data(p2)

    if not all([t_data['seeds'], p1_data['seeds'], p2_data['seeds']]):
        print("Error: Missing data files. Ensure fetch/calc steps are run for all tickers.")
        return

    md = f"# Financial Comparison: {target}\n"
    md += f"**Peers:** {p1}, {p2} | **Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n---\n\n"

    md += "## 1. Projection Seeds\n\n"
    md += build_metric_table(target, p1, p2, t_data, p1_data, p2_data, "Revenue", "revenue", "seeds", "dollars")
    md += build_metric_table(target, p1, p2, t_data, p1_data, p2_data, "COGS %", "cogs_pct", "seeds", "percent")
    md += build_metric_table(target, p1, p2, t_data, p1_data, p2_data, "Operating Margin", "operating_margin", "metrics", "percent")
    
    md += "## 2. Priority Metrics\n\n"
    md += build_metric_table(target, p1, p2, t_data, p1_data, p2_data, "Operating Cash Flow", "operating_cashflow", "metrics", "dollars")
    md += build_metric_table(target, p1, p2, t_data, p1_data, p2_data, "Free Cash Flow", "free_cashflow", "metrics", "dollars")
    md += build_metric_table(target, p1, p2, t_data, p1_data, p2_data, "ROTC", "rotc", "metrics", "percent")

    output_path = os.path.join(get_data_directory(target), f"{target}_comparison.md")
    with open(output_path, "w") as f:
        f.write(md)
    print(f"✓ Comparison report generated: {output_path}")

if __name__ == "__main__":
    main()

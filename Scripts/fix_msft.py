import os
import re
import json
from bs4 import BeautifulSoup

def extract_mda(html_path, start_item, end_item):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    text = soup.get_text(separator='\n', strip=True)
    
    # Try to find the start and end of the items
    # Microsoft usually has "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS..."
    
    # Let's just do a regex on the extracted text
    start_pattern = re.compile(rf'ITEM\s+{start_item}\.\s+MANAGEMENT', re.IGNORECASE)
    end_pattern = re.compile(rf'ITEM\s+{end_item}\.', re.IGNORECASE)
    
    starts = [m.start() for m in start_pattern.finditer(text)]
    ends = [m.start() for m in end_pattern.finditer(text)]
    
    # TOC mentions will be early in the text, so we take the last start match, or the one past the first 10000 chars.
    valid_starts = [s for s in starts if s > 5000]
    if not valid_starts:
        valid_starts = starts
    
    start_pos = valid_starts[-1] if valid_starts else 0
    
    valid_ends = [e for e in ends if e > start_pos + 5000]
    end_pos = valid_ends[0] if valid_ends else len(text)
    
    return text[start_pos:end_pos]

mda_10k = extract_mda('Data/tickers/MSFT/raw/MSFT_10k_latest.html', '7', '7A')
mda_10q = extract_mda('Data/tickers/MSFT/raw/MSFT_10q_latest.html', '2', '3')

# Check sizes
print(f"Extracted 10-K MD&A: {len(mda_10k.split())} words")
print(f"Extracted 10-Q MD&A: {len(mda_10q.split())} words")

# Overwrite the broken text files
with open('Data/tickers/MSFT/raw/MSFT_10k_mda.txt', 'w', encoding='utf-8') as f:
    f.write(mda_10k)
    
with open('Data/tickers/MSFT/raw/MSFT_10q_mda.txt', 'w', encoding='utf-8') as f:
    f.write(mda_10q)

# Load metadata and update stats so we can generate the final MD&A file
with open('Data/tickers/MSFT/raw/MSFT_filings_metadata.json', 'r') as f:
    meta = json.load(f)

# Manually create the MSFT_mda.md file
md = ["# NOW SEC Filings: MD&A", "**Generated:** 2026-05-10", "**Filings:** 10-K, 10-Q", "", "---", "## 10-K MD&A (Item 7)", mda_10k, "---", "## 10-Q MD&A (Item 2)", mda_10q]

with open('Data/tickers/MSFT/MSFT_mda.md', 'w', encoding='utf-8') as f:
    f.write("\n\n".join(md))
    
print("Successfully generated MSFT_mda.md manually.")

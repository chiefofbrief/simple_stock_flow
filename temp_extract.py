import json
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.text.append(cleaned)

with open("Data/tickers/NVDA/raw/NVDA_10k_latest.html", "r", encoding="utf-8") as f:
    html_content = f.read()

html_clean = re.sub(r'</?(ix|xbrli):[^>]*>', '', html_content)
parser = TextExtractor()
parser.feed(html_clean)
lines = parser.text

# MD&A lines
mda_lines = lines[1457:1861]
mda_text = "\n".join(mda_lines)
with open("Data/tickers/NVDA/raw/NVDA_10k_mda.txt", "w", encoding="utf-8") as f:
    f.write(mda_text)

# Notes lines
notes_lines = lines[2699:4699]
notes_text = "\n".join(notes_lines)
with open("Data/tickers/NVDA/raw/NVDA_10k_notes.txt", "w", encoding="utf-8") as f:
    f.write(notes_text)

print(f"MD&A words: {len(mda_text.split())}")
print(f"Notes words: {len(notes_text.split())}")

# The user's prompt indicated to proceed with earnings_calls.py after footnotes.py succeeds.

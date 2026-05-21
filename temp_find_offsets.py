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
full_text = '\n'.join(parser.text)
norm_text = re.sub(r'\s+', ' ', full_text)

# Find all Item 7 / 7A / 8
print("--- ITEM 7, 7A, 8 matches ---")
matches = list(re.finditer(r'\bITEM\s+(7|7A|8)\b', norm_text, re.IGNORECASE))
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(norm_text), m.start() + 150)
    print(f"Pos {m.start()} [ITEM {m.group(1)}]: {norm_text[start:end]}")

print("\n--- NOTES matches ---")
notes_matches = list(re.finditer(r'\bNotes\s+to\s+Consolidated\s+Financial\s+Statements\b', norm_text, re.IGNORECASE))
for m in notes_matches:
    start = max(0, m.start() - 50)
    end = min(len(norm_text), m.start() + 150)
    print(f"Pos {m.start()}: {norm_text[start:end]}")

import re

with open(r"c:\Users\Antonela\Desktop\Caroline\revista\index.html", "r", encoding="utf-8") as f:
    html = f.read()

sections = re.findall(r'<section class="page"[^>]*id="([pP]\d+)"', html)
print(f"Total pages found: {len(sections)}")
print(f"Page IDs: {sections}")

headers = re.findall(r'<div class="rubric-header">', html)
print(f"Total .rubric-header found: {len(headers)}")

# Pages that shouldn't have rubric-header: p1 (cover), p2 (TOC), p24 (backcover)
# So expected headers: len(sections) - 3 (which is 21 if there are 24 pages)

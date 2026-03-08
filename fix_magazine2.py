import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Fix stray div
pattern = r'(padding-bottom:\s*2mm;">.*?</div>)\s*</div>'
index_html = re.sub(pattern, r'\1', index_html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Stray divs removed.")

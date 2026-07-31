import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")
orig_path = os.path.join(base_dir, "original_index.html")

# 1. Read the original HTML for the genuine page 1 (cover) and page 2 (TOC)
with open(orig_path, "r", encoding="utf-8") as f:
    orig_html = f.read()

p1_orig = re.search(r'(<section class="page page-cover" id="p1">.*?</section>)', orig_html, flags=re.DOTALL).group(1)
p2_orig = re.search(r'(<section class="page toc-page" id="p2">.*?</section>)', orig_html, flags=re.DOTALL).group(1)

# Ensure cover image points to the right place
p1_orig = p1_orig.replace('Coperta_noua.png', 'Coperta.png')

# 2. Read current index
with open(index_path, "r", encoding="utf-8") as f:
    current_index = f.read()

# 3. Replace the placeholder p1 and p2 with the genuine ones
# p1 might just be class="page" right now
current_index = re.sub(r'<section class="page"[^>]*id="p1".*?</section>', p1_orig, current_index, flags=re.DOTALL)
current_index = re.sub(r'<section class="page"[^>]*id="p2".*?</section>', p2_orig, current_index, flags=re.DOTALL)

# 4. Remove TOC navigation buttons on top if any (there shouldn't be, but just in case)
nav_pattern = r'<!-- Navigation -->\s*<nav class="page-nav">.*?</nav>'
current_index = re.sub(nav_pattern, '', current_index, flags=re.DOTALL)

# Write back
with open(index_path, "w", encoding="utf-8") as f:
    f.write(current_index)

print("Pages 1 and 2 successfully restored as Cover and TOC.")

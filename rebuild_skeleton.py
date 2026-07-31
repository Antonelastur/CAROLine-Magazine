import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")
pages2_path = os.path.join(base_dir, "pages2.html")
orig_path = os.path.join(base_dir, "original_index.html")

# 1. Read current files
with open(index_path, "r", encoding="utf-8") as f:
    current_index = f.read()

pages2_content = ""
if os.path.exists(pages2_path):
    with open(pages2_path, "r", encoding="utf-8") as f:
        pages2_content = f.read()

# 2. Extract sections from current index and pages2
section_pattern = r'(<section class="page"[^>]*id="([pP]\d+)".*?</section>)'
index_sections = re.findall(section_pattern, current_index, flags=re.DOTALL)
pages2_sections = re.findall(section_pattern, pages2_content, flags=re.DOTALL)

# Create a dictionary of all sections by ID (p1, p2, ...)
all_sections = {}
for sec_html, p_id in index_sections:
    all_sections[p_id.lower()] = sec_html
for sec_html, p_id in pages2_sections:
    all_sections[p_id.lower()] = sec_html

# 3. Read the original HTML skeleton
with open(orig_path, "r", encoding="utf-8") as f:
    orig_html = f.read()

# Extract everything before <section class="page" id="p1">
# Except we want to remove the navigation as requested before.
skeleton_top_match = re.search(r'^(.*?)<!-- Navigation -->', orig_html, flags=re.DOTALL)
if skeleton_top_match:
    skeleton_top = skeleton_top_match.group(1)
else:
    skeleton_top_match = re.search(r'^(.*?)<section class="page"', orig_html, flags=re.DOTALL)
    skeleton_top = skeleton_top_match.group(1)

# Ensure body tag is there
if "<body>" not in skeleton_top:
    skeleton_top += "\n<body>\n"

# 4. Remove stray div inside all sections (the fix from earlier)
def remove_stray_divs(html):
    pattern = r'(padding-bottom:\s*2mm;">.*?</div>)\s*</div>'
    return re.sub(pattern, r'\1', html, flags=re.DOTALL)

for pid in all_sections:
    all_sections[pid] = remove_stray_divs(all_sections[pid])

# 5. Fix the cover (Restore to Coperta.png)
if 'p1' in all_sections:
    all_sections['p1'] = all_sections['p1'].replace('Coperta_noua.png', 'Coperta.png')

# 6. Combine all sections 1 to 24
combined_sections = []
for i in range(1, 25):
    pid = f"p{i}"
    if pid in all_sections:
        combined_sections.append(all_sections[pid])
    else:
        # missing page? shouldn't happen based on the previous scripts, but just in case
        print(f"Warning: {pid} is missing.")

# 7. Assemble final HTML
final_html = skeleton_top + "\n" + "\n".join(combined_sections) + "\n</body>\n</html>"

with open(index_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("index.html rebuilt successfully with correct HTML structure and all 24 pages.")

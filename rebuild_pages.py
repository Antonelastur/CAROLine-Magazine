import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")
p2_path = os.path.join(base_dir, "pages2.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Pages list
pages = {}
sections = re.findall(r'(<section class="page"[^>]*id="([pP]\d+)".*?</section>)', html, flags=re.DOTALL)
for sec_html, p_id in sections:
    pages[p_id.lower()] = sec_html

# Read pages2 if we have anything there
if os.path.exists(p2_path):
    with open(p2_path, "r", encoding="utf-8") as f2:
        html2 = f2.read()
    sections2 = re.findall(r'(<section class="page"[^>]*id="([pP]\d+)".*?</section>)', html2, flags=re.DOTALL)
    for sec_html, p_id in sections2:
        if p_id.lower() not in pages:
            pages[p_id.lower()] = sec_html

# Expected missing pages
for i in range(1, 25):
    pid = f"p{i}"
    if pid not in pages:
        # Create a placeholder for missing page
        print(f"Missing {pid}, generating placeholder...")
        pages[pid] = f'''<section class="page" id="{pid}">
    <div class="page-inner">
      <div class="rubric-header">
        <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
        <div class="header-content">
          <h2 style="color: #C8A97E; font-family: var(--font-heading); font-size: 20pt; font-weight: 700; margin-bottom: 2px;">Pagina {i} Placeholder</h2>
          <div class="rubric-sub" style="font-family: var(--font-subheading); font-size: 9pt; color: var(--gold-warm); text-transform: uppercase;">Necesită Conținut</div>
        </div>
        <div class="header-page-num">{i}</div>
      </div>
      <!-- placeholder content -->
    </div>
</section>'''

# Combine all 24 pages in order
final_html_parts = []

# Get everything before <section class="page" id="p1">
pre_match = re.search(r'^(.*?)<section class="page"[^>]*id="[pP]1"', html, flags=re.DOTALL)
if pre_match:
    final_html_parts.append(pre_match.group(1))

for i in range(1, 25):
    pid = f"p{i}"
    final_html_parts.append(pages[pid])

# Get everything after <section class="page" id="p24"> (but if not exact, we close the tags manually)
final_html_parts.append("\n  </div>\n</body>\n</html>")

final_html = "\n".join(final_html_parts)

# Remove "TIMELINE" and other english words like Spotlight, Focus, Zoom
final_html = re.sub(r'\bTIMELINE!!!\b', '', final_html, flags=re.IGNORECASE)
final_html = re.sub(r'\bTIMELINE\b', '', final_html, flags=re.IGNORECASE)
final_html = re.sub(r'\bSpotlight\b', 'Reflector', final_html, flags=re.IGNORECASE)
final_html = re.sub(r'\bZoom\b', 'Aproape', final_html, flags=re.IGNORECASE)
final_html = re.sub(r'\bFocus\b', 'Atenție', final_html, flags=re.IGNORECASE)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Rebuilt index.html with 24 pages + removed EN words.")

import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")
pages2_path = os.path.join(base_dir, "pages2.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()
    
with open(pages2_path, "r", encoding="utf-8") as f:
    pages2_html = f.read()

# 1. Remove stray `</div>` after the subtitle exactly matching the pattern
def remove_stray_divs(html):
    # The stray div looks like:
    #       <div style="font-family: var(--font-subheading); ... padding-bottom: 2mm;">...</div>
    #
    #       </div>
    # We want to remove the latter </div> which appears right after the subtitle's closing </div> and any whitespace/newlines.
    
    # We can match `padding-bottom: 2mm;">.*?</div>\s*</div>` and replace it with `...</div>`
    pattern = r'(padding-bottom:\s*2mm;">.*?</div>)\s*</div>'
    return re.sub(pattern, r'\1', html)

index_html = remove_stray_divs(index_html)
pages2_html = remove_stray_divs(pages2_html)

# 2. Revert the cover to Coperta.png
index_html = index_html.replace('src="../Imagini/Coperta_noua.png"', 'src="../Imagini/Coperta.png"')

# 3. Remove navigation (ținta paginilor)
nav_pattern = r'<!-- Navigation -->\s*<nav class="page-nav">.*?</nav>'
index_html = re.sub(nav_pattern, '', index_html, flags=re.DOTALL)

# 4. Remove PARTEA 2 script from index.html
part2_pattern = r'<!-- PARTEA 2 -->\s*<div id="pages-part2"></div>\s*<script>fetch.*?</script>'
index_html = re.sub(part2_pattern, '', index_html, flags=re.DOTALL)

# 5. Extract sections from pages2.html
# pages2.html just contains <section class="page"...> elements.
sections_pattern = r'(<section class="page".*?</section>)'
sections = re.findall(sections_pattern, pages2_html, flags=re.DOTALL)

# 6. Append sections to index.html before </body>
combined_sections = "\n".join(sections)
index_html = index_html.replace('</body>', f'{combined_sections}\n</body>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Pages merged, stray divs removed, cover reverted, and navigation removed.")

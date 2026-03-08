import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Pages to skip placing generic headers (cover, toc, backcover)
# We match each section, determine its page ID (e.g. `id="p3"`), and replace its header

def replace_header(match):
    section_content = match.group(0)
    
    # Exclude pages 1, 2, 24
    if 'id="p1"' in section_content or 'id="p2"' in section_content or 'id="p24"' in section_content:
        return section_content
        
    # Extract page ID number
    page_id_match = re.search(r'id="p(\d+)"', section_content)
    page_num = page_id_match.group(1) if page_id_match else ""

    # Find the <h2> and subtitle <div>
    # Format current:
    # <h2 style="...">[TITLE]</h2>
    # <div style="...">[SUBTITLE]</div>
    
    h2_pattern = re.compile(r'<h2[^>]*>(.*?)</h2>', re.DOTALL)
    sub_pattern = re.compile(r'<div[^>]*font-family:\s*var\(--font-subheading\)[^>]*>(.*?)</div>', re.DOTALL)
    
    h2_match = h2_pattern.search(section_content)
    sub_match = sub_pattern.search(section_content)
    
    if not h2_match or not sub_match:
        return section_content
        
    title = h2_match.group(1).strip()
    subtitle = sub_match.group(1).strip()
    
    # We want to remove the matched elements from the section content 
    # and insert the new rubric-header at the very top of `.page-inner`
    
    # Rebuild the new header
    new_header = f'''<div class="rubric-header">
  <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
  <div class="header-content">
    <h2>{title}</h2>
    <div class="rubric-sub">{subtitle}</div>
  </div>
  <div class="header-page-num">{page_num}</div>
</div>'''

    # Remove the old h2 and subtitle using sub, taking care to replace only the first occurrence 
    # (though they should be unique)
    
    # Remove h2
    section_content = h2_pattern.sub("", section_content, count=1)
    # Remove sub
    section_content = sub_pattern.sub("", section_content, count=1)
    
    # Insert new header right after <div class="page-inner">
    section_content = section_content.replace('<div class="page-inner">', f'<div class="page-inner">\n      {new_header}', 1)
    
    return section_content

new_html = re.sub(r'<section class="page"[^>]*>.*?</section>', replace_header, html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Headers replaced successfully.")

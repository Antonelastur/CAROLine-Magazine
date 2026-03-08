import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove segment badges
    html = re.sub(r'\s*<span class="segment-badge[^>]*>.*?</span>', '', html)

    # 2. Extract and replace rubric-header
    # We use a non-greedy match to find the whole rubric-header div
    pattern = r'<div class="rubric-header">([\s\S]*?)</div>\s*(?=<div class="two-columns|<div class="sidebar-layout|<span|<div class="placeholder|<div class="article-content|<hr|<div class="interview-q|<div style="text-align:center|<div class="three-columns)'
    
    # Actually, a safer way to replace rubric-header without a complex regex is to parse with html.parser or just match the exact div structure if it's consistent.
    # The structure is:
    # <div class="rubric-header">
    #   <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
    #   <div class="header-content">
    #     <h2 style="...">Title</h2>
    #     <div class="rubric-sub">Subtitle</div>
    #   </div>
    #   <div class="header-page-num">4</div>
    # </div>
    
    # Let's use string manipulation to carefully replace it.
    
    new_html = html
    while '<div class="rubric-header">' in new_html:
        start_idx = new_html.find('<div class="rubric-header">')
        # Find the end of this div block
        # We know it contains 3 inner divs/imgs before closing
        end_idx = new_html.find('</div>', new_html.find('</div>', new_html.find('</div>', start_idx) + 1) + 1) + 6
        
        block = new_html[start_idx:end_idx]
        
        # Extract content
        h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', block)
        h2 = h2_match.group(1) if h2_match else ''
        
        sub_match = re.search(r'<div class="rubric-sub">(.*?)</div>', block)
        sub = sub_match.group(1) if sub_match else ''
        
        page_match = re.search(r'<div class="header-page-num">(.*?)</div>', block)
        page_num = page_match.group(1) if page_match else ''
        
        replacement = ''
        if h2:
            replacement += f'<h2 style="color: var(--navy-deep); font-family: var(--font-heading); font-size: 22pt; margin-bottom: 2mm;">{h2}</h2>\n'
        if sub:
            replacement += f'      <div style="font-family: var(--font-subheading); font-size: 10pt; color: var(--gold-warm); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4mm; border-bottom: 2px solid var(--gold-classic); padding-bottom: 2mm;">{sub}</div>\n'
        if page_num:
            # We add the page number at the end of the page inner later or just let the existing one handle it
            pass
            
        new_html = new_html[:start_idx] + replacement + new_html[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

process_file('revista/index.html')
process_file('revista/pages2.html')

print("Banners and segment badges removed.")

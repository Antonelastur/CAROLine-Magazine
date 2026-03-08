import re

with open('p4_full.txt', 'r', encoding='utf-8') as f:
    p4_text = f.read()

with open('p7.txt', 'r', encoding='utf-8') as f:
    p5_text = f.read()

def text_to_html(text):
    html = '<div class="article-content" style="column-count: 2; column-gap: 6mm; font-size: 10pt; line-height: 1.5; margin-top: 4mm;">\n'
    for p in text.split('\n'):
        p = p.strip()
        if not p: continue
        # Detect headings based on length or specific endings
        if (p.isupper() and len(p) > 3) or p.endswith(':-') or (len(p) < 60 and not p.endswith('.')):
            html += f'  <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">{p}</h3>\n'
        else:
            html += f'  <p style="margin-bottom: 2mm;">{p}</p>\n'
    html += '</div>'
    return html

p4_html = text_to_html(p4_text)
p5_html = text_to_html(p5_text)

with open('revista/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Page 4 article content
# Find <div class="article-content" under <section class="page" id="p4">
p4_start = html.find('<section class="page" id="p4">')
ac_p4_start = html.find('<div class="article-content"', p4_start)
# Find the end of this article content
# It ends right before the 5 FAPTE div
next_div_p4 = html.find('<div\n        style="background: linear-gradient(135deg, #fdfbf7, #f4ecd8)', ac_p4_start)
html = html[:ac_p4_start] + p4_html + '\n      ' + html[next_div_p4:]

# Replace Page 5 article content
p5_start = html.find('<section class="page" id="p5">')
ac_p5_start = html.find('<div class="article-content"', p5_start)
next_div_p5 = html.find('<div\n        style="background: linear-gradient(135deg, #fdfbf7, #f4ecd8)', ac_p5_start)
html = html[:ac_p5_start] + p5_html + '\n      ' + html[next_div_p5:]

# Change the 5 FAPTE titles to the requested ones
html = html.replace('5 FAPTE DESPRE\n          LICEUL DIN 1921', '5 CURIOZITA?I DESPRE LICEUL „PRINCIPELE CAROL”')
html = html.replace('5 FAPTE DESPRE LICEUL DIN 1921', '5 CURIOZITA?I DESPRE LICEUL „PRINCIPELE CAROL”')

html = html.replace('5 FAPTE\n          SURPRINZATOARE', '5 CURIOZITA?I DESPRE REGELE CAROL I')
html = html.replace('5 FAPTE SURPRINZATOARE', '5 CURIOZITA?I DESPRE REGELE CAROL I')

with open('revista/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

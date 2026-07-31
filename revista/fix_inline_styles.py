import re

html_path = 'c:/Users/Antonela/Desktop/Caroline/revista/pages2.html'
css_path = 'c:/Users/Antonela/Desktop/Caroline/revista/styles.css'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Identify all unique styles
styles = re.findall(r'style="(.*?)"', html_content)
# Keep their original order to maintain determinism, but remove duplicates
unique_styles = []
for style in styles:
    if style not in unique_styles:
        unique_styles.append(style)

# 2. Map styles to class names
style_to_class = {}
new_css_classes = '\n\n/* ── Extracted from pages2.html ── */\n'
for i, style in enumerate(unique_styles):
    # Give it a generic name or based on page
    class_name = f'inline-style-p2-{i+1}'
    style_to_class[style] = class_name
    
    new_css_classes += f'.{class_name} {{\n'
    props = style.split(';')
    for prop in props:
        if prop.strip():
            new_css_classes += f'    {prop.strip()};\n'
    new_css_classes += '}\n'

# 3. Replace in HTML
# If element already has a class attribute, append it
# e.g., class="card" style="..." -> class="card {class_name}"
# Else, just replace style="..." with class="{class_name}"
for style, class_name in style_to_class.items():
    # Regex to handle existing class attributes before or after style
    # Actually, simplest approach:
    # 1. replace class="xxx" style="YYY"
    # 2. replace style="YYY" class="xxx"
    # 3. replace style="YYY"
    
    # We can do this with a function
    pattern = re.compile(fr'(<[^>]*?)(class="([^"]*)")([^>]*?)(style="{re.escape(style)}")([^>]*?>)')
    
    def replacer(match):
        pre_class = match.group(1)
        classes = match.group(3)
        mid = match.group(4)
        style_attr = match.group(5)
        post = match.group(6)
        
        # New class string combined
        new_class_str = f'class="{classes} {class_name}"'
        return pre_class + new_class_str + mid + post

    html_content, count = pattern.subn(replacer, html_content)
    
    # Also handle style="..." before class="..."
    pattern2 = re.compile(fr'(<[^>]*?)(style="{re.escape(style)}")([^>]*?)(class="([^"]*)")([^>]*?>)')
    def replacer2(match):
        pre = match.group(1)
        mid = match.group(3)
        classes = match.group(5)
        post = match.group(6)
        
        return pre + f'class="{classes} {class_name}"' + mid + post
        
    html_content, count2 = pattern2.subn(replacer2, html_content)
    
    # And finally handle if there was NO class attribute
    if count == 0 and count2 == 0:
        html_content = html_content.replace(f'style="{style}"', f'class="{class_name}"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css_classes)

print("Styles extracted and replaced successfully.")

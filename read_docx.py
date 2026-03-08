import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Conținuturi', 'Distribuție pagini.docx')

z = zipfile.ZipFile(docx_path)
tree = ET.parse(z.open('word/document.xml'))
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
lines = []
for p in tree.findall('.//w:p', ns):
    text = ''.join(t.text or '' for t in p.findall('.//w:t', ns))
    if text.strip():
        lines.append(text)
z.close()

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'distributie_output.txt')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f"Written {len(lines)} lines to {out_path}")

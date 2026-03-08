import sys
import zipfile
import re

if len(sys.argv) < 3:
    print("Usage: python read_any_docx.py <in_file.docx> <out_file.txt>")
    sys.exit(1)

docx_path = sys.argv[1]
out_path = sys.argv[2]

try:
    z = zipfile.ZipFile(docx_path)
    xml_content = z.read('word/document.xml').decode('utf-8', errors='ignore')
    z.close()
    
    # Extract text from <w:p> elements roughly
    paragraphs = re.findall(r'<w:p[^>]*>(.*?)</w:p>', xml_content)
    text_content = []
    
    for p in paragraphs:
        # Extract all <w:t> tags from paragraph
        texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', p)
        text = ''.join(texts)
        if text.strip():
            text_content.append(text)
            
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_content))
    print(f"Wrote to {out_path}")
except Exception as e:
    print(f"Error reading docx: {e}")

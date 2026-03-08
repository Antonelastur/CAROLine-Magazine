import docx
import os

files = [
    r"c:\Users\Antonela\Desktop\Caroline\Conținuturi\DE CE ȘCOALA NOASTRĂ SE NUMEȘTE.docx",
    r"c:\Users\Antonela\Desktop\Caroline\Conținuturi\Principele Carol.docx"
]

for f in files:
    try:
        doc = docx.Document(f)
        text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        name = os.path.basename(f)
        with open(os.path.join(r"c:\Users\Antonela\Desktop\Caroline", name + ".txt"), "w", encoding="utf-8") as out:
            out.write(text)
        print(f"Extracted {len(text)} chars from {name}")
    except Exception as e:
        print(f"Error on {f}: {e}")

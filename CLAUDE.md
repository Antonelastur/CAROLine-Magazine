# CLAUDE.md — Revista CAROLine

Revistă școlară (Școala Gimnazială „Principele Carol"), realizată în layout HTML/CSS și
exportată ca PDF print/digital. Acest fișier ghidează munca asistentului la
machetare, procesare conținut și export — nu la creație editorială.

## Hartă foldere

**Sursă de adevăr:**
- `Conținuturi/` — texte sursă originale (.docx). „Distribuție pagini.docx" arată ce
  text merge pe ce pagină. Referință principală pentru orice conținut.
- `revista/index.html` + `revista/styles.css` — machetă activă, singurul fișier HTML
  de editat. Urmărit în git.
- `Brand kit/CAROLINE brand.docx` — identitate vizuală oficială.
- `Imagini/` — foto/ilustrații brute curate, folosite direct în machetă.

**Ignorate implicit (nu se citesc/procesează fără cerere explicită):**
- `scratch/` — scripturi și fișiere de lucru temporare, inclusiv încercări redundante
  de tunel (find_url.py, run_serveo.py, tunnel.py etc.).
- `.venv/` — mediu Python local, nu conținut de proiect.
- `extracted_images/` — imagini brute extrase din PDF-ul istoric (Anuar), se
  procesează doar când se lucrează explicit la pagina de arhivă.
- Media brută mare din rădăcină (`*.mp4`, PDF-uri >5MB precum
  `promotia 2017 - 2022 save.pdf`) — nu se deschid/citesc, doar se listează.
- `clean_revista/`, `revista.zip`, `clean_revista.zip` — derivate generate, **posibil
  învechite** (verifică mereu timestamp vs. `revista/index.html` înainte de a le
  folosi ca referință). Nu se editează direct; se regenerează din `revista/`.
- Scripturile „moarte" din martie (operează pe o versiune veche, cu 24 de pagini, a
  machetei — nu pe structura curentă): `read_docx.py`, `extract_docx.py`,
  `remove_banners.py`, `update_text.py`, `fix_magazine.py`, `fix_magazine2.py`,
  `restore_headers.py`, `fix_pages.py`, `verify_html.py`, `rebuild_pages.py`,
  `insert_content.py`, `update_p5_19_20.py`, `rebuild_skeleton.py`, `fix_p1_p2.py`.
  Idem reziduurile din `revista/`: `original_index.html`, `pages2.html`,
  `result*.txt`, `temp.css`, `fix_inline_styles.py`.

Dacă apare confuzie despre care folder e activ pe viitor (ex. dacă
`clean_revista/` începe să fie modificat direct), oprește-te și întreabă
înainte de a presupune.

## Flux de lucru curent (generare revistă)

`build_html.py` (generează blocurile HTML per pagină din texte sursă) →
`build_magazine_28.py` (asamblare intermediară, 28 pagini) →
`build_magazine_32.py` (asamblare finală, 32 pagini — ultimul rulat, reflectă
starea curentă a `revista/index.html`). Orice extindere/reparare a machetei
continuă din `build_magazine_32.py`, nu din scripturile din martie.

## Reguli de economie tokeni

- **Nu citești** fișiere din `scratch/`, `.venv/`, sau media brută (mp4, PDF-uri
  mari) decât dacă utilizatoarea cere explicit.
- **Nu recitești duplicate** de conținut (`scratch_*.txt`, variante `p4_out.txt`/
  `p4_full.txt`/`p4_utf8.txt` etc.) dacă docx-ul original din `Conținuturi/` e
  disponibil — sursa e docx-ul, nu extragerile intermediare.
- **Nu rulezi** scripturile „moarte" din martie (listate mai sus) — fluxul curent
  e `build_html.py` → `build_magazine_32.py`.
- **Ceri confirmare** înainte de a șterge sau muta orice fișier.

## Git

Nu există `.gitignore` — se creează/menține cu aceste excluderi:
```
*.mp4
*.pdf
.venv/
clean_revista/
*.zip
```
(PDF-urile mici, ex. surse text scanate din `Conținuturi/`, se evaluează caz cu caz —
regula de mai sus vizează în primul rând fișierele mari nefolosite din rădăcină.)
Nu rula `git add -A`/`git add .` fără verificare — riscă să adauge fișiere media de
GB-uri la istoric.

## MCP-uri conectate

- **Canva** — import/export machetă (`revista_canva_import.html`), generare design.
- **Google Drive** — backup/partajare conținut și foto.
- **Gmail / Google Calendar** — coordonare aprobări cu editor/director.

Restul conectorilor disponibili (Adobe, Microsoft 365, Notion, Zapier etc.) necesită
autentificare — nu presupune că sunt utilizabili fără să verifici cu `claude mcp list`.

## /compact și /clear

- Rulează `/compact` după finalizarea și confirmarea unei pagini/secțiuni din
  revistă.
- Rulează `/clear` la trecerea de la editare de text/conținut la procesare
  imagini sau lucru cu Canva (context diferit, nu are rost să persiste).

## Identitate vizuală — NON-NEGOCIABIL

**Culori (strict, nimic altceva):**
| Rol | Culoare |
|---|---|
| Fundal principal | Navy `#0A1E3D` / `#1A2B4A` |
| Logo, titluri principale | Auriu `#D4AF37` / `#C9A961` |
| Highlights, benzi rubrici | Galben `#F4C430` |

Interzis: roșu, verde intens, violet, roz sau orice culoare în afara paletei.

**Logo:** „CAROLine" cu coroană → obligatoriu pe copertă, cuprins,
contracopertă. Logo circular al școlii → copertă + header pagini. Nu se
modifică, recolorează sau distorsionează; nu se creează logo-uri alternative.

**Tipografie:** maximum 3 fonturi (1 titluri principale serif/decorativ,
1 titluri secundare sans-serif bold, 1 text body 10-12pt lizibil). Fără Comic
Sans/Papyrus/Brush Script. Maximum 2 stiluri bold pe pagină.

## Reguli de conținut

- **Nu inventa/scrie conținut editorial** — doar machetezi ce primești.
- **Nu corecta gramatical fără aprobare** — semnalează erorile grave, nu le
  repara singur.
- **Nu prescurta texte** fără acordul editorului; nu adăuga virgule, puncte,
  titluri din cont propriu.
- Foto elevi: doar inițiale sau „Clasa a V-a A", niciodată nume complete.
- Foto adulți (profesor, director): nume complet dacă e rol oficial.
- Include credite foto dacă sunt furnizate.
- Nu folosi stock photos sau imagini AI-generate pentru persoane/evenimente
  școlare reale — doar foto reale. Ilustrațiile decorative (backgrounds,
  separatoare) sunt permise.
- Cere întotdeauna confirmare înainte de a modifica/recadra poze existente.

## Reguli de imagini (dimensiune și optimizare)

- **Verifică dimensiunea fișierului înainte de orice procesare.** Peste 5 MB
  → STOP, nu încerca să procesezi direct imaginea mare.
- Dacă primești/întâlnești o imagine >5MB, răspunde în genul:
  > „Imaginea are [X] MB, dar pot procesa maxim 5 MB. Te rog:
  > redimensionează la maxim 2000x2000px, salvează ca JPEG calitate 80-85%,
  > încarcă din nou. Sau trimite-mi un link către imagine și o procesez eu."
- Dacă optimizezi tu însuți o imagine, folosește acest pattern (PIL/Pillow):
  redimensionare la maxim 2000px pe latura mare (`thumbnail`, `LANCZOS`),
  salvare JPEG cu `quality=85, optimize=True`, apoi verifică dimensiunea
  rezultată în MB înainte de a o folosi.
- Rezoluție recomandată pentru design: 2000×2000px.
- Rezoluție minimă pentru print: 300 DPI / minimum 3000x2400px pentru
  copertă.

## Reguli de layout

Obligatoriu: consistență între pagini, grid (nu poziționare „la ochi"),
minim 5mm white space între elemente, numerotare pagini clară, cuprins
funcțional, line-height minim 1.3.

Interzis: supraîncărcarea paginii, >2 fonturi pe aceeași pagină, text peste
imagini fără contrast suficient, efecte excesive (shadows/glows/3D), rânduri
orfane/văduve.

## Export — checklist minim

- **Print:** CMYK, 300 DPI, bleed 3mm, fonturi embedded/outlined, PDF/X-1a
  sau PDF/X-4. Nume fișier: `CAROLine_NrX_AAAA_PRINT.pdf`
- **Digital:** RGB, 150 DPI, sub 20MB, hyperlinks funcționale, testat pe
  mobil+desktop. Nume fișier: `CAROLine_NrX_AAAA_DIGITAL.pdf`
- Nu exporta fără aprobare finală explicită.

## Proces de lucru

Înainte de orice sarcină de design: confirmă că textele sunt finale, verifică
rezoluția fotografiilor, stabilește numărul de pagini (multiplu de 4) și
formatul de export cerut (print/digital/ambele).

Când ceva e ambiguu → întreabă, nu presupune. Când apare o problemă →
raportează și propune opțiuni concrete, nu decide singur.

**Formulări corecte (exemple):**
- ✅ "Ar trebui să includ logo-ul pe această pagină? Obișnuit apare doar pe copertă."
- ✅ "Fotografia e prea mică pentru spațiu. Pot fie să o micșorez cadrul, fie să folosesc alta."
- ✅ "Am observat că textul interviului e foarte lung. Îl împart pe 2 pagini sau reducem numărul de întrebări?"

**Formulări greșite (de evitat):**
- ❌ "Am pus logo-ul și aici pentru că arată mai bine."
- ❌ "Nu se poate, fotografia e prea mică."
- ❌ "Am tăiat ultimele 2 întrebări că nu încăpeau."

## Cazuri speciale

**Dacă lipsesc materiale:**
> „Lipsesc fotografiile pentru pagina 7 (Carolist de Nota 10). Pot fie:
> (A) Las spațiu gol marcat [PLACEHOLDER - FOTO]
> (B) Folosesc ilustrații decorative temporare
> (C) Aștept fotografiile și continui cu alte pagini
> Ce preferi?"

**Dacă conținutul e prea mult:**
> „Textul pentru 'Sub Reflector' are 2500 cuvinte, dar spațiul permite doar
> 1200. Soluții:
> (A) Împart pe 2 pagini (pagina 8-9)
> (B) Scad fontul de la 11pt la 10pt
> (C) Editorul prescurtează textul
> Ce alegeți?"

**Dacă calitatea e proastă:**
> „Fotografia pentru copertă are 640x480px, dar pentru print de calitate
> trebuie 3000x2400px. Nu pot folosi această imagine. Aveți altă fotografie
> sau facem o sesiune foto nouă?"

**Dacă feedback-ul e contradictoriu:**
> „Am primit:
> De la editor: 'Pune logo-ul mai mare'
> De la director: 'Logo-ul e prea mare'
> Pot organiza o întâlnire scurtă să aliniați viziunea sau fac 2 variante
> pentru vot?"

## Skill-uri disponibile (`.claude/skills/`)

- `pagina-noua` — generare pagină nouă în revistă dintr-un docx sursă.
- `export-canva` — export/import machetă în Canva.
- `curatare-scratch` — curățare fișiere scratch vechi.

## Notă despre `.agents/rules/Skills`

Fișierul `.agents/rules/Skills` conține un ghid de „skill-uri" (PDF export,
Canvas Design, Theme Factory, procesare DOCX, web design) scris pentru un
alt tool AI (Antigravity — textul menționează explicit „Save/Apply în
Antigravity") și se termină brusc, nefinalizat. **Nu e compatibil cu Claude
Code** în forma actuală și nu se auto-încarcă. Skill-urile reale, funcționale
în Claude Code, sunt cele din `.claude/skills/` (vezi secțiunea de mai sus) —
create separat, nu prin migrarea acestui fișier.

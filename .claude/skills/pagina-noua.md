# Skill: pagina-noua

Generare pagină nouă în revistă dintr-un docx sursă din `Conținuturi/`.

1. Verifică `Conținuturi/Distribuție pagini.docx` — ce text merge pe ce pagină.
2. Citește docx-ul sursă direct; nu folosi variante `scratch_*.txt` dacă docx-ul e disponibil.
3. Verifică rezoluția fotografiilor asociate (min. 300 DPI print) — cere altele dacă lipsesc/sunt mici.
4. Scrie blocul `<section class="page" id="pN">` în `revista/index.html`, urmând pattern-ul din `build_html.py` (`gen_header`, `gen_footer`, `page-inner`).
5. Respectă paleta de culori și tipografia din `CLAUDE.md` (NON-NEGOCIABIL).
6. Nu inventa/prescurta text editorial — doar machetezi ce ai primit.
7. Cere confirmare înainte de a suprascrie o pagină existentă.
8. După finalizare și confirmare → `/compact`.

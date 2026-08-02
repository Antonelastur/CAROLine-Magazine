---
name: export-canva
description: Export/import machetă între revista/index.html și Canva prin revista_canva_import.html, inclusiv checklist de export PDF final. Folosește acest skill pentru sincronizare cu Canva sau export print/digital.
---

Export/import machetă în Canva.

1. Compară timestamp `revista_canva_import.html` vs `revista/index.html` — dacă cel din urmă e mai nou, regenerează întâi.
2. Regenerare: rulează fluxul din `scratch/` (`embed_images_base64.py` → `build_optimized_import.py`), nu scripturi din martie.
3. Nu folosi `clean_revista/` sau `.zip`-urile ca sursă — pot fi versiuni vechi.
4. Urcă `revista_canva_import.html` într-un loc accesibil public prin HTTPS (ex. Google Drive cu link public, Netlify, Vercel) — `import-design-from-url` NU poate accesa fișiere locale de pe disc (`C:\...`).
5. Cere confirmarea explicită a utilizatoarei înainte de a face public/upload orice fișier (regulă de securitate).
6. Import în Canva prin MCP-ul conectat (`import-design-from-url` / `upload-asset-from-url`).
7. Verifică vizual în Canva că paleta navy/auriu și logo-urile sunt intacte.
8. Cere aprobare finală explicită înainte de orice export PDF (print sau digital).
9. La trecerea de la editare text la acest pas → `/clear`.

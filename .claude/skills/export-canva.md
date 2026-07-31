# Skill: export-canva

Export/import machetă în Canva.

1. Compară timestamp `revista_canva_import.html` vs `revista/index.html` — dacă cel din urmă e mai nou, regenerează întâi.
2. Regenerare: rulează fluxul din `scratch/` (`embed_images_base64.py` → `build_optimized_import.py`), nu scripturi din martie.
3. Nu folosi `clean_revista/` sau `.zip`-urile ca sursă — pot fi versiuni vechi.
4. Import în Canva prin MCP-ul conectat (`import-design-from-url` / `upload-asset-from-url`).
5. Verifică vizual în Canva că paleta navy/auriu și logo-urile sunt intacte.
6. Cere aprobare finală explicită înainte de orice export PDF (print sau digital).
7. La trecerea de la editare text la acest pas → `/clear`.

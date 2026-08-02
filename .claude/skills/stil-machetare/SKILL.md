---
name: stil-machetare
description: Rețeta completă de stil vizual (culori exacte, tipografie, structură header/footer, tratarea imaginilor, verificare obligatorie) pentru machetarea revistei CAROLine. Referință obligatorie la orice modificare de machetă, pe oricare din cele 32 de pagini.
---

Rețeta de stil vizual pentru `revista/index.html` + `revista/styles.css` — măsurată direct din designul Canva „CAROLine" (sursa de adevăr confirmată). Referință **obligatorie** pentru orice modificare de machetă, pe oricare din cele 32 de pagini.

## 1. Culori exacte (hex)

| Element | Valoare |
|---|---|
| Fundal header/footer | `#122849` (navy **plat** — niciun gradient) |
| Text auriu pe navy (titlu, nr. pagină, footer) | `#D6C3A1` / `#CBC2AD` |
| Fundal casetă-citat (`.pull-quote`) | `#FDF8F0` (crem cald) |
| Bară accent lângă citate | `#F47E57` (corai) |
| Fundal pagină | `#FFFFFF` |

Variabile CSS deja definite în `:root`: `--navy-deep`, `--gold-canva`, `--gold-canva-num`, `--cream-quote`, `--coral-accent`, `--header-underline`. Folosește-le mereu prin `var(...)`, nu hexuri hardcodate noi.

## 2. Tipografie

- Titluri (`h2` în `.rubric-header`): `var(--font-heading)`, `font-variant: small-caps`.
- Corp de text (`p`, `.body-text`, `--font-body`): **serif** (Merriweather/Georgia) — niciodată sans-serif.
- Font-size body: **minim 10pt** pe pagini normale. Sub 10pt (9pt/9.5pt) doar dacă e singura variantă de încăpere pe o pagină densă, și doar cu confirmare explicită — nu implicit.

## 3. Structură header/footer (regulă critică)

- Header **și** footer: edge-to-edge (bleed complet, lățimea paginii), identice ca structură pe toate cele 32 de pagini.
- **Ambele** trebuie să aibă linie de demarcație gri închis (`var(--header-underline)`, `#9AA4B2`) față de restul conținutului — nu doar header-ul.
- Număr de pagină: `var(--font-heading)`, **~55-60pt** (`.header-page-num` din CSS: `58pt`), colț dreapta-sus în header.
- Footer: doar text centrat „CAROLine - NR. 1" (sau varianta curentă de footer-text), **fără număr de pagină repetat** (`.footer-page-num { display: none; }`).
- **Footer-ul trebuie să fie chiar la marginea de jos a paginii fizice, nu doar sub conținut.** `.page-footer` e `position: absolute; bottom: 0`, dar containerul lui de referință e `.page-inner` (are `position: relative`), nu `.page`. De aceea `.page-inner` trebuie să aibă `min-height: var(--page-height)` (nu `calc(page-height - 2*margin)` — cu `box-sizing: border-box` global, scăderea marginii de două ori lasă un gol de exact `2 × page-margin` sub footer, invizibil pe pagini cu conținut bogat, dar vizibil ca bandă albă pe pagini cu conținut puțin, sub bara footer-ului).
- Logo header: `.header-logo`, cerc **72px** (mărit ~10% față de valoarea inițială de 65px, la cererea explicită a utilizatoarei).
- Titluri header (`h2`, `.rubric-sub`): **aliniate la stânga**, imediat lângă logo (`text-align: left`, fără centrare) — nu centrate în bandă.

✅ **Stare conformă** (verificat vizual, Edge headless + eșantionare de pixeli pe imaginea PNG): footer lipit de marginea reală a paginii, cu linia de demarcație (`::before` gri + `::after` auriu) simetrică cu cea de sub header, edge-to-edge — confirmat pe pagini cu conținut sărac (P8, P24) unde defectul era vizibil, nu doar pe pagini cu conținut bogat.

## 4. Tratarea imaginilor

- Fotografii reale (nu placeholder): `.framed-photo` — chenar auriu simplu (linie fină, `var(--gold-classic)`), cu `.photo-caption` italic dedesubt.
- Rezoluție minimă: 2000×2000px pentru design/digital; 300 DPI sau minimum 3000×2400px pentru elemente destinate print (copertă etc.).

## 5. Verificare obligatorie înainte de a considera o pagină „gata"

1. Generează screenshot real (Edge headless, `msedge --headless=new --disable-gpu --screenshot=...`) și **verifică vizual** — nu te baza doar pe citirea codului.
2. Confirmă edge-to-edge pe header și footer.
3. Confirmă linia de demarcație gri pe **ambele** (header + footer).
4. **Pe pagini cu conținut puțin** (placeholder, galerie foto, pagini scurte), nu te baza doar pe privirea rapidă a screenshot-ului pentru poziția footer-ului — eșantionează culoarea de pixel pe verticală (PIL `im.getpixel((x,y))`) lângă marginea de jos, ca să confirmi că tranziția navy→gri (canvas) e directă, fără bandă albă de „pagină" între ele. Ochiul liber poate rata un gol de 20-25mm pe o imagine mică.
5. Caută stiluri inline care contrazic `styles.css` (culori/fonturi/mărimi hardcodate direct în `index.html`).
6. Caută conținut „scurs" din altă pagină — blocuri `.rubric-header` sau body dublate/suprapuse (bug de duplicare între secțiuni `<section id="pN">`).

## 6. Greșeli deja întâlnite — de evitat

- Gradient (`linear-gradient(navy-deep, navy-medium)`) în loc de navy plat pe header.
- Font sans-serif (Open Sans) pentru body text.
- Footer fără linie de demarcație.
- Casete-citat cu fundal gri neutru (`--gray-light`) în loc de crem cald (`--cream-quote`).
- Markup HTML duplicat/suprapus între pagini — bloc `.rubric-header` sau conținut de pagină copiat greșit dintr-o altă secțiune (`<section id="pN">`), cauzând titluri/numere de pagină străine vizibile pe pagina greșită.
- `.page-inner { min-height: calc(page-height - 2*margin) }` cu `box-sizing: border-box` global — lasă footer-ul „suspendat" cu un gol alb de `2×page-margin` dedesubt, invizibil pe pagini pline, vizibil pe pagini scurte. Corect: `min-height: var(--page-height)` direct.
- Logo mic (65px) cu titlu centrat în bandă — actualizat la logo 72px + titluri aliniate stânga, lângă logo (vezi secțiunea 3).

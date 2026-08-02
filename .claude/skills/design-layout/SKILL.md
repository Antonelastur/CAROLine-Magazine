---
name: design-layout
description: Principii de compoziție și layout editorial pentru revista CAROLine — grilă de coloane, ierarhie vizuală, plasarea imaginilor, umplerea paginii, tipare de layout reutilizabile. Complementar cu stil-machetare (acesta acoperă aranjarea conținutului, nu identitatea vizuală).
---

Principii de compoziție și layout editorial pentru revista CAROLine (A4, 210×297mm, HTML/CSS). Skill complementar cu `stil-machetare` (identitate vizuală) — acesta acoperă **cum se aranjează conținutul pe pagină**, nu cum arată elementele individuale.

Bazat pe practici editoriale profesionale (surse: FlipLink, BAS Big Graphics / Azura Magazine, iPixel, Walsworth, Envato Tuts+).

---

## 1. Sistemul de grilă

### Grila de coloane
- **Standard CAROLine**: grilă de **3 coloane** (cea mai flexibilă — funcționează atât pentru pagini dense, cât și pentru pagini mixte text+foto).
- Gutter (spațiu între coloane): **5–6mm** (nu mai puțin de 4mm, nu mai mult de 8mm).
- Margini exterioare: definite global prin `--page-margin` din `styles.css` — nu le modifica inline.
- Un element poate ocupa 1, 2 sau toate 3 coloanele — dar aliniază-l mereu la grila de coloane, nu la valori arbitrare.

### Grila de bază (baseline grid)
- Incrementul grilei de bază = leading-ul textului body (ex.: body la 10pt cu leading 14pt → grila = 14pt).
- Toate liniile de text, din orice coloană, trebuie să cadă pe aceeași grilă verticală — altfel pagina pare „dezaliniată".

### Variante de grilă per tip de pagină
| Tip pagină | Coloane recomandate | Observații |
|---|---|---|
| Articol narativ lung | 2 coloane | Coloană de text largă = lectură confortabilă |
| Articol scurt + fotografii | 2 coloane asimetrice (60/40 sau 65/35) | Text dominant + coloana îngustă pt. foto/citate |
| Galerie foto | 1–3 coloane | Modulare: grid cu rânduri egale |
| Portret de clasă / grup | 2 coloane asimetrice | Text într-o coloană, foto stivuite în cealaltă |
| Manifest / text dens | 2–3 coloane egale | Permite text mai scurt pe linie = citire mai ușoară |
| Citate / Vocea elevilor | 1–2 coloane | Spațiu generos, casete separate |

---

## 2. Ierarhia vizuală (ce vede ochiul primul)

Ordinea naturală a privirii pe o pagină (pattern Z / Gutenberg):
1. **Colțul stânga-sus** → titlu / header (zona de aterizare)
2. **Diagonal spre dreapta** → element dominant (foto hero, ilustrație)
3. **Stânga-jos** → corp de text
4. **Dreapta-jos** → element de închidere (semnătură, credit, caption)

### Reguli de ierarhie
- **Un singur element dominant per pagină** — fie o fotografie mare (hero), fie un titlu mare. Nu două elemente care concurează.
- Elementul dominant trebuie să fie vizibil mai mare decât orice altceva (minim 1.5× dimensiunea celorlalte imagini).
- **Titlul articolului** e al doilea element ierarhic — mai mare decât subtitlul, care e mai mare decât textul body.
- Pull-quotes / citate evidențiate rup monotonia textului dens și creează un al treilea nivel de interes.

### Scara tipografică (pentru HTML/CSS pe A4)
| Element | Dimensiune | Observații |
|---|---|---|
| Titlu articol (`h3`) | 13–18pt | Pe o pagină — nu mai mare decât header-ul rubricii |
| Subtitlu / deck | 10–12pt, italic | Sub titlu, cu culoare atenuată |
| Corp text (`p`) | 10pt (standard) / 9–9.5pt (pagini dense) | Leading: 1.4–1.5 |
| Pull-quote | 14–18pt | Evidențiat vizual (casetă, bară accent, font diferit) |
| Caption foto | 7–8pt | Italic, sub imagine |
| Credit autor / semnătură | 8–9pt | Bold, aliniat dreapta |
| Folio (nr. pagină, footer) | 7–8pt | În header/footer |

---

## 3. Plasarea imaginilor — reguli concrete

### Dimensionare
- **O imagine dominantă** per pagină, care ocupă minim 40% din spațiul util (fără header/footer).
- Imaginile de suport: maxim 30–40% din suprafața imaginii dominante.
- **Variație de scală** = cel mai puternic instrument de contrast. Fotografii identice ca dimensiune = layout plat, fără ritm.

### Tehnici de plasare
1. **Full-width** (toată lățimea zonei de conținut): pentru foto hero — maximum 1 per pagină.
2. **Coloană dedicată**: foto stivuite vertical într-o coloană laterală — fiecare foto ocupă toată lățimea coloanei.
3. **Inline / plutitoare**: foto intercalată în text, cu `text-wrap` (în CSS: float sau grid cu text care curge).
4. **Bleed** (margine la margine): extindere peste margini — doar pentru impact maxim, rar.

### Wrap text în jurul imaginii
- Offset minim de wrap: **3–5mm** între marginea imaginii și text — consistență pe toată pagina.
- Textul nu trebuie să ajungă sub 25mm lățime lângă o imagine — devine ilizibil. Dacă e prea îngust, trece imaginea pe lățime completă.

### INTERZIS: trunchierea fotografiilor (REGULĂ ABSOLUTĂ)
- **NU folosi `object-fit: cover`** — taie din fotografie, pierde conținut vizual. Elevii, profesorii și părinții vor să vadă TOATĂ fotografia, nu o decupare arbitrară.
- Folosește **`object-fit: contain`** — se vede toată imaginea, fără tăiere, fără deformare.
- Dacă `contain` lasă benzi laterale (letterbox), pune `background: var(--cream-quote)` sau `background: #f5f0e4` pe containerul `.framed-photo` pentru a umple vizual spațiul.
- Alternativa: dimensionează containerul proporțional cu imaginea (`aspect-ratio`) în loc să forțezi o înălțime fixă.
- Aceasta e o cerință explicită a utilizatoarei. Nu o ignora niciodată.

### Caption
- **Întotdeauna** sub imagine, nu deasupra și nu lateral.
- Aliniat la marginea stângă a imaginii.
- Font italic, 7–8pt, cu `var(--navy-medium)` sau gri.

### Aliniere bloc text + fotografie
Când text și foto sunt alăturate (coloană dedicată sau grid asimetric), ultima
linie a textului trebuie să se alinieze aproximativ cu marginea de jos a
fotografiei — nu lăsa fotografia sau textul să se termine mult mai sus/jos
decât celălalt, creează aspect dezechilibrat. Ajustează dimensiunea foto sau
spațierea textului (line-height, padding) pentru a obține alinierea, nu
trunchia conținutul.

### Spațiere consistentă între blocuri
Toate blocurile de conținut de pe o pagină (paragrafe, casete, citate,
secțiuni) trebuie să aibă spații verticale aproximativ EGALE între ele — nu
variabile de la un bloc la altul. Stabilește o valoare standard (ex.
`margin-top: 4mm`, consistent cu grila de bază a paginii) și aplic-o uniform,
în loc să ajustezi ad-hoc spațiul de la caz la caz. Excepție: spațiere
intenționat mai mare înainte/după un element dominant, pentru a-l separa
vizual — dar și acolo, valoarea trebuie să fie consistentă pe toate paginile
care au acest tip de element.

---

## 4. Umplerea paginii — eliminarea spațiului gol (REGULA CRITICĂ)

Aceasta e problema recurentă. Reguli:

### Principiul fundamental
**Conținutul trebuie să umple toată zona utilă** (de la baza header-ului până la vârful footer-ului). Spațiul gol la baza paginii nu e „white space" — e eroare de layout.

### Strategii CSS pentru umplere completă

#### A. Pagini cu text + colțar foto (layout asimetric)
```css
.article-content {
  display: grid;
  grid-template-columns: 1.6fr 0.4fr; /* sau 1.5fr 0.5fr */
  gap: 6mm;
  /* CRITIC: forțează înălțimea să umple tot spațiul disponibil */
  flex: 1; /* dacă .page-inner e flex column */
}
```
Containerul exterior (`.page-inner`) trebuie să fie `display: flex; flex-direction: column;` și zona de conținut trebuie să aibă `flex: 1` ca să ocupe tot spațiul rămas după header.

#### B. Fotografi stivuite vertical într-o coloană
```css
.photo-sidebar {
  display: grid;
  grid-template-rows: repeat(N, 1fr); /* N = numărul de fotografii */
  gap: 3mm;
  height: 100%; /* umple containerul părinte */
}
.photo-sidebar .framed-photo {
  min-height: 0; /* permite grid-ului să comprima sub dimensiunea naturală */
  overflow: hidden;
}
.photo-sidebar .framed-photo img {
  width: 100%;
  height: 100%;
  object-fit: contain; /* NICIODATĂ cover — nu trunchia fotografiile */
}
.photo-sidebar .framed-photo {
  background: var(--cream-quote); /* umple vizual spațiul dacă contain lasă benzi */
}
```

#### C. Pagini cu text pur (manifest, eseuri lungi)
- Folosește `column-count: 2` sau `3` — textul se distribuie automat.
- Dacă textul nu umple pagina: mărește font-size (10pt → 11pt), crește leading (1.4 → 1.6), adaugă `column-gap` mai mare, sau intercalează un pull-quote / un element decorativ (linie, casetă, inițială drop-cap).

#### D. Pagini cu puțin conținut
- **Nu lăsa spațiu gol** — redistribuie conținutul sau adaugă elemente vizuale:
  - Mărește imaginea hero
  - Adaugă un pull-quote din text
  - Adaugă o casetă info / un fact-box
  - Mărește spațiul între elemente **uniform** (nu doar la bază)
- Ultima soluție: `justify-content: space-between` pe containerul flex vertical, distribuind spațiul egal între blocuri.

### Verificare finală
După orice layout, întreabă-te:
1. **Există bandă albă între ultimul element de conținut și footer?** → Eroare. Repară.
2. **Fotografiile au dimensiuni identice fără variație?** → Layout plat. Variază.
3. **Textul e într-o singură coloană pe toată lățimea?** → Probabil prea larg. Împarte în coloane sau adaugă imagini laterale.

---

## 5. Ritmul paginilor (pacing)

- **Alternează** pagini dense (text) cu pagini deschise (foto, spațiu).
- Nu pune două pagini de text pur una lângă alta — intercalează o pagină cu element vizual dominant.
- O revistă profesională are un ritm de tip „respirație": pagina deschisă (intro vizual) → pagini medii (conținut) → pagină de culminare (fotografie mare / pull-quote) → pagină de închidere (text, credite).

---

## 6. Tipare de layout (rețete reutilizabile)

### Tipar A: Articol narativ cu fotografie hero
```
┌──────────────────────────┐
│ [HEADER - rubrica]       │
├──────────────────────────┤
│ ┌──────────────────────┐ │
│ │   FOTO HERO (full)   │ │
│ └──────────────────────┘ │
│ Caption foto              │
│                           │
│ ┌─────────┐ ┌──────────┐ │
│ │ Text    │ │ Text     │ │
│ │ col. 1  │ │ col. 2   │ │
│ │         │ │          │ │
│ └─────────┘ └──────────┘ │
│          Semnătura        │
├──────────────────────────┤
│ [FOOTER]                 │
└──────────────────────────┘
```

### Tipar B: Text + coloană de fotografii (lateral)
```
┌──────────────────────────┐
│ [HEADER - rubrica]       │
├──────────────────────────┤
│ Titlu articol             │
│ ┌───────────┐ ┌────────┐ │
│ │           │ │ Foto 1 │ │
│ │  Text     │ ├────────┤ │
│ │  principal│ │ Foto 2 │ │
│ │  (1 col)  │ ├────────┤ │
│ │           │ │ Foto 3 │ │
│ │           │ ├────────┤ │
│ │ Semnătura │ │ Foto 4 │ │
│ └───────────┘ └────────┘ │
├──────────────────────────┤
│ [FOOTER]                 │
└──────────────────────────┘
```
- Raport coloane: **60-65% text / 35-40% foto**.
- Fotografiile păstrează proporțiile naturale (niciodată `cover` sau stretch).
- Dacă fotografiile nu umplu coloana, redistribuie-le în jurul textului (vezi Tipar F).

### Tipar C: Galerie de artă / expoziție
```
┌──────────────────────────┐
│ [HEADER - rubrica]       │
├──────────────────────────┤
│                           │
│    ┌──────────────────┐   │
│    │                  │   │
│    │  OPERA CENTRALĂ  │   │
│    │  (max 60% lățime)│   │
│    │                  │   │
│    └──────────────────┘   │
│    Caption + credit       │
│                           │
├──────────────────────────┤
│ [FOOTER]                 │
└──────────────────────────┘
```
- Opera centrată, cu spațiu generos în jur — respectă opera, nu o înghesui.
- Dacă sunt mai multe opere: grid modular 2×2 sau 3×2, cu caption sub fiecare.

### Tipar D: Citate / Vocea elevilor
```
┌──────────────────────────┐
│ [HEADER - rubrica]       │
├──────────────────────────┤
│ ┌────────────────────┐   │
│ │ CASETĂ CITAT 1     │   │
│ │ „text..."          │   │
│ │ — Elev, clasa      │   │
│ └────────────────────┘   │
│                           │
│ ┌────────────────────┐   │
│ │ CASETĂ CITAT 2     │   │
│ │ „text..."          │   │
│ │ — Elev, clasa      │   │
│ └────────────────────┘   │
│        ...                │
├──────────────────────────┤
│ [FOOTER]                 │
└──────────────────────────┘
```

### Tipar F: Text cu fotografii intercalate (wrap-around)
```
┌──────────────────────────┐
│ [HEADER - rubrica]       │
├──────────────────────────┤
│ Titlu articol             │
│ ┌────────┐                │
│ │ Foto 1 │ Text text text │
│ │        │ text text text │
│ └────────┘ text text text │
│ text text text text text  │
│                ┌────────┐ │
│ text text text │ Foto 2 │ │
│ text text text │        │ │
│ text text text └────────┘ │
│ ┌────────┐ ┌────────┐    │
│ │ Foto 3 │ │ Foto 4 │    │
│ └────────┘ └────────┘    │
│        Semnătura          │
├──────────────────────────┤
│ [FOOTER]                 │
└──────────────────────────┘
```
- Fotografiile **plutesc** (`float: left`/`right`) în jurul textului, alternând stânga/dreapta.
- Fiecare foto la **proporții naturale** — niciodată trunchiată sau deformată.
- Dimensionare: `width: 45–50%` din lățimea conținutului, `height: auto`.
- `margin: 0 4mm 3mm 0` (float left) sau `margin: 0 0 3mm 4mm` (float right) — spațiu între foto și text.
- Fotografiile care rămân la final (sub text) se pun pe un rând orizontal (`display: flex; gap: 3mm`).
- **Regula de umplere**: distribuie fotografiile uniform pe verticală — nu le înghesui pe toate sus sau toate jos. Obiectivul e ca textul + fotografiile împreună să acopere toată pagina fără goluri.

### Tipar E: Text dens (manifest, regulament)
- 2–3 coloane egale cu `column-count`.
- Subtitluri bold la fiecare secțiune.
- Eventual o inițială drop-cap la începutul textului.
- `text-align: justify` cu `hyphens: auto` (dacă limba permite).

---

## 7. Greșeli de layout de evitat

1. **Spațiu gol la baza paginii** — cea mai frecventă eroare. Conținutul trebuie să se întindă până la footer.
2. **Fotografii toate la aceeași dimensiune** — creează monotonie. Variază scara.
3. **Text pe toată lățimea fără coloane** — linia prea lungă (>80 caractere) e greu de citit. Împarte în coloane sau adaugă margine laterală.
4. **Prea multe elemente concurente** — un titlu mare + o foto mare + un pull-quote mare pe aceeași pagină = haos. Un singur element dominant.
5. **Fotografii în gutter** (zona de pliere) — pe print, fețele tăiate la îndoire. Ține elementele importante departe de centrul spread-ului.
6. **Orfani și văduve** — un cuvânt singur pe ultima linie a unui paragraf (`orphans: 2; widows: 2` în CSS).
7. **Margini inconsistente** — toate paginile trebuie să aibă aceleași margini. Nu inventa margini per pagină.
8. **Fotografie trunchiată sau distorsionată** — mereu `object-fit: contain`, niciodată `cover` (taie) sau stretching fără proporții. Fotografiile trebuie vizibile integral.

---

## 8. Procedură de lucru la macheta unei pagini noi

1. **Identifică tipul de conținut**: text lung? text + foto? galerie? citate? → alege tiparul potrivit din secțiunea 6.
2. **Inventariază conținutul**: câte paragrafe de text? câte fotografii? câte citate? → determină densitatea paginii.
3. **Alege grila**: 2 coloane egale / 2 asimetrice / 3 coloane / full-width → pe baza tipului.
4. **Plasează elementul dominant** (foto hero sau titlu) — acesta ancorează pagina.
5. **Distribuie restul** în grilă, respectând ierarhia (titlu > text > caption > credit).
6. **Verifică umplerea**: containerul de conținut trebuie să aibă `flex: 1` sau `height: 100%` — fără bandă albă la bază.
7. **Screenshot + verificare vizuală** (conform `stil-machetare`, secțiunea 5).

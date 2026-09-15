# AGENDA, planul aplicației

Agendă interactivă a profesorului pentru un an școlar întreg, cu generare automată
a celor 53 de săptămâni și 12 luni pornind de la o singură dată introdusă manual.

Document de planificare. Nu conține cod de implementare.

---

## 1. Ce rezolvă aplicația

Problema concretă: informația despre un an școlar stă acum împrăștiată în caiete,
fișiere Excel separate pe clase, catalog, mesaje cu părinții și hârtii de la
secretariat. Duminica se pierde în recuperarea acestei informații, nu în munca
propriu-zisă.

Aplicația adună totul într-un singur loc și automatizează exact partea mecanică:
datele calendaristice, mediile, totalurile de absențe, rapoartele pe modul.

### Ce automatizează (mecanic, sigur)
- generarea calendarului: 53 de săptămâni, 12 luni, încadrarea pe module
- completarea datelor în fiecare fișă săptămânală și lunară
- calculul mediilor pe modul și pe an, după o regulă configurabilă
- totalurile de absențe, întârzieri, absențe motivate și nemotivate
- statistica pe clasă: număr de note per elev, elevi cu medii sub un prag, elevi
  fără număr minim de note
- exportul în PDF și Excel

### Ce NU automatizează (rămâne decizia profesorului)
- conținutul planificării calendaristice, competențele, unitățile de învățare
- nota efectivă, calificativul, aprecierea la purtare
- textul comunicării cu părinții

---

## 2. Decizia de platformă

Trei variante realiste, comparate pe criteriile care contează aici.

| Criteriu | A. Excel sau Google Sheets | B. Aplicație web React, local-first | C. Aplicație web cu server și cont |
|---|---|---|---|
| Timp până la prima versiune utilizabilă | 1 la 2 săptămâni de lucru pe seară | 4 la 6 săptămâni | 8 la 12 săptămâni |
| File interactive, navigare în câteva clicuri | limitat, hyperlink-uri între foi | complet controlabil | complet controlabil |
| Generare automată a 53 de săptămâni | posibil cu formule, fragil la editare | curat, o funcție de calendar | curat |
| Calcul medii | formule vizibile, ușor de stricat accidental | logică testabilă, protejată | idem |
| Funcționare offline, la școală, fără net | da (Excel desktop) | da, prin PWA | nu, fără conexiune |
| Date personale ale elevilor | rămân pe calculatorul tău | rămân în browserul tău | ajung pe un server, apar obligații GDPR serioase |
| Folosire pe telefon sau tabletă | greoi | bună, se instalează ca aplicație | bună |
| Cost recurent | zero | zero | hosting și bază de date |
| Partajare cu alți profesori | prin fișier | prin export sau, mai târziu, sincronizare | nativ |

**Recomandare: varianta B.**

Motivele:
1. Datele despre minori (note, absențe, purtare, observații, comunicare cu
   părinții) rămân local, în browserul tău, nu pe un server. Asta elimină cea mai
   grea parte a discuției GDPR. Dacă datele ajung pe un server, școala devine
   operator de date, ai nevoie de temei legal, informare, contract de
   împuternicire cu furnizorul de hosting. Pentru o unealtă personală nu merită.
2. Ai deja HTML, CSS, JavaScript și React, deci construiești fără dependență de
   altcineva.
3. PWA înseamnă că o instalezi pe laptop și pe telefon, funcționează în clasă fără
   internet, și arată ca o aplicație, nu ca un fișier Excel.

Varianta A rămâne valabilă ca soluție de tranziție, dacă vrei ceva funcțional
pentru anul acesta școlar cât timp construiești varianta B.

Varianta C devine interesantă doar dacă, mai târziu, aplicația se extinde la mai
mulți profesori din școală. Atunci se discută separat, cu directorul și cu
responsabilul de protecția datelor.

---

## 3. Stiva tehnică propusă (varianta B)

| Strat | Alegere | De ce |
|---|---|---|
| Build | Vite | pornire rapidă, configurare minimă |
| UI | React cu TypeScript | TypeScript prinde erorile de model de date înainte să ajungă în catalog |
| Stil | Tailwind CSS | consistență vizuală fără fișiere CSS care cresc necontrolat |
| Stare | Zustand | simplu, fără ceremonia Redux |
| Stocare | IndexedDB prin Dexie | mii de note și absențe fără limita de 5 MB a localStorage |
| Date calendaristice | date-fns | calcule pe săptămâni ISO, fără surprize la trecerea anului |
| Export Excel | SheetJS sau ExcelJS | catalogul se poate deschide și în afara aplicației |
| Export PDF | CSS de print plus fereastra de tipărire a browserului | control total asupra aspectului, fără bibliotecă grea |
| Offline | Vite PWA plugin | instalare pe desktop și telefon, funcționare fără net |
| Teste | Vitest | obligatoriu pentru motorul de calendar și pentru calculul mediilor |

---

## 4. Modelul de date

Șapte entități de bază. Numele sunt în română pentru că domeniul este românesc și
citirea codului rămâne clară.

### 4.1 An școlar
```
AnScolar {
  id
  denumire            // "2026-2027"
  primaZiDeLuni       // data introdusă de tine, punctul de pornire
  modele              // preset ales: gimnaziu, primar, liceu
  module[]            // 5 module: { numar, dataStart, dataFinal }
  vacante[]           // { denumire, dataStart, dataFinal }
  saptamaniSpeciale[] // Săptămâna verde, Școala altfel: { denumire, saptamanaId }
  zileLibere[]        // sărbători legale și zile libere locale
}
```

### 4.2 Săptămână (generate automat, 53)
```
Saptamana {
  numar               // 1 la 53
  numarISO            // numărul ISO din calendar, util la raportări
  dataStart           // luni
  dataFinal           // duminică
  modulId             // sau null dacă este vacanță
  tip                 // curs | vacanta | speciala | inainte_de_an | dupa_an
  esteSaptamanaDeCurs // boolean derivat
}
```

### 4.3 Clasă și elev
```
Clasa {
  id, denumire        // "V A"
  disciplina          // "Limba și literatura română" sau "Limba spaniolă"
  nrOreSaptamana
  esteDiriginte       // schimbă ce secțiuni apar pentru clasa asta
  anScolarId
}

Elev {
  id, clasaId
  nume, prenume
  initiale            // generate automat, folosite în rapoartele publice
  dataNasterii        // opțional
  observatii
  contactParinte      // nume, telefon, email, relație
  activ               // pentru transferuri în timpul anului
}
```

### 4.4 Orar
```
IntrareOrar {
  clasaId
  zi                  // 1 la 5
  ora                 // 1 la 7
  sala
}
```
Orarul este piesa care face posibilă completarea automată. Din el rezultă ce clase
apar în fișa fiecărei zile, câte ore ai pe săptămână și unde se pot marca absențe
pe oră.

### 4.5 Evaluare
```
Nota {
  id, elevId, clasaId
  valoare             // 1 la 10, sau calificativ: FB, B, S, I
  data
  modulId             // dedus automat din dată
  tip                 // oral | scris | test | practic | proiect | portofoliu
  observatie
  contorizataInMedie  // permite note informative, necontorizate
}

Absenta {
  id, elevId, clasaId
  data, ora
  tip                 // absenta | intarziere
  motivata            // boolean
  documentMotivare    // text scurt: adeverință, cerere părinte
}

Purtare {
  elevId, modulId
  nota                // sau calificativ
  implicare           // scor 1 la 5, uz intern, nu apare în catalog
  incidente[]         // { data, descriere, masura }
}
```

### 4.6 Planificare
```
UnitateInvatare {
  id, clasaId
  denumire
  competenteSpecifice[]
  continuturi
  nrOre
  saptamani[]         // intervalul de săptămâni alocat
  resurse
  evaluare
  observatii          // coloana de ajustări din planificarea reală
}

PlanificareSaptamanala {
  saptamanaId, clasaId
  lectii[]            // { ora, titlu, competente, resurse, tema, realizat }
  note                // ce a rămas nefăcut, ce se mută
}
```

### 4.7 Activități și comunicare
```
Activitate {
  id, data
  tip                 // suplinire | lucrare | sedinta | consiliu |
                      // serviciu_scoala | curs_formare | proiect_erasmus | altele
  titlu, descriere
  clasaId             // opțional
  status              // planificat | realizat | anulat
  documentAsociat
}

Comunicare {
  id, elevId
  data
  canal               // consultatie | telefon | email | sedinta_parinti | mesaj
  subiect
  rezumat
  urmare              // ce s-a stabilit, termen
  rezolvat
}

Notita {
  id, data, categorie, titlu, continut, fixata
}

FisaElev {
  elevId
  // vedere agregată, nu entitate separată: adună note, absențe, purtare,
  // comunicare și observații într-un singur ecran printabil
}
```

---

## 5. Motorul de calendar, inima aplicației

Aceasta este funcția centrală. Restul aplicației depinde de ea, deci se scrie
prima și se testează cel mai serios.

**Intrare:** o singură dată, prima zi de luni a anului școlar, plus modelul de an
ales.

**Ieșire:** 53 de obiecte Saptamana, 12 obiecte Luna, fiecare zi din an încadrată
corect.

### Algoritm
1. Pornim de la data introdusă și verificăm că este într-adevăr o zi de luni. Dacă
   nu, aplicația corectează la lunea cea mai apropiată și te anunță.
2. Generăm 53 de săptămâni consecutive, fiecare cu luni ca zi de start.
3. Suprapunem intervalele de module și de vacanțe peste săptămâni. O săptămână
   tăiată de o vacanță la mijloc primește marcaj parțial, cu zilele clasificate
   individual.
4. Marcăm zilele libere legale și sărbătorile.
5. Construim vederea pe 12 luni, fiecare lună trimițând către săptămânile care o
   ating.
6. Calculăm numărul de ore efective per clasă, pe modul și pe an, din orar minus
   zilele nelucrătoare.

### De ce 53 și nu 52
Un an calendaristic acoperă 52 de săptămâni complete plus una sau două zile. Când
anul școlar începe la mijlocul lunii septembrie și se termină în iunie, intervalul
plus vacanțele de la capete poate atinge 53 de săptămâni ISO. Generând 53 acoperim
orice configurație, iar săptămânile în plus rămân marcate ca fiind în afara anului
de curs.

### Punct care necesită confirmarea ta
Structura anului școlar, cu cele 5 module și datele vacanțelor, se stabilește
anual prin ordin de ministru. Nu construim aplicația cu date fixe în cod. În
schimb:
- aplicația vine cu un preset editabil pentru anul curent
- la prima pornire îți cere să confirmi sau să corectezi datele modulelor, cu
  trimitere la ordinul oficial
- presetul se poate salva și reîncărca anul următor

Același principiu se aplică la Săptămâna verde și la Școala altfel, care se
programează la nivelul fiecărei școli, deci le introduci tu.

---

## 6. Regula de calcul al mediilor

Aici este singurul loc unde nu recomand valori fixe în cod, din motive de
corectitudine.

Reglementarea privind modul de încheiere a mediilor s-a schimbat în ultimii ani
odată cu trecerea la structura pe module și cu noua lege a învățământului. Nu îți
pot garanta din memorie care este formula oficială în vigoare pentru anul acesta,
iar o formulă greșită într-un catalog este o problemă reală.

**Soluția de proiectare:** ecran de configurare a regulii, cu următoarele opțiuni.

| Parametru | Opțiuni |
|---|---|
| Unitatea de agregare | pe modul, pe semestru, pe an |
| Formula | media aritmetică simplă, medie ponderată pe tipuri de evaluare |
| Rotunjire | matematică standard, în favoarea elevului, fără rotunjire |
| Număr minim de note | prag configurabil, cu alertă pentru elevii sub prag |
| Note necontorizate | note de lucru, vizibile, excluse din medie |
| Media la purtare | separată, cu scădere pe absențe nemotivate, prag configurabil |

Mediile calculate apar întotdeauna cu mențiunea „calcul orientativ", iar catalogul
oficial rămâne referința legală. Aplicația te ajută să nu faci greșeli de aritmetică,
nu înlocuiește catalogul.

Înainte de implementare îmi confirmi regula corectă, sau o verificăm împreună în
ordinul în vigoare.

---

## 7. Structura de ecrane și navigația

### Bara laterală, permanentă
```
🏠  Azi
📅  Anul (12 luni)
📆  Săptămâni (53)
🗓  Luna curentă
👥  Clasele
    └ V A, V B, VI A ...
🧑  Elevi și fișe
📘  Planificare calendaristică
📗  Unități de învățare
💬  Părinți și consultații
📋  Activități școlare
📝  Notițe
📤  Export și backup
⚙️  Setări
```

### Navigare rapidă
- `Ctrl+K` deschide o casetă de căutare care sare oriunde: un elev după nume, o
  săptămână după număr, o clasă, o notiță
- săgeți stânga și dreapta pentru săptămâna anterioară și următoare
- `G` apoi `A` pentru anul întreg, `G` apoi `S` pentru săptămâni, așa cum
  funcționează în majoritatea aplicațiilor de productivitate
- breadcrumb permanent sus: An → Modul → Săptămâna 14 → Marți → Clasa V A

Acesta este răspunsul concret la cerința „în câteva clicuri exact la secțiunea de
care am nevoie". Maximum două clicuri sau o combinație de taste către orice ecran.

### Ecranul „Azi", pagina de start
Un singur ecran care răspunde la întrebarea „ce am azi".
- data, săptămâna, modulul, ziua din structura anului
- orarul zilei, cu butoane rapide: marchează absențe, notează, adaugă observație
- ce am de corectat, din lucrările marcate ca date
- ce urmează în săptămâna asta
- alerte: elevi fără număr minim de note, absențe nemotivate peste prag,
  comunicări cu părinții fără urmare

---

## 8. Etapele de dezvoltare

Fiecare etapă produce ceva utilizabil. Nu construim luni întregi fără să folosim
nimic.

### Etapa 0, fundația (estimat 3 la 5 zile de lucru)
- proiect Vite plus React plus TypeScript plus Tailwind
- schema de date în Dexie
- motorul de calendar, cu teste
- ecranul de configurare inițială: alegi modelul de an, introduci prima zi de luni,
  confirmi modulele

**Rezultat:** poți genera și vedea structura anului tău.

### Etapa 1, nucleul zilnic (estimat 1 la 2 săptămâni)
- clase și elevi, cu import dintr-un fișier Excel sau lipire din catalog
- orar
- ecranul „Azi"
- note și absențe, introducere rapidă
- calculul mediilor, cu regula configurabilă

**Rezultat:** aplicația înlocuiește carnetul de note. Din acest moment o folosești
zilnic.

### Etapa 2, planificarea (estimat 1 la 2 săptămâni)
- cele 53 de fișe săptămânale, cu completare automată a datelor
- vederea pe 12 luni
- planificare calendaristică și unități de învățare, legate de săptămâni
- marcarea lecțiilor realizate și mutarea automată a celor rămase

**Rezultat:** planificarea nu se mai rescrie de la zero, se ajustează.

### Etapa 3, restul agendei (estimat 1 săptămână)
- purtare și implicare
- comunicare cu părinții și consultații
- activități: supliniri, lucrări, ședințe, cursuri, Erasmus+
- notițe și informații importante

**Rezultat:** agenda completă.

### Etapa 4, ieșirile (estimat 1 săptămână)
- fișa individuală a elevului, printabilă
- raport pe clasă și pe modul
- export Excel al catalogului
- export PDF al planificării, în formatul cerut la dosar
- backup și restaurare, fișier JSON

**Rezultat:** documentele pentru dosar ies din aplicație, nu se scriu separat.

### Etapa 5, comoditate (opțional)
- PWA, instalare pe telefon
- mod întunecat
- șabloane reutilizabile de lecție
- copiere a unei săptămâni peste alta

Estimările presupun lucru pe seară și în weekend, nu normă întreagă. Etapele 0 și 1
sunt cele care contează, restul se poate întinde.

---

## 9. Backup și siguranța datelor

Datele stau în browser, deci trebuie protejate explicit.

- **backup automat** la fiecare pornire, fișier JSON descărcat în folderul tău
- **backup manual** cu un buton, oricând
- **restaurare** din fișier, cu previzualizare a ce se va suprascrie
- **avertisment clar** în aplicație: ștergerea datelor de navigare din browser
  șterge și agenda, dacă nu ai backup
- opțional, mai târziu: sincronizare cu Google Drive, pe contul tău, folosind
  exact fișierul de backup

Regula de aur pe care o punem vizibil în interfață: catalogul oficial rămâne
referința legală, aplicația este unealta ta de lucru.

---

## 10. Protecția datelor, ce trebuie clarificat de la început

Aplicația conține date personale ale unor minori. Chiar dacă rămân local, câteva
lucruri merită stabilite înainte de a scrie cod.

1. **Datele nu părăsesc dispozitivul.** Fără server, fără analytics, fără servicii
   externe. Se scrie explicit în aplicație.
2. **Inițiale în ieșirile publice.** Orice raport destinat afișării sau
   partajării folosește inițiale și clasa, niciodată numele complet. Numele
   complet apare doar în fișa individuală și în catalogul tău.
3. **Backup-urile sunt date personale.** Fișierul JSON conține tot. Se păstrează
   pe un dispozitiv protejat cu parolă, nu se trimite pe email.
4. **Dacă aplicația ajunge la alți profesori din școală,** discuția se mută la
   nivel instituțional și are nevoie de avizul conducerii.

---

## 11. Ce trebuie să confirmi înainte de implementare

1. Varianta de platformă: recomand B, aplicație web local-first. Confirmi sau
   alegi altceva.
2. Regula oficială de calcul al mediilor pentru anul acesta, sau acordul să o
   verificăm împreună în ordinul în vigoare.
3. Structura anului școlar curent: datele exacte ale celor 5 module și ale
   vacanțelor, plus săptămânile speciale stabilite de școală.
4. Clasele și disciplinele pe care le predai anul acesta, cu numărul de ore, ca să
   dimensionăm corect orarul.
5. Dacă ești diriginte, pentru că asta adaugă secțiuni întregi: ședințe cu
   părinții, situație școlară pe toate disciplinele, consiliere.
6. Formatul exact cerut de școală pentru planificarea calendaristică, ca exportul
   PDF să iasă direct bun de pus la dosar.

---

## 12. Riscuri și cum le tratăm

| Risc | Tratament |
|---|---|
| Structura anului școlar se schimbă prin ordin nou | nimic fix în cod, totul editabil din interfață |
| Regula de calcul al mediilor este greșită | regulă configurabilă, mențiune „calcul orientativ", verificare înainte de folosire |
| Pierderea datelor din browser | backup automat la fiecare pornire, avertisment vizibil |
| Proiectul se întinde și rămâne neterminat | etapele 0 și 1 produc o unealtă utilizabilă în sub trei săptămâni |
| Dublarea muncii, aplicație plus catalog | aplicația este locul unde lucrezi, catalogul se completează din ea, nu invers |
| Introducerea datelor devine ea însăși o corvoadă | import din Excel pentru elevi, orar introdus o singură dată, completare automată peste tot |

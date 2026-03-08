import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# PAGE 4 CONTENT
p4_content = '''<div class="article-content" style="column-count: 2; column-gap: 6mm; font-size: 10pt; line-height: 1.5; margin-top:4mm;">
  <p><strong>Pentru că tânărul Principe Carol I a crezut în puterea educației și a construit România pe care o cunoaștem astăzi.</strong> Fiecare școală, fiecare bibliotecă, fiecare copil care învață este parte din visul lui Carol I - o Românie educată, puternică și mândră de ea.</p>
  
  <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">O nouă Românie, o nouă școală</h3>
  <p>Imaginează-ți anul 1921. Gura Humorului tocmai scăpase de sub ocupația austriacă (1918) și acum făcea parte din România Mare. În clădirea unde acum înveți tu, se născuse un liceu românesc - primul din oraș care preda în limba română, nu în germană!</p>
  <p>La 1 noiembrie 1920, s-a deschis prima clasă cu doar 47 de elevi români. Un an mai târziu, în 1921, liceul a primit numele "Principele Carol".</p>
  
  <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">De ce acest nume?</h3>
  <p>Pentru românii din Gura Humorului, care timp de 143 de ani (1775-1918) fuseseră sub stăpânire străină, a numi liceul după moștenitorul tronului românesc, era un gest de mândrie națională și de recunoștință pentru cel care a crezut într-un popor educat. Era ca și cum ar fi spus: "Acum suntem români liberi și avem propria noastră școală românească!"</p>

  <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:4mm; margin-bottom:1mm; font-size:12pt;">Povestea liceului "Principele Carol"</h3>
  <ul style="padding-left: 4mm; margin-bottom: 2mm; list-style-type: none;">
    <li><strong>1920</strong> - Prima clasă (47 elevi)</li>
    <li><strong>1921</strong> - Denumirea "Principele Carol" + funcționează cu clasele I-II</li>
    <li><strong>1923-1924</strong> - Gimnaziu complet (clasele I-IV), 227 elevi</li>
    <li><strong>1927-1928</strong> - Liceu complet (clasele I-VIII)</li>
    <li><strong>1931</strong> - Se desființează (criză economică)</li>
    <li><strong>1932-1938</strong> - Devine gimnaziu</li>
  </ul>
  
  <p>În 1944, când Bucovina de Nord (cu Cernăuțiul) a intrat definitiv în componența Rusiei, Școala Normală de Fete "Maria Voichița" din Cernăuți a fost mutată aici, la Gura Humorului, în aceeași clădire unde fusese Liceul "Principele Carol". Carol I înțelegea ceva fundamental: "O școală fără profesori buni este o clădire goală". De aceea, încă din 1871, a înființat Școli Normale - instituții care pregăteau profesori. Ce este o Școală Normală? Un liceu special unde tinerii (mai ales tinere, în cazul celor pentru învățământul primar) învățau cum să le predea copiilor. Ieșeau de acolo pregătiți să meargă în sate și orașe să-i învețe pe alții.</p>
  
  <ul style="padding-left: 4mm; margin-bottom: 2mm; list-style-type: none;">
    <li><strong>1945-1959</strong> - Școala Pedagogică de Fete. Timp de 15 ani, în această clădire nu au învățat doar elevi, ci și viitoare învățătoare. Fete tinere veneau aici să învețe pedagogie, psihologie, metodică, practicau alături de profesorii care îi învățau pe copiii din aceeași clădire, apoi plecau în satele Bucovinei să predea la rândul lor. Un elev bun devine profesor bun. Un profesor bun creează elevi buni. Și povestea continuă. Poate că într-o zi vei fi și tu profesorul care va sta în fața unei clase, tot în această clădire, continuând povestea.</li>
  </ul>
  
  <p>După 1959, școala s-a numit, pe rând: Școala Generală Nr. 2, apoi Școala Gimnazială „Petru Comarnescu”. Școala Gimnazială „Principele Carol” de astăzi (înființată oficial cu acest nume recent) poartă același nume ca liceul istoric din 1921! Când mergi la școală, pășești prin aceeași clădire unde acum 105 ani se năștea învățământul românesc la Gura Humorului.</p>
  <p>Carol I (1866-1914) a construit România modernă și a pus educația în centrul țării. Tu, elevul de astăzi, continui povestea începută acum un secol - când primii 47 de elevi români au intrat în această clădire, visând la o Românie educată și liberă.</p>

  <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">De ce este important să știi asta?</h3>
  <p>Când cineva te întreabă "De ce se numește școala ta „Principele Carol”?, acum poți răspunde: Pentru că în 1921, acum 105 ani, în această clădire s-a deschis primul liceu românesc din Gura Humorului, după ce Bucovina s-a unit cu România. L-au numit după Principele Carol, moștenitorul tronului, pentru că era simbolul speranței pentru o Românie nouă, liberă și educată. Școala noastră de astăzi continuă acea poveste: de 105 ani, iar pe aceste holuri, elevii scriu istoria orașului Gura Humorului, a Bucovinei, a țării și poate chiar a Europei."</p>
  <p>Ești parte dintr-o poveste care a început în 1921. Când mergi la școală, continui visul unui rege care credea că educația poate schimba lumea. Și avea dreptate! Ce capitol vei scrie tu?</p>

  <hr class="gold-divider" style="margin: 4mm 0;">
  
  <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:2mm; margin-bottom:1mm; font-size:11pt;">💡 5 FAPTE DESPRE LICEUL DIN 1921</h3>
  <ul style="padding-left: 4mm; margin-bottom: 2mm;">
    <li><strong>Prima școală românească din oraș:</strong> Până în 1920, predarea era doar în germană. Românii erau minoritate în propriul oraș!</li>
    <li><strong>Directorul a fost prof. Emanuil Antonovici:</strong> Preda matematica și fizica. Corpul didactic avea 16 profesori.</li>
    <li><strong>Creștere rapidă:</strong> De la 47 elevi (1920) la 408 elevi (1928) - în doar 8 ani!</li>
    <li><strong>Bibliotecă impresionantă:</strong> În 1928, biblioteca avea 1.179 volume - o avere pentru acele timpuri!</li>
    <li><strong>A supraviețuit războaielor:</strong> Clădirea a fost spital militar o perioadă, dar liceul și-a continuat, apoi, misiunea de educare.</li>
  </ul>
</div>'''

# PAGE 5 CONTENT
p5_content = '''<div class="sidebar-layout reversed" style="margin-top:4mm">
  <div>
    <div class="placeholder-photo" style="height:160px">
      <div class="ph-icon">📷</div>
      <div class="ph-label">Portret Carol I</div>
      <div class="ph-desc">Portret oficial sau pictură istorică</div>
      <div class="ph-specs">Sursă: domeniu public</div>
    </div>
  </div>
  <div>
    <div class="article-content" style="column-count: 2; column-gap: 6mm; font-size: 10pt; line-height: 1.5;">
      <p><strong>Imaginează-ți că ai 27 de ani</strong> și primești misiunea de a conduce o țară pe care abia o cunoști, unde nu vorbești limba și unde totul trebuie construit de la zero. Aceasta a fost provocarea lui Carol I în 1866, când a devenit domnitor al României. Ce a urmat? O poveste extraordinară de transformare!</p>
      
      <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">Visul educației pentru toți</h3>
      <p>Carol I credea că o țară puternică începe din școală. „Fără educație, nu există viitor", spunea el. Și s-a apucat de treabă:</p>
      <ul style="padding-left: 4mm; margin-bottom: 2mm;">
        <li><strong>Școli pentru toți copiii.</strong> În 1864, când Carol a ajuns în România, doar 1 din 10 copii mergea la școală. El a construit mii de școli în sate și orașe. A făcut educația primară gratuită și obligatorie - primul pas către o Românie educată!</li>
        <li><strong>Universități și licee.</strong> A înființat Universitatea din București (1864), licee prestigioase și școli profesionale. Voia ca tinerii români să poată studia acasă, nu doar în străinătate.</li>
        <li><strong>Biblioteci și muzee.</strong> A deschis Biblioteca Națională și primul muzeu al țării. Credea că românii trebuie să-și cunoască istoria și cultura.</li>
      </ul>
      
      <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">Constructorul României moderne</h3>
      <p>Carol I nu s-a oprit la educație. A fost un adevărat arhitect al țării:</p>
      <ul style="padding-left: 4mm; margin-bottom: 2mm; list-style-type: none;">
        <li>🏛️ A construit primul parlament, palate, teatre, căi ferate</li>
        <li>🇷🇴 A câștigat independența României (1877) și a devenit rege (1881)</li>
        <li>💰 A stabilizat economia - a introdus leul ca monedă</li>
        <li>⚖️ A creat o constituție și legi moderne</li>
      </ul>
      
      <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">Un rege simplu, dar mare</h3>
      <p>Deși era rege, Carol I trăia simplu. Purta uniformă militară în loc de haine scumpe, lucra 12 ore pe zi și nu risipea banii statului. Când România era în criză, dona din averea personală. "Eu slujesc România, nu mă slujesc de România", spunea el.</p>
    </div>
  </div>
</div>
<hr class="gold-divider">
<div class="info-box" style="margin-top: 2mm;">
  <div class="info-title">📚 Repere cronologice — Viața lui Carol I</div>
  <ul style="list-style: none; padding: 0; margin: 0; font-size: 9pt;">
    <li style="margin-bottom:1mm;"><strong>1839</strong> - Se naște în Germania, la Castelul Sigmaringen</li>
    <li style="margin-bottom:1mm;"><strong>1866</strong> - Vine în România ca domnitor, la doar 27 de ani</li>
    <li style="margin-bottom:1mm;"><strong>1877</strong> - România câștigă independența în Războiul de Independență</li>
    <li style="margin-bottom:1mm;"><strong>1881</strong> - Carol I devine primul rege al României</li>
    <li style="margin-bottom:1mm;"><strong>1866-1914</strong> - 48 de ani de domnie - cea mai lungă din istoria României</li>
    <li style="margin-bottom:1mm;"><strong>1914</strong> - Moare la 75 de ani, lăsând în urmă o țară complet transformată</li>
  </ul>
</div>

<h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:11pt;">💡 5 FAPTE SURPRINZĂTOARE</h3>
<ul style="padding-left: 4mm; margin-bottom: 2mm; font-size: 10pt;">
  <li><strong>Nu vorbea românește când a venit!</strong> A învățat limba în timpul călătoriei cu trenul spre București. După câteva luni vorbea fluent.</li>
  <li><strong>A fost primul rege al României.</strong> Înainte de el, România avea domni, nu regi.</li>
  <li><strong>Pasionat de educație.</strong> Vizita personal școlile și vorbea cu elevii. Întotdeauna întreba: "Ce ați învățat astăzi?"</li>
  <li><strong>A construit Peleșul.</strong> Castelul de la Sinaia, unul dintre cele mai frumoase din Europa, a fost proiectat de el. Prima cameră cu electricitate din România era acolo!</li>
  <li><strong>48 de ani de domnie.</strong> A condus România mai mult decât orice alt rege sau președinte din istoria noastră.</li>
</ul>'''

def replace_section(html, section_id, new_content):
    # Match the <div class="page-inner"> header so we keep the rubric-header, but replace everything after it.
    header_pattern = r'(<section class="page" id="' + section_id + r'">\s*<div class="page-inner">\s*<div class="rubric-header">.*?</div[^>]*>\s*</div>\s*<!--.*?-->\s*)*'
    # Actually, let's just use re.sub to replace the contents inside page-inner after the header.
    
    # We can match:
    # <section class="page" id="pX">
    #   <div class="page-inner">
    #     <div class="rubric-header">...</div>
    #   ...
    # </section>
    
    def repl(m):
        header_part = m.group(1)
        return header_part + "\n" + new_content + "\n    </div>\n</section>"
        
    pattern = r'(<section class="page"[^>]*id="' + section_id + r'">\s*<div class="page-inner">\s*<div class="rubric-header">.*?<div class="header-page-num">\d+</div>\s*</div>)(.*?)</section>'
    return re.sub(pattern, repl, html, flags=re.DOTALL)

html = replace_section(html, "p4", p4_content)
html = replace_section(html, "p5", p5_content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Pages 4 and 5 contents updated successfully!")

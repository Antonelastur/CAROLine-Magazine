import os
import re

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix Page 5
p5_content = '''<section class="page" id="p5">
    <div class="page-inner">
      <div class="rubric-header">
        <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
        <div class="header-content">
          <h2>Reportaj Special</h2>
          <div class="rubric-sub">Ceremonia schimbării denumirii școlii</div>
        </div>
        <div class="header-page-num">5</div>
      </div>
      <div class="two-columns" style="margin-top:4mm">
        <div class="placeholder-photo" style="height:140px">
          <div class="ph-icon">📷</div>
          <div class="ph-label">Foto ceremonie #1</div>
          <div class="ph-desc">Imaginea principală a evenimentului</div>
          <div class="ph-specs">Min. 2000×1500px</div>
        </div>
        <div class="placeholder-text" style="min-height:140px">
          <div class="ph-label">📝 TEXT REPORTAJ</div>
          <div class="ph-desc">Articol despre ceremonia schimbării numelui școlii. Cum a fost atmosfera, cine a participat.</div>
          <div class="ph-specs">Lungime: 300–400 cuvinte</div>
        </div>
      </div>
      <div class="two-columns" style="margin-top:4mm">
        <div class="placeholder-photo" style="height:90px">
          <div class="ph-icon">📷</div>
          <div class="ph-label">Foto ceremonie #2</div>
          <div class="ph-desc">Invitați oficiali / discurs</div>
          <div class="ph-specs">Min. 1500×1500px</div>
        </div>
        <div class="placeholder-photo" style="height:90px">
          <div class="ph-icon">📷</div>
          <div class="ph-label">Foto ceremonie #3</div>
          <div class="ph-desc">Elevi la eveniment</div>
          <div class="ph-specs">Min. 1500×1500px</div>
        </div>
      </div>
    </div>
</section>'''

html = re.sub(r'<section class="page" id="p5">.*?</section>', p5_content, html, flags=re.DOTALL)


# Create content for page 19
p19_content = '''<section class="page" id="p19">
    <div class="page-inner">
      <div class="rubric-header">
        <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
        <div class="header-content">
          <h2>Hoinar prin Țara Fagilor</h2>
          <div class="rubric-sub">Gura Humorului — 5 Locuri Recomandate de Caroliști</div>
        </div>
        <div class="header-page-num">19</div>
      </div>
      
      <p class="lead-text" style="margin:4mm 0; font-style: italic;">Mini-ghid local: Unde mergem noi când nu suntem la școală? De la elevi pentru elevi (și pentru oricine vrea să descopere orașul nostru!)</p>
      
      <div class="two-columns" style="margin-top:4mm">
        <div class="card" style="margin-bottom:4mm; border: 2px solid var(--gold-warm); background-color: rgba(244, 196, 48, 0.05);">
          <div class="card-body">
            <h3 style="color: var(--navy-dark); font-family: var(--font-heading); font-size: 12pt; margin-bottom: 2px;">1. MĂNĂSTIREA HUMOR ⛪</h3>
            <div style="font-size: 8.5pt; font-weight: bold; color: var(--gold-warm); text-transform: uppercase; margin-bottom: 2mm;">Recomandată de: Clasa a VII-a B</div>
            <p style="font-size: 9.5pt; line-height: 1.4; margin-bottom: 2mm;"><strong>De ce merită:</strong> "Da, știm - toată lumea vorbește despre ea. Dar serios, mergi dimineața devreme (8:00-9:00) când nu sunt autocare cu turiști. E o liniște magică și pereții vopsiți în albastru sunt chiar spectaculoși când soarele răsare. Bonus: caută 'Scara Virtuților' pe peretele nordic - e ca un joc video medieval!"</p>
            <ul style="font-size: 8.5pt; color: #555; padding-left: 4mm; margin:0;">
              <li><strong>Perfect pentru:</strong> Fotografii pentru Instagram, proiecte la istorie, liniște</li>
              <li><strong>Intrare:</strong> Mic tarif (studenții au reducere)</li>
              <li><strong>Pro-tip:</strong> Du-te în săptămâna Paștelui - e atmosferă specială!</li>
            </ul>
          </div>
        </div>

        <div class="card" style="margin-bottom:4mm; border: 2px solid var(--gold-warm); background-color: rgba(244, 196, 48, 0.05);">
          <div class="card-body">
            <h3 style="color: var(--navy-dark); font-family: var(--font-heading); font-size: 12pt; margin-bottom: 2px;">2. PARCUL CENTRAL 🌳</h3>
            <div style="font-size: 8.5pt; font-weight: bold; color: var(--gold-warm); text-transform: uppercase; margin-bottom: 2mm;">Recomandată de: Clasa a VI-a A</div>
            <p style="font-size: 9.5pt; line-height: 1.4; margin-bottom: 2mm;"><strong>De ce merită:</strong> "E locul nostru de întâlnire când nu vrem să fim în mall sau acasă. Vii cu rolele, cu bicicleta, sau pur și simplu stai pe bancă și mănânci înghețată. Vara sunt concerte gratuite vinerea seara. Plus: wifi public (când merge)!"</p>
            <ul style="font-size: 8.5pt; color: #555; padding-left: 4mm; margin:0;">
              <li><strong>Perfect pentru:</strong> Plimbări cu bicicleta, picnic, întâlniri</li>
              <li><strong>Când să mergi:</strong> După-amiaza (16:00-19:00)</li>
              <li><strong>Pro-tip:</strong> Gheața de la chioșcul din parc e mai ieftină!</li>
            </ul>
          </div>
        </div>

        <div class="card" style="margin-bottom:4mm; border: 2px solid var(--gold-warm); background-color: rgba(244, 196, 48, 0.05);">
          <div class="card-body">
            <h3 style="color: var(--navy-dark); font-family: var(--font-heading); font-size: 12pt; margin-bottom: 2px;">3. DEALUL CETĂȚII 🥾</h3>
            <div style="font-size: 8.5pt; font-weight: bold; color: var(--gold-warm); text-transform: uppercase; margin-bottom: 2mm;">Recomandat de: Clasa a VIII-a</div>
            <p style="font-size: 9.5pt; line-height: 1.4; margin-bottom: 2mm;"><strong>De ce merită:</strong> "Traseu spre Piatra Șoimului. Urcuș de ~40 minute, dar ai panoramă 360° - vezi tot Gura Humorului și munții în jur. Mergi cu prietenii, cu rucsacul plin de snacks, și stai acolo până la apus. Conversații deep și poze spectaculoase."</p>
            <ul style="font-size: 8.5pt; color: #555; padding-left: 4mm; margin:0;">
              <li><strong>Perfect pentru:</strong> Drumeții, aventură, poze</li>
              <li><strong>Când să mergi:</strong> Primăvara sau toamna</li>
              <li><strong>Pro-tip:</strong> Luați apă și bocanci buni!</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</section>'''

# Create content for page 20
p20_content = '''<section class="page" id="p20">
    <div class="page-inner">
      <div class="rubric-header">
        <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
        <div class="header-content">
          <h2>Hoinar prin Țara Fagilor</h2>
          <div class="rubric-sub">...continuare Ghid Local</div>
        </div>
        <div class="header-page-num">20</div>
      </div>
      
      <div class="two-columns" style="margin-top:4mm">
        <div>
            <div class="card" style="margin-bottom:4mm; border: 2px solid var(--gold-warm); background-color: rgba(244, 196, 48, 0.05);">
              <div class="card-body">
                <h3 style="color: var(--navy-dark); font-family: var(--font-heading); font-size: 12pt; margin-bottom: 2px;">4. BIBLIOTECA ORĂȘENEASCĂ 📚</h3>
                <div style="font-size: 8.5pt; font-weight: bold; color: var(--gold-warm); text-transform: uppercase; margin-bottom: 2mm;">Recomandată de: Clasa a V-a C</div>
                <p style="font-size: 9.5pt; line-height: 1.4; margin-bottom: 2mm;"><strong>De ce merită:</strong> "Nu râdeți - biblioteca e de fapt mișto! Au secțiune nouă cu benzi desenate și manga, au wifi rapid (mai rapid ca la școală!), și doamna bibliotecar e super friendly. Poți împrumuta cărți gratuit și ai fotolii comfy unde îți faci temele în pace."</p>
                <ul style="font-size: 8.5pt; color: #555; padding-left: 4mm; margin:0;">
                  <li><strong>Perfect pentru:</strong> Teme, lectură, refugiu când plouă</li>
                  <li><strong>Când să mergi:</strong> După școală (14:00-18:00)</li>
                  <li><strong>Pro-tip:</strong> Cere carnet de împrumut - e gratis!</li>
                </ul>
              </div>
            </div>

            <div class="card" style="margin-bottom:4mm; border: 2px solid var(--gold-warm); background-color: rgba(244, 196, 48, 0.05);">
              <div class="card-body">
                <h3 style="color: var(--navy-dark); font-family: var(--font-heading); font-size: 12pt; margin-bottom: 2px;">5. "LOCUL NOSTRU SECRET" 🌊</h3>
                <div style="font-size: 8.5pt; font-weight: bold; color: var(--gold-warm); text-transform: uppercase; margin-bottom: 2mm;">Recomandat de: Clasa a VII-a A</div>
                <p style="font-size: 9.5pt; line-height: 1.4; margin-bottom: 2mm;"><strong>De ce merită:</strong> "Malul Humorului. Lângă podul vechi, unde râul face o curbă, e o zonă cu pietre plate perfecte pentru șezut. Mergi acolo când vrei să fii singur cu gândurile tale. Apa clocotește frumos, sunt copaci în jur, și nimeni nu te deranjează. E ca propriul nostru 'Central Park'."</p>
                <ul style="font-size: 8.5pt; color: #555; padding-left: 4mm; margin:0;">
                  <li><strong>Perfect pentru:</strong> Reflecție, citit, desenat</li>
                  <li><strong>Pro-tip:</strong> Du-ți o pătură și o carte. Spune părinților unde ești!</li>
                </ul>
              </div>
            </div>
            
            <p style="font-size: 9pt; font-style: italic; color: var(--navy-medium); text-align: center;">Ai descoperit un loc mișto pe care noi nu-l știm? Scrie-ne pentru următorul număr!</p>
        </div>
        
        <div>
            <div class="info-box" style="margin-bottom:4mm; background-color: var(--navy-dark); color: white; border-color: var(--navy-dark);">
                <div class="info-title" style="color: var(--gold-warm); border-bottom: 1px solid rgba(255,255,255,0.2);">⚡ BONUSURI RAPIDE</div>
                <ul style="list-style: none; padding: 0; margin: 0; font-size: 9pt; padding-top: 2mm;">
                  <li style="margin-bottom:2mm;">🍕 <strong>Pizza Express</strong> - Pizza preferată a caroliștilor (oferta student)</li>
                  <li style="margin-bottom:2mm;">☕ <strong>Caf. "La Colț"</strong> - Ciocolată caldă excelentă</li>
                  <li style="margin-bottom:2mm;">🎮 <strong>Sala de jocuri</strong> - Lângă piață, când plouă</li>
                  <li style="margin-bottom:0;">🏊 <strong>Bazinul</strong> - Când e caniculă vara</li>
                </ul>
            </div>
            
            <div class="info-box" style="background-color: var(--gold-warm); color: var(--navy-dark); border-color: var(--gold-warm); margin-bottom:4mm;">
                <div class="info-title" style="color: var(--navy-dark); border-bottom: 1px solid rgba(10,30,61,0.2);">🛡️ REGULA CAROLIȘTILOR</div>
                <ul style="font-size: 8.5pt; padding-left: 4mm; margin-bottom: 0;">
                  <li>Spune-le părinților unde ești</li>
                  <li>Nu lăsa gunoaie</li>
                  <li>Respectă localnicii și monumentele</li>
                  <li>Mergi în grup când e posibil</li>
                  <li>Întoarce-te acasă la timp</li>
                </ul>
            </div>
            
            <div class="placeholder-photo" style="height: 120px;">
              <div class="ph-icon">🗺️</div>
              <div class="ph-label">Hartă Gura Humorului</div>
              <div class="ph-desc">Hartă stilizată cu cele 5 locuri marcate + coduri QR</div>
              <div class="ph-specs">Ilustrație vectorială</div>
            </div>
        </div>
      </div>
    </div>
</section>'''

html = re.sub(r'<section class="page" id="p19">.*?</section>', p19_content, html, flags=re.DOTALL)
html = re.sub(r'<section class="page" id="p20">.*?</section>', p20_content, html, flags=re.DOTALL)


with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Pages 5, 19, 20 updated successfully.")

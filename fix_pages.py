import re
import os

base_dir = r"c:\Users\Antonela\Desktop\Caroline\revista"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# I will recreate the content of pages 5, 6, 7, 8 correctly.
# The `restore_headers.py` has already added the `.rubric-header` correctly, but I will override the entire <section class="page" id="pX"> block to be safe.

def generate_page(page_id, title, subtitle, content_html):
    return f'''  <section class="page" id="{page_id}">
    <div class="page-inner">
      <div class="rubric-header">
        <img src="../Imagini/Logo.jpeg" alt="Logo" class="header-logo">
        <div class="header-content">
          <h2>{title}</h2>
          <div class="rubric-sub">{subtitle}</div>
        </div>
        <div class="header-page-num">{page_id.replace("p", "")}</div>
      </div>
{content_html}
    </div>
  </section>'''

# Page 5: Reportaj Special
p5_content = '''      <div class="two-columns" style="margin-top:4mm">
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
      </div>'''

# Page 6: Reportaj Special (continuare)
p6_content = '''      <div class="two-columns" style="margin-top:4mm">
        <div class="placeholder-photo" style="height:90px">
          <div class="ph-icon">📷</div>
          <div class="ph-label">Foto ceremonie #4</div>
          <div class="ph-desc">Moment artistic / spectacol elevi</div>
          <div class="ph-specs">Min. 1500×1500px</div>
        </div>
        <div class="placeholder-photo" style="height:90px">
          <div class="ph-icon">📷</div>
          <div class="ph-label">Foto ceremonie #5</div>
          <div class="ph-desc">Foto de grup / moment festiv</div>
          <div class="ph-specs">Min. 1500×1500px</div>
        </div>
      </div>
      <div class="placeholder-text" style="min-height:100px;margin-top:4mm">
        <div class="ph-label">📝 TEXT REPORTAJ (PARTEA 2)</div>
        <div class="ph-desc">Continuarea: momente emoționante, declarații ale participanților.</div>
        <div class="ph-specs">Lungime: 300–400 cuvinte</div>
      </div>
      <div class="pull-quote" style="margin-top:4mm">
        <div class="placeholder-text" style="border:none;background:none;padding:0;min-height:auto">
          <div class="ph-label" style="font-size:8pt">📝 DECLARAȚIE</div>
          <div class="ph-desc">Citat de la un participant / invitat important</div>
        </div>
      </div>
      <div class="placeholder-photo" style="height:80px;margin-top:3mm">
        <div class="ph-icon">📷</div>
        <div class="ph-label">Foto ceremonie #6</div>
        <div class="ph-desc">Foto finală/panoramică</div>
        <div class="ph-specs">Format landscape, min. 2500×1000px</div>
      </div>'''

# Page 7: Principele Carol
p7_content = '''      <div class="sidebar-layout" style="margin-top:4mm">
        <div>
          <div class="placeholder-text" style="min-height:150px">
            <div class="ph-label">📝 TEXT EDUCAȚIONAL</div>
            <div class="ph-desc">Articol despre Principele Carol — cine este, legătura cu Gura Humorului, vizitele regale, valori.</div>
            <div class="ph-specs">Așteptare text: Fișierul Principele Carol.docx</div>
          </div>
        </div>
        <div>
          <div class="placeholder-photo" style="height:150px">
            <div class="ph-icon">📷</div>
            <div class="ph-label">Portret / Foto</div>
            <div class="ph-desc">Imagine istorică sau oficială cu Principele Carol</div>
            <div class="ph-specs">Sursă: domeniu public</div>
          </div>
        </div>
      </div>
      <hr class="gold-divider">
      <div class="info-box">
        <div class="info-title">👑 Fișa personajului</div>
        <div class="placeholder-text" style="min-height:50px;border:none;background:none;padding:0">
          <div class="ph-desc">Date biografice esențiale: Nume complet, Născut, Familie, Rol, Legătura cu Gura Humorului</div>
        </div>
      </div>
      <div class="placeholder-illustration" style="height:60px;margin-top:3mm">
        <div class="ph-icon">🎨</div>
        <div class="ph-label">Ilustrație decorativă</div>
        <div class="ph-desc">Stemă regală sau element heraldic decorativ</div>
      </div>'''

# Page 8: Carol I
p8_content = '''      <div class="sidebar-layout reversed" style="margin-top:4mm">
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
            <p>Carol I credea că o țară puternică începe din școală. „Fără educație, nu există viitor", spunea el.</p>
            <ul style="padding-left: 4mm; margin-bottom: 2mm;">
              <li><strong>Școli pentru toți copiii.</strong> A construit mii de școli făcând educația primară gratuită.</li>
              <li><strong>Universități și licee.</strong> A înființat Universitatea din București.</li>
            </ul>
            <h3 style="color: var(--navy-medium); font-family: var(--font-heading); margin-top:3mm; margin-bottom:1mm; font-size:12pt;">Constructorul României</h3>
            <p>A fost un arhitect al țării: a construit primul parlament, palate, a obținut independența (1877) și a devenit rege (1881).</p>
          </div>
        </div>
      </div>
      <hr class="gold-divider">
      <div class="info-box">
        <div class="info-title">📚 Timeline — Momente-cheie</div>
        <ul style="list-style: none; padding: 0; margin: 0; font-size: 9pt;">
          <li style="margin-bottom:1mm;"><strong>1839</strong> - Se naște în Germania</li>
          <li style="margin-bottom:1mm;"><strong>1866</strong> - Vine în România ca domnitor (la 27 ani)</li>
          <li style="margin-bottom:1mm;"><strong>1877</strong> - România câștigă independența</li>
          <li style="margin-bottom:1mm;"><strong>1881</strong> - Carol I devine primul rege al României</li>
          <li style="margin-bottom:1mm;"><strong>1866-1914</strong> - Cea mai lungă domnie (48 ani)</li>
          <li style="margin-bottom:1mm;"><strong>1914</strong> - Moare la 75 de ani</li>
        </ul>
      </div>
      <div class="pull-quote" style="margin-top:4mm; font-size: 12pt;">
        <em>„Un popor care nu-și cunoaște istoria e ca un copil care nu-și cunoaște părinții."</em>
      </div>'''

pages = {
    "p5": generate_page("p5", "Reportaj Special", "Ceremonia schimbării denumirii școlii", p5_content),
    "p6": generate_page("p6", "Reportaj Special", "...continuare", p6_content),
    "p7": generate_page("p7", "Principele Carol", "Patronul spiritual al școlii noastre", p7_content),
    "p8": generate_page("p8", "Carol I", "Fondatorul României Moderne", p8_content)
}

# Replace loops
for p_id, p_html in pages.items():
    # Matches <section class="page" id="pX"> ... </section> correctly across lines. Wait, section content could have nested tags.
    # We will use re.sub with a non-greedy .*? up to the closing section that matches the indentation or just splitting it.
    pattern = r'<section class="page"[^>]*id="' + p_id + r'".*?</section>'
    html = re.sub(pattern, p_html, html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Pages 5, 6, 7, 8 have been fixed.")

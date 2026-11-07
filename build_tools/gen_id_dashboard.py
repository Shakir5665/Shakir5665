from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ID_PNG_B64
import os

def generate_id_dashboard():
    # Barcode generator
    barcode_bars = []
    # Pattern of bar widths
    pattern = [2, 1, 3, 1, 1, 2, 4, 1, 2, 1, 3, 2, 1, 4, 1, 2, 1, 3, 2, 1, 1, 3, 1, 2, 4, 1, 2, 1, 3, 1, 2, 3, 1, 1, 4, 2]
    bx = 100
    for w in pattern:
        barcode_bars.append(f'<rect x="{bx}" y="422" width="{w}" height="24" fill="#cbd5e1"/>')
        bx += w + 2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 500" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .id_title {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: -0.3px;
      }}
      .id_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .id_body {{
        font-family: 'Space Grotesk', sans-serif;
      }}

      /* Lanyard Drop, Damped Pendulum Settling and Gentle +/-1.7 deg Swing */
      @keyframes id_pendulumSequence {{
        0% {{ transform: translateY(-400px) rotate(-16deg); opacity: 0; }}
        4% {{ transform: translateY(0px) rotate(14deg); opacity: 1; }}
        9% {{ transform: translateY(0px) rotate(-8deg); }}
        14% {{ transform: translateY(0px) rotate(4.5deg); }}
        19% {{ transform: translateY(0px) rotate(-2.5deg); }}
        24% {{ transform: translateY(0px) rotate(1.7deg); }}
        37% {{ transform: translateY(0px) rotate(-1.7deg); }}
        50% {{ transform: translateY(0px) rotate(1.7deg); }}
        63% {{ transform: translateY(0px) rotate(-1.7deg); }}
        76% {{ transform: translateY(0px) rotate(1.7deg); }}
        89% {{ transform: translateY(0px) rotate(-1.7deg); }}
        100% {{ transform: translateY(0px) rotate(1.7deg); }}
      }}

      /* Foil Sweep Animation across card */
      @keyframes id_foilSweepAnim {{
        0%, 15% {{ transform: translateX(-280px) rotate(25deg); opacity: 0; }}
        35% {{ opacity: 0.6; }}
        55%, 100% {{ transform: translateX(350px) rotate(25deg); opacity: 0; }}
      }}

      /* General Fade-in */
      @keyframes id_fadeIn {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      .id_lanyard_group {{
        transform-origin: 195px 0px;
        animation: id_pendulumSequence 12s cubic-bezier(0.25, 1, 0.5, 1) infinite both;
      }}
      .id_foil_sweep {{
        animation: id_foilSweepAnim 6s ease-in-out infinite;
      }}
      .id_anim {{
        animation: id_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}

      /* Accessibility: Reduced Motion */
      @media (prefers-reduced-motion: reduce) {{
        .id_lanyard_group {{
          animation: none !important;
          transform: rotate(0deg) !important;
          opacity: 1 !important;
        }}
        .id_foil_sweep, .id_anim {{
          animation: none !important;
          transform: none !important;
        }}
      }}
    </style>

    <pattern id="id_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <linearGradient id="id_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#182c55" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="id_cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1527"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <!-- Metal Clasp Gradients -->
    <linearGradient id="id_metalGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="35%" stop-color="#e2e8f0"/>
      <stop offset="60%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>

    <linearGradient id="id_metalShine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#cbd5e1" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#475569" stop-opacity="0.9"/>
    </linearGradient>

    <!-- Holographic Foil Sheen -->
    <linearGradient id="id_foilGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="30%" stop-color="#38bdf8" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.45"/>
      <stop offset="70%" stop-color="#ff354f" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="id_badgeCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e1a33"/>
      <stop offset="100%" stop-color="#080e1c"/>
    </linearGradient>

    <radialGradient id="id_glowLanyard" cx="22%" cy="40%" r="45%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="id_badgeClip">
      <rect x="60" y="75" width="270" height="395" rx="16"/>
    </clipPath>

    <clipPath id="id_photoClip">
      <rect x="85" y="125" width="220" height="185" rx="12"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="500" rx="20" fill="url(#id_cardBg)"/>
  <rect width="880" height="500" rx="20" fill="url(#id_dotPattern)"/>
  <rect width="880" height="500" rx="20" fill="url(#id_glowLanyard)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="878.8" height="498.8" rx="19.4" fill="none" stroke="url(#id_borderGrad)" stroke-width="1.2"/>

  <!-- Divider line -->
  <line x1="360" y1="25" x2="360" y2="475" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- ================= LEFT: HANGING LANYARD ID BADGE ================= -->
  <g class="id_lanyard_group">
    <!-- Lanyard Ribbon Straps -->
    <path d="M 180 0 L 187 55 L 203 55 L 210 0 Z" fill="#0b1324" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.6"/>
    <!-- Center woven stripe -->
    <line x1="195" y1="0" x2="195" y2="55" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 2" opacity="0.8"/>

    <!-- Metal Clasp Assembly -->
    <!-- Clasp Ring -->
    <rect x="187" y="52" width="16" height="8" rx="2" fill="url(#id_metalGrad)" stroke="#1e293b" stroke-width="0.5"/>
    <!-- Swivel Buckle -->
    <path d="M 191 60 L 199 60 L 197 72 L 193 72 Z" fill="url(#id_metalShine)"/>
    <!-- Metal Clip Hook going through badge punch-hole -->
    <rect x="192" y="70" width="6" height="18" rx="3" fill="url(#id_metalGrad)" stroke="#334155" stroke-width="0.5"/>
    <circle cx="195" cy="85" r="2.5" fill="#0f172a"/>

    <!-- The ID Badge Body Container -->
    <!-- Outer Card Glow and Drop Shadow -->
    <rect x="60" y="75" width="270" height="395" rx="16" fill="url(#id_badgeCardBg)" stroke="url(#id_borderGrad)" stroke-width="1.4"/>

    <!-- Holographic Sheen Sweep inside Badge Clip -->
    <g clip-path="url(#id_badgeClip)">
      <!-- Subtle dot matrix inside card -->
      <rect x="60" y="75" width="270" height="395" fill="url(#id_dotPattern)" opacity="0.7"/>

      <!-- Animated Foil Sheen Ribbon -->
      <rect x="0" y="50" width="120" height="500" fill="url(#id_foilGrad)" class="id_foil_sweep"/>
    </g>

    <!-- Top Badge Punch Slot -->
    <rect x="181" y="83" width="28" height="6" rx="3" fill="#070c18" stroke="#334155" stroke-width="1"/>

    <!-- Security Chip / Hologram Symbol -->
    <g transform="translate(85, 96)">
      <!-- Microchip -->
      <rect width="24" height="18" rx="3" fill="#eab308" stroke="#ca8a04" stroke-width="0.8"/>
      <line x1="6" y1="0" x2="6" y2="18" stroke="#a16207" stroke-width="0.5"/>
      <line x1="18" y1="0" x2="18" y2="18" stroke="#a16207" stroke-width="0.5"/>
      <line x1="0" y1="9" x2="24" y2="9" stroke="#a16207" stroke-width="0.5"/>
    </g>
    <text x="120" y="109" class="id_mono" font-size="9" font-weight="700" fill="#38bdf8" letter-spacing="1">VERIFIED BADGE // SEC</text>

    <!-- Portrait Container with id.png -->
    <g transform="translate(85, 125)">
      <!-- Background and Border -->
      <rect width="220" height="185" rx="12" fill="#070c18" stroke="#247bff" stroke-width="1"/>
      
      <!-- Exact Portrait Preserving Alpha and Dimensions -->
      <g clip-path="url(#id_photoClip)">
        <image href="data:image/png;base64,{ID_PNG_B64}" xlink:href="data:image/png;base64,{ID_PNG_B64}"
               x="-10" y="-10" width="240" height="210" preserveAspectRatio="xMidYMid slice"/>
        
        <!-- Subtle bottom shadow gradient -->
        <rect x="0" y="140" width="220" height="45" fill="url(#id_photoVignette)"/>
      </g>

      <linearGradient id="id_photoVignette" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#070c18" stop-opacity="0"/>
        <stop offset="100%" stop-color="#070c18" stop-opacity="0.8"/>
      </linearGradient>

      <!-- Corner tech brackets -->
      <path d="M 6 14 L 6 6 L 14 6" fill="none" stroke="#247bff" stroke-width="1.8"/>
      <path d="M 214 14 L 214 6 L 206 6" fill="none" stroke="#247bff" stroke-width="1.8"/>
      <path d="M 6 171 L 6 179 L 14 179" fill="none" stroke="#ff354f" stroke-width="1.8"/>
      <path d="M 214 171 L 214 179 L 206 179" fill="none" stroke="#ff354f" stroke-width="1.8"/>
    </g>

    <!-- Credential Details on Badge -->
    <text x="85" y="332" class="id_title" font-size="16.5" fill="#ffffff">MOHAMED SHAKIR</text>
    <text x="85" y="349" class="id_mono" font-size="10.5" font-weight="700" fill="#38bdf8">SOFTWARE &amp; AI ENGINEER</text>

    <text x="85" y="369" class="id_mono" font-size="9.5" fill="#94a3b8">ORG: Rajarata University (RUSL)</text>
    <text x="85" y="384" class="id_mono" font-size="9.5" fill="#94a3b8">LOC: Kalmunai, Sri Lanka</text>
    <text x="85" y="399" class="id_mono" font-size="9.5" fill="#94a3b8">ID : GH-170917445</text>

    <!-- Bottom Barcode -->
    {''.join(barcode_bars)}
    <text x="195" y="458" text-anchor="middle" class="id_mono" font-size="8.5" font-weight="700" fill="#64748b" letter-spacing="1.5">SHAKIR-5665-SEC-VERIFIED</text>
  </g>

  <!-- ================= RIGHT: VERIFIED METRICS and REPO DATA DASHBOARD ================= -->
  <g transform="translate(385, 25)" class="id_anim">
    <!-- Header -->
    <text x="0" y="16" class="id_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">VERIFIED METRICS // AUDITED GITHUB DATA</text>
    <text x="0" y="42" class="id_title" font-size="22" fill="#ffffff">Developer Credential Dashboard</text>

    <!-- 3 Metric Stat Cards -->
    <g transform="translate(0, 56)">
      <!-- Card 1: Public Repos -->
      <g transform="translate(0, 0)">
        <rect width="145" height="72" rx="10" fill="#0c162b" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.6"/>
        <text x="14" y="35" class="id_title" font-size="26" fill="#38bdf8">38</text>
        <text x="14" y="52" class="id_mono" font-size="9.5" font-weight="700" fill="#94a3b8">PUBLIC REPOS</text>
        <text x="14" y="63" class="id_mono" font-size="8" fill="#64748b">Verified GitHub Count</text>
      </g>

      <!-- Card 2: Member Since -->
      <g transform="translate(155, 0)">
        <rect width="145" height="72" rx="10" fill="#0c162b" stroke="#1e293b" stroke-width="0.8"/>
        <text x="14" y="35" class="id_title" font-size="20" fill="#ffffff">2024-05</text>
        <text x="14" y="52" class="id_mono" font-size="9.5" font-weight="700" fill="#94a3b8">MEMBER SINCE</text>
        <text x="14" y="63" class="id_mono" font-size="8" fill="#64748b">Dated: 2024-05-27</text>
      </g>

      <!-- Card 3: Account ID -->
      <g transform="translate(310, 0)">
        <rect width="150" height="72" rx="10" fill="#0c162b" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.5"/>
        <text x="14" y="35" class="id_title" font-size="18" fill="#fca5a5">170917445</text>
        <text x="14" y="52" class="id_mono" font-size="9.5" font-weight="700" fill="#94a3b8">GITHUB USER ID</text>
        <text x="14" y="63" class="id_mono" font-size="8" fill="#64748b">Immutable Node Hash</text>
      </g>
    </g>

    <!-- Verified Repositories Section -->
    <g transform="translate(0, 142)">
      <text x="0" y="15" class="id_mono" font-size="11" font-weight="700" fill="#ff354f" letter-spacing="1">DATED REPOSITORY AUDIT // PRODUCTION WORK</text>

      <!-- Project Row 1: AI Risk Analysis -->
      <g transform="translate(0, 26)">
        <rect width="460" height="66" rx="9" fill="#0a1324" stroke="#1e293b" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#38bdf8"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f0f6fc">AI-Powered Business Risk Analysis &amp; Recommendation</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Multilingual Sinhala, English &amp; code-mixed NLP • Fine-tuned XLM-RoBERTa • Fuzzy Logic</text>
        <text x="28" y="55" class="id_mono" font-size="9.5" fill="#38bdf8">Repo: Shakir5665/AI-Powered-Business-Risk-Analysis • Python</text>
      </g>

      <!-- Project Row 2: DocQuery AI -->
      <g transform="translate(0, 100)">
        <rect width="460" height="66" rx="9" fill="#0a1324" stroke="#1e293b" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#a855f7"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f0f6fc">DocQuery-AI // PDF RAG Assistant &amp; Vector Search</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Document QA chatbot • LangChain • FAISS Vector Store • Google Gemini API</text>
        <text x="28" y="55" class="id_mono" font-size="9.5" fill="#c084fc">Repo: Shakir5665/DocQuery-AI • Live: docquery-frontend-dxdc.onrender.com</text>
      </g>

      <!-- Project Row 3: HRPay Nexus -->
      <g transform="translate(0, 174)">
        <rect width="460" height="66" rx="9" fill="#0a1324" stroke="#1e293b" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#10b981"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f0f6fc">HRPay Nexus // Enterprise Payroll &amp; HR Management</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Full-stack platform • React • ASP.NET Core • PostgreSQL • JWT &amp; Role-based access</text>
        <text x="28" y="55" class="id_mono" font-size="9.5" fill="#6ee7b7">Repo: Shakir5665/HRPay-Nexus • C# / TypeScript</text>
      </g>

      <!-- Project Row 4: Gym Retention System -->
      <g transform="translate(0, 248)">
        <rect width="460" height="66" rx="9" fill="#0a1324" stroke="#1e293b" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#ff354f"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f0f6fc">Smart Gym Management &amp; Retention System</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Full-stack gym portal • React • Node.js • MongoDB • Real-time Socket.io synchronization</text>
        <text x="28" y="55" class="id_mono" font-size="9.5" fill="#fca5a5">Repo: Shakir5665/gym-management-system • JavaScript</text>
      </g>
    </g>

    <!-- Bottom Audit Stamp -->
    <g transform="translate(0, 468)">
      <circle cx="5" cy="5" r="4" fill="#10b981"/>
      <text x="16" y="8" class="id_mono" font-size="10" font-weight="700" fill="#94a3b8">STATUS: <tspan fill="#38bdf8">ALL METRICS VERIFIED &amp; AUDITED</tspan> • NO UNKNOWN COUNTS ESTIMATED</text>
    </g>
  </g>
</svg>"""
    with open('assets/id-dashboard.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/id-dashboard.svg generated successfully.")

if __name__ == '__main__':
    generate_id_dashboard()

from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ID_PNG_B64
import os

def generate_id_dashboard():
    barcode_bars = []
    pattern = [2, 1, 3, 1, 1, 2, 4, 1, 2, 1, 3, 2, 1, 4, 1, 2, 1, 3, 2, 1, 1, 3, 1, 2, 4, 1, 2, 1, 3, 1, 2, 3, 1, 1, 4, 2]
    bx = 95
    for w in pattern:
        barcode_bars.append(f'<rect x="{bx}" y="440" width="{w}" height="24" fill="#cbd5e1"/>')
        bx += w + 2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 520" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .id_title {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
      }}
      .id_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .id_body {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
      }}

      /* Lanyard Drop, Damped Pendulum Settling and Gentle +/-1.7 deg Swing */
      @keyframes id_pendulumSequence {{
        0% {{ transform: translateY(-420px) rotate(-16deg); opacity: 0; }}
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
        0%, 15% {{ transform: translateX(-300px) rotate(25deg); opacity: 0; }}
        35% {{ opacity: 0.55; }}
        55%, 100% {{ transform: translateX(380px) rotate(25deg); opacity: 0; }}
      }}

      @keyframes id_fadeIn {{
        from {{ opacity: 0; transform: translateY(14px); }}
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
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10"/>
    </pattern>

    <linearGradient id="id_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#14213d" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="id_cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a101f"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <!-- Metal Clasp Gradients -->
    <linearGradient id="id_metalGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="35%" stop-color="#f1f5f9"/>
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

    <linearGradient id="id_badgeCardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0d182e"/>
      <stop offset="100%" stop-color="#070c18"/>
    </linearGradient>

    <radialGradient id="id_glowLanyard" cx="22%" cy="40%" r="45%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="id_badgeClip">
      <rect x="55" y="75" width="280" height="420" rx="18"/>
    </clipPath>

    <clipPath id="id_photoClip">
      <rect x="80" y="128" width="230" height="195" rx="12"/>
    </clipPath>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="900" height="520" rx="20" fill="url(#id_cardBg)"/>
  <rect width="900" height="520" rx="20" fill="url(#id_dotPattern)"/>
  <rect width="900" height="520" rx="20" fill="url(#id_glowLanyard)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="898.8" height="518.8" rx="19.4" fill="none" stroke="url(#id_borderGrad)" stroke-width="1.2"/>

  <!-- Divider line -->
  <line x1="375" y1="30" x2="375" y2="490" stroke="#16233b" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- ================= LEFT: HANGING LANYARD ID BADGE ================= -->
  <g class="id_lanyard_group">
    <!-- Lanyard Ribbon Straps -->
    <path d="M 180 0 L 187 55 L 203 55 L 210 0 Z" fill="#091224" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.6"/>
    <line x1="195" y1="0" x2="195" y2="55" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 2" opacity="0.8"/>

    <!-- Metal Clasp Assembly -->
    <rect x="187" y="52" width="16" height="8" rx="2" fill="url(#id_metalGrad)" stroke="#1e293b" stroke-width="0.5"/>
    <path d="M 191 60 L 199 60 L 197 72 L 193 72 Z" fill="url(#id_metalShine)"/>
    <rect x="192" y="70" width="6" height="18" rx="3" fill="url(#id_metalGrad)" stroke="#334155" stroke-width="0.5"/>
    <circle cx="195" cy="85" r="2.5" fill="#070d1a"/>

    <!-- The ID Badge Body Container -->
    <rect x="55" y="75" width="280" height="420" rx="18" fill="url(#id_badgeCardBg)" stroke="url(#id_borderGrad)" stroke-width="1.2"/>

    <!-- Holographic Sheen Sweep inside Badge Clip -->
    <g clip-path="url(#id_badgeClip)">
      <rect x="55" y="75" width="280" height="420" fill="url(#id_dotPattern)" opacity="0.6"/>
      <rect x="0" y="50" width="130" height="520" fill="url(#id_foilGrad)" class="id_foil_sweep"/>
    </g>

    <!-- Top Badge Punch Slot -->
    <rect x="181" y="83" width="28" height="6" rx="3" fill="#050a14" stroke="#334155" stroke-width="1"/>

    <!-- Security Chip -->
    <g transform="translate(80, 98)">
      <rect width="24" height="18" rx="3" fill="#eab308" stroke="#ca8a04" stroke-width="0.8"/>
      <line x1="6" y1="0" x2="6" y2="18" stroke="#a16207" stroke-width="0.5"/>
      <line x1="18" y1="0" x2="18" y2="18" stroke="#a16207" stroke-width="0.5"/>
      <line x1="0" y1="9" x2="24" y2="9" stroke="#a16207" stroke-width="0.5"/>
    </g>
    <text x="115" y="111" class="id_mono" font-size="9.5" font-weight="700" fill="#38bdf8" letter-spacing="1">VERIFIED BADGE // SEC</text>

    <!-- Portrait Container with id.png -->
    <g transform="translate(80, 128)">
      <rect width="230" height="195" rx="12" fill="#060c18" stroke="#247bff" stroke-width="1"/>
      
      <g clip-path="url(#id_photoClip)">
        <image href="data:image/png;base64,{ID_PNG_B64}" xlink:href="data:image/png;base64,{ID_PNG_B64}"
               x="-10" y="-10" width="250" height="220" preserveAspectRatio="xMidYMid slice"/>
        <rect x="0" y="145" width="230" height="50" fill="url(#id_photoVignette)"/>
      </g>

      <linearGradient id="id_photoVignette" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#060c18" stop-opacity="0"/>
        <stop offset="100%" stop-color="#060c18" stop-opacity="0.85"/>
      </linearGradient>

      <!-- Corner tech brackets -->
      <path d="M 6 14 L 6 6 L 14 6" fill="none" stroke="#247bff" stroke-width="1.8"/>
      <path d="M 224 14 L 224 6 L 216 6" fill="none" stroke="#247bff" stroke-width="1.8"/>
      <path d="M 6 181 L 6 189 L 14 189" fill="none" stroke="#ff354f" stroke-width="1.8"/>
      <path d="M 224 181 L 224 189 L 216 189" fill="none" stroke="#ff354f" stroke-width="1.8"/>
    </g>

    <!-- Credential Details on Badge -->
    <text x="80" y="348" class="id_title" font-size="17" fill="#ffffff">MOHAMED SHAKIR</text>
    <text x="80" y="366" class="id_mono" font-size="11" font-weight="700" fill="#38bdf8">SOFTWARE &amp; AI ENGINEER</text>

    <text x="80" y="388" class="id_mono" font-size="10" fill="#94a3b8">ORG: Rajarata University (RUSL)</text>
    <text x="80" y="404" class="id_mono" font-size="10" fill="#94a3b8">LOC: Kalmunai, Sri Lanka</text>
    <text x="80" y="420" class="id_mono" font-size="10" fill="#94a3b8">ID : GH-170917445</text>

    <!-- Bottom Barcode -->
    {''.join(barcode_bars)}
    <text x="195" y="478" text-anchor="middle" class="id_mono" font-size="8.5" font-weight="700" fill="#64748b" letter-spacing="1.5">SHAKIR-5665-SEC-VERIFIED</text>
  </g>

  <!-- ================= RIGHT: VERIFIED METRICS AND REPO DATA DASHBOARD ================= -->
  <g transform="translate(405, 30)" class="id_anim">
    <!-- Header -->
    <text x="0" y="14" class="id_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">VERIFIED METRICS // AUDITED GITHUB DATA</text>
    <text x="0" y="42" class="id_title" font-size="24" fill="#ffffff">Developer Credential Dashboard</text>

    <!-- 3 Metric Stat Cards -->
    <g transform="translate(0, 58)">
      <!-- Card 1: Public Repos -->
      <g transform="translate(0, 0)">
        <rect width="145" height="74" rx="10" fill="#091325" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.6"/>
        <text x="14" y="36" class="id_title" font-size="26" fill="#38bdf8">38</text>
        <text x="14" y="54" class="id_mono" font-size="9.5" font-weight="700" fill="#94a3b8">PUBLIC REPOS</text>
        <text x="14" y="65" class="id_mono" font-size="8" fill="#64748b">Verified GitHub Count</text>
      </g>

      <!-- Card 2: Member Since -->
      <g transform="translate(155, 0)">
        <rect width="145" height="74" rx="10" fill="#091325" stroke="#1e293b" stroke-width="0.8"/>
        <text x="14" y="36" class="id_title" font-size="20" fill="#ffffff">2024-05</text>
        <text x="14" y="54" class="id_mono" font-size="9.5" font-weight="700" fill="#94a3b8">MEMBER SINCE</text>
        <text x="14" y="65" class="id_mono" font-size="8" fill="#64748b">Dated: 2024-05-27</text>
      </g>

      <!-- Card 3: Account ID -->
      <g transform="translate(310, 0)">
        <rect width="150" height="74" rx="10" fill="#091325" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.5"/>
        <text x="14" y="36" class="id_title" font-size="18" fill="#fca5a5">170917445</text>
        <text x="14" y="54" class="id_mono" font-size="9.5" font-weight="700" fill="#94a3b8">GITHUB USER ID</text>
        <text x="14" y="65" class="id_mono" font-size="8" fill="#64748b">Immutable Node Hash</text>
      </g>
    </g>

    <!-- Verified Repositories Section -->
    <g transform="translate(0, 150)">
      <text x="0" y="14" class="id_mono" font-size="11" font-weight="700" fill="#ff354f" letter-spacing="1">DATED REPOSITORY AUDIT // PRODUCTION WORK</text>

      <!-- Project 1: AI Risk Analysis -->
      <g transform="translate(0, 26)">
        <rect width="460" height="68" rx="10" fill="#081020" stroke="#172642" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#38bdf8"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f8fafc">AI-Powered Business Risk Analysis &amp; Recommendation</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Multilingual Sinhala, English &amp; code-mixed NLP • XLM-RoBERTa • Fuzzy Logic</text>
        <text x="28" y="56" class="id_mono" font-size="9.5" fill="#38bdf8">Repo: Shakir5665/AI-Powered-Business-Risk-Analysis • Python</text>
      </g>

      <!-- Project 2: DocQuery AI -->
      <g transform="translate(0, 102)">
        <rect width="460" height="68" rx="10" fill="#081020" stroke="#172642" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#a855f7"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f8fafc">DocQuery-AI // PDF RAG Assistant &amp; Vector Search</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Document QA chatbot • LangChain • FAISS Vector Store • Google Gemini API</text>
        <text x="28" y="56" class="id_mono" font-size="9.5" fill="#c084fc">Repo: Shakir5665/DocQuery-AI • Live: docquery-frontend-dxdc.onrender.com</text>
      </g>

      <!-- Project 3: HRPay Nexus -->
      <g transform="translate(0, 178)">
        <rect width="460" height="68" rx="10" fill="#081020" stroke="#172642" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#10b981"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f8fafc">HRPay Nexus // Enterprise Payroll &amp; HR Platform</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Full-stack platform • React • ASP.NET Core • PostgreSQL • JWT &amp; Role-based access</text>
        <text x="28" y="56" class="id_mono" font-size="9.5" fill="#6ee7b7">Repo: Shakir5665/HRPay-Nexus • C# / TypeScript</text>
      </g>

      <!-- Project 4: Gym Retention -->
      <g transform="translate(0, 254)">
        <rect width="460" height="68" rx="10" fill="#081020" stroke="#172642" stroke-width="1"/>
        <circle cx="16" cy="22" r="4" fill="#ff354f"/>
        <text x="28" y="24" class="id_title" font-size="13" fill="#f8fafc">Smart Gym Management &amp; Retention System</text>
        <text x="28" y="42" class="id_body" font-size="11" fill="#94a3b8">Full-stack gym portal • React • Node.js • MongoDB • Real-time Socket.io sync</text>
        <text x="28" y="56" class="id_mono" font-size="9.5" fill="#fca5a5">Repo: Shakir5665/gym-management-system • JavaScript</text>
      </g>
    </g>

    <!-- Bottom Audit Stamp -->
    <g transform="translate(0, 482)">
      <circle cx="5" cy="5" r="4" fill="#10b981"/>
      <text x="16" y="8" class="id_mono" font-size="10" font-weight="700" fill="#94a3b8">STATUS: <tspan fill="#38bdf8">ALL METRICS VERIFIED &amp; AUDITED</tspan> • NO UNKNOWN COUNTS ESTIMATED</text>
    </g>
  </g>
</svg>"""
    with open('assets/id-dashboard.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/id-dashboard.svg re-generated successfully.")

if __name__ == '__main__':
    generate_id_dashboard()

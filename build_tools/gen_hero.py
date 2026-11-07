from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ID_PNG_B64
import os

def generate_hero():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 340" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .hero_title {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
      }}
      .hero_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .hero_body {{
        font-family: 'Space Grotesk', sans-serif;
      }}

      /* Entrance Animations */
      @keyframes hero_fadeIn {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes hero_nameRise {{
        0% {{ transform: translateY(65px); opacity: 0; }}
        15% {{ opacity: 1; }}
        100% {{ transform: translateY(0); opacity: 1; }}
      }}
      @keyframes hero_cursorBlink {{
        0%, 49% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      @keyframes hero_pulseDot {{
        0%, 100% {{ r: 4.5px; opacity: 1; }}
        50% {{ r: 6.5px; opacity: 0.6; }}
      }}
      @keyframes hero_pulseRing {{
        0% {{ r: 4.5px; opacity: 0.8; stroke-width: 1.5; }}
        100% {{ r: 12px; opacity: 0; stroke-width: 0.5; }}
      }}
      @keyframes hero_portraitFloat {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-4px); }}
      }}

      /* 4 Cycling Roles Animation (12s total: 3s each) */
      @keyframes hero_role1 {{
        0%, 2% {{ opacity: 0; transform: translateY(10px); }}
        5%, 23% {{ opacity: 1; transform: translateY(0); }}
        26%, 98% {{ opacity: 0; transform: translateY(-10px); }}
        100% {{ opacity: 0; transform: translateY(10px); }}
      }}
      @keyframes hero_role2 {{
        0%, 24% {{ opacity: 0; transform: translateY(10px); }}
        28%, 48% {{ opacity: 1; transform: translateY(0); }}
        51%, 100% {{ opacity: 0; transform: translateY(-10px); }}
      }}
      @keyframes hero_role3 {{
        0%, 49% {{ opacity: 0; transform: translateY(10px); }}
        53%, 73% {{ opacity: 1; transform: translateY(0); }}
        76%, 100% {{ opacity: 0; transform: translateY(-10px); }}
      }}
      @keyframes hero_role4 {{
        0%, 74% {{ opacity: 0; transform: translateY(10px); }}
        78%, 97% {{ opacity: 1; transform: translateY(0); }}
        99%, 100% {{ opacity: 0; transform: translateY(-10px); }}
      }}

      .hero_anim_fade {{
        animation: hero_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}
      .hero_name_el {{
        animation: hero_nameRise 1s cubic-bezier(0.16, 1, 0.3, 1) 0.15s both;
      }}
      .hero_cursor {{
        animation: hero_cursorBlink 1s step-start infinite;
      }}
      .hero_dot {{
        animation: hero_pulseDot 2s ease-in-out infinite;
      }}
      .hero_ring {{
        animation: hero_pulseRing 2s cubic-bezier(0.2, 0.8, 0.2, 1) infinite;
      }}
      .hero_portrait_wrap {{
        animation: hero_portraitFloat 6s ease-in-out infinite;
      }}

      .hero_r1 {{ animation: hero_role1 12s ease-in-out infinite both; }}
      .hero_r2 {{ animation: hero_role2 12s ease-in-out infinite both; }}
      .hero_r3 {{ animation: hero_role3 12s ease-in-out infinite both; }}
      .hero_r4 {{ animation: hero_role4 12s ease-in-out infinite both; }}

      /* Accessibility: Reduced Motion */
      @media (prefers-reduced-motion: reduce) {{
        .hero_anim_fade, .hero_name_el, .hero_portrait_wrap {{
          animation: none !important;
          transform: none !important;
          opacity: 1 !important;
        }}
        .hero_cursor, .hero_dot, .hero_ring {{
          animation: none !important;
        }}
        .hero_r1 {{
          animation: none !important;
          opacity: 1 !important;
          transform: none !important;
        }}
        .hero_r2, .hero_r3, .hero_r4 {{
          display: none !important;
        }}
      }}
    </style>

    <!-- Gradients & Patterns -->
    <pattern id="hero_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.14"/>
    </pattern>

    <linearGradient id="hero_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#182c55" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="hero_cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1527"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="hero_nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#93c5fd"/>
    </linearGradient>

    <linearGradient id="hero_roleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>

    <radialGradient id="hero_glowBlue" cx="20%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="hero_glowCrimson" cx="80%" cy="70%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="hero_rolePillGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#122347"/>
      <stop offset="100%" stop-color="#091428"/>
    </linearGradient>

    <clipPath id="hero_nameClip">
      <rect x="40" y="88" width="560" height="68"/>
    </clipPath>

    <clipPath id="hero_portraitClip">
      <rect x="0" y="0" width="220" height="260" rx="18"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="340" rx="20" fill="url(#hero_cardBg)"/>
  <rect width="880" height="340" rx="20" fill="url(#hero_dotPattern)"/>
  <rect width="880" height="340" rx="20" fill="url(#hero_glowBlue)"/>
  <rect width="880" height="340" rx="20" fill="url(#hero_glowCrimson)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="878.8" height="338.8" rx="19.4" fill="none" stroke="url(#hero_borderGrad)" stroke-width="1.2"/>

  <!-- Top System Status Pill -->
  <g class="hero_anim_fade" style="animation-delay: 0.1s;">
    <rect x="45" y="26" width="285" height="26" rx="13" fill="#0b172d" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.5"/>
    <circle cx="58" cy="39" r="4.5" fill="#10b981" class="hero_dot"/>
    <circle cx="58" cy="39" r="4.5" fill="none" stroke="#10b981" class="hero_ring"/>
    <text x="70" y="43" class="hero_mono" font-size="10.5" font-weight="700" fill="#93c5fd" letter-spacing="1.2">SYSTEM STATUS: READY FOR HIRE</text>
  </g>

  <!-- Typed Greeting Row -->
  <g class="hero_anim_fade" style="animation-delay: 0.2s;">
    <text x="45" y="78" class="hero_mono" font-size="14" font-weight="500" fill="#64748b">
      <tspan fill="#247bff">➜</tspan> ~ <tspan fill="#94a3b8">whoami &amp;&amp; echo "Hello, world! I am"</tspan>
    </text>
    <rect x="390" y="66" width="7.5" height="15" fill="#247bff" class="hero_cursor"/>
  </g>

  <!-- Large Rising-Mask Name Reveal -->
  <g clip-path="url(#hero_nameClip)">
    <g class="hero_name_el">
      <text x="45" y="142" class="hero_title" font-size="46" fill="url(#hero_nameGrad)">MOHAMED SHAKIR</text>
    </g>
  </g>

  <!-- Specialization / Four Cycling Roles -->
  <g class="hero_anim_fade" style="animation-delay: 0.35s;">
    <text x="45" y="187" class="hero_mono" font-size="13" font-weight="700" fill="#64748b" letter-spacing="1">SPECIALIZATION // </text>

    <!-- Role Container Pill -->
    <rect x="195" y="167" width="285" height="30" rx="8" fill="url(#hero_rolePillGrad)" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
    
    <!-- Role 1: AI Engineer (Default/Fallback) -->
    <g class="hero_r1">
      <circle cx="212" cy="182" r="3.5" fill="#247bff"/>
      <text x="224" y="187" class="hero_mono" font-size="13.5" font-weight="700" fill="#60a5fa">AI Engineer</text>
    </g>

    <!-- Role 2: Software Engineer -->
    <g class="hero_r2" style="opacity: 0;">
      <circle cx="212" cy="182" r="3.5" fill="#38bdf8"/>
      <text x="224" y="187" class="hero_mono" font-size="13.5" font-weight="700" fill="#38bdf8">Software Engineer</text>
    </g>

    <!-- Role 3: Full-Stack Developer -->
    <g class="hero_r3" style="opacity: 0;">
      <circle cx="212" cy="182" r="3.5" fill="#ff354f"/>
      <text x="224" y="187" class="hero_mono" font-size="13.5" font-weight="700" fill="#fca5a5">Full-Stack Developer</text>
    </g>

    <!-- Role 4: GenAI & RAG Specialist -->
    <g class="hero_r4" style="opacity: 0;">
      <circle cx="212" cy="182" r="3.5" fill="#a855f7"/>
      <text x="224" y="187" class="hero_mono" font-size="13.5" font-weight="700" fill="#c084fc">GenAI &amp; RAG Specialist</text>
    </g>
  </g>

  <!-- One-Line Pitch -->
  <g class="hero_anim_fade" style="animation-delay: 0.45s;">
    <text x="45" y="232" class="hero_body" font-size="14.5" font-weight="400" fill="#cbd5e1">
      Architecting autonomous AI agents, enterprise RAG systems, and resilient full-stack architectures.
    </text>
  </g>

  <!-- Location / Education / Opportunities Row -->
  <g class="hero_anim_fade" style="animation-delay: 0.55s;">
    <!-- Location Chip -->
    <g transform="translate(45, 265)">
      <rect width="180" height="32" rx="10" fill="#0c162b" stroke="#1e293b" stroke-width="1"/>
      <text x="14" y="21" font-size="13">📍</text>
      <text x="36" y="21" class="hero_mono" font-size="11.5" font-weight="500" fill="#94a3b8">Kalmunai, Sri Lanka</text>
    </g>

    <!-- University Chip -->
    <g transform="translate(235, 265)">
      <rect width="185" height="32" rx="10" fill="#0c162b" stroke="#1e293b" stroke-width="1"/>
      <text x="14" y="21" font-size="13">🎓</text>
      <text x="36" y="21" class="hero_mono" font-size="11.5" font-weight="500" fill="#94a3b8">BSc IT @ RUSL</text>
    </g>

    <!-- Availability Chip -->
    <g transform="translate(430, 265)">
      <rect width="165" height="32" rx="10" fill="#0c162b" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.4"/>
      <text x="14" y="21" font-size="13">💼</text>
      <text x="36" y="21" class="hero_mono" font-size="11.5" font-weight="700" fill="#38bdf8">Remote / On-site</text>
    </g>
  </g>

  <!-- Right Side: Portrait Frame with id.png -->
  <g transform="translate(630, 35)" class="hero_portrait_wrap">
    <!-- Ambient backlight -->
    <circle cx="110" cy="130" r="105" fill="#247bff" opacity="0.18" filter="blur(20px)"/>
    
    <!-- Outer Decorative Border -->
    <rect x="-4" y="-4" width="228" height="268" rx="22" fill="none" stroke="url(#hero_borderGrad)" stroke-width="1.5"/>

    <!-- Inner Card Background -->
    <rect x="0" y="0" width="220" height="260" rx="18" fill="#0a1224"/>

    <!-- Exact Portrait (Preserving exact image and alpha) -->
    <g clip-path="url(#hero_portraitClip)">
      <image href="data:image/png;base64,{ID_PNG_B64}" xlink:href="data:image/png;base64,{ID_PNG_B64}"
             x="-15" y="-5" width="250" height="270" preserveAspectRatio="xMidYMid slice"/>
      
      <!-- Subtle bottom gradient vignette to blend into card -->
      <rect x="0" y="190" width="220" height="70" fill="url(#hero_vignette)"/>
    </g>

    <linearGradient id="hero_vignette" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a1224" stop-opacity="0"/>
      <stop offset="100%" stop-color="#0a1224" stop-opacity="0.85"/>
    </linearGradient>

    <!-- Tech Corner Crosshairs -->
    <path d="M 8 18 L 8 8 L 18 8" fill="none" stroke="#247bff" stroke-width="2"/>
    <path d="M 212 18 L 212 8 L 202 8" fill="none" stroke="#247bff" stroke-width="2"/>
    <path d="M 8 242 L 8 252 L 18 252" fill="none" stroke="#ff354f" stroke-width="2"/>
    <path d="M 212 242 L 212 252 L 202 252" fill="none" stroke="#ff354f" stroke-width="2"/>

    <!-- Floating Badge on Portrait -->
    <g transform="translate(18, 222)">
      <rect width="184" height="26" rx="13" fill="#070d1be6" stroke="#247bff" stroke-width="1"/>
      <circle cx="14" cy="13" r="3.5" fill="#38bdf8"/>
      <text x="25" y="17" class="hero_mono" font-size="10.5" font-weight="700" fill="#f0f6fc" letter-spacing="0.5">SHAKIR5665 // AI-ENG</text>
    </g>
  </g>
</svg>"""
    os.makedirs('assets', exist_ok=True)
    with open('assets/hero.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/hero.svg generated successfully.")

if __name__ == '__main__':
    generate_hero()

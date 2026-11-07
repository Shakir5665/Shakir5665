from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ID_PNG_B64
import os

def generate_hero():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 380" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .hero_title {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-weight: 700;
        letter-spacing: -0.03em;
      }}
      .hero_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .hero_body {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
      }}

      /* Entrance Animations */
      @keyframes hero_fadeIn {{
        from {{ opacity: 0; transform: translateY(14px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes hero_nameRise {{
        0% {{ transform: translateY(65px); opacity: 0; }}
        20% {{ opacity: 1; }}
        100% {{ transform: translateY(0); opacity: 1; }}
      }}
      @keyframes hero_cursorBlink {{
        0%, 49% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      @keyframes hero_pulseDot {{
        0%, 100% {{ r: 4px; opacity: 1; }}
        50% {{ r: 5.5px; opacity: 0.6; }}
      }}
      @keyframes hero_pulseRing {{
        0% {{ r: 4px; opacity: 0.8; stroke-width: 1.5; }}
        100% {{ r: 12px; opacity: 0; stroke-width: 0.5; }}
      }}
      @keyframes hero_portraitFloat {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-4px); }}
      }}

      /* 4 Cycling Roles (12s total: 3s each) */
      @keyframes hero_role1 {{
        0%, 2% {{ opacity: 0; transform: translateY(8px); }}
        5%, 23% {{ opacity: 1; transform: translateY(0); }}
        26%, 98% {{ opacity: 0; transform: translateY(-8px); }}
        100% {{ opacity: 0; transform: translateY(8px); }}
      }}
      @keyframes hero_role2 {{
        0%, 24% {{ opacity: 0; transform: translateY(8px); }}
        28%, 48% {{ opacity: 1; transform: translateY(0); }}
        51%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes hero_role3 {{
        0%, 49% {{ opacity: 0; transform: translateY(8px); }}
        53%, 73% {{ opacity: 1; transform: translateY(0); }}
        76%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes hero_role4 {{
        0%, 74% {{ opacity: 0; transform: translateY(8px); }}
        78%, 97% {{ opacity: 1; transform: translateY(0); }}
        99%, 100% {{ opacity: 0; transform: translateY(-8px); }}
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

    <pattern id="hero_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10"/>
    </pattern>

    <linearGradient id="hero_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#14213d" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="hero_cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a101f"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <linearGradient id="hero_nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#93c5fd"/>
    </linearGradient>

    <radialGradient id="hero_glowBlue" cx="15%" cy="20%" r="55%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="hero_glowCrimson" cx="85%" cy="85%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="hero_nameClip">
      <rect x="44" y="96" width="580" height="74"/>
    </clipPath>

    <clipPath id="hero_portraitClip">
      <rect x="0" y="0" width="225" height="295" rx="20"/>
    </clipPath>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="900" height="380" rx="20" fill="url(#hero_cardBg)"/>
  <rect width="900" height="380" rx="20" fill="url(#hero_dotPattern)"/>
  <rect width="900" height="380" rx="20" fill="url(#hero_glowBlue)"/>
  <rect width="900" height="380" rx="20" fill="url(#hero_glowCrimson)"/>

  <!-- Precision Hairline Border -->
  <rect x="0.6" y="0.6" width="898.8" height="378.8" rx="19.4" fill="none" stroke="url(#hero_borderGrad)" stroke-width="1.2"/>

  <!-- Left Content Column -->
  <!-- 1. Top Status Pill -->
  <g class="hero_anim_fade" style="animation-delay: 0.1s;">
    <g transform="translate(48, 36)">
      <rect width="270" height="26" rx="13" fill="#091428" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.45"/>
      <circle cx="16" cy="13" r="4" fill="#10b981" class="hero_dot"/>
      <circle cx="16" cy="13" r="4" fill="none" stroke="#10b981" class="hero_ring"/>
      <text x="28" y="17" class="hero_mono" font-size="10" font-weight="700" fill="#93c5fd" letter-spacing="1">STATUS: READY FOR AI ROLES</text>
    </g>
  </g>

  <!-- 2. Typed Greeting -->
  <g class="hero_anim_fade" style="animation-delay: 0.2s;">
    <g transform="translate(48, 86)">
      <text x="0" y="0" class="hero_mono" font-size="14" font-weight="500" fill="#64748b">
        <tspan fill="#247bff">$&gt;</tspan> <tspan fill="#cbd5e1">whoami &amp;&amp; echo "Hello, world! I am"</tspan>
      </text>
      <rect x="330" y="-12" width="8" height="15" fill="#247bff" class="hero_cursor"/>
    </g>
  </g>

  <!-- 3. Large Rising-Mask Reveal Name -->
  <g clip-path="url(#hero_nameClip)">
    <g class="hero_name_el">
      <text x="48" y="152" class="hero_title" font-size="48" fill="url(#hero_nameGrad)">MOHAMED SHAKIR</text>
    </g>
  </g>

  <!-- 4. Specialization / 4 Cycling Roles -->
  <g class="hero_anim_fade" style="animation-delay: 0.35s;">
    <g transform="translate(48, 192)">
      <text x="0" y="20" class="hero_mono" font-size="12" font-weight="700" fill="#64748b" letter-spacing="1">SPECIALIZATION // </text>

      <!-- Role Container Badge -->
      <rect x="150" y="0" width="270" height="32" rx="8" fill="#0c1830" stroke="#247bff" stroke-width="1" stroke-opacity="0.5"/>
      
      <!-- Role 1: AI Engineer -->
      <g class="hero_r1">
        <circle cx="168" cy="16" r="3.5" fill="#247bff"/>
        <text x="180" y="21" class="hero_mono" font-size="13" font-weight="700" fill="#60a5fa">AI Engineer</text>
      </g>

      <!-- Role 2: Software Engineer -->
      <g class="hero_r2" style="opacity: 0;">
        <circle cx="168" cy="16" r="3.5" fill="#38bdf8"/>
        <text x="180" y="21" class="hero_mono" font-size="13" font-weight="700" fill="#38bdf8">Software Engineer</text>
      </g>

      <!-- Role 3: Full-Stack Developer -->
      <g class="hero_r3" style="opacity: 0;">
        <circle cx="168" cy="16" r="3.5" fill="#ff354f"/>
        <text x="180" y="21" class="hero_mono" font-size="13" font-weight="700" fill="#fca5a5">Full-Stack Developer</text>
      </g>

      <!-- Role 4: GenAI & RAG Specialist -->
      <g class="hero_r4" style="opacity: 0;">
        <circle cx="168" cy="16" r="3.5" fill="#a855f7"/>
        <text x="180" y="21" class="hero_mono" font-size="13" font-weight="700" fill="#d8b4fe">GenAI &amp; RAG Specialist</text>
      </g>
    </g>
  </g>

  <!-- 5. One-Line Pitch -->
  <g class="hero_anim_fade" style="animation-delay: 0.45s;">
    <text x="48" y="254" class="hero_body" font-size="14.5" font-weight="400" fill="#94a3b8">
      Architecting autonomous AI agents, enterprise RAG systems, and resilient full-stack software.
    </text>
  </g>

  <!-- 6. Metadata Chips -->
  <g class="hero_anim_fade" style="animation-delay: 0.55s;">
    <g transform="translate(48, 292)">
      <!-- Location Chip -->
      <g transform="translate(0, 0)">
        <rect width="180" height="34" rx="8" fill="#091224" stroke="#1e293b" stroke-width="1"/>
        <text x="12" y="22" font-size="13">📍</text>
        <text x="34" y="22" class="hero_mono" font-size="11.5" font-weight="500" fill="#cbd5e1">Kalmunai, Sri Lanka</text>
      </g>

      <!-- University Chip -->
      <g transform="translate(192, 0)">
        <rect width="185" height="34" rx="8" fill="#091224" stroke="#1e293b" stroke-width="1"/>
        <text x="12" y="22" font-size="13">🎓</text>
        <text x="34" y="22" class="hero_mono" font-size="11.5" font-weight="500" fill="#cbd5e1">BSc IT @ RUSL</text>
      </g>

      <!-- Opportunities Chip -->
      <g transform="translate(389, 0)">
        <rect width="175" height="34" rx="8" fill="#091224" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.5"/>
        <text x="12" y="22" font-size="13">💼</text>
        <text x="34" y="22" class="hero_mono" font-size="11.5" font-weight="700" fill="#38bdf8">Remote / On-site</text>
      </g>
    </g>
  </g>

  <!-- Right Column: Portrait Card -->
  <g transform="translate(625, 42)" class="hero_portrait_wrap">
    <!-- Ambient halo -->
    <circle cx="112" cy="147" r="115" fill="#247bff" opacity="0.16"/>

    <!-- Outer Frame Card with Hairline Glow -->
    <rect x="-3" y="-3" width="231" height="301" rx="23" fill="none" stroke="url(#hero_borderGrad)" stroke-width="1.2"/>

    <!-- Dark Card Frame Base -->
    <rect x="0" y="0" width="225" height="295" rx="20" fill="#070c18"/>

    <!-- Inlined Portrait Preserving Exact Image & Alpha -->
    <g clip-path="url(#hero_portraitClip)">
      <image href="data:image/png;base64,{ID_PNG_B64}" xlink:href="data:image/png;base64,{ID_PNG_B64}"
             x="-15" y="-5" width="255" height="305" preserveAspectRatio="xMidYMid slice"/>

      <!-- Soft Vignette at bottom to blend into base -->
      <rect x="0" y="220" width="225" height="75" fill="url(#hero_photoVignette)"/>
    </g>

    <linearGradient id="hero_photoVignette" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#070c18" stop-opacity="0"/>
      <stop offset="100%" stop-color="#070c18" stop-opacity="0.95"/>
    </linearGradient>

    <!-- Sleek Tech Crosshairs -->
    <path d="M 10 20 L 10 10 L 20 10" fill="none" stroke="#247bff" stroke-width="2"/>
    <path d="M 215 20 L 215 10 L 205 10" fill="none" stroke="#247bff" stroke-width="2"/>
    <path d="M 10 275 L 10 285 L 20 285" fill="none" stroke="#ff354f" stroke-width="2"/>
    <path d="M 215 275 L 215 285 L 205 285" fill="none" stroke="#ff354f" stroke-width="2"/>

    <!-- Bottom Pill Tag on Portrait -->
    <g transform="translate(20, 255)">
      <rect width="185" height="28" rx="14" fill="#060a14e6" stroke="#247bff" stroke-width="0.9"/>
      <circle cx="14" cy="14" r="3.5" fill="#38bdf8"/>
      <text x="26" y="18" class="hero_mono" font-size="10.5" font-weight="700" fill="#f8fafc" letter-spacing="0.5">SHAKIR5665 // AI-ENG</text>
    </g>
  </g>
</svg>"""
    with open('assets/hero.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/hero.svg re-generated successfully.")

if __name__ == '__main__':
    generate_hero()

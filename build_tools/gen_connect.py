from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ICONS, POINTING_PNG_B64
import os

def generate_connect():
    def icon_markup(slug, color, x, y, size=24):
        d = ICONS.get(slug, '')
        scale = size / 24.0
        return f'<g transform="translate({x}, {y}) scale({scale})"><path d="{d}" fill="{color}"/></g>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 380" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .cnt_title {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: -0.3px;
      }}
      .cnt_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .cnt_body {{
        font-family: 'Space Grotesk', sans-serif;
      }}

      /* Entrance Animation */
      @keyframes cnt_fadeIn {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      /* Character Idle Float */
      @keyframes cnt_charFloatAnim {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-5px); }}
      }}

      /* Nudging Arrow Animation */
      @keyframes cnt_nudgeAnim {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(6px); }}
      }}

      /* Speech bubble pulse */
      @keyframes cnt_bubblePulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.03); }}
      }}

      .cnt_anim {{
        animation: cnt_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}
      .cnt_char {{
        animation: cnt_charFloatAnim 5s ease-in-out infinite;
      }}
      .cnt_arrow {{
        animation: cnt_nudgeAnim 1.6s ease-in-out infinite;
      }}
      .cnt_bubble {{
        transform-origin: 160px 45px;
        animation: cnt_bubblePulse 3s ease-in-out infinite;
      }}

      /* Accessibility: Reduced Motion */
      @media (prefers-reduced-motion: reduce) {{
        .cnt_anim, .cnt_char, .cnt_arrow, .cnt_bubble {{
          animation: none !important;
          transform: none !important;
        }}
      }}
    </style>

    <pattern id="cnt_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <linearGradient id="cnt_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#182c55" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="cnt_cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1527"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="cnt_socialCardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f1c36"/>
      <stop offset="100%" stop-color="#091224"/>
    </linearGradient>

    <radialGradient id="cnt_floorGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="cnt_glowRight" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="380" rx="20" fill="url(#cnt_cardBg)"/>
  <rect width="880" height="380" rx="20" fill="url(#cnt_dotPattern)"/>
  <rect width="880" height="380" rx="20" fill="url(#cnt_glowRight)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="878.8" height="378.8" rx="19.4" fill="none" stroke="url(#cnt_borderGrad)" stroke-width="1.2"/>

  <!-- ================= LEFT: POINTING CHARACTER ================= -->
  <g class="cnt_char">
    <!-- Floor Ambient Glow -->
    <ellipse cx="170" cy="340" rx="110" ry="18" fill="url(#cnt_floorGlow)"/>

    <!-- Exact Character Preserving Alpha & Dimensions -->
    <image href="data:image/png;base64,{POINTING_PNG_B64}" xlink:href="data:image/png;base64,{POINTING_PNG_B64}"
           x="30" y="55" width="280" height="295" preserveAspectRatio="xMidYMid meet"/>

    <!-- Interactive Speech Bubble -->
    <g class="cnt_bubble" transform="translate(100, 22)">
      <rect width="170" height="30" rx="15" fill="#122347" stroke="#247bff" stroke-width="1"/>
      <polygon points="40,30 50,30 45,36" fill="#122347" stroke="#247bff" stroke-width="0.8"/>
      <circle cx="16" cy="15" r="3.5" fill="#38bdf8"/>
      <text x="28" y="19" class="cnt_mono" font-size="10.5" font-weight="700" fill="#f0f6fc">LET'S CONNECT! 👉</text>
    </g>
  </g>

  <!-- ================= RIGHT: GENEROUSLY SPACED SOCIAL CARDS ================= -->
  <g transform="translate(340, 25)" class="cnt_anim">
    <!-- Header -->
    <text x="0" y="16" class="cnt_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">COMMUNICATION // CHANNELS</text>
    <text x="0" y="44" class="cnt_title" font-size="24" fill="#ffffff">Let's Build Something Intelligent</text>
    <text x="0" y="65" class="cnt_body" font-size="13" fill="#94a3b8">
      Open for AI Engineering &amp; Software opportunities • Let's discuss agents, RAG &amp; systems.
    </text>

    <!-- Social Cards Grid: 2 columns x 2 rows -->
    <!-- Card 1: LinkedIn -->
    <g transform="translate(0, 85)">
      <rect width="245" height="84" rx="12" fill="url(#cnt_socialCardBg)" stroke="#247bff" stroke-width="1" stroke-opacity="0.45"/>
      <!-- Icon Container -->
      <rect x="14" y="18" width="46" height="46" rx="10" fill="#0d1f3d" stroke="#247bff" stroke-width="0.8"/>
      {icon_markup('linkedin', '#38bdf8', 25, 29, size=24)}
      <text x="70" y="38" class="cnt_title" font-size="14.5" fill="#ffffff">LinkedIn</text>
      <text x="70" y="55" class="cnt_mono" font-size="10" fill="#94a3b8">mohamedshakir5665</text>
      <!-- Nudging Arrow -->
      <g class="cnt_arrow" transform="translate(210, 42)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Card 2: GitHub -->
    <g transform="translate(260, 85)">
      <rect width="245" height="84" rx="12" fill="url(#cnt_socialCardBg)" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.4"/>
      <!-- Icon Container -->
      <rect x="14" y="18" width="46" height="46" rx="10" fill="#131c2d" stroke="#38bdf8" stroke-width="0.8"/>
      {icon_markup('github', '#ffffff', 25, 29, size=24)}
      <text x="70" y="38" class="cnt_title" font-size="14.5" fill="#ffffff">GitHub</text>
      <text x="70" y="55" class="cnt_mono" font-size="10" fill="#94a3b8">@Shakir5665</text>
      <!-- Nudging Arrow -->
      <g class="cnt_arrow" transform="translate(210, 42)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Card 3: Email -->
    <g transform="translate(0, 185)">
      <rect width="245" height="84" rx="12" fill="url(#cnt_socialCardBg)" stroke="#ff354f" stroke-width="1" stroke-opacity="0.45"/>
      <!-- Icon Container -->
      <rect x="14" y="18" width="46" height="46" rx="10" fill="#29121a" stroke="#ff354f" stroke-width="0.8"/>
      {icon_markup('gmail', '#ff354f', 25, 29, size=24)}
      <text x="70" y="38" class="cnt_title" font-size="14.5" fill="#ffffff">Email</text>
      <text x="70" y="55" class="cnt_mono" font-size="9" fill="#94a3b8">mohamedsakir3456</text>
      <!-- Nudging Arrow -->
      <g class="cnt_arrow" transform="translate(210, 42)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#ff354f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Card 4: WhatsApp -->
    <g transform="translate(260, 185)">
      <rect width="245" height="84" rx="12" fill="url(#cnt_socialCardBg)" stroke="#10b981" stroke-width="1" stroke-opacity="0.45"/>
      <!-- Icon Container -->
      <rect x="14" y="18" width="46" height="46" rx="10" fill="#10261e" stroke="#10b981" stroke-width="0.8"/>
      {icon_markup('whatsapp', '#25d366', 25, 29, size=24)}
      <text x="70" y="38" class="cnt_title" font-size="14.5" fill="#ffffff">WhatsApp</text>
      <text x="70" y="55" class="cnt_mono" font-size="10" fill="#94a3b8">+94 75 295 8134</text>
      <!-- Nudging Arrow -->
      <g class="cnt_arrow" transform="translate(210, 42)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#25d366" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Portfolio Footer Banner -->
    <g transform="translate(0, 285)">
      <rect width="505" height="40" rx="10" fill="#091428" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.5"/>
      <circle cx="20" cy="20" r="4" fill="#38bdf8"/>
      <text x="34" y="24" class="cnt_mono" font-size="11" font-weight="700" fill="#38bdf8">PORTFOLIO // </text>
      <text x="135" y="24" class="cnt_mono" font-size="11" fill="#cbd5e1">shakir-portfolio-one-amber-87.vercel.app</text>
      <g class="cnt_arrow" transform="translate(475, 20)">
        <path d="M 0 0 L 8 0 M 5 -3 L 8 0 L 5 3" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round" fill="none"/>
      </g>
    </g>
  </g>
</svg>"""
    with open('assets/connect.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/connect.svg generated successfully.")

if __name__ == '__main__':
    generate_connect()

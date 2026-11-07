from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ICONS, POINTING_PNG_B64
import os

def generate_connect():
    def icon_markup(slug, color, x, y, size=24):
        d = ICONS.get(slug, '')
        scale = size / 24.0
        return f'<g transform="translate({x}, {y}) scale({scale})"><path d="{d}" fill="{color}"/></g>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 400" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .cnt_title {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
      }}
      .cnt_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .cnt_body {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
      }}

      @keyframes cnt_fadeIn {{
        from {{ opacity: 0; transform: translateY(14px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      @keyframes cnt_charFloatAnim {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-5px); }}
      }}

      @keyframes cnt_nudgeAnim {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(6px); }}
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

      @media (prefers-reduced-motion: reduce) {{
        .cnt_anim, .cnt_char, .cnt_arrow {{
          animation: none !important;
          transform: none !important;
        }}
      }}
    </style>

    <pattern id="cnt_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10"/>
    </pattern>

    <linearGradient id="cnt_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#14213d" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="cnt_cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a101f"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <linearGradient id="cnt_socialCardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0c162b"/>
      <stop offset="100%" stop-color="#080f1e"/>
    </linearGradient>

    <radialGradient id="cnt_floorGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="cnt_glowRight" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="900" height="400" rx="20" fill="url(#cnt_cardBg)"/>
  <rect width="900" height="400" rx="20" fill="url(#cnt_dotPattern)"/>
  <rect width="900" height="400" rx="20" fill="url(#cnt_glowRight)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="898.8" height="398.8" rx="19.4" fill="none" stroke="url(#cnt_borderGrad)" stroke-width="1.2"/>

  <!-- ================= LEFT: POINTING CHARACTER ================= -->
  <g class="cnt_char">
    <!-- Ambient Floor Glow Pedestal -->
    <ellipse cx="175" cy="355" rx="120" ry="18" fill="url(#cnt_floorGlow)"/>

    <!-- Exact Character Preserving Alpha and Proportions -->
    <image href="data:image/png;base64,{POINTING_PNG_B64}" xlink:href="data:image/png;base64,{POINTING_PNG_B64}"
           x="30" y="45" width="295" height="320" preserveAspectRatio="xMidYMid meet"/>

    <!-- Sleek Tech Badge above character -->
    <g transform="translate(95, 26)">
      <rect width="165" height="26" rx="13" fill="#0c1830e6" stroke="#247bff" stroke-width="0.8"/>
      <circle cx="14" cy="13" r="3.5" fill="#38bdf8"/>
      <text x="26" y="17" class="cnt_mono" font-size="10" font-weight="700" fill="#f0f6fc">CONNECT // BUILD 🤝</text>
    </g>
  </g>

  <!-- ================= RIGHT: GENEROUSLY SPACED SOCIAL CARDS ================= -->
  <g transform="translate(355, 30)" class="cnt_anim">
    <!-- Header -->
    <text x="0" y="14" class="cnt_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">COMMUNICATION // CHANNELS</text>
    <text x="0" y="44" class="cnt_title" font-size="24" fill="#ffffff">Let's Build Something Intelligent</text>
    <text x="0" y="66" class="cnt_body" font-size="13" fill="#94a3b8">
      Open for AI Engineering &amp; Software roles • Available for collaboration &amp; consultation.
    </text>

    <!-- Social Cards Grid: 2 columns x 2 rows -->
    <!-- Card 1: LinkedIn -->
    <g transform="translate(0, 88)">
      <rect width="240" height="88" rx="12" fill="url(#cnt_socialCardBg)" stroke="#247bff" stroke-width="1" stroke-opacity="0.45"/>
      <rect x="14" y="20" width="48" height="48" rx="10" fill="#091428" stroke="#247bff" stroke-width="0.8"/>
      {icon_markup('linkedin', '#38bdf8', 26, 32, size=24)}
      <text x="72" y="40" class="cnt_title" font-size="15" fill="#ffffff">LinkedIn</text>
      <text x="72" y="58" class="cnt_mono" font-size="10" fill="#94a3b8">mohamedshakir5665</text>
      <!-- Nudging Arrow -->
      <g class="cnt_arrow" transform="translate(206, 44)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Card 2: GitHub -->
    <g transform="translate(255, 88)">
      <rect width="240" height="88" rx="12" fill="url(#cnt_socialCardBg)" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.4"/>
      <rect x="14" y="20" width="48" height="48" rx="10" fill="#0c121e" stroke="#38bdf8" stroke-width="0.8"/>
      {icon_markup('github', '#ffffff', 26, 32, size=24)}
      <text x="72" y="40" class="cnt_title" font-size="15" fill="#ffffff">GitHub</text>
      <text x="72" y="58" class="cnt_mono" font-size="10" fill="#94a3b8">@Shakir5665</text>
      <g class="cnt_arrow" transform="translate(206, 44)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Card 3: Email -->
    <g transform="translate(0, 192)">
      <rect width="240" height="88" rx="12" fill="url(#cnt_socialCardBg)" stroke="#ff354f" stroke-width="1" stroke-opacity="0.45"/>
      <rect x="14" y="20" width="48" height="48" rx="10" fill="#200d14" stroke="#ff354f" stroke-width="0.8"/>
      {icon_markup('gmail', '#ff354f', 26, 32, size=24)}
      <text x="72" y="40" class="cnt_title" font-size="15" fill="#ffffff">Direct Email</text>
      <text x="72" y="58" class="cnt_mono" font-size="9" fill="#94a3b8">mohamedsakir3456</text>
      <g class="cnt_arrow" transform="translate(206, 44)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#ff354f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Card 4: WhatsApp -->
    <g transform="translate(255, 192)">
      <rect width="240" height="88" rx="12" fill="url(#cnt_socialCardBg)" stroke="#10b981" stroke-width="1" stroke-opacity="0.45"/>
      <rect x="14" y="20" width="48" height="48" rx="10" fill="#0d1f18" stroke="#10b981" stroke-width="0.8"/>
      {icon_markup('whatsapp', '#25d366', 26, 32, size=24)}
      <text x="72" y="40" class="cnt_title" font-size="15" fill="#ffffff">WhatsApp Direct</text>
      <text x="72" y="58" class="cnt_mono" font-size="10" fill="#94a3b8">+94 75 295 8134</text>
      <g class="cnt_arrow" transform="translate(206, 44)">
        <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" stroke="#25d366" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </g>
    </g>

    <!-- Bottom Portfolio Banner -->
    <g transform="translate(0, 296)">
      <rect width="495" height="42" rx="10" fill="#081020" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.5"/>
      <circle cx="20" cy="21" r="4" fill="#38bdf8"/>
      <text x="34" y="25" class="cnt_mono" font-size="11" font-weight="700" fill="#38bdf8">PORTFOLIO // </text>
      <text x="135" y="25" class="cnt_mono" font-size="11" fill="#e2e8f0">shakir-portfolio-one-amber-87.vercel.app</text>
      <g class="cnt_arrow" transform="translate(465, 21)">
        <path d="M 0 0 L 8 0 M 5 -3 L 8 0 L 5 3" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round" fill="none"/>
      </g>
    </g>
  </g>
</svg>"""
    with open('assets/connect.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/connect.svg re-generated successfully.")

if __name__ == '__main__':
    generate_connect()

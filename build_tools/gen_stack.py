from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ICONS
import math
import os

def generate_stack():
    def icon_markup(slug, color, x, y, size=16):
        d = ICONS.get(slug, '')
        scale = size / 24.0
        return f'<g transform="translate({x}, {y}) scale({scale})"><path d="{d}" fill="{color}"/></g>'

    def render_chip(name, slug, dot_color, x, y, width=105, height=28):
        icon_x = 9
        icon_y = (height - 15) / 2
        text_x = 29
        text_y = height / 2 + 4
        im = icon_markup(slug, '#cbd5e1', icon_x, icon_y, size=15) if slug in ICONS else ''
        return f"""<g transform="translate({x}, {y})">
          <rect width="{width}" height="{height}" rx="7" fill="#091325" stroke="#1a2b47" stroke-width="0.9"/>
          {im}
          <text x="{text_x}" y="{text_y}" class="stk_mono" font-size="11" font-weight="500" fill="#e2e8f0">{name}</text>
        </g>"""

    # Orbit math
    cx, cy = 450, 160

    def orbit_point(a, b, tilt_deg, angle_deg):
        rad = math.radians(angle_deg)
        tilt = math.radians(tilt_deg)
        ex = a * math.cos(rad)
        ey = b * math.sin(rad)
        rx = ex * math.cos(tilt) - ey * math.sin(tilt)
        ry = ex * math.sin(tilt) + ey * math.cos(tilt)
        return cx + rx, cy + ry

    # Nodes
    o1_nodes = [
        ('PyTorch', 'pytorch', '#ee4c2c', 35),
        ('LangChain', 'langchain', '#38bdf8', 155),
        ('Gemini API', 'googlegemini', '#8e75c2', 275)
    ]
    o2_nodes = [
        ('Python', 'python', '#38bdf8', 40),
        ('FastAPI', 'fastapi', '#009688', 130),
        ('.NET Core', 'dotnet', '#512bd4', 220),
        ('Node.js', 'nodedotjs', '#22c55e', 310)
    ]
    o3_nodes = [
        ('React', 'react', '#61dafb', 15),
        ('Docker', 'docker', '#2496ed', 105),
        ('PostgreSQL', 'postgresql', '#336791', 195),
        ('Next.js', 'nextdotjs', '#ffffff', 285)
    ]

    orbit_nodes_markup = []

    # Orbit 1 (Inner)
    for name, slug, col, ang in o1_nodes:
        nx, ny = orbit_point(175, 60, -14, ang)
        im = icon_markup(slug, col, -9, -9, size=18)
        orbit_nodes_markup.append(f"""
        <g transform="translate({nx:.1f}, {ny:.1f})">
          <circle cx="0" cy="0" r="19" fill="#081224" stroke="#247bff" stroke-width="1.2"/>
          {im}
          <rect x="-35" y="22" width="70" height="18" rx="5" fill="#050a14ee" stroke="#247bff" stroke-width="0.6"/>
          <text x="0" y="34.5" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#e2e8f0">{name}</text>
        </g>
        """)

    # Orbit 2 (Middle)
    for name, slug, col, ang in o2_nodes:
        nx, ny = orbit_point(280, 88, 11, ang)
        im = icon_markup(slug, col, -9, -9, size=18)
        orbit_nodes_markup.append(f"""
        <g transform="translate({nx:.1f}, {ny:.1f})">
          <circle cx="0" cy="0" r="19" fill="#081224" stroke="#38bdf8" stroke-width="1.2"/>
          {im}
          <rect x="-35" y="22" width="70" height="18" rx="5" fill="#050a14ee" stroke="#38bdf8" stroke-width="0.6"/>
          <text x="0" y="34.5" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#e2e8f0">{name}</text>
        </g>
        """)

    # Orbit 3 (Outer)
    for name, slug, col, ang in o3_nodes:
        nx, ny = orbit_point(385, 115, -5, ang)
        im = icon_markup(slug, col, -9, -9, size=18)
        orbit_nodes_markup.append(f"""
        <g transform="translate({nx:.1f}, {ny:.1f})">
          <circle cx="0" cy="0" r="19" fill="#081224" stroke="#ff354f" stroke-width="1.2"/>
          {im}
          <rect x="-35" y="22" width="70" height="18" rx="5" fill="#050a14ee" stroke="#ff354f" stroke-width="0.6"/>
          <text x="0" y="34.5" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#e2e8f0">{name}</text>
        </g>
        """)

    # Grouped chips
    row1 = [
        ('Python', 'python', '#38bdf8', 95),
        ('JavaScript', 'javascript', '#38bdf8', 115),
        ('Java', 'openjdk', '#38bdf8', 85),
        ('C#', 'csharp', '#38bdf8', 80),
        ('C++', 'cplusplus', '#38bdf8', 80),
    ]
    row2 = [
        ('PyTorch', 'pytorch', '#a855f7', 95),
        ('LangChain', 'langchain', '#a855f7', 110),
        ('Gemini API', 'googlegemini', '#a855f7', 115),
        ('RAG Systems', 'fastapi', '#a855f7', 120),
        ('AI Agents', 'docker', '#a855f7', 105),
    ]
    row3 = [
        ('FastAPI', 'fastapi', '#f87171', 95),
        ('ASP.NET Core', 'dotnet', '#f87171', 115),
        ('Node.js', 'nodedotjs', '#f87171', 95),
        ('Spring Boot', 'springboot', '#f87171', 115),
        ('React', 'react', '#f87171', 85),
        ('Next.js', 'nextdotjs', '#f87171', 95),
    ]
    row4 = [
        ('PostgreSQL', 'postgresql', '#34d399', 115),
        ('MongoDB', 'mongodb', '#34d399', 105),
        ('MySQL', 'mysql', '#34d399', 90),
        ('Docker', 'docker', '#34d399', 95),
        ('Git', 'git', '#34d399', 75),
        ('Postman', 'postman', '#34d399', 95),
    ]

    def render_row_chips(row_data, start_x, start_y, spacing=10):
        markup = []
        cur_x = start_x
        for name, slug, col, w in row_data:
            markup.append(render_chip(name, slug, col, cur_x, start_y, width=w, height=28))
            cur_x += w + spacing
        return '\n'.join(markup)

    row1_chips = render_row_chips(row1, 145, 335)
    row2_chips = render_row_chips(row2, 145, 373)
    row3_chips = render_row_chips(row3, 145, 411)
    row4_chips = render_row_chips(row4, 145, 449)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 500" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .stk_title {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
      }}
      .stk_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .stk_body {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
      }}

      @keyframes stk_fadeIn {{
        from {{ opacity: 0; transform: translateY(14px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes stk_pulseCore {{
        0%, 100% {{ r: 24px; opacity: 0.95; }}
        50% {{ r: 28px; opacity: 0.7; }}
      }}

      .stk_anim {{
        animation: stk_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}
      .stk_core {{
        animation: stk_pulseCore 3s ease-in-out infinite;
      }}

      @media (prefers-reduced-motion: reduce) {{
        .stk_anim, .stk_core {{
          animation: none !important;
          transform: none !important;
        }}
      }}
    </style>

    <pattern id="stk_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10"/>
    </pattern>

    <linearGradient id="stk_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#14213d" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="stk_cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a101f"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <radialGradient id="stk_glowCenter" cx="50%" cy="32%" r="42%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.22"/>
      <stop offset="65%" stop-color="#ff354f" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="stk_coreGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="50%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#091428"/>
    </radialGradient>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="900" height="500" rx="20" fill="url(#stk_cardBg)"/>
  <rect width="900" height="500" rx="20" fill="url(#stk_dotPattern)"/>
  <rect width="900" height="500" rx="20" fill="url(#stk_glowCenter)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="898.8" height="498.8" rx="19.4" fill="none" stroke="url(#stk_borderGrad)" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(48, 30)" class="stk_anim">
    <text x="0" y="14" class="stk_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">ARCHITECTURE &amp; TOOLS // TECH STACK</text>
    <text x="0" y="42" class="stk_title" font-size="24" fill="#ffffff">Core Tech Orbits &amp; Ecosystem</text>
  </g>

  <!-- ================= UPPER SECTION: 3 TILTED ELLIPTICAL ORBITS ================= -->
  <g class="stk_anim">
    <!-- Orbit 3 Path (Outer, rx=385, ry=115, tilt=-5deg) -->
    <ellipse cx="{cx}" cy="{cy}" rx="385" ry="115" transform="rotate(-5, {cx}, {cy})"
             fill="none" stroke="#ff354f" stroke-width="1" stroke-dasharray="6 8" stroke-opacity="0.32"/>

    <!-- Orbit 2 Path (Middle, rx=280, ry=88, tilt=+11deg) -->
    <ellipse cx="{cx}" cy="{cy}" rx="280" ry="88" transform="rotate(11, {cx}, {cy})"
             fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="5 7" stroke-opacity="0.38"/>

    <!-- Orbit 1 Path (Inner, rx=175, ry=60, tilt=-14deg) -->
    <ellipse cx="{cx}" cy="{cy}" rx="175" ry="60" transform="rotate(-14, {cx}, {cy})"
             fill="none" stroke="#247bff" stroke-width="1.2" stroke-dasharray="4 6" stroke-opacity="0.5"/>

    <!-- Orbiting Nodes with labels -->
    {''.join(orbit_nodes_markup)}

    <!-- Center Nucleus Core -->
    <g transform="translate({cx}, {cy})">
      <circle cx="0" cy="0" r="32" fill="#247bff" opacity="0.2"/>
      <circle cx="0" cy="0" r="24" fill="url(#stk_coreGrad)" stroke="#60a5fa" stroke-width="1.4" class="stk_core"/>
      <circle cx="0" cy="0" r="24" fill="none" stroke="#ff354f" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>
      <text x="0" y="-3" text-anchor="middle" class="stk_mono" font-size="9" font-weight="700" fill="#ffffff">AI • SE</text>
      <text x="0" y="8" text-anchor="middle" class="stk_mono" font-size="8" font-weight="700" fill="#93c5fd">NUCLEUS</text>
    </g>
  </g>

  <!-- ================= LOWER SECTION: GROUPED STACK CHIPS ================= -->
  <g class="stk_anim" transform="translate(48, 0)">
    <!-- Category Row 1: Languages -->
    <g transform="translate(0, 335)">
      <rect width="84" height="28" rx="6" fill="#0d1b33" stroke="#247bff" stroke-width="0.8"/>
      <text x="42" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#93c5fd">LANG</text>
    </g>
    {row1_chips}

    <!-- Category Row 2: AI / ML & GenAI -->
    <g transform="translate(0, 373)">
      <rect width="84" height="28" rx="6" fill="#1b1226" stroke="#a855f7" stroke-width="0.8"/>
      <text x="42" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#d8b4fe">AI / ML</text>
    </g>
    {row2_chips}

    <!-- Category Row 3: Systems -->
    <g transform="translate(0, 411)">
      <rect width="84" height="28" rx="6" fill="#1f1217" stroke="#ff354f" stroke-width="0.8"/>
      <text x="42" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#fca5a5">SYSTEMS</text>
    </g>
    {row3_chips}

    <!-- Category Row 4: Data/Ops -->
    <g transform="translate(0, 449)">
      <rect width="84" height="28" rx="6" fill="#0e211b" stroke="#10b981" stroke-width="0.8"/>
      <text x="42" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#6ee7b7">DATA/OPS</text>
    </g>
    {row4_chips}
  </g>
</svg>"""
    with open('assets/stack.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/stack.svg re-generated successfully.")

if __name__ == '__main__':
    generate_stack()

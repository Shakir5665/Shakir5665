from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ICONS
import math
import os

def generate_stack():
    # Helper to generate an SVG path for an icon scaled and centered in a box
    def icon_markup(slug, color, x, y, size=16):
        d = ICONS.get(slug, '')
        scale = size / 24.0
        return f'<g transform="translate({x}, {y}) scale({scale})"><path d="{d}" fill="{color}"/></g>'

    # Chip generator
    def render_chip(name, slug, color, x, y, width=105, height=28):
        icon_x = 8
        icon_y = (height - 15) / 2
        text_x = 28
        text_y = height / 2 + 4.5
        im = icon_markup(slug, color, icon_x, icon_y, size=15) if slug in ICONS else ''
        return f"""<g transform="translate({x}, {y})">
          <rect width="{width}" height="{height}" rx="7" fill="#0d182e" stroke="{color}" stroke-opacity="0.4" stroke-width="0.9"/>
          {im}
          <text x="{text_x}" y="{text_y}" class="stk_mono" font-size="11" font-weight="500" fill="#f0f6fc">{name}</text>
        </g>"""

    # Orbit path calculations
    cx, cy = 440, 150
    # Orbit 1: rx=160, ry=55, rot=-12
    # Orbit 2: rx=260, ry=80, rot=10
    # Orbit 3: rx=365, ry=105, rot=-6

    # Node positions along orbit (ellipse point rotated by angle)
    def orbit_point(a, b, tilt_deg, angle_deg):
        rad = math.radians(angle_deg)
        tilt = math.radians(tilt_deg)
        ex = a * math.cos(rad)
        ey = b * math.sin(rad)
        rx = ex * math.cos(tilt) - ey * math.sin(tilt)
        ry = ex * math.sin(tilt) + ey * math.cos(tilt)
        return cx + rx, cy + ry

    # Nodes for Orbit 1 (Inner: AI/GenAI)
    o1_nodes = [
        ('PyTorch', 'pytorch', '#ee4c2c', 30),
        ('LangChain', 'langchain', '#ffffff', 150),
        ('Gemini API', 'googlegemini', '#8e75c2', 270)
    ]
    # Orbit 2 (Middle: Backend & Core)
    o2_nodes = [
        ('Python', 'python', '#38bdf8', 45),
        ('FastAPI', 'fastapi', '#009688', 135),
        ('.NET Core', 'dotnet', '#512bd4', 225),
        ('Node.js', 'nodedotjs', '#22c55e', 315)
    ]
    # Orbit 3 (Outer: Frontend, Systems & Data)
    o3_nodes = [
        ('React', 'react', '#61dafb', 15),
        ('Docker', 'docker', '#2496ed', 105),
        ('PostgreSQL', 'postgresql', '#336791', 195),
        ('Next.js', 'nextdotjs', '#ffffff', 285)
    ]

    orbit_nodes_markup = []
    
    # Render Orbit 1 nodes
    for name, slug, col, ang in o1_nodes:
        nx, ny = orbit_point(160, 55, -12, ang)
        im = icon_markup(slug, col, -9, -9, size=18)
        orbit_nodes_markup.append(f"""
        <!-- Orbit 1 Node: {name} -->
        <g transform="translate({nx:.1f}, {ny:.1f})">
          <circle cx="0" cy="0" r="19" fill="#091427" stroke="#247bff" stroke-width="1.2"/>
          {im}
          <rect x="-35" y="22" width="70" height="18" rx="5" fill="#070c18dd" stroke="#247bff" stroke-width="0.6"/>
          <text x="0" y="34.5" text-anchor="middle" class="stk_mono" font-size="10" font-weight="700" fill="#cbd5e1">{name}</text>
        </g>
        """)

    # Render Orbit 2 nodes
    for name, slug, col, ang in o2_nodes:
        nx, ny = orbit_point(260, 80, 10, ang)
        im = icon_markup(slug, col, -9, -9, size=18)
        orbit_nodes_markup.append(f"""
        <!-- Orbit 2 Node: {name} -->
        <g transform="translate({nx:.1f}, {ny:.1f})">
          <circle cx="0" cy="0" r="19" fill="#091427" stroke="#38bdf8" stroke-width="1.2"/>
          {im}
          <rect x="-36" y="22" width="72" height="18" rx="5" fill="#070c18dd" stroke="#38bdf8" stroke-width="0.6"/>
          <text x="0" y="34.5" text-anchor="middle" class="stk_mono" font-size="10" font-weight="700" fill="#cbd5e1">{name}</text>
        </g>
        """)

    # Render Orbit 3 nodes
    for name, slug, col, ang in o3_nodes:
        nx, ny = orbit_point(365, 105, -6, ang)
        im = icon_markup(slug, col, -9, -9, size=18)
        orbit_nodes_markup.append(f"""
        <!-- Orbit 3 Node: {name} -->
        <g transform="translate({nx:.1f}, {ny:.1f})">
          <circle cx="0" cy="0" r="19" fill="#091427" stroke="#ff354f" stroke-width="1.2"/>
          {im}
          <rect x="-36" y="22" width="72" height="18" rx="5" fill="#070c18dd" stroke="#ff354f" stroke-width="0.6"/>
          <text x="0" y="34.5" text-anchor="middle" class="stk_mono" font-size="10" font-weight="700" fill="#cbd5e1">{name}</text>
        </g>
        """)

    # Chips rows in lower section
    # Row 1: Languages (5 chips)
    row1 = [
        ('Python', 'python', '#38bdf8', 95),
        ('JavaScript', 'javascript', '#f7df1e', 115),
        ('Java', 'openjdk', '#ea580c', 85),
        ('C#', 'csharp', '#a855f7', 80),
        ('C++', 'cplusplus', '#3b82f6', 80),
    ]
    # Row 2: AI/ML & GenAI (5 chips)
    row2 = [
        ('PyTorch', 'pytorch', '#ee4c2c', 95),
        ('LangChain', 'langchain', '#38bdf8', 110),
        ('Gemini API', 'googlegemini', '#8e75c2', 115),
        ('RAG Systems', 'fastapi', '#10b981', 120),
        ('AI Agents', 'docker', '#ff354f', 105),
    ]
    # Row 3: Backend & Frontend (6 chips)
    row3 = [
        ('FastAPI', 'fastapi', '#009688', 95),
        ('ASP.NET', 'dotnet', '#512bd4', 100),
        ('Node.js', 'nodedotjs', '#22c55e', 95),
        ('Spring Boot', 'springboot', '#6db33f', 115),
        ('React', 'react', '#61dafb', 85),
        ('Next.js', 'nextdotjs', '#ffffff', 95),
    ]
    # Row 4: Databases & Tools (6 chips)
    row4 = [
        ('PostgreSQL', 'postgresql', '#336791', 115),
        ('MongoDB', 'mongodb', '#47a248', 105),
        ('MySQL', 'mysql', '#00758f', 90),
        ('Docker', 'docker', '#2496ed', 95),
        ('Git', 'git', '#f05032', 75),
        ('Postman', 'postman', '#ff6c37', 95),
    ]

    def render_row_chips(row_data, start_x, start_y, spacing=10):
        markup = []
        cur_x = start_x
        for name, slug, col, w in row_data:
            markup.append(render_chip(name, slug, col, cur_x, start_y, width=w, height=28))
            cur_x += w + spacing
        return '\n'.join(markup)

    row1_chips = render_row_chips(row1, 140, 310)
    row2_chips = render_row_chips(row2, 140, 348)
    row3_chips = render_row_chips(row3, 140, 386)
    row4_chips = render_row_chips(row4, 140, 424)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 475" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .stk_title {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: -0.3px;
      }}
      .stk_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .stk_body {{
        font-family: 'Space Grotesk', sans-serif;
      }}

      /* Entrance Animation */
      @keyframes stk_fadeIn {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes stk_pulseCore {{
        0%, 100% {{ r: 24px; opacity: 0.9; }}
        50% {{ r: 28px; opacity: 0.7; }}
      }}
      @keyframes stk_orbitSpin1 {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      @keyframes stk_orbitSpin2 {{
        from {{ transform: rotate(360deg); }}
        to {{ transform: rotate(0deg); }}
      }}
      @keyframes stk_orbitSpin3 {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      .stk_anim {{
        animation: stk_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}
      .stk_core {{
        animation: stk_pulseCore 3s ease-in-out infinite;
      }}

      /* Accessibility: Reduced Motion */
      @media (prefers-reduced-motion: reduce) {{
        .stk_anim, .stk_core {{
          animation: none !important;
          transform: none !important;
        }}
      }}
    </style>

    <pattern id="stk_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <linearGradient id="stk_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#182c55" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="stk_cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1527"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <radialGradient id="stk_glowCenter" cx="50%" cy="32%" r="40%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#ff354f" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="stk_coreGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="50%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#0d1f45"/>
    </radialGradient>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="475" rx="20" fill="url(#stk_cardBg)"/>
  <rect width="880" height="475" rx="20" fill="url(#stk_dotPattern)"/>
  <rect width="880" height="475" rx="20" fill="url(#stk_glowCenter)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="878.8" height="473.8" rx="19.4" fill="none" stroke="url(#stk_borderGrad)" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(45, 26)" class="stk_anim">
    <text x="0" y="16" class="stk_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">ARCHITECTURE &amp; TOOLS // TECH STACK</text>
    <text x="0" y="42" class="stk_title" font-size="22" fill="#ffffff">Core Tech Orbits &amp; Ecosystem</text>
  </g>

  <!-- ================= UPPER SECTION: 3 TILTED ELLIPTICAL ORBITS ================= -->
  <g class="stk_anim">
    <!-- Orbit 3 Path (Outer, rx=365, ry=105, tilt=-6deg) -->
    <ellipse cx="{cx}" cy="{cy}" rx="365" ry="105" transform="rotate(-6, {cx}, {cy})"
             fill="none" stroke="#ff354f" stroke-width="1" stroke-dasharray="6 8" stroke-opacity="0.35"/>

    <!-- Orbit 2 Path (Middle, rx=260, ry=80, tilt=+10deg) -->
    <ellipse cx="{cx}" cy="{cy}" rx="260" ry="80" transform="rotate(10, {cx}, {cy})"
             fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="5 7" stroke-opacity="0.4"/>

    <!-- Orbit 1 Path (Inner, rx=160, ry=55, tilt=-12deg) -->
    <ellipse cx="{cx}" cy="{cy}" rx="160" ry="55" transform="rotate(-12, {cx}, {cy})"
             fill="none" stroke="#247bff" stroke-width="1.2" stroke-dasharray="4 6" stroke-opacity="0.55"/>

    <!-- Orbiting Nodes with labels -->
    {''.join(orbit_nodes_markup)}

    <!-- Center Nucleus Core -->
    <g transform="translate({cx}, {cy})">
      <!-- Glow aura -->
      <circle cx="0" cy="0" r="32" fill="#247bff" opacity="0.2"/>
      <circle cx="0" cy="0" r="24" fill="url(#stk_coreGrad)" stroke="#60a5fa" stroke-width="1.5" class="stk_core"/>
      <circle cx="0" cy="0" r="24" fill="none" stroke="#ff354f" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
      <text x="0" y="-3" text-anchor="middle" class="stk_mono" font-size="9" font-weight="700" fill="#ffffff">AI • SE</text>
      <text x="0" y="8" text-anchor="middle" class="stk_mono" font-size="8" font-weight="700" fill="#93c5fd">NUCLEUS</text>
    </g>
  </g>

  <!-- ================= LOWER SECTION: GROUPED STACK CHIPS ================= -->
  <g class="stk_anim" transform="translate(45, 0)">
    <!-- Category Row 1: Languages -->
    <g transform="translate(0, 310)">
      <rect width="80" height="28" rx="6" fill="#132247" stroke="#247bff" stroke-width="0.8"/>
      <text x="40" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#93c5fd">LANG</text>
    </g>
    {row1_chips}

    <!-- Category Row 2: AI / ML & GenAI -->
    <g transform="translate(0, 348)">
      <rect width="80" height="28" rx="6" fill="#20132b" stroke="#a855f7" stroke-width="0.8"/>
      <text x="40" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#d8b4fe">AI / ML</text>
    </g>
    {row2_chips}

    <!-- Category Row 3: Backend & Web -->
    <g transform="translate(0, 386)">
      <rect width="80" height="28" rx="6" fill="#20141b" stroke="#ff354f" stroke-width="0.8"/>
      <text x="40" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#fca5a5">SYSTEMS</text>
    </g>
    {row3_chips}

    <!-- Category Row 4: Databases & Tools -->
    <g transform="translate(0, 424)">
      <rect width="80" height="28" rx="6" fill="#0f2420" stroke="#10b981" stroke-width="0.8"/>
      <text x="40" y="18" text-anchor="middle" class="stk_mono" font-size="9.5" font-weight="700" fill="#6ee7b7">DATA/OPS</text>
    </g>
    {row4_chips}
  </g>
</svg>"""
    with open('assets/stack.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/stack.svg generated successfully.")

if __name__ == '__main__':
    generate_stack()

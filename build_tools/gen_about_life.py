from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT
import os

def generate_about_life():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 380" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .abt_title {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
      }}
      .abt_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .abt_body {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
      }}

      /* Entrance */
      @keyframes abt_fadeIn {{
        from {{ opacity: 0; transform: translateY(14px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      .abt_anim {{
        animation: abt_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}

      /* 3-Slide Carousel: 12s total (4s each) */
      @keyframes abt_slide1 {{
        0%, 1% {{ opacity: 0; transform: translateY(8px); }}
        4%, 30% {{ opacity: 1; transform: translateY(0); }}
        33%, 99% {{ opacity: 0; transform: translateY(-8px); }}
        100% {{ opacity: 0; transform: translateY(8px); }}
      }}
      @keyframes abt_slide2 {{
        0%, 32% {{ opacity: 0; transform: translateY(8px); }}
        35%, 63% {{ opacity: 1; transform: translateY(0); }}
        66%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes abt_slide3 {{
        0%, 65% {{ opacity: 0; transform: translateY(8px); }}
        68%, 96% {{ opacity: 1; transform: translateY(0); }}
        99%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}

      /* Segment Progress Bars (4s each in 12s loop) */
      @keyframes abt_prog1 {{
        0% {{ width: 0px; }}
        33.33% {{ width: 122px; }}
        100% {{ width: 122px; }}
      }}
      @keyframes abt_prog2 {{
        0%, 33.33% {{ width: 0px; }}
        66.66% {{ width: 122px; }}
        100% {{ width: 122px; }}
      }}
      @keyframes abt_prog3 {{
        0%, 66.66% {{ width: 0px; }}
        100% {{ width: 122px; }}
      }}

      .abt_s1 {{ animation: abt_slide1 12s cubic-bezier(0.4, 0, 0.2, 1) infinite both; }}
      .abt_s2 {{ animation: abt_slide2 12s cubic-bezier(0.4, 0, 0.2, 1) infinite both; }}
      .abt_s3 {{ animation: abt_slide3 12s cubic-bezier(0.4, 0, 0.2, 1) infinite both; }}

      .abt_p1 {{ animation: abt_prog1 12s linear infinite both; }}
      .abt_p2 {{ animation: abt_prog2 12s linear infinite both; }}
      .abt_p3 {{ animation: abt_prog3 12s linear infinite both; }}

      @media (prefers-reduced-motion: reduce) {{
        .abt_anim, .abt_p1, .abt_p2, .abt_p3 {{
          animation: none !important;
          transform: none !important;
        }}
        .abt_p1 {{ width: 122px !important; }}
        .abt_p2, .abt_p3 {{ width: 0px !important; }}
        .abt_s1 {{
          animation: none !important;
          opacity: 1 !important;
          transform: none !important;
        }}
        .abt_s2, .abt_s3 {{
          display: none !important;
        }}
      }}
    </style>

    <pattern id="abt_dotPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10"/>
    </pattern>

    <linearGradient id="abt_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#14213d" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="abt_cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a101f"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <linearGradient id="abt_innerCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0c162b"/>
      <stop offset="100%" stop-color="#080f1e"/>
    </linearGradient>

    <radialGradient id="abt_glowLeft" cx="15%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="abt_glowRight" cx="85%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="abt_barClip">
      <rect width="122" height="4" rx="2"/>
    </clipPath>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="900" height="380" rx="20" fill="url(#abt_cardBg)"/>
  <rect width="900" height="380" rx="20" fill="url(#abt_dotPattern)"/>
  <rect width="900" height="380" rx="20" fill="url(#abt_glowLeft)"/>
  <rect width="900" height="380" rx="20" fill="url(#abt_glowRight)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="898.8" height="378.8" rx="19.4" fill="none" stroke="url(#abt_borderGrad)" stroke-width="1.2"/>

  <!-- Center Divider Line -->
  <line x1="440" y1="35" x2="440" y2="345" stroke="#16233b" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- ================= LEFT COLUMN: CAPABILITIES ================= -->
  <g transform="translate(45, 32)" class="abt_anim">
    <!-- Header -->
    <text x="0" y="14" class="abt_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">PILLARS // EXPERTISE</text>
    <text x="0" y="42" class="abt_title" font-size="24" fill="#ffffff">Technical Capabilities</text>

    <!-- Card 1: Autonomous AI & RAG -->
    <g transform="translate(0, 60)">
      <rect width="365" height="74" rx="12" fill="url(#abt_innerCard)" stroke="#1a2a47" stroke-width="1"/>
      <rect x="14" y="16" width="42" height="42" rx="10" fill="#102040" stroke="#247bff" stroke-width="0.8"/>
      <!-- AI Icon -->
      <path d="M 27 30 L 43 30 M 27 37 L 39 37 M 27 44 L 43 44" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
      <circle cx="41" cy="37" r="2.5" fill="#247bff"/>

      <text x="68" y="32" class="abt_title" font-size="14" fill="#f8fafc">Autonomous AI Agents &amp; RAG</text>
      <text x="68" y="50" class="abt_body" font-size="11.5" fill="#94a3b8">Multi-turn LLMs • Function calling • Vector search (FAISS, Atlas)</text>
      <text x="68" y="64" class="abt_mono" font-size="9.5" fill="#38bdf8">LangChain • Google Gemini • Prompt pipelines</text>
    </g>

    <!-- Card 2: Distributed Backend & APIs -->
    <g transform="translate(0, 146)">
      <rect width="365" height="74" rx="12" fill="url(#abt_innerCard)" stroke="#1a2a47" stroke-width="1"/>
      <rect x="14" y="16" width="42" height="42" rx="10" fill="#241424" stroke="#ff354f" stroke-width="0.8"/>
      <!-- Backend Icon -->
      <path d="M 27 28 L 43 28 L 43 46 L 27 46 Z M 27 34 L 43 34 M 27 40 L 43 40" stroke="#ff354f" stroke-width="1.8" fill="none"/>

      <text x="68" y="32" class="abt_title" font-size="14" fill="#f8fafc">Scalable Distributed Backend</text>
      <text x="68" y="50" class="abt_body" font-size="11.5" fill="#94a3b8">High-throughput microservices • Clean architecture • JWT Auth</text>
      <text x="68" y="64" class="abt_mono" font-size="9.5" fill="#fca5a5">FastAPI • ASP.NET Core • Node.js • Spring Boot</text>
    </g>

    <!-- Card 3: Cloud & Modern Engineering -->
    <g transform="translate(0, 232)">
      <rect width="365" height="74" rx="12" fill="url(#abt_innerCard)" stroke="#1a2a47" stroke-width="1"/>
      <rect x="14" y="16" width="42" height="42" rx="10" fill="#10251f" stroke="#10b981" stroke-width="0.8"/>
      <!-- Cloud/DB Icon -->
      <circle cx="35" cy="37" r="9" stroke="#10b981" stroke-width="1.8" fill="none"/>
      <path d="M 35 31 L 35 37 L 39 40" stroke="#10b981" stroke-width="1.6" stroke-linecap="round"/>

      <text x="68" y="32" class="abt_title" font-size="14" fill="#f8fafc">Cloud, Data &amp; Systems</text>
      <text x="68" y="50" class="abt_body" font-size="11.5" fill="#94a3b8">Containerized workflows • ACID compliance • Real-time sync</text>
      <text x="68" y="64" class="abt_mono" font-size="9.5" fill="#6ee7b7">Docker • PostgreSQL • MongoDB • Socket.io</text>
    </g>
  </g>

  <!-- ================= RIGHT COLUMN: 3-SLIDE CAROUSEL ================= -->
  <g transform="translate(470, 32)" class="abt_anim">
    <!-- Header Row -->
    <text x="0" y="14" class="abt_mono" font-size="11" font-weight="700" fill="#ff354f" letter-spacing="1.2">LIFE &amp; INTERESTS // 4S ROTATION</text>

    <!-- 3 Segment Progress Bars -->
    <g transform="translate(0, 26)">
      <!-- Segment 1 Track -->
      <g transform="translate(0, 0)">
        <rect width="125" height="4" rx="2" fill="#142138"/>
        <g clip-path="url(#abt_barClip)">
          <rect class="abt_p1" height="4" rx="2" fill="#247bff"/>
        </g>
      </g>
      <!-- Segment 2 Track -->
      <g transform="translate(133, 0)">
        <rect width="125" height="4" rx="2" fill="#142138"/>
        <g clip-path="url(#abt_barClip)">
          <rect class="abt_p2" height="4" rx="2" fill="#ff354f"/>
        </g>
      </g>
      <!-- Segment 3 Track -->
      <g transform="translate(266, 0)">
        <rect width="125" height="4" rx="2" fill="#142138"/>
        <g clip-path="url(#abt_barClip)">
          <rect class="abt_p3" height="4" rx="2" fill="#10b981"/>
        </g>
      </g>
    </g>

    <!-- Carousel Container Card -->
    <g transform="translate(0, 44)">
      <rect width="390" height="262" rx="16" fill="url(#abt_innerCard)" stroke="#1a2a47" stroke-width="1"/>

      <!-- ============ SLIDE 1: Exploring Emerging Technologies ============ -->
      <g class="abt_s1" transform="translate(24, 24)">
        <rect x="0" y="0" width="180" height="24" rx="6" fill="#102040" stroke="#247bff" stroke-width="0.8"/>
        <text x="12" y="16" class="abt_mono" font-size="10" font-weight="700" fill="#38bdf8">01 // RESEARCH &amp; AI</text>

        <text x="0" y="52" class="abt_title" font-size="21" fill="#ffffff">Exploring Emerging Tech</text>

        <text x="0" y="80" class="abt_body" font-size="13" fill="#cbd5e1">
          Deeply passionate about frontier LLM architectures,
        </text>
        <text x="0" y="101" class="abt_body" font-size="13" fill="#cbd5e1">
          agentic workflows, transformer attention dynamics,
        </text>
        <text x="0" y="122" class="abt_body" font-size="13" fill="#cbd5e1">
          and pushing the boundaries of intelligent software.
        </text>

        <!-- Highlights -->
        <g transform="translate(0, 142)">
          <rect x="0" y="0" width="105" height="28" rx="6" fill="#091428" stroke="#247bff" stroke-width="0.8"/>
          <text x="12" y="18" class="abt_mono" font-size="11" fill="#93c5fd">⚡ Agentic AI</text>

          <rect x="115" y="0" width="105" height="28" rx="6" fill="#091428" stroke="#247bff" stroke-width="0.8"/>
          <text x="127" y="18" class="abt_mono" font-size="11" fill="#93c5fd">🧠 RAG Systems</text>

          <rect x="230" y="0" width="105" height="28" rx="6" fill="#091428" stroke="#247bff" stroke-width="0.8"/>
          <text x="242" y="18" class="abt_mono" font-size="11" fill="#93c5fd">🔬 Research</text>
        </g>

        <text x="0" y="202" class="abt_mono" font-size="11" fill="#64748b" font-style="italic">
          "Finding smarter ways to engineer intelligent software."
        </text>
      </g>

      <!-- ============ SLIDE 2: Building Personal Projects ============ -->
      <g class="abt_s2" transform="translate(24, 24)" style="opacity: 0;">
        <rect x="0" y="0" width="180" height="24" rx="6" fill="#241422" stroke="#ff354f" stroke-width="0.8"/>
        <text x="12" y="16" class="abt_mono" font-size="10" font-weight="700" fill="#fca5a5">02 // CREATION &amp; BUILD</text>

        <text x="0" y="52" class="abt_title" font-size="21" fill="#ffffff">Building Personal Projects</text>

        <text x="0" y="80" class="abt_body" font-size="13" fill="#cbd5e1">
          Translating cutting-edge machine learning research
        </text>
        <text x="0" y="101" class="abt_body" font-size="13" fill="#cbd5e1">
          into practical, scalable, and resilient applications
        </text>
        <text x="0" y="122" class="abt_body" font-size="13" fill="#cbd5e1">
          that solve authentic, high-impact enterprise problems.
        </text>

        <!-- Highlights -->
        <g transform="translate(0, 142)">
          <rect x="0" y="0" width="105" height="28" rx="6" fill="#1c0f18" stroke="#ff354f" stroke-width="0.8"/>
          <text x="12" y="18" class="abt_mono" font-size="11" fill="#fca5a5">🛠️ DocQuery AI</text>

          <rect x="115" y="0" width="105" height="28" rx="6" fill="#1c0f18" stroke="#ff354f" stroke-width="0.8"/>
          <text x="127" y="18" class="abt_mono" font-size="11" fill="#fca5a5">📊 Risk Analysis</text>

          <rect x="230" y="0" width="105" height="28" rx="6" fill="#1c0f18" stroke="#ff354f" stroke-width="0.8"/>
          <text x="242" y="18" class="abt_mono" font-size="11" fill="#fca5a5">🚀 HRPay Nexus</text>
        </g>

        <text x="0" y="202" class="abt_mono" font-size="11" fill="#64748b" font-style="italic">
          "Transforming bold concepts into resilient software."
        </text>
      </g>

      <!-- ============ SLIDE 3: Open-Source Contribution ============ -->
      <g class="abt_s3" transform="translate(24, 24)" style="opacity: 0;">
        <rect x="0" y="0" width="190" height="24" rx="6" fill="#10251f" stroke="#10b981" stroke-width="0.8"/>
        <text x="12" y="16" class="abt_mono" font-size="10" font-weight="700" fill="#6ee7b7">03 // COMMUNITY &amp; DEV</text>

        <text x="0" y="52" class="abt_title" font-size="21" fill="#ffffff">Open-Source Contribution</text>

        <text x="0" y="80" class="abt_body" font-size="13" fill="#cbd5e1">
          Active contributor to open-source software ecosystems,
        </text>
        <text x="0" y="101" class="abt_body" font-size="13" fill="#cbd5e1">
          collaborative university portals (FOT Hub), and
        </text>
        <text x="0" y="122" class="abt_body" font-size="13" fill="#cbd5e1">
          continuous community-driven knowledge sharing.
        </text>

        <!-- Highlights -->
        <g transform="translate(0, 142)">
          <rect x="0" y="0" width="115" height="28" rx="6" fill="#091b15" stroke="#10b981" stroke-width="0.8"/>
          <text x="12" y="18" class="abt_mono" font-size="11" fill="#6ee7b7">🤝 FOT Hub Dev</text>

          <rect x="125" y="0" width="105" height="28" rx="6" fill="#091b15" stroke="#10b981" stroke-width="0.8"/>
          <text x="137" y="18" class="abt_mono" font-size="11" fill="#6ee7b7">🌱 Code Reviews</text>

          <rect x="240" y="0" width="95" height="28" rx="6" fill="#091b15" stroke="#10b981" stroke-width="0.8"/>
          <text x="252" y="18" class="abt_mono" font-size="11" fill="#6ee7b7">🌐 38+ Repos</text>
        </g>

        <text x="0" y="202" class="abt_mono" font-size="11" fill="#64748b" font-style="italic">
          "Continuous learning through open collaboration."
        </text>
      </g>
    </g>
  </g>
</svg>"""
    with open('assets/about-life.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/about-life.svg re-generated successfully.")

if __name__ == '__main__':
    generate_about_life()

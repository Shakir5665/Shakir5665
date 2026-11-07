from shared import COMMON_FONTS_CSS, FONT_LICENSE_COMMENT, ICONS
import os

def generate_about_life():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 340" width="100%" height="100%">
  {FONT_LICENSE_COMMENT}
  <defs>
    <style>
      {COMMON_FONTS_CSS}

      .abt_title {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: -0.3px;
      }}
      .abt_mono {{
        font-family: 'JetBrains Mono', monospace;
      }}
      .abt_body {{
        font-family: 'Space Grotesk', sans-serif;
      }}

      /* Entrance */
      @keyframes abt_fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      .abt_anim {{
        animation: abt_fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}

      /* 3-Slide Carousel: 12s total (4s per slide) */
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
        33.33% {{ width: 110px; }}
        100% {{ width: 110px; }}
      }}
      @keyframes abt_prog2 {{
        0%, 33.33% {{ width: 0px; }}
        66.66% {{ width: 110px; }}
        100% {{ width: 110px; }}
      }}
      @keyframes abt_prog3 {{
        0%, 66.66% {{ width: 0px; }}
        100% {{ width: 110px; }}
      }}

      .abt_s1 {{ animation: abt_slide1 12s cubic-bezier(0.4, 0, 0.2, 1) infinite both; }}
      .abt_s2 {{ animation: abt_slide2 12s cubic-bezier(0.4, 0, 0.2, 1) infinite both; }}
      .abt_s3 {{ animation: abt_slide3 12s cubic-bezier(0.4, 0, 0.2, 1) infinite both; }}

      .abt_p1 {{ animation: abt_prog1 12s linear infinite both; }}
      .abt_p2 {{ animation: abt_prog2 12s linear infinite both; }}
      .abt_p3 {{ animation: abt_prog3 12s linear infinite both; }}

      /* Accessibility: Reduced Motion */
      @media (prefers-reduced-motion: reduce) {{
        .abt_anim, .abt_p1, .abt_p2, .abt_p3 {{
          animation: none !important;
          transform: none !important;
        }}
        .abt_p1 {{ width: 110px !important; }}
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
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <linearGradient id="abt_borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#182c55" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="abt_cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1527"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="abt_innerCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f1c35"/>
      <stop offset="100%" stop-color="#0a1324"/>
    </linearGradient>

    <radialGradient id="abt_glowLeft" cx="15%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="abt_glowRight" cx="85%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="abt_barClip">
      <rect width="110" height="4" rx="2"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="340" rx="20" fill="url(#abt_cardBg)"/>
  <rect width="880" height="340" rx="20" fill="url(#abt_dotPattern)"/>
  <rect width="880" height="340" rx="20" fill="url(#abt_glowLeft)"/>
  <rect width="880" height="340" rx="20" fill="url(#abt_glowRight)"/>

  <!-- Border Hairline -->
  <rect x="0.6" y="0.6" width="878.8" height="338.8" rx="19.4" fill="none" stroke="url(#abt_borderGrad)" stroke-width="1.2"/>

  <!-- Divider line between left and right columns -->
  <line x1="430" y1="25" x2="430" y2="315" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- ================= LEFT COLUMN: CAPABILITIES ================= -->
  <g transform="translate(35, 25)" class="abt_anim">
    <!-- Header -->
    <text x="0" y="16" class="abt_mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.2">PILLARS // EXPERTISE</text>
    <text x="0" y="42" class="abt_title" font-size="22" fill="#ffffff">Technical Capabilities</text>

    <!-- Capability 1: Autonomous AI & RAG -->
    <g transform="translate(0, 58)">
      <rect width="365" height="70" rx="10" fill="url(#abt_innerCard)" stroke="#1e293b" stroke-width="1"/>
      <!-- Icon Container -->
      <rect x="12" y="14" width="42" height="42" rx="8" fill="#122347" stroke="#247bff" stroke-width="0.8"/>
      <path d="M 23 27 L 33 27 M 23 35 L 43 35 M 23 43 L 37 43" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
      <circle cx="39" cy="27" r="2" fill="#247bff"/>
      
      <text x="64" y="30" class="abt_title" font-size="13.5" fill="#f0f6fc">Autonomous AI Agents &amp; RAG</text>
      <text x="64" y="47" class="abt_body" font-size="11" fill="#94a3b8">Gemini API • LangChain • Vector search (FAISS, Atlas) • Function calling</text>
      <text x="64" y="60" class="abt_mono" font-size="9.5" fill="#38bdf8">Agentic workflows • Multi-turn RAG • NLP</text>
    </g>

    <!-- Capability 2: Full-Stack & Microservices -->
    <g transform="translate(0, 136)">
      <rect width="365" height="70" rx="10" fill="url(#abt_innerCard)" stroke="#1e293b" stroke-width="1"/>
      <!-- Icon Container -->
      <rect x="12" y="14" width="42" height="42" rx="8" fill="#21152a" stroke="#ff354f" stroke-width="0.8"/>
      <path d="M 25 26 L 41 26 L 41 44 L 25 44 Z M 25 32 L 41 32" stroke="#ff354f" stroke-width="1.8" fill="none"/>
      
      <text x="64" y="30" class="abt_title" font-size="13.5" fill="#f0f6fc">Distributed Backend &amp; APIs</text>
      <text x="64" y="47" class="abt_body" font-size="11" fill="#94a3b8">FastAPI • ASP.NET Core • Node.js • Spring Boot • Clean architecture</text>
      <text x="64" y="60" class="abt_mono" font-size="9.5" fill="#fca5a5">High-throughput REST • JWT Auth • Rate limiting</text>
    </g>

    <!-- Capability 3: Cloud & Modern Engineering -->
    <g transform="translate(0, 214)">
      <rect width="365" height="70" rx="10" fill="url(#abt_innerCard)" stroke="#1e293b" stroke-width="1"/>
      <!-- Icon Container -->
      <rect x="12" y="14" width="42" height="42" rx="8" fill="#13242e" stroke="#10b981" stroke-width="0.8"/>
      <circle cx="33" cy="35" r="9" stroke="#10b981" stroke-width="1.8" fill="none"/>
      <path d="M 33 29 L 33 35 L 37 38" stroke="#10b981" stroke-width="1.5" stroke-linecap="round"/>

      <text x="64" y="30" class="abt_title" font-size="13.5" fill="#f0f6fc">Production Data &amp; Systems</text>
      <text x="64" y="47" class="abt_body" font-size="11" fill="#94a3b8">Docker containers • PostgreSQL • MongoDB • Real-time Socket.io</text>
      <text x="64" y="60" class="abt_mono" font-size="9.5" fill="#6ee7b7">ACID compliance • Caching • CI/CD workflows</text>
    </g>
  </g>

  <!-- ================= RIGHT COLUMN: 3-SLIDE CAROUSEL ================= -->
  <g transform="translate(460, 25)" class="abt_anim">
    <!-- Header Row -->
    <text x="0" y="16" class="abt_mono" font-size="11" font-weight="700" fill="#ff354f" letter-spacing="1.2">LIFE &amp; INTERESTS // 4S ROTATION</text>
    
    <!-- 3 Segment Progress Bars -->
    <g transform="translate(0, 30)">
      <!-- Segment 1 Track -->
      <g transform="translate(0, 0)">
        <rect width="115" height="4" rx="2" fill="#152338"/>
        <g clip-path="url(#abt_barClip)">
          <rect class="abt_p1" height="4" rx="2" fill="#247bff"/>
        </g>
      </g>
      <!-- Segment 2 Track -->
      <g transform="translate(125, 0)">
        <rect width="115" height="4" rx="2" fill="#152338"/>
        <g clip-path="url(#abt_barClip)">
          <rect class="abt_p2" height="4" rx="2" fill="#ff354f"/>
        </g>
      </g>
      <!-- Segment 3 Track -->
      <g transform="translate(250, 0)">
        <rect width="115" height="4" rx="2" fill="#152338"/>
        <g clip-path="url(#abt_barClip)">
          <rect class="abt_p3" height="4" rx="2" fill="#10b981"/>
        </g>
      </g>
    </g>

    <!-- Carousel Container Card -->
    <g transform="translate(0, 48)">
      <rect width="385" height="236" rx="14" fill="url(#abt_innerCard)" stroke="#1e293b" stroke-width="1"/>

      <!-- ============ SLIDE 1: Exploring Emerging Technologies ============ -->
      <g class="abt_s1" transform="translate(20, 24)">
        <!-- Category Tag -->
        <rect x="0" y="0" width="165" height="22" rx="6" fill="#122347" stroke="#247bff" stroke-width="0.8"/>
        <text x="10" y="15" class="abt_mono" font-size="10" font-weight="700" fill="#38bdf8">01 // INNOVATION &amp; AI</text>

        <!-- Slide Title -->
        <text x="0" y="48" class="abt_title" font-size="20" fill="#ffffff">Exploring Emerging Tech</text>

        <!-- Description -->
        <text x="0" y="74" class="abt_body" font-size="12.5" fill="#cbd5e1">
          Deeply curious about breakthrough developments in
        </text>
        <text x="0" y="93" class="abt_body" font-size="12.5" fill="#cbd5e1">
          large language models, agentic workflows, transformer
        </text>
        <text x="0" y="112" class="abt_body" font-size="12.5" fill="#cbd5e1">
          architectures, and high-performance computing.
        </text>

        <!-- Bullet Highlights -->
        <g transform="translate(0, 130)">
          <!-- Chip 1 -->
          <rect x="0" y="0" width="105" height="26" rx="6" fill="#0d182e" stroke="#247bff" stroke-width="0.8"/>
          <text x="10" y="17" class="abt_mono" font-size="10.5" fill="#93c5fd">⚡ Agentic AI</text>

          <!-- Chip 2 -->
          <rect x="115" y="0" width="100" height="26" rx="6" fill="#0d182e" stroke="#247bff" stroke-width="0.8"/>
          <text x="125" y="17" class="abt_mono" font-size="10.5" fill="#93c5fd">🧠 RAG Pipelines</text>

          <!-- Chip 3 -->
          <rect x="225" y="0" width="115" height="26" rx="6" fill="#0d182e" stroke="#247bff" stroke-width="0.8"/>
          <text x="235" y="17" class="abt_mono" font-size="10.5" fill="#93c5fd">🔬 Research</text>
        </g>

        <!-- Micro Quote -->
        <text x="0" y="182" class="abt_mono" font-size="10.5" fill="#64748b" font-style="italic">
          "Finding smarter ways to build intelligent software."
        </text>
      </g>

      <!-- ============ SLIDE 2: Building Personal Projects ============ -->
      <g class="abt_s2" transform="translate(20, 24)" style="opacity: 0;">
        <!-- Category Tag -->
        <rect x="0" y="0" width="170" height="22" rx="6" fill="#241320" stroke="#ff354f" stroke-width="0.8"/>
        <text x="10" y="15" class="abt_mono" font-size="10" font-weight="700" fill="#fca5a5">02 // CREATION &amp; BUILD</text>

        <!-- Slide Title -->
        <text x="0" y="48" class="abt_title" font-size="20" fill="#ffffff">Building Personal Projects</text>

        <!-- Description -->
        <text x="0" y="74" class="abt_body" font-size="12.5" fill="#cbd5e1">
          Translating complex machine learning algorithms
        </text>
        <text x="0" y="93" class="abt_body" font-size="12.5" fill="#cbd5e1">
          and system architectures into reliable, production-ready
        </text>
        <text x="0" y="112" class="abt_body" font-size="12.5" fill="#cbd5e1">
          applications solving authentic real-world challenges.
        </text>

        <!-- Bullet Highlights -->
        <g transform="translate(0, 130)">
          <!-- Chip 1 -->
          <rect x="0" y="0" width="105" height="26" rx="6" fill="#1e101a" stroke="#ff354f" stroke-width="0.8"/>
          <text x="10" y="17" class="abt_mono" font-size="10.5" fill="#fca5a5">🛠️ DocQuery AI</text>

          <!-- Chip 2 -->
          <rect x="115" y="0" width="105" height="26" rx="6" fill="#1e101a" stroke="#ff354f" stroke-width="0.8"/>
          <text x="125" y="17" class="abt_mono" font-size="10.5" fill="#fca5a5">📊 Risk Analysis</text>

          <!-- Chip 3 -->
          <rect x="230" y="0" width="110" height="26" rx="6" fill="#1e101a" stroke="#ff354f" stroke-width="0.8"/>
          <text x="240" y="17" class="abt_mono" font-size="10.5" fill="#fca5a5">🚀 HRPay Nexus</text>
        </g>

        <!-- Micro Quote -->
        <text x="0" y="182" class="abt_mono" font-size="10.5" fill="#64748b" font-style="italic">
          "Transforming bold concepts into resilient software."
        </text>
      </g>

      <!-- ============ SLIDE 3: Open-Source Contribution ============ -->
      <g class="abt_s3" transform="translate(20, 24)" style="opacity: 0;">
        <!-- Category Tag -->
        <rect x="0" y="0" width="185" height="22" rx="6" fill="#11241f" stroke="#10b981" stroke-width="0.8"/>
        <text x="10" y="15" class="abt_mono" font-size="10" font-weight="700" fill="#6ee7b7">03 // COMMUNITY &amp; DEV</text>

        <!-- Slide Title -->
        <text x="0" y="48" class="abt_title" font-size="20" fill="#ffffff">Open-Source Contribution</text>

        <!-- Description -->
        <text x="0" y="74" class="abt_body" font-size="12.5" fill="#cbd5e1">
          Active participant in collaborative developer initiatives,
        </text>
        <text x="0" y="93" class="abt_body" font-size="12.5" fill="#cbd5e1">
          university student portal development (FOT Hub), and
        </text>
        <text x="0" y="112" class="abt_body" font-size="12.5" fill="#cbd5e1">
          continuous peer knowledge sharing across open repos.
        </text>

        <!-- Bullet Highlights -->
        <g transform="translate(0, 130)">
          <!-- Chip 1 -->
          <rect x="0" y="0" width="115" height="26" rx="6" fill="#0d1f19" stroke="#10b981" stroke-width="0.8"/>
          <text x="10" y="17" class="abt_mono" font-size="10.5" fill="#6ee7b7">🤝 FOT Hub Dev</text>

          <!-- Chip 2 -->
          <rect x="125" y="0" width="105" height="26" rx="6" fill="#0d1f19" stroke="#10b981" stroke-width="0.8"/>
          <text x="135" y="17" class="abt_mono" font-size="10.5" fill="#6ee7b7">🌱 Code Reviews</text>

          <!-- Chip 3 -->
          <rect x="240" y="0" width="105" height="26" rx="6" fill="#0d1f19" stroke="#10b981" stroke-width="0.8"/>
          <text x="250" y="17" class="abt_mono" font-size="10.5" fill="#6ee7b7">🌐 38+ Repos</text>
        </g>

        <!-- Micro Quote -->
        <text x="0" y="182" class="abt_mono" font-size="10.5" fill="#64748b" font-style="italic">
          "Continuous learning through open collaboration."
        </text>
      </g>
    </g>
  </g>
</svg>"""
    with open('assets/about-life.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("assets/about-life.svg generated successfully.")

if __name__ == '__main__':
    generate_about_life()

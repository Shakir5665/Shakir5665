import base64
import json
import os

with open('assets/fonts/SpaceGrotesk-Bold.woff2', 'rb') as f:
    SPACE_GROTESK_B64 = base64.b64encode(f.read()).decode('ascii')

with open('assets/fonts/JetBrainsMono-Medium.woff2', 'rb') as f:
    JB_MONO_MED_B64 = base64.b64encode(f.read()).decode('ascii')

with open('assets/fonts/JetBrainsMono-Bold.woff2', 'rb') as f:
    JB_MONO_BOLD_B64 = base64.b64encode(f.read()).decode('ascii')

with open('id.png', 'rb') as f:
    ID_PNG_B64 = base64.b64encode(f.read()).decode('ascii')

with open('right_pointing.png', 'rb') as f:
    POINTING_PNG_B64 = base64.b64encode(f.read()).decode('ascii')

with open('assets/icons.json', 'r') as f:
    ICONS = json.load(f)

FONT_LICENSE_COMMENT = """<!--
  EMBEDDED FONTS LICENSES:
  1. Space Grotesk (Bold): Copyright 2020 The Space Grotesk Project Authors.
     Licensed under the SIL Open Font License, Version 1.1 (OFL-1.1).
  2. JetBrains Mono (Medium, Bold): Copyright 2020 The JetBrains Mono Project Authors.
     Licensed under the SIL Open Font License, Version 1.1 (OFL-1.1).
  Full license text is included in assets/fonts/LICENSE.txt.
-->"""

COMMON_FONTS_CSS = f"""
    @font-face {{
      font-family: 'Space Grotesk';
      font-style: normal;
      font-weight: 700;
      font-display: swap;
      src: url('data:font/woff2;base64,{SPACE_GROTESK_B64}') format('woff2');
    }}
    @font-face {{
      font-family: 'JetBrains Mono';
      font-style: normal;
      font-weight: 500;
      font-display: swap;
      src: url('data:font/woff2;base64,{JB_MONO_MED_B64}') format('woff2');
    }}
    @font-face {{
      font-family: 'JetBrains Mono';
      font-style: normal;
      font-weight: 700;
      font-display: swap;
      src: url('data:font/woff2;base64,{JB_MONO_BOLD_B64}') format('woff2');
    }}
"""

print("shared.py loaded successfully. Font and image assets ready.")

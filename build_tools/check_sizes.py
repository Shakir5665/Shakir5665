import base64
import os

files = {
    'font_space': 'assets/fonts/SpaceGrotesk-Bold.woff2',
    'font_mono_med': 'assets/fonts/JetBrainsMono-Medium.woff2',
    'font_mono_bold': 'assets/fonts/JetBrainsMono-Bold.woff2',
    'id_png': 'id.png',
    'pointing_png': 'right_pointing.png'
}

for k, p in files.items():
    if os.path.exists(p):
        size = os.path.getsize(p)
        print(f"{k} ({p}): {size:,} bytes")
    else:
        print(f"MISSING: {p}")

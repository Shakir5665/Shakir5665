import urllib.request
import re
import os

os.makedirs('assets/fonts', exist_ok=True)

# Fetch css from google fonts with a modern user-agent that receives woff2
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def download_font(family, weight, out_name):
    url = f"https://fonts.googleapis.com/css2?family={family}:wght@{weight}&display=swap"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        css = resp.read().decode('utf-8')
    
    # find latin woff2 url
    # Usually the latin block is marked with /* latin */
    matches = re.findall(r'/\* latin \*/\s*@font-face\s*\{[^}]*src:\s*url\((https://[^)]+\.woff2)\)', css)
    if not matches:
        # fallback to any woff2
        matches = re.findall(r'src:\s*url\((https://[^)]+\.woff2)\)', css)
    
    if matches:
        font_url = matches[0]
        print(f"Downloading {family} from {font_url}")
        req2 = urllib.request.Request(font_url, headers=headers)
        with urllib.request.urlopen(req2) as resp2:
            data = resp2.read()
        out_path = f"assets/fonts/{out_name}.woff2"
        with open(out_path, 'wb') as f:
            f.write(data)
        print(f"Saved {out_path} ({len(data)} bytes)")
        return out_path
    else:
        print(f"Could not find woff2 for {family}")
        return None

download_font('Space+Grotesk', '700', 'SpaceGrotesk-Bold')
download_font('JetBrains+Mono', '500', 'JetBrainsMono-Medium')
download_font('JetBrains+Mono', '700', 'JetBrainsMono-Bold')

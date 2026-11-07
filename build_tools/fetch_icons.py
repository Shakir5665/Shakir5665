import urllib.request
import json
import re

slugs = [
    'python', 'javascript', 'openjdk', 'cplusplus', 'csharp',
    'react', 'nextdotjs', 'fastapi', 'dotnet', 'nodedotjs', 'springboot',
    'pytorch', 'langchain', 'googlegemini',
    'postgresql', 'mongodb', 'mysql',
    'docker', 'git', 'postman', 'swagger',
    'linkedin', 'github', 'whatsapp', 'gmail'
]

icons = {}

for slug in slugs:
    try:
        url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/master/icons/{slug}.svg"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            svg = resp.read().decode('utf-8')
            # extract path
            m = re.search(r'<path d="([^"]+)"', svg)
            if m:
                icons[slug] = m.group(1)
                print(f"Loaded {slug}")
            else:
                print(f"No path in {slug}")
    except Exception as e:
        print(f"Failed {slug}: {e}")

with open('assets/icons.json', 'w') as f:
    json.dump(icons, f, indent=2)

print(f"Total icons saved: {len(icons)}")

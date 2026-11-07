import urllib.request
import json
import re

slugs = [
    'python', 'javascript', 'openjdk', 'csharp', 'cplusplus',
    'react', 'nextdotjs', 'fastapi', 'dotnet', 'nodedotjs', 'springboot',
    'pytorch', 'langchain', 'googlegemini',
    'postgresql', 'mongodb', 'mysql',
    'docker', 'git', 'postman', 'swagger',
    'linkedin', 'github', 'whatsapp', 'gmail', 'vercel'
]

icons = {}
for s in slugs:
    url = f"https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/{s}.svg"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        m = re.search(r'<path d="([^"]+)"', content)
        if m:
            icons[s] = m.group(1)
            print(f"Loaded {s}")
        else:
            print(f"Could not extract path from {s}")

with open('assets/icons.json', 'w') as f:
    json.dump(icons, f, indent=2)

print(f"All {len(icons)} icons loaded successfully!")

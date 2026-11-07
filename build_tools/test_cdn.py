import urllib.request

urls = [
    "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/linkedin.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/csharp.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/c.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/cplusplus.svg",
    "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/vercel.svg",
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            print(f"Success: {u} -> {len(resp.read())} bytes")
    except Exception as e:
        print(f"Failed {u}: {e}")

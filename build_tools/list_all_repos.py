import urllib.request, json
req = urllib.request.Request('https://api.github.com/users/Shakir5665/repos?per_page=100', headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
repos = json.loads(resp.read().decode('utf-8'))
for r in repos:
    print(f"{r['name']} - {r['html_url']}")

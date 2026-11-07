import urllib.request
import json

req = urllib.request.Request('https://api.github.com/users/Shakir5665/repos?per_page=100&sort=updated', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
        print(f"Total repos: {len(repos)}")
        for r in repos[:15]:
            print(f"- {r['name']} (Stars: {r['stargazers_count']}, Forks: {r['forks_count']}, Lang: {r['language']}, Updated: {r['updated_at'][:10]})")
except Exception as e:
    print("Error:", e)

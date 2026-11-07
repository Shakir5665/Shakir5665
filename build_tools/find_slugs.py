import urllib.request
import json
import re

req = urllib.request.Request('https://raw.githubusercontent.com/simple-icons/simple-icons/master/_data/simple-icons.json', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for item in data['icons']:
    t = item['title'].lower()
    if 'linkedin' in t or 'c sharp' in t or 'c#' in t or 'portfolio' in t or 'globe' in t:
        print(item['title'], '--> slug:', item.get('slug'))

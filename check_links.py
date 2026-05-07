import os
import re
import urllib.request
import urllib.error

directory = 'src_docs/md/posts'
pattern = re.compile(r'\[.*\]\((.*?)\)\{\s*\.fl-help-cta\s*\}')

broken_links = []

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            matches = pattern.findall(content)
            for url in matches:
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        if response.getcode() >= 400:
                            print(f"{filepath}: {url} -> {response.getcode()}")
                            broken_links.append((filepath, url))
                except urllib.error.HTTPError as e:
                    print(f"{filepath}: {url} -> {e.code}")
                    broken_links.append((filepath, url))
                except Exception as e:
                    print(f"{filepath}: {url} -> {e}")
                    broken_links.append((filepath, url))

if not broken_links:
    print("All CTA links are working perfectly!")
else:
    print(f"Found {len(broken_links)} broken links.")

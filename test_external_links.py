import os
import re
import glob
import urllib.request
import urllib.error
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed

MD_DIR = "src_docs/md"

def extract_links(content):
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    return [l.strip() for l in links if l and not l.startswith('#') and '{' not in l]

def check_link(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req, timeout=5, context=ctx)
        return url, True, None
    except urllib.error.HTTPError as e:
        if e.code in [403, 401]:
            return url, True, None
        return url, False, f"HTTP {e.code}"
    except Exception as e:
        return url, False, str(e)

def verify_all_links():
    files = glob.glob(f"{MD_DIR}/**/*.md", recursive=True)
    all_links = set()
    link_to_files = {}
    
    for fpath in files:
        if not os.path.exists(fpath): continue
        with open(fpath, 'r', encoding='utf-8') as f:
            links = extract_links(f.read())
        for l in set(links):
            if l.startswith(('http://', 'https://')) and 'localhost' not in l and '127.0.0.1' not in l:
                all_links.add(l)
                if l not in link_to_files: link_to_files[l] = []
                link_to_files[l].append(fpath)

    broken_links = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_link, url): url for url in all_links}
        for future in as_completed(futures):
            url, ok, err = future.result()
            if not ok:
                for fpath in link_to_files[url]:
                    broken_links.append((fpath, url, err))

    print(f"Found {len(broken_links)} broken external links.")
    for fpath, link, err in broken_links:
        print(f"[{os.path.basename(fpath)}] {link} -> {err}")

if __name__ == '__main__':
    verify_all_links()

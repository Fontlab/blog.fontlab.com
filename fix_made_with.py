import glob
import re

for filepath in glob.glob('src_docs/md/posts/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()
        
    match = re.search(r'^title:\s*(.+)$', content, flags=re.MULTILINE)
    if match:
        old_title = match.group(1)
        if "made with fontlab" in old_title.lower():
            new_title = old_title.replace("made with fontlab", "Made with FontLab")
            if new_title != old_title:
                print(f"Updating {filepath}: {old_title} -> {new_title}")
                content = content.replace(f"title: {old_title}", f"title: {new_title}")
                with open(filepath, 'w') as f:
                    f.write(content)


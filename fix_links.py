import os

base_dir = "reference/fldoc/src/fontlab/8/md"
urls_to_fix = [
    "https://help.fontlab.com/fontlab/8/manual/Hinting/",
    "https://help.fontlab.com/fontlab/8/manual/Color-fonts/",
    "https://help.fontlab.com/fontlab/8/tutorials/briem/2-0-basics/",
    "https://help.fontlab.com/fontlab/8/manual/Glyphs/Anchors/",
    "https://help.fontlab.com/fontlab/8/manual/Glyphs/Drawing/",
    "https://help.fontlab.com/fontlab/8/manual/Scripting/",
    "https://help.fontlab.com/fontlab/8/tutorials/briem/3-0-decisions/",
    "https://help.fontlab.com/fontlab/8/manual/Spacing-and-kerning/",
    "https://help.fontlab.com/fontlab/8/manual/Variable-fonts/Design-space/",
    "https://help.fontlab.com/fontlab/8/manual/OpenType-features/",
    "https://help.fontlab.com/fontlab/8/manual/Variable-fonts/",
    "https://help.fontlab.com/fontlab/8/tutorials/briem/4-2-bold/"
]

for url in urls_to_fix:
    # Extract path from URL
    # e.g. https://help.fontlab.com/fontlab/8/manual/Hinting/ -> manual/Hinting
    path = url.replace("https://help.fontlab.com/fontlab/8/", "").strip("/")
    
    local_path = os.path.join(base_dir, path)
    if os.path.isdir(local_path):
        # Find first md file
        md_files = [f for f in sorted(os.listdir(local_path)) if f.endswith('.md')]
        if 'index.md' in md_files:
            print(f"URL OK (has index.md): {url}")
        elif md_files:
            # No index.md, use the first md file, removing .md extension
            new_page = md_files[0].replace('.md', '')
            new_url = f"{url}{new_page}/"
            print(f"REPLACE: {url} -> {new_url}")
        else:
            print(f"NO MD FILES: {url}")
    else:
        print(f"DIR NOT FOUND: {url} ({local_path})")

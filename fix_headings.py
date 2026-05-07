import os, glob

MD_DIR = "src_docs/md/posts"
# Manually mapped replacements to preserve proper nouns
REPLACEMENTS = {
    "what hinting actually is": "What hinting actually is",
    "the trap of overlapping contours": "The trap of overlapping contours",
    "the .glyphspackage opening": "The .glyphspackage opening",
    "the moral": "The moral",
    "More from Fábio Duarte Martins": "More from Fábio Duarte Martins",
    "The Proposals": "The proposals",
    "Color Palettes": "Color palettes",
    "Relation to Existing Solutions": "Relation to existing solutions",
    "More from Dave Lawrence": "More from Dave Lawrence",
    "the boring 90%": "The boring 90%",
}

# Find all bad headings again
def is_title_case(heading):
    words = heading.split()
    if len(words) < 2: return False
    cap_count = sum(1 for w in words if w.istitle())
    return cap_count / len(words) > 0.5

def is_lowercase(heading):
    return heading == heading.lower()

files = glob.glob(f"{MD_DIR}/*.md")
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    changed = False
    for i, line in enumerate(lines):
        if line.startswith('#'):
            h_text = line.lstrip('#').strip()
            
            # Use manual replacement if defined
            if h_text in REPLACEMENTS:
                prefix = line[:line.find(h_text)]
                lines[i] = prefix + REPLACEMENTS[h_text]
                changed = True
                continue
                
            # Otherwise apply basic heuristics
            if is_title_case(h_text) or (is_lowercase(h_text) and len(h_text.split()) > 1):
                # We need to capitalize first letter, make others lower EXCEPT FontLab, OpenType, etc.
                # Actually, let's just print the ones that still need mapping
                print(f"NEEDS MAPPING: {h_text}")


import os
import re
import glob

MD_DIR = "src_docs/md/posts"
BULLSHIT_WORDS = ["revolutionary", "delve", "furthermore", "in conclusion", "cutting-edge", "game-changer", "innovative", "synergy", "paradigm shift", "leverage", "disrupt", "transformative"]

def is_title_case(heading):
    words = heading.split()
    if len(words) < 2: return False
    # If more than half of the words (excluding short words) are capitalized, it's likely title case
    cap_count = sum(1 for w in words if w.istitle())
    return cap_count / len(words) > 0.5

def is_lowercase(heading):
    return heading == heading.lower()

def check_files():
    files = glob.glob(f"{MD_DIR}/*.md")
    
    issues = {"headings": [], "bullshit": [], "short": []}
    
    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check length
        if len(content.split()) < 100:
            issues["short"].append(fpath)
            
        # Check bullshit words
        content_lower = content.lower()
        found_bs = []
        for bw in BULLSHIT_WORDS:
            if bw in content_lower:
                found_bs.append(bw)
        if found_bs:
            issues["bullshit"].append((fpath, found_bs))
            
        # Check headings
        for line in content.split('\n'):
            if line.startswith('#'):
                # Strip # and spaces
                heading = line.lstrip('#').strip()
                if not heading: continue
                
                if is_title_case(heading):
                    issues["headings"].append((fpath, "Title Case", heading))
                elif is_lowercase(heading) and len(heading.split()) > 1:
                    # Ignore single word lowercase as it might be code or single term
                    issues["headings"].append((fpath, "All Lowercase", heading))

    print(f"Found {len(issues['short'])} unusually short articles.")
    print(f"Found {len(issues['bullshit'])} articles with corporate fluff/hype words.")
    print(f"Found {len(issues['headings'])} headings with wrong case.")
    
    print("\n--- HYPE WORDS ---")
    for fpath, bs in issues['bullshit']:
        print(f"{os.path.basename(fpath)}: {', '.join(bs)}")
        
    print("\n--- BAD HEADINGS (Sample of 10) ---")
    for fpath, issue, h in issues['headings'][:10]:
        print(f"{os.path.basename(fpath)}: [{issue}] {h}")

check_files()

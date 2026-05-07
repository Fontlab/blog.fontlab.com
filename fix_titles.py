import os
import glob
import re

def sentence_case(title):
    if not title:
        return title
    
    # Remove quotes if present
    has_quotes = False
    if title.startswith('"') and title.endswith('"'):
        has_quotes = True
        title = title[1:-1]
        
    # Capitalize first letter
    title = title[0].upper() + title[1:]
    
    # Fix proper nouns
    replacements = {
        r'\bfontlab\b': 'FontLab',
        r'\btranstype\b': 'TransType',
        r'\bvexy lines\b': 'Vexy Lines',
        r'\bopentype\b': 'OpenType',
        r'\bpython\b': 'Python',
        r'\bmac\b': 'Mac',
        r'\bwindows\b': 'Windows',
        r'\bpostscript\b': 'PostScript',
        r'\btype 1\b': 'Type 1',
        r'\bcss\b': 'CSS',
        r'\bui\b': 'UI',
        r'\bux\b': 'UX',
        r'\bhangul\b': 'Hangul',
        r'\bcyrillic\b': 'Cyrillic',
        r'\bcjk\b': 'CJK',
        r'\bcolrv1\b': 'COLRv1',
        r'\bsvg\b': 'SVG',
        r'\bpdf\b': 'PDF',
        r'\beps\b': 'EPS',
        r'\bpng\b': 'PNG',
        r'\bjpg\b': 'JPG',
        r'\bwoff2\b': 'WOFF2',
        r'\bwoff\b': 'WOFF',
        r'\bttf\b': 'TTF',
        r'\botf\b': 'OTF',
        r'\bgithub\b': 'GitHub',
        r'\bapple\b': 'Apple',
        r'\bgoogle\b': 'Google',
        r'\bmicrosoft\b': 'Microsoft',
        r'\badobe\b': 'Adobe',
        r'\bmozilla\b': 'Mozilla',
        r'\bmacos\b': 'macOS',
        r'\blinux\b': 'Linux',
        r'\bcalfonts\b': 'Calfonts',
        r'\bbriem\b': 'Briem',
        r'\bfrank griesshammer\b': 'Frank Griesshammer',
        r'\bvassil kateliev\b': 'Vassil Kateliev',
        r'\byuri gordon\b': 'Yuri Gordon',
        r'\beduardo tunni\b': 'Eduardo Tunni',
        r'\bnate piekos\b': 'Nate Piekos',
        r'\bpatrick griffin\b': 'Patrick Griffin',
        r'\balexander kapusta\b': 'Alexander Kapusta',
        r'\bdave lawrence\b': 'Dave Lawrence',
        r'\bfábio duarte martins\b': 'Fábio Duarte Martins',
    }
    
    for pattern, replacement in replacements.items():
        title = re.sub(pattern, replacement, title, flags=re.IGNORECASE)
        
    if has_quotes:
        return f'"{title}"'
    return title

for filepath in glob.glob('src_docs/md/posts/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Find title
    match = re.search(r'^title:\s*(.+)$', content, flags=re.MULTILINE)
    if match:
        old_title = match.group(1)
        # Check if it's mostly lowercase (ignoring first char and quotes)
        clean_title = old_title.strip('"\'')
        if clean_title and clean_title[1:].islower() or clean_title.islower():
            new_title = sentence_case(old_title)
            if new_title != old_title:
                print(f"Updating {filepath}: {old_title} -> {new_title}")
                content = content.replace(f"title: {old_title}", f"title: {new_title}")
                with open(filepath, 'w') as f:
                    f.write(content)


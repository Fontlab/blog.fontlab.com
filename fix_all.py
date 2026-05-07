import os

replacements = {
    "https://help.fontlab.com/fontlab/8/manual/Hinting/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/manual/Color-fonts/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://www.fontlab.com/made-with-fontlab/": "https://fontlab.com/",
    "https://help.fontlab.com/fontlab/8/tutorials/briem/2-0-basics/": "https://help.fontlab.com/fontlab/8/tutorials/briem/2-0-basics/briem-2-01-basics/",
    "https://help.fontlab.com/fontlab/8/manual/Glyphs/Anchors/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/manual/Glyphs/Drawing/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/manual/Scripting/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/tutorials/briem/3-0-decisions/": "https://help.fontlab.com/fontlab/8/tutorials/briem/3-0-decisions/briem-3-01-decisions/",
    "https://help.fontlab.com/fontlab/8/manual/Spacing-and-kerning/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/manual/Variable-fonts/Design-space/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/manual/OpenType-features/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/manual/Variable-fonts/": "https://help.fontlab.com/fontlab/8/manual/",
    "https://help.fontlab.com/fontlab/8/tutorials/briem/4-2-bold/": "https://help.fontlab.com/fontlab/8/tutorials/briem/4-2-bold/briem-4-21-exercise2/",
    "https://help.fontlab.com/fontlab/8/tutorials/calfonts/1.%20Drawing/01b%20Basics%20of%20Drawing%20in%20FontLab/": "https://help.fontlab.com/fontlab/8/tutorials/calfonts/",
    "https://help.fontlab.com/fontlab/8/tutorials/calfonts/6.%20Italics/6a%20Intro%20to%20Italics/": "https://help.fontlab.com/fontlab/8/tutorials/calfonts/"
}

directory = 'src_docs/md/posts'
files_fixed = 0

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            files_fixed += 1
            print(f"Fixed {filepath}")

print(f"Total files fixed: {files_fixed}")

import os, glob
MD_DIR = "src_docs/md/posts"
for fpath in glob.glob(f"{MD_DIR}/*.md"):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if len(content.split()) < 100:
        print(f"{os.path.basename(fpath)}: {len(content.split())} words")

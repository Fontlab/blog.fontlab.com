#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
# this_file: tools/inject_illu.py
"""Inject pencil-sketch thumbnail references into every blog post.

Adds ![title](../media/illu/{slug}.png){ .illu-thumb } as the first body
element after the YAML frontmatter so the blog plugin picks it up as the
post's hero / excerpt thumbnail. Idempotent: skips posts that already
reference the illustration.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "src_docs/md/posts"
ILLU = ROOT / "src_docs/md/media/illu"


def slug_for(stem: str) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)


def inject(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, flags=re.DOTALL)
    if not m:
        return "no-frontmatter"
    fm_block, body = m.group(1), m.group(2)
    fm = yaml.safe_load(fm_block.strip("-\n")) or {}
    title = str(fm.get("title", path.stem)).replace('"', "'")

    slug = slug_for(path.stem)
    # Default to variant 1 (literal). Reviewer can swap to -2 or -3 later.
    img_path = ILLU / f"{slug}-1.png"
    if not img_path.exists():
        return "no-image"

    md = f"![{title}](../media/illu/{slug}-1.png){{ .illu-thumb }}"
    if "media/illu/" in body:
        # Already injected; refresh in case slug changed
        body_new = re.sub(
            r"^!\[[^\]]*\]\(\.\./media/illu/[^)]+\)\{[^}]*\.illu-thumb[^}]*\}\s*\n+",
            md + "\n\n",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        if body_new == body:
            return "already-present"
        body = body_new
    else:
        # Insert as first body element. Strip a leading blank line.
        body_stripped = body.lstrip("\n")
        body = md + "\n\n" + body_stripped

    path.write_text(fm_block + body, encoding="utf-8")
    return "injected"


def main() -> int:
    posts = sorted(POSTS.glob("*.md"))
    counts: dict[str, int] = {}
    for p in posts:
        r = inject(p)
        counts[r] = counts.get(r, 0) + 1
    print(f"Processed {len(posts)} posts: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

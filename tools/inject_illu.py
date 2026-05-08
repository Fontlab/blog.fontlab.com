#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
# this_file: tools/inject_illu.py
"""Inject illustration thumbnails into every blog post.

Emits one short, decorative line of Markdown immediately after the YAML
frontmatter:

    ![](../media/illu/{slug}-1.png){.illu-thumb}

Empty alt text is intentional: the post's H1 provides the accessible name and
keeping the line under ~80 chars stops Flowmark's semantic reflow from
splitting the attr-list off onto its own line (which would defeat attr_list).
The class default is variant 1 (literal interpretation); a reviewer can swap
to ``-2`` or ``-3`` by hand.

Idempotent: rewrites any previously injected illu line so a slug change or a
Flowmark-broken attr-list both heal on the next run.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "src_docs/md/posts"
ILLU = ROOT / "src_docs/md/media/illu"

# Matches a previous injection — even when Flowmark has split the attr-list
# onto its own line. Captures the whole image-plus-attr block plus trailing
# blank lines so we can replace it cleanly.
_PREV_INJECTION = re.compile(
    r"""
    ^                              # start of a line
    !\[[^\]]*\]                    # ![alt]
    \(\.\./media/illu/[^)]+\)      # (../media/illu/foo.png)
    \s*                            # any whitespace (incl. a Flowmark linebreak)
    \{[^}]*\.illu-thumb[^}]*\}     # { … .illu-thumb … }  attr-list
    \s*\n+                         # trailing newlines
    """,
    re.VERBOSE | re.MULTILINE,
)


def slug_for(stem: str) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)


def inject(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, flags=re.DOTALL)
    if not m:
        return "no-frontmatter"
    fm_block, body = m.group(1), m.group(2)

    slug = slug_for(path.stem)
    img_rel = f"../media/illu/{slug}-1.png"
    if not (ILLU / f"{slug}-1.png").exists():
        return "no-image"

    md_line = f"![]({img_rel}){{.illu-thumb}}"
    block = md_line + "\n\n"

    if _PREV_INJECTION.search(body):
        new_body, n = _PREV_INJECTION.subn(block, body, count=1)
        if n == 0 or new_body == body:
            return "already-present"
        body = new_body
        verdict = "refreshed"
    else:
        body = block + body.lstrip("\n")
        verdict = "injected"

    path.write_text(fm_block + body, encoding="utf-8")
    return verdict


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

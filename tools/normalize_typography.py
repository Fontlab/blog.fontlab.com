#!/usr/bin/env python3
# this_file: tools/normalize_typography.py
"""
Typography normalizer for blog.fontlab.com markdown posts.

Rules applied to PROSE only (skips fenced code blocks, inline code,
YAML front-matter, URLs, HTML tags, and attr_list {…} blocks):
  1. Apostrophes: ASCII ' between letters → U+2019; leading '90s → '90s
  2. Double quotes: ASCII "…" pairs → U+201C … U+201D
  3. Em-dashes: word—word → word — word (space on each side)

Run:
    uv run python tools/normalize_typography.py
"""

import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_PROTECT_RE = re.compile(
    r'(`[^`]*`)'           # inline code
    r'|(https?://\S+)'     # URLs
    r'|(ftp://\S+)'        # FTP URLs
    r'|(\{[^}]*\})'        # attr_list / HTML attr blocks
    r'|(<[^>]+>)'          # HTML tags
)


def _protect(text: str) -> tuple[str, dict]:
    """Replace protected spans with placeholders. Returns (masked, mapping)."""
    mapping: dict[str, str] = {}
    counter = [0]

    def replacer(m: re.Match) -> str:
        key = f'\x00P{counter[0]}\x00'
        mapping[key] = m.group(0)
        counter[0] += 1
        return key

    masked = _PROTECT_RE.sub(replacer, text)
    return masked, mapping


def _restore(text: str, mapping: dict) -> str:
    for key, val in mapping.items():
        text = text.replace(key, val)
    return text


# ---------------------------------------------------------------------------
# Transform functions (operate on already-masked prose)
# ---------------------------------------------------------------------------

def _fix_apostrophes(text: str) -> tuple[str, int]:
    count = 0

    # Contraction / possessive: letter'letter  e.g. don't, it's, Adam's
    def apos_between(m: re.Match) -> str:
        nonlocal count
        count += 1
        return m.group(1) + '’' + m.group(2)

    text = re.sub(r'([A-Za-z])\'([A-Za-z])', apos_between, text)

    # Leading apostrophe before digits: '90s, '60s
    def apos_leading(m: re.Match) -> str:
        nonlocal count
        count += 1
        return '’' + m.group(1)

    text = re.sub(r"(?<![A-Za-z])'(\d)", apos_leading, text)

    return text, count


def _fix_double_quotes(text: str) -> tuple[str, int]:
    """Convert ASCII double-quote pairs to curly quotes."""
    count = 0
    result = []
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]
        if ch != '"':
            result.append(ch)
            i += 1
            continue

        # Decide open vs close
        before = text[i - 1] if i > 0 else ' '
        after = text[i + 1] if i + 1 < n else ' '

        # Opening: preceded by whitespace, open bracket, or start of field
        if before in (' ', '\t', '\n', '(', '[', '—', '–', '—', '–') or i == 0:
            result.append('“')
        else:
            result.append('”')

        count += 1
        i += 1

    return ''.join(result), count


def _fix_emdashes(text: str) -> tuple[str, int]:
    """Ensure exactly one space on each side of every em-dash."""
    count = 0

    def spacer(m: re.Match) -> str:
        nonlocal count
        before_sp = m.group(1)
        after_sp = m.group(2)
        if before_sp != ' ' or after_sp != ' ':
            count += 1
        return ' — '

    # Match optional leading space, em-dash, optional trailing space
    text = re.sub(r'( ?)—( ?)', spacer, text)
    # Collapse any accidental double spaces (but not inside code — already protected)
    text = re.sub(r'  +', ' ', text)
    return text, count


# ---------------------------------------------------------------------------
# Line-level processing
# ---------------------------------------------------------------------------

def process_line(line: str) -> tuple[str, int]:
    masked, mapping = _protect(line)

    masked, c1 = _fix_apostrophes(masked)
    masked, c2 = _fix_double_quotes(masked)
    masked, c3 = _fix_emdashes(masked)

    restored = _restore(masked, mapping)
    return restored, c1 + c2 + c3


# ---------------------------------------------------------------------------
# File-level processing
# ---------------------------------------------------------------------------

def process_file(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    result_lines: list[str] = []
    total = 0

    in_frontmatter = False
    frontmatter_closed = False
    in_fence = False

    for idx, line in enumerate(lines):
        stripped = line.rstrip('\r\n')

        # --- YAML front-matter ---
        if idx == 0 and stripped == '---':
            in_frontmatter = True
            result_lines.append(line)
            continue
        if in_frontmatter:
            if stripped in ('---', '...'):
                in_frontmatter = False
                frontmatter_closed = True
            result_lines.append(line)
            continue

        # --- Fenced code blocks ---
        if re.match(r'^(```|~~~)', stripped):
            in_fence = not in_fence
            result_lines.append(line)
            continue
        if in_fence:
            result_lines.append(line)
            continue

        # --- Prose ---
        new_line, changes = process_line(line)
        total += changes
        result_lines.append(new_line)

    if total > 0:
        path.write_text(''.join(result_lines), encoding='utf-8')

    return total


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    posts_dir = Path(__file__).parent.parent / 'src_docs' / 'md' / 'posts'
    if not posts_dir.exists():
        print(f'Posts directory not found: {posts_dir}', file=sys.stderr)
        sys.exit(1)

    md_files = sorted(posts_dir.glob('*.md'))
    print(f'Processing {len(md_files)} files in {posts_dir}\n')

    grand_total = 0
    changed = 0
    for f in md_files:
        n = process_file(f)
        if n:
            print(f'  {f.name}: {n}')
            changed += 1
            grand_total += n

    print(f'\nDone. {changed}/{len(md_files)} files changed, {grand_total} total substitutions.')


if __name__ == '__main__':
    main()

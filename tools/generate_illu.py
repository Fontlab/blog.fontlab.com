#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.12"
# dependencies = ["tenacity", "pyyaml", "loguru"]
# ///
# this_file: tools/generate_illu.py
"""Generate consistent pencil-sketch thumbnails for every blog post.

Walks src_docs/md/posts/*.md, extracts a visual prompt from the YAML frontmatter
title plus the first line of body text, and calls imgquotio.py per post to
produce src_docs/md/media/illu/{slug}.png. Async with bounded concurrency,
retries on failure, skips existing outputs.
"""

from __future__ import annotations

import asyncio
import re
import sys
from pathlib import Path

import yaml
from loguru import logger
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "src_docs/md/posts"
OUT = ROOT / "src_docs/md/media/illu"
OUT.mkdir(parents=True, exist_ok=True)

STYLE = (
    "Modern Bauhaus / Saul Bass editorial illustration. Flat geometric shapes only: "
    "circles, half-circles, arcs, rectangles, triangles, lines, and bold curves "
    "arranged as a small abstract poster. STRICTLY TWO COLORS plus the paper: "
    "charcoal black (#1a1a1a) and a single warm red (#c81a27), composed on a "
    "warm cream paper background (#f5f4f0). Subtle paper grain texture, no "
    "gradients, no shading, no 3D, no perspective, no photography, no people, "
    "no scenes, no objects rendered literally. Always include ONE typographic "
    "element abstracted into the geometric composition: a stem, a counter, a "
    "baseline, a serif fragment, a curve from a glyph, or a single letterform "
    "treated as a shape (NOT as text — never legible words or labels, never a "
    "signature). Strong silhouettes that read at 32 px and at 256 px. Bold, "
    "asymmetric, confident composition with generous negative space. Square "
    "1024x1024. The result must look like a hand-cut paper collage poster from "
    "a 2026 Swiss editorial design studio: timeless, calm, graphic, abstract."
)

CONCURRENCY = 3


def parse_post(path: Path) -> tuple[str, str]:
    """Return (title, first_line_of_body)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, flags=re.DOTALL)
    if not m:
        return path.stem, ""
    fm = yaml.safe_load(m.group(1)) or {}
    title = str(fm.get("title", path.stem))
    body = m.group(2).strip()
    # First non-empty paragraph line
    first = ""
    for line in body.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "!", "[", "<", "```")):
            first = s
            break
    # Trim
    first = re.sub(r"\s+", " ", first)[:240]
    return title, first


def slug_for(path: Path) -> str:
    """Strip leading YYYY-MM-DD- date from filename stem."""
    stem = path.stem
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)


def build_prompt(title: str, first: str) -> str:
    subject = title.strip()
    if first:
        return (
            f"{STYLE} Conceptual vibe to evoke (do NOT depict literally — translate "
            f"into abstract geometric shapes only): {subject}. Mood cue (inspiration "
            f"only, do not render as illustration): {first}"
        )
    return (
        f"{STYLE} Conceptual vibe to evoke (do NOT depict literally — translate "
        f"into abstract geometric shapes only): {subject}."
    )


async def generate_one(
    sem: asyncio.Semaphore, path: Path, idx: int, total: int
) -> bool:
    slug = slug_for(path)
    out = OUT / f"{slug}.png"
    if out.exists() and out.stat().st_size > 5000:
        logger.info(f"[{idx}/{total}] SKIP {slug} (exists)")
        return True
    title, first = parse_post(path)
    prompt = build_prompt(title, first)

    async with sem:
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=2, min=4, max=30),
            retry=retry_if_exception_type(Exception),
            reraise=True,
        ):
            with attempt:
                logger.info(f"[{idx}/{total}] GEN {slug} :: {title[:60]}")
                proc = await asyncio.create_subprocess_exec(
                    "imgquotio.py",
                    prompt,
                    "--model",
                    "gpt",
                    "--output",
                    str(out),
                    "--size",
                    "1024x1024",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                stdout, stderr = await proc.communicate()
                if proc.returncode != 0 or not out.exists() or out.stat().st_size < 5000:
                    err = stderr.decode("utf-8", errors="replace")[-400:]
                    raise RuntimeError(f"imgquotio failed for {slug}: {err}")
                logger.success(f"[{idx}/{total}] OK   {slug} ({out.stat().st_size // 1024} KB)")
                return True
    return False


async def main() -> int:
    posts = sorted(POSTS.glob("*.md"))
    if not posts:
        logger.error(f"No posts found in {POSTS}")
        return 1
    sem = asyncio.Semaphore(CONCURRENCY)
    total = len(posts)
    tasks = [
        asyncio.create_task(generate_one(sem, p, i + 1, total))
        for i, p in enumerate(posts)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    ok = sum(1 for r in results if r is True)
    fail = total - ok
    logger.info(f"Done: {ok}/{total} ok, {fail} failed")
    return 0 if fail == 0 else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

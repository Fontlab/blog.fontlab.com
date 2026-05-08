#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "fire>=0.6",
#   "httpx>=0.27",
#   "loguru",
#   "numpy",
#   "openai>=1.50",
#   "pillow",
#   "python-slugify>=8",
#   "rich>=13",
#   "tenacity",
#   "webcolors",
# ]
# ///
# this_file: tools/style_explore.py

"""Generate the same two reference posts in 20 different illustration styles.

Output: src_docs/md/media/illu_explore/{NN}-{style}-{a|b}.png
  - 'a' = post about Halftone (visual / historical / technical)
  - 'b' = post about the Briem method (abstract / conceptual / pedagogical)

Each result is post-processed via :mod:`imgopti` so the styles can be compared
side-by-side at the same compact black-on-transparent format the production run
uses.
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import fire
from loguru import logger
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from imgopti import optimize_inplace  # noqa: E402
from imgquotio import generate as imgquotio_generate  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src_docs/md/media/illu_explore"
OUT.mkdir(parents=True, exist_ok=True)

DEFAULT_CONCURRENCY = 3

POSTS = {
    "a": {
        "title": "Halftone — from Fox Talbot to shantytown",
        "vibe": (
            "the history of the halftone screen — turning continuous tone into "
            "a regular grid of dots so an image can survive the printing press; "
            "Victorian science meets cheap newspaper reproduction"
        ),
    },
    "b": {
        "title": "The Briem method and the geometry of nothing",
        "vibe": (
            "Gunnlaugur Briem's pedagogy of teaching letterforms by negative "
            "space — the white inside a letter matters more than the black; "
            "a quiet, almost zen approach to drawing type"
        ),
    },
}

STYLES: list[tuple[str, str]] = [
    (
        "01-riso-poster",
        "Two-color risograph print on warm off-white cardstock. Heavy grain, "
        "slightly off-register, fluorescent pink + warm black, hand-cut shapes, "
        "imperfect ink coverage. Single bold abstract motif. No text. Square.",
    ),
    (
        "02-sumi-wash",
        "Loose Japanese sumi ink wash on raw cream rice paper. ONE confident "
        "brush gesture in warm black ink, wet edges, slight bleed. Vast empty "
        "space. Meditative, calm, single mark. No text, no signature. Square.",
    ),
    (
        "03-soft-clay-3d",
        "Premium soft 3D matte clay render, dusty pastel palette (cream, sand, "
        "dusty rose, terracotta). One sculptural abstract form, large, soft "
        "ambient shadow. Linear/Vercel/Rauno aesthetic. No text, no logos. "
        "Square framing.",
    ),
    (
        "04-gradient-blob",
        "A single huge soft blurred gradient blob on cream paper. Muted earthy "
        "palette: sand, clay, sage, dusty rose. No outlines, no shapes besides "
        "the blob. Pure mood. Slight noise grain. No text. Square.",
    ),
    (
        "05-engraving-line",
        "Banknote / steel-engraving illustration. Fine parallel line hatching, "
        "warm sepia ink on cream paper, dense intricate cross-hatching to build "
        "tone. Vintage scientific etching feel. ONE central abstract motif. "
        "No text, no banknote frame. Square.",
    ),
    (
        "06-mid-century-line",
        "Saul Steinberg / Paul Rand single-weight pen-line illustration on "
        "cream paper. ONE continuous black line drawing forming a loose abstract "
        "shape, witty, economical, charming. No fill. No text. Square.",
    ),
    (
        "07-cyanotype",
        "Cyanotype photogram on cotton paper. Deep Prussian-blue silhouette of "
        "an abstract organic form against pale blue paper, edges soft from sun "
        "exposure. Botanical / scientific archive aesthetic. No text. Square.",
    ),
    (
        "08-blueprint-drafting",
        "Architectural drafting on pale blueprint paper. Fine white technical "
        "lines, dimension marks, drafted curves and arcs forming an abstract "
        "construction. ZERO text labels. Hand-precise but no actual building. "
        "Square.",
    ),
    (
        "09-watercolor-soft",
        "Loose watercolor wash on cold-press cream paper. Muted earthy palette "
        "(ochre, terracotta, slate, sage). Single abstract shape, soft wet "
        "edges, paper grain showing through. Apartamento magazine vibe. No text. "
        "Square.",
    ),
    (
        "10-isometric-mini",
        "Tiny isometric vector illustration centered on cream background. "
        "Three flat muted colors only. ONE small geometric construct floating "
        "in vast empty space. Crisp edges, no shading. No text. Square.",
    ),
    (
        "11-art-deco-mono",
        "1920s Art Deco geometric ornament. Black ink + a single warm gold "
        "tone on cream paper. Symmetric, fan shapes, stepped triangles, thin "
        "rules. Single elegant motif. No text, no border frame. Square.",
    ),
    (
        "12-collage-cut-paper",
        "Hand-cut paper collage. Torn-edge shapes in muted color (cream, brown "
        "kraft, dusty teal, faded red), drop shadows from the paper layers. "
        "ONE clear central composition, calm, tactile, gallery-quality. No text. "
        "Square.",
    ),
    (
        "13-charcoal-gestural",
        "Loose gestural charcoal drawing on toned tan paper, broad smudged "
        "marks, white chalk highlights, lots of negative space. ONE abstract "
        "form with energy. No text. Square.",
    ),
    (
        "14-vector-flat-2026",
        "Modern 2026 editorial flat vector illustration. Limited muted palette "
        "(four colors: cream, charcoal, dusty rose, soft teal). Geometric "
        "abstract composition with subtle texture overlay for depth. Wired/MIT "
        "Tech Review feel. No text. Square.",
    ),
    (
        "15-silkscreen-warhol",
        "Warhol-era silkscreen aesthetic. Bold flat color blocks (one cream, "
        "one warm red, one black) slightly misregistered. Halftone dot fill in "
        "one block. ONE large abstract shape filling the frame. No text. Square.",
    ),
    (
        "16-newsprint-halftone",
        "1960s newsprint halftone illustration. Black ink dots only on cream "
        "newsprint paper. Pure dot pattern density builds an abstract form. "
        "No outlines. Slight registration noise. No text. Square.",
    ),
    (
        "17-medieval-woodcut",
        "Medieval European woodcut. Bold black ink on cream paper, thick "
        "hand-carved lines, parallel hatching, no perspective. ONE abstract "
        "emblem-like motif centered. No text, no scroll, no border. Square.",
    ),
    (
        "18-botanical-plate",
        "Vintage scientific botanical / specimen plate. Faded muted color "
        "wash + fine ink lines on aged cream paper. ONE abstract specimen-like "
        "form floating, with subtle archival number ghosted out. No legible "
        "text. Square.",
    ),
    (
        "19-photoreal-still-life",
        "Photographic still life. Single object made of folded cream paper / "
        "soft clay, lit by soft north window light, on a textured concrete "
        "surface. Editorial magazine photography. Muted, contemplative. No "
        "text in frame. Square.",
    ),
    (
        "20-glitch-soft",
        "Soft glitch aesthetic on cream background. Faint chromatic-aberration "
        "split between dusty cyan and dusty magenta, scanline noise, ONE "
        "abstract shape softly fractured. Calm, not aggressive. No text. Square.",
    ),
]
assert len(STYLES) == 20


def build_prompt(style_prompt: str, post: dict) -> str:
    return (
        f"{style_prompt} "
        f"The illustration should evoke (do NOT depict literally — abstract "
        f"interpretation only): {post['vibe']}. Reference title (do not include "
        f"in image): \"{post['title']}\"."
    )


async def gen_one(
    sem: asyncio.Semaphore,
    style_slug: str,
    style_prompt: str,
    post_key: str,
    post: dict,
    idx: int,
    total: int,
    *,
    color: str,
    quantize: bool,
) -> bool:
    out = OUT / f"{style_slug}-{post_key}.png"
    if out.exists() and out.stat().st_size > 4000:
        logger.info(f"[{idx}/{total}] SKIP {out.name}")
        return True
    prompt = build_prompt(style_prompt, post)

    async with sem:
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=2, min=4, max=30),
            retry=retry_if_exception_type(Exception),
            reraise=True,
        ):
            with attempt:
                logger.info(f"[{idx}/{total}] GEN  {out.name}")
                paths = await asyncio.to_thread(
                    imgquotio_generate,
                    prompt,
                    output=str(out),
                    model="gpt",
                    size="1024x1024",
                )
                if not paths or not paths[0].exists() or paths[0].stat().st_size < 4000:
                    raise RuntimeError(f"imgquotio produced no usable file for {out.name}")
                await asyncio.to_thread(
                    optimize_inplace, paths[0], color=color, quantize=quantize
                )
                size_kb = paths[0].stat().st_size // 1024
                logger.success(f"[{idx}/{total}] OK   {out.name} ({size_kb} KB)")
                return True
    return False


async def _run(*, color: str, quantize: bool, concurrency: int) -> int:
    sem = asyncio.Semaphore(concurrency)
    jobs = [
        (slug, sp, pk, p)
        for slug, sp in STYLES
        for pk, p in POSTS.items()
    ]
    total = len(jobs)
    tasks = [
        asyncio.create_task(
            gen_one(sem, slug, sp, pk, p, i + 1, total, color=color, quantize=quantize)
        )
        for i, (slug, sp, pk, p) in enumerate(jobs)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    ok = sum(1 for r in results if r is True)
    logger.info(f"Done: {ok}/{total} ok")
    return 0 if ok == total else 2


def cli(
    color: str = "black",
    quantize: bool = True,
    concurrency: int = DEFAULT_CONCURRENCY,
) -> None:
    """Generate all 40 style-explore images.

    Args:
        color: Ink color for the post-processed PNG.
        quantize: Run pngquant after PIL save.
        concurrency: Number of concurrent generations.
    """
    sys.exit(asyncio.run(_run(color=color, quantize=quantize, concurrency=concurrency)))


if __name__ == "__main__":
    fire.Fire(cli)

# this_file: mkdocs/hooks/glightbox_small_images.py
"""Exclude small images from the lightbox, one image at a time.

`mkdocs-glightbox` wraps every `<img>` in the page content with a lightbox
anchor. Zooming an icon, an avatar or a 300px screenshot crop is pointless —
the lightbox shows the same pixels at the same size, only on a dim overlay.

This hook runs *before* the plugin (higher event priority) and stamps the
plugin's own opt-out class, `off-glb`, onto any image whose intrinsic size is
below `SMALL_MAX_PX` on both axes. The decision is per image and based on the
real file on disk, so no Markdown has to be touched.

Images we cannot measure (remote URLs, data URIs, SVG, missing files) are left
alone and stay zoomable. To exclude one by hand, add the class in Markdown:

    ![alt](../media/thing.png){ .off-glb }
"""

from __future__ import annotations

import posixpath
import re
from pathlib import Path

from mkdocs.plugins import event_priority
from PIL import Image

# An image smaller than this on both axes gains nothing from a lightbox.
SMALL_MAX_PX = 480

IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
SRC_RE = re.compile(r"""\bsrc\s*=\s*("([^"]*)"|'([^']*)')""", re.IGNORECASE)
CLASS_RE = re.compile(r"""\bclass\s*=\s*("([^"]*)"|'([^']*)')""", re.IGNORECASE)

# path -> is-small, so each file is opened once per build
_size_cache: dict[Path, bool] = {}


def _attr(match: re.Match[str] | None) -> str | None:
    if match is None:
        return None
    return match.group(2) if match.group(2) is not None else match.group(3)


def _resolve(src: str, docs_dir: Path, page_dir: str) -> Path | None:
    """Map an `<img src>` back to the source file under `docs_dir`.

    By this event the Markdown relative-path extension has already rewritten
    `src` against the page's *output* location, so we resolve it the same way
    and then read the matching file from `docs_dir` (media is copied verbatim).
    """
    if not src or "://" in src or src.startswith(("data:", "//", "#")):
        return None
    src = src.split("#", 1)[0].split("?", 1)[0]
    if not src:
        return None
    if src.startswith("/"):
        rel = src.lstrip("/")
    else:
        rel = posixpath.normpath(posixpath.join(page_dir, src))
    if rel.startswith(".."):
        return None
    return docs_dir / rel


def _is_small(path: Path) -> bool:
    cached = _size_cache.get(path)
    if cached is not None:
        return cached
    try:
        with Image.open(path) as img:
            width, height = img.size
        small = max(width, height) < SMALL_MAX_PX
    except Exception:
        small = False
    _size_cache[path] = small
    return small


def _add_off_glb(tag: str) -> str:
    class_match = CLASS_RE.search(tag)
    if class_match is None:
        # Keep a self-closing slash after the new attribute, not before it.
        head = tag[:-1].rstrip().rstrip("/").rstrip()
        tail = " />" if tag[:-1].rstrip().endswith("/") else ">"
        return head + ' class="off-glb"' + tail
    classes = (_attr(class_match) or "").split()
    if "off-glb" in classes:
        return tag
    classes.append("off-glb")
    return tag[: class_match.start()] + f'class="{" ".join(classes)}"' + tag[class_match.end() :]


# Runs before mkdocs-glightbox (priority 0), so the plugin sees `off-glb`.
@event_priority(50)
def on_page_content(html: str, page, config, **kwargs) -> str:
    if "<img" not in html:
        return html
    docs_dir = Path(config["docs_dir"])
    page_dir = posixpath.dirname(page.file.dest_uri)

    def replace(match: re.Match[str]) -> str:
        tag = match.group(0)
        src = _attr(SRC_RE.search(tag))
        if src is None:
            return tag
        path = _resolve(src, docs_dir, page_dir)
        if path is None or not _is_small(path):
            return tag
        return _add_off_glb(tag)

    return IMG_RE.sub(replace, html)

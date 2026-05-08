#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.12"
# dependencies = ["fire>=0.6", "numpy", "pillow", "webcolors", "loguru"]
# ///
# this_file: tools/imgopti.py

"""Convert raster art to a compact black-on-transparent (or recolored) PNG.

Steps for each input:
  1. Read.
  2. Convert to grayscale.
  3. Auto-contrast and threshold (white-point / black-point) so the line work
     becomes near-black and the paper becomes near-white.
  4. Build an RGBA image whose RGB channels are filled with a fixed ink color
     (default ``black``) and whose alpha is derived from the (inverted) mask —
     dark source pixels → opaque ink; light pixels → transparent.
  5. Save as PNG.
  6. If ``pngquant`` is on PATH, run it in place to shrink the file.

Importable API:
    from imgopti import optimize, optimize_inplace
    optimize("input.png", "output.png", color="black", quantize=True)

CLI:
    imgopti.py input.png --output out.png --color "#c81a27" --no-quantize
    imgopti.py raw.png  # rewrites raw.png in place
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from typing import Union

import fire
import numpy as np
import webcolors
from loguru import logger
from PIL import Image, ImageOps

ColorSpec = Union[str, tuple[int, int, int]]


def parse_color(color_spec: ColorSpec) -> tuple[int, int, int]:
    """Parse a color spec (hex string, CSS name, or RGB tuple) into RGB."""
    match color_spec:
        case (r, g, b) if all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)):
            return (r, g, b)
        case str() as s:
            s = s.strip().lower()
            if s.startswith("#"):
                s = s[1:]
            if re.fullmatch(r"[0-9a-f]{6}", s):
                return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))
            try:
                return tuple(webcolors.name_to_rgb(s))  # type: ignore[return-value]
            except ValueError as exc:
                msg = f"Invalid color specification: {color_spec!r}"
                raise ValueError(msg) from exc
        case _:
            msg = f"Color must be a string or an RGB tuple, got: {color_spec!r}"
            raise ValueError(msg)


def _norm_threshold(value: float, *, is_white: bool) -> float:
    """Accept 0–1 fractions or 1–100 percentages."""
    if value > 1:
        value = (1 - value / 100) if is_white else (value / 100)
    return value


def normalize_grayscale(
    img: Image.Image, white_point: float = 0.9, black_point: float = 0.1
) -> Image.Image:
    """Auto-contrast then threshold a grayscale image."""
    wp = _norm_threshold(white_point, is_white=True)
    bp = _norm_threshold(black_point, is_white=False)
    if not (0 <= bp < wp <= 1):
        msg = f"Invalid thresholds: black_point={bp}, white_point={wp}"
        raise ValueError(msg)

    img = ImageOps.autocontrast(img)
    data = np.array(img, dtype=np.float32) / 255.0
    out = np.empty_like(data, dtype=np.uint8)

    white_mask = data >= wp
    black_mask = data <= bp
    mid_mask = ~(white_mask | black_mask)

    out[white_mask] = 255
    out[black_mask] = 0
    if np.any(mid_mask):
        scaled = ((data[mid_mask] - bp) / (wp - bp) * 255).clip(0, 255)
        out[mid_mask] = scaled.astype(np.uint8)
    return Image.fromarray(out)


def _flatten_to_white(img: Image.Image) -> Image.Image:
    """Composite an image onto a solid white background.

    Without this, an already-transparent RGBA input would map ``convert("L")``
    on its zero RGB channels to pure black for the transparent regions, and
    every pixel would land below the dark threshold — producing a fully-black
    output. Flattening preserves the original luminance contract: dark pixels
    are ink, light pixels are paper.
    """
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        return bg
    if img.mode == "LA":
        return _flatten_to_white(img.convert("RGBA"))
    if img.mode == "P":
        return _flatten_to_white(img.convert("RGBA"))
    if img.mode != "RGB":
        return img.convert("RGB")
    return img


def make_inked_alpha(
    src: Image.Image,
    *,
    color: ColorSpec = "black",
    white_point: float = 0.9,
    black_point: float = 0.1,
    negative: bool = False,
) -> Image.Image:
    """Return RGBA: RGB filled with ``color``, alpha from inverted mask."""
    flat = _flatten_to_white(src)
    gray = flat.convert("L")
    norm = normalize_grayscale(gray, white_point, black_point)
    rgb = parse_color(color)
    base = Image.new("RGBA", norm.size, rgb)
    alpha = norm if negative else ImageOps.invert(norm)
    base.putalpha(alpha)
    return base


def _pngquant_inplace(path: Path, quality: str = "65-90") -> bool:
    """Shrink a PNG with pngquant if it is on PATH. Returns True if shrunk."""
    binary = shutil.which("pngquant")
    if not binary:
        return False
    try:
        proc = subprocess.run(
            [
                binary,
                f"--quality={quality}",
                "--skip-if-larger",
                "--strip",
                "--force",
                "--output",
                str(path),
                "--",
                str(path),
            ],
            check=False,
            capture_output=True,
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        logger.warning(f"pngquant timed out for {path}")
        return False
    # pngquant returns 0 on success, 98 if --skip-if-larger refused, others = error
    return proc.returncode == 0


def optimize(
    input_path: str | Path,
    output_path: str | Path | None = None,
    *,
    color: ColorSpec = "black",
    white_point: float = 0.9,
    black_point: float = 0.1,
    negative: bool = False,
    quantize: bool = True,
    quality: str = "65-90",
) -> Path:
    """Read raster art at ``input_path``, write inked-alpha PNG, return Path.

    If ``output_path`` is None, ``input_path`` is rewritten in place.
    """
    src = Path(input_path)
    dst = Path(output_path) if output_path is not None else src
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as img:
        if img.mode == "P" and "transparency" in img.info:
            img = img.convert("RGBA")
        result = make_inked_alpha(
            img,
            color=color,
            white_point=white_point,
            black_point=black_point,
            negative=negative,
        )
    result.save(dst, "PNG", optimize=True)
    if quantize:
        _pngquant_inplace(dst, quality=quality)
    return dst


def optimize_inplace(path: str | Path, **kwargs) -> Path:
    """Convenience: optimize ``path`` overwriting itself."""
    return optimize(path, None, **kwargs)


def cli(
    input_path: str,
    output_path: str | None = None,
    color: str = "black",
    white_point: float = 0.9,
    black_point: float = 0.1,
    negative: bool = False,
    quantize: bool = True,
    quality: str = "65-90",
) -> None:
    """Optimise a single image. ``output_path`` defaults to overwriting input."""
    out = optimize(
        input_path,
        output_path,
        color=color,
        white_point=white_point,
        black_point=black_point,
        negative=negative,
        quantize=quantize,
        quality=quality,
    )
    print(out)


if __name__ == "__main__":
    fire.Fire(cli)

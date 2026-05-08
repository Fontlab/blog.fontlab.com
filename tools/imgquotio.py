#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["fire>=0.6", "openai>=1.50", "python-slugify>=8", "rich>=13", "httpx>=0.27"]
# ///
# this_file: tools/imgquotio.py

"""Generate or edit images via a local OpenAI-compatible CLIPROXY.

Two entry points:
  - generate(prompt, output=..., ...) -> list[Path]   importable Python API
  - cli(prompt, output=..., ...)                      Fire-wrapped CLI
"""

from __future__ import annotations

import base64
import contextlib
import os
import sys
import traceback
from pathlib import Path

import fire
import httpx
import openai
from rich.console import Console
from slugify import slugify

console = Console()

_MODEL_ALIASES = {
    "gpt": "gpt-image-2",
    "nano": "gemini-3.1-flash-image",
}


def _resolve_model(model: str) -> str:
    return _MODEL_ALIASES.get(model, model)


def _pick_extension(data: bytes, output_format: str | None) -> str:
    if output_format:
        return f".{output_format.lstrip('.')}"
    if data[:4] == b"\x89PNG":
        return ".png"
    if data[:3] == b"\xff\xd8\xff":
        return ".jpeg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    return ".png"


def _default_output_name(prompt: str) -> str:
    slug = slugify(prompt, max_length=60, word_boundary=True, save_order=True)
    segments = slug.split("-")[:6]
    return "-".join(segments)


def _write_image(
    img,
    output: str | None,
    index: int,
    n: int,
    prompt: str,
    output_format: str | None,
) -> Path:
    if img.b64_json:
        data = base64.b64decode(img.b64_json)
    elif img.url:
        data = httpx.get(img.url, timeout=60).content
    else:
        raise ValueError("Image response has neither b64_json nor url")

    ext = _pick_extension(data, output_format)

    if output is not None:
        out_path = Path(output)
        if n > 1:
            out_path = out_path.with_stem(f"{out_path.stem}-{index}")
    else:
        base = _default_output_name(prompt)
        name = f"{base}-{index}{ext}" if n > 1 else f"{base}{ext}"
        out_path = Path.cwd() / name

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    return out_path


def _client() -> openai.OpenAI:
    endpoint = os.environ.get("CLIPROXY_API_ENDPOINT", "http://0.0.0.0:18317/v1")
    api_key = os.environ.get(
        "CLIPROXY_API_KEY", "quotio-local-1BD64D2D-C5BF-4496-9A71-9D61DC823DC2"
    )
    return openai.OpenAI(base_url=endpoint, api_key=api_key, timeout=120.0)


def generate(
    prompt: str,
    *,
    input: str | list | None = None,
    mask: str | None = None,
    output: str | None = None,
    model: str = "gpt",
    n: int = 1,
    size: str | None = None,
    quality: str | None = None,
    response_format: str | None = None,
    output_format: str | None = None,
    output_compression: int | None = None,
    background: str | None = None,
    moderation: str | None = None,
    style: str | None = None,
    user: str | None = None,
    verbose: bool = False,
) -> list[Path]:
    """Generate or edit images. Returns the list of saved file paths.

    Raises ``openai.OpenAIError`` subclasses on API failure.
    """
    client = _client()
    resolved_model = _resolve_model(model)

    kwargs: dict = {}
    for k, v in [
        ("n", n),
        ("size", size),
        ("quality", quality),
        ("response_format", response_format),
        ("output_format", output_format),
        ("output_compression", output_compression),
        ("background", background),
        ("moderation", moderation),
        ("style", style),
        ("user", user),
    ]:
        if v is not None:
            kwargs[k] = v

    if verbose:
        console.print(f"[dim]Endpoint:[/dim] {client.base_url}")
        console.print(f"[dim]Model:[/dim] {resolved_model}")
        console.print(f"[dim]Kwargs:[/dim] {kwargs}")

    if input is None:
        response = client.images.generate(model=resolved_model, prompt=prompt, **kwargs)
    else:
        paths = [input] if isinstance(input, str) else list(input)
        with contextlib.ExitStack() as stack:
            handles = [stack.enter_context(open(p, "rb")) for p in paths]
            img_arg = handles[0] if len(handles) == 1 else handles
            edit_kwargs = {**kwargs}
            if mask is not None:
                edit_kwargs["mask"] = stack.enter_context(open(mask, "rb"))
            response = client.images.edit(
                model=resolved_model, image=img_arg, prompt=prompt, **edit_kwargs
            )

    return [
        _write_image(img, output, i, n, prompt, output_format)
        for i, img in enumerate(response.data, start=1)
    ]


def cli(
    prompt: str,
    input: str | list | None = None,
    mask: str | None = None,
    output: str | None = None,
    model: str = "gpt",
    n: int = 1,
    size: str | None = None,
    quality: str | None = None,
    response_format: str | None = None,
    output_format: str | None = None,
    output_compression: int | None = None,
    background: str | None = None,
    moderation: str | None = None,
    style: str | None = None,
    user: str | None = None,
    verbose: bool = False,
) -> None:
    """CLI wrapper around :func:`generate` with friendly error handling."""
    try:
        with console.status(
            f"[cyan]Calling {_resolve_model(model)}…[/cyan]", spinner="dots"
        ):
            paths = generate(
                prompt,
                input=input,
                mask=mask,
                output=output,
                model=model,
                n=n,
                size=size,
                quality=quality,
                response_format=response_format,
                output_format=output_format,
                output_compression=output_compression,
                background=background,
                moderation=moderation,
                style=style,
                user=user,
                verbose=verbose,
            )
    except openai.AuthenticationError as exc:
        console.print(f"[bold red]Authentication error:[/bold red] {exc.message}")
        if verbose:
            traceback.print_exc()
        sys.exit(1)
    except openai.APIConnectionError as exc:
        console.print(f"[bold red]Connection error:[/bold red] {exc}")
        if verbose:
            traceback.print_exc()
        sys.exit(1)
    except openai.APIStatusError as exc:
        console.print(
            f"[bold red]API error {exc.status_code}:[/bold red] {exc.message}"
        )
        if verbose:
            traceback.print_exc()
        sys.exit(1)

    for p in paths:
        console.print(f"[green]Saved:[/green] {p}")


if __name__ == "__main__":
    fire.Fire(cli)

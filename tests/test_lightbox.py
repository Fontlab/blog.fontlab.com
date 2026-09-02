# this_file: tests/test_lightbox.py
"""Lightbox wiring: mkdocs-glightbox plus the small-image exclusion hook.

The hook lives outside the importable package (MkDocs loads it by path), so it
is imported here from `mkdocs/hooks/`.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MKDOCS_YML = ROOT / "mkdocs" / "mkdocs.yml"
HOOK_PATH = ROOT / "mkdocs" / "hooks" / "glightbox_small_images.py"


def _load_hook():
    spec = importlib.util.spec_from_file_location("glightbox_small_images", HOOK_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_config() -> dict:
    class _Loader(yaml.SafeLoader):
        pass

    # mkdocs.yml carries `!!python/name:` tags for the emoji extension.
    _Loader.add_multi_constructor("tag:yaml.org,2002:python/name:", lambda *_: None)
    return yaml.load(MKDOCS_YML.read_text(encoding="utf-8"), Loader=_Loader)


def _plugin_config(name: str):
    for entry in _load_config()["plugins"]:
        if isinstance(entry, str) and entry == name:
            return {}
        if isinstance(entry, dict) and name in entry:
            return entry[name] or {}
    raise AssertionError(f"plugin {name!r} not configured in mkdocs.yml")


def test_glightbox_plugin_is_enabled():
    assert _plugin_config("glightbox") is not None


def test_illu_thumbs_are_skipped():
    # Index thumbnails are click-targets for the post link (js/illu-link.js);
    # a lightbox anchor would hijack that click.
    assert "illu-thumb" in _plugin_config("glightbox")["skip_classes"]


def test_hook_is_registered():
    assert "hooks/glightbox_small_images.py" in _load_config()["hooks"]


def test_small_images_get_the_plugin_opt_out_class(tmp_path):
    hook = _load_hook()
    assert hook._add_off_glb('<img src="a.png">') == '<img src="a.png" class="off-glb">'
    assert (
        hook._add_off_glb('<img class="illu-photo" src="a.png">')
        == '<img class="illu-photo off-glb" src="a.png">'
    )
    # Raw HTML in the corpus writes self-closing tags; the slash stays last.
    assert (
        hook._add_off_glb('<img src="a.png" decoding="async" />')
        == '<img src="a.png" decoding="async" class="off-glb" />'
    )
    # Idempotent — a hand-tagged image is left alone.
    tagged = '<img class="off-glb" src="a.png">'
    assert hook._add_off_glb(tagged) == tagged


def test_size_threshold(tmp_path):
    from PIL import Image

    hook = _load_hook()
    small = tmp_path / "small.png"
    big = tmp_path / "big.png"
    Image.new("RGB", (hook.SMALL_MAX_PX - 1, 64)).save(small)
    Image.new("RGB", (hook.SMALL_MAX_PX, 64)).save(big)
    assert hook._is_small(small)
    assert not hook._is_small(big)
    # Unreadable files stay zoomable rather than silently dropping out.
    missing = tmp_path / "nope.png"
    assert not hook._is_small(missing)


def test_src_resolution():
    hook = _load_hook()
    docs = Path("/docs")
    page_dir = "2026/03/26/five-centuries-of-line"
    assert hook._resolve("../../../../media/x.png", docs, page_dir) == docs / "media/x.png"
    assert hook._resolve("/media/x.png", docs, page_dir) == docs / "media/x.png"
    assert hook._resolve("https://example.com/x.png", docs, page_dir) is None
    assert hook._resolve("data:image/png;base64,AAAA", docs, page_dir) is None


def test_real_small_media_is_below_threshold():
    hook = _load_hook()
    icon = ROOT / "src_docs" / "md" / "media" / "fontlab-8-app-icon.png"
    if icon.exists():
        assert hook._is_small(icon)

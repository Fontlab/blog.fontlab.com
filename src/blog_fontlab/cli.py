# this_file: src/blog_fontlab/cli.py
"""Build orchestrator for the FontLab Blog site.

Single entry point. Run it via the shell wrapper:

    ./build.sh build

or via uv directly:

    uv run blog-fontlab build

See ``./build.sh --help`` for subcommands.
"""

from __future__ import annotations

import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import fire
from loguru import logger


class BuildError(RuntimeError):
    """Raised when the build pipeline cannot proceed."""


HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>]*>", re.DOTALL)
FL_HELP_CTA_RE = re.compile(
    r"(?P<link>\[[^\]\n]+\]\([^)]+\))\{\s*\.fl-help-cta\s*\}",
    re.DOTALL,
)


def _configure_logging(verbose: bool) -> None:
    """Configure loguru sink."""
    import os

    level = "DEBUG" if verbose else os.environ.get("BLOG_LOG_LEVEL", "INFO").upper()
    logger.remove()
    logger.add(sys.stderr, level=level, format="<level>{level: <8}</level> | {message}")


def _find_repo_root() -> Path:
    """Walk up from cwd until we find a dir with both pyproject.toml and build.sh."""
    cur = Path.cwd().resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "pyproject.toml").is_file() and (candidate / "build.sh").is_file():
            return candidate
    raise BuildError(
        "cannot locate blog-fontlab repo root "
        "(no pyproject.toml + build.sh found walking up from cwd). "
        "Run via ./build.sh or cd to the repo root first."
    )


def _clean_docs(docs_dir: Path) -> None:
    """Remove everything in ``docs_dir`` except ``CNAME``. Recreate if missing."""
    if not docs_dir.exists():
        docs_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created {docs_dir}")
        return
    cname_content: str | None = None
    cname_path = docs_dir / "CNAME"
    if cname_path.is_file():
        cname_content = cname_path.read_text(encoding="utf-8")
        logger.debug(f"Preserving CNAME: {cname_content.strip()!r}")
    for child in docs_dir.iterdir():
        if child.name == "CNAME":
            continue
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
        logger.debug(f"Removed {child}")
    if cname_content is not None:
        cname_path.write_text(cname_content, encoding="utf-8")
    logger.info(f"Cleaned {docs_dir} (preserved CNAME)")


def _run_command(cmd: list[str], cwd: Path) -> None:
    """Run a subprocess with consistent logging."""
    logger.info(f"Running: {shlex.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=cwd)


def _restore_html_tag_quotes(markdown: str) -> str:
    """Restore ASCII quotes in raw HTML tags after Flowmark smart quotes."""

    def restore(match: re.Match[str]) -> str:
        return (
            match.group(0).replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        )

    return HTML_TAG_RE.sub(restore, markdown)


def _restore_fl_help_cta_attributes(markdown: str) -> str:
    """Keep CTA attribute lists attached to their Markdown links."""
    return FL_HELP_CTA_RE.sub(r"\g<link>{ .fl-help-cta }", markdown)


def _repair_markdown_after_flowmark(src_docs_dir: Path) -> int:
    """Restore post-Flowmark markdown details in files below ``src_docs_dir``."""
    changed_count = 0
    for markdown_path in sorted(src_docs_dir.rglob("*.md")):
        original = markdown_path.read_text(encoding="utf-8")
        restored = _restore_fl_help_cta_attributes(_restore_html_tag_quotes(original))
        if restored == original:
            continue
        markdown_path.write_text(restored, encoding="utf-8")
        changed_count += 1
    return changed_count


class Build:
    """FontLab Blog build orchestrator."""

    def __init__(self, root: str | None = None) -> None:
        self._root = Path(root).resolve() if root else _find_repo_root()

    @property
    def _docs_dir(self) -> Path:
        return self._root / "docs"

    @property
    def _mkdocs_config(self) -> Path:
        return self._root / "mkdocs" / "mkdocs.yml"

    @property
    def _src_docs_dir(self) -> Path:
        return self._root / "src_docs" / "md"

    def _format_markdown_source(self) -> None:
        """Format source Markdown with Flowmark before rendering the site."""
        src_docs_dir = self._src_docs_dir
        if not src_docs_dir.is_dir():
            raise BuildError(f"source Markdown directory missing: {src_docs_dir}")
        cmd = [
            "flowmark",
            "--inplace",
            "--nobackup",
            "--semantic",
            "--cleanups",
            "--smartquotes",
            "--ellipses",
            "--width",
            "0",  # disable column wrapping; attr_list lines stay intact
            str(src_docs_dir),
        ]
        _run_command(cmd, self._root)
        repaired_count = _repair_markdown_after_flowmark(src_docs_dir)
        if repaired_count:
            logger.info(f"Repaired Flowmark output in {repaired_count} Markdown files")
        logger.info("Formatted source Markdown with Flowmark")

    def clean(self, verbose: bool = False) -> None:
        """Remove everything in docs/ except CNAME."""
        _configure_logging(verbose)
        try:
            _clean_docs(self._docs_dir)
        except BuildError as exc:
            logger.error(str(exc))
            sys.exit(1)

    def format(self, verbose: bool = False) -> None:
        """Format src_docs/md Markdown with Flowmark in place."""
        _configure_logging(verbose)
        try:
            self._format_markdown_source()
        except BuildError as exc:
            logger.error(str(exc))
            sys.exit(1)
        except subprocess.CalledProcessError as exc:
            logger.error(f"Flowmark formatting failed (exit {exc.returncode})")
            sys.exit(1)

    def build(self, verbose: bool = False) -> None:
        """Run the full build pipeline: format → clean → properdocs build."""
        _configure_logging(verbose)
        try:
            self._format_markdown_source()
            _clean_docs(self._docs_dir)
            config = self._mkdocs_config
            if not config.is_file():
                raise BuildError(f"mkdocs config missing: {config}")
            cmd = [
                "properdocs",
                "build",
                "-f",
                str(config),
                "-d",
                str(self._docs_dir),
            ]
            _run_command(cmd, self._root)
            (self._docs_dir / ".nojekyll").touch()
            logger.info("Build complete")
        except BuildError as exc:
            logger.error(str(exc))
            sys.exit(1)
        except subprocess.CalledProcessError as exc:
            logger.error(f"build command failed (exit {exc.returncode})")
            sys.exit(1)

    def serve(self, verbose: bool = False) -> None:
        """Serve the site locally via properdocs serve."""
        _configure_logging(verbose)
        try:
            config = self._mkdocs_config
            if not config.is_file():
                raise BuildError(f"mkdocs config missing: {config}")
            cmd = [
                "properdocs",
                "serve",
                "-f",
                str(config),
            ]
            _run_command(cmd, self._root)
        except BuildError as exc:
            logger.error(str(exc))
            sys.exit(1)
        except subprocess.CalledProcessError as exc:
            logger.error(f"properdocs serve failed (exit {exc.returncode})")
            sys.exit(1)
        except KeyboardInterrupt:
            logger.info("Server stopped")


def main() -> None:
    """Console-script entry point for ``blog-fontlab``."""
    fire.Fire(Build)


if __name__ == "__main__":
    main()

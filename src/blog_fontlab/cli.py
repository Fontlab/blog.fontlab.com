# this_file: src/blog_fontlab/cli.py
"""Build orchestrator for the FontLab Blog site.

Single entry point. Run it via the shell wrapper:

    ./build.sh build

or via uv directly:

    uv run blog-fontlab build

See ``./build.sh --help`` for subcommands.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import fire
from loguru import logger


class BuildError(RuntimeError):
    """Raised when the build pipeline cannot proceed."""


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

    def clean(self, verbose: bool = False) -> None:
        """Remove everything in docs/ except CNAME."""
        _configure_logging(verbose)
        try:
            _clean_docs(self._docs_dir)
        except BuildError as exc:
            logger.error(str(exc))
            sys.exit(1)

    def build(self, verbose: bool = False) -> None:
        """Run the full build pipeline: clean → properdocs build."""
        _configure_logging(verbose)
        try:
            _clean_docs(self._docs_dir)
            config = self._mkdocs_config
            if not config.is_file():
                raise BuildError(f"mkdocs config missing: {config}")
            cmd = [
                "properdocs",
                "build",
                "-f", str(config),
                "-d", str(self._docs_dir),
            ]
            logger.info(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True, cwd=self._root)
            (self._docs_dir / ".nojekyll").touch()
            logger.info("Build complete")
        except BuildError as exc:
            logger.error(str(exc))
            sys.exit(1)
        except subprocess.CalledProcessError as exc:
            logger.error(f"properdocs build failed (exit {exc.returncode})")
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
                "-f", str(config),
            ]
            logger.info(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True, cwd=self._root)
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

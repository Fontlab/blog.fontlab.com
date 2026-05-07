# this_file: src/blog_fontlab/__init__.py
"""blog-fontlab — build orchestrator for blog.fontlab.com."""
from __future__ import annotations

try:
    from .__version__ import __version__
except ImportError:
    __version__ = "0.0.0+unknown"

__all__ = ["__version__"]

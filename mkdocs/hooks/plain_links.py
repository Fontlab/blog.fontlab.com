# this_file: mkdocs/hooks/plain_links.py
"""Mark the blog's CTA links as components for fly-january.

fly-january styles every article link except those carrying data-fly-plain (or a class
starting "md-"). Posts write the CTA as Markdown with `{ .fl-help-cta }`, so the attribute
is added here at build time; css/extra.css styles `.md-typeset .fl-help-cta`.
"""

from __future__ import annotations

import re
from typing import Any

CTA_LINK = re.compile(r'<a\b(?=[^>]*\bclass="[^"]*\bfl-help-cta\b)(?![^>]*\bdata-fly-plain\b)')


def on_page_content(html: str, **_: Any) -> str:
    return CTA_LINK.sub("<a data-fly-plain", html)

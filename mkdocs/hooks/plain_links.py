# this_file: mkdocs/hooks/plain_links.py
"""Mark the blog's CTA links as components for fly-january.

fly-january styles every article link except those carrying data-fly-plain (or a class
starting "md-"). Posts write the CTA as Markdown with `{ .fl-help-cta }`, so the attribute
is added here at build time; css/extra.css styles `.md-typeset .fl-help-cta`.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser
from typing import Any

HTML_SPACE = r"[ \t\n\f\r]"
# HTMLParser recovers missing attribute separators and stray '<' in attribute names.
ATTRIBUTE_VALUE = r"""(?:"[^"]*"|'[^']*'|[^\s"'`=<>]+)"""
ANCHOR = re.compile(
    rf"<a(?:{HTML_SPACE}+[\w:.-]+(?:{HTML_SPACE}*={HTML_SPACE}*{ATTRIBUTE_VALUE})?)*"
    rf"{HTML_SPACE}*/?>",
    re.ASCII | re.IGNORECASE,
)


class _PlainLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.insertions: list[tuple[int, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attributes = dict(attrs)
        if len(attributes) != len(attrs) or "data-fly-plain" in attributes:
            return
        classes = re.split(HTML_SPACE + "+", attributes.get("class") or "")
        if "fl-help-cta" in classes and ANCHOR.fullmatch(self.get_starttag_text()):
            line, column = self.getpos()
            self.insertions.append((line - 1, column + 2))


def on_page_content(html: str, **_: Any) -> str:
    parser = _PlainLinks()
    try:
        parser.feed(html)
        parser.close()
    except (AssertionError, ValueError):
        # Malformed declarations or out-of-range character references can abort parsing.
        return html
    # Work backwards so each position still points just after the original '<a'.
    lines = html.split("\n")
    for row, column in reversed(parser.insertions):
        lines[row] = lines[row][:column] + " data-fly-plain" + lines[row][column:]
    return "\n".join(lines)

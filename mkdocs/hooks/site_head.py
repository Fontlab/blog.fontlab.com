# this_file: mkdocs/hooks/site_head.py
"""Page-wide additions that have no template slot in fly-january or MaterialX.

Adds Google Tag Manager (the head script and the <noscript> iframe after <body>) and the
JSON Feed autodiscovery links, and titles MaterialX's two RSS links for the blog.
A custom main.html would replace fly-january's own, so these go in a
hook. Runs on every page (on_post_page) and on 404.html (on_post_template).
"""

from __future__ import annotations

import re
from typing import Any

GTM_ID = "GTM-5WNRV8Z7"
GTM_HEAD = (
    "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
    "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
    "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src="
    "'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
    f"}})(window,document,'script','dataLayer','{GTM_ID}');</script>"
)
GTM_BODY = (
    f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" '
    'height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
)
JSON_FEEDS = (
    ("feed_json_created.json", "FontLab Blog (JSON Feed, by creation date)"),
    ("feed_json_updated.json", "FontLab Blog (JSON Feed, by update date)"),
)
RSS_TITLES = {
    "created": "FontLab Blog (RSS, by creation date)",
    "updated": "FontLab Blog (RSS, by update date)",
}
# MaterialX emits this attribute order and makes the feed paths relative to each page.
RSS_TITLE = re.compile(
    r'(?<=<link rel="alternate" type="application/rss\+xml" title=")[^"]*'
    r'(?=" href="(?:/|(?:\.\./)*)feed_rss_(created|updated)\.xml")'
)
BODY_OPEN = re.compile(r"<body\b[^>]*>")


def add_site_head(html: str, site_url: str) -> str:
    """Set the RSS titles and insert GTM and JSON Feed links once per page."""
    if GTM_ID in html or "</head>" not in html:
        return html
    feeds = "".join(
        f'<link rel="alternate" type="application/feed+json" title="{title}" '
        f'href="{site_url}{name}">'
        for name, title in JSON_FEEDS
    )
    head, end_head, body = html.partition("</head>")
    head = RSS_TITLE.sub(lambda match: RSS_TITLES[match[1]], head)
    html = f"{head}{GTM_HEAD}{feeds}{end_head}{body}"
    return BODY_OPEN.sub(lambda m: m.group(0) + GTM_BODY, html, count=1)


def on_post_page(output: str, page: Any, config: Any, **_: Any) -> str:
    return add_site_head(output, config["site_url"])


def on_post_template(output_content: str, template_name: str, config: Any, **_: Any) -> str:
    if template_name != "404.html":
        return output_content
    return add_site_head(output_content, config["site_url"])

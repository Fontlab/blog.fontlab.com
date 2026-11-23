# this_file: mkdocs/hooks/site_head.py
"""Page-wide additions that have no template slot in fly-january or MaterialX.

Adds Google Tag Manager (the head script and the <noscript> iframe after <body>) and the
JSON Feed autodiscovery links. MaterialX already emits the two RSS links because the rss
plugin is enabled. A custom main.html would replace fly-january's own, so these go in a
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
BODY_OPEN = re.compile(r"<body\b[^>]*>")


def add_site_head(html: str, site_url: str) -> str:
    """Insert GTM and the JSON Feed links into one rendered page (once)."""
    if GTM_ID in html or "</head>" not in html:
        return html
    feeds = "".join(
        f'<link rel="alternate" type="application/feed+json" title="{title}" '
        f'href="{site_url}{name}">'
        for name, title in JSON_FEEDS
    )
    html = html.replace("</head>", f"{GTM_HEAD}{feeds}</head>", 1)
    return BODY_OPEN.sub(lambda m: m.group(0) + GTM_BODY, html, count=1)


def on_post_page(output: str, page: Any, config: Any, **_: Any) -> str:
    return add_site_head(output, config["site_url"])


def on_post_template(output_content: str, template_name: str, config: Any, **_: Any) -> str:
    if template_name != "404.html":
        return output_content
    return add_site_head(output_content, config["site_url"])

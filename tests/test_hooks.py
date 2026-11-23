# this_file: tests/test_hooks.py
from pathlib import Path
from runpy import run_path

import pytest

HOOKS = Path(__file__).resolve().parents[1] / "mkdocs" / "hooks"
add_site_head = run_path(str(HOOKS / "site_head.py"))["add_site_head"]
on_page_content = run_path(str(HOOKS / "plain_links.py"))["on_page_content"]
SITE_URL = "https://blog.fontlab.com/"


@pytest.mark.parametrize("prefix", ["", "../../../", "/"], ids=["home", "post", "404"])
def test_site_head_preserves_feed_links_and_adds_metadata_once(prefix):
    created = f'<link rel="alternate" type="application/rss+xml" title="RSS feed" href="{prefix}feed_rss_created.xml">'
    updated = f'<link rel="alternate" type="application/rss+xml" title="RSS feed of updated content" href="{prefix}feed_rss_updated.xml">'
    html = f'<head>{created}{updated}</head><body class="blog"><p>Post</p></body>'
    result = add_site_head(html, SITE_URL)
    head, body = result.split("</head>")

    assert head.count('type="application/rss+xml"') == 2
    assert created.replace("RSS feed", "FontLab Blog (RSS, by creation date)") in head
    assert (
        updated.replace("RSS feed of updated content", "FontLab Blog (RSS, by update date)") in head
    )
    for order in ("created", "updated"):
        assert head.count(f'href="{SITE_URL}feed_json_{order}.json"') == 1
    assert head.count("GTM-5WNRV8Z7") == body.count("GTM-5WNRV8Z7") == 1
    assert body.startswith('<body class="blog"><noscript><iframe')
    assert add_site_head(result, SITE_URL) == result


def test_site_head_preserves_html_without_closing_head():
    fragment = "<body><p>A page fragment</p></body>"
    assert add_site_head(fragment, SITE_URL) == fragment


@pytest.mark.parametrize(
    "classes", ["fl-help-cta next", "first\tfl-help-cta\nnext", "first fl-help-cta"]
)
def test_plain_links_marks_only_the_anchor_and_preserves_its_markup(classes):
    html = f"""<p><a
  href="/manual/" title="A > B"
  class='{classes}'>Read more</a></p>"""
    marked = html.replace("<a\n", "<a data-fly-plain\n")
    assert on_page_content(html) == marked
    assert on_page_content(marked) == marked


@pytest.mark.parametrize(
    "html",
    [
        '<a class="fl-help-cta-x">more</a>',
        '<a class="fl-help-cta__x">more</a>',
        '<a class="x-fl-help-cta">more</a>',
        '<a class="fl-help-cta.extra">more</a>',
        '<abbr class="fl-help-cta">CTA</abbr>',
        '<a data-class="fl-help-cta">more</a>',
        """<a title=' class="fl-help-cta"'>more</a>""",
        '<a class="fl-help-cta" data-fly-plain="">more</a>',
        '<!-- <a class="fl-help-cta"> -->',
        '<a class="fl-help-cta" <abbr>',
        '<a class="fl-help-cta"href="target">',
        '<a class="fl-help-cta',
    ],
)
def test_plain_links_leaves_other_markup_intact(html):
    assert on_page_content(html) == html

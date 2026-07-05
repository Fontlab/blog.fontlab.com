# this_file: tests/test_content_state.py
"""Content-state invariants for the published blog corpus.

The `review:` front-matter block is an editorial QA overlay applied during the
2026-05 reconciliation sprint. Not every post carries it: posts written after
the sprint ship with plain front matter and are reviewed later. These tests
therefore split into two tiers:

- invariants that must hold for *every* published post (core front matter), and
- invariants that must hold only for posts that opted into the `review:` overlay
  (valid status vocabulary, and a CTA target that actually appears in the body).

The editorial backlog itself — posts still awaiting a review pass, and posts
whose hero image is still a placeholder — is tracked in TODO.md, and
`test_todo_summary_matches_live_content_state` keeps that summary honest.
"""

from __future__ import annotations

import re
from pathlib import Path

import frontmatter
import yaml

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "src_docs" / "md" / "posts"
TODO_PATH = ROOT / "TODO.md"
DRAFT_POSTS_DIR = ROOT / "issues" / "draft-posts"
AUTHORS_PATH = ROOT / "src_docs" / "md" / "authors.yml"
TOPIC_DIR = ROOT / "src_docs" / "md" / "topic"
TOPIC_INDEX_PATH = TOPIC_DIR / "index.md"

# Known-good values for the editorial `review:` overlay.
KNOWN_IMAGE_STATUS = {"present", "missing", "weak"}
CTA_LINK_RE = re.compile(r"\[[^\]\n]+\]\(([^)]+)\)\{\s*\.fl-help-cta\s*\}")


def _published_posts() -> list[tuple[Path, frontmatter.Post]]:
    return [
        (path, frontmatter.loads(path.read_text(encoding="utf-8")))
        for path in sorted(POSTS_DIR.glob("*.md"))
    ]


def _review(post: frontmatter.Post) -> dict[str, object] | None:
    """Return the post's review overlay, or None if it has not been reviewed yet."""
    review = post.get("review")
    return review if isinstance(review, dict) else None


def _reviewed_posts() -> list[tuple[Path, frontmatter.Post, dict[str, object]]]:
    return [(p, post, r) for p, post in _published_posts() if (r := _review(post)) is not None]


def test_every_post_has_core_frontmatter() -> None:
    """Title, date, and author are mandatory for every published post."""
    failures = [
        f"{path.name}: missing {sorted({'title', 'date', 'authors'} - set(post.keys()))}"
        for path, post in _published_posts()
        if not {"title", "date", "authors"} <= set(post.keys())
    ]
    assert not failures, "\n".join(failures)


def test_reviewed_posts_use_known_image_status() -> None:
    """A review overlay must declare an image_status we recognise."""
    failures = [
        f"{path.name}: image_status={review.get('image_status')!r}"
        for path, _post, review in _reviewed_posts()
        if review.get("image_status") not in KNOWN_IMAGE_STATUS
    ]
    assert not failures, "\n".join(failures)


def test_reviewed_posts_cta_target_appears_in_body() -> None:
    """If a post has been reviewed, its CTA target must be a link in the body.

    This catches the common drift where the CTA link in the body is edited but
    the review annotation still points at the old destination.
    """
    failures: list[str] = []
    for path, post, review in _reviewed_posts():
        target = review.get("cta_target")
        if not isinstance(target, str) or target in {"", "NEEDS-DEEP-LINK"}:
            failures.append(f"{path.name}: invalid cta_target {target!r}")
            continue
        cta_links = CTA_LINK_RE.findall(post.content)
        if target not in cta_links:
            failures.append(
                f"{path.name}: cta_target {target!r} not among body CTA links {cta_links!r}"
            )
    assert not failures, "\n".join(failures)


def test_todo_summary_matches_live_content_state() -> None:
    """TODO.md must report the true live corpus counts, not a stale snapshot."""
    todo = TODO_PATH.read_text(encoding="utf-8")
    posts = _published_posts()
    draft_count = len(list(DRAFT_POSTS_DIR.glob("*.md")))
    reviewed = [(p, post) for p, post in posts if _review(post) is not None]
    unreviewed_count = len(posts) - len(reviewed)
    missing_count = sum(
        1 for _, post in reviewed if (_review(post) or {}).get("image_status") == "missing"
    )

    expected_lines = [
        f"- {len(posts)} published source posts in `src_docs/md/posts/`",
        f"- {draft_count} offline draft/research files in `issues/draft-posts/`",
        f"- {len(reviewed)} posts carry the editorial `review:` overlay",
        f"- {unreviewed_count} posts still awaiting an editorial review pass",
        f"- {missing_count} reviewed posts with `review.image_status: missing`",
    ]

    missing_lines = [line for line in expected_lines if line not in todo]
    assert not missing_lines, "\n".join(missing_lines)


def test_authors_resolve_to_local_profile_pages() -> None:
    data = yaml.safe_load(AUTHORS_PATH.read_text(encoding="utf-8"))
    authors = data.get("authors", {})
    failures: list[str] = []

    for author_id, author in authors.items():
        if author.get("url"):
            failures.append(f"{author_id}: author.url bypasses generated profile page")

        slug = author.get("slug") or author_id
        profile = TOPIC_DIR / f"{slug}.md"
        if not profile.is_file():
            failures.append(f"{author_id}: missing {profile.relative_to(ROOT)}")

    assert not failures, "\n".join(failures)


def test_topic_index_links_all_author_profiles() -> None:
    data = yaml.safe_load(AUTHORS_PATH.read_text(encoding="utf-8"))
    authors = data.get("authors", {})
    topic_index = TOPIC_INDEX_PATH.read_text(encoding="utf-8")
    failures: list[str] = []

    for author_id, author in authors.items():
        slug = author.get("slug") or author_id
        if f"]({slug}.md)" not in topic_index:
            failures.append(f"{author_id}: missing topic index link to {slug}.md")

    assert not failures, "\n".join(failures)

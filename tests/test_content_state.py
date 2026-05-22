# this_file: tests/test_content_state.py
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
AUTHOR_DIR = ROOT / "src_docs" / "md" / "author"


def _published_posts() -> list[tuple[Path, frontmatter.Post]]:
    return [(path, frontmatter.loads(path.read_text(encoding="utf-8"))) for path in sorted(POSTS_DIR.glob("*.md"))]


def _review(post: frontmatter.Post) -> dict[str, object]:
    review = post.get("review")
    assert isinstance(review, dict), "every published post must carry review metadata"
    return review


def test_all_published_posts_have_concrete_cta_targets() -> None:
    failures: list[str] = []
    for path, post in _published_posts():
        review = _review(post)
        target = review.get("cta_target")
        if not isinstance(target, str) or target in {"", "NEEDS-DEEP-LINK"}:
            failures.append(f"{path.name}: invalid cta_target {target!r}")
            continue
        cta_links = re.findall(r"\[[^\]\n]+\]\(([^)]+)\)\{\s*\.fl-help-cta\s*\}", post.content)
        if target not in cta_links:
            failures.append(f"{path.name}: cta_target {target!r} not found in body CTA links {cta_links!r}")

    assert not failures, "\n".join(failures)


def test_no_published_post_has_missing_or_weak_image_status() -> None:
    failures = [
        f"{path.name}: image_status={_review(post).get('image_status')!r}"
        for path, post in _published_posts()
        if _review(post).get("image_status") in {"missing", "weak"}
    ]

    assert not failures, "\n".join(failures)


def test_todo_summary_matches_live_content_state() -> None:
    todo = TODO_PATH.read_text(encoding="utf-8")
    posts = _published_posts()
    draft_count = len(list(DRAFT_POSTS_DIR.glob("*.md")))
    missing_count = sum(1 for _, post in posts if _review(post).get("image_status") == "missing")
    weak_count = sum(1 for _, post in posts if _review(post).get("image_status") == "weak")
    needs_deep_link_count = sum(
        1 for _, post in posts if _review(post).get("cta_target") == "NEEDS-DEEP-LINK"
    )

    expected_lines = [
        f"- {len(posts)} published source posts in `src_docs/md/posts/`",
        f"- {draft_count} offline draft/research files in `issues/draft-posts/`",
        f"- {needs_deep_link_count} live CTA deep-link research items remaining",
        f"- {missing_count} posts with `review.image_status: missing`",
        f"- {weak_count} posts with `review.image_status: weak`",
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
        profile = AUTHOR_DIR / f"{slug}.md"
        if not profile.is_file():
            failures.append(f"{author_id}: missing {profile.relative_to(ROOT)}")

    assert not failures, "\n".join(failures)

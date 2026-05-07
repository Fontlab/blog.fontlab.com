# this_file: tests/test_cli.py
from __future__ import annotations

from pathlib import Path

from blog_fontlab import cli


def test_build_formats_before_cleaning_and_running_properdocs(monkeypatch, tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("", encoding="utf-8")
    (tmp_path / "build.sh").write_text("", encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "mkdocs").mkdir()
    (tmp_path / "mkdocs" / "mkdocs.yml").write_text("site_name: Test\n", encoding="utf-8")
    (tmp_path / "src_docs" / "md").mkdir(parents=True)

    calls: list[tuple[str, object]] = []

    monkeypatch.setattr(cli, "_configure_logging", lambda verbose: calls.append(("log", verbose)))
    monkeypatch.setattr(
        cli.Build,
        "_format_markdown_source",
        lambda self: calls.append(("format", self._src_docs_dir)),
    )
    monkeypatch.setattr(cli, "_clean_docs", lambda path: calls.append(("clean", path)))
    monkeypatch.setattr(cli, "_run_command", lambda cmd, cwd: calls.append(("run", cmd)))

    cli.Build(root=str(tmp_path)).build()

    assert calls == [
        ("log", False),
        ("format", tmp_path / "src_docs" / "md"),
        ("clean", tmp_path / "docs"),
        (
            "run",
            [
                "properdocs",
                "build",
                "-f",
                str(tmp_path / "mkdocs" / "mkdocs.yml"),
                "-d",
                str(tmp_path / "docs"),
            ],
        ),
    ]
    assert (tmp_path / "docs" / ".nojekyll").exists()


def test_restore_html_tag_quotes_leaves_text_smart_quotes_alone() -> None:
    source = "<a class=“fl-help-cta” href=‘/manual/’>“Read more”</a>"

    assert cli._restore_html_tag_quotes(source) == (
        "<a class=\"fl-help-cta\" href='/manual/'>“Read more”</a>"
    )


def test_restore_fl_help_cta_attributes_joins_split_attribute_list() -> None:
    source = (
        "[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta\n}\n"
        "[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/){\n.fl-help-cta }"
    )

    assert cli._restore_fl_help_cta_attributes(source) == "\n".join(
        [
            "[Read more →](https://help.fontlab.com/fontlab/8/manual/){ .fl-help-cta }",
            "[Read more →](https://help.fontlab.com/fontlab/8/tutorials/intro/){ .fl-help-cta }",
        ]
    )

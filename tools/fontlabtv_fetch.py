#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["fire", "requests"]
# ///
# this_file: tools/fontlabtv_fetch.py
"""
Harvest video metadata from the FontLab TV YouTube channel.

Usage:
    uv run tools/fontlabtv_fetch.py --limit 30
    uv run tools/fontlabtv_fetch.py --limit 30 --out-dir .omc/notes/fontlabtv
    uv run tools/fontlabtv_fetch.py --limit 30 --thumbnails --media-dir src_docs/md/media
"""

import json
import subprocess
import sys
from pathlib import Path

import fire
import requests

CHANNEL_URL = "https://www.youtube.com/@fontlabtv/videos"
YTDLP = "/Library/Frameworks/Python.framework/Versions/3.13/bin/yt-dlp"


def fetch(
    limit: int = 50,
    out_dir: str = ".omc/notes/fontlabtv",
    thumbnails: bool = False,
    media_dir: str = "src_docs/md/media",
    enrich: bool = False,
) -> None:
    """
    Fetch FontLab TV channel video metadata.

    Args:
        limit:      Maximum number of videos to fetch (0 = all).
        out_dir:    Directory where videos.jsonl is written.
        thumbnails: If True, download thumbnails for each fetched video.
        media_dir:  Directory where thumbnails are saved (used with --thumbnails).
        enrich:     If True, fetch full metadata (upload_date, description) per video.
                    Slower — makes one request per video. Use with small --limit.
    """
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_path / "videos.jsonl"

    print(f"Fetching channel playlist (limit={limit or 'all'}) …")
    cmd = [
        YTDLP,
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--playlist-end", str(limit) if limit > 0 else "0",
        CHANNEL_URL,
    ]
    if limit == 0:
        # Remove --playlist-end 0 which is invalid; omit the flag entirely
        cmd = [c for c in cmd if c != "0" or cmd[cmd.index(c) - 1] != "--playlist-end"]
        # Rebuild without the limit flags
        cmd = [YTDLP, "--flat-playlist", "--dump-json", "--no-warnings", CHANNEL_URL]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"yt-dlp error: {result.stderr[:500]}", file=sys.stderr)
        sys.exit(1)

    lines = [l for l in result.stdout.splitlines() if l.strip()]
    if limit > 0:
        lines = lines[:limit]

    jsonl_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} videos → {jsonl_path}")

    videos = [json.loads(l) for l in lines]

    if enrich:
        print(f"Enriching {len(videos)} videos with full metadata …")
        enriched_path = out_path / "videos_enriched.jsonl"
        urls = [v.get("webpage_url") or f"https://www.youtube.com/watch?v={v['id']}" for v in videos]
        enrich_cmd = [YTDLP, "--skip-download", "--no-warnings", "--print-json"] + urls
        enrich_result = subprocess.run(enrich_cmd, capture_output=True, text=True, timeout=600)
        enriched_lines = [l for l in enrich_result.stdout.splitlines() if l.strip()]
        enriched_path.write_text("\n".join(enriched_lines) + "\n", encoding="utf-8")
        print(f"Wrote {len(enriched_lines)} enriched records → {enriched_path}")

    if thumbnails:
        media_path = Path(media_dir)
        media_path.mkdir(parents=True, exist_ok=True)
        print(f"Downloading thumbnails → {media_path}")
        downloaded = 0
        failed = 0
        for v in videos:
            vid_id = v["id"]
            out_file = media_path / f"fontlabtv-{vid_id}.jpg"
            if out_file.exists():
                print(f"  skip (exists) {vid_id}")
                continue
            # Try maxresdefault first, fall back to hqdefault
            for quality in ("maxresdefault", "hqdefault"):
                url = f"https://i.ytimg.com/vi/{vid_id}/{quality}.jpg"
                try:
                    resp = requests.get(url, timeout=15)
                    if resp.status_code == 200 and len(resp.content) > 5000:
                        out_file.write_bytes(resp.content)
                        print(f"  OK ({quality}) {vid_id}")
                        downloaded += 1
                        break
                except requests.RequestException as e:
                    print(f"  error fetching {url}: {e}", file=sys.stderr)
            else:
                print(f"  FAIL {vid_id}", file=sys.stderr)
                failed += 1
        print(f"Thumbnails: {downloaded} downloaded, {failed} failed, {len(videos) - downloaded - failed} skipped")


if __name__ == "__main__":
    fire.Fire(fetch)

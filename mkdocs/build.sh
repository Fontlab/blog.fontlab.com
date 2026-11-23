#!/usr/bin/env bash
# this_file: mkdocs/build.sh
# Build the adjacent site; remaining arguments are forwarded to the renderer.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

if [[ "${1:-}" == build ]]; then shift; fi
# fly-january (theme + fly plugin) from the local checkout until its first PyPI release;
# at release this becomes a pinned `--with fly-january==X.Y.Z`.
FLY=/Users/adam/Developer/vcs3/github.fontlab/fontlab-www-docstheme.fly
exec uvx --directory .. --python 3.13 --from properdocs==1.6.7 \
  --with mkdocs==1.6.1 \
  --with mkdocs-materialx==10.1.8 \
  --with-editable "$FLY" \
  --with mkdocs-include-markdown-plugin==7.2.2 \
  --with mkdocs-llmstxt==0.5.0 \
  --with mkdocs-glightbox==0.5.2 \
  --with mkdocs-rss-plugin==1.19.0 \
  --with pymdown-extensions==11.0.1 \
  --with pillow \
  properdocs build --config-file mkdocs/mkdocs.yml "$@"

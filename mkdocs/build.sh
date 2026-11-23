#!/usr/bin/env bash
# this_file: mkdocs/build.sh
# Build the adjacent site; remaining arguments are forwarded to the renderer.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

if [[ "${1:-}" == build ]]; then shift; fi
exec uvx --directory .. --python 3.12 --from properdocs==1.6.7 \
  --with mkdocs==1.6.1 \
  --with mkdocs-materialx \
  --with mkdocs-include-markdown-plugin \
  --with mkdocs-llmstxt \
  --with mkdocs-glightbox \
  --with mkdocs-rss-plugin \
  --with pymdown-extensions \
  --with pillow \
  properdocs build --config-file mkdocs/mkdocs.yml "$@"

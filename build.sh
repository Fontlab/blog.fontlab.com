#!/usr/bin/env bash
# this_file: build.sh
#
# Thin wrapper that invokes the blog-fontlab CLI via uv.
#
# Usage:
#   ./build.sh              # defaults to `build`
#   ./build.sh build
#   ./build.sh clean
#   ./build.sh serve
#   ./build.sh --help
#
# uv resolves dependencies from pyproject.toml on first run and caches
# them in .venv/. Subsequent runs are instantaneous.

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${SCRIPT_DIR}"

if [[ $# -eq 0 ]]; then
  exec uv run blog-fontlab build
fi

exec uv run blog-fontlab "$@"

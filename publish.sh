#!/usr/bin/env bash
# this_file: publish.sh
#
# Build the static site, sanity-check the generated output, then publish by
# creating and pushing the next semver git tag via gitnextver. The GitHub
# Actions deploy workflow runs from pushed v*.*.* tags.
#
# Usage:
#   ./publish.sh
#   ./publish.sh --verbose

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${SCRIPT_DIR}"

./build.sh build

required_outputs=(
  "docs/index.html"
  "docs/about/index.html"
  "docs/CNAME"
  "docs/.nojekyll"
  "docs/llms.txt"
  "docs/llms-full.txt"
)

for path in "${required_outputs[@]}"; do
  if [[ ! -f "${path}" ]]; then
    printf 'publish.sh: missing required build output: %s\n' "${path}" >&2
    exit 1
  fi
done

uvx gitnextver --directory "${SCRIPT_DIR}" "$@"

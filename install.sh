#!/usr/bin/env bash
# Install a Living Workspace Agent into your Claude skills folder.
# Usage:
#   bash install.sh            # list available agents
#   bash install.sh blog-engine   # install one
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$HOME/.claude/skills"

# Agents = top-level dirs that contain a SKILL.md
list_agents() {
  for d in "$REPO_DIR"/*/; do
    [ -f "${d}SKILL.md" ] && basename "$d"
  done
}

if [ $# -eq 0 ]; then
  echo "Living Workspace Agents — available to install:"
  echo
  list_agents | sed 's/^/  - /'
  echo
  echo "Install one with:  bash install.sh <name>"
  exit 0
fi

AGENT="$1"
SRC="$REPO_DIR/$AGENT"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "✗ '$AGENT' is not an agent in this repo. Available:"
  list_agents | sed 's/^/  - /'
  exit 1
fi

mkdir -p "$DEST"
TARGET="$DEST/$AGENT"

if [ -d "$TARGET" ]; then
  echo "⚠  $TARGET already exists. Overwrite? [y/N]"
  read -r ans
  case "$ans" in
    [yY]*) rm -rf "$TARGET" ;;
    *) echo "Skipped."; exit 0 ;;
  esac
fi

cp -R "$SRC" "$TARGET"
echo "✓ Installed '$AGENT' to $TARGET"
echo "  Start a new Claude session and it's ready. Just describe what you want."

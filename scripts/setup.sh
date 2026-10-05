#!/bin/sh
# One-time setup for each member: enable the pre-push lint hook and check Python.

cd "$(git rev-parse --show-toplevel)" || exit 1

git config core.hooksPath scripts/hooks
echo "Git hooks enabled (core.hooksPath = scripts/hooks)."

PY=$(command -v python3 || command -v python)
if [ -z "$PY" ]; then
    echo "Python 3 not found. Install Python 3, then run this script again." >&2
    exit 1
fi

if "$PY" -c "import yaml" 2>/dev/null; then
    echo "PyYAML found."
else
    echo "PyYAML is missing. Run: $PY -m pip install -r requirements.txt"
    echo "If pip refuses to install system-wide, create a virtual environment first."
fi

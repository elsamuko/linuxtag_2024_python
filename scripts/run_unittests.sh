#!/usr/bin/env bash
# run unittests in test/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPT_DIR/.."

cd "$MAIN_DIR" || exit

if [ -d venv ]; then
    echo "Using venv"
    source venv/bin/activate
fi

python3 -m unittest --verbose

#!/usr/bin/env bash
# check coverage of tests

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPT_DIR/.."

cd "$MAIN_DIR" || exit

if [ -d venv ]; then
    echo "Using venv"
    source venv/bin/activate
fi

python3 -m coverage run -m unittest
python3 -m coverage report

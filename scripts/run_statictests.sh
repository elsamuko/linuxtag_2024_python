#!/usr/bin/env bash
# run static analyzers

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPT_DIR/.."

cd "$MAIN_DIR" || exit

if [ -d venv ]; then
    echo "Using venv"
    source venv/bin/activate
fi

RC=0

echo "flake8"
flake8 linuxtag
RC=$((RC + $?))

echo "mypy"
mypy linuxtag --ignore-missing-imports
RC=$((RC + $?))

exit $RC

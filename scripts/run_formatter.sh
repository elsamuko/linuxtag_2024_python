#!/usr/bin/env bash
# run black formatter

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPT_DIR/.."

cd "$MAIN_DIR" || exit

if [ -d venv ]; then
    echo "Using venv"
    source venv/bin/activate
fi

RC=0

echo "black"
black linuxtag
RC=$((RC + $?))

exit $RC

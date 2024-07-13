#!/usr/bin/env bash
# setup venv
# sudo apt install python3-venv

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPT_DIR/.."

cd "$MAIN_DIR" || exit

python3 -m venv venv
./venv/bin/python3 -m pip install -r requirements.txt

#!/usr/bin/env bash
# reinstall app as pip
# pip install --upgrade pip
# pip install --upgrade setuptools

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPT_DIR/.."

cd "$MAIN_DIR" || exit

function indent {
    sed 's/^/    /'
}

function green {
    echo -e "\033[1;32m$*\033[0m"
}

green "Removing old package"
./venv/bin/python3 -m pip uninstall linuxtag --yes 2>&1 | indent

green "Cleaning build"
./venv/bin/python3 setup.py clean --all 2>&1 | indent
rm -rf linuxtag.egg-info

green "Installing new package"
./venv/bin/python3 -m pip install . 2>&1 | indent

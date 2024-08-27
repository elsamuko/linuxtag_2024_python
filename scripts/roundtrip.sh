#!/usr/bin/env bash
# roundtrip with json validation

function separator {
    printf %"$COLUMNS"s | tr " " "#"
}

cat << EOF | ./venv/bin/python3 -m linuxtag --json | jq
{
    "foo" : "bar"
}
EOF
separator

cat << EOF | ./venv/bin/python3 -m linuxtag --json | jq
{
    "foo" : {
        "version" : 1,
        "blocks" : {
        }
    }
}
EOF

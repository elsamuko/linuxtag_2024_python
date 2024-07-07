#!/usr/bin/env python3

import yaml

if __name__ == "__main__":
    gitlab = {}

    with open(".gitlab-ci.yml", "r") as file:
        gitlab = yaml.safe_load(file)

    for key, value in gitlab.items():
        if "script" in value:
            commands = value["script"]
            print(f"Running job {key}")
            for command in commands:
                print(f"    {command}")

#!/usr/bin/env python3

import yaml

if __name__ == "__main__":
    github = {}

    with open(".github/workflows/python-app.yml", "r") as file:
        github = yaml.safe_load(file)

    for item in github["jobs"]["build"]["steps"]:
        if "run" in item:
            print(f"Running job {item["name"]}")
            commands = item["run"]
            for command in commands.split("\n"):
                print(f"    {command}")

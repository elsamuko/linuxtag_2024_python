#!/usr/bin/env python3
# https://github.com/pypa/sampleproject/blob/main/setup.py

from setuptools import find_packages, setup

setup(
    name='linuxtag',
    use_scm_version=True,
    description='Demo project for Linuxtag 2024',
    url='https://github.com/elsamuko/linuxtag_2024_python',
    packages=find_packages(),
    test_suite="tests",
    setup_requires=[
        "setuptools_scm", # for use_scm_version
    ],
    install_requires=[
        "importlib-metadata",
    ],
    entry_points={
        "console_scripts": [
            "linuxtag=linuxtag.__main__:main",
        ],
    },
)
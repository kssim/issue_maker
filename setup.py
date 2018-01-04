#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

packages = ["redmine-issue-maker"]

requires = [
    "python-redmine>=2.0.2"
]

with open("README.md", "r") as f:
    readme = f.read()

with open("VERSION", "r") as f:
    version = f.read()

setup(
    name = "redmine_issue_maker",
    version = version,
    description = "Open an issue in redmine by slack.",
    long_description = readme,
    author = "kssim",
    author_email = "ksub0912@gmail.com",
    url = "https://github.com/kssim/redmine_open_issue_by_slack",
    packages = packages,
    packages_data = {},
    packages_dir = {},
    include_package_data = True,
    install_requires = requires,
    license = "MIT",
    zip_safe = False,
    classifiers = (
		"Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ),
)

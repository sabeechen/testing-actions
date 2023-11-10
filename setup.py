"""Simcompass setup package"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

version_file = here / "VERSION"

setup(
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning<2"],
    name="testing_actions",
    packages=find_packages(),
)

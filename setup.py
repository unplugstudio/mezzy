#!/usr/bin/env python

from __future__ import print_function

import os
import sys

from setuptools import setup, find_packages
from codecs import open

from mezzy import __version__

# Get the long description from the README file
with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

# Bump version and generate CHANGELOG
# npm install -g conventional-changelog-cli
if sys.argv[:2] == ["setup.py", "bump"]:
    try:
        version = sys.argv[2]
    except IndexError:
        print("Please provide a version number in the format X.X.X")
        sys.exit(1)
    with open("mezzy/__init__.py", "w") as f:
        f.write('__version__ = "%s"\n' % version)
    with open("package.json", "w") as f:
        f.write('{ "version": "%s" }' % version)
    os.system("conventional-changelog -p angular -i CHANGELOG.md -s")
    os.remove("package.json")
    sys.exit()

# Tag and release the package to PyPI
if sys.argv[:2] == ["setup.py", "release"]:
    os.system("git tag v%s" % __version__)
    os.system("git push && git push --tags")
    os.system("rm -rf dist/")
    os.system("./setup.py sdist")
    os.system("./setup.py bdist_wheel")
    os.system("twine upload dist/*")

setup(
    name="mezzy",
    version=__version__,
    description="Useful utilities for Mezzanine projects",
    long_description=long_description,
    url="https://gitlab.com/unplugstudio/mezzy",
    author="Ed Rivas",
    author_email="ed@unplug.studio",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="django mezzanine utility helper",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True
)

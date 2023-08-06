#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import popobot

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="popobot",
    version=popobot.__version__,
    author="HydroGest",
    author_email="me@mkc.icu",
    description="泡泡aiM机器人库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/HydroGest/PoPoBot",
    py_modules=['popobot'],
    install_requires=[
        "requests <= 2.29.0"
        ],
    classifiers=[
        "Topic :: Games/Entertainment ",
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Board Games',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
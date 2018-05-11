#!/usr/bin/env python
from setuptools import setup

setup(
    name='lukofs',
    packages=['lukofs'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    scripts=['scripts/lukofs'],
)



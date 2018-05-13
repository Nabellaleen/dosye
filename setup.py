#!/usr/bin/env python
from setuptools import setup

from io import open

with open('lukofs/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        raise EnvironmentError('No __version__ found in lukofs package (lukofs/__init__.py)')

setup(
    name='lukofs',
    version=version,
    description='A little webserver to store and manage some files',
    author='F. Briand',
    maintainer='F. Briand',
    url='https://github.com/Nabellaleen/lukofs',

    packages=['lukofs'],
    install_requires=[
        'flask',
    ],
    scripts=['scripts/lukofs'],
)

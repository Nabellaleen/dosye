#!/usr/bin/env python

# Import from standard library
from io import open
from setuptools import setup


with open('dosye/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        raise EnvironmentError(
            'No __version__ found in dosye package (dosye/__init__.py)')

setup(
    name='dosye',
    version=version,
    description='A little webserver to store and manage some files',
    author='F. Briand',
    maintainer='F. Briand',
    url='https://github.com/bepatient-fr/dosye',

    packages=['dosye'],
    install_requires=[
        'flask',
        'Flask-Menu',
        'path.py',
    ],
    scripts=['scripts/dosye'],
)

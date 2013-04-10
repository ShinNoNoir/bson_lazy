#!/usr/bin/env python
import os
import sys

if sys.version < '2.6':
    print 'Python >= 2.6 required'
    sys.exit(1)

from setuptools import setup

if os.path.isfile('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = '''A lazy BSON file loader that leverages PyMongo's
    built-in BSON decoder. Comes with a bson2json utility.'''

setup(
    name = 'bson_lazy',
    version='0.2.3',
    author = 'Raynor Vliegendhart, Rick van Hattem',
    author_email = 'ShinNoNoir@gmail.com, Rick.van.Hattem@Fawo.nl',
    url = 'https://github.com/ShinNoNoir/bson_lazy',
    
    packages=['bson_lazy'],
    scripts=['bin/bson2json.py'],
    
    description = 'A lazy BSON file loader',
    long_description = long_description,
    platforms = 'Any',
    license = 'LICENSE.txt',
    keywords = 'BSON lazy',
    
    install_requires = [
        'PyMongo >= 2.5',
    ],
)


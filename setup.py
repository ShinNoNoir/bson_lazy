#!/usr/bin/env python

import sys
if sys.version < '2.6':
    print 'Python >= 2.6 required'
    sys.exit(1)

from distutils.core import setup

setup(
    name = 'bson_lazy',
    version='0.2.2',
    author = 'Raynor Vliegendhart',
    author_email = 'ShinNoNoir@gmail.com',
    url = 'https://github.com/ShinNoNoir/bson_lazy',
    
    packages=['bson_lazy'],
    scripts=['bin/bson2json.py'],
    
    description = 'A lazy BSON file loader',
    long_description = \
    """A lazy BSON file loader that leverages PyMongo's built-in BSON decoder. """ + \
    """Comes with a bson2json utility.""",
    platforms = 'Any',
    license = 'LICENSE.txt',
    keywords = 'BSON lazy',
    
    install_requires = [
        'PyMongo >= 2.5'
    ],
)

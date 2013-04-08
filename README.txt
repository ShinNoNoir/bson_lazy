===========
bson_lazy
===========

The bson_lazy package provides a `load()` function that lazily reads a 
BSON file. The package also comes with a simple BSON to JSON utility.

Example usage:

    import bson_lazy
    from bson.json_util import dumps
    
    def json_pprint(doc):
        print dumps(doc, sort_keys=True, indent=4, separators=(',',':'))
    
    with open('sample.bson', 'rb') as f:
        for doc in bson_lazy.load(f):
            json_pprint(doc)


The implementation of `bson_lazy.load()` is based on PyMongo's bson package.


Installation
=============

This package can be installed using `pip`:

    pip install https://github.com/ShinNoNoir/bson_lazy/archive/master.zip

Or:

    pip install -e git://github.com/ShinNoNoir/bson_lazy.git#egg=bson_lazy



bson2json.py
=============

This utility displays BSON files to stdout.

Usage: bson2json.py FILE... [OPTIONS]

Options:
  --pretty  Pretty print JSON
  --help    Print this help message

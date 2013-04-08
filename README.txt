===========
bson_lazy
===========

The bson_lazy package provides a `load()` function that lazily reads a 
BSON file.

Example usage:

    import bson_lazy
    import json
    
    def json_pprint(doc):
        print json.dumps(doc, sort_keys=True, indent=4, separators=(',',':'))
    
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

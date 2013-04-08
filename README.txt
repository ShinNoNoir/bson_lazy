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

#!/usr/bin/env python
"""
Simple utility to display BSON files.
"""

import sys
import errno
from bson.json_util import dumps
import bson_lazy

usage = '''
Usage: %s FILE... [OPTIONS]

Options:
  --pretty  Pretty print JSON
  --help    Print this help message
'''.strip() % sys.argv[0]

def main():
    args = sys.argv[1:]
    kwargs = {}
    if '--pretty' in args:
        args.remove('--pretty')
        kwargs = {'sort_keys': True, 'indent': 4, 'separators': (',',':')}
    
    if len(args) == 0 or '--help' in args:
        print >>sys.stderr, usage
        sys.exit()
    
    for path in args:
        try:
            with open(path, 'rb') as f:
                for doc in bson_lazy.load(f):
                    print dumps(doc, **kwargs)
        
        except IOError, e:
            if e.errno != errno.EPIPE:
                print >>sys.stderr, 'ERROR: %s' % e
    

if __name__ == '__main__':
    main()

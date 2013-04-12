import bson
import bson_lazy
import StringIO

from nose import tools

def test_load_normal():
    value = {'hello': 'world'}
    bson_string = bson.BSON.encode(value)

    bson_fh = StringIO.StringIO(bson_string)
    bson_fh.seek(0)
    assert value == bson_lazy.load(bson_fh).next()

@tools.raises(StopIteration)
def test_load_empty():
    bson_lazy.load(StringIO.StringIO()).next()

@tools.raises(bson.InvalidBSON)
def test_invalid_bson():
    value = {'hello': 'world'}
    bson_string = bson.BSON.encode(value)

    bson_fh = StringIO.StringIO(bson_string + '    ')
    bson_fh.seek(0)
    list(bson_lazy.load(bson_fh))

@tools.raises(bson.InvalidBSON)
def test_bad_eeo():
    bson_fh = StringIO.StringIO('\0\0\0\0')
    bson_fh.seek(0)
    list(bson_lazy.load(bson_fh))


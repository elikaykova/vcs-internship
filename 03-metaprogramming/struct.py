"""
Using metaclasses and descriptors define a `Struct` class, that
represents a structure in the C programming language. We can use it
as a normal object in Python, and when needed we can pack it to a binary
representation, that could be read in a C program.
>>> class Message(Struct):
...
...     data = StringField(10)
...     length = IntField()
>>> m = Message(data='helloworld', length=3)
>>> m.schema
[('data', 'char[]'), ('length', 'int')]
>>> repr(m.packed)
"'helloworld\\\\x03\\\\x00\\\\x00\\\\x00'"
>>> m.data = 'hello'
>>> m.length = 5
>>> repr(m.packed)
"'hello\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00\\\\x05\\\\x00\\\\x00\\\\x00'"
>>> m2 = Message(data="foobar", length=6)
>>> repr(m2.packed)
"'foobar\\\\x00\\\\x00\\\\x00\\\\x00\\\\x06\\\\x00\\\\x00\\\\x00'"
"""
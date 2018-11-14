class Predicat:
    def __init__(self, func):
        # print("__init__")
        self.func = func

    def __call__(self, val=None):
        # print("__call__")
        return self.func(val)

    def __and__(self, other):
        return lambda x: self(x) & other(x)

    def __or__(self, other):
        return lambda x: self(x) | other(x)

    def __invert__(self):
        return lambda x: not self(x)

    def __rshift__(self, other):
        return lambda x: other(x) if self(x) else True


def gt(x):
    return Predicat(lambda y: y > x)


def lt(x):
    return Predicat(lambda y: y < x)


def eq(x):
    return Predicat(lambda y: y == x)


def oftype(t):
    return Predicat(lambda x: isinstance(x, t))


def present():
    return Predicat(lambda x: x is not None)


def pred(function):
    return Predicat(lambda x: function(x))


def for_any(*predicats):
    return Predicat(lambda x: any([func(x) for func in predicats]))


def for_all(*predicats):
    return Predicat(lambda x: all([func(x) for func in predicats]))


digit = oftype(int) & gt(-1)  # & lt(10)
binary = eq(0) | eq(1)
number = for_any(oftype(int), oftype(float), oftype(complex))
is_the_empty_string = pred(lambda x: x is "")

a = oftype(int)
print(a(10))
print((~a)(10))

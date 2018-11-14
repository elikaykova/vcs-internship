# def gt(x):
#     return lambda y: y > x


# def lt(x):
#     return lambda y: x > y


# def eq(x):
#     return lambda y: x == y


# def oftype(t):
#     return lambda x: isinstance(x, t)


# def present():
#     return lambda x: x is not None


# def pred(function):
#     return lambda x: function(x)

# lt = make_func(lambda x, y: x > y)
# eq = make_func(lambda y: x == y)
# oftype = make_func(lambda x: isinstance(x, t))
# present = make_func(lambda x: x is not None)
# pred = make_func(lambda x: function(x))

# def for_any(*predicats):
#     return lambda x: any([func(x) for func in predicats])


# def for_all(*predicats):
#     return lambda x: all([func(x) for func in predicats])

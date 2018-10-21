"""
@validate(
    arg('x', [number, lambda x: 0 < x]),
    arg('y', [instance_of(Iterable)]),
)
def calc(x, y):
    pass


Validator could be:

simpe types:
    bool,
    func,
    number,
    string,
    any
    instance_of(type)

cumpaund types:
    one_of(...values),
    one_of_type(...types),
    iterable_of(type),
    mapping_of(type, type)
    shape({prop: type, prop: type})

cusotm function
"""
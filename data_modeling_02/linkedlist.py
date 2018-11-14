import collections
import functools
import operator

nil = "?"


class Cons:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __iter__(self):
        return Iterator(self)

    # def __iter__(self):
    #     item = self
    #     while item is not nil:
    #         yield item
    #         item = item.next

    def __repr__(self):
        return f'<{", ".join([str(i.val) for i in self])}>'

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        index = 0
        node = iter(self)
        while index != key and node.next is not nil:
            node = next(node)
            index = index + 1
        if node.next is nil and index < key - 1:
            raise IndexError
        return node.val


class Iterator:

    def __init__(self, item):
        self.item = item

    def __iter__(self):
        return self

    def __next__(self):
        if self.item is not nil:
            item = self.item
            self.item = self.item.next
            return item
        raise StopIteration


def make_list(*items):
    # print([*items])
    if not [*items]:
        return nil
    return Cons([*items][0], make_list(*[*items][1:]))


"""
Create a linked list with idiomatic python interface

Creation
========

    >>> l = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, nil)))))
    >>> l
    <1, 2, 3, 4, 5>
    >>> l = make_list(1, 2, 3, 4, 5)
    >>> l
    <1, 2, 3, 4, 5>

Iteration
=========

    >>> [li + 1 for li in l]
    [2, 3, 4, 5, 6]

Indexing:
=========

    >>> l[1]
    2
    >>> l[-2]
    4

"""


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# l = Cons(1, Cons(2, Cons(Cons(3, nil), Cons(Cons(Cons(4, nil), Cons(5, nil)), nil))))
# print(l)

# l = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, nil)))))
# print(l)
# print("l[1] =  {} \nl[-1] = {}".format(l[1], l[-1]))
# print(l[0])

# it = iter(l)
# while True:
#     try:
#         print(next(it).val)
#     except StopIteration:
#         break

# for item in l:
#     print("{} ".format(item.val))
# print(l)

print(make_list(1, 2, 3, 4, 5))

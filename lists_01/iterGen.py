# groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]) {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]} iterate
import collections
import functools
import operator


def groupby(func, seq):
    ans = {}
    while seq:
        key = func(seq[0])
        ans[key] = [i for i in seq if func(i) == key]
        seq = [i for i in seq if func(i) != key]
        # print(seq)
    return ans


def compose(f1, f2):
    return lambda x: f1(f2(x))
# a = compose(float, min)
# print(a([-1, 2, 3]))


def iterate(func):
    f = lambda x: x
    while True:
        yield f
        f = compose(func, f)


def double(x):
    return 2 * x


i = iterate(double)
f = next(i)
print(f(3))
f = next(i)
print(f(3))
f = next(i)
print(f(3))
f = next(i)
print(f(3))


def zip_with(func, *iterables):
    min_l = min(map(lambda x: len(x), iterables))
    for i in range(0, min_l):
        yield func(*map(lambda l: l[i], iterables))


def concat3(x, y, z):
    return x + y + z


# first_names = ['John', 'Miles']
# last_names = ['Coltrane', 'Davis']
# spaces = [' '] * 2
# print(list(zip_with(concat3, first_names, spaces, last_names)))

import functools
import operator


def task_1(a, b):
    return [i for i in range(a, b + 1) if i % 2 == 0]


def task_2(str):
    return [i for i in str if i.isupper()]


def task_3(a , b):
    return {i : (i % 5) for i in range(a, b + 1)}


def task_4(arr):
    return {str : (len(str)) for str in arr}


def task_5(arr):
    return len(list(filter(lambda x: x > 0 and x % 2 == 0, arr)))


def task_6(str):
    return len([i for i in str if i.isupper()])


def task_7(a, b):
    return functools.reduce(operator.add, map((lambda x: x**2), range(a, b + 1)))

from collections import abc

from . import feautures

functions = [x for x in dir(feautures) if '__' not in x]

def base(st):
    statistics = {}
    for fn in functions:
        if fn[0] != '_':
            func = getattr(feautures, fn)
            if isinstance(func, abc.Callable):
                statistics[fn] = func(st)
    return statistics

def full(st):
    statistics = {}
    for fn in functions:
        func = getattr(feautures, fn)
        if isinstance(func, abc.Callable):
            statistics[fn] = func(st)
    return statistics

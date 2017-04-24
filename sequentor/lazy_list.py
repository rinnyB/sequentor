from functools import reduce as func_red
from itertools import chain

class lazy_list(list):

    def __str__(self):
        return "lazy_list(" + repr(self) + ")"

    """ ITERABLES """
    def map(self, func):
        return lazy_list(map(func, self))

    def filter(self, func):
        return lazy_list(filter(func, self))

    def flatMap(self, func):
        return lazy_list(chain.from_iterable(map(func, self)))


    """ ONE VALUE """
    def reduce(self, func):
        return func_red(func, self)

    def sum(self):
        return sum(self)

    def count(self):
        return len(self)

    """ foreach """
    def foreach(self, func):
        for elem in self:
            func(elem)

    def reduceByKey(self):
        kv = {}
        for elem in self:
            kv[elem[0]] = kv.get(elem[0],0) + 1
        return lazy_list(kv.items())

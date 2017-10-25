from itertools import chain
from functools import reduce as freduce

class FList(list):
    def __init__(self, *arr):

        if isinstance(arr, tuple):
            if len(arr) == 1:
                super().__init__(arr[0])
            else:
                super().__init__(arr)
        else:
            super().__init__(arr)

    '''Transformations'''

    def map(self, func):
        try:
            return FList(map(func, self))
        except:
            print("Function is not applicable")

    def filter(self, func):
        try:
            return FList(filter(func, self))
        except:
            print("Function is not applicable")

    def flatMap(self, func):
        return FList(chain.from_iterable(map(func, self)))

    def reduce(self, func):
        return freduce(func, self)

    def reduceByKey(self):
        kv = {}
        for elem in self:
            kv[elem[0]] = kv.get(elem[0],0) + 1
        return FList(kv.items())

    '''Output'''
    def foreach(self, func):
        try:
            for elem in self:
                func(elem)
        except Exception as e:
            print("Function is not applicable")

    '''Properties'''
    @property
    def sum(self):
        return sum(self)

    @property
    def count(self):
        return len(self)

    @property
    def size(self):
        return self.count

    @property
    def length(self):
        return self.count

    @property
    def head(self):
        return self[0]

    @property
    def tail(self):
        return self[1:]

    @property
    def toList(self):
        return list(self)

    @property
    def toSet(self):
        return set(self)


    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "FList("  + str(list(self))  + ")"

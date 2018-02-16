from itertools import chain, groupby
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
        self.isSorted = False

    '''Transformations'''


    def map(self, func):
        try:
            return FList(map(func, self))
        except Exception as e:
            raise Exception("MapError: Function is not applicable") from e


    def filter(self, func):
        try:
            return FList(filter(func, self))
        except Exception as e:
            raise Exception("FilterError: Function is not applicable") from e


    def flatMap(self, func):
        try:
            return FList(chain.from_iterable(map(func, self)))
        except Exception as e:
            raise Exception("FlatMapError: function is not applicable") from e


    def reduce(self, func):
        try:
            return freduce(func, self)
        except Exception as e:
            raise Exception("ReduceError") from e


    def sortBy(self, func):
        if not self.isSorted:
            try:
                self.sort(key = func)
                self.isSorted = True
                return self
            except Exception as e:
                raise Exception("SortByError") from e


    def sort(self):
        if not self.isSorted:
            try:
                self.sort()
                self.isSorted = True
                return self
            except Exception as e:
                raise Exception("SortError") from e


    def groupBy(self, func):
        if not self.isSorted:
            self.sortBy(func)
        try:
            return FList([(k, FList(g).map(lambda x: x[1])) for k, g in groupby(self, func)])
        except Exception as e:
            raise Exception("GroupByError") from e


    def reduceByKey(self, func):
        try:
            return FList((key, freduce(func, group)) for key, group in self)
        except Exception as e:
            raise Exception("ReduceByKeyError") from e

    def maxBy(self, func):
        try:
            return max(self, key = func)
        except Exception as e:
            raise Exception("MaxByError") from e

    def argMaxBy(self, func):
        try:
            return self.index(self.maxBy(func))
        except Exception as e:
            raise Exception("ArgMaxByError") from e

    '''Output'''
    def foreach(self, func):
        try:
            for elem in self:
                func(elem)
        except Exception as e:
            raise Exception("ForeachError: funcion is not applicable") from e


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

    @property
    def max(self):
        try:
            return max(self)
        except Exception as e:
            raise Exception("MaxError") from e

    @property
    def min(self):
        try:
            return min(self)
        except Exception as e:
            raise Exception("MinError") from e

    @property
    def avg(self):
        try:
            return self.sum / self.size
        except Exception as e:
            raise Exception("AvgError") from e

    @property
    def mean(self):
        try:
            return self[ int(self.size / 2) ]
        except Exception as e:
            raise Exception("MeanError") from e

    @property
    def argMax(self):
        try:
            return self.argMaxBy(lambda x: x)
        except Exception as e:
            raise Exception("ArgMaxError") from e


    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "FList("  + str(list(self))  + ")"

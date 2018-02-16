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
            print("MapError: Function is not applicable: {}".format(e))


    def filter(self, func):
        try:
            return FList(filter(func, self))
        except Exception as e:
            print("FilterError: Function is not applicable: {}".format(e))


    def flatMap(self, func):
        try:
            return FList(chain.from_iterable(map(func, self)))
        except Exception as e:
            print("FlatMapError: function is not applicable: {}".format(e))


    def reduce(self, func):
        try:
            return freduce(func, self)
        except Exception as e:
            print("Reduce error: {}".format(e))


    def sortBy(self, func):
        if not self.isSorted:
            try:
                self.sort(key = func)
                self.isSorted = True
            except Exception as e:
                print("SortingBy error: {}".format(e))
        return self

    def sort(self):
        if not self.isSorted:
            try:
                self.sort()
                self.isSorted = True
            except Exception as e:
                print("Sorting error: {}".format(e))
        return self


    def groupBy(self, func):
        if not self.isSorted:
            self.sortBy(func)
        try:
            return FList([(k, FList(g).map(lambda x: x[1])) for k, g in groupby(self, func)])
        except Exception as e:
            print("GroupBy error: {}".format(e))


    def reduceByKey(self, func):
        try:
            return FList((key, freduce(func, group)) for key, group in self)
        except Exception as e:
            print("ReduceByKey error: {}".format(e))


    '''Output'''
    def foreach(self, func):
        try:
            for elem in self:
                func(elem)
        except Exception as e:
            print("Function is not applicable: {}".format(e))


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

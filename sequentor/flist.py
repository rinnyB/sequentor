from itertools import chain, groupby
from functools import reduce as freduce

from sequentor.flist_errors import (
    FListError,
    MapError, FilterError, FlatMapError,
    FlattenError, SortError,
    HeadError, TailError)
from sequentor.helpers import require


class FList(list):
    """
    Initialize a FList
    possible inputs to construct FList from:
    - a number of arguments
    - a list
    - a tuple
    """
    def __init__(self, *arr, isSorted=False):
        # arr is always a tuple
        # for example:
        # tuple([list],)
        # tuple((tuple),)
        # tuple(a,r,g,s, ...)
        # tuple(map,) or tuple(filter,)

        if isinstance(arr, tuple):
            if len(arr) == 1:
                if isinstance(arr[0], (map, filter, list, tuple, chain)):
                    super().__init__(arr[0])
                else:
                    try:  # case for single element
                        super().__init__(arr)
                    except Exception as e:
                        raise FListError() from e
            else:
                super().__init__(arr)
        self.isSorted = isSorted

    def map(self, func):
        """Apply func to every element of FList returning a new collection."""
        try:
            return FList(map(func, self))
        except Exception as e:
            raise MapError() from e

    def filter(self, func):
        """Keep elements of FList that satisfy `func` predicate."""
        try:
            return FList(filter(func, self))
        except Exception as e:
            raise FilterError() from e

    def flatten(self):
        """Convert a FList of iterables to a one-dimenstional list."""
        try:
            return FList(chain.from_iterable(self))
        except Exception as e:
            raise FlattenError() from e

    def flatMap(self, func):
        """Apply a function to all of FList, flattening the result."""
        try:
            return self.map(func).flatten()
        except Exception as e:
            raise FlatMapError() from e

    def sortBy(self, func=None):
        """Sort elements of FList using func as a key."""
        try:
            return FList(sorted(self, key=func if func else None))
        except Exception as e:
            raise SortError() from e

    def sorted(self):
        """Sort elements of FList by default ordering."""
        return self.sortBy()

    def sort(self):
        raise FListError("No 'sort' method.")

    def groupBy(self, func):
        res = {}
        for elem in self:
            k = func(elem)
            res[k] = res.get(k, []) + [elem]
        return res

    def zip(self, other):
        size = min(self.size, len(other))
        return FList([(self[i], other[i]) for i in range(0, size)])

    '''Properties'''
    @property
    def head(self):
        try:
            return self[0]
        except Exception as e:
            raise HeadError() from e

    @property
    def tail(self):
        try:
            return self[1:]
        except Exception as e:
            raise TailError() from e

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
    def toList(self):
        return list(self)

    @property
    def toSet(self):
        return set(self)
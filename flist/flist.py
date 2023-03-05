from collections.abc import Callable, Sequence
from typing import TypeVar

from flist.flist_errors import (
    FListError,
    MapError, FilterError, FlatMapError,
    FlattenError, SortError,
    HeadError, TailError,
    InitError, LastError)
from flist.helpers import identity

A = TypeVar('A')
B = TypeVar('B')


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
                if hasattr(arr[0], '__iter__') or isinstance(arr[0], (map, filter, list, tuple)):
                    super().__init__(arr[0])
                else:
                    try:  # case for single element
                        super().__init__(arr)
                    except Exception as e:
                        raise FListError() from e
            
            else:
                super().__init__(arr)
        else:
            raise FListError()
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
        # based on
        # https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable
        def from_iterable(iterables):
            els = []
            for it in iterables:
                if it is not None:
                    for element in it:
                        els.append(element)
                elif it is None:
                    pass
                else:
                    error_msg = "{0} is not iterable".format(it)
                    raise FlattenError(error_msg)
            return els
        try:
            return FList(from_iterable(self))
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
            return FList(sorted(self, key=func))
        except Exception as e:
            raise SortError() from e

    def sorted(self):
        """Sort elements of FList by default ordering."""
        return self.sortBy()

    def sort(self):
        raise FListError("No 'sort' method.")

    def groupBy(self, func):
        """Group elements of FList by func as a key."""
        res = {}
        for elem in self:
            k = func(elem)
            res[k] = res.get(k, []) + [elem]
        return res

    def zip(self, other):
        """Combines each element of FList with elements of other collection."""
        size = min(self.size, len(other))
        return FList([(self[i], other[i]) for i in range(0, size)])

    def zipWithIndex(self):
        """Combines each element of FList with its indexes"""
        return FList([(self[i], i) for i in range(0, self.size)])

    def exists(self, func):
        """Checks if FList has at least one element that satisfies func."""
        if self.size == 0:
            return False
        for item in self:
            if func(item):
                return True
        return False

    def find(self, func):
        """Finds first element in FList that satisfies func."""
        if self.size == 0:
            return None
        for item in self:
            if func(item):
                return item
        return None

    def distinctBy(self, func):
        """Removes all duplicates from FList."""
        elements_present = set()
        new_coll = FList()
        for item in self:
            identifier = func(item)
            if identifier in elements_present:
                pass
            else:
                elements_present.add(identifier)
                new_coll.append(item)
        return new_coll

    def countBy(self, func):
        """Counts elements by func."""
        res = {}
        for elem in self:
            identifier = func(elem)
            res[identifier] = res.get(identifier, 0) + 1
        return res

    def mkString(self, separator: str):
        return separator.join(self.map(str))

    def reduce(self, func):
        raise NotImplementedError

    def fold(self: Sequence[A], zero: B, f: Callable[[A, A], B]) -> B:
        acc = zero
        for a in self:
            acc = f(a, acc)
        return acc

    '''Properties'''

    @property
    def head(self):
        if self.nonEmpty:
            return self[0]
        else:
            raise HeadError()

    @property
    def tail(self):
        if self.nonEmpty:
            return self[1:]
        else:
            raise TailError()

    @property
    def init(self):
        if self.nonEmpty:
            return self[:-1]
        else:
            raise InitError()

    @property
    def last(self):
        try:
            return self[-1]
        except Exception as e:
            raise LastError() from e

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
    def nonEmpty(self):
        return len(self) > 0

    @property
    def isEmpty(self):
        return not self.nonEmpty

    @property
    def toList(self):
        return list(self)

    @property
    def toSet(self):
        return set(self)

    @property
    def distinct(self):
        return self.distinctBy(identity)

# ignore E731
import pytest
from sequentor.flist import FList
from sequentor.flist_errors import (
    MapError, FilterError, FlatMapError,
    FlattenError, SortError)
"""
Test that FList is initialized successfully
for different input types: a single list
and a various arguments list
"""


class Test_FlistInit:
    def test_FList_init_list(self):
        data = [1, 2, 3, 4, 5]
        assert FList(data) == data

    def test_FList_init_args(self):
        data = [1, 2, 3, 4, 5]
        assert FList(*data) == data

    def test_FList_init_list_tuples(self):
        data = [(1, 2), (3, 4), (5, 6)]
        assert FList(data) == data

    def test_FList_init_tuple(self):
        data = (1, 2, 3, 4, 5)
        assert(FList(data) == list(data))

    def test_FList_init_from_map(self):
        data = [1, 2, 3, 4, 5]
        awaited = [2, 3, 4, 5, 6]
        func = lambda x: x + 1
        assert(FList(map(func, data)) == awaited)

    def test_FList_init_from_filter(self):
        data = [1, 2, 3, 4, 5]
        awaited = [1, 2]
        func = lambda x: x < 3
        assert(FList(filter(func, data)) == awaited)


class Test_FListMap:
    def test_FList_map(self):
        data = [1, 2, 3, 4, 5]
        awaited = [0.5, 1, 1.5, 2, 2.5]
        func = lambda x: x / 2
        assert (FList(data).map(func) == awaited)

    def test_FList_map_raise_exception(self):
        data = [1, 2, 3, 4, 5]
        # use inappropriate function
        func = lambda x: x.lower()
        with pytest.raises(MapError):
            FList(data).map(func)


class Test_FListFilter:
    def test_FList_filter(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        awaited = [1, 3, 5, 7, 9]
        func = lambda x: x % 2 == 1
        assert(FList(data).filter(func) == awaited)

    def test_FList_filter_raise_exception(self):
        data = ["this", "is", "a", "list"]
        # use inappropriate function
        func = lambda x: float(x)
        with pytest.raises(FilterError):
            FList(data).filter(func)


class Test_FListFlatten:
    def test_FList_flatten(self):
        data = [[1, 2, 3, 4], [5, 6]]
        awaited = [1, 2, 3, 4, 5, 6]
        assert FList(data).flatten() == awaited

    def test_FList_flatten_raise_exception(self):
        data = [1, 2, 3]
        # can't flatten FList of non-iterables
        with pytest.raises(FlattenError):
            FList(data).flatten()


class Test_FListFlatMap:
    def test_FList_flatMap(self):
        data = [1, 2, 3]
        awaited = [0, 0, 1, 0, 1, 2]
        func = lambda x: range(0, x)
        assert FList(data).flatMap(func) == awaited

    def test_FList_flatMap_raise_exception(self):
        data = [1, 2, 3]
        func = lambda x: x.lower()
        # use inappropriate function
        with pytest.raises(FlatMapError):
            FList(data).flatMap(func)


class Test_FList_sorting:
    def test_FList_sorted(self):
        data = [9, 32, 1, -257]
        assert FList(data).sorted() == [-257, 1, 9, 32]

    def test_FList_sorted_raise_exception(self):
        data = [1, 'some', [1, 2]]
        with pytest.raises(SortError):
            FList(data).sorted()

    def test_FList_sortBy(self):
        data = [{"a": 1, "b": 2}, {"a": -155, "b": 1}]
        func = lambda x: x['a']
        assert FList(data).sortBy(func) ==\
            [{"a": -155, "b": 1}, {"a": 1, "b": 2}]

    def test_FList_sortBy(self):
        data = [{"a": 1, "b": 2}, {"a": -155, "b": 1}]
        func = lambda x: -x['a']
        assert FList(data).sortBy(func) == data

    def test_FList_sortBy_raises_exception(self):
        data = [{"a": 1, "b": 2}, {"a": -155, "b": 1}]
        func = lambda x: x
        with pytest.raises(SortError):
            FList(data).sortBy(func)
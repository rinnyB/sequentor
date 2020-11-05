from collections import namedtuple
import pytest
from sequentor.flist import FList
from sequentor.flist_errors import (
    MapError, FilterError, FlatMapError,
    FlattenError, SortError)


class Test_FlistInit:
    """
    Test that FList is initialized successfully
    for different input types: a single list
    and a various arguments list
    """

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
        assert (FList(data) == list(data))

    def test_FList_init_from_map(self):
        data = [1, 2, 3, 4, 5]
        expected_result = [2, 3, 4, 5, 6]

        def func(x): return x + 1

        assert (FList(map(func, data)) == expected_result)

    def test_FList_init_from_filter(self):
        data = [1, 2, 3, 4, 5]
        expected_result = [1, 2]

        def func(x): return x < 3

        assert (FList(filter(func, data)) == expected_result)


class Test_FListMap:
    def test_FList_map(self):
        data = [1, 2, 3, 4, 5]
        expected_result = [0.5, 1, 1.5, 2, 2.5]

        def func(x): return x / 2

        assert (FList(data).map(func) == expected_result)

    def test_FList_map_raise_exception(self):
        data = [1, 2, 3, 4, 5]

        # use inappropriate function
        def func(x): return x.lower()

        with pytest.raises(MapError):
            FList(data).map(func)


class Test_FListFilter:
    def test_FList_filter(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = [1, 3, 5, 7, 9]

        def func(x): return x % 2 == 1

        assert (FList(data).filter(func) == expected_result)

    def test_FList_filter_raise_exception(self):
        data = ["this", "is", "a", "list"]

        # use inappropriate function
        def func(x): return float(x)

        with pytest.raises(FilterError):
            FList(data).filter(func)


class Test_FListFlatten:
    def test_FList_flatten(self):
        data = [[1, 2, 3, 4], [5, 6]]
        expected_result = [1, 2, 3, 4, 5, 6]
        assert FList(data).flatten() == expected_result

    def test_FList_flatten_raise_exception(self):
        data = [1, 2, 3]
        # can't flatten FList of non-iterables
        with pytest.raises(FlattenError):
            FList(data).flatten()


class Test_FListFlatMap:
    def test_FList_flatMap(self):
        data = [1, 2, 3]
        expected_result = [0, 0, 1, 0, 1, 2]

        def func(x): return range(0, x)

        assert FList(data).flatMap(func) == expected_result

    def test_FList_flatMap_raise_exception(self):
        data = [1, 2, 3]

        def func(x): return x.lower()

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

        def func(x): return x['a']

        assert FList(data).sortBy(func) == \
               [{"a": -155, "b": 1}, {"a": 1, "b": 2}]

    def test_FList_sortBy_2(self):
        data = [{"a": 1, "b": 2}, {"a": -155, "b": 1}]

        def func(x): return -x['a']

        assert FList(data).sortBy(func) == data

    def test_FList_sortBy_raises_exception(self):
        data = [{"a": 1, "b": 2}, {"a": -155, "b": 1}]

        def func(x): return x

        with pytest.raises(SortError):
            FList(data).sortBy(func)


class Test_FListGroupBy:

    def test_FList_groupBy(self):
        # group by first two letters
        data = ['cat', 'tac', 'dog', 'god', 'godeatgod', 'category', 'cats']
        expected_result = {
            'ca': ['cat', 'category', 'cats'],
            'ta': ['tac'],
            'do': ['dog'],
            'go': ['god', 'godeatgod']
        }
        assert FList(data).groupBy(lambda x: x[0:2]) == expected_result

    def test_FList_groupBy_2(self):
        data = [(1, 2), (3, 2), (4, 2), (4, 1), (5, 1)]
        expected_result = {
            2: [(1, 2), (3, 2), (4, 2)],
            1: [(4, 1), (5, 1)]
        }
        assert FList(data).groupBy(lambda x: x[1]) == expected_result

    def test_FList_groupBy_complex_elements(self):
        point = namedtuple("point", ['x', 'y'])
        points = [
            point(1, 1), point(1, 2), point(1, 3),
            point(2, 1), point(2, 21),
            point(3, 4), point(3, 5)
        ]

        assert FList(points).groupBy(lambda p: p.x) == {
            1: [point(1, 1), point(1, 2), point(1, 3)],
            2: [point(2, 1), point(2, 21)],
            3: [point(3, 4), point(3, 5)]
        }

    def test_FList_zip(self):
        data = ['one', 'two', 'three']
        other_data = [1, 2, 3]
        assert FList(data).zip(other_data) == \
               [('one', 1), ('two', 2), ('three', 3)]

    def test_FList_zip_minimal_length_used(self):
        data = ['one', 'two', 'three']
        other_data = [1, 2]
        assert FList(data).zip(other_data) == [('one', 1), ('two', 2)]

    def test_FList_zip_minimal_length_used_2(self):
        data = ['one']
        other_data = [1, 2, 3]
        assert FList(data).zip(other_data) == [('one', 1)]

    def test_zipWithIndex(self):
        data = ['one', 'two', 'three']
        assert FList(data).zipWithIndex() == \
               [('one', 0), ('two', 1), ('three', 2)]

    def test_zipWithIndex_empty_FList(self):
        data = []
        assert FList(data).zipWithIndex() == []


class Test_FListExists:

    def test_exists(self):
        data = [1, 2, 3, 4, 5]
        test_data = FList(data)
        assert test_data.exists(lambda x: x == 1) is True
        assert test_data.exists(lambda x: x == 0) is False

    def test_exists_empty_FList(self):
        assert FList().exists(lambda x: x == 0) is False


class Test_find:

    def test_find(self):
        data = [1, 2, 3, 4, 5]
        test_data = FList(data)
        assert test_data.find(lambda x: x == 1) == 1
        assert test_data.find(lambda x: x == 0) is None

    def test_find_empty(self):
        assert FList().find(lambda x: x == 0) is None


class Test_distinct:

    def test_distinct(self):
        data = [1, 1, 1, 1, 5, 4, 3, 2, 1]
        expected_result = [1, 5, 4, 3, 2]
        assert FList(data).distinct == expected_result

    def test_distinct_empty(self):
        assert FList().distinct == []

    def test_distinctBy(self):
        data = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1]
        expected_result = [1, 2, 3, 4, 5, 6]
        assert FList(data).distinctBy(lambda x: x) == expected_result

    def test_distinctBy_tuples(self):
        data = [("one", "cookie"), ("one", "banana"), ("two", "cakes")]
        expected_result = [("one", "cookie"), ("two", "cakes")]
        assert FList(data).distinctBy(lambda x: x[0]) == expected_result


class Test_countBy:

    def test_countBy(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_result = {True: 4, False: 4}
        assert FList(data).countBy(lambda x: x % 2 == 0) == expected_result

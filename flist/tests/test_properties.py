from collections import namedtuple
import pytest
from sequentor.flist import FList
from sequentor.flist_errors import (
    MapError, FilterError, FlatMapError,
    FlattenError, SortError,
    HeadError, LastError, TailError, InitError)


class Test_FListProperties_head:

    def test_FList_head(self):
        data = [1, 2, 3]
        assert FList(data).head == data[0]

    def test_FList_head_empty(self):
        data = []
        with pytest.raises(HeadError):
            FList(data).head

    def test_FList_head_single_elem(self):
        data = [1]
        assert FList(data).head == data[0]


class Test_FListProperties_tail:

    def test_FList_tail(self):
        data = [1, 2, 3]
        assert FList(data).tail == data[1:]

    def test_FList_tail_empty(self):
        data = []
        with pytest.raises(TailError):
            FList(data).tail

    def test_FList_tail_single_elem(self):
        data = [1]
        assert FList(data).tail == []


class Test_FListProperties_init:

    def test_FList_init(self):
        data = [1, 2, 3]
        assert FList(data).init == [1, 2]

    def test_FList_init_empty(self):
        data = []
        with pytest.raises(InitError):
            FList(data).init

    def test_FList_init_single_elem(self):
        data = [1]  # ?
        assert FList(data).init == []


class Test_FListProperties_last:

    def test_FList_last(self):
        data = [1, 2, 3]
        assert FList(data).last == 3

    def test_FList_last_empty(self):
        data = []
        with pytest.raises(LastError):
            FList(data).last
    
    def  test_FList_last_single_elem(self):
        data = [1]
        assert FList(data).last == 1

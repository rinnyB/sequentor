import pytest
from sequentor.flist import FList

# Test that FList is initialized successfully
# for different input types: a single list
# and a various arguments list

def test_FList_init_list():
    data = [1, 2, 3, 4, 5]
    assert FList(data) == data

def test_FList_init_args():
    data = [1, 2, 3, 4, 5]
    assert FList(*data) == data

def test_FList_init_list_tuples():
    data = [(1,2), (3,4), (5,6)]
    assert FList(data) == data

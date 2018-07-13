import pytest
from sequentor.flist import FList

## Test that FList is initialized successfully
## for different input types: a single list
## and a various arguments list
@pytest.mark.parametrize('data', [[1, 2, 3, 4, 5]])
def test_FList_init(data):
    assert FList(data) == data
    assert FList(*data) == data


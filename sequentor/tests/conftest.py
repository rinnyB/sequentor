import pytest
from sequentor.flist import FList

@pytest.fixture(scope='function', autouse=True)
def lst():
    return FList(range(0, 500000))

@pytest.fixture(scope='function', autouse=True)
def strlst():
    return FList("hello", "little", "world")

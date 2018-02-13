import pytest
from sequentor.flist import FList



@pytest.mark.parametrize('data',
[
[1, 2, 3],
["hello", "world"]
])
def testFList(data):
    assert FList(data) == data
    assert FList( *data ) == data


@pytest.mark.parametrize('data, function, expectedData',
[
    ([1, 2, 3], lambda x: x + 1, [2, 3, 4]),
    (["hello", "world"], lambda x: x.upper(), ["HELLO", "WORLD"])
])
def testMap(data, function, expectedData):
    assert FList(data).map(function) == expectedData


@pytest.mark.parametrize('data, function, expectedData',
[
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x > 5, [6, 7, 8, 9, 10]),
    ([[1, 2, 3], [1, 2], [1,2,3,4], [2]], lambda x: len(x) > 2, [[1,2,3],[1,2,3,4]])
]
)
def testFilter(data, function, expectedData):
    FList(data).filter(function) == expectedData

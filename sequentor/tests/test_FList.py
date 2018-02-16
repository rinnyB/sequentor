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
])
def testFilter(data, function, expectedData):
    FList(data).filter(function) == expectedData


@pytest.mark.parametrize('data, function, expectedData',
[
    ('word', lambda x: x.upper(), ["W", "O", "R", "D"]),
    (['words','about','words'], lambda x: x, ["w","o","r","d","s","a","b","o","u","t","w","o","r","d","s"]),
    ([1, 2, 3], lambda x: range(0, x), [0, 0, 1, 0, 1, 2])
])
def testFlatMap(data, function, expectedData):
    assert FList(data).flatMap(function) == expectedData


@pytest.mark.parametrize('data, function, expectedData',
[
    ([1, 2, 3, 4, 5, 6], lambda x, y: x + y,  1 + 2 + 3 + 4 + 5 + 6),
    ([6, 5, 4, 3, 2, -1], lambda x, y: x - y, 6 - 5 - 4 - 3- 2 - -1 ),
    ([6 , 4, 2], lambda x, y: x / y, ((6 / 4 ) / 2))
])
def testReduce(data, function, expectedData):
    assert FList(data).reduce(function) == expectedData

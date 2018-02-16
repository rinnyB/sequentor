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

def testMapRaises():
    try:
        FList(1, 2, 3).map(lambda x: x.upper())
    except Exception as e:
        assert str(e) == "MapError: Function is not applicable"


@pytest.mark.parametrize('data, function, expectedData',
[
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x > 5, [6, 7, 8, 9, 10]),
    ([[1, 2, 3], [1, 2], [1,2,3,4], [2]], lambda x: len(x) > 2, [[1,2,3],[1,2,3,4]])
])
def testFilter(data, function, expectedData):
    FList(data).filter(function) == expectedData

def testFilterRaises():
    try:
        FList(1, 2, 3).filter(lambda x: len(x) > 5)
    except Exception as e:
        assert str(e) == "FilterError: Function is not applicable"

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


@pytest.mark.parametrize('data, function, expectedData',
[
    ([{'name': 'jack','id' : 1}, {'id': 2, 'name' : 'rinnyB'}, {'name' : 'joe', 'id' :  0}],
    lambda x: x['id'],
    [{'name' : 'joe', 'id' : 0}, {'name': 'jack','id' : 1},  {'id': 2, 'name' : 'rinnyB'}]),
    ([-2,5,4,112, 0, -22, 11], lambda x: x, [-22, -2, 0, 4, 5, 11, 112])

])
def testSortBy(data, function, expectedData):
    _test = FList(data)
    assert _test.isSorted == False
    _transformed = _test.sortBy(function)
    assert _transformed.isSorted == True
    assert _transformed == expectedData



def testMin(lst):
    assert lst.min == 0

def testMax(lst):
    assert lst.max == 499999

def testAvg(lst):
    assert lst.avg == sum(lst) / len (lst)

def testMean(lst, strlst):
    assert lst.mean == 500000/2
    assert strlst.mean == 'little'

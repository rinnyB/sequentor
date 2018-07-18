from sequentor.flist_errors import MapError


class FList(list):
    """
    Initialize a FList
    possible inputs to construct FList from:
    - a number of arguments
    - a list
    - a tuple
    """
    def __init__(self, *arr):
        # arr is always a tuple
        # for example:
        # tuple([list],)
        # tuple((tuple),)
        # tuple(a,r,g,s)
        # tuple(map,) or tuple(filter,)

        if isinstance(arr, tuple):
            if len(arr) == 1:
                if isinstance(arr[0], (map, filter, list, tuple)):
                    super().__init__(arr[0])
            else:
                super().__init__(arr)
        self.isSorted = False

    def map(self, func):
        try:
            return FList(map(func, self))
        except Exception as e:
            print(e)
            raise MapError() from e

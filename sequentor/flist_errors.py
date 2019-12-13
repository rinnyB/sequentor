class FListError(Exception):
    pass


class MapError(FListError):
    pass


class FilterError(FListError):
    pass


class FlattenError(FListError):
    pass


class FlatMapError(FListError):
    pass


class SortError(FListError):
    pass


class HeadError(FListError):
    pass


class TailError(FListError):
    pass

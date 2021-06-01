from typing import Any


def isNumeric(arr):
    flag = True
    for elem in arr:
        if not (isinstance(elem, int) or
                isinstance(elem, float) or
                isinstance(elem, complex)):
            flag = False
            break
    return flag


def require(statement: bool, message: str):
    if not statement:
        raise Exception(message)


def identity(x: Any) -> Any:
    return x

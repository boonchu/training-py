import json
from typing import List, Optional, Callable


# https://www.slingacademy.com/article/union-type-in-python-the-complete-guide/
# Optional Types
resultTypes = Optional[int | float]  # pylint: disable=invalid-name
sqaure: Callable[[int], int] = lambda x: x**2


def avg(_a: int = 100, _b: int = 2) -> float:
    """
    *** Docstring ***
    https://www.programiz.com/python-programming/docstrings

    Finds average of _a and _b

    Args:
        _a (int): an integer
        _b (int): an integer

    Returns:
        (float): average of _a and _b
    """
    return (_a + _b) / 2


def apply(_a: List[int], _f: Callable[[], List[resultTypes]]) -> List[resultTypes]:
    """
    Higher-Order Functions
    https://en.wikipedia.org/wiki/Higher-order_function

    * takes in function (or more) as an argument
    * returns another function
    * or both 1 and 2

    Apply lambda function to list comprehension

    Args:
        _a (int): a List of integer(s)
        _f (int): lambda

    Returns:
        List of (float or int)
    """
    return [_f(i) for i in _a]


def testFormulaImpl(_a: int, _b: int, *args) -> None:
    """
    Test result from average function of a and b

    Args:
        _a (int): an integer
        _b (int): an integer

    Returns:
        None
    """
    print(f"testing inputs {args=} {_a=} {_b=}")
    result = avg(_a, _b)
    try:
        assert result == (_a + _b) / 2
    except Exception as error:
        raise AssertionError(
            json.dumps({"ERROR": "result implements with wrong formula!"})
        ) from error


if __name__ == "__main__":
    VALUE = avg()
    print(f"answer is {VALUE}")

    test_case = {
        "_a": 1,
        "_b": 2,
    }
    testFormulaImpl(**test_case)

    test_case = [1, 2]
    testFormulaImpl(*test_case)

    a: List[int] = [1, 2, 3, 4]
    b: List[int] = [6, 7, 8, 9, 10]
    c: List[int] = [5]
    numbers: List[int] = [*a, *b, *c, 11, 12]
    lists: resultTypes = sorted(apply(numbers, sqaure))
    print(f"answers is {lists=}")

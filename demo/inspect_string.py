#!/usr/bin/env python3

from typing import TypeVar, Union

"""
https://realpython.com/python312-typing/
"""
S = TypeVar("S", str, bytes)

Numbers = Union[int, float]

class Words(str):
    def __len__(self):
        return len(self.split())


class QSorted():
    """
    https://stackoverflow.com/questions/43957034/specifying-a-type-to-be-a-list-of-numbers-ints-and-or-floats
    """
    def qsorted(self, nums: list[Numbers]) -> None:
        nums.append(3.14)
        self.nums = nums[:]


def inspect(text: S) -> S:
    print(f"'{text.upper()}' has length {len(text)}")
    return text


inspect("Hello, World!")
inspect(Words("Hello, World!"))

foo = [1,2,3,4,5]
QSorted.qsorted(foo)

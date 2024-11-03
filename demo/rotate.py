#!/usr/bin/env python3 


def rotate_BoN(nums: list[int], k: int) -> list[int]:
    """
    https://github.com/JenilGajjar20/Competitive-Programming_problems/blob/master/Cpp/189-rotate-array/problem.md#medium

    Given an integer array nums, rotate the array to the right by k steps, 
    where k is non-negative.

    Solution: O(n)
    """

    l = len(nums)
    result = [0] * l

    for i in range(l):
        result[(i+k) % l] = nums[i]

    return result

def rotate_Bo1(nums: list[int], k: int) -> None:
    """
    Solution: O(1)
    - Reverse the first part of the list (0 to n-k-1)
    - Reverse the second part of the list (n-k to n-1)
    - Reverse the entire list
    """

    l = len(nums)
    k = k % l
    nums[:l-k] = reversed(nums[:l-k])
    nums[l-k:] = reversed(nums[l-k:])
    nums[:] = reversed(nums)

nums = [1,2,3,4,5,6,7]
print(rotate_BoN(nums, 3))
rotate_Bo1(nums, 3)
print(nums)

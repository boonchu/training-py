#!/usr/bin/env python3

from numpy.testing import assert_array_equal

class deDuplication:
    def __init__(self, nums: list[int], method: str = 'dedup'):
        """
        Class deDuplication accepts the list of integer and 
        feature with method class label.
        """
        self.nums = sorted(nums)
        self.message = f'procedure how to sorted {method}'


    def removeDuplication(self) -> list[int]:
        dedup_list = []
        for num in self.nums:
            if num not in dedup_list:
                dedup_list.append(num)
        return dedup_list
        #return list(set(self.nums))


    def removeDuplicates1(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        length_nums = len(nums)
        while i < (length_nums - 1):
            j = i + 1
            while j < length_nums:
                if nums[i] == nums[j]:
                    nums[j] = -9999
                j += 1
            i += 1
        nums[:] = [x for x in nums if x>=0]
        return len(nums)


    def removeDuplicates2(self, nums: list[int]) -> int:
        nums.sort()
        i,j=0,1 
        while i<=j and j<len(nums):
            if nums[i] == nums[j]:
                j += 1 
            else:
                nums[i+1] = nums[j]
                i += 1 
        return i+1


    def removeDuplicates3(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

         
nums = deDuplication([0, 1, 3, 1, 2, 1, 3, 4, 0, 3, 4, 1])

print(nums.message)
print(nums.nums)
print(nums.removeDuplication())

numbers = [0, 1, 3, 1, 2, 1, 3, 4, 0, 3, 4, 1]
results = [0, 1, 2, 3, 4]
assert nums.removeDuplicates3(numbers) == 5
assert_array_equal(numbers, results)

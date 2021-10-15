'''
41.Hard First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''
import sys
from typing import List
class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     print(sys.maxsize)
    #     for x in range(1,10000000000000000):
    #         if x not in nums:
    #             return x

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == None or n == 0:
            return 1
        contains_one = 0
        #         for num in nums:
        #             if num==1:
        #                 contains_one=1
        #             elif num<=0 or num>n:
        #                 num=1
        for i in range(n):
            if nums[i] == 1:
                contains_one = 1
            elif nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if contains_one == 0:
            return 1
        # step 2
        for i in range(n):
            # make the index 0 based
            index = abs(nums[i]) - 1
            # if it is negative that means we already have seen it
            if nums[index] > 0:
                nums[index] *= -1
        # step3
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1





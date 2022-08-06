'''
41.Hard First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''
import sys
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)  # inclusive
        if nums == None or n == 0:
            return 1
        if 1 not in nums:
            return 1
        # result range is [1....len(nums)+1]. So we care about only numbers in this range because it will be in this range
        # we are going to find negaitves and numbers than greater n, we convert them to any number in the range. so i choose 1. all numbers will be in [1,len(nums)]
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        nums.sort()
        for i in range(1, n):
            # skip the repeating numbers
            if nums[i] - nums[i - 1] == 0:
                continue
            if nums[i] - nums[i - 1] != 1:
                return nums[i - 1] + 1
        # that means you hit the last element and still no missing value.
        return nums[-1] + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) # inclusive
        if nums == None or n == 0:
            return 1
        if 1 not in nums:
            return 1
        # result range is [1....len(nums)+1]. So we care about only numbers in this range because it will be in this range
        # we are going to find negaitves and numbers than greater n, we convert them to any number in the range. so i choose 1. all numbers will be in [1,len(nums)]
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # after first step, we know that all the elements are in range[1,len(nums)]
        # step 2 (i did not understand this part) this part removes the need for set
        # we are going to map the  numbers to the index and swap the sign
        for i in range(n):
            # make the index 0 based. given the nums[1,n] it was 1 based
            # if i had [7,1,3,1,2,1,1] nums[0]=7-1. now we look up on index 6
            # we use abs incase nums[i] is negative
            index = abs(nums[i]) - 1
            # if it is negative that means we already have seen it. so if it is positive we make it negative to mark it seen
            # now we do lookup
            if nums[index] > 0:
                # this signs that we have seen number index
                nums[index] *= -1
        # step3
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     print(sys.maxsize)
    #     for x in range(1,10000000000000000):
    #         if x not in nums:
    #             return x



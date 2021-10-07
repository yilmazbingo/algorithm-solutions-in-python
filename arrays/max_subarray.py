'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_sum = 0
        for n in nums:
            # remove the negatif prefixes.
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            ans = max(ans, cur_sum)
        return ans

    def brute(selfself,nums:List[int])->int:
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans = max(ans, sum(nums[i:j + 1]))
        return ans

'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
# this is kinda sliding window. KADANE'S algorithm
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_sum = 0
        for num in nums:
            # remove the negatif prefix that came before current positive. they wont help us at all
            # [-2, 1, -3, 4, -1, 2] first -2 was prefix, ignore it start with 1, then -3 and total -2. before 4 ignore total -2
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            ans = max(ans, cur_sum)
        return ans

    def brute(selfself,nums:List[int])->int:
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans = max(ans, sum(nums[i:j + 1]))
        return ans

'''
https://leetcode.com/problems/longest-increasing-subsequence/
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1] * len(nums)
        # i starts at 1
        for i in range(1, len(nums)):
            # j starts at 0 till i
            for j in range(i):
                if nums[j] < nums[i]:
                    counts[i] = max(counts[i], counts[j] + 1)
        return max(counts)
# [10,9,2,5,3,7,101,18]
# [2,3,7,101]
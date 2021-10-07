'''
1. Easy Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
from typing import List
# since we are returning indices, we cannot sort it and run while loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in range(len(nums)):
            if  (target-nums[i]) in res:
                return [i,res[target-nums[i]]]
            res[nums[i]]=i
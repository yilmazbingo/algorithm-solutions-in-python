'''
47. Permutations II
Medium

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

'''

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(nums, path):
            if len(nums) == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i]==nums[i-1]:
                    continue
                # do not take ith element. path+[nums[i]] this creates a list so we dont need append the path.append()
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
        backtrack(nums, [])
        return res
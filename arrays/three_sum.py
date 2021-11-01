'''
15. 3Sum Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need to sort to eliminate duplicates
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # pass the duplicate. i>0 makes sure we start from 1
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            # after here we are looking for two sum
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # [-2,-2,0,2] lets say first -2+2=0 make sure no duplicate, jump to next number
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


'''
414. Third Maximum Number Easy
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''

from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited = set()
        for num in nums:
            visited.add(num)
        #sort() sorts in place, returns None
        sorted_nums = sorted(list(visited));
        if len(sorted_nums) < 3:
            return max(sorted_nums)
        return sorted_nums[-3]

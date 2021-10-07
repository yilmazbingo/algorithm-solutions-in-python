'''
268. Easy Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        store=set()
        for num in nums:
            store.add(num)
        for i in range(len(nums)+1):
            if not i in store:
                return i
        return None
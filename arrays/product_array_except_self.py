'''
    238. Medium Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Prefix= [1, 1, 2, 6]
       Postfix= [24, 12, 4, 1]
'''

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix is the multiplication of elements in order. [1,2,3,4]->[1,2,6,24]
        prefix = [1] * (len(nums))
        left = 1
        # postfix is multiplication of nums in reverse order. [1,2,3,4] -> [24,24,12,4]
        postfix = [1] * (len(nums))
        while left < len(nums):
            prefix[left] = prefix[left - 1] * nums[left - 1]
            left += 1
        right = len(nums) - 2
        while right >= 0:
            postfix[right] = postfix[right + 1] * nums[right + 1]
            right -= 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]
        return result


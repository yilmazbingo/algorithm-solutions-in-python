#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        left = 1
        postfix = [1] * (len(nums))
        while left < len(nums):
            res[left] = res[left - 1] * nums[left - 1]
            left += 1
        right = len(nums) - 2
        while right >= 0:
            postfix[right] = postfix[right + 1] * nums[right + 1]
            right -= 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = res[i] * postfix[i]

        return result


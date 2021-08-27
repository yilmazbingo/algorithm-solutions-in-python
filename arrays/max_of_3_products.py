# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution():
    def maximumProduct(self, nums):
        output = 0
        nums.sort()
        output = max(nums[-3]*nums[-2]*nums[-1],nums[-1]*nums[1]*nums[0])
        return output
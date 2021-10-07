# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution():
    def maximumProduct(self, nums):
        nums.sort()
        # if all nums is negative, we need the maximum neg number which has lowest absolute value |multiplicatino|
        return max(nums[-3]*nums[-2]*nums[-1],nums[-1]*nums[1]*nums[0])
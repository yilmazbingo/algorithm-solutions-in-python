'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

# if we rob house1, we cannot rob last house, or if we rob last house we cannot rob the first hous
class Solution:
    def with_recursive_helper(self,nums):
        if len(nums)==1:
            return nums[0]
        nums1=nums[1:]
        nums2=nums[:-1]
        return max(self.recursive_helper(nums1),self.recursive_helper(nums2))

    def with_tabulated_helper(self,nums):
        if len(nums)==1:
            return nums[0]
        nums1=nums[1:]
        nums2=nums[:-1]
        return max(self.tabulated_helper(nums1),self.tabulated_helper(nums2))

    def recursive_helper(self,nums):
        def rob(i,memo={}):
            if i in memo:
                return memo[i]
            if i<0:
                return 0
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            memo[i] = max(rob(i - 1), rob(i - 2) + nums[i])
            return memo[i]
        return max(rob(len(nums)-1),rob(len(nums)-2))

    def tabulated_helper(self,nums):
        first=nums[0]
        second=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=second
            second=max(first+nums[i],second)
            first=temp
        return second

s=Solution()
print(s.with_recursive_helper([2,3,4,4,5,7]))
print(s.with_tabulated_helper([2,3,4,4,5,7]))


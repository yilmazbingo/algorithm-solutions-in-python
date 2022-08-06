'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Recurrence Relation: is a way break up dynamic programming. result depends only those two values.
rob=max( arr[0]+rob[2:n], rob[1:n] )
'''
from typing import List
class Solution:
    def memoized(self,nums:List[int]):
        def rob(i,memo={}):
            if i in memo:
                return memo[i]
            if i < 0:
                return 0
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            # this is recurrence relation of minimum cost of climbing stairs. a little difference
            #memo[i]=nums[i]+min(climbing(i-1,memo),climbing(i-2,memo))
            memo[i]=max(rob(i-1),rob(i-2)+nums[i])
            return memo[i]
        return max(rob(len(nums) - 1), rob(len(nums) - 2))
    def tabulated(self,nums:List[int]):
        if len(nums) == 1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return max(dp[-1],dp[-2])
    def best(self,nums:List[int])->int:
        if len(nums) == 1:
            return nums[0]
        first=nums[0]
        second=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=second
            second=max(first+nums[i],second)
            first=temp
        return second


s=Solution()
print(s.unoptimized([2,7,9,3,1,32,43,22,11]))
print(s.memoized([2,7,9,3,1,32,43,22,11]))
print(s.tabulated([2,7,9,3,1,32,43,22,11]))

print(s.best([2,7,9,3,1,32,43,22,11]))


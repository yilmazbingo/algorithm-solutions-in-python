"""
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
Once you pay the cost for a step , you can either climb one or two steps.
Find the minimum cost to reach the top of the staircase. Your first step can either be the first or second step.
"""
from typing import List
# T:O(N), S:O(N) for both but runnnig tabulation mthod is faster with python %timeit on jupyter
class Solution:
    def min_cost(self,nums:List[int])->int:
        def climbing(i,memo={}):
            if i in memo:
                return memo[i]
            if i<0:
                return 0
            if i==0 or i==1:
                return nums[i]
            memo[i]=nums[i]+min(climbing(i-1,memo),climbing(i-2,memo))
            # returning memo[i] is faster
            return memo[i]
            #return nums[i] + min(climbing(i - 1), climbing(i - 2))
        return min(climbing(len(nums)-1),climbing(len(nums)-2))
    def tabulation(self,nums:List[int]):
        dp=[0] * len(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            dp[i]=nums[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])


s=Solution()
print(s.min_cost([1, 4, 22, 11, 22]))
print(s.tabulation([1, 4, 22, 11, 22]))



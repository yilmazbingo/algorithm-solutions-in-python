"""
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
Once you pay the cost for a step , you can either climb one or two steps.
Find the minimum cost to reach the top of the staircase. Your first step can either be the first or second step.
"""
# its decision tree is similar to climbing stairs in diffeernt ways. In this ways we need to trees one starts from 0 and another 1.
from typing import List
# T:O(N), S:O(N) for min_cost and tabulation but runnnig tabulation mthod is faster with python %timeit on jupyter
# tabulation_optimized: T:O(N) S:O(1)
class Solution:
    def min_cost(self,nums:List[int])->int:
        def climbing(i,memo={}):
            if i in memo:
                return memo[i]
            if i<0:
                return 0
            if i==0 or i==1:
                return nums[i]
            # i'th step is the current step.
            memo[i]=nums[i]+min(climbing(i-1,memo),climbing(i-2,memo))
            return memo[i]
            #return nums[i] + min(climbing(i - 1), climbing(i - 2)).
            # Because we have two decision trees.
        return min(climbing(len(nums)-1),climbing(len(nums)-2))
    def tabulation(self,nums:List[int]):
        if len(nums) == 1:
            return nums[0]
        dp=[0] * len(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            dp[i]=nums[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
    # this is optimized because we do not create a dp array. only holding 2 values.
    def tabulation_optimized(self,nums:List[int])->int:
        if len(nums) == 1:
            return nums[0]
        first=nums[0]
        second=nums[1]
        for i in range(2,len(nums)):
            temp=second
            second=nums[i]+min(first,second)
            first=temp
        return min(first,second)





s=Solution()
print(s.min_cost([1, 4, 22, 11, 22]))
print(s.tabulation([1, 4, 22, 11, 22]))
print(s.tabulation_optimized([1, 4, 22, 11, 22]))



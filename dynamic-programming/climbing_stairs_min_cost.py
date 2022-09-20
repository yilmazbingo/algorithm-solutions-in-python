"""
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
Once you pay the cost for a step , you can either climb one or two steps.
Find the minimum cost to reach the top of the staircase. Your first step can either be the first or second step.
"""
# Recurrence Relation is formula that we need to derive that gives us the basis of the recursive function that we are trying to write.
'''
minCost(N) =cost(N) + min(min(cost(n-1), cost(n-2) )
'''
#    TOP-DOWN APPROACH
from typing import List
# T:O(N), S:O(N) for min_cost and tabulation but runnnig tabulation mthod is faster with python %timeit on jupyter
# tabulation_optimized: T:O(N) S:O(1)
# Instead of recursive solution, with bottom-up aproach we solve with iteration so we remove the need for the call stack that comes with recursion. we will save space
class Solution:
    def min_cost(self,nums:List[int])->int:
        # each step we ask what is the minimum cost to reach step "i"
        def climbing(i,memo={}):
            if i in memo:
                return memo[i]
            if i<0:
                return 0
            if i==0 or i==1:
                # we have to step on each step, if i==0 or i==1
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
            first, two = two, nums[i] + min(first, two)
        return min(first,second)



 # one,two=1,1
 #        for i in range(n-1):
 #            one,two=two,one+two
 #        return two

s=Solution()
print(s.min_cost([1, 4, 22, 11, 22]))
print(s.tabulation([1, 4, 22, 11, 22]))
print(s.tabulation_optimized([1, 4, 22, 11, 22]))



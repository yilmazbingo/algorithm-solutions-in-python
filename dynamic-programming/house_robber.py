# [1] [2] [3] [4]
# if we decide to rob the first house rob=max(arr[0]+rob[2:n])
# if we skip the first house rob=max(rob[1:n])

from typing import List
class Solution:
    def unoptimized(self,nums:List[int])->int:
        def rob(i:int):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            if i==1:
                return max(nums[0],nums[1])
            return max(rob(i-1),rob(i-2)+nums[i])
        return max(rob(len(nums)-1),rob(len(nums)-2))
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


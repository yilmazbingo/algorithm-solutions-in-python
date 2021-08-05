'''
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.
'''

from typing import List
class Solution:
    def combination(self,nums:List[int],target:int)->List[List[int]]:
        dp=[[] for _ in range(target+1)]
        for num in nums:
            for i in range(target+1):
                if num>i:
                    continue
                if num==i:
                    dp[i].append([num])
                else:
                    for prevList in dp[i-num]:
                        dp[i].append(prevList+[num])
        return dp[target]

s=Solution()
print(s.combination([2,3,6,7],7))
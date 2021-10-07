'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different. we do not want permutation

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
# since they want unique combinations, normal decision wont work.

# T:O(2^Target) one side we choose 2, other side we skip 2
from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(cur,pos,total):
            if total==target:
                res.append(cur.copy())
                return
            if total>target or pos>=len(nums):
                return
            cur.append(nums[pos])
            backtrack(cur,pos,total+nums[pos])
            cur.pop()
            backtrack(cur,pos+1,total)
        backtrack([],0,0)
        return res
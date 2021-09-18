'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
 in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

# T:O(2^N)
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(cur,pos,target):
            if target==0:
                res.append(cur.copy())
            if target<=0:
                return
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i]==prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur,i+1,target-candidates[i])
                cur.pop()
                prev=candidates[i]
        backtrack([],0,target)
        return res
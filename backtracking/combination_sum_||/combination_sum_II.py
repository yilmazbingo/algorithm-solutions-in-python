'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
 in candidates where the candidate numbers sum to target.
------------- THIS IS THE DIFFERENCE FROM COMBINATION 1 --------------------
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''

# In first combinationSum array has distinct values but here not. That is why its decision tree is different

# T:O(2^N)
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(cur,pos,total):
            if total==target:
                res.append(cur.copy())
            # in combinationSum1 we also had to check if pos passed the len(candidates)
            # in this case we used for loop to keep track of uniquness
            if total>=target:
                return
            # we sorted first then we check if next value is the same as current. we can add it but if for the postion of skipping that value we cannot add it
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i]==prev:
                    continue
                # In combinationSum1 we could use the same value again. So after cur.append we backtrack with adding the same value
                # this time we will just adding the next item
                cur.append(candidates[i])
                # each number in the array can be used once.  that is why i+1
                # sum problem is reach total-candidates[i] from the rest of the array
                backtrack(cur,i+1,total+candidates[i])
                cur.pop()
                prev=candidates[i]
        backtrack([],0,0)
        return res

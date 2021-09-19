'''
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

'''

from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        res=[]
        def backtrack(cur,pos,target):
            if target==0 and len(cur)==k:
                res.append(cur.copy())
            if target<=0:
                return
            prev=-1
            for i in range(pos,len(nums)):
                cur.append(nums[i])
                backtrack(cur,i+1,target-nums[i])
                cur.pop()
        backtrack([],0,n)
        return res
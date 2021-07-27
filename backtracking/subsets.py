# Given a set of distinct integers, nums, return all possible subsets
# Set must not contain duplicate subsets

from typing import List
class Solution:
    def brute_solution(self,l:List[int])->List:
        ans=[[]]
        for i in range(len(l)+1):
            # i add +1 because down below it wont be added
            for j in range(i):
                ans.append(l[j:i])
        return ans

    def subsets(self,nums:List[])->List:
        res=[]
        # [1],[2] or [3]
        subset=[]

        def dfs(i):
            if i >=len(nums):
                res.append(subset.copy())
                return
            # shall I include this
            subset.append(nums[i])
            dfs(i+1)
            # not to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

# Given a set of distinct integers, nums, return all possible subsets
# Set must not contain duplicate subsets. it is not permutaion

# T:O(N*2^N)
from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[int]:
        res=[]
        # [1],[2] or [3]
        subset=[]
        # i is the index of the value that we are making decision on
        def dfs(i):
            if i >=len(nums):
                res.append(subset.copy())
                return
            # shall I include nums[i]
            subset.append(nums[i])
            # recursively run dfs on next eleement
            # eachd dfs has a different subset given
            dfs(i+1)
            # decision not to include nums[i]
            subset.pop()
            # above dfs(i+1) is different because it will have a different subset
            dfs(i+1)
        dfs(0)
        return res

s=Solution()
print(s.subsets([1,2,3]))
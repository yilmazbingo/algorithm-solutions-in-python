# Given a set of distinct integers, nums, return all possible subsets
# Set must not contain duplicate subsets. it is not permutaion

# T:O(N*2^N) we have 2^n subsets and each subset can have length n to copy
'''
For every index we are making 2 recursive calls. so time complexity for generating subsets is O(2^n). then u need to copy each subset to the res
How long does it take to copy each. Copying operations is related to the size of the subset, in worst case it is then subset has n elements.
'''
'''
You need to take into account all memory that is allocated by your algorithm (or, rather, the greatest amount of allocated memory that is "in use" at any time) 
 not only on the stack, but also on the heap. Each of the generated subsets is being stored in the subsets list, which will eventually contain 2^n sets, each of size
somewhere between 0 and n (with most of the sets containing around n / 2 elements) - so the space complexity is actually O(n 2^n).
'''
from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[int]:
        res=[]
        # [1],[2] or [3]
        subset=[]
        # i is the index of the value that we are making decision on
        def dfs(i):
            if i ==len(nums):
                res.append(subset.copy())
                return
            # shall I include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # decision not to include nums[i]
            subset.pop()
            # above dfs(i+1) is different because it will have a different subset
            dfs(i+1)
        dfs(0)
        return res

s=Solution()
print(s.subsets([1,2,3]))
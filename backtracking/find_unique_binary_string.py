'''
1980. Find Unique Binary String
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n
that does not appear in nums. If there are multiple answers, you may return any of them.
'''

# since strings are immutable, keep them in an array and then join the array
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        my_set={num for num in nums}
        n=len(nums)
        def backtrack(cur,i):
            if (i==n):
                res="".join(cur)
                return None if res in my_set else res
            res=backtrack(cur,i+1)
            if res: return res
            cur[i]="1"
            res=backtrack(cur,i+1)
            if res: return res
        return backtrack(["0" for _ in nums],0) #backtrack(["0","0","0"],0]




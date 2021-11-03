'''
1980. Find Unique Binary String
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n
that does not appear in nums. If there are multiple answers, you may return any of them.
'''


from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        def backtrack(cur,i):
            if (i==n):
                res="".join(cur)
                return None if res in nums else res
            res=backtrack(cur,i+1)
            if res: return res
            # if n=3 we start with "000". if it does not exist, we switch to "001"
            cur[i]="1"
            res=backtrack(cur,i+1)
            # we are returning either None or string
            if res: return res

        # since strings are immutable, keep them in an array and then join the array-backtrack(["0","0","0"],0]
        # starting case is ["0","0","0"]
        return backtrack(["0" for _ in nums],0)




'''
1980. Find Unique Binary String
Given an array of strings nums containing "N" unique binary strings each of length "N", return a binary string of length n
that does not appear in nums. If there are multiple answers, you may return any of them.
'''

'''
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
'''
# T : O((n+1) * n) For each string we check if that string exists, that takes n
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        str_set={s for s in nums}
        n=len(nums)
        def dfs(cur):
            if len(cur)==n:
                return None if cur in str_set else cur
            for c in ["0","1"]:
                res=dfs(cur+c)
                if res:return res
        return dfs("")

    def findDifferentBinaryStringg(self, nums: List[str]) -> str:
        n=len(nums)
        # cur is the current string. we start with "000" if n==3, i is the index
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




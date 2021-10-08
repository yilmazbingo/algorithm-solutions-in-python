# Given a string s, partition s such that every substring of the partition is a palindrome
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            # this creates width of the decision tree
            for j in range(i, len(s)):
                # i cannot pass s[i:j] as an argument
                if self.palindrome(s, i, j):
                    part.append(s[i:j + 1])
                    # this creates height of the decision tree
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

'''
he time complexity given in the solutions is O(N * 2^N)

I understand that:

there are 2^(N-1) possible partitions,
in the worst case any partition yields palindromes,
checking for palindrome is linear in the size of the input.
'''
'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters
without disturbing the remaining characters' relative positions.("ACE" is a subsequence of "ABCDE" while "AEC" is not).
'''

# T:O(len(s)*len(t)) this is becasuse we are caching. we dont repeat the same work twice
class Solution:
    def distinct(self,s,t):
        cache={}
        # i is the ith pos of s, j is the jth pos of t
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            # if characters match we look at the subproblems. how many different ways can rest of subsequences match each other
            # if they match we increase the both indices.
            if s[i]==t[j]:
                # s=rabbbbit t=rabbit, when first "b" matches, also check for next carracter in s.
                cache[(i,j)]=dfs(i+1,j+1)+dfs(i+1,j)
            # if chars dont match each other, we dont move the j'th but i'th
            else:
                cache[(i,j)]=dfs(i+1,j)
            return cache[(i,j)]
        return dfs(0,0)

s=Solution()
print(s.distinct("rabbbit","rabbit"))

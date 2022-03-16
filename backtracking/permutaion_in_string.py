'''
567-Medium Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''
# this is correct but takes too much time to run
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res=self.permute(s1)
        print(res)
        for perm in res:
            if perm in s2:
                return True
        return False
    def permute(self,s):
        res=[]
        chars=list(s)
        def dfs(chars,path):
            if len(chars)==0:
                res.append("".join(path))
                return
            for i in range(len(chars)):
                dfs(chars[:i]+chars[i+1:],path+[chars[i]])
        dfs(chars,[])
        return res
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        # Counter will count how many letters in
        s1_c = Counter(s1)
        for i in range(len(s2)-window+1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True
        return False
'''
567-Medium Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res=self.permute(s1)
        print(res)
        for perm in res:
            if perm in s2:
                return True
        return False
    def permute(self,str):
        res=[]
        chars=list(str)
        def dfs(chars,path):
            if len(chars)==0:
                res.append("".join(path))
                return
            for i in range(len(chars)):
                dfs(chars[:i]+chars[i+1:],path+[chars[i]])
        dfs(chars,[])
        return res
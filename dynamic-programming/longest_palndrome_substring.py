# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
class Solution:
    def palind(self,s:str):
        res = ""
        res_len = 0
        for i in range(len(s)):
            # STARTING FROM i
            # odd lenght
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -=1
                r +=1
            # even length. starting points are the difference
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -=1
                r +=1
        return res
s=Solution()
print(s.palind("dafjsj"))
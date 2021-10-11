'''
139. Medium Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
#height of tree is len(target)=m
    # brancshing is len(words)=n
    # in each recursive call, I make slicing suffix=target[len(word):]. worst case is m
    # O(N^m * M)=O(n^m)
    # space from callstack is height of  tree=m
    # IN each recursive call I am making suffix and storing it. its lenght is m
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(word, memo={}):
            if word in memo:
                return memo[word]
            if word == "":
                return True
            for w in wordDict:
                if word.startswith(w):
                    suffix = word[len(w):]
                    if dfs(suffix, memo):
                        memo[word] = True
                        return True
            memo[word] = False
            return False
        return dfs(s)


s=Solution()
print(s.memoized("leetcode", ["leet","code"]))
from typing import List
class Solution:
    def word_break(self,target:str,words:List[str]):
        dp=[False] * (len(target)+1)
        dp[0]=True
        for i in range(len(target)):
            for word in words:
                if target[i:i+len(word)]==word:
                    dp[i+len(word)]=True
        return dp[-1]

s=Solution()

print(s.word_break('leetcode',['leet','code']))

from typing import List
class Solution:
    def construct(self,target:str,words:List[str]):
        count=0
        if target=='':
            return 1
        for word in words:
            if target.startswith(word):
                suffix=target[len(word):]
                result=self.construct(suffix,words)
                count+=result
        return count

    def memoized(self,target:str,words:List[str],memo={}):
        if target in memo:
            return memo[target]
        if target=='':
            return 1
        count=0
        for word in words:
            if target.startswith(word):
                suffix=target[len(word):]
                result=self.memoized(suffix,words,memo)
                count+=result
        # memoize before returning a value
        memo[target]=count

        return count

s=Solution()
print(s.construct("purple",["purp","p","ur","le","purpl"]))
print(s.memoized("purple",["purp","p","ur","le","purpl"]))

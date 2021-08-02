# given an array of words, find if u can constrcut the target

from typing import List
class Solution:
    #height of tree is len(target)=m
    # brancshing is len(words)=n
    # in each recursive call, I make slicing suffix=target[len(word):]. worst case is m
    # O(N^m * M)=O(n^m)

    # space from callstack is height of  tree=m
    # IN each recursive call I am making suffix and storing it. its lenght is m
    def construct(self,target:str, words:List[str])->bool:
        if target=="":
            return True
        for word in words:
            if target.startswith(word):
                suffix=target[len(word):]
                if self.construct(suffix,words):
                    return True
        return False

    def memoized(self,target:str, words:List[str],memo={})->bool:
        if target in memo:
            return memo[target]
        if target=="":
            return True
        for word in words:
            if target.startswith(word):
                suffix=target[len(word):]
                if self.construct(suffix,words,memo):
                    # suffix becomes target here
                    memo[target]=True
                    return True
        memo[target]=False
        return False
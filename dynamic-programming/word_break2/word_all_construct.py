'''
the function should return a 2D array containing all of the ways that the 'target' can be constructed
by concatenating elements of the words array
Each element of the 2 array should represent one combination that constructs the 'target'
You may reuse elements of words as many as u need
'''

from typing import List
class Solution:
    # Memoization does not work here. time complexisty is exponential
    def memoized(self,target:str,words:List[str],memo={}):
        if target in memo:
            return memo[target]
        if target=="":
            return [[]]
        result=[]
        for word in words:
            if target.startswith(word):
                suffix=target[len(word):]
                buble_up_ways=self.memoized(suffix,words,memo)
                combinations=[[*way,word] for way in buble_up_ways]
                if combinations:
                    result.extend(combinations)
        memo[target] = result
        return result


# can("abcdef",["ab","abc","cd","def","abcd","ef","c"])
s=Solution()
print(s.construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(s.memoized("purple", ["purp", "p", "ur", "le", "purpl"]))
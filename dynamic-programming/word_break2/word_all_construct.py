'''
WORDBREAK-2-HARD
the function should return a 2D array containing all of the ways that the 'target' can be constructed
by concatenating elements of the words array
Each element of the 2 array should represent one combination that constructs the 'target'
You may reuse elements of words as many as u need
'''

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, memo={}):
            result = []

            if s in memo:
                return memo[s]
            if s == "":
                return [[]]
            for word in wordDict:
                if s.startswith(word):
                    suffix = s[len(word):]
                    bubble_up_ways = dfs(suffix)
                    combinations = [[*way, word] for way in bubble_up_ways]
                    if combinations:
                        # result.extend([" ".join(combination) for combination in combinations])
                        result.extend(combinations)

                        memo[s] = result
            return result

        res = dfs(s)
        for a in res:
            a.reverse()
        return [" ".join(a) for a in res]


# can("abcdef",["ab","abc","cd","def","abcd","ef","c"])
s=Solution()
print(s.construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(s.memoized("purple", ["purp", "p", "ur", "le", "purpl"]))
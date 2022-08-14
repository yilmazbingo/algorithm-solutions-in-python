'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

from typing import List

# ALWAYS CREATE THE DECISION TREE
# T:O(4 ^ N) BECASUE 9->{XWYZ} wors secenoria
L = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
     '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []

        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for letter in L[digits[i]]:
                dfs(i + 1, cur + letter)

        dfs(0, "")
        return res

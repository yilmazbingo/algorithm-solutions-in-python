'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
'''

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            # draw the decision tree
            if len(comb) == k:
                # since comb is object, we need to create a separate one not to modify it later
                res.append(comb.copy())
                return
            for i in range(start, n + 1):
                comb.append(i)
                #conmbination is not same as permutation. duplicates are not allowed
                # that's why we backtrack(i+1)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return res
# time complexity is k * (number of combinations)
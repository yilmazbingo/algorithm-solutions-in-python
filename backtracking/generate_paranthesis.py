'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''

from typing import List

# Our choice do i open or do i close the bracket
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # after generating each result, we clear the stack
        stack =[]
        res =[]
        def backtrack(openN ,closedN):
            # this is end case
            if openN==closedN==n:
                res.append("".join(stack))
                return
            # only add open parantheses if open<n
            if openN<n:
                stack.append("(")
                backtrack(openN+1 ,closedN)
                # everytime we are done with backtracking we have the pop the element we added to the stack
                stack.pop()
            # only add a closing parantheses if closed<n
            if closedN <openN:
                stack.append(")")
                backtrack(openN ,closedN +1)
                stack.pop()
        backtrack(0 ,0)
        return res

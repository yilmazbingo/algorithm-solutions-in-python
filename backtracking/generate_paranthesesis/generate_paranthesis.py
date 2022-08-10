'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''
# this is an example of Catalan Numbers
'''
Time Complexity: O((4^n)/(√n)), in simple terms, the time complexity will be the nth Catalan number.

Space Complexity: O((4^n)/(√n)), including recursion stack space.
'''
from typing import List

# S:O(call stack)=O(n*2)
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
            # only add open parentheses if open<n. you are not comparing openN to closeN
            if openN<n:
                stack.append("(")
                backtrack(openN+1, closedN)
                # when we res.append("".join(stack)) we would pop the item till
                stack.pop()
 # IMPORTANT only add a closing parantheses if   closedN <openN
            if closedN <openN:
                stack.append(")")
                backtrack(openN ,closedN +1)
                stack.pop()
        backtrack(0 ,0)
        return res


'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
'''

from collections import deque
class Solution:
    def __init__(self):
        self._parentheses={ "(": ")", "[": "]", "{": "}" }
    def is_valid(self,S:str):
        if len(S)==0:
            return True
        queue=deque()
        for s in S:
            if s in self._parentheses:
                queue.append(s)
            elif s not in self._parentheses and len(queue)==0:
                return False
            else:
                last_left_par=queue.pop()
                if s!=self._parentheses[last_left_par]:
                    return False
        return len(queue)==0

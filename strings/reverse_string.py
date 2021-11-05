'''
Write a function that reverses a string. The input string is given as an array of characters s.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:

        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

'''
Given a string reverse it wit recursion
'''

class Solution2:
    def reverse(self,s:str)->str:
        if s=="":
            return ""
        if len(s)==1:
            return s
        return self.reverse(s[1:])+s[0]

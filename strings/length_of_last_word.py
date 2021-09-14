'''
58. Length of Last Word

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,length=len(s)-1,0
        while s[i]==" ":
            i-=1
        # now i is at the first characater of the last word
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length


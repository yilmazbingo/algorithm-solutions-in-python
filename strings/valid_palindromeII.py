# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
class Solution:
    def is_palindrome(self ,s :str ,start :int ,end :int )->bool:
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    def validPalindrome(self, s: str) -> bool:

        left =0
        right =len(s) -1
        while left <right:
            if s[left]!=s[right]:
                return self.is_palindrome(s,left +1 ,right) or self.is_palindrome(s ,left ,right -1)
            left+=1
            right-=1
        return True
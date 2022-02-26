# An anagram of a string is another string that contains the same characters, only the order of characters can be different.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted converts string into sorted array
        if "".join(sorted(s))=="".join(sorted(t)):
            return True
        return False

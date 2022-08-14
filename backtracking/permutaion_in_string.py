'''
567-Medium Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
s1 = "ab", s2 = "eidbaooo". s2 contains one permutation of s1 ("ba")

s1 = "ab", s2 = "eidbaooo"
'''
from collections import Counter
class Solution:
    # the length of substring s2 should be equal to that of s1 and frequency of characters in the substring should match to that of s1.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        # Counter will count how many letters in
        s1_c = Counter(s1)
        for i in range(len(s2)-window+1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True
        return False


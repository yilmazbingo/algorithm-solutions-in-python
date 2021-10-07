'''
922 · Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

'''

from collections import defaultdict
class Solution:
    # if you group somehting, think of using a dict
    def groupStrings(self, strings):
        result=defaultdict(list)
        for string in strings:
            key=""
            # I start from 1 because i need to check the prev char
            for char in range(1,len(string)):
                key+=str(((ord(string[char])-ord(string[char-1])) +26 ) % 26)

            result[key].append(string)
        return list(result.values())
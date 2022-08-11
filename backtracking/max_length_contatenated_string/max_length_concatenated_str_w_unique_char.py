'''
1239. Maximum Length of a Concatenated String with Unique Characters
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements in array.
Input: arr = ["un","iq","ue"]
Output: 4

"uniq" ("un" + "iq")
"ique" ("iq" + "ue")
'''
'''
There are 3 conditions:
1- If it overlaps or not. 
2- It does not overlap so we add the string and then look for the next item
3- we do not add it
'''

# T:O(2^n * m) because we either chose an element or not to choose. then we need to build the string. m is the length of the string
# Look at the decision tree
from typing import List
from collections import Counter
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # check if current charset overlaps with the current string which is another set
        def overlap(chars_set, string):
            # here we keep the chars in string
            prev = set()
            for c in string:
                if c in prev or c in chars_set:
                    return True
                prev.add(c)
            return False
        charset=set()
        def backtrack(i):
            # Attention! when the i==len(arr)
            if i == len(arr):
                return len(charset)
            # we need to make two decisions: 1- include the substring
            res = 0
            if not overlap(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                # If I include the i'th index, what will be the res for the rest of strings
                res = backtrack(i + 1)
                # we either include the current or not.
                # after we include now we remove to choose not to include
                for c in arr[i]:
                    charset.remove(c)
            # res is if we process the current arr item and backrack(i+1) is if we skip it
            # before we start to calculate the without including the current item, we have to clean up the set
            return max(res, backtrack(i + 1))
        return backtrack(0)

    def overlap2(self,charset,s):
        c=Counter(charset+Counter(s))
        return max(c.values()) > 1


s = Solution()
s.maxLength(["un", "iq", "ae"])
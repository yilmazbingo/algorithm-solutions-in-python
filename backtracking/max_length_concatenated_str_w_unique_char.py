'''
1239. Maximum Length of a Concatenated String with Unique Characters
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements in array.
'''

from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # stores what we have in our concatenation so far
        charset = set()
        # checking if any character in string exist in charset
        def overlap(chars, string):
            prev = set()
            for c in string:
                if c in prev or c in chars:
                    return True
                prev.add(c)
            return False
        def backtrack(i):
            # if we looped entire array
            if i == len(arr):
                return len(charset)
            res = 0
            if not overlap(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                # we already made our decision at index i, now continue with the i+1 th index
                res = backtrack(i + 1)
                # we cleanup. we do not want those characters to be included when we make our next decision
                for c in arr[i]:
                    # this shows that last element that added is removed
                    print(c)
                    charset.remove(c)
            # when i call backtract this time, our charset will not have string at index i.
            return max(res, backtrack(i + 1))
        return backtrack(0)


s = Solution()
s.maxLength(["un", "iq", "ae"])
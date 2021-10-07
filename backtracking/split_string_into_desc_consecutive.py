'''
1849. Splitting a String Into Descending Consecutive Values
You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
Return true if it is possible to split s​​​​​​ as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.
'''


class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev):
            if index == len(s):
                return True
            # iterate through remainder of the string
            for j in range(index, len(s)):
                val = int(s[index:j + 1])
                # our constraint is val+1==prev. dfs() wont execute if val+1!=prev
                if val + 1 == prev and dfs(j + 1, val):
                    return True
            # if we get here, means we could not split the string
            return False
        # since we have to split, we cannot take entire s. that is why: range(len(s)-1)
        for i in range(len(s) - 1):
            # val is the starting value and it is actually preve value for next dfs()
            val = int(s[:i + 1])
            if dfs(i + 1, val): return True
        return False


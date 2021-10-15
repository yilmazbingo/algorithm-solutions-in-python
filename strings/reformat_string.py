'''
1417. Easy Reformat The String

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

'''

class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        chars = list(s)
        alpha = []
        numerics = []
        res = []
        l = 0
        r = 0
        print(chars)
        for char in chars:
            if char.isalpha():
                alpha.append(char)
            else:
                numerics.append(char)
        if alpha == [] or numerics == []:
            return ""
        print(alpha)
        if len(alpha) > len(numerics):
            while l < len(alpha) and r < len(numerics):
                res.append(alpha[l])
                res.append(numerics[r])
                l += 1
                r += 1
            if len(alpha) - l >= 2:
                return ""
            else:
                res.append(alpha[l])
                return "".join(res)
        elif len(alpha) < len(numerics):
            while l < len(alpha) and r < len(numerics):
                res.append(numerics[r])
                res.append(alpha[l])
                l += 1
                r += 1
            if len(numerics) - r >= 2:
                return ""
            else:
                res.append(numerics[r])
                return "".join(res)
        else:
            while l < len(alpha) and r < len(numerics):
                res.append(numerics[r])
                res.append(alpha[l])
                l += 1
                r += 1
            return "".join(res)

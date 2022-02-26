'''
1417. Easy Reformat The String
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.
'''
class Solution:
    def reformat(self, s: str) -> str:
        if len(s) < 2:
            return s
        alpha = []
        numeric = []
        res = []
        l, r = 0, 0
        for letter in s:
            if letter.isalpha():
                alpha.append(letter)
            else:
                numeric.append(letter)
        len_al, len_nu = len(alpha), len(numeric)
        if abs(len_al - len_nu) >= 2:
            return ""
        if len_al < len_nu:
            while l < len_al and r < len_nu:
                res.append(numeric[r])
                res.append(alpha[l])
                l += 1
                r += 1
            else:
                res.append(numeric[r])
                return "".join(res)
        elif len_al > len_nu:
            while l < len_al and r < len_nu:
                res.append(alpha[l])
                res.append(numeric[r])
                l += 1
                r += 1
            else:
                res.append(alpha[r])
                return "".join(res)
        else:
            while l < len_al and r < len_nu:
                res.append(alpha[l])
                res.append(numeric[r])
                l += 1
                r += 1
            return "".join(res)











'''
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        res = []
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry:
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0
            total = d1 + d2 + carry
            digit, carry = total % 10, total // 10
            res.append(str(digit))
            p1 -= 1
            p2 -= 1
        return "".join(res[::-1])

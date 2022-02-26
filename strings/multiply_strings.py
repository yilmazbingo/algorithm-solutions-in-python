'''
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        # we get rid of leading zeroes after
        res = [0] * (len(num1) + len(num2))
        # reversing so we can start from first index in for loop
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # first add the multiplication to the count value and then mod it
                # i1 + i2 is where we add the result of multiplication
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = (res[i1 + i2] % 10)
        # if 10*10=100 but in res array [0100]. we need to get rid of leading zeroes
        res, beginning = res[::-1], 0
        while beginning < len(res) and res[beginning] == 0:
            beginning += 1
        # convert array to array of strings
        res = map(str, res[beginning:])
        return "".join(res)

    def multiply(self, num1, num2):
        ans = 0
        # The reversed() function returns an iterator that accesses the given sequence in the reverse order.
        for i, x in enumerate(reversed(num1)):
            for j, y in enumerate(reversed(num2)):
                ans += (int(x) * 10 ** (i)) * (int(y) * 10 ** (j))
        return str(ans)

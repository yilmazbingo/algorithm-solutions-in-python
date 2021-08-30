'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        n_str = str(n)
        val = 0
        while True:
            for i in n_str:
                val = val + int(i)*int(i)
            # this will detect a loop
            if val in seen:
                return False
            seen.add(val)
            n_str = str(val)
            if val == 1:
                return True
            val = 0
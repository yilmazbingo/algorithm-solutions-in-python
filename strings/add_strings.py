'''
415. Add Strings Easy
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
'''

from collections import deque
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=deque()
        i,j=len(num1)-1,len(num2)-1
        carry=0
        while i>=0 or j>=0 or carry:
            total=carry
            if i>=0:
                total+=int(num1[i])
                i-=1
            if j>=0:
                total+=int(num2[j])
                j-=1
            # pay attention to here. appending left
            res.appendleft(str(total%10))
            carry=total//10
        return "".join(res)

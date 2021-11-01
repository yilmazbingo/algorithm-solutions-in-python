# 67. Add Binary - Easy
from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=deque()
        i,j=len(a)-1,len(b)-1
        carry=0
        while i>=0 or j>=0 or carry:
            total=carry
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(b[j])
                j-=1
            # pay attention to here. appending left
            res.appendleft(str(total%2))
            carry=total//2
        return "".join(res)
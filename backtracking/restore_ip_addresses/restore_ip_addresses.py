'''
93. Medium Restore IP Addresses
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
'''

from typing import List
# T:O(3^5) cause max height is 5
class Solution:
    def restoreIpAddresses(self,s:str)->List[int]:
        res=[]
        if len(s)>12:
            return res
        def backtrack(pos,dots,curIP):
            # we could have 4 dots but we have not reached the end
            if dots==4 and pos==len(s):
                # chop the last dot .
                res.append(curIP[:-1])
                return
            # we dont need this
            if dots>4:
                return
            # what is (i+3) is out of bounds
            for i in range(pos,min(pos+3,len(s))):
                # cannot have leading zeros except only single 0 like .0 is fine but .03 is not
                # If i==j it can have leading zero because that means length of digit is 1. "123.2"
                # if length is not 1, then first character should not be 0
                if int(s[pos:i+1])<256 and (pos==i or s[pos]!="0"):
                    # each time we make a decison we already add 1 dot
                    # ATTENTION updating index. always i+1 not pos+1
                    backtrack(i+1,dots+1,curIP+s[pos:i+1]+".")
        backtrack(0,0,"")
        return res
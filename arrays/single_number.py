'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
'''
Order of XOR operation does not matter. . 0x0=1x1=0 0x1=1x0=1
num^0 => zero does not change the operation. When we apply xor operation eventually dublicates will end up being 0. 
num^0=num
'''
'''
Python bitwise operators are used to perform bitwise calculations on integers. First, the integers are converted into binary format, 
and then operations are performed bit by bit, hence the name the bitwise operators.

XOR in Python is also known as “exclusive or” that compares two binary numbers bitwise. If both bits are the same, 
the XOR operator outputs 0. If both bits are different, the XOR operator outputs 1. 
The Bitwise XOR sets the input bits to 1 if either, but not both, of the analogous bits in the two operands is 1.
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initalized with zero because num^0=num
        #  if either input is true, then the result is true, but if both inputs are true, then the result is false.
        res=0
        for num in nums:
            res=num^res
        return res

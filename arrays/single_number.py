'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
'''
Order of XOR operation does not matter. . 0x0=1x1=0 0x1=1x0=1
num^0 => zero does not change the operation. When we apply xor operation eventually dublicates will end up being 0. 
num^0=num
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initalized with zero because num^0=num
        res=0
        for num in nums:
            res=num^res
        return res

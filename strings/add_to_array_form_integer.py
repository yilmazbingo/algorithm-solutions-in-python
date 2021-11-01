'''
989. Add to Array-Form of Integer-Easy
The array-form of an integer num is an array representing its digits in left to right order.

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
'''

from typing import List
class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        string = ""
        for num in nums:
            # concatenation will append
            string += str(num)
        res = int(string) + k
        return [int(x) for x in str(res)]

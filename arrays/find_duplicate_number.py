'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
'''

'''
Convert the array to a linked list. There are n+1 position but only n values
     [1,3,4,2,2]     
      0,1,2,3,4
Each index in the array points to array[value]. For example first index is 0 and its value is 1. 0 points to 
array[1] which is 3, second index=1 points to array[3]=2
     0 -> 3 -> 2 ->4
               \
                4
Notice none of the elements after first index ever points to value at index 0. becayse our range is 1-n
'''
# We have to apply Floyd's algorithm to find the cycle

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast are index
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow2
'''
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
'''

'''
Convert the array to a linked list. There are n+1 position but only n values, think values as `pointers` 
     [1,3,4,2,2]     
      0,1,2,3,4
Each index in the array points to array[value]. For example first index is 0 and its value is 1. 0 points to array[1] which is 3, second index=1 points to array[3]=2
     0 -> 3 -> 2 ->4      
               \
                4
                
 Notice 2 is the start of the cycle, 3 and 4 points to 2. 
Notice none of the elements after first index ever points to value at index 0. because our range is 1-n, none of the values will be 0 so
 it is guaranteed that 0 will not be the part of the cycle. so result will never be 0 is guaranteed. 
'''
# We have to apply Floyd's algorithm to find the cycle

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # they always start from zero because 0 is guaranteed that is not part of the cycle
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        # so far we have found where slow and fast met. we are in the cycle
        # this algorithm assumes that distance from beginning to cycle start point is same length as start point to the meeting point of slow and fast
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow2
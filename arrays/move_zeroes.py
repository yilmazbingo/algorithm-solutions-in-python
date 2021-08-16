'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

from typing import List
class Solution:
    def move(self,nums:List[int]):
        j=0
        for num in nums:
            if num!=0:
                nums[j]=num
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
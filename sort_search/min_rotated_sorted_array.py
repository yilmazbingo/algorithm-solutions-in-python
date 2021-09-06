'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        left=0
        right=len(nums)-1
        # res could be any of the nums element
        res=nums[0]
        while left<=right:
            # if subarray is already sorted
            if nums[left]<nums[right]:
                res=min(res,nums[left])
                break
            # if not sorted we do binary search
            medium=(left+right)//2
            res=min(res,nums[medium])
            #now we decide are we going to search left or right
            if nums[medium]>=nums[left]:
                #if we are on the left portion, we search the right portion
                left=medium+1
            else:
                right=medium-1

        return res


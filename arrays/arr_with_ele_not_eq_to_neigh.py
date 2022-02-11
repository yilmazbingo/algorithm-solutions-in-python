'''
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array
such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that
 for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.
'''

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # we sort it and then we try to place each item such that its neighbors is less than itself
        #  list sort() has been using the Timsort algorithm since version 2.3. This algorithm has a runtime complexity of O(n. logn).
        nums.sort()
        res=[]
        left,right=0,len(nums)-1
        while len(res)!=len(nums):
            res.append(nums[left])
            left+=1
            if left<right:
                res.append(nums[right])
                right-=1
        return res
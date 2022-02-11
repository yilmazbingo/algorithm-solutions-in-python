'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
 nums = [5,7,7,8,8,10], target = 8
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(log n) means it is a binary search
        #  sorted array means we use binary search. time complexity should O(Log(N))
        if len(nums)==0:
            return [-1 ,-1]
        first_position =self.binary_search(nums ,0 ,len(nums)-1 ,target)
        if first_position==-1:
            return [-1 ,-1]
        start_position =first_position
        end_position =first_position
        while start_position!=-1:
            temp1 =start_position
            # we are shifting to the left. thats why start_position-1
            start_position =self.binary_search(nums ,0,start_position-1 ,target)
        start_position =temp1
        while end_position != -1:
            temp2 =end_position
            end_position =self.binary_search(nums ,end_position+1 ,len(nums ) -1 ,target)
        end_position =temp2
        return [start_position ,end_position]


    def binary_search(self ,nums :List[int] ,left :int ,right :int ,target :int )->int:
        while left<=right:
            mid =(left +right )//2
            found_value =nums[mid]
            if found_value==target:
                return mid
            elif found_value <target:
                left =mid +1
            else:
                right =mid-1
        return -1


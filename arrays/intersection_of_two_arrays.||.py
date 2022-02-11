'''
350. Easy Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
                # If I didnot remove it [1,2,2,1] and [2] would return [2,2]
                nums2.remove(num)
        return res

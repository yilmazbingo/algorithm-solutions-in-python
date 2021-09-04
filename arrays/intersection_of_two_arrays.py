'''
 350. Intersection of Two Arrays II
 Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
 appear as many times as it shows in both arrays and you may return the result in any order.
'''

from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        visited = set()
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.remove(num)
        return res

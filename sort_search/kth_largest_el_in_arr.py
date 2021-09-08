'''
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

'''

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums[-k]

    def quick_sort(self, A: List[int], low: int, high: int):
        if low <= high:
            pi = self.partition(A, low, high)
            self.quick_sort(A, low, pi - 1)
            self.quick_sort(A, pi + 1, high)

    def partition(self, nums: List[int], low: int, high: int):
        pivot = nums[low]
        i = low
        j = high
        while True:
            if i <= j and nums[i] <= pivot:
                i += 1
            if i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        nums[low], nums[j] = nums[j], nums[low]
        return j

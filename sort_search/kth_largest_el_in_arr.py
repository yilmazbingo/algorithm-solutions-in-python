'''
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

'''
from heapq import heapify,heappop,heappush
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
    # partitioning O(log(N)) and each level we make n comparisons total is O(N * Log(N))
    # worst case is when the array is already sorted. so we will have right skewed tree, so n partitions and n comparisons each level so O(N^2)
    def partition(self, nums: List[int], low: int, high: int):
        pivot = nums[low]
        i = low
        j = high
        # when low,high merges that means we traversed all the elements
        while True:
            if i <= j and nums[i] <= pivot:
                i += 1
            if i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        # after swapping we guarantee that elements to the left of pivot is less, elements to the right are greater
        nums[low], nums[j] = nums[j], nums[low]
        return j

# T :O(k*log(k))
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # this creates min-heap
        heapify(heap)
        #  wheneever you add, it will sort them internally. it will bring the min number on top
        for e in nums:
            heappush(heap,e)
            if len(heap)>k:
                heappop(heap)
        return heappop(heap)

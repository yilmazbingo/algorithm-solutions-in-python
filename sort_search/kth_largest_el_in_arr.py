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
    # first partition has 2 partition, then 4 and each level it increases expoenntially=2^0 + 2^1 + 2^2=log2(N)
    # each partition we make at most n number of comparisons.
    # in the worst case, it is already sorted, quick sort will be called for the right side always. Each level u make n comparisons and then n-1
    # worst case is when the array is already sorted. so we will have right skewed tree, so n partitions and n comparisons each level so O(N^2)
    def partition(self, nums: List[int], low: int, high: int):
        # pivot is greater than left elements but smaller than right elements. partitioning is finding the pivot element.
        pivot = nums[low]
        i = low
        j = high
        # when low,high merges that means we traversed all the elements
        while True:
            if i <= j and nums[i] <= pivot:
                i += 1
            # if element in ith index is greater than pivot, i will stop
            if i <= j and nums[j] > pivot:
                j -= 1
            # becasue of this I cannot write while i<=j
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        # after swapping we guarantee that elements to the left of pivot is less, elements to the right are greater
        # ELEMENT AT jth POSITION IS SWAPPED WITH THE PIVOT. but using pivot instead of nums[low] breaks the app.
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
            #  with O(log n) push and O(log n) pop
            heappush(heap,e)
            if len(heap)>k:
                # this is the critical part.
                heappop(heap)
        return heappop(heap)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target=[]
        for i in nums:
            heapq.heappush(target,(i))
            print(i)
            if len(target)>k:
                heapq.heappop(target)
        print(target)
        return target[0]

s=Solution()
s.findKthLargest([3,2,1,5,6,4], k = 2)


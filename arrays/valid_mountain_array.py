# Leetcode 941. Valid Mountain Array

# Basically find if there is an increasing subarray followed by a decreasing subarruy

from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr ) <3:
            return False
        i=1

        while i<len(arr ) and arr[i]>arr[i-1] :
            i+=1

        if i==1 or i == len(arr):
            return False
        while i<len(arr ) and arr[i]<arr[i-1 ] :
            i+=1
        return i==len(arr)


'''
941-Easy Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

# Basically find if there is an increasing subarray followed by a decreasing subarruy

from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr ) <3:
            return False
        i=1
        while i<len(arr ) and arr[i]>arr[i-1] :
            i+=1
        # i ==1 means it is just a decreasing array
        if i==1 or i == len(arr):
            return False
        while i<len(arr ) and arr[i]<arr[i-1 ] :
            i+=1
        return i==len(arr)


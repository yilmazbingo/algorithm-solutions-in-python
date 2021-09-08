'''
        378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''
from typing import List
class Solution:
    def flatten(self, matrix: List[List[int]], k: int) -> int:
        temp =[]
        for c in matrix:
            temp.extend(c)
        temp.sort()
        return temp[ k -1]

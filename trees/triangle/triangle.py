'''
Medium- Given a triangle array, return the minimum path sum from top to bottom.
 triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row
you may move to either index i or index i + 1 on the next row.
'''
# for each step, you may move to an adjacent number on the row below.
# Memory complexity is O(n). n is the length of array. Because to calculate the min value, we need to keep reference to the lower level
# Time complexity is O(n)

from typing import List
# redraw this as tree.   triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
class Solution:
    def min_total(self,triangle:List[List[int]])->int:
        # dp[] is the bottom row, always starts with base case
        dp=[0]*(len(triangle)+1)
        for row in triangle[::-1]:
            for i,n in enumerate(row):
                # for each step you may move to an adjacent number on the row below
                dp[i]=n+min(dp[i],dp[i+1])
                '''
                    [4, 0, 0, 0, 0]
                    [4, 1, 0, 0, 0]
                    [4, 1, 8, 0, 0]
                    [4, 1, 8, 3, 0]
                    [7, 1, 8, 3, 0]
                    [7, 6, 8, 3, 0]
                    [7, 6, 10, 3, 0]
                    [9, 6, 10, 3, 0]
                    [9, 10, 10, 3, 0]
                    [11, 10, 10, 3, 0]
                '''
        return dp[0]
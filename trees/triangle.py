# Given a triangle array of arrays, find the lowest pathsum
# for each step, you may move to an adjacent number on the row below.
# Memory complexity is O(n). n is the length of array. Because to calculate the min value, we need to keep reference to the lower level
# Time complexity is O(n)

from typing import List
class Solution:
    def min_total(self,triangle:List[List[int]])->int:
        # dp[] is the bottom row
        dp=[0]*(len(triangle)+1)
        for row in triangle[::-1]:
            for i,n in enumerate(row):
                dp[i]=n+min(dp[i],dp[i+1])
        return dp[0]
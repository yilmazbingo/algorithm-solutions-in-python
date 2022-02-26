'''
84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
'''
'''
If stack was decreasing it would be easier to calculate the area as we traverse. [5,4,3]. 5*1, 4*2, 3*3
The problem is when it is i increasing order, I dont know the width In order to calculate the width I use stack
'''

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area =0
        stack =[]
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                max_area =max(max_area, height * (i-index))
                # after we finihed the stack and move to decreased value, the area could be calculated from that index back to start point of stack
                start = index
            stack.append((start ,h))
        # this is if the increasing stack is end of the array
        for i, h in stack:
            max_area = max(max_area, h * (len(heights ) -i))
        return max_area

    def brute(self, heights: List[int]) -> int:
        max_area=0
        n=len(heights)
        for i in range(n):
            min_height=float('inf')
            for j in range(i,n):
                min_height=min(min_height,heights[j])
                max_area=max(max_area,min_height * (j-i+1))
        return max_area

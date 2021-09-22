'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
'''

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area =0
        stack =[] # pair:(index,height)
        for i, h in enumerate(heights):
            start =i
            # if the last element in stack greater than current h, pop it
            while stack and stack[-1][1 ] >h:
                index ,height =stack.pop()
                # height*(i-index) is the height of that histogram we popped
                max_area =max(max_area ,height *( i -index))
                start =index
            stack.append((start ,h))
        for i, h in stack:
            max_area =max(max_area , h *(len(heights ) -i))
        return max_area

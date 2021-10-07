'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
'''

from typing import List
class Solution:
    # if next item is greater we can extend the width, for example,[5,6], 5*2=10
    # as long it is increasing, we can extend the width
    # if heights are not incresing order, they will be popped
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area =0
        # we store a pair:(index,height)
        stack =[]
        for i, h in enumerate(heights):
            start = i
            # if the last element in stack greater than current h, means decreasing, pop it till current h is equal or greater.
            # we are not popiing only one. we are popping in while loop
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                # height*(i-index) is the height of that histogram we popped
                max_area =max(max_area, height * (i-index))
                # as we pop since 1, means [3,2,1], we are changing the index backward
                start = index
            stack.append((start ,h))
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

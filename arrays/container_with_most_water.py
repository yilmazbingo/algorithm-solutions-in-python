'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
'''
'''
What happens if we move larger value b?
- If "b=9" gets larger. it has no direct impact in our calculation. [4,8,1,2,3,9] becasue min would be same and width would get smaller
    area= min(a,b) * (b-a)
   If b was 12 calculation would be same. If larger number gets smaller, min changes so our are would be smaller if b=3
   So we will be moving the smaller value
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        # move smller height. we want to find max container.
        l, r = 0, len(height) - 1
        while l < r:
            # min height is limiting factor. we dont want small height
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            # we are trying to maximize the area
            # we are moving the smaller value in each case
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                # if they are equal, do either
                r -= 1
        return res

    def brute(self, height: List[int]) -> int:
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        return res

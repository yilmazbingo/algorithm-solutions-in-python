'''
001. Number of Pairs of Interchangeable Rectangles

You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles. That means another pair that has same ratio

'''

from typing import List
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)
        # res is the number pairs of that has same ratio
        res = 0
        for c in count.values():
            # if c=1 we cannot create a pair. what are we gonna switch it with
            if c > 1:
                # "/" returns float. it accepts integer. that is why //2
                res += (c * (c - 1)) // 2
        return res
    '''
    combination of 2
    4! / ((4-2)!*2!)
    
    '''
'''
https://www.lintcode.com/problem/919/
'''

"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        # sort by the beginning time because this is the first starting group will wait for next first finishing
        intervals.sort(key=lambda interval:interval.start)
        # If I could use any room, it would be the one that ends quickest. so keep track of ending time
        used_rooms=[intervals[0].end]
        # this operation is done in space S:O(1),T:O(N)
        heapq.heapify(used_rooms)
        for interval in intervals[1:]:
            # if no overlap:
            # we can essentially reuse the same room
            if interval.start>=used_rooms[0]:
                heapq.heappop(used_rooms)
            heapq.heappush(used_rooms,interval.end)
        return len(used_rooms)

s=Solution()
s.minMeetingRooms([(0,30),(5,10),(15,20)])
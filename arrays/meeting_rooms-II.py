'''
https://www.lintcode.com/problem/919/
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        # sort by the beginning time because this is the first starting group will wait for next first finishing
        intervals.sort(key=lambda interval:interval[0])
        # create heap structure
        # start with a value
        used_rooms=[intervals[0][1]]
        # this operation is done in space S:O(1),T:O(N)
        heapq.heapify(used_rooms)
        for interval in intervals[1:]:
            # if no overlap:
            # check if beginning is smaller than end
            if interval[0]>=used_rooms[0]:
                heapq.heappop(used_rooms)
            heapq.heappush(used_rooms,interval[1])
        return len(used_rooms)

s=Solution()
s.minMeetingRooms([(0,30),(5,10),(15,20)])
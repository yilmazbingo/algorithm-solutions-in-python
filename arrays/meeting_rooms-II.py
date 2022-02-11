"""
https://www.lintcode.com/problem/919/
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.
"""


"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# T: O(nLog(N) S:O(N)
"""
[(0,30),(5,10),(15,20)]
start=[0,5,15]
end=[10,20,30]
when start[i]<end[j] that means 1 meeting is going on
"""
class Solution:
    def minMeetingRooms(self, intervals):
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        i,j=0,0
        res,count=0,0
        while i < len(intervals):
            if start[i]<end[j]:
                i+=1
                count+=1
            else:
                j+=1
                count-=1
            res=max(res,count)
        return res
s=Solution()
s.minMeetingRooms([(0,30),(5,10),(15,20)])
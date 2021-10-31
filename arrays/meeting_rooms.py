'''
Easy- Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i:i.start)
        for i in range(len(intervals)-1):
            if intervals[i].end>intervals[i+1].start:
                return False
        return True
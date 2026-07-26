"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key = lambda x: x.start)
        prev_end = 0
        for interval in intervals:
            start, end = interval.start, interval.end
            if start < prev_end:
                return False
            prev_end = end
        return True
        
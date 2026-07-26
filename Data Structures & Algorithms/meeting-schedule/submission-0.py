"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev_end = 0
        for interval in intervals:
            start, end = interval[0], interval[1]
            if start < prev_end:
                return False
            prev_end = end
        return True
        
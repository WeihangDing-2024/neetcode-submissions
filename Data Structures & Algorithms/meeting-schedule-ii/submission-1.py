"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweeping line
        points = []
        for interval in intervals:
            start, end = interval.start, interval.end
            points.append((start, "start"))
            points.append((end, "end"))
        points.sort()

        curr = 0
        res = 0
        for point in points:
            if point[1] == "start":
                curr += 1
                res = max(res, curr)
            else:
                curr -= 1
        
        return res

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        i = 0

        prev_end = -50001

        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            if start < prev_end:
                res += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
            i += 1
        return res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            if i == len(intervals) - 1:
                res.append(intervals[i])
                break

            start, end = intervals[i][0], intervals[i][1]
            nxt_start, nxt_end = intervals[i+1][0], intervals[i+1][1]
            if end < nxt_start:
                res.append(intervals[i])
                i += 1
                continue

            new_start = start
            new_end = max(end, nxt_end)
            i += 1

            while i < len(intervals):
                start, end = intervals[i][0], intervals[i][1]
                if start > new_end:
                    break
                else:
                    new_end = max(end, new_end)
                    i += 1
            res.append([new_start, new_end])
        return res


        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        arr = []
        new_start, new_end = newInterval[0], newInterval[1]
        i = 0
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            if end >= new_start:
                break
            arr.append(intervals[i])
            i += 1

        merged = [new_start, new_end]      
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            if start > new_end:
                break
            merged[0] = min(merged[0], start)
            merged[1] = max(new_end, end)
            i += 1
        
        arr.append(merged)

        while i < len(intervals):
            arr.append(intervals[i])
            i += 1
        
        return arr

            
                
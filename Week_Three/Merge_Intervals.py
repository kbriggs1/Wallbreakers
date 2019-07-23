class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item: item[0])
        for k in range(1, len(intervals)):
            if intervals[k][0] > intervals[k-1][1]:
                continue
            elif intervals[k][1] >= intervals[k-1][1]:
                intervals[k] = [intervals[k-1][0], intervals[k][1]]
                intervals[k-1] = True
            else:
                intervals[k] = intervals[k-1]
                intervals[k-1] = True
        
        return [item for item in intervals if item != True]
        

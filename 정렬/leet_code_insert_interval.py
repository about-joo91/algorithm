class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START = 0
        END = 1
        
        left = 0
        right = len(intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][START] <= newInterval[START]:
                left = mid + 1
            else:
                right = mid -1
        intervals.insert(left, newInterval)
        result = []
        for interval in intervals:
            if not result or result[-1][END] < interval[START]:
                result.append(interval)
            else:
                result[-1][END] = max(result[-1][END], interval[END])
            
        return result

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START = 0
        END = 1
        
        res = []
        for idx, interval in enumerate(intervals):
            if interval[START] > newInterval[END]:
                res.append(newInterval)
                res.extend(intervals[idx:])
                return res
            elif interval[END] < newInterval[START]:
                res.append(interval)
            else:
                newInterval[START] = min(newInterval[START], interval[START])
                newInterval[END] = max(newInterval[END], interval[END])
        
        res.append(newInterval)
        
        return res



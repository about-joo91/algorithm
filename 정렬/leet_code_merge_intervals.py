class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START = 0
        END = 1
        intervals.sort(key=lambda x: x[START])
        result = []
        for interval in intervals:
            if not result or result[-1][END] < interval[START]:
                result.append(interval)
            else:
                result[-1][END] = max(result[-1][END], interval[END])
            
        return result

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        result, end_point = 0, float("-inf")

        for start, end in points:
            if start > end_point:
                result += 1 
                end_point = end

        return result



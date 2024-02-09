class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

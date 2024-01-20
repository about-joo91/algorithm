class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        mid = len(x) // 2
        left = mid -1
        right = mid if len(x) % 2 == 0 else mid +1
        while left >= 0 and right < len(x):
            if x[left] != x[right]:
                return False
            left -= 1
            right += 1
        return True

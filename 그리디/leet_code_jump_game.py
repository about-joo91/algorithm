class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rechable = 0

        for i in range(len(nums)):
            if rechable < i:
                return False
            
            rechable = max(rechable, i + nums[i])

        return True

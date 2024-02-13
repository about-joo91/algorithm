class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = int(10e9)
        left = total = 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                result = min(result, i - left + 1)
                total -= nums[left]
                left +=1
        
        return result if result != int(10e9) else 0
        

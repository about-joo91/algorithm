class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        local_min = local_max = 0
        global_min = 3 * int(10e4)
        global_max = -3 * int(10e4)
        for num in nums:
            total += num
            
            local_min = min(local_min+num, num)
            global_min = min(global_min, local_min)
            
            local_max = max(local_max+num, num)
            global_max = max(global_max, local_max)
        
        if global_max > 0:
            return max(total - global_min, global_max)
        return global_max

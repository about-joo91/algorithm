class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        unique_values = set(nums)
        for unique_value in unique_values:
            if nums.count(unique_value) > n/2:
                return unique_value

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        element = nums[0]
        for value in nums:
            if cnt == 0:
                element = value
            if element == value:
                cnt += 1
            else:
                cnt -=1
        
        return element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

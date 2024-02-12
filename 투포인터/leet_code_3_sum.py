class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue

            left = i+1
            right = len(nums) -1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left +=1
                    right -=1
                elif three_sum < 0:
                    left +=1
                else:
                    right -=1
        
        return result



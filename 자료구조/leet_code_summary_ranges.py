class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        answer = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[start] == nums[i-1]:
                    answer.append(str(nums[start]))
                else:
                    answer.append(f'{nums[start]}->{nums[i-1]}')
                start = i
        
        if nums[start] == nums[-1]:
            answer.append(str(nums[start]))
        else:
            answer.append(f'{nums[start]}->{nums[-1]}')
        
        return answer

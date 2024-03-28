class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def make_permute(permute):
            if len(permute) == len(nums):
                result.append(permute[:])
                return
            
            for num in nums:
                if num not in permute:
                    permute.append(num)
                    make_permute(permute)
                    permute.pop()
        
        result = []
        make_permute([])
        return result

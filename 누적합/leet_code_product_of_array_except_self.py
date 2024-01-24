class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            answers[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            answers[i] *= post
            post *= nums[i]

        return answers

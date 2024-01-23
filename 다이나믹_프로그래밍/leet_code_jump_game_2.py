class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_reach = steps = nums[0]
        cnt = 1

        for i in range(1, n - 1):
            max_reach = max(max_reach, i + nums[i])
            steps -= 1

            if steps == 0:
                cnt += 1
                steps = max_reach - i

        return cnt


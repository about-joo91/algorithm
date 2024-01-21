class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k:
            last_num = nums.pop()
            nums.insert(0, last_num)
            k-=1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_array(left: int, right: int):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1
        

        N = len(nums)
        K = k % N

        reverse_array(0, N-1)
        reverse_array(0, K-1)
        reverse_array(K, N-1)

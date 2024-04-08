class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_left_search):
            index = -1
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    index = mid
                    if is_left_search:
                        right = mid-1
                    else:
                        left = mid+1 
            return index
        
        start = binary_search(True)
        end = binary_search(False)

        return [start, end]

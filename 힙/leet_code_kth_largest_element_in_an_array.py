class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        count = 0
        for num in nums:
            heapq.heappush(min_heap, num)
            count +=1
            if count > k:
                heapq.heappop(min_heap)
        return min_heap[0]

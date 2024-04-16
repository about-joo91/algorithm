class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        pq = [(nums1[0] + nums2[0], 0, 0)]
        n, m = len(nums1), len(nums2)
        visited = set((0, 0))
        
        for _ in range(k):
            _cur_sum, i, j = heapq.heappop(pq)
            result.append([nums1[i], nums2[j]])
            if i+1 < n and (i+1, j) not in visited:
                heapq.heappush(pq, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            if j+1 < m and (i, j+1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
        return result

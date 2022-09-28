import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
left_heap = []
right_heap = []

for _ in range(N):
    cur_num = int(input().rstrip())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -cur_num)
    else:
        heapq.heappush(right_heap, cur_num)
        
    if right_heap and -left_heap[0] > right_heap[0]:
        
        right_value = heapq.heappop(right_heap)
        left_value = heapq.heappop(left_heap)
        
        heapq.heappush(right_heap, -left_value)
        heapq.heappush(left_heap, -right_value)
    print(-left_heap[0])
import heapq
import sys

input = sys.stdin.readline
N = int(input())
max_heap = []

for _ in range(N):
    input_data = int(input())
    if input_data:
        heapq.heappush(max_heap, -input_data)
    else:
        if max_heap: print(-heapq.heappop(max_heap))
        else: print(0)
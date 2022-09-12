import heapq
import sys

input = sys.stdin.readline
N = int(input())
abs_heap = []

for _ in range(N):
    input_data = int(input())
    if input_data:
        push_data = (input_data, 1) if input_data > 0 else (-input_data, -1)
        heapq.heappush(abs_heap, push_data)
    else:
        if abs_heap: 
            number,sign = heapq.heappop(abs_heap)
            print(number * sign)
        else: print(0)
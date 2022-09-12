import heapq

N = int(input())
min_heap = []

for _ in range(N):
    input_data = int(input())
    if input_data:
        heapq.heappush(min_heap, input_data)
    else:
        if min_heap: print(heapq.heappop(min_heap))
        else: print(0)
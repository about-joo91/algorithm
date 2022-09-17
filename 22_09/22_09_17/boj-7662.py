import heapq
import sys
input = sys.stdin.readline

def discard_deleted_nums(heap, exists):
    while heap and not exists[heap[0][1]]:
        heapq.heappop(heap)

def pop_from_heap(heap, exists):
    if heap:
        exists[heap[0][1]] = False
        heapq.heappop(heap)
T = int(input().rstrip())

for _ in range(T):
    K = int(input().rstrip())
    min_heap = []
    max_heap = []
    exists = [False] * K
    for i in range(K):
        operator, num = input().rstrip().split()
        num = int(num)
        if operator == 'I':
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,((-num,i)))
            exists[i] = True
        else:
            if num == 1:
                discard_deleted_nums(max_heap, exists)
                pop_from_heap(max_heap, exists)
            else:
                discard_deleted_nums(min_heap, exists)
                pop_from_heap(min_heap, exists)

    discard_deleted_nums(max_heap, exists)
    discard_deleted_nums(min_heap, exists)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
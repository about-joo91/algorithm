import sys
from collections import deque

cnt = 0
N, M = map(int, sys.stdin.readline().split())
queue = deque(list(range(1,N+1)))
nums_to_find = list(map(int, sys.stdin.readline().split()))
for num in nums_to_find:
    if queue[0] == num:
        queue.popleft()
        continue
    idx = queue.index(num)
    minus_idx = len(queue) - idx
    if idx < minus_idx:
        queue.rotate(-1*idx)
        queue.popleft()
        cnt+= idx
    else:
        queue.rotate(minus_idx)
        queue.popleft()
        cnt+= minus_idx
print(cnt)
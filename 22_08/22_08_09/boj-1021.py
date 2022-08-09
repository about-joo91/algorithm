import sys
from collections import deque

cnt = 0
N, M = map(int, sys.stdin.readline())
queue = deque(list(range(1,N+1)))
print(queue.index(2))
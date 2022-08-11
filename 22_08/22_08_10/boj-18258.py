import sys
from collections import deque

iter_num = int(sys.stdin.readline())
queue = deque()
for _ in range(iter_num):
    operator = sys.stdin.readline().split()
    if operator[0] == 'push':
        queue.append(operator[1])
    elif operator[0] == 'size':
        print(len(queue))
    elif operator[0] == 'empty':
        if queue: print(0)
        else: print(1)
    elif operator[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif operator[0] =='pop':
        if queue: print(queue.popleft())
        else: print(-1)
    else:
        if queue: print(queue[-1])
        else: print(-1)

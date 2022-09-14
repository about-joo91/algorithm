from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    operators = input().split()
    operator = operators[0]
    if operator == "push":
        queue.append(operators[1])
    elif not queue and (operator=="pop" or operator == "front" or operator == "back"):
        print(-1)
    elif operator == "empty":
        print(int(len(queue) == 0))
    elif operator == "pop":
        print(queue.popleft())
    elif operator == "size":
        print(len(queue))
    elif operator == "front":
        print(queue[0])
    elif operator == "back":
        print(queue[-1])
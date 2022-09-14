from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    operators = input().split()
    operator = operators[0]
    if operator == "push_back":
        queue.append(operators[1])
    elif operator == "push_front":
        queue.appendleft(operators[1])
    elif not queue and (operator=="pop_front" or operator=="pop_back" or operator == "front" or operator == "back"):
        print(-1)
    elif operator == "empty":
        print(int(len(queue) == 0))
    elif operator == "pop_front":
        print(queue.popleft())
    elif operator == "pop_back":
        print(queue.pop())
    elif operator == "size":
        print(len(queue))
    elif operator == "front":
        print(queue[0])
    elif operator == "back":
        print(queue[-1])
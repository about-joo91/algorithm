from collections import deque

N, K = map(int, input().split())
queue = deque(list(range(1, N+1)))
answer = []
while queue:
    queue.rotate(-K)
    answer.append(queue.pop())

print('<' + ", ".join(list(map(str, answer)))+">")
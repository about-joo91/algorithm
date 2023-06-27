import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[ ] for _ in range(N+1)]
counts = [0] * (N+1)
answer = [0] * (N+1)

for _ in range(M):
    pre, cur = map(int, input().rstrip().split())
    graph[pre].append(cur)
    counts[cur] +=1

queue = deque()
for node in range(1, N+1):
    if counts[node] == 0:
        queue.append((node, 1))
        answer[node] = 1

while queue:
    cur_node, cnt = queue.popleft()
    for next_node in graph[cur_node]:
        counts[next_node] -= 1
        if counts[next_node] == 0:
            queue.append((next_node, cnt+1))
            answer[next_node] = cnt+1

print(*answer[1:])
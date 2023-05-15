import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[ ] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()

def bfs(start):
    cnt = 1
    queue = deque()
    queue.append(start)
    visited[start] = cnt
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node]: continue
            cnt+=1
            visited[next_node] = cnt
            queue.append(next_node)
    return cnt

bfs(R)

for visited_idx in visited[1:]:
    print(visited_idx)

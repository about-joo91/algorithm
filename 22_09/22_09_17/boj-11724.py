from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[ ] for _ in range(N+1)]
visited = [0] * (N+1) 

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                queue.append(next_node)


for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        if not graph[i]:
            cnt+=1
            visited.append(i)
        else:
            bfs(i)
            cnt+=1
print(cnt)
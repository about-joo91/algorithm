from collections import deque

N, M = map(int, input().split())
graph = [[ ] for _ in range(N+1)]
for _ in range(N-1):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))
    graph[end].append((dist, start))

def dfs(cur_node, target_node, cur_dist):
    global answer
    visited[cur_node] = True
    if cur_node == target_node:
        answer = cur_dist
        return

    for next_dist, next_node in graph[cur_node]:
        if visited[next_node]:continue
        dfs(next_node, target_node, cur_dist + next_dist)

def bfs(start, end):
    queue = deque()
    visited = [False] * (N+1)

    queue.append((0, start))
    visited[start] = True
    
    while queue:
        cur_dist, cur_node = queue.popleft()

        if cur_node == end:
            return cur_dist
        
        for next_dist, next_node in graph[cur_node]:
            if visited[next_node]: continue
            visited[next_node] = True
            queue.append((cur_dist + next_dist, next_node))
    
    return -1

for _ in range(M):
    start, end = map(int, input().split())
    answer = bfs(start,end)
    print(answer)
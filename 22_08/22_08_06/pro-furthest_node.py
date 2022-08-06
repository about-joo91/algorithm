import sys
from collections import deque
def solution(n, edge):
    max_size = sys.maxsize
    visited = [0] * (n+1)
    graph = [[ ] for _ in range(n+1)]
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    queue = deque([1])
    visited[1] = 1
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[node]+1
                queue.append(next_node)
    return visited.count(max(visited))
    
        
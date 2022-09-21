from collections import deque

N, M = map(int, input().split())
graph = [[ ] for _ in range(N+1)]

def bfs(start):
    bacon = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
                bacon[next_node] += bacon[node] + 1
    
    return sum(bacon)
        


for _ in range(M):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

result = []
for i in range(1, N+1):
    result.append(bfs(i))


print(result.index(min(result))+1)
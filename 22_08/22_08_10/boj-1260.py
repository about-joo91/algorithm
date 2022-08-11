from collections import deque
def bfs(graph, start):
    vistied = []
    queue = deque([start])
    visited.append(start)
    while queue:
        cur_node = queue.popleft()
        for next_node in sorted(graph[cur_node]):
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    return visited
def dfs(graph, start):
    visited =[]
    stack = []
    stack.append(start)
    while stack:
        cur_node = stack.pop()
        if cur_node not in visited:
            visited.append(cur_node)
            stack.extend(sorted(graph[cur_node] , reverse=True))
    return visited
N, M, V = map(int, input().split())
visited = []
graph = [[ ] for _ in range(N+1)]
for _ in range(M):
    fir, sec = map(int, input().split())
    graph[fir].append(sec)
    graph[sec].append(fir)
print(' '.join(list(map(str,dfs(graph, V)))))
print(' '.join(list(map(str,bfs(graph, V)))))
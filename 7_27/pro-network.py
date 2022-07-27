
def dfs(visited, graph, node):
    if visited[node] == 0:
        visited[node] = 1
        for next_node in graph[node]:
            if visited[next_node] == 0:
                dfs(visited, graph, next_node)
        return True
    

def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    cnt = 0
    visited = [0] * n
    for i in range(n):
        if dfs(visited, graph, i):
            cnt+=1
    return cnt



print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
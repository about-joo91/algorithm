def dfs(visited, computers, node):
    if visited[node] == 0:
        visited[node] = 1
        for idx, is_network in enumerate(computers[node]):
            if visited[idx] == 0 and is_network:
                dfs(visited, computers, idx)
        return True
    return False

def solution(n, computers):
    cnt = 0
    visited = [0] * n
    for i in range(n):
        if dfs(visited, computers, i):
            cnt+=1
    return cnt



print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
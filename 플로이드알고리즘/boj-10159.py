N = int(input())
M = int(input())
graph = [[False] * N for _ in range(N)]

for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy-1][light-1] = True

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

for i in range(N):
    cnt = 1
    for j in range(N):
        if graph[i][j] or graph[j][i]:
            cnt += 1
    print(N - cnt)

# N = int(input())
# M = int(input())
# heavier = [[ ] for _ in range(N+1)]
# lighter = [[ ] for _ in range(N+1)]


# for _ in range(M):
#     heavy, light = map(int, input().split())
#     heavier[heavy].append(light)
#     lighter[light].append(heavy)


# def dfs(cur_node, graph):
#     global answer

#     if visited[cur_node]:
#         return
#     visited[cur_node] = True
#     answer +=1
    
#     for next_node in graph[cur_node]:
#         dfs(next_node, graph)


# for i in range(1, N+1):
#     visited = [False] * (N+1)
#     answer = 0
#     dfs(i, heavier)
#     visited = [False] * (N+1)
#     dfs(i, lighter)
#     print(N -(answer-1))
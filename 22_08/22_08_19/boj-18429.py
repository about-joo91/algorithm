import sys
N, K = map(int, sys.stdin.readline().split())
weight_sets = list(map(int, sys.stdin.readline().split()))
LIMIT = 500
cur_weight = 500
cnt = 0
visited = [0] * N
def dfs(depth, idx, cur_weight):
    global cnt
    if depth == N-1:
        cnt+=1
    next_weight = cur_weight - K
    for i in range(N):
        if visited[i] == 0 and (next_weight + weight_sets[i]) >= LIMIT:
            visited[i] = 1
            dfs(depth+1, i+1, next_weight + weight_sets[i])
            visited[i] = 0
dfs(0, 0, cur_weight)
print(cnt)
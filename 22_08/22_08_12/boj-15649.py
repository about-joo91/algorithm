N, M = map(int, input().split())
answers = []
visited = [False] * (N+1)
def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, answers)))
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            answers.append(i)
            dfs(depth+1, N, M)
            visited[i] = False
            answers.pop()
dfs(0,N,M)
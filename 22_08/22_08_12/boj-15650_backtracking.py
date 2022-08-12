def dfs(depth, n, m, idx):
    if depth == m:
        print(' '.join(map(str, answers)))
    for i in range(idx, n+1):
        if not visited[i]:
            visited[i] = True
            answers.append(i)
            dfs(depth+1, n, m, i+1)
            visited[i] = False
            answers.pop()
N, M = map(int, input().split())
answers = []
visited =[False] * (N+1)
dfs(0, N, M, 1)
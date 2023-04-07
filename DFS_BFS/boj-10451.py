def dfs(value):
    visited[value] = True
    next_v = numbers[value]-1
    if not visited[next_v]:
        dfs(next_v)

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    visited = [False] * N
    answer = 0
    for i in range(N):
        if not visited[i]:
            dfs(i)
            answer+=1
    print(answer)
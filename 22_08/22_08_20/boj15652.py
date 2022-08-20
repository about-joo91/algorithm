import sys
N, M = map(int, input().split())
answer = []

def dfs(depth):
    if depth  == M:
        print(' '.join(map(str,answer)))
        return
    for i in range(1, N+1):
        if len(answer) == 0 or (answer and answer[-1] <= i):    
            answer.append(i)
            dfs(depth+1)
            answer.pop()
dfs(0)
import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j: continue
            if graph[i][j] == "Y" or (graph[i][k] =="Y" and graph[k][j] == 'Y'):
                answer[i][j] = 1

print(max(map(sum, answer)))
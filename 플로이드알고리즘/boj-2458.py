import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    tall, small = map(int, input().rstrip().split())
    graph[tall][small] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

answer = 0
for i in range(1, N+1):
    besides = 0
    for j in range(1, N+1):
        besides += (graph[i][j] + graph[j][i])
    if besides == N-1:
        answer +=1

print(answer)
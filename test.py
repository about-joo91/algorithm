import sys
sys.stdin = open('test.txt','r')

N = int(input())
INF = int(10e9)
graph = [list(input()) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j: continue
            if graph[i][j] == "Y" or (graph[i][k] =="Y" and graph[k][j] == 'Y'):
                answer[i][j] = 1

print(max(map(sum, answer)))
import sys
sys.stdin = open('', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(10e9)

costs = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    costs[i][i] = 0
        

for _ in range(M):
    start, arrive, cost = map(int, input().split())
    
    costs[start][arrive] = min(costs[start][arrive], cost )
    
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            costs[i][j] = min(costs[i][j] , costs[i][k] + costs[k][j])
            
for i in range(1, N+1):
    for j in range(1, N+1):
        if costs[i][j] == INF: print(0, end= ' ')
        else: print(costs[i][j], end=' ')
    print()
    
import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/플로이드알고리즘/test.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(10e9)

costs = [[INF] * (N+1) for _ in range(N+1)]
nexts = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    costs[i][i] = 0
        

for _ in range(M):
    start, arrive, cost = map(int, input().split())
    
    costs[start][arrive] = min(costs[start][arrive], cost )
    nexts[start][arrive] = arrive
    
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if costs[i][k] + costs[k][j] < costs[i][j]:
                costs[i][j] = costs[i][k] + costs[k][j]
                nexts[i][j] = nexts[i][k]
            
            
for i in range(1, N+1):
    for j in range(1, N+1):
        if costs[i][j] == INF: print(0, end= ' ')
        else: print(costs[i][j], end=' ')
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if costs[i][j] == 0 or costs[i][j] == INF:
            print(0)
            continue

        stack = []
        start = i
        while start != j:
            stack.append(start)
            start = nexts[start][j]
        stack.append(j)
        print(len(stack), end=' ')
        for node in stack:
            print(node, end= ' ')
        print()
    
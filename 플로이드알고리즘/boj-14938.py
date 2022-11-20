import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/플로이드알고리즘/test.txt', 'r')
N, M, R = map(int, input().split())

items = [0] + list(map(int, input().split()))

INF = int(10e9)

distances = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    distances[i][i] = 0

for _ in range(R):
    u, v, distance = map(int, input().split())
    distances[u][v] = distance
    distances[v][u] = distance

    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distances[i][j] = min(distances[i][j] , distances[i][k] + distances[k][j])



answers = []
for i in range(1, N+1):
    answer = 0
    for j in range(1, N+1):
        if distances[i][j] <= M:
            answer+= items[j]
    answers.append(answer)

print(max(answers))
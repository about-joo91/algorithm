V, E = map(int, input().split())
INF = int(10e9)
distances = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E):
    start, end, dist = map(int, input().split())
    distances[start][end] = dist

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

answer = INF
for i in range(1, V+1):
    answer = min(answer, distances[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)
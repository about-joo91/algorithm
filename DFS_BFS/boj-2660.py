import sys
N = int(input())
INF = sys.maxsize
distances = [[INF]*(N+1) for _ in range(N+1)]

while True:
    member1, member2 = map(int, input().split())
    if member1 == member2 == -1: break
    distances[member1][member2] = 1
    distances[member2][member1] = 1
    
for i in range(1, N+1):
    distances[i][i] = 0
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distances[i][j] = min(distances[i][j], distances[i][k]+distances[k][j])

result = []
for i in range(1, N+1):
    result.append(max(distances[i][1:]))

minimum = min(result)
answer = [i+1 for i, v in enumerate(result) if v == minimum]
print(minimum, len(answer))
print(*answer)
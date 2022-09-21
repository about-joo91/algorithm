N, M = map(int, input().split())

relations = [[N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    friend_1, friend_2 = map(int, input().split())
    relations[friend_1-1][friend_2-1] = 1
    relations[friend_2-1][friend_1-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: relations[i][j] = 0
            else: relations[i][j] = min(relations[i][j] , relations[i][k] + relations[k][j])

bacon = []
for row in relations:
    bacon.append(sum(row))
print(bacon.index(min(bacon)) + 1)
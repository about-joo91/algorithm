N = int(input())
stair_numbers = [[0] * 10 for _ in range(N + 1)]
MOD = 1000000000
for i in range(1, 10):
    stair_numbers[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            stair_numbers[i][j] = stair_numbers[i-1][1]
        elif j == 9:
            stair_numbers[i][j] = stair_numbers[i-1][8]
        else:
            stair_numbers[i][j] = stair_numbers[i-1][j-1] + stair_numbers[i-1][j+1]

print(sum(stair_numbers[N]) % MOD)
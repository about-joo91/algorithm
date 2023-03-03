import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N+1)]
dp[0][numbers[0]] = 1
weights = [1, -1]

for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j] == 0: continue
        for weight in weights:
            next_num = j + numbers[i] * weight
            if next_num < 0 or next_num > 20: continue
            dp[i][next_num] += dp[i-1][j]

print(dp[N-2][numbers[-1]])
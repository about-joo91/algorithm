N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = i
    for sqrt in range(1, int(i ** (1/2))+1):
        if dp[i-(sqrt * sqrt)]+1 < dp[i]:
            dp[i] = dp[i-(sqrt * sqrt)]+1

print(dp[N])
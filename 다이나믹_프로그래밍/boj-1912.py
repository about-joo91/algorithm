import sys
N = int(input())
numbers = list(map(int , input().split()))
dp = [0] * (N+1)
dp[0] = numbers[0]
answer = dp[0]
for i in range(1, N):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    answer = max(answer, dp[i])
print(answer)
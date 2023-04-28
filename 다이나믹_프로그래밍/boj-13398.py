N = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N)]
dp[0][0] = answer =  numbers[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][0] + numbers[i], numbers[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + numbers[i])
    answer = max(answer , dp[i][0], dp[i][1])

print(answer)

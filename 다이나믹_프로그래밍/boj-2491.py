N = int(input())
numbers = list(map(int, input().split()))

ascending_dp = [1] * N
descending_dp = [1] * N

for i in range(1, N):
    if numbers[i] <= numbers[i-1]:
        ascending_dp[i] = max(ascending_dp[i], ascending_dp[i-1]+1)
    if numbers[i] >= numbers[i-1]:
        descending_dp[i] = max(descending_dp[i], descending_dp[i-1]+1)

ascending_max = max(ascending_dp)
descending_max = max(descending_dp)
answer = max(ascending_max, descending_max)
print(answer)
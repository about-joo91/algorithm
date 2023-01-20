N = int(input())
numbers = list(map(int, input().split()))
r_numbers = numbers[::-1]
dp = [1] * N
r_dp = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)
        if r_numbers[i] > r_numbers[j]:
            r_dp[i] = max(r_dp[i], r_dp[j]+1)


result = [0] * N
for i in range(N):
    result[i] = dp[i] + r_dp[N-i-1] - 1

print(max(result))
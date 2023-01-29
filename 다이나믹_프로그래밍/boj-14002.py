N = int(input())
numbers = list(map(int, input().split()))
dp = [[number] for number in numbers]

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            if len(dp[i]) < len(dp[j]) +1:
                dp[i] = dp[j] + [numbers[i]]

max_len =max(map(len, dp))
print(max_len)
print(*list(filter(lambda x: len(x) == max_len, dp))[0])
N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, N+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK" if dp[N] == 0 else "CY")

# other way
# print("SK" if N % 2 == 0 else "CY")
fir_str = input()
sec_str = input()
N = len(fir_str)
M = len(sec_str)
dp = [[0] * (M+1)  for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if fir_str[i-1] == sec_str[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(max(map(max, dp)))
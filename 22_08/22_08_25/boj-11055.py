import sys
input= sys.stdin.readline
len_arr = int(input())
arr = list(map(int, input().split()))
dp = arr[:]
for i in range(1, len_arr):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0]*3 for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
print(sum(dp[N]) % 9901)

# 사자를 우리에 넣지 않을 경우
# 오른쪽에 둘 경우
# 왼쪽에 둘 경우를 계산해서 결과도출
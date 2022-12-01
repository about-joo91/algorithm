import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/다이나믹_프로그래밍/15486.txt','r')

N = int(input())

schedules = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + schedules[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+ schedules[i][0]] + schedules[i][1])
        
print(dp[0])
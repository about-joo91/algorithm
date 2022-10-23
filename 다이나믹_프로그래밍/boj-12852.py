N = int(input())

path = [0] * (N+1)
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    path[i] = i-1
    
    if i % 2 == 0 and dp[i] > dp[i//2] +1:
        dp[i] = dp[i//2] +1
        path[i] = i//2
        
    if i % 3 == 0 and dp[i] > dp[i//3] +1:
        dp[i] = dp[i//3] +1
        path[i] = i//3
print(dp[N])
cur_num = N
while True:
    print(cur_num, end = " ")
    if cur_num == 1:
        break
    cur_num = path[cur_num]
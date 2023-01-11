import sys
# N, K = map(int, input().split())

N, K = 15,12

dp = [True] * (N+1)
cnt = 0

for i in range(2, N+1):
    if dp[i]:
        cnt+=1
        if cnt == K:
            print(i)
            sys.exit(0)
        for j in range(i+i, N+1, i):
            if dp[j]:
                cnt+=1
                if cnt == K:
                    print(j)
                    sys.exit(0)
            dp[j] = False
            
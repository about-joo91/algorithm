import sys
input = sys.stdin.readline
iter_num = int(input())
for _ in range(iter_num):
    cur_num = int(input())
    dp = [[ ] for _ in range(cur_num+1)]
    def fibo(n):
        if n == 0:
            return [1, 0]
        elif n == 1:
            return [0, 1]
        elif dp[n] != []:
            return dp[n]
        dp[n] = [fibo(n-1)[0] + fibo(n-2)[0], fibo(n-1)[1] + fibo(n-2)[1]]
        return dp[n]
    print(*fibo(cur_num))
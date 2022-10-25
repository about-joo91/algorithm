from collections import defaultdict
N, P, Q = map(int, input().split())

dp = defaultdict(int)

dp[0] = 1

def get_value(N, P, Q):
    if dp[N] != 0:
        return dp[N]
    dp[N] = get_value(N//P, P, Q) + get_value(N//Q, P, Q)
    return dp[N]
    

print(get_value(N, P, Q))
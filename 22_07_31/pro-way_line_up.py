def solution(n, k):
    dp = [0]* (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] * i
    rows = list(range(1,n+1))
    answer = []
    while n != 0:
        idx = (k-1) // dp[n-1]
        k = k % dp[n-1]
        answer.append(rows.pop(idx))
        n-=1
    return answer
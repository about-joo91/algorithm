def get_number_of_cases():
    dp =[0]* (N+1)

    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    idx_diff= 0
    answer = 1
    for vip_sheat in vip_sheats:
        answer *= dp[vip_sheat - 1 - idx_diff]
        idx_diff = vip_sheat

    answer *= dp[N - idx_diff]

    return answer

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    vip_sheats =[int(input()) for _ in range(M)]

    print(get_number_of_cases())
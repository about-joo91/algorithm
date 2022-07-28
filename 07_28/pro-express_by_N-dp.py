def solution(N, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        cur_dp = set()
        cur_dp.add(int(str(N) *i))
        for j in range(0,i-1):
            for dp_val1 in dp[j]:
                for dp_val2 in dp[-j-1]:
                    cur_dp.add(dp_val1 + dp_val2)
                    cur_dp.add(dp_val1 - dp_val2)
                    cur_dp.add(dp_val1 * dp_val2)
                    if dp_val2 != 0:
                        cur_dp.add(dp_val1 // dp_val2)
        if number in cur_dp:
            return i
        dp.append(cur_dp)
    return answer

print(solution(5, 12))
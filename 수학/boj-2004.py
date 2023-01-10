N, M = map(int, input().split())

def get_two_cnt_and_five_cnt(n):
    two_cnt = 0
    five_cnt = 0

    i = 2
    while i <= n:
        two_cnt += n//i
        i *= 2
    i = 5
    while i <= n:
        five_cnt += n//i
        i *= 5

    return two_cnt, five_cnt

N_two_cnt, N_five_cnt = get_two_cnt_and_five_cnt(N)
M_two_cnt, M_five_cnt = get_two_cnt_and_five_cnt(M)
N_minus_M_two_cnt, N_minus_M_five_cnt = get_two_cnt_and_five_cnt(N-M)

total_two_cnt = N_two_cnt - (M_two_cnt + N_minus_M_two_cnt)
total_five_cnt = N_five_cnt - (M_five_cnt + N_minus_M_five_cnt)

print(min(total_two_cnt, total_five_cnt))
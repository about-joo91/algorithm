import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
electric_wires = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
extracted_numbers_right_side = list(map(lambda x: x[1], electric_wires))
dp = [extracted_numbers_right_side[0]]

for i in range(1, N):
    if dp[-1] < extracted_numbers_right_side[i]:
        dp.append(extracted_numbers_right_side[i])
    else:
        cur_idx = bisect_left(dp,extracted_numbers_right_side[i])
        dp[cur_idx] = extracted_numbers_right_side[i]

print(N - len(dp))
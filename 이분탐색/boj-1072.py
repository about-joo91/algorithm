import sys
import math
input = sys.stdin.readline

X, Y = map(int, input().split())
cur_win_rate = math.floor(100 * Y / X)
limit = int(10e8)

left = 0
right = limit

while left <= right:
    mid = (left + right) // 2
    if math.floor(((Y + mid) / (X + mid)) * 100) > cur_win_rate:
        right = mid-1
    else:
        left = mid+1

if cur_win_rate >= 99:
    print(-1)
else: print(right+1)
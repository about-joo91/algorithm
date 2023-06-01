import sys
from bisect import bisect_left
input = sys.stdin.readline

N, H = map(int, input().rstrip().split())

up = []
down = []
for i in range(N):
	cur_height = int(input().rstrip())
	if i % 2 == 0:
		down.append(cur_height)
		continue
	up.append(cur_height)

down.sort()
up.sort()
min_val = sys.maxsize
count = 0
for i in range(1, H+1):
	up_count = N//2 - bisect_left(down,i)
	do_count = N//2 - bisect_left(up, H-i+1)
	cur_val = up_count + do_count
	if min_val > cur_val:
		min_val = cur_val
		count = 1
	elif min_val == cur_val:
		count+=1

print(min_val, count)

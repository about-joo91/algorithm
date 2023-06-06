import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
	n, m = map(int, input().rstrip().split())
	count = 0
	a_fish_sizes = sorted(list(map(int, input().rstrip().split())))
	b_fish_sizes = sorted(list(map(int, input().rstrip().split())))
	for cur_size in a_fish_sizes:
		count += bisect_left(b_fish_sizes, cur_size)
	print(count)

import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().rstrip().split())
diffs = list(map(int, input().rstrip().split()))
answer = 0
def backtracking(cur_s, min_s, max_s, idx):
	global answer
	if cur_s > R: return
	if L<= cur_s and max_s - min_s >= X:
		answer += 1
	for i in range(idx+1, N):
		backtracking(cur_s + diffs[i], min(min_s, diffs[i]), max(max_s, diffs[i]), i)

backtracking(0, sys.maxsize, 0, -1)
print(answer)

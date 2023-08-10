import sys
input = sys.stdin.readline

def check_broken():
	count = 0
	for egg in eggs:
		if egg[S] <= 0:
			count += 1
	return count


def backtracking(cur_idx):
	global answer

	if cur_idx == N:
		answer = max(answer, check_broken())
		return

	if eggs[cur_idx][S] <= 0:
		backtracking(cur_idx + 1)
		return

	is_all_broken = True
	for i in range(N):
		if i == cur_idx: continue
		if eggs[i][S] > 0:
			is_all_broken = False
			break
	if is_all_broken:
		answer = max(answer, N - 1)
		return

	for i in range(N):
		if i != cur_idx and eggs[i][S] > 0:
			eggs[cur_idx][S] -= eggs[i][W]
			eggs[i][S] -= eggs[cur_idx][W]
			backtracking(cur_idx + 1)
			eggs[cur_idx][S] += eggs[i][W]
			eggs[i][S] += eggs[cur_idx][W]


N = int(input().rstrip())
S, W = 0, 1
eggs = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = 0
backtracking(0)
print(answer)

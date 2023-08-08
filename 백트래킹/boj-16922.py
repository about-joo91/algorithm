import sys

sys.setrecursionlimit(int(10e6))
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [1, 5, 10, 50]
answer = set()


def backtracking(cur_idx, depth, cur_number):
	global answer
	if depth == N:
		answer.add(cur_number)
		return
	for i in range(cur_idx, len(numbers)):
		backtracking(i, depth + 1, cur_number + numbers[i])


backtracking(0, 0, 0)
print(len(answer))

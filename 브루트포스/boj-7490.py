def backtracking(depth, cur_op, idx):
	if depth == LIMIT:
		if calculate(cur_op) == 0:
			answer.append(cur_op)
		return
	for i in range(idx, LIMIT + 1):
		for op in operator:
			next_op = cur_op + op + str(i)
			backtracking(depth + 1, next_op, i + 1)


def calculate(cur_op):
	return eval(cur_op.replace(' ', ''))


T = int(input())
operator = [' ', '+', '-']
while T:
	LIMIT = int(input())
	answer = []
	backtracking(1, "1", 2)
	print("\n".join(answer))
	T -= 1
	if T != 0: print()

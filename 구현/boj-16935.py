import sys
import copy

input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
operators = list(map(int, input().rstrip().split()))

def operate_one():
	for i in range(len(graph)//2):
			graph[i], graph[len(graph)-i-1] = graph[len(graph)-i-1], graph[i]

def operate_two():
	for row_idx in range(len(graph)):
		graph[row_idx] = graph[row_idx][::-1]

def operate_three():
	global graph
	row_len = len(graph)
	col_len = len(graph[0])
	tmp = [[0] * row_len for _ in range(col_len)]
	for i in range(row_len):
		for j in range(col_len):
			tmp[j][row_len -i-1]  = graph[i][j]
	graph = tmp

def operate_four():
	global graph
	row_len = len(graph)
	col_len = len(graph[0])
	tmp = [[0] * row_len for _ in range(col_len)]
	for i in range(row_len):
		for j in range(col_len):
			tmp[col_len-j-1][i]  = graph[i][j]
	graph = tmp

def position_number(row, col):
	row_len = len(graph)
	col_len = len(graph[0])
	if (row < row_len//2 and col < col_len//2):
		return 1
	elif (row < row_len//2 and col >= col_len//2):
		return 2
	elif (row >= row_len//2 and col >= col_len//2):
		return 3
	else:
		return 4

def operate_five():
	tmp = copy.deepcopy(graph)
	row_len = len(graph)
	col_len = len(graph[0])
	for i in range(row_len):
		for j in range(col_len):
			row_weight = row_len // 2
			col_weight = col_len // 2
			match position_number(i, j):
				case 1:
					graph[i][j + col_weight] = tmp[i][j]
				case 2:
					graph[i+ row_weight][j] = tmp[i][j]
				case 3:
					graph[i][j-col_weight] = tmp[i][j]
				case 4:
					graph[i-row_weight][j] = tmp[i][j]

def operate_six():
	tmp = copy.deepcopy(graph)
	row_len = len(graph)
	col_len = len(graph[0])
	for i in range(row_len):
		for j in range(col_len):
			row_weight = row_len // 2
			col_weight = col_len // 2
			match position_number(i, j):
				case 1:
					graph[i+ row_weight][j] = tmp[i][j]
				case 2:
					graph[i][j - col_weight] = tmp[i][j]
				case 3:
					graph[i - row_weight][j] = tmp[i][j]
				case 4:
					graph[i][j + col_weight] = tmp[i][j]

def operator(op):
	match op:
		case 1:
			operate_one()
		case 2:
			operate_two()
		case 3:
			operate_three()
		case 4:
			operate_four()
		case 5:
			operate_five()
		case 6:
			operate_six()
		

for idx in range(R):
	operator(operators[idx])
	

for row in graph:
	print(*row)

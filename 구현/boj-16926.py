import sys
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

for _ in range(R):
	for i in range(min(N, M) // 2):
		fir_value = arr[i][i]

		for j in range(i + 1, M - i):
			arr[i][j-1] = arr[i][j]
		cur_col = j
			
		for j in range(i + 1, N - i):
			arr[j-1][cur_col] = arr[j][cur_col]
		cur_row = j

		for j in range(M-i-1, i, -1):
			arr[cur_row][j] = arr[cur_row][j-1]
		cur_col = i
		
		for j in range(N-i-1, i, -1):
			arr[j][cur_col] = arr[j-1][cur_col]
		arr[i+1][i] = fir_value

for i in range(N):
	print(*arr[i])

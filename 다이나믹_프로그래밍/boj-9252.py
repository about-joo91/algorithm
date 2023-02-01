import sys
input = sys.stdin.readline

fir_str = " " + input().rstrip()
sec_str = " " + input().rstrip()
N = len(fir_str)
M = len(sec_str)

lcs = [[0] * M for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if fir_str[i] == sec_str[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[N-1][M-1])

answer = []
row = N-1
col = M-1

while row > 0 and col > 0:
    if lcs[row][col-1] == lcs[row][col]:
        col -=1
    elif lcs[row-1][col] == lcs[row][col]:
        row -=1
    else:
        answer.append(fir_str[row])
        row-=1
        col-=1

print("".join(answer[::-1]))
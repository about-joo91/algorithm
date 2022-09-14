import sys

input = sys.stdin.readline
N, M = map(int, input().split())
chess_map = []
for _ in range(N):
    chess_map.append(list(input()))

cnt = sys.maxsize

for i in range(N - 7):
    for j in range(M - 7):
        W_first = 0
        B_first = 0
        for row in range(i, i+8):
            for col in range(j , j+8):
                if (row + col) % 2 == 0:
                    if chess_map[row][col] != "W":
                        W_first += 1
                    if chess_map[row][col] != "B":
                        B_first+=1
                else:
                    if chess_map[row][col] != "W":
                        B_first+=1
                    if chess_map[row][col] != "B":
                        W_first += 1
        cnt = min(cnt, W_first, B_first)
print(cnt)
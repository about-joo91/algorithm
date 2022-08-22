import sys
input = sys.stdin.readline
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(3):
        colors[i][j] += min(colors[i-1][:j] + colors[i-1][j+1:])

print(min(colors[N-1]))
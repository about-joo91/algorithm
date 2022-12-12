import sys
input = sys.stdin.readline

N, L = map(int, input().split())

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
maps = [list(map(int, input().split())) for _ in range(N)]

def get_cur_line_can_be_path(cur_line):
    idx = 0
    cnt = 1
    while idx < N-1:
        if abs(cur_line[idx+1] - cur_line[idx]) > 1: return 0
        if cur_line[idx] == cur_line[idx+1]:
            cnt+=1
            idx+=1
        elif cur_line[idx] < cur_line[idx+1]:
            if cnt < L: return 0
            cnt = 1
            idx+=1
        else:
            if idx + L >= N: return 0
            for i in range(idx+1, idx+L):
                if cur_line[i] != cur_line[i+1]: return 0
            idx = idx+L
            cnt = 0
    return 1

answer = 0
for i in range(N):
    cur_line = []
    for j in range(N):
        cur_line.append(maps[i][j])
    answer+= get_cur_line_can_be_path(cur_line=cur_line)

for i in range(N):
    cur_line = []
    for j in range(N):
        cur_line.append(maps[j][i])
    answer += get_cur_line_can_be_path(cur_line=cur_line)


print(answer)
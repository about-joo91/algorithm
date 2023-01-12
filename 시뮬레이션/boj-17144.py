import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = []
for _ in range(R):
    room.append(list(map(int, input().split())))

directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

air_purifier = []

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air_purifier.append(i)

def add_weight_to_spreads(n, r, c, spreads):
    cnt = 0
    for direction in directions:
        next_r = r + direction[0]
        next_c = c + direction[1]

        if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C: continue
        if room[next_r][next_c] == -1: continue

        cnt+=1
        spreads[next_r][next_c] += n

    spreads[r][c] -= (n * cnt)


def clear_upper_area():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    direct = 0
    before = 0
    r, c = air_purifier[0], 1
    while True:
        nr = r + dr[direct]
        nc = c + dc[direct]
        if r == air_purifier[0] and c == 0:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            direct += 1
            continue
        room[r][c], before = before, room[r][c]
        r = nr
        c = nc


def clear_down_area():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direct = 0
    before = 0
    r, c = air_purifier[1], 1
    while True:
        nr = r + dr[direct]
        nc = c + dc[direct]
        if r == air_purifier[1] and c == 0:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            direct += 1
            continue
        room[r][c], before = before, room[r][c]
        r = nr
        c = nc

while T:
    spreads = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                add_weight_to_spreads(room[i][j] // 5, i, j, spreads)

    for i in range(R):
        for j in range(C):
            room[i][j] += spreads[i][j]

    clear_upper_area()
    clear_down_area()
    T-=1

print(sum(map(sum, room)) + 2)
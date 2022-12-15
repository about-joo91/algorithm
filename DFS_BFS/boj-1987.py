import sys
input= sys.stdin.readline

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

queue = set([(0, 0, maps[0][0])])

answer = 0

while queue:
    cur_row, cur_col, _set = queue.pop()

    answer = max(answer, len(_set))

    for direction in directions:
        next_row = cur_row + direction[0]
        next_col = cur_col + direction[1]

        if 0 > next_row or next_row >= R or 0 > next_col or next_col >=C: continue
        if maps[next_row][next_col] in _set: continue

        queue.add((next_row, next_col, maps[next_row][next_col] + _set))


print(answer)
    
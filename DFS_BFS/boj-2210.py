def dfs(r, c, cur_number):
    if len(cur_number) == 6:
        answer.add(cur_number)
        return
    
    for direction in directions:
        next_r = r + direction[0]
        next_c = c + direction[1]
        if next_r < 0 or next_r > 4 or next_c < 0 or next_c > 4: continue
        dfs(next_r, next_c, cur_number+board[next_r][next_c])


board = [input().split() for _ in range(5)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(answer))
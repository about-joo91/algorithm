import sys
input = sys.stdin.readline

N = 7
target = 1
board = [[0]*N for _ in range(N)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
r = c = N //2
length = 0
cur_num = 1
board[r][c] = cur_num
answer = [r+1, c+1]


while True:    
    for direction in directions:
      for _ in range(length):
        r += direction[0]
        c += direction[1]
        cur_num+=1
        board[r][c] = cur_num
        if cur_num == target:
            answer = [r+1, c+1]
    if r == c == 0:
       break
    r -=1
    c -=1
    length+=2


for row in board:
    print(*row)         
print(*answer)
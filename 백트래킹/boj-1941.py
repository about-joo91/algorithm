import sys

sys.stdin = open('', 'r')

answer = 0
class_room = []
for _ in range(5):
    class_room += list(input())
check = [[0] * 5 for _ in range(5)]
directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
visit = [0 for _ in range(25)]

members = []
def backtracking(depth, members, position):
    global answer, check
    if depth == 7:
        if members.count("S") >=4:
            position_check(position[0], position)
            if sum(sum(check, [])) == 7:
                answer +=1
            check = [[0] * 5 for _ in range(5)]
        return
    
    for i in range(25):
        if visit[i] == 0:
            visit[i] = 1
            backtracking(depth+1, members+class_room[i], position+[i])
            for j in range(i+1, 25):
                visit[j]= 0

def position_check(s, position):
    row = s // 5
    col = s % 5
    check[row][col] = 1
    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if 0 <= next_row < 5 and 0 <= next_col < 5:
            next_idx = next_row * 5 + next_col
            if check[next_row][next_col] == 0 and next_idx in position:
                check[next_row][next_col] = 1
                position_check(next_idx, position)


backtracking(0,'',[])
print(answer)
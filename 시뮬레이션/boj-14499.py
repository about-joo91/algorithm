from collections import deque
import sys
sys.stdin = open('', 'r')

vertical_dice = deque([0] * 4)
horizontal_dice = [0] * 3


directions = [[0], [0, 1], [0, -1], [-1, 0], [1, 0]]
N, M, row, column, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

def move_dice(direction_num):
    if direction_num == 1:
        move_to_east()
    elif direction_num == 2:
        move_to_west()
    elif direction_num == 3:
        move_to_north()
    else:
        move_to_south()

def move_to_north():
    vertical_dice.rotate(-1)
    horizontal_dice[1] = vertical_dice[1]
    
def move_to_south():
    vertical_dice.rotate(1)
    horizontal_dice[1] = vertical_dice[1]
    
def move_to_east():
    horizontal_dice[1], horizontal_dice[0] = horizontal_dice[0], horizontal_dice[1]
    horizontal_dice[0], vertical_dice[3] = vertical_dice[3], horizontal_dice[0]
    vertical_dice[3], horizontal_dice[2] = horizontal_dice[2], vertical_dice[3]
    vertical_dice[1] = horizontal_dice[1]
    
    
def move_to_west():
    horizontal_dice[1], horizontal_dice[2] = horizontal_dice[2], horizontal_dice[1]
    horizontal_dice[2], vertical_dice[3] = vertical_dice[3], horizontal_dice[2]
    vertical_dice[3], horizontal_dice[0] = horizontal_dice[0], vertical_dice[3]
    vertical_dice[1] = horizontal_dice[1]
        
move_queue = deque(list(map(int, input().split())))

while move_queue:
    direction_num = move_queue.popleft()
    direction = directions[direction_num]
    
    next_row = row + direction[0]
    next_col = column + direction[1]
    
    if 0 <= next_row < N and 0 <= next_col < M:
        move_dice(direction_num)
        row = next_row
        column = next_col
        if maps[row][column] == 0:
            maps[row][column] = vertical_dice[3]
        else:
            vertical_dice[3] = maps[row][column]
            maps[row][column] = 0
        print(horizontal_dice[1])
    else: continue
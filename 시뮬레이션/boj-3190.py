from collections import deque
import sys
input = sys.stdin.readline

def change_location(cur_row:int, cur_col:int) -> None:
    if maps[cur_row][cur_col] == 0:
        path.append((cur_row, cur_col))
        maps[cur_row][cur_col] = "s"
        last_row, last_col = path.popleft()
        maps[last_row][last_col] = 0

    elif maps[cur_row][cur_col] == 1:
        maps[cur_row][cur_col] = "s"
        path.append((cur_row, cur_col))

def rotate_direction(cur_direction:int , command:str):
    if command == "D":
        cur_direction = cur_direction +1 if cur_direction + 1 < 4 else 0
    else: cur_direction = cur_direction - 1 if cur_direction - 1 >= 0 else 3
    return cur_direction



def is_wall(cur_row:int, cur_col:int) -> bool:
    return 0 > cur_row or cur_row >= N or 0 > cur_col or cur_col >= N

def is_snake_body(cur_row:int, cur_col:int) -> bool:
    return maps[cur_row][cur_col] == "s"
    

def get_end_time(cur_direction:int, time:int, cur_row:int, cur_col:int) -> int:
    
    maps[cur_row][cur_col] = "s"
    path.append((cur_row,cur_col))

    change_timing, command = commands.popleft()
        
    while True:
        cur_row += directions[cur_direction][0]
        cur_col += directions[cur_direction][1]

        if is_wall(cur_row, cur_col):
            return time + 1

        if is_snake_body(cur_row, cur_col):
            return time + 1

        change_location(cur_row ,cur_col)
        time+=1

        if change_timing == time:

            cur_direction = rotate_direction(cur_direction, command)

            if commands:
                next_timing, command = commands.popleft()
                change_timing = next_timing

if __name__ == "__main__":
    N = int(input())
    maps = [[0] * N for _ in range(N)]
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    path = deque()

    apple_cnt = int(input())
    for _ in range(apple_cnt):
        row, col = map(int, input().split())
        maps[row-1][col-1] = 1

    command_cnt = int(input())
    commands = deque()
    for _ in range(command_cnt):
        second, command = input().split()
        second = int(second)
        commands.append((second, command))

    print(get_end_time(cur_direction=2, cur_row=0, cur_col=0, time=0))
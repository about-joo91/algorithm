from collections import deque
from itertools import permutations
import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/시뮬레이션/test.txt','r')



def get_fastest_way() -> None:
    global answer

    distances = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    distances[0][0][0] = 0
    queue = deque()
    queue.append((0, 0, 0))

    
    while queue:
        cur_height, cur_row, cur_col = queue.popleft()
        if cur_height == cur_row == cur_col == 4:
            if distances[cur_height][cur_row][cur_col] < answer:
                answer = distances[cur_height][cur_row][cur_col]
            return 
        
        for direction in directions:
            next_height = cur_height + direction[0]
            next_row = cur_row + direction[1]
            next_col = cur_col + direction[2]
            
            if 0 <= next_height < 5 and 0 <= next_row < 5 and 0 <= next_col < 5:
                if distances[next_height][next_row][next_col] == -1 and rotated_maze[next_height][next_row][next_col] == 1:
                    distances[next_height][next_row][next_col] = distances[cur_height][cur_row][cur_col]+1
                    queue.append((next_height, next_row, next_col))

def rotate_board(height:int) -> None:
    tmp = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            tmp[j][4-i] = rotated_maze[height][i][j]

    rotated_maze[height] = tmp

def find_fastest_way_from_rotated_maze(depth:int) -> None:
    
    if depth == 5:
        if rotated_maze[4][4][4]:
            get_fastest_way()
        return
    
    for _ in range(4):
        if rotated_maze[0][0][0]:
            find_fastest_way_from_rotated_maze(depth+1)
        rotate_board(depth)


def make_cur_maze() -> None:
    global rotated_maze
    for numbers in permutations(list(range(5))):
        rotated_maze = [maze[number] for number in numbers]
        find_fastest_way_from_rotated_maze(0)


if __name__ == "__main__":

    maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
    rotated_maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    answer = sys.maxsize

    make_cur_maze()

    if answer == sys.maxsize:
        print(-1)
    else: print(answer)
from collections import deque
import sys
input = sys.stdin.readline



def get_moving_time(start:list[int], end:list[int]) -> int:
    queue = deque()
    queue.append(start+[0])
    visited[start[0]][start[1]] = 1
    
    while queue:
        cur_node = queue.popleft()
        
        if cur_node[:2] == end: return cur_node[2]
        
        cur_row, cur_col, cnt = cur_node[0], cur_node[1], cur_node[2]
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if 0 <= next_row < N and 0<= next_col < N and not visited[next_row][next_col]:
                visited[next_row][next_col] = 1
                queue.append([next_row, next_col, cnt + 1])
                

if __name__ == "__main__":                
    T = int(input())
    directions = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]] 
    for _ in range(T):
        N = int(input())
        start = list(map(int, input().split()))
        end = list(map(int , input().split()))
        visited = [[0] * N for _ in range(N)]

        print(get_moving_time(start = start, end = end))
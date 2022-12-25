from collections import deque
import sys

input = sys.stdin.readline

def is_land(row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    
    while queue:
        cur_row, cur_col = queue.popleft()
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if next_row < 0 or next_row >= H or next_col < 0 or next_col >= W: continue
            if visited[next_row][next_col]: continue
            if maps[next_row][next_col] == 0: continue
                
            visited[next_row][next_col] = True
            queue.append((next_row, next_col))
            
    return True


if __name__ == "__main__":
    while True:
        W, H = map(int, input().split())
        
        if W == H == 0:
            break

        maps = [list(map(int, input().split())) for _ in range(H)]
        visited = [[False] * W for _ in range(H)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        cnt = 0
        
        for i in range(H):
            for j in range(W):
                if not visited[i][j] and maps[i][j] == 1 and is_land(i, j):
                    cnt+=1
        print(cnt)
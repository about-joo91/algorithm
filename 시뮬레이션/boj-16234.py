import sys
from collections import deque

def get_union_candidates(r,c):
    queue = deque()
    queue.append((r,c))
    visited[r][c] = True
    candidates = []
    while queue:
        cur_row, cur_col = queue.popleft()
        candidates.append((cur_row, cur_col))
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N: continue
            if visited[next_row][next_col]: continue
            if L <= abs(maps[cur_row][cur_col] - maps[next_row][next_col]) <= R:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col))

    return candidates


def display_new_population(candidates):
    new_population = sum(maps[r][c] for r, c in candidates) // len(candidates)
    for r, c in candidates:
        maps[r][c] = new_population


if __name__ == "__main__":
    input = sys.stdin.readline

    N, L, R = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cnt = 0
    
    while True:
        visited = [[False] * N for _ in range(N)]
        exists_candidate = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    candidates = get_union_candidates(i,j)
                    if len(candidates) > 1:
                        exists_candidate = True
                        display_new_population(candidates)
        
        if not exists_candidate: break
        cnt+=1

    print(cnt)
import sys
from collections import deque
input = sys.stdin.readline

def adjacent_soldier_count(t_soldier, start_row, start_col):
	queue = deque()
	queue.append((start_row, start_col))
	visited[start_row][start_col] = True
	cnt = 1
	while queue:
		cur_row, cur_col = queue.popleft()
		for direction in directions:
			next_row = cur_row + direction[0]
			next_col = cur_col + direction[1]
			if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M: continue
			if visited[next_row][next_col]: continue
			if graph[next_row][next_col] != t_soldier: continue
			visited[next_row][next_col] = True
			queue.append((next_row, next_col))
			cnt+=1
	return cnt

def calculate_power_of_mine_and_enemy():
	my_power = 0
	enemy_power = 0
	for i in range(N):
		for j in range(M):
			if graph[i][j] == "B" and not visited[i][j]:
				enemy_count = adjacent_soldier_count("B", i, j)
				enemy_power += enemy_count **2
			elif graph[i][j] == "W" and not visited[i][j]:
				my_count = adjacent_soldier_count("W", i, j)
				my_power += my_count ** 2
	return (my_power, enemy_power)

if __name__ == '__main__':
    M, N = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    my_power, enemy_power = calculate_power_of_mine_and_enemy()
    print(my_power, enemy_power)

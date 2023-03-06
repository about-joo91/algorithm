from collections import deque

def get_minimum_time(start):
    queue = deque()
    queue.append((start, 0, 0))
    visited[start][0] = True

    while queue:
        cur_number, cur_time, clip_board = queue.popleft()
        clip_board_added = cur_number + clip_board

        if cur_number == S:
            return cur_time
        
        if clip_board_added <= 1000 and not visited[clip_board_added][clip_board]:
            visited[clip_board_added][clip_board] = True
            queue.append((clip_board_added, cur_time+1, clip_board))
        
        if cur_number > 0 and not visited[cur_number-1][clip_board]:
            visited[cur_number-1][clip_board] = True
            queue.append((cur_number-1, cur_time+1, clip_board))

        if not visited[cur_number][cur_number]:
            queue.append((cur_number, cur_time+1, cur_number))
        
    return -1


if __name__ == "__main__":
    S = int(input())
    visited = [[False] * 1001 for _ in range(1001)]
    print(get_minimum_time(1))
import sys
input = sys.stdin.readline

N = int(input().rstrip())
friends_data = [list(map(int, input().rstrip().split())) for _ in range(N**2)]
class_room = [[0] * N for _ in range(N)]
directions = [[0, 1], [1, 0],[-1, 0], [0, -1]]

def count_adjacent_data_by_cond(r, c, favorite_stu = []):
    is_cond_favorite = False
    if favorite_stu:
        is_cond_favorite = True
    
    count = 0
    for direction in directions:
        next_r = r + direction[0]
        next_c = c + direction[1]
        
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N: continue

        if is_cond_favorite and class_room[next_r][next_c] in favorite_stu:
            count+=1
        elif not is_cond_favorite and class_room[next_r][next_c] == 0:
            count+=1

    return count


for friend_data in friends_data:
    cur_friend = friend_data[0]
    cur_favorite_stu = friend_data[1:]

    max_adjacent_favorite_stu = 0
    location_candidates = []

    for i in range(N):
        for j in range(N):
            if class_room[i][j] != 0: continue
            favorite_stu_count = count_adjacent_data_by_cond(i, j, cur_favorite_stu)

            if favorite_stu_count > max_adjacent_favorite_stu:
                max_adjacent_favorite_stu = favorite_stu_count
                location_candidates = [(i, j)]
            elif favorite_stu_count == max_adjacent_favorite_stu:
                location_candidates.append((i, j))
    
    max_adjacent_empty_loc = -1
    last_row = last_col = 0
    for cand_row, cand_col in location_candidates:
        empty_loc_count = count_adjacent_data_by_cond(cand_row, cand_col)
        if empty_loc_count > max_adjacent_empty_loc:
            max_adjacent_empty_loc = empty_loc_count
            last_row, last_col = cand_row, cand_col
    
    class_room[last_row][last_col] = cur_friend

answer = 0
friends_data.sort()
for i in range(N):
    for j in range(N):
        cur_friend = class_room[i][j]
        cur_favorite_stu = friends_data[cur_friend-1][1:]
        favorite_stu_count = count_adjacent_data_by_cond(i, j, cur_favorite_stu)
        answer += 0 if favorite_stu_count == 0 else 10 ** (favorite_stu_count-1)

print(answer)

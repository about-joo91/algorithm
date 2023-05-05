def is_over_board(next_row, next_col):
    return next_row < 0 or next_row >= 8 or next_col < 0 or next_col >= 8

def get_cur_direction(moving):
    row_d = 0
    col_d = 0
    for char in moving:
        direction = king_moving_map[char]
        row_d += direction[0]
        col_d += direction[1]
    
    return (row_d, col_d)

def location_to_column_formatter(location):
    return [8 - int(location[1]), ord(location[0]) - ord('A')]

def column_to_location_formatter(column):
    return chr(column[1] + ord('A')) + str(8 - column[0])

if __name__ == "__main__":
    king_moving_map = {
        "R": [0, 1],
        "L": [0, -1],
        "B": [1, 0],
        "T": [-1, 0]
    }

    king, rock, N = input().split()
    N = int(N)
    king = location_to_column_formatter(king)
    rock = location_to_column_formatter(rock)

    for _ in range(N):
        moving = input()
        row_d, col_d = get_cur_direction(moving)
        next_king = [king[0] + row_d, king[1] + col_d]
        if is_over_board(*next_king): continue
        if next_king == rock:
            next_rock = [rock[0] + row_d, rock[1] + col_d]
            if is_over_board(*next_rock): continue
            rock = next_rock
        king = next_king
        

    print(column_to_location_formatter(king))
    print(column_to_location_formatter(rock))
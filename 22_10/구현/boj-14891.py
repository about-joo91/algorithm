from collections import deque
gears = [deque(map(int,input())) for _ in range(4)]

RIGHT = 2
LEFT = 6

circle_cnt = int(input())

# 지금으로부터 오른쪽 톱니바퀴들이 돌아갈지 여부를 확인하고 돌려준다.
def rotate_right(cur_num, rotate_dir):
    # 오른쪽을 확인할 때 마지막 인덱스 3이 톱니바퀴의 끝이고
    # 값이 같다면 회전하지 않으므로 지금 값의 오른쪽 값을 확인할 필요가 없다.
    if cur_num > 2 or gears[cur_num][RIGHT] == gears[cur_num+1][LEFT]:
        return
    
    if gears[cur_num][RIGHT] != gears[cur_num+1][LEFT]:
        rotate_right(cur_num+1, -rotate_dir)
        gears[cur_num+1].rotate(rotate_dir)
        
def rotate_left(cur_num, rotate_dir):
    # 오른쪽 확인과 마찬가지이다.
    if cur_num < 1 or gears[cur_num][6] == gears[cur_num-1][RIGHT]:
        return
    
    if gears[cur_num][LEFT] != gears[cur_num-1][RIGHT]:
        rotate_left(cur_num-1, -rotate_dir)
        gears[cur_num-1].rotate(rotate_dir)

for _ in range(circle_cnt):
    gear_number, rotate_direction = map(int, input().split())
    # 리스트의 인덱스 값과 일치하지 않기 때문에 
    gear_number-=1
    
    rotate_right(gear_number, -rotate_direction)
    rotate_left(gear_number,-rotate_direction)
    
    gears[gear_number].rotate(rotate_direction)
    
answer = 0
for i in range(len(gears)):
    answer+= (2 ** i) *gears[i][0]
print(answer)
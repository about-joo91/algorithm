N = int(input())

balls = input()

# 왼쪽으로 밀어넣은 값과 오른쪽으로 밀어넣은 값을 각각 비교하여 최소값을 프린트한다.

red_cnt = min(balls.rstrip("R").count("R"), balls.lstrip("R").count("R"))

blue_cnt = min(balls.rstrip("B").count("B"), balls.lstrip("B").count("B"))

print(min(red_cnt, blue_cnt))
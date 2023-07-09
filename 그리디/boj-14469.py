N = int(input())
arrival_info = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))

cur_time = 0
for arrival, duration in arrival_info:
    if cur_time < arrival:
        cur_time = arrival + duration
    else:
        cur_time += duration

print(cur_time)
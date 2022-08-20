import sys
from itertools import combinations
iter_num = int(sys.stdin.readline())
soccer_stats = [list(map(int, sys.stdin.readline().split())) for _ in range(iter_num)]
combs = list(combinations(list(range(iter_num)), iter_num//2))
left = 0
right = len(combs)-1
min_diff = 101
while left <= right:
    start_team = 0
    cur_start = combs[left]
    for check_stat in list(combinations(cur_start,2)):
        start_team += (soccer_stats[check_stat[0]][check_stat[1]] + soccer_stats[check_stat[1]][check_stat[0]])
    
    
    link_team = 0
    cur_link = combs[right]
    for check_stat in list(combinations(cur_link,2)):
        link_team += (soccer_stats[check_stat[0]][check_stat[1]] + soccer_stats[check_stat[1]][check_stat[0]])
    
    min_diff = min(min_diff, abs(link_team - start_team))
    left += 1
    right -=1
print(min_diff)
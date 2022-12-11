import sys
from itertools import combinations
input = sys.stdin.readline

N =  int(input())

stats = [list(map(int, input().split())) for _ in range(N)]
possible_team = list(combinations(range(N), N//2))

answer = sys.maxsize
left = 0
right = len(possible_team)-1

while left <= right:
    start_team = possible_team[left]
    start_team_stat = 0
    for fir_person, sec_person in list(combinations(start_team, 2)):
        start_team_stat += (stats[fir_person][sec_person] + stats[sec_person][fir_person])

    
    link_team = possible_team[right]
    link_team_stat = 0
    for fir_person, sec_person in list(combinations(link_team, 2)):
        link_team_stat += (stats[fir_person][sec_person] + stats[sec_person][fir_person])


    left+=1
    right -=1
    answer = min(answer, abs(start_team_stat- link_team_stat))

print(answer)

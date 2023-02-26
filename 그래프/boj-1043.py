import sys
input = sys.stdin.readline

# DFS 활용 버전
# 속도 : 44ms 
N, M = map(int, input().split())
known_info = list(map(int, input().split()))
known_people_cnt = known_info[0]
known_people = known_info[1:]

graph = [[ ] for _ in range(N+1)]
party_infos = []
is_known_person = [False] * (N+1)

for _ in range(M):
    party_info = list(map(int, input().split()))
    party_infos.append(party_info)
    party_participant_cnt = party_info[0]
    party_participants = party_info[1:]
    for i in range(party_participant_cnt):
        for j in range(party_participant_cnt):
            if i == j: continue
            graph[party_participants[i]].append(party_participants[j])

def check_people_may_know(cur_person):
    
    if is_known_person[cur_person]:
        return
    
    is_known_person[cur_person] = True
    for next_person in graph[cur_person]:
        if not is_known_person[next_person]:
            check_people_may_know(next_person)

for known_person in known_people:
    check_people_may_know(known_person)

cnt = 0
for party_info in party_infos:
    party_participant_cnt = party_info[0]
    party_participants = party_info[1:]

    for i in range(party_participant_cnt):
        if is_known_person[party_participants[i]]:
            break
    else:
        cnt+=1

print(cnt)


# 집합을 이용한 풀이
# 40ms
N, M = map(int, input().split())
known_people = set(map(int, input().split()[1:]))
party_infos = [set(map(int, input().split()[1:])) for _ in range(M)]

for _ in range(M):
    for party_info in party_infos:
        if party_info & known_people:
            known_people = known_people.union(party_info)

cnt = 0
for party_info in party_infos:
    if party_info & known_people: continue
    cnt+=1

print(cnt)
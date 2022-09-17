import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_seen_heard_map = {}

for _ in range(N):
    not_seen_heard_map[input().rstrip()] = 1
    
for _ in range(M):
    not_heard_person = input().rstrip()
    if not_heard_person in not_seen_heard_map:
        not_seen_heard_map[not_heard_person] += 1
    else: not_seen_heard_map[not_heard_person] = 1

not_seen_heard_people = sorted(list(filter(lambda x: not_seen_heard_map[x] > 1, not_seen_heard_map.keys())))

print(len(not_seen_heard_people))
for not_seen_heard_person in not_seen_heard_people:
    print(not_seen_heard_person)
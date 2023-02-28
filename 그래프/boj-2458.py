import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
forword_graph = [[ ] for _ in range(N+1)]
backword_graph = [[ ] for _ in range(N+1)]

for _ in range(M):
    tall, small = map(int, input().rstrip().split())
    forword_graph[tall].append(small)
    backword_graph[small].append(tall)


def get_smaller_people(cur_person, depth):
    if visited[cur_person] == True:
        return

    visited[cur_person] = True
    
    for next_person in forword_graph[cur_person]:
        get_smaller_people(next_person, depth+1)

def get_taller_people(cur_person, depth):
    if visited[cur_person] == True:
        return

    visited[cur_person] = True
    
    for next_person in backword_graph[cur_person]:
        get_taller_people(next_person, depth+1)


cnt = 0
for i in range(1, N+1):
    answer = 0
    visited = [False] * (N+1)
    get_smaller_people(i, 0)
    answer += sum(visited)
    visited = [False] * (N+1)
    get_taller_people(i, 0)
    answer += sum(visited)

    if answer > N:
        cnt+=1

print(cnt)
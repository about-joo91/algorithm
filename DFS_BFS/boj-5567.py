from collections import deque
N = int(input())
M = int(input())

friend_graph = [[ ] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    person, friend = map(int, input().split())
    
    friend_graph[person].append(friend)
    friend_graph[friend].append(person)
    
friend_queue = deque()
friend_queue.append((1, 0))
visited[1] = 1
answer = 0

while friend_queue:
    friend_node, distance = friend_queue.popleft()
    
    if 0 < distance <= 2:
        answer +=1
    
    for next_node in friend_graph[friend_node]:
        if visited[next_node] == 0:
            visited[next_node]= 1
            friend_queue.append((next_node, distance+1))
            
print(answer)
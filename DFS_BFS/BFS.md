### 개념

다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘

### 예시

1. 시작하는 칸을 큐에 넣고 방문했다는 표시를 남김
2. 큐에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
3. 해당 칸을 이전에 방문했다면 아무것도 하지 않고 처음으로 방문했다면 방문했다는 표시를 남기고 해당칸을 큐에 삽입
4. 큐가 빌 때까지 2번을 반복

모든 칸이 큐에 1번씩 들어가므로 시간복잡도는 칸이 N개일 때 O(N)

어느정도 정석적인 구현이 있다. 그 구현을 거의 외우다시피 해도 괜찮다.

### 자주 실수 하는 것들

1. 시작점에 방문했다는 표시를 남기지 않는다.
2. 큐에 넣을 때 방문했다는 표시를 하는 대신 큐에서 빼낼 때 방문했다는 표시를 남긴다.
3. 이웃한 원소가 범위를 벗어났는지에 대한 체크를 잘못했다.

### 연습문제

boj-1926

방문했던 칸을 제외하고 순회하기 때문에 전체 O(NM)의 시간복잡도로 구현이 가능하다.

pop을 해줄 때 마다 사이즈를 증가 시키면서 사이즈의 값도 같이 구해줄 수 있다

BFS과정을 잘 이해하고 있다면 이 정도 응용은 따라가는데 큰 무리가 없을 것

```python
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
sizes= []

def count_paints_size(row: int,col: int) -> bool:
    queue = deque([(row, col)])
    visited[row][col] = 1

    size = 0

    while queue:
        cur_row, cur_col = queue.popleft()
        size +=1

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if 0 <= next_row < N and 0<= next_col < M and graph[next_row][next_col] == 1 and visited[next_row][next_col] == 0:

                visited[next_row][next_col] = 1

                queue.append((next_row, next_col))

    sizes.append(size)
    return True

cnt = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] == 1:
            if count_paints_size(i,j):
                cnt+=1

if cnt:
    print(cnt)
    print(max(sizes))
else:
    print(0)
    print(0)
```

boj-2178

내가 직접 푼 문제 아래와 같이 visited를 사용해서 거리값을 구할수도 있겠지만

```python
from collections import deque

N, M = map(int, input().split())
map_of_maze = [list(map(int, input())) for _ in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[0] * M for _ in range(N)]

def can_move(row, col):
    if 0<= row < N and 0 <= col < M and visited[row][col] == 0:
        if map_of_maze[row][col] == 1:
            return True
    return False

def get_length_of_path(row, col, distance):
    possible_ways = deque([(row, col, distance)])

    while possible_ways:
        cur_row, cur_col, cur_distance = possible_ways.popleft()

        if cur_row == N-1 and cur_col == M-1:
            return cur_distance

        for direction in directions:

            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if can_move(next_row, next_col):
                visited[next_row][next_col] = 1
                possible_ways.append((next_row, next_col, cur_distance +1))

print(get_length_of_path(0, 0, 1))
```

바킹독님은 아래와 같이 distances 리스트를 통해서 거리를 구함과 동시에 방문처리까지 했다.

```python
from collections import deque

N, M = map(int, input().split())
map_of_maze = [list(map(int, input())) for _ in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
distances = [[-1] * M for _ in range(N)]

def can_move(row, col):
    if 0<= row < N and 0 <= col < M and map_of_maze[row][col] == 1:
        if distances[row][col] < 0:
            return True
    return False

def count_length_of_path(row, col):
    possible_ways = deque([(row, col)])
    distances[row][col] = 0
    while possible_ways:
        cur_row, cur_col = possible_ways.popleft()

        for direction in directions:

            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if can_move(next_row, next_col):
                visited[next_row][next_col] = 1
                possible_ways.append((next_row, next_col))
                distances[next_row][next_col] = distances[cur_row][cur_col] +1

count_length_of_path(0, 0)

print(distances[N-1][M-1] +1)
```

boj-7576

익은 토마토의 갯수가 여러개일 수 있다. 익은 토마토들에 대해 해당위치를 시작점으로 하는 bfs를 각각 돌릴 수 잇겠지만 그렇게 되면 토마토의 갯수는 최대 NM개 일 수 있고 순회를 다 돌면 O(N**2M**2)의 시간복잡도를 가질 수도 있기 때문에 각 토마토들을 미리 뽑아서 bfs를 순회해주면 간단하게 해결될 수 있다.

```python
import sys
from collections import deque

def count_day_of_done():
    while queue:
        cur_row, cur_col = queue.popleft()

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if 0 <= next_row < N and 0 <= next_col < M and distances[next_row][next_col] < 0:
                distances[next_row][next_col] = distances[cur_row][cur_col] + 1
                queue.append((next_row, next_col))

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
distances = [[0] * M for _ in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))
        if tomatoes[i][j] == 0:
            distances[i][j] = -1

count_day_of_done()
answer = 0
for i in range(N):
    for j in range(M):
        if distances[i][j] == -1:
            print(-1)
            sys.exit(0)
        answer = max(answer, distances[i][j])

print(answer)
```

3차원 문제인 boj - 7569

```python
from collections import deque
import sys
input = sys.stdin.readline

N , M = map(int, input().split())
visited = [[0] * N for _ in range(M)]
tomato_box = [list(map(int, input().split())) for _ in range(M)]
queue = deque()
directions = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs():
    day = 0
    while queue:
        cur_row, cur_col, day = queue.popleft()
        visited[cur_row][cur_col] = 1
        for direc in directions:
            next_row = cur_row + direc[0]
            next_col = cur_col + direc[1]
            if 0 <= next_row < M and 0<= next_col < N and visited[next_row][next_col] == 0:
                if tomato_box[next_row][next_col] == 0:
                    tomato_box[next_row][next_col] = 1
                    queue.append((next_row, next_col, day+1))
    return day

for i in range(M):
    for j in range(N):
        if tomato_box[i][j] == 1:
            queue.append((i, j, 0))

day = bfs()

for i in range(M):
    if 0 in tomato_box[i]:
        print(-1)
        break
else: print(day)
```
